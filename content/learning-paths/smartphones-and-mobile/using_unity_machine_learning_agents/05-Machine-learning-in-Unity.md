---
title: Machine Learning in Unity
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview of machine learning

One way to implement a machine learning system is using "Neural Networks". This is the method enabled by Unity ML Agents.

In this method, we train a neural network model (a "brain") that takes inputs (observations), processes them, and produces outputs (decisions). These outputs drive the actions of the AI characters in our game.

Neural networks are a vast and complex subject. To simplify, they contain inputs (input nodes), outputs (output nodes), and internal nodes that process the input values. Input values get modified as they pass through the internal nodes to reach the output nodes.

Internal nodes have "weights" which are numerical parameters that affect a node's output to subsequent nodes. We train a neural network model by feeding sample input values, inspecting the output values, and comparing the output to expected values over many iterations. We change these node weights until satisfied with the results.

Neural networks with more than one layer of internal nodes are called _Multilayer Perceptrons_ (MLPs).

In a game, the outputs of such a model directly control an AI character's actions, which affect the data for each training iteration. It can take thousands of iterations before results are satisfactory and usable in a real game.

This computationally intensive process runs during the training stage only. We prepare the data (the model) before building and deploying the game. The training produces the model in the form of a data file that we embed in the game, loaded at runtime into our game's ML subsystem.

The goal of training is a network that produces desirable outputs (sensible decisions leading to sensible actions) from sensible inputs (observations).

As you can imagine, training the model becomes a separate new build step before bundling and deploying the game. Carefully choosing observations and actions is key to AI quality.

![Neural network](images/mlp-network.png "Figure 1. Neural network diagram")

## What is Unity ML Agents toolkit?

The Unity ML Agents toolkit is an open source machine learning framework created and released by Unity Software Inc.

Written in C# and Python, it contains APIs and tools for training AI "Agents". On the Unity side, we have _Agents_ we train that provide observations and actions. The _Agents_ connect to the Python framework (_mlagents-learn_ program) which provides algorithms for "Reinforcement Learning".

The training step produces a data file which would be our pre-trained model. This model is then embedded into our game and used at runtime to act as "the brain" of our AI character (the _Agent_).

## Dr Arm and Reinforcement Learning

Reinforcement learning is an the type of machine learning where an "agent" is trained with the goal of maximizing some reward and/or minimizing some punishment.

Rewards and punishments are scores (floating point numbers). Inputs are "observations" of the environment and opponent (also as floating point numbers).

### Our reward function

The reward tells the character if actions succeeded (positive) or failed (negative). This allows characters to learn to do the right thing - in our case, quick victories.

We reward 1 for winning and -1 for losing. A small negative reward over time reduces the reward for slower wins. This will incentivize quick wins during training iterations.

### The inputs

There are a number of inputs that we will use - each input is in the form of a floating point number. Our inputs include:

* Health, stamina and mana level of both characters
* Is character rolling?
* Is the enemy rolling?
* Is the enemy facing the character?

### The outputs

The outputs from the neural network model directly translate to actions the character can perform. There are 3 outputs in total:

* Floating point (-1, 1) used as joystick input X
* Floating point (-1, 1) used as joystick input Y
* Integer that will decide whether character should attack, roll or use fire attack.

### Unity training scene

We have a dedicated scene that runs 6 battles simultaneously. Both characters are AI. This reduces training time.

## How does the training work?

First off, projects need to implement all the necessary hooks for Unity ML Agents to function. We have scripts for our "intelligent" characters that derive from the _Agent_ class and call the necessary ML-related functions at the correct times:

1. Setup training limits such as maximum simulation steps (so we don't allow a battle to go on forever)
1. Send observations (inputs) to the agent
1. Receive outputs from the agent (in the form of buffers of numbers)
1. Character performs actions based on the output from the agent
1. Send reward (positive or negative) to the agent

Training with Unity ML Agents toolkit leverages the Unity project itself in the training. Here is a quick overview of the steps:

1. Open your training scene in Unity
1. Run the _mlagents-learn_ python process
1. Launch your game in the Unity editor (if you wait too long the connection may fail)
1. ML Agents Toolkit will automatically connect and run the simulation
1. You can monitor the training by using TensorBoard (described later)

Training neural networks is computationally intensive and can take a long time (hours to potentially days), but can leverage GPU computing to reduce the time it takes.

It is worth mentioning that the time it takes to train a neural network is different to the runtime performance of using a pre-trained ML model. Runtime performance is crucial for end users who will be playing the game. We have found Unity ML Agents runs very well on Arm devices.

In the next section we'll go through the main Dr Arm scene and some of the key objects and ML components.
