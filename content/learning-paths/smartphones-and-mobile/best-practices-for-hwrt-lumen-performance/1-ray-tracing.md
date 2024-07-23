---
title: Lumen and Ray Tracing
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In 2023, we developed a demo content to pioneer the new frontier of next-gen graphics technologies of the **Immortalis** GPU via the Unreal Lumen rendering system. If you are not familiar with Lumen and global illumination, please check this [learning path](/learning-paths/smartphones-and-mobile/how-to-enable-hwrt-on-lumen-for-android-devices/) before proceeding.

The demo content was named **Steel Arms**. Created with Unreal Engine 5.3, Steel Arms brings desktop-level Bloom, Motion Blur, and Depth of Field (DOF) effects, alongside Physically Based Rendering (PBR), to smartphones.

The following screenshots are from scenes in Steel Arms, powered by Unreal Lumen. During the development of Steel Arms, we discovered several optimization tips for achieving the best performance with Lumen. This article will start with an introduction to ray tracing and then cover the best practices for hardware ray tracing in Lumen.


![](images/Garage.png)

![](images/Garage2.png)


## What is Ray Tracing
Ray tracing is a rendering technique used in computer graphics to simulate the way light interacts with objects in a scene. Essentially, developers can cast a ray in any direction and find the closest intersection between the ray and scene geometries. Arm has implemented this ray tracing technique in hardware to accelerate the speed of ray traversal since the Immortalis-G715 GPU.

To accelerate the speed of ray traversal, the scene geometry data needs to be organized into a data structure called an **Acceleration Structure**. When finding intersections between rays and scene geometries, the hardware traverses the acceleration structure to quickly locate the intersections. Therefore, the acceleration structure is critical to the performance of hardware ray tracing. The next topic will explain acceleration structures in more detail.