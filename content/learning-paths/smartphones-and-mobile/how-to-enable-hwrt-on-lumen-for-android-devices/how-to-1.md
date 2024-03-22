---
title: Unreal Engine Setup
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Unreal Engine Setup
Lumen is the latest dynamic global illumination solution from Unreal Engine which also supports hardware ray tracing. When lighting the indoor scene, direct lighting can't generate a good enough quality rendering result. To generate the best lighting result, you also need indirect lighting. Lumen provides a new ray tracing-based solution which allows the developers to render both dynamic direct lighting and indirect lighting at run-time.

![](images/no_lumen.png "Figure 1. The scene without Lumen has only dirct lighting.")

![](images/lumen.png "Figure 2. The scene with Lumen has both direct and indirect lighting")

To use hardware ray tracing Lumen for your application, you will need to set up a few options to enable hardware ray tracing support on Lumen for Android devices. This learning path will show you how to set up all options before using Unreal Engine to build your application.

### Enable SM5 Shader Format
Lumen is only enabled when the SM5 shader format is selected. In project settings, under Platforms – Android, click the `Support Vulkan Desktop [Experimented]` option to enable SM5 shader format support.


![](images/sm5.png)


###  Select Deferred Shading Mode
Currently, Lumen only supports deferred shading mode. In project settings, under Engine – Rendering, select `Deferred Shading` for Mobile Shading option.

![](images/deferred.png)

###  Enable Support Hardware Ray Tracing
To enable hardware ray tracing for Lumen, you need to enable it. In project settings, under Engine - Rendering, select the `Support Hardware Ray Tracing` option.

![](images/hwrt.png)
 

###  Enable Use Hardware Ray Tracing when available
Lumen supports both software and hardware ray tracing. To enable hardware ray tracing for lumen, in the project setting, under Engine - Rendering, select the `Use Hardware Ray Tracing when available` option. This setting will tell the application to use hardware ray tracing first and then to use software ray tracing, if hardware ray tracing is not supported on the device. 
 

![](images/hwrt_lumen.png)

###  Set Up Console Variables
Finally, you will also need to set up 2 console variables in your engine configuration file. `r.Android.DisableVulkanSM5Support=0` removes the restriction of using SM5 shader format. `r.RayTracing.AllowInline=1` enables the Ray Query shader support for Vulkan:

```C 
r.Android.DisableVulkanSM5Support=0
r.RayTracing.AllowInline=1
```
