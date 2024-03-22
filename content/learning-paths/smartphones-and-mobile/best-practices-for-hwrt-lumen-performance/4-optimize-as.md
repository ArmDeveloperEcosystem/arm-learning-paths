---
title: Optimize Acceleration Structure
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Optimize Acceleration Structure

To get the best performance out of ray traversal, you need to reduce the overlap between meshes as much as possible. The overlap increases the cost of ray traversal because the hardware needs to check more meshs which may never be hit with the ray. Therefore, we need to make sure that the bounding box of each actor covers the least amount of empty space.

You can use the `Instance Overlap` view under _Ray Tracing Debug_ of the Unreal editor to check the overlap of your level. 

![](images/instance-overlap.png)


The color of the view shows the degree of overlap. The closer to yellow the color is, the more overlap there is. You can see there is a big yellow area in the middle of the screen which means that there is a lot of overlap there. This is caused by the mesh which combines all 4 pillars of the boxing ring and also covers the empty area over the stage. 

![](images/before_opt.png "Figure 1. Before acceleration structure optimization.")

After reorganizing the scene objects, we split the pillars to 4 meshs. As you can see from the next image, the yellow area has been eliminated and now we have less overlap in the same scene.


![](images/after_opt.png "Figure 2. After acceleration structure optimization.")
