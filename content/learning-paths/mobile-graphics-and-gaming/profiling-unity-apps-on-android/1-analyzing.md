---
title: Analyzing the sample application
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

This learning path will guide you through your first steps in analyzing the performance of a sample application on an Android device.

The sample project has been written in Unity and is freely available on the Unity Asset Store. You will build and deploy the application to your Android device.

We have covered building and deploying Unity applications for profiling on Android devices in the learning path [Get started with Unity on Android](/learning-paths/mobile-graphics-and-gaming/get-started-with-unity-on-android).

You will use the Profiler and Analyzer tools to collect and analyze performance data. While the Profiler is focused more on examining specific frames, the Analyzer allows developers to compare frames over time or between two different captures (for example, before and after a change to the code).

You will need to log in to your Unity account in order to download and import the sample project.

## The sample code

The sample code implements collision detection and response between many objects. This is a use case which can be implemented with well-optimized or un-optimized code, making it suitable for this learning path.

An increasing number of characters (actually just simple capsules) are spawned over time. Characters start walking in a random direction. They will change direction upon collision with a static wall or another character.

The walls are visually represented by simple boxes. The bounds of the walls are stored as Axis-Aligned Bounding Boxes (AABB).

The characters are presented as simple capsules and their bounds are stored as a radius value in a static array, and as AABBs that are updated every frame.

Character-to-wall collisions are detected by checking for overlapping AABBs. Character-to-character collisions are detected by checking overlapping circles where each circle is made from the position and radius of a character.

![Collision detection diagram#center](images/collision-detection.png "Figure 1. Character-wall collision detection using AABBs (left) and character-character collision detection (right) using position and radius (R).")
