---
title: Profiling the Neural Network
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Tools that you can use
App profilers provide a good overall view of performance, but you might want to look inside the model and identify bottlenecks within the network. The network is often where the bulk of the bottlenecks lie, so it warrants closer analysis. 

With general profilers this is hard to do, as there needs to be annotation inside the ML framework code to retrieve the information. It is a complex task to write the profiling annotation throughout the framework, so it is easier to use tools from a framework or inference engine that already has the required instrumentation.

Depending on the model you use, your choice of tools will vary. For example, if you are using LiteRT (formerly TensorFlow Lite), Arm provides the Arm NN delegate that you can run with the model running on Linux or Android, CPU or GPU. 

Arm NN in turn provides a tool called ExecuteNetwork that can run the model and provide layer timings.

If you are using PyTorch, you will probably use ExecuTorch, which is the on-device inference runtime for your Android phone. ExecuTorch has a profiler available alongside it.
