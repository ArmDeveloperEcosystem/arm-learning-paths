---
title: The project
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

The sample application you will use is from the Unity Asset Store. It is a complete project and is freely available. You will need to log in to your Unity account to download and import it.

## The sample code
The sample code implements collision detection and response between many objects.

This is a use case which can be implemented with well-optimized or unoptimized code, making it suitable for this learning path.

A simple environment is created with many walls and then an increasing number of characters (actually just simple capsules) are spawned over time. The characters walk in random directions. The characters will react to colliding with static walls and other characters. Characters react in such a way as to avoid walking through walls and other characters.

The walls are visually represented by simple boxes. The bounds of the walls are stored as [Axis-Aligned Bounding Boxes (AABB)](https://en.wikipedia.org/wiki/Bounding_volume).

The characters are presented as simple capsules and their bounds are stored as a radius value.

Character-to-wall collisions are detected using radius-AABB checks. Character-to-character collisions are detected using radius checks.

![Collision detection diagram#center](images/collision-detection.png "Figure 1. Collision detection uses functions for checking intersection between radius-AABB (left) and radius-radius (right).")
