---
title: Acceleration Structure
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Acceleration Structure

Acceleration structure is a data structure for improving the ray traversal speed on ray tracing hardware. Acceleration structure use a hierarchical tree to store the geometry data of the scene in order to minimize the hit test of ray and geometry. Ray tracing hardware usually uses this structure to quickly find the triangles which have hit with a ray.

As the Figure 1 shows, the scene will be split to several smaller volumes and the acceleration structure store the hierarchical tree of all small volumes. When doing a ray traversal, hardware can use this structure to quickly find the volumes which have hit with a ray. Then the hardware can find the intersections of ray and triangles inside those volumes.

![](images/as2.png "Figure1. The acceleration structure used to present a scene.")



Usually there will be many duplicated objects in a regular game scene, these objects share the same geometry data but have some different instance attributes like position or color. So acceleration structure has 2 levels. Top Level Acceleration Structure (TLAS) and Bottom Level Acceleration Structure (BLAS) as Figure 2 shows. 

![](images/as.png "Figure2. The acceleration structure tree.")

### TLAS 
TLAS only stores instancing data of BLAS, for example, transform data of each instance. TLAS doesn't store any geometry data, it only store which BLAS is related. By this way, the hardware can save memory usage by just storing one geometry data for many duplicated objects.


### BLAS
BLAS stores the geometry data and Hierarchical bounding volumes of the scene. Multiple instances at TLAS can point to the one BLAS.




