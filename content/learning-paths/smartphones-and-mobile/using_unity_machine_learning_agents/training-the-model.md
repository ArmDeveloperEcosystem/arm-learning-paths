---
title: Training the Model
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Loading the Training Model Scene
Go to the _Project_ tab (normally bottom left) and navigate to _Assets->#DevSummit2022->Scenes_ and this time double click the _Level_DevSummit2022_Training_ scene to open it.

![Training Scene selection](project-assets-scenes-training.png "Figure 1. Training Scene selection")

Remember to save the original scene! Once the training one is loaded, it should look similar to this:

![Training Scene](training-scene.png "Figure 2. Training Scene")

Notice there are 6 "arenas". You may have to adjust your view in Unity to be able to see all of them.

Six are used here to speed up the training. If you have more CPU power you could use more.

The other thing we are doing is that we speed time up massively. For our scene, normally there's quite a bit of frame time where it's just sitting waiting for the next frame. We don't need that for training. We want to go as fast as possible and we want to get through hundreds of thousands of battles! So we run at a lot more than 60fps.

Now when you do speed it up you have to be very careful. We had a bug where the fireball was moving at real-time speeds and everything else sped up to bullet time. The fireball would appear to go slowly to the fast-moving models who then could easily avoid the fireball during training, but didn't learn about avoiding it during the real battle. So it's a good idea to speed up time during training, but make sure it speeds up for everything or it will learn the wrong thing 😀.

The light has been removed from the individual scenes as we only need one and also only one event system is required. We also removed UI, as that isn't required for training. 

If you select _ML-Player_ you'll notice in the _Inspector_ that the _Is Player_ flag is no longer set, because in training it will not be controlled by a human player. Also in the _ML Player Manager_ we've set _Init on Start_ to true, as it does some extra initialisation. Then under _Agent Settings_ we have to make sure that the _Training_ property is set to true.

Take some time to look through each object in the arena, to see how it differs slightly, to the game scene.

We're now ready to kick off the training.

# Starting the Training
1. Open up a console or terminal window and change directory so you are in the directory where you unzipped the project.

2. Now we will activate the python virtual environment we set up in the **Preparation** section:
 
`.\python-envs\mlagents-r18-env\Scripts\activate`

3. Once inside the python VM, change directory:

`cd Assets\Scripts\MlAgents`

this is where all the required scripts are grouped.

4. Now you should be able to execute the command _mlagents-learn --torch-device cuda:0 .\config\BossBattle.yaml --run-id=firstrun --force_
    * _--torch-device_ is which GPU to use for your training. _cuda:0_ is just the default GPU.
    * _.\config\BossBattle.yaml_ is the script that we will use for training.
    * _--run-id=firstrun_ creates a folder called "firstrun" (use your own name, if you like) to store the results of our training.  
    You can use this run-id to resume training, see below.
    * _--force_ is not strictly necessary, unless you are overwriting a previous run of the same run-id.
    * another option, not used here is _--resume_. This is useful for when you start your training and you either need to stop your computer, or you think you've done enough training but discover you haven't. When you stop the training it saves where it is up to, with a checkpoint and the latest neural network; if you wish to resume, it's then able to continue from there.

5. Once it starts, after a few seconds it will come up with a text Unity logo, that looks similar to this:

![Python-Unity Startup](python-mlagent-unity-startup.png "Figure 1. Python-Unity Startup")

6. Notice at the bottom it tells you to _Start training by pressing the Play button in the Unity Editor_. So switch to the Unity Editor and do just that.

7. Once the Unity Editor starts and the learning begins it will usually switch to the _Game_ tab, which can be a little disorientating as everything is updating as fast as it can and you are using a zoomed-in camera. Switch to the _Scene_ tab to be able to see all 6 agents going through the learning process. It should look similar to this:

![Unity Agents Learning](unity-agents-learning.png "Figure 2. Unity Agents Learning")

8. If we switch back to our console/terminal window, every 5000 steps it will output the state of our learning, similar to this:

![Learning Steps Status](terminal-steps-status.png "Figure 3. Learning Steps Status")
* _Boss Battle_ : The name of the behaviour that is training within our script that we are running.
* _Step_: How many steps/iteration have happened so far.
* _Time Elapsed_: How much time has elapsed since the training began.
* _Mean Reward_: The average reward given in each battle. -1.000 means we're always losing. Usually after 100,000 steps is when the agents starts winning a bit more regularly.
* _ELO_: Is awarded when someone actually wins. ELO (named after Arpad Elo) is a method for calculating the relative skill levels of players in zero-sum games. While the Mean Reward will get stuck around 0 (the other agent's skill increases with ours, meaning we lose about half the time), ELO can increase, giving us a better measure of progress.

## The Training Scripts
Within Visual Studio (or your code editor) open the _BossBattle.yaml_ and _BossBattle_separation.yaml_ files. You'll find both in the _Assets->Scripts->MlAgents->config_ subdirectory.
_BossBattle.yaml_ should looks like this:

![Boss Battle Script](boss-battle-script.png "Figure 4. Boss Battle Script")

This essentially gives both the Player and the NPC the same brain, although each with their own instance of it. 
These are the properties:
* _trainer type:ppo_ : PPO is an ML-Agent algorithm. The name stands for Proximal Policy Optimization. There are quite a number of different algorithms and if you go onto their GitHub you can learn about all the different ones they have. This one works very well for our scenario.
* _hyperparameters_ : Normal machine learning hyperparameters
* _network settings_ : Sets up the actual size of the neural network. Notice it has _num layer: 2_ and _hidden units:128_ . In a more complex scenario you might have 3 layers and 256 hidden units. Refer to Figure 5 below for the MLP (multi-layer perceptron) explanation of the current setup.
    * The 1st layer is all of our observations. Note that we have 3 stacked vectors (for the last 3 frames), as input into the _neural network_.
    * Then in the _neural network_ we have 2 hidden layers, each with 128 units.
    * The NN output layer maps to _Actions_, which in this case is the joystick movements and the ability to dodge-roll, use sword or fireball attack.

![MLP Network](mlp-network.png "Figure 5. MLP Network")

* On line 23 is _keep_checkpoints_ : This is how many checkpoints it should keep saved. If we have more than this it will delete the oldest ones.
* On line 24 is _checkpoint_interval_ : This is the number of battles between checkpoints.
* _max steps_ : Tells the learning to stop after 3,000,000 battles.
* _self play_ (line 28): This is how often it switches between characters and brains
    * _team change_: This value means it will change between characters every 100,000 battles.
    * _swap steps_: This is the number of battles it should perform before creating a new brain for this character.

_BossBattle_separation.yaml_ should looks similar to this:

![Boss Battle Separation Script](boss-battle-separation-script.png "Figure 6. Boss Battle Separation Script")

Within this yaml we have the ability to set-up 2 separate brains. One named _Paladin_ (for the knight) and another named _Vampire_ (for the NPC). Currently they have identical properties, but you could customise each to have slightly different behaviours.

Let's leave that running, as training to a competent level can take from 6 to 8 hours. While that is running we can take a look at Tensorboard.

# Tensorboard
In this section we look at what tensorboard provides us.

1. Open up a console or terminal window and navigate to the directory where you unzipped the project, then:

`cd Assets\Scripts\MlAgents`

2. Launch _tensorboard_ by executing the following command :

`tensorboard --logDir results\firstrun --port 6006 --reload_multiple True`

3. This monitors our Neural Network and calculates how our learning is progressing.

4. Now open up your browser to http://localhost:6006 (the port we passed to the launch command), which should look similar to this:

![Tensorboard UI](tensorboard-ui.png "Figure 7. Tensorboard UI")

5. Some cards to take a note of:
    * _Episode Length_: Initially when no one is winning the episode length is maximum, until someone wins. Then the average slowly comes down. Once they start winning regularly it should come down a lot.
    * _Cumulative Reward_: Starts off being -1, because both sides is losing, but once they start regularly having a winner it will go up rapidly and will eventually settle around zero, as that is where average will tend towards that over time.
    * _ELO_: As mentioned previously this is the score over time, as characters win, giving you an idea of how well your training is going.

**Note:** you can proceed onto the next step if you wish to take a shortcut on your training time.
