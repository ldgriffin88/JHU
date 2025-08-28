import numpy as np
from grid import Grid
from agent import Agent
import matplotlib
matplotlib.use("Qt5Agg") 
import matplotlib.pyplot as plt
import pygame

"""
This file trains an agent to pick up an object and place it in the correct container. The object can be one of 4 different objects and the containers are located at the corners of the grid. In this file, the grid is 5x5. The agent starts in the middle of the grid and the object spawns randomly each episode, but cannot appear in the middle or in one of the containers to start. 

There are 4 sequential sections of this file. 
1) Training Loop
2) Plot Generation
    - average number of steps per episode
    - average reward per episode
3) Success Rate Testing on 100 episodes
4) Simulation of 10 episodes using pygame for visualization

Notes:
- The file will continue execution after each figure window is closed. The figure windows must be closed in order to reach the simulation.

Sources:

https://www.geeksforgeeks.org/python/pygame-tutorial/

https://www.pygame.org/docs/
"""


"""
Section 1: Training Loop

"""
# training parameters
episodes = 2000
steps = 100
seed = 1

# instantiate grid
env = Grid()
obs, info = env.reset(seed = seed)

# instantiate agent with tuning parameters
agent = Agent(
    env = env,
    learning_rate = 0.1,
    initial_epsilon = 1,
    epsilon_decay = 0.995,
    final_epsilon = 0.05,
    discount_factor = 0.99,
)

# to track steps and rewards per episode
steps_training = []
ep_rewards = []

# run each episode
for ep in range(episodes):

    # reset environment
    obs, info = env.reset()
    episode_reward = 0

    # run steps for each episode
    for step in range(steps):

        # get action, update env, update Q table, reset obs
        action = agent.get_action(obs)
        next_obs, reward, terminated, truncated, info = env.step(action)
        agent.update(obs, action, reward, terminated, next_obs)
        obs = next_obs

        # to plot reward per episode
        episode_reward += reward

        # when object is dropped
        if terminated or truncated:
            steps_training.append(step + 1)
            ep_rewards.append(episode_reward)
            break

    # if loop didnt break
    else:
        steps_training.append(steps)
        ep_rewards.append(episode_reward)

    # lower epsilon
    agent.decay_epsilon()


"""
Section 2: Plot Generation

"""
# plotting results
k = 10  
N = len(ep_rewards)

starts = np.arange(0, N, k)
x = np.minimum(starts + k, N)

# calculate means
steps_mean   = [np.mean(steps_training[s: min(s+k, N)]) for s in starts]
returns_mean = [np.mean(ep_rewards[s:  min(s+k, N)]) for s in starts]

plt.figure()
plt.plot(x, steps_mean, marker='.', linestyle='', label='avg steps / 25 eps')
plt.xlabel('Episode')
plt.ylabel('Steps')
plt.title('Steps')
plt.grid(alpha=0.2); plt.legend()
plt.show()

plt.figure()
plt.plot(x, returns_mean, marker='.', linestyle='', label='avg return / 25 eps')
plt.xlabel('Episode')
plt.ylabel('Rewards')
plt.title('Rewards')
plt.grid(alpha=0.2); plt.legend()
plt.show()


"""
Section 3: Success Rate Testing on 100 Episodes (after training)
"""
print("\nStarting Testing")

# parameters
test_episodes = 100
test_max_steps = 50
agent.epsilon = 0
successes = 0
steps = []

# for all eposides
for e in range(test_episodes):

    # reset environment
    obs, info = env.reset()

    # over all steps
    for s in range(test_max_steps):

        # get action, iterate environment, get next observation
        action = agent.get_action(obs)
        next_obs, reward, terminated, truncated, info = env.step(action)
        obs = next_obs

        # add success if terminated and reward is positive
        if terminated:
            if reward > 0: 
                successes += 1
                steps.append(s + 1)
            break

success_rate = successes / test_episodes
print(f"Success Rate of testing on 100 episodes after training: ", success_rate)


"""
Section 4: Simulation over 10 Episodes

"""
# set parameters
pygame.init()
n = int(env.size)
FPS = 2
W = H = 100 * n
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 18)

# rgb colors
background = (28, 28, 28)
grid = (245, 245, 245)
agent_color = (245, 245, 245)
containers = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
]

def draw(obs, step = None, reward = None):
    """
    Function to draw the simualtion window each time step
    """
    # background color
    screen.fill(background)

    # draw grid lines
    for i in range(n+1):
        pygame.draw.line(screen, grid, (0, i*100), (W, i*100))
        pygame.draw.line(screen, grid, (i*100, 0), (i*100, H))

    # draw containers
    for i, c in enumerate(np.asarray(env.container_locations, dtype=int)):
        cx = int(c[0])
        cy = int(c[1])

        pygame.draw.rect(screen, containers[i], pygame.Rect(cx*100, cy*100, 100, 100))

    # get object coordinates and draw
    ox = int(obs["obj"][0])
    oy = int(obs["obj"][1])
    obj_color = containers[int(obs["obj_id"])]
    center_obj = (ox * 100 + 100 // 2, oy * 100 + 100 // 2)
    radius_obj = int(.4 * 100)
    pygame.draw.circle(screen, obj_color, center_obj, radius_obj)
    pygame.draw.circle(screen, (20, 20, 20), center_obj, radius_obj, width=2)

    # get agent coordinates and draw
    ax = int(obs["agent"][0])
    ay = int(obs["agent"][1])
    center = center = (ax * 100 + 100 // 2, ay * 100 + 100 // 2)
    radius = int(.3 * 100)
    pygame.draw.circle(screen, agent_color, center, radius)

    # render
    pygame.display.flip()    


# for 10 episodes
for ep in range(10):

    # reset env
    obs, info = env.reset()
    running = True
    last_reward = 0

    # for allowable steps
    for step in range(test_max_steps):

        # option to close
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                running = False

        if not running: 
            break

        # call to draw function
        draw(obs, step = step, reward = last_reward)

        # get action, iterate environment, get new observation
        action = agent.get_action(obs)
        next_obs, reward, terminated, truncated, info = env.step(action)
        obs = next_obs
        last_reward += reward 

        # move clock
        clock.tick(FPS)

        # delay closing or next episode
        if terminated:
            draw(obs, step = step + 1, reward = reward)
            pygame.time.wait(2000)
            break

# close
pygame.quit()