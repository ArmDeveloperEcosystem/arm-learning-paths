---
title: Take Good Advantage of Instancing
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Take Good Advantage of Instancing
Instanced actors can share the same geometry data in BLAS as the acceleration structure hence saving memory usage and increasing the cache hit. Therefore, to get the best performance and memory usage when using hardware ray tracing, you should try to use object instancing as much as possible. 

You can also use the Picker view under _Ray Tracing Debug_ of the Unreal editor to check the instancing status of the acceleration structure. Here are the steps for checking the instancing status in the Unreal editor:

1. Use the command `r.RayTracing.Debug.PickerDomain 1` to select the instance mode for the Picker:

![](images/picker-command.png)

2. Select `Picker` view under _Ray Tracing Debug_ on viewport of the Unreal editor:

![](images/picker-view.png)

3. Use the mouse cursor to select the instance which you want to check. Then there will be shown the acceleration structure infomation of this instance on the screen. Use the detail information under [BLAS] to check if two instances share the same BLAS data:

![](images/blas.png)
