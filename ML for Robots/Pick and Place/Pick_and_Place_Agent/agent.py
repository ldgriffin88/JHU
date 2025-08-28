from collections import defaultdict
import gymnasium as gym
import numpy as np

"""
This file defines a Q-Learning Agent class using gymnasium.

Sources:
https://gymnasium.farama.org/introduction/create_custom_env/

https://medium.com/@ym1942/create-a-gymnasium-custom-environment-part-1-04ccc280eea9

https://gymnasium.farama.org/tutorials/gymnasium_basics/environment_creation/

https://gymnasium.farama.org/introduction/train_agent/
"""

class Agent:
    def __init__(
        self,
        env: gym.Env,
        learning_rate: float,
        initial_epsilon: float,
        epsilon_decay: float,
        final_epsilon: float,
        discount_factor: float,
    ):
        """
        Initialize a Q-Learning agent.

        Args:
            env: The training environment
            learning_rate: How quickly to update Q-values (0-1)
            initial_epsilon: Starting exploration rate (usually 1.0)
            epsilon_decay: How much to reduce epsilon each episode
            final_epsilon: Minimum exploration rate (usually 0.1)
            discount_factor: How much to value future rewards (0-1)
        """
        self.env = env

        # q-table: maps (state, action) to expected reward
        self.q_values = defaultdict(lambda: np.zeros(env.action_space.n))
        self.lr = learning_rate
        self.discount_factor = discount_factor  

        # exploration parameters
        self.epsilon = initial_epsilon
        self.epsilon_decay = epsilon_decay
        self.final_epsilon = final_epsilon


    def _key(self, obs):
        """
        Unpack Observation
        """

        ax = int(obs["agent"][0])
        ay = int(obs["agent"][1])
        ox = int(obs["obj"][0])
        oy = int(obs["obj"][1])
        k = int(obs["obj_id"])
        g = int(obs["grip"])

        return (ax, ay, ox, oy, k, g)


    def get_action(self, obs) -> int:
        """
        Choose an action using epsilon-greedy strategy.

        Returns:
            action: 0 (right)
                    1 (up)
                    2 (left)
                    3 (down)
                    4 (gripper toggle)
        """
        # get the mask from the observation
        mask = np.asarray(obs["mask"], dtype=bool)

        # get whatever choices are valid from mask
        choices = np.flatnonzero(mask)

        # exploration probability
        if np.random.random() < self.epsilon:
            return int(np.random.choice(choices))

        # with probability (1-epsilon): exploit (best known action)
        else:
            s = self._key(obs)
            q = self.q_values[s]

            # flip illegal values and give them very negatvie value
            # for when no options are best
            q[~mask] = -1e9  
            best = np.flatnonzero(q == q.max())
            return int(np.random.choice(best))


    def update(
        self,
        obs,
        action: int,
        reward: float,
        terminated: bool,
        next_obs,
    ):
        """
        Update Q-value
        """

        # hash observation and next observation
        s = self._key(obs)
        next_s = self._key(next_obs)

        # if dropped object, no future reward
        if terminated:
            future_q_value = 0
        else:

            mask = next_obs.get("mask")
            m = np.asarray(mask, dtype=bool)
            if m.any():
                q_next = self.q_values[next_s]
                future_q_value = q_next[m].max()
            else:
                future_q_value = 0

        # q value from bellman equation
        target = reward + self.discount_factor * future_q_value

        # currest estimate error
        temporal_difference = target - self.q_values[s][action]

        # update estimate in the direction of the error
        self.q_values[s][action] = (
            self.q_values[s][action] + self.lr * temporal_difference
        )


    def decay_epsilon(self):
        """
        Reduce exploration rate after each episode
        """
        self.epsilon = max(self.final_epsilon, self.epsilon * self.epsilon_decay)
