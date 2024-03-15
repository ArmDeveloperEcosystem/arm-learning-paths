---
title: Inside the code
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

For the purpose of demonstrating the tools introduced in this learning path, we are going to take advantage of the three different modes that are available in the sample code.

Each of the three modes represent the different levels of optimizations that are already implemented in the code.

- Plain mode runs the unoptimized code

- Burst mode uses code that has been tagged for use with [the Burst compiler](https://docs.unity3d.com/Manual/com.unity.burst.html). The code has been modified with Burst in mind to make full use of auto-vectorization

- Neon mode is the most optimized mode. This uses code that contains hand-written [Arm Neon intrinsics](https://www.arm.com/technologies/neon) to get even more performance in addition to the Burst compiler.

Our aim here is to measure and see the difference between these different modes.

The next learning path [Using Neon intrinsics to optimize Unity on Android](/learning-paths/smartphones-and-mobile/using-neon-intrinsics-to-optimize-unity-on-android) in this series will go through how the above optimizations were implemented and why.

## Overview of the scene and the code
The environment is split into four separate areas. Each set of walls is parented to a single object. The areas are called walls, walls (1), walls (2) and walls (3). This keeps the hierarchy of the scene simple to manage. Each wall is an instance of a prefab called Wall in Assets/BurstNeonCollisions/Scenes.

The custom component CollisionCalculationScript is the main game component and controls which mode to run. Each mode has a different set of functions.There is one instance of this component. It is attached to the game object called ScriptHolder.

The ground is a simple plane mesh on an object called Ground and the Canvas contains a simple UI that displays some information at runtime.

## Switch to plain (unoptimized) mode
The sample project provides ready-to-go optimizations using Burst and Neon. Ignore Burst and Neon for now. Enable the unoptimized version by editing the script CollisionCalculationScript.cs

In _Assets/BurstNeonCollisions/CollisionCalculationScript.cs_. Edit line 66 to set _codeMode_ to _Mode.Plain_

```
public const Mode codeMode = Mode.Plain;
```
