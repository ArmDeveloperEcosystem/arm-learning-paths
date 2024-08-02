---
title: Take Full Advantage of Instancing
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Instanced actors can share the same geometry data in the BLAS of the acceleration structure, thereby saving memory usage and increasing cache hits. To achieve the best performance and memory efficiency when using hardware ray tracing, you should use object instancing as much as possible.

You can also use the `Picker` view under the `Ray Tracing Debug` options in the Unreal Editor to check the instancing status of the acceleration structure. Here are the steps for checking the instancing status in Unreal Editor:

1. Use command `r.RayTracing.Debug.PickerDomain 1` to select instance mode for picker.
![](images/picker-command.png)

2. Select `Picker` view under `Ray Tracing Debug` on viewport of Unreal editor.
![](images/picker-view.png)

3. Use the mouse cursor to select the instance you want to check. The acceleration structure information for this instance will be displayed on the screen. Use the detailed information under `[BLAS]` to verify if two instances share the same BLAS data.
![](images/blas.png)

