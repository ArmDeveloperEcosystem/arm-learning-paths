---
title: Profiling the Neural Network
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Profiling your model
App profilers will give you a good overall view of your performance, but often you might want to look inside the model and work out bottlenecks within the network. The network is often the bulk of the time, in which case it will warrant closer analysis. 

General profilers are unable to do this, as there needs to be annotations inside the ML framework code to get the information. It is a large task to write the profiling annotations throughout the framework, so it is easier if we use tools from a framework or inference engine that can already do the job.

Depending on your model the tools available will differ. For example, if you are using LiteRT (formerly TensorFlow Lite), Arm provides the ArmNN delegate that you can run the model with on Linux or Android, CPU or GPU. ArmNN in turn provides a tool called `ExecuteNetwork` that can run the model and give you layer timings and other useful information.

If you are using PyTorch, you will probably want ExecuTorch on an Android phone, and this also has a profiler available alongside it.
