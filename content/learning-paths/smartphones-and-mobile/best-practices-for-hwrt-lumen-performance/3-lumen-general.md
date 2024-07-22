---
title: Lumen General Setting Optimizations
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

To use Lumen in your game scene, you can add a **Post Process Volume** actor. Within the details panel of  **Post Process Volume** actor, there are several options you can tweak. During the development of our Lumen content, **“Steel Arms”**, we found a few recommended values for these options that are suitable for Android devices. Figures 1 and 2 show all the option values we used in **“Steel Arms”**.

## Global Illumination Settings
![](images/gl-setting.png "Figure1. These global illumination parameters are used in our Lumen content - Steel Arms.")

### Lumen Scene Detail
•	Higher values ensure smaller objects contribute to Lumen lighting but increase GPU cost.

### Final Gather Quality
•	Controls the density of the screen probes; higher values increase GPU cost.

•	<font color=#00FF00>**1.0**</font> strikes a good balance between performance and quality for mobile games.

### Max Trace Distance
•	Controls how far the ray tracing will go; keeping it small decreases GPU cost.

•	Do not set it larger than the size of the scene.

•	Smaller values can also reduce ray incoherence.

### Scene Capture Cache Resolution Scale
•	Controls the surface cache resolution; smaller values save memory.

### Lumen Scene Lighting Update Speed
•	Can be kept low if lighting changes are slow to save GPU cost.

•	<font color=#00FF00>**0.5 ~ 1.0**</font> strikes a good balance between performance and quality for mobile games.

### Final Gather Lighting Update Speed
•	Can be kept low if slow lighting propagation is acceptable.

•	<font color=#00FF00>**0.5 ~ 1.0**</font>  strikes a good balance between performance and quality for mobile games.
 
 ## Lumen Reflection Settings
![](images/reflection-setting.png "Figure 2. These reflection parameters are used in our Lumen content - Steel Arms.")

### Reflection Quality
•	Controls the reflection tracing quality, essentially the resolution of the reflection.

### Ray Lighting Mode
• The default mode is `Surface Cache`, which reuses surface cache data for reflection.

• `Hit Lighting` mode is available when using hardware ray tracing; it evaluates direct lighting instead of using the surface cache.

• `Hit Lighting` mode offers higher quality but at a higher GPU cost.

• `Hit Lighting` mode can reflect lighting of skinned meshes, which `Surface Cache` mode cannot.

• `Hit Lighting` mode is not supported yet on mobile device.

• `Surface Cache` mode is recommended for mobile games.

### Max Reflection Bounces
• Controls the number of reflection bounces; higher values increase GPU cost.

• <font color=#00FF00>**1**</font> is recommended for mobile games.