---
title: Take advantage of instancing
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Instanced actors can share the same geometry data in BLAS of acceleration structure hence save the memory usage. 

Try to use object instancing as much as possible when using hardware ray tracing. You can also use the Picker view under `Ray Tracing Debug` to check the instancing status of acceleration structure. 

Here are the steps to check the instancing status in Unreal editor:

1. Use command “r.RayTracing.Debug.PickerDomain 1” to select instance mode for picker

![Picker #center](images/picker-command.png)

2. Select `Picker` view under `Ray Tracing Debug` on viewport

![Picker view #center](images/picker-view.png)

3. Use the mouse cursor to select the instance you want to check and you will see the acceleration structure information for this instance on the screen. Use the detail information under `[BLAS]` to check if two instances share the same Basic Linear  Algebra Subprogram (BLAS) data.

![BLAS #center](images/blas.png)