---
title: Unreal Engine Setup
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Lumen is Unreal Engine’s fully dynamic global illumination and reflections system. Lumen allows lighting to be changed on the fly during game play.

## Unreal Engine setup 

You need to set up a few options to enable hardware ray tracing support on Lumen for Android devices. This article explains how to set up the options before using Unreal Engine to build your application.

### Enable Shader Model 5 (SM5)

Lumen is enabled only when the SM5 shader format is enabled. 

In the project settings, under `Platforms – Android` enable `Support Vulkan Desktop [Experimental]` to enable SM5 shader format support.

![Shader Model 5 #center](images/sm5.png)

### Select Deferred Shading Mode

Currently, Lumen only supports deferred shading mode. In the project settings, under `Engine – Rendering` select `Deferred Shading` for the `Mobile Shading` option.

![Deferred Shading #center](images/deferred.png)

### Enable Support Hardware Ray Tracing

To enable hardware ray tracing for Lumen, you need to enable it for engine. In the project settings, under `Engine - Rendering` enable `Support Hardware Ray Tracing`.

![Hardware Ray Tracing #center](images/hwrt.png)

### Enable Use Hardware Ray Tracing when available

Lumen supports both software and hardware ray tracing. To enable hardware ray tracing the project settings, under `Engine - Rendering` enable `Use Hardware Ray Tracing when available`. 

This setting tells the application to use hardware ray tracing first, then use software ray tracing if hardware ray tracing is not supported on the device. 

![Hardware when available #center](images/hwrt_lumen.png)

### Set Up Console Variables

Finally, you will need to set up 2 console variables in your engine configuration file. 

Setting `r.Android.DisableVulkanSM5Support=0` allows the use of SM5 shader format. 

Setting `r.RayTracing.AllowInline=1` enables the Ray Query shader support for Vulkan.

```C 
r.Android.DisableVulkanSM5Support=0
r.RayTracing.AllowInline=1
```

Rebuild your project and install it on your Android device which has a Mali GPU with hardware ray tracing support.