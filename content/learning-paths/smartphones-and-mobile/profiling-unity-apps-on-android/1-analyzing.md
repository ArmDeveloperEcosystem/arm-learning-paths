---
title: Analyzing the sample application
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

This learning path will guide you through your first steps in analyzing the performance of a sample application on an Android device.

The sample project has been written in Unity and is freely available on the Unity Asset Store. You will build and deploy the application to your Android device.

We have covered building and deploying Unity applications for profiling on Android devices in the learning path [Get started with Unity on Android](/learning-paths/smartphones-and-mobile/get-started-with-unity-on-android)

You will then use the Profiler and Analyzer tools to collect and analyze performance data. While the Profiler is focused more on examining specific frames, the Analyzer allows developers to compare frames over time or between two different captures (for example, before and after a change to the code).

The sample application you will use is from the Unity Asset Store. It is a complete project and is freely available. You will need to log in to your Unity account to download and import it.

## The sample code

The sample code implements collision detection and response between many objects. This is a use case which can be implemented with well-optimized or unoptimized code, making it suitable for this learning path.

An increasing number of characters (actually just simple capsules) are spawned over time. Characters start walking in a random direction. They will change direction upon collision with a static wall or other character.

The walls are visually represented by simple boxes. The bounds of the walls are stored as [Axis-Aligned Bounding Boxes (AABB)](https://en.wikipedia.org/wiki/Bounding_volume).

The characters are presented as simple capsules and their bounds are stored as a radius value.

Character-to-wall collisions are detected using radius-AABB checks. Character-to-character collisions are detected using radius checks.

![Collision detection diagram#center](images/collision-detection.png "Figure 1. Collision detection uses functions for checking intersection between radius-AABB (left) and radius-radius (right).")
