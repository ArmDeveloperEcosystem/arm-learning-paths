---
title: Optimizations
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Some notes about reducing training time

A few things were done to reduce the time it takes to train the ML agents to a reasonable level.

![Training Scene](images/training-scene.png "Figure 1. The Training Scene (again)")

### Multiple simultaneous battles

Six "arenas" are employed in the training scene (you may have to adjust your view in Unity to be able to see all of them). Running multiple battles simultaneously speeds up the training. If you have more CPU power, you could use more.

### Fast forward time

To speed things up even more, the game is run at a much higher speed when training. Rendering still runs at normal speed but everything else should update at a much higher frequency. The Unity value _Time.timeScale_ is normally 1.0 which runs the game at real-time. _Time.timeScale_ is set to a higher value in order to speed up the training.

When you speed it up, be careful to make sure it speeds up for everything equally so that the models learn the correct behaviors.

### Some minor optimizations

The light has been removed from the individual scenes as only one is needed and only one event system is required. The UI has also been removed, as it isn't required for training.

### Switching the human character to AI

If you select the _ML-Player_ object you'll notice in the _Inspector_ that the _Is Player_ flag is no longer set. During training, the character will not be controlled by a human player. Also in the _ML Player Manager_ object _Init on Start_ has been set to true, as it does some extra initialization. Then under _Agent Settings_ the _Training_ property has to be set to true.

Take some time to look through each object in the training arena. They differ slightly to those in the game scene that are used when playing the game.

The next section summarizes what we have learned and suggests a few ideas for how to improve the Dr Arm project.
