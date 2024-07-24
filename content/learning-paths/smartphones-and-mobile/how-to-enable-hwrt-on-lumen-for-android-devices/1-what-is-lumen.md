---
title: What is Lumen
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Lumen is the latest dynamic global illumination solution in the Unreal Engine, which also supports hardware ray tracing. Lighting indoor scenes which rely solely on direct lighting do not produce high-quality rendering results. To achieve superior indoor lighting quality, you also need indirect lighting.

Rendering dynamic indirect lighting used to be computationally expensive, but Lumen introduces a new ray-tracing based solution that allows developers to render both dynamic direct lighting and indirect lighting in real-time.

You can observe the improvements in rendering quality by comparing two images. The first image considers only direct lighting, and details in areas beyond the direct lighting range (such as the background) are not visible.

In contrast, the second image utilizes Lumen lighting, incorporating both direct and indirect lighting. Now, you can discern many details in the background that were previously hidden, as Lumen takes light bounces into account.

![](images/no_lumen.png "Figure 1. The scene without Lumen has only dirct lighting.")

![](images/lumen.png "Figure 2. The scene with Lumen has both direct and indirect lighting.")

Lumen supports both software and hardware ray tracing. Software ray tracing uses a simplified Lumen scene to replace actual geometries in the scene. In contrast, hardware ray tracing uses actual geometries to trace rays, resulting in better lighting quality.
