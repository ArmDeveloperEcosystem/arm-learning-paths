---
title: What do you need to profile?
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Performance
Working out what is taking the time and memory in your application is the first step to getting the performance you want. Profiling can help you identify the bottlenecks in your application and understand how to optimize it.

With Machine Learning (ML) applications, the inference of the Neural Network (NN) itself is often the heaviest part of the application in terms of computation and memory usage. This is not guaranteed however, so it is important to profile the application as a whole to see if pre- or post-processing or other code is an issue.

We will be looking at an Android example using TFLite in this learning path, but most of the tools also work with Linux to cover a wide range of Arm devices. The principles are the same for other inference engines and platforms, but the tools are different.

## Tools

Currently, you need to use different tools to profile the ML inference or the application's performance as a whole.

For profiling the ML inference we will look at [ArmNN](https://github.com/ARM-software/armnn/releases)'s ExecuteNetwork.

For profiling the application as a whole we will look at [Arm Performance Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Studio)'s Streamline, and at the Android Studio Profiler.

