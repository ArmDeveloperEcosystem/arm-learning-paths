---
title: Evaluate .NET versions for performance on Arm
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Evaluate .NET versions for performance on Arm

Understanding which versions perform best and the features they offer can help you make informed decisions when developing applications for Arm-based systems.

.NET has evolved significantly over the years, with each version introducing new features and performance improvements. Here, we will focus on the key versions that have notable performance implications for Arm architecture.

## .NET Core 3.1 (end-of-life 2022)

.NET Core 3.1 was a significant release that introduced better support for Arm64, making it a viable option for developing applications on Arm-based systems. Key features include:

- Improved JIT (Just-In-Time) compilation for Arm64.
- Enhanced garbage collection performance.
- Support for hardware intrinsics, allowing for optimized low-level operations.

## .NET 5 (end-of-life 2022)

.NET 5 marked the unification of the .NET platform, bringing together .NET Core, .NET Framework, and Xamarin. It continued to build on the performance improvements of .NET Core 3.1, with additional enhancements:

- Improved cross-platform performance, including Arm64.
- Introduction of single-file applications, reducing deployment complexity.
- Enhanced support for containerized applications, which is beneficial for cloud deployments on Arm servers.

## .NET 6 (end-of-life 2024)

.NET 6 is a Long-Term Support (LTS) release that further optimizes performance for Arm architecture. It includes:

- TieredPGO (Profile Guided Optimization). TieredPGO is a feature in .NET that allows the runtime to optimize code execution based on the actual usage patterns observed during the application's execution. It combines the benefits of both Tiered Compilation and Profile Guided Optimization to improve performance.
- Improved support for high core counts, making it ideal for modern Arm servers with many cores.

## .NET 7

.NET 7 continues the trend of performance enhancements, with a focus on:

- Native AOT (Ahead-Of-Time) compilation, which can significantly improve startup times and reduce memory usage.
- Enhanced support for cloud-native applications, which are increasingly deployed on Arm-based infrastructure.
- Continued optimizations for high-performance computing scenarios.

## .NET 8 (current LTS)

.NET 8, as the current Long-Term Support (LTS) version, builds upon the advancements of its predecessors with a focus on stability and performance. Key features include:

- Further improvements in Native AOT, enhancing startup times and reducing resource consumption.
- Optimized performance for cloud-native and microservices architectures on Arm.
- Enhanced developer productivity features, making it easier to build and deploy applications on Arm-based systems.

## .NET 9

.NET 9 introduces experimental features and performance enhancements aimed at future-proofing applications. While not an LTS release, it offers:

- Cutting-edge performance optimizations for Arm architecture.
- New language features and runtime improvements.
- Enhanced support for emerging technologies and platforms.

## .NET 10 (preview)


## Hands-on performance comparison

Let's do a comparison between OrchardCore running on .NET 8 and the earliest compatible version of .NET
