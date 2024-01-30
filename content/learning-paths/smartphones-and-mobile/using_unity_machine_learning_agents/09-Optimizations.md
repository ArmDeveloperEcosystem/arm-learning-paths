---
title: Optimizations
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Some notes about reducing training time

There are a few things we did to reduce the time it takes to train the ML agents to a reasonable level.

![Training Scene](images/training-scene.png "Figure 1. The Training Scene (again)")

### Multiple simultaneous battles

We employ 6 "arenas" in the training scene (you may have to adjust your view in Unity to be able to see all of them). By running multiple battles simultaneously we are able to speed up the training. If you have more CPU power you could use more.

### Fast forward time

To speed things up even more, we run the game at a much higher speed when training. Rendering still runs at normal speed but we want everything else to update at a much higher frequency. The Unity value _Time.timeScale_ is normally 1.0 which runs the game at real-time. _Time.timeScale_ is set to a higher value in order to speed up the training.

Now when you do speed it up you have to be very careful. We had a bug where the fireball was moving at real-time speeds and everything else sped up to bullet time. The fireball would appear to go slowly to the fast-moving models who then could easily avoid the fireball during training, so didn't learn how to avoid it during battle.

So it is a good idea to speed up time during training, but make sure it speeds up for everything or it will learn the wrong thing 😀.

### Some minor optimizations

The light has been removed from the individual scenes as we only need one and also only one event system is required. We also removed the UI as that isn't required for training.

### Switching the human character to AI

If you select the _ML-Player_ object you'll notice in the _Inspector_ that the _Is Player_ flag is no longer set. During training the character will not be controlled by a human player. Also in the _ML Player Manager_ object we've set _Init on Start_ to true, as it does some extra initialization. Then under _Agent Settings_ we have to make sure that the _Training_ property is set to true.

Take some time to look through each object in the training arena. They differ slightly to those in the game scene that we use when playing the game.

In the next section we will summarize what we have learned and suggest a few ideas for how to improve the Dr Arm project.
