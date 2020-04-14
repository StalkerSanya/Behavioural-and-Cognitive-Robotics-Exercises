# Behavioural-and-Cognitive-Robotics-Exercises
## Exercise 1
- location of python code: /exercize_1

   I runned 2 environment "CartPole-vO" and "Pendulum-v0" and studied parameters of env.observation and env.action. For example, for env.action of "CartPole-vO" we have two discrete actions and for env.action of "Pendulum-v0" we have one continuous action.

## Exercise 2
- location of python code: /exercize_2

  For "CartPole-vO" my script slove problem, such as give me 5 best neuron nets with max reward(I cheked), but in case  "Pendulum-v0" script doesn't solve problem, I think in this case we need more episodes, generations and max steps for 1 episode or possibly also need to increase number of hidden layers of neurons, because 5 is too small.

## Exercise 3 
For "Acrobot-v1" I train neuron net for different seeds. For different seeds we obtain similar results which give us the best fitness near -60. Also training neuron net doesn't solve problem, maybe we need more ntrains.

## Exercise 4
In this exercise I evolve the robots(cases: hopper and halfcheetah) with original reward function and modified reward function.
The original function has: 
* progress - it's the movement of the robot to the target. 
* alive - check robot fall or not.
* electricity_cost -  cost using robot's motors.
* joints_at_limit_cost - it's a penalty due to stucking joints of the robot. 
* feet_collision_cost - it's a penalty for avoiding collisions, for example, touching legs to each other.

The modified function has simalar parts but has some changes: 
* progress - it's the movement of the robot to the target, but normolize between[-1,1]
* alive - give bonus when robot avoid falling down
* feet_cost - check if both of the feet on the ground or not and gives penalty -0.33 if both feet on the ground, -1.0 if both feet not on the ground.
* angle_offset_cost - it's the penalty for difference angle between the robot and the target.

How I can see with modified function robot can move to target, but in case original function robot doesn't move, he only hold his state in equilibrium. Why it happens, Modified function is adapted to fit evolutionary strategies, where we have population agents, so choose best. But Original function is suitable for reinforcement learning which work with one agent. 

## Exercise 5 
I found out how to create own enviroment class with robot described by urdf file. Also I tried to train robot and watched behaviour of the robot. It was very intresting, and It became more clear.

But at first evolving a have problem when launched evolved robot by comand:
``` 
python3 ../../bin/es.py -f balance.ini -t bestg(NUMBER).npy
```
which gives mistake like "pybullet.error: Joint index out-of-range."

But I could escape mistake by changing line in ```balancebot_env.py``` file:

```
self.physicsClient = p.connect(p.GUI)
``` 
and changing render function on:
```
def render(self, mode='human', close=False):
    pass
```

Files with result in folder /exercise 5/balancebot_result 

## Exersise 6
In this exersice I did 1-10 replications of the experiment with the LSTM architecture by using different seeds (1-10). Also I did 2 replications by using a feed-forward neural architecture with seed(11-12).

So I noticed 4 different behaviors of the robot:
* 1) for seeds: 1, 2, 4, 8, 10 robot moves clockwise and achieve target with fluctuation near of traget.
* 2) for seeds: 5, 7, 9 robot moves counterclockwise and achieve target with fluctuation near of traget.
* 3) for seed: 2 robot moves counterclockwise and achieve target with movement around target cylinder in the same direction.
* 4) for seed: 6 robot moves clockwise and in almost all cases doesn't achieve target. If robot achieve, it moves around target cylinder in another same direction.

For evolved case without memory robot also achieve target and fluctuate or moves around traget.
Difference between train robot with memory and without is in strategy of evalution. So in case without memory robot can learn another features of evironment which allow him to solve his task, to be more adapted.

