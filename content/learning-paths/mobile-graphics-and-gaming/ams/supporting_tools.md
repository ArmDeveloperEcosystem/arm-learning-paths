---
# User change
title: "Supporting tools"

weight: 11 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

Arm provides the following projects to further assist application developers:

[Unity Integration package](https://github.com/ARM-software/mobile-studio-integration-for-unity/). Integrate this package in to your Unity application during development and gain the ability to add more application awareness to Performance Advisor and Streamline profiling reports. This package exports key software counters from the Unity profiler to Streamline, and also exports a C# API to allow developers to export custom annotations and software counters that can be visualized in performance reports.

[Unity System Metrics for Mali package](https://forum.unity.com/threads/introducing-system-metrics-mali-package.1126178/). Integrate this package in to your Unity application during development and visualize frame-based Arm GPU performance metrics using the Unity profiler. This allows efficient early triage of performance problems in-editor, allowing developers to switching to Streamline only when they need to investigate rendering performance issues in more detail.

[Godot integration package](https://github.com/ARM-software/arm-performance-studio-integration-for-godot). This package provides an open-source Godot game engine integration for Streamline and Performance Advisor. It contains GDScript bindings for the Streamline annotation API, allowing users to export custom software counters, and event annotations.

[Arm ASTC Encoder texture compressor](https://github.com/ARM-software/astc-encoder) is an open-source texture compressor for the Adaptive Scalable Texture Compression (ASTC) texture format. It supports all block sizes, all color profiles, as well as both 2D and volumetric 3D textures. The astcenc compressor can be built as either a standalone command-line application or a library that can be integrated into an existing asset creation pipeline.

[libGPUInfo library](https://github.com/ARM-software/libGPUInfo) is an open-source utility that can be integrated into an application to query the configuration of the Arm GPU present in the system, including the GPU model, shader core count, shader core performance characteristics, and cache size. This information can be used to adjust the application workload at runtime to match the capabilities of the device being used.

[libGPUCounters library](https://github.com/ARM-software/libGPUCounters) is an open-source utility that allows applications to select and sample a set of Arm GPU performance counters. This library provides access to the same counter data that can be visualized in the Streamline tool, allowing integration of Arm GPU data into custom tooling.

[libGPULayers library](https://github.com/ARM-software/libGPULayers) is an open-source project that provides tooling to quickly create new Vulkan layers for Android, as well as some off-the-shelf layers that can be used during development.
