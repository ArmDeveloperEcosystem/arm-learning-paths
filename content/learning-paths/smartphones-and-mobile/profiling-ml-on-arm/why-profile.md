---
title: Why should you profile your ML application?
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Optimizing Performance
A first step towards achieving optimal performance in a Machine Learning Model is to identify what is consuming the most time and memory in your application. Profiling can help you identify the bottlenecks, and it can offer clues about how to optimize operations.

With Machine Learning (ML) applications, whilst the inference of the Neural Network (NN) is often the heaviest part of the application in terms of computation and memory usage, it is not necessarily always the case. It is therefore important to profile the application as a whole to detect other possible issues that can negatively impact performance, such as issues with pre- or post-processing, or the code itself.

In this Learning Path, you will profile an Android example using LiteRT. Most of the steps are transferable and work with Linux, and you can use them on a wide range of Arm devices. 

The principles for profiling an application apply to many other inference engines and platforms, only the tools differ.

{{% notice Note %}}
LiteRT is the new name for TensorFlow Lite, or TFLite.
{{% /notice %}}


