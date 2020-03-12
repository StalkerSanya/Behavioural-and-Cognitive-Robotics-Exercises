import gym
import time
import numpy as np
env = gym.make('Pendulum-v0')
pvariance = 0.1
# variance of initial parameters
ppvariance = 0.02
# variance of perturbations
nhiddens = 5
# number of hidden neurons
# the number of inputs and outputs depends on the problem
# we assume that observations consist of vectors of continuous value
# and that actions can be vectors of continuous values or discrete actions
ninputs = env.observation_space.shape[0]
if (isinstance(env.action_space, gym.spaces.box.Box)):
    noutputs = env.action_space.shape[0]
else:
    noutputs = env.action_space.n
# initialize the training parameters randomly by using a gaussian distribution with
# average 0.0 and variance 0.1

#number of neurons
lamda = 10 
W = []
B = []
for _ in range(lamda):
    # biases (thresholds) are initialized to 0.0
    W1 = np.random.randn(nhiddens,ninputs) * pvariance # first layer
    W2 = np.random.randn(noutputs, nhiddens) * pvariance # second layer
    b1 = np.zeros(shape=(nhiddens, 1)) # bias first layer
    b2 = np.zeros(shape=(noutputs, 1)) # bias second layer
    W.append([W1,W2])
    B.append([b1,b2]) 

sigma = ppvariance
n_generation = 100 # number of generation
n_episodes = 100
for g in  range(n_generation):
    rew = []
    for i in range(lamda):
        reward_sum = 0
        for _ in range(n_episodes):
            # for set initional parameters of env
            observation = env.reset()
            for _ in range(100):
                # for draw in localhost
                # time.sleep(0.01)
                # convert the observation array into a matrix with 1 column and ninputs rows
                observation.resize(ninputs,1)
                # compute the netinput of the first layer of neurons
                Z1 = np.dot(W[i][0], observation) + B[i][0]
                # compute the activation of the first layer of neurons with the tanh function
                A1 = np.tanh(Z1)
                # compute the netinput of the second layer of neurons
                Z2 = np.dot(W[i][1], A1) + B[i][1]
                # compute the activation of the second layer of neurons with the tanh function
                A2 = np.tanh(Z2)
                # if actions are discrete we select the action corresponding to the most activated unit
                if (isinstance(env.action_space, gym.spaces.box.Box)):
                    action = A2
                else:
                    action = np.argmax(A2)
                env.render()
                observation, reward, done, info = env.step(action)
                reward_sum = reward_sum + float(reward)
                if done: 
                    break
        fitness = reward_sum/n_episodes
        rew.append(fitness)
    print("Reward of newrons for", g + 1, "generation:", rew)
    ind_neurons = []
    for i in range(int(len(rew)/2)):
        ind = np.argmax(rew)
        rew[ind] = min(rew)
        ind_neurons.append(ind)
    for i in range(int(lamda/2)):
        ind = min(ind_neurons)
        index = np.argmin(ind_neurons)
        ind_neurons[index] = lamda
        W[i] = W[ind]
        B[i] = B[ind]
    for i in range(int(lamda/2)):
        W[i+int(lamda/2)] = [W[i][0]+np.random.normal(0.1)*sigma, W[i][1]+np.random.normal(0.1)*sigma]
        B[i+int(lamda/2)] = [B[i][0]+np.random.normal(0.1)*sigma, B[i][1]+np.random.normal(0.1)*sigma]

      
env.close()