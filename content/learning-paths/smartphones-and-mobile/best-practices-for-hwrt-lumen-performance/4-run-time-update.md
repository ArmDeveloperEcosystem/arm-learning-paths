---
title: Reduce acceleration structure runtime cost
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

The acceleration structure of static meshes is built offline and is not updated at runtime. But the acceleration structure of skinned mesh needs to be updated at runtime and incurs update cost. 

To reduce the update cost, you can use a higher Level of Detail (LOD) of a skinned mesh for ray tracing.

![Skin load #center](images/skin-lod.png)

There may be some artifacts if you turn on ray tracing shadow when using higher LOD values for skinned mesh ray tracing. 

The artifact is caused by the difference between the rendering mesh and the ray tracing mesh.

![Skin error #center](images/skin-lod-error.png)

