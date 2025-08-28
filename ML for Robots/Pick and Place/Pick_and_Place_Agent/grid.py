from typing import Optional
import gymnasium as gym
import numpy as np

"""
This file creates a grid environment using gymnasium.

Sources:
https://gymnasium.farama.org/introduction/create_custom_env/

https://medium.com/@ym1942/create-a-gymnasium-custom-environment-part-1-04ccc280eea9

https://gymnasium.farama.org/tutorials/gymnasium_basics/environment_creation/

Main Functions
- reset() resets the environment to the initial state. required before calling step. Returns the first agent observation for an episode and information.

- step() updates an environment with actions, the next agent observation, the reward for taking that action, if the env is terminated or truncated due to the latest action and information from the environment about the step

"""

class Grid(gym.Env):
 
    def __init__(self, size: int = 5):
        # The size of the square grid (5x5)
        self.size = size
        s = size - 1
        c = self.size // 2

        # initialize positions - will be set randomly in reset()
        # using -1,-1 as "uninitialized" state
        self._agent_location = np.array([c, c], dtype=np.int32)
        self._object_location = np.array([-1, -1], dtype=np.int32)

        # the containers
        self.container_locations = np.array([[0, 0], [0, s], [s, 0], [s, s]], dtype=np.int32)

        # give each container an id
        self.container_ids = np.array([0, 1, 2, 3], dtype=np.int32)

        # number of ids
        self.ids = 4

        # set gripper status, 0 = open and empty, 1 = closed, no obj, 2 = closed with obj
        self.gripper_status = 0

        # define what actions are available (4 directions)
        self.action_space = gym.spaces.Discrete(5)

        # define what the agent can observe
        # dict space gives us structured, human-readable observations
        self.observation_space = gym.spaces.Dict(
            {
                # [x, y] coordinates
                "agent": gym.spaces.Box(0, size - 1, shape=(2,), dtype=int), 
                # [x, y] coordinates  
                "obj": gym.spaces.Box(0, size - 1, shape=(2,), dtype=int),  

                "obj_id": gym.spaces.Discrete(self.ids),
                "grip": gym.spaces.Discrete(3),
                "mask": gym.spaces.MultiBinary(5),
            }
        )

        # map action numbers to actual movements on the grid
        self._action_to_direction = {
            0: np.array([1, 0]),   # Move right (positive x)
            1: np.array([0, 1]),   # Move up (positive y)
            2: np.array([-1, 0]),  # Move left (negative x)
            3: np.array([0, -1]),  # Move down (negative y)
        }


    def _get_obs(self):
        """
        Convert internal state to observation format.

        Returns:
            dict: Observation with agent and target positions
        """
        return {"agent": self._agent_location, "obj": self._object_location, "obj_id": self.object_id, "grip": self.gripper_status, "mask": self.get_legal_actions().astype(np.int8),}
    

    def _get_info(self):
        """
        Compute auxiliary information for debugging.

        Returns:
            dict: Info with distance between agent and target
        """
        return {
            "distance": np.linalg.norm(
                self._agent_location - self._object_location, ord=1
            )
        }
    

    def reset(self, seed: Optional[int] = None):
        """
        Start a new episode.

        Args:
            seed: Random seed for reproducible episodes

        Returns:
            tuple: (observation, info) for the initial state
        """
        # seed the random number generator
        super().reset(seed=seed)

        c = self.size // 2
        self.gripper_status = 0

        # place the effector in middle of grid
        self._agent_location = np.array([c, c], dtype=np.int32)

        # pick object type
        self.object_id = int(self.np_random.integers(0, self.ids))

        # get correct container based on object type
        self.correct_container = self.object_id

        # get correct container location
        self.correct_container_location = self.container_locations[self.object_id]

        s = self.size - 1
        corners_and_middle = {(0,0), (0,s), (s,0), (s,s), (3,3)}

        # randomly place object (not in middle or corners)
        while True:
            temp_start_coord = tuple(self.np_random.integers(0, self.size, size=2))
            if temp_start_coord not in corners_and_middle:
                self._object_location = np.array(temp_start_coord, dtype=np.int32)
                break

        # get first observation
        observation = self._get_obs()
        info = self._get_info()

        return observation, info
    
    def get_legal_actions(self):
        """
        Mask options and return only legal actions.
        - stops agent from moving off grid
        - stops agent from dropping the object randomly
        - ensures agent only toggles gripper when at object or container

        Returns: 
            binary array of length actions
        """
        mask = np.ones(5, dtype=np.int8)

        # get agent location
        ax = int(self._agent_location[0])
        ay = int(self._agent_location[1])

        # if near borders, set illegal movement
        if ax + 1 >= self.size: mask[0] = 0
        if ay + 1 >= self.size: mask[1] = 0
        if ax - 1 < 0: mask[2] = 0
        if ay - 1 < 0: mask[3] = 0

        # if agent is at object or container
        at_obj = np.array_equal(self._agent_location, self._object_location)
        at_container = any(np.array_equal(self._agent_location, c) for c in self.container_locations)
        
        # conditions for picking up or dropping
        can_pick_up = (self.gripper_status == 0) and at_obj
        can_drop = (self.gripper_status == 2) and at_container
        mask[4] = 1 if (can_pick_up or can_drop) else 0

        return mask
    
    def step(self, action):
        """
        Execute one timestep within the environment.

        Args:
            action: The action to take (0-3 for directions, 4 for gripper toggle)

        Returns:
            tuple: (observation, reward, terminated, truncated, info)
        """
        # trim options
        mask = self.get_legal_actions()

        # init reward and status
        reward = 0
        terminated = False

        # if moving in a direction
        if action < 4:
            if mask[action]:
                # map the discrete action (0-3) to a movement direction
                direction = self._action_to_direction[action]
                self._agent_location = self._agent_location + direction
            else:
                reward -= 1
        else:
            if mask[4]:
                # if action is grab object
                if self.gripper_status == 0:
                    self.gripper_status = 2
                    reward += 1
                else: 
                    self.gripper_status = 0
                    if np.array_equal(self.correct_container_location, self._object_location):
                        reward += 1     
                    else: 
                        reward -= 1

                    terminated = True

        # if gripper has the object
        if self.gripper_status == 2:
            self._object_location = self._agent_location.copy()

        truncated = False

        # get next observation
        observation = self._get_obs()
        info = self._get_info()

        return observation, reward, terminated, truncated, info
    
