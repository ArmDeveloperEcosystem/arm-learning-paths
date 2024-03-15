---
title: Optimize Lumen general settings
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Below is more information about how to optimize the Lumen general settings.

## Global Illumination Settings

The global illumination parameters used in the example Lumen content "Steel Arms", a demonstration used to test the developer experience for Arm products, are provided below. 

For more information refer to [Arm GPUs built on new 5th Generation GPU architecture to redefine visual computing](https://community.arm.com/arm-community-blogs/b/announcements/posts/arm-gpus-built-on-new-fifth-gen-architecture).

![Global settings #center](images/gl-setting.png)

### Lumen Scene Detail

- Higher values ensure that smaller objects contribute to Lumen lighting, but also increase GPU cost

### Final Gather Quality

- Final Gather Quality controls the density of the screen probes, higher values increase GPU cost 

- A value of **1.0** provides a good balance between performance and quality for mobile games

### Max Trace Distance

- Max Trace Distance controls how far the ray tracing will go, keep it small to decrease GPU cost

- Don’t set it larger than the size of the scene

- Smaller values can also reduce some ray incoherence

### Scene Capture Cache Resolution Scale

- Scene Capture Cache Resolution Scale controls the surface cache resolution, smaller values save memory

### Lumen Scene Lighting Update Speed

- Keep Lumen Scene Lighting Update Speed low if the lighting changes are slow and this saves GPU cost

- A value in the range of **0.5 - 1.0** should provide a good balance between performance and quality for mobile games

### Final Gather Lighting Update Speed

- Keep Final Gather Lighting Update Speed low if slow lighting propagation is acceptable

- A value in the range of **0.5 - 1.0** should reach a good balance between performance and quality for mobile games
 
## Lumen Reflection Settings

The reflection parameters below are used in "Steel Arms".

![Reflection #center](images/reflection-setting.png)

### Reflection Quality

- Reflection Quality controls the reflection tracing quality, it is the resolution of the reflection

### Ray Lighting Mode

- The Lighting Mode default is `Surface Cache` which reuses the surface cache data for reflection 

- `Hit Lighting` mode is available when using hardware ray tracing, it evaluates direct lighting instead of using the surface cache

- `Hit Lighting` mode has higher quality with higher GPU cost

- `Hit Lighting` mode can reflect direct lighting of skinned meshes which `Surface cache` mode cannot

- `Surface Cache` mode is recommended for mobile games

### Max Reflection Bounces

- Max Reflection Bounces controls the amount of reflection bounces, a higher value has higher GPU cost

- A value of **1** is recommended for mobile games

After considering the various options to get the best performance, you can build your project and install it on your Android device which has a Mali GPU with hardware ray tracing support and check the results.