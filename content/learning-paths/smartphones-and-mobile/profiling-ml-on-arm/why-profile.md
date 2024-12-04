---
title: Why do you need to profile your ML application?
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Performance
A first step towards achieving the performance that you want in a ML Model is to identify what is consuming time and memory in your application. Profiling can help you identify the bottlenecks in your application, and provide clues about how to optimize operations.

With Machine Learning (ML) applications, whilst the inference of the Neural Network (NN) is often the heaviest part of the application in terms of computation and memory usage, it is not necessarily always the case. It is therefore important to profile the application as a whole to detect other possible issues that can negatively impact performance, such as issues with pre- or post-processing, or the code itself.

In this Learning Path, you will profile an Android example using LiteRT. Most of the steps are transferable and also work with Linux, and across a wide range of Arm devices. 

The principles for profiling an application apply to many other inference engines and ?? , only the tools differ.

{{% notice Note %}}
LiteRT is the new name for TensorFlow Lite, or TFLite.
{{% /notice %}}


