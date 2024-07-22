---
title: Acceleration Structure
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is Acceleration Structure

An acceleration structure is a data structure designed to improve ray traversal speed on ray tracing hardware. It uses a hierarchical tree to store the geometry data of the scene, minimizing the number of hit tests between rays and geometry. Ray tracing hardware typically utilizes this structure to quickly identify the triangles that intersect with a ray.

As shown in Figure 1, the scene is divided into several smaller volumes, and the acceleration structure stores the hierarchical tree of all these smaller volumes. During ray traversal, the hardware can use this structure to quickly locate the volumes that intersect with a ray. Subsequently, the hardware can find the intersections between the ray and the triangles within those volumes.

![](images/as2.png "Figure1. The acceleration structure used to represent a scene.")



In a typical game scene, there are often many duplicated objects that share the same geometry data but have different instance attributes, such as position or color. Therefore, the acceleration structure is divided into two levels: the Top Level Acceleration Structure (TLAS) and the Bottom Level Acceleration Structure (BLAS), as shown in Figure 2.

![](images/as.png "Figure2. The acceleration structure tree.")

### TLAS 
The TLAS stores only the instancing data of the BLAS, such as the transform data of each instance. It does not store any geometry data; instead, it references the relevant BLAS. This approach allows the hardware to save memory by storing a single set of geometry data for many duplicated objects.


### BLAS
The BLAS stores the geometry data and hierarchical bounding volumes of the scene. Multiple instances in the TLAS can point to a single BLAS.




