---
title: Why do you need to profile your ML application?
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Performance
Working out what is consuming time and memory in your application is the first step to achieving the performance you want. Profiling can help you identify the bottlenecks in your application, and understand how to optimize it.

With Machine Learning (ML) applications, the inference of the Neural Network (NN) is often the heaviest part of the application in terms of computation and memory usage. This is not guaranteed however, so it is important to profile the application as a whole to see if pre- or post-processing or other code is an issue.

In this Learning Path, you will profile an Android example using TFLite, but most of the steps listed will also work with Linux, and cover a wide range of Arm devices. The principles for profiling your application are the same for use with other inference engines and platforms, but the tools are different.

## Tools

You need to use different tools to profile the ML inference or the application's performance running on your Arm device.

For profiling the ML inference, you will use [ArmNN](https://github.com/ARM-software/armnn/releases)'s ExecuteNetwork.

For profiling the application as a whole, you will use [Arm Performance Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Studio)'s Streamline, and the Android Studio Profiler.

