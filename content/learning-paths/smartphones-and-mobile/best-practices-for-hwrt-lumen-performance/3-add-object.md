---
title: Only Add Important Objects into Ray Tracing
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Only Add Important Objects into Ray Tracing

As already discussed, the acceleration structure stores all geometry data for ray traversal. This means that you can get faster ray traversal if there isn't much geometry data in the acceleration structure. The first optimization needed is to remove unecessary geometry data from the acceleration structure:
- exclude the actors which are not contributing to lighting from ray tracing
- exclude the small actors from ray tracing since they contribute very little to the final lighting and may also cause noise for indirect lighting
- to do this, in the actor detail panel, uncheck `Visible in Ray Tracing` to exclude these actors from ray tracing, as shown below:

![](images/add_object.png)


