---
title: Add important objects only into ray tracing
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

For best performance exclude actors which are not contributing to lighting from ray tracing. 

Exclude small actors from ray tracing since they contribute very little to the final lighting and may also cause noise for indirect lighting. 

In the Actor detail panel, uncheck `Visible in Ray Tracing` to exclude an actor from ray tracing.

![Visible #center](images/add_object.png)


