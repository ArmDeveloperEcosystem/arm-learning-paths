---
title: Optimize acceleration structure
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

To get the best ray transversal performance, you need to reduce the overlap of meshes as much as possible. The overlap increases the cost of ray traversal because the hardware needs to check more meshes which may never have a hit.

You can use the `Instance Overlap` view under `Ray Tracing Debug` to check the overlap of your level. 

![Instance Overlap #center](images/instance-overlap.png)

The color of the view represents the degree of overlap. The more yellow the color, the more overlap there is. 

You can see there is a big yellow area in the middle of the screen which indicates significant overlap. This is caused by the mesh which combines all 4 pillars of the boxing ring and covers the empty area within the ropes.

![Overlap #center](images/before_opt.png)

To reorganize the scene objects, split the pillars to 4 meshes. 

As you can see from the new image, the yellow area has been eliminated and there is less overlap in the scene.

![New overlap #center](images/after_opt.png)
