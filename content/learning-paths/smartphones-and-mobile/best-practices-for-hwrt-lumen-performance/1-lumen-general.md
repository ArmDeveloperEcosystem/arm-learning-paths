---
title: Lumen General Setting Optimizations
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Lumen General Setting Optimizations
To use Lumen in your game scene, you need to add a _PostProcessVolume_ actor to your scene. Under _PostProcessVolume_ actor, there are a few options you can tweak. During the period of making our Lumen content, "Steel Arms", we found a few recommended values for those options which are suited for Android devices. The following two images show all option values we used in "Steel Arms".

![](images/Garage.png)

![](images/Garage2.png)

We will now discuss the general settings.

## Global Illumination Settings
![](images/gl-setting.png "Figure1. These global illumination parameters are used in our Lumen content - Steel Arms.")

### Lumen Scene Detail:
•	Higher values can make sure that smaller objects also contribute to Lumen lighting but this will increase the GPU cost

### Final Gather Quality:
•	Controls the density of the screen probes but higher values will increase the GPU cost 

•	<font color=#00FF00>**1.0**</font> should reach a good balance between performance and quality for mobile games

### Max Trace Distance:
•	Controls how far the ray tracing will go, keeping it low can decrease the GPU cost

•	Don’t set it bigger than the size of the scene

•	Smaller values can also reduce some ray incoherence

### Scene Capture Cache Resolution Scale:
•	Controls the surface cache resolution, smaller values can save memory

### Lumen Scene Lighting Update Speed:
•	It's possible to keep this low if the lighting changes are slow to save GPU cost

•	<font color=#00FF00>**0.5 ~ 1.0**</font> should reach a good balance between performance and quality for mobile games

### Final Gather Lighting Update Speed:
•	Keep it low if slow lighting propagation is acceptable

•	<font color=#00FF00>**0.5 ~ 1.0**</font> should reach a good balance between performance and quality for mobile games

 
 ## Lumen Reflection Settings:
![](images/reflection-setting.png "Figure 2. These reflection parameters are used in our Lumen content - Steel Arms.")

### Reflection Quality:
•	Controls the reflection tracing quality (basically the resolution of the reflection)

### Ray Lighting Mode:
•	The default mode is `Surface Cache` mode which reuses the surface cache data for reflections 

•	`Hit Lighting` mode is available when using hardware ray tracing, it evaluates direct lighting instead of using the surface cache

•	`Hit Lighting` mode has a higher quality but with a higher GPU cost

•	`Hit Lighting` mode can reflect direct lighting of the skinned mesh which the surface cache mode can't do

•	`Surface cache` mode is recommended for mobile games

### Max Reflection Bounces:
•	Controls the amount of reflection bounces, higher values have a higher GPU cost

•	<font color=#00FF00>**1**</font> is recommended for mobile games

