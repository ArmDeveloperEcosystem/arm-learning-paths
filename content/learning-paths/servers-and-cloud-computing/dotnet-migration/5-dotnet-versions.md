---
title: Evaluate .NET versions for performance on Arm
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Evaluate .NET versions for performance on Arm

In this section, we will explore the performance characteristics of different .NET versions on Arm architecture. Understanding which versions perform best and the features they offer can help you make informed decisions when developing applications for Arm-based systems.

## .NET versions overview

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

- TieredPGO (Profile Guided Optimization), which optimizes runtime performance based on actual usage patterns.
- Improved support for high core counts, making it ideal for modern Arm servers with many cores.

## .NET 7

.NET 7 continues the trend of performance enhancements, with a focus on:

- Native AOT (Ahead-Of-Time) compilation, which can significantly improve startup times and reduce memory usage.
- Enhanced support for cloud-native applications, which are increasingly deployed on Arm-based infrastructure.
- Continued optimizations for high-performance computing scenarios.

## .NET 8 (current LTS)

## .NET 9

## .NET 10 (preview)



## Choosing the right .NET version

When selecting a .NET version for your Arm-based application, consider the following:

- **Performance needs**: If performance is critical, .NET 6 or later is recommended due to its advanced optimizations and support for modern Arm features.
- **Long-term support**: If you require long-term support, .NET 6 is the current LTS version.
- **Feature requirements**: Evaluate the specific features of each version to determine which best meets your application's needs.
