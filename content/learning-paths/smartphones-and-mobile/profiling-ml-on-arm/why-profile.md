---
title: Why do you need to profile your ML application?
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Performance
Working out what is consuming time and memory in your application is the first step to achieving the performance that you want. Profiling can help you identify the bottlenecks in your application, and give you clues as how to optimize it.

With Machine Learning (ML) applications, the inference of the Neural Network (NN) is often the heaviest part of the application in terms of computation and memory usage. This is not always the case however, so it is important to profile the application as a whole to detect other possible issues in pre- or post-processing, or the code.

In this Learning Path, you will profile an Android example using LiteRT, but most of the steps also work with Linux, and a wide range of Arm devices. The principles for profiling your application apply to many other inference engines and platforms - only the tools are different.

## Tools

You need two different tools to profile the ML inference or the application's performance running on your Arm device.

* For profiling the ML inference, you will use [ArmNN](https://github.com/ARM-software/armnn/releases)'s ExecuteNetwork.

* For profiling the application as a whole, you will use [Arm Performance Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Studio)'s Streamline, and the Android Studio Profiler.

