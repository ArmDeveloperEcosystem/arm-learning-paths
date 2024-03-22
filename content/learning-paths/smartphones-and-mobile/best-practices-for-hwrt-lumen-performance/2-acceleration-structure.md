---
title: Acceleration Structure
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Acceleration Structure

Acceleration structure is a data structure for improving the ray traversal speed on ray tracing hardware. It uses a hierarchical tree to store the geometry data of the scene, in order to minimize the hit test of ray and geometry. Ray tracing hardware usually uses this structure to quickly find the triangles which have been hit with a ray.

As Figure 1 shows (see below), the scene will be split to several smaller volumes and the acceleration structure stores the hierarchical tree of all of the small volumes. When doing a ray traversal, hardware can use this structure to quickly find the volumes which have been hit with a ray. Then the hardware can find the intersections of ray and triangles inside those volumes.

![](images/as2.png "Figure1. The acceleration structure used to present a scene.")



Usually there will be many duplicated objects in a regular game scene, these objects share the same geometry data but have some different instance attributes, like position or color. So the acceleration structure has 2 levels: Top Level Acceleration Structure (TLAS) and Bottom Level Acceleration Structure (BLAS) as the below figure shows: 

![](images/as.png "Figure2. The acceleration structure tree.")

### Top Level Acceleration Structure (TLAS) 
TLAS only stores instancing data of BLAS, for example, the transform data of each instance. TLAS doesn't store any geometry data, it only stores data which is BLAS-related. In this way, the hardware can save memory usage by just storing one piece of geometry data for many duplicated objects.


### Bottom Level Acceleration Structure (BLAS)
BLAS stores the geometry data and hierarchical bounding volumes of the scene. Multiple instances at TLAS can point to one BLAS.




