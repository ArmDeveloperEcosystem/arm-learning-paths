---
# User change
title: "Supporting tools"

weight: 11 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

Arm provides the following projects to further assist application developers:

* [Unity Integration package](https://github.com/ARM-software/mobile-studio-integration-for-unity/). Integrate this package in to your Unity application during development and gain the ability to add more application awareness to Performance Advisor and Streamline profiling reports. This package exports key software counters from the Unity profiler to Streamline, and also exports a C# API to allow developers to export custom annotations and software counters that can be visualized in performance reports.
* [Unity System Metrics for Mali package](https://forum.unity.com/threads/introducing-system-metrics-mali-package.1126178/). Integrate this package in to your Unity application during development and visualize frame-based Arm GPU performance metrics using the Unity profiler. This allows efficient early triage of performance problems in-editor, allowing developers to switching to Streamline only when they need to investigate rendering performance issues in more detail.
* [Arm ASTC Encoder texture compressor](https://github.com/ARM-software/astc-encoder) is an advanced lossy texture compression format for the OpenGL ES and Vulkan graphics APIs. The ASTC Encoder (astcenc) compressor is the Arm best-in-class texture compressor for this format, available as an open-source project on GitHub.
* [libGPUInfo library](https://github.com/ARM-software/libGPUInfo) is a small utility library that enables applications to query the configuration of the Arm Immortalis or Arm Mali GPU present in the system. This information enables you to adjust application workload complexity to match the performance capability of the current device.
* [Hardware Counter Pipe (HWCPipe) library](https://github.com/ARM-software/HWCPipe) is a utility library that gives applications the ability to sample Mali GPU performance counters. This allows hardware performance data to be integrated data directly in to an application or custom developer tooling.