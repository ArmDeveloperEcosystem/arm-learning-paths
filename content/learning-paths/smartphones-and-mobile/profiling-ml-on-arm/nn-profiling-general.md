---
title: Profiling the Neural Network
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Profiling your model
App profilers will give you a good overall view of your performance, but often you might want to look inside the model and work out bottlenecks within the network. The network is often the bulk of the time, in which case it will warrant closer analysis. 

With general profilers this is hard to do, as there needs to be annotations inside the ML framework code to get the information. It is a large task to write the profiling annotations throughout the framework, so it is easier to use tools from a framework or inference engine that already has the required instrumentation.

Depending on your model, your choice of tools will differ. For example, if you are using LiteRT (formerly TensorFlow Lite), Arm provides the ArmNN delegate that you can run with the model running on Linux or Android, CPU or GPU. ArmNN in turn provides a tool called `ExecuteNetwork` that can run the model and give you layer timings among other useful information.

If you are using PyTorch, you will probably use ExecuTorch the ons-device inference runtime for your Android phone. ExecuTorch has a profiler available alongside it.
