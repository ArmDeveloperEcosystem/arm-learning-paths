---
title: Understand the tradeoffs of building native AOT arm64 binaries
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Understand the tradeoffs of building native AOT arm64 binaries

In this section, we will explore the tradeoffs involved in building native Ahead-Of-Time (AOT) arm64 binaries. AOT compilation can offer significant performance benefits, but it also comes with certain considerations that developers need to be aware of.

## What is AOT compilation?

Ahead-Of-Time (AOT) compilation is a process where the code is compiled into a native binary before execution, rather than being interpreted or compiled Just-In-Time (JIT) during execution. This can lead to faster startup times and reduced memory usage, which are critical for performance-sensitive applications.

## Benefits of AOT for arm64

- **Improved startup time**: Since the code is pre-compiled, applications can start faster as there is no need for JIT compilation at runtime.
- **Reduced memory footprint**: AOT-compiled binaries can have a smaller memory footprint, which is beneficial for devices with limited resources.
- **Consistent performance**: AOT provides more predictable performance as the code is already optimized and compiled.

## Tradeoffs of AOT for arm64

- **Larger binary size**: AOT compilation can result in larger binaries, as all the code is included in the final executable.
- **Longer build times**: The process of AOT compilation can increase build times, as the entire application needs to be compiled ahead of time.
- **Limited runtime optimizations**: Unlike JIT, AOT does not benefit from runtime optimizations that can be applied based on the actual execution context.

## Considerations for using AOT

When deciding whether to use AOT for your arm64 application, consider the following:

- **Application size**: If your application is large, the increase in binary size might be a concern.
- **Deployment environment**: For environments where startup time and memory usage are critical, AOT can be advantageous.
- **Development cycle**: If rapid iteration and testing are important, the longer build times of AOT might be a drawback.

Understanding the tradeoffs of AOT compilation is crucial for making informed decisions about your application's deployment strategy. While AOT can offer significant performance benefits, it is important to weigh these against the potential downsides such as increased binary size and longer build times.

In the next section, we will delve into TieredPGO (Profile Guided Optimization) for .NET and how it can further enhance the performance of your applications.

