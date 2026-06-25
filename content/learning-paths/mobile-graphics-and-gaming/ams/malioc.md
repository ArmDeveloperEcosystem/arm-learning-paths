---
# User change
title: Generate a performance report with Mali Offline Compiler

weight: 10 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Before you begin 

Mali Offline Compiler is a command-line tool that you can use to compile all shaders and kernels from OpenGL ES and Vulkan, and generate a performance report for the GPU of interest.

In a terminal, test that Mali Offline Compiler is installed correctly, by typing:

```
malioc --help
```

The `--help` option returns usage instructions and the full list of available options for the malioc command.
Note

{{% notice %}}
On macOS, Mali Offline Compiler might not be recognized as an application from an identified developer. To enable Mali Offline Compiler, open **System Preferences > Security & Privacy**, and select **Allow Anyway** for the `malioc` item.
{{% /notice %}}

## Supported GPUs

To see the full list of [supported GPUs](https://developer.arm.com/documentation/101863/latest/Platform-support/GPU-support) use:

```console
malioc --list
```

To get information on [API support](https://developer.arm.com/documentation/101863/latest/Platform-support/API-support) for a given GPU, use:

```console
malioc --info --core <GPU_name>
```

## Compile your shader

You can compile OpenGL ES (`--opengles`) and Vulkan (`--vulkan`) shader programs, as well as Open GL (`--opengl <version>`) C kernels (Linux host only).

A performance report will be generated.

An example (`OpenGL ES`) shader is provided in the [documentation](https://developer.arm.com/documentation/102468/latest/Compile-your-shader):
```C
#version 310 es
#define WINDOW_SIZE 5

precision highp float;
precision highp sampler2D;

uniform bool toneMap;
uniform sampler2D texUnit;
uniform mat4 colorModulation;
uniform float gaussOffsets[WINDOW_SIZE];
uniform float gaussWeights[WINDOW_SIZE];

in vec2 texCoord;
out vec4 fragColor;

void main() {
	fragColor = vec4(0.0);
	for (int i = 0; i < WINDOW_SIZE; i++) {
		vec2 offsetTexCoord = texCoord + vec2(gaussOffsets[i], 0.0);
		vec4 data = texture(texUnit, offsetTexCoord);
		if (toneMap) data *= colorModulation;
		fragColor += data * gaussWeights[i];
    }
}
```

Compile the shader for [Mali-G76](https://developer.arm.com/Processors/Mali-G76) with:
```command
 malioc --core Mali-G76 shader.frag
```

The full list of available options can be seen with:
```console
malioc --help
```
For more information, refer to [Compiling OpenGL ES shaders](https://developer.arm.com/documentation/101863/latest/Using-Mali-Offline-Compiler/Compiling-OpenGL-ES-shaders) and [Compiling Vulkan shaders](https://developer.arm.com/documentation/101863/latest/Using-Mali-Offline-Compiler/Compiling-Vulkan-shaders) in the Mali Offline Compiler User Guide.

## Analyze the report

The report will provide an approximate cycle cost breakdown for the major functional units in the design. Use this information to optimize your shader.

For example, compiling the unoptimized implementation for `Mali-G76` reports the following cycle information:
```output
                                A      LS       V       T    Bound
Total instruction cycles:    4.53    0.00    0.25    2.50        A
Shortest path cycles:        1.00    0.00    0.25    2.50        T
Longest path cycles:         4.53    0.00    0.25    2.50        A
A = Arithmetic, LS = Load/Store, V = Varying, T = Texture
```

An example optimization is explained in the [documentation](https://developer.arm.com/documentation/102468/latest/Optimize-your-shader).
```C
#version 310 es
#define WINDOW_SIZE 5

// Lower precision to fp16
precision mediump float;
precision mediump sampler2D;

uniform bool toneMap;
uniform sampler2D texUnit;
uniform mat4 colorModulation;
uniform float gaussOffsets[WINDOW_SIZE];
uniform float gaussWeights[WINDOW_SIZE];

in vec2 texCoord;
out vec4 fragColor;

void main() {
	fragColor = vec4(0.0);
	for (int i = 0; i < WINDOW_SIZE; i++) {
		vec2 offsetTexCoord = texCoord + vec2(gaussOffsets[i], 0.0);
		vec4 data = texture(texUnit, offsetTexCoord);
		fragColor += data * gaussWeights[i];
    }
    // Tone map final color
	if (toneMap) fragColor *= colorModulation;
}
```
Compiling the optimized implementation reports:
```output
                                A      LS       V       T    Bound
Total instruction cycles:    0.96    0.00    0.25    2.50        T
Shortest path cycles:        0.54    0.00    0.25    2.50        T
Longest path cycles:         0.96    0.00    0.25    2.50        T
A = Arithmetic, LS = Load/Store, V = Varying, T = Texture
```
Observe that the number of `Arithmetic` cycles has been significantly reduced.

Understanding the output of the report is key to the usefulness of the Mali Offline Compiler. This brief [video tutorial](https://developer.arm.com/Additional%20Resources/Video%20Tutorials/Arm%20Mali%20GPU%20Training%20-%20EP3-5) is an excellent starter.

## What you've accomplished

You've used Mali Offline Compiler to analyze shader performance on a Mali-based GPU of interest. 

You can use the components and workflows described in this Learning Path to profile your applications and analyze performance using Arm Performance Studio.

You can also explore the following supporting tools:

- [Unity Integration package](https://github.com/ARM-software/mobile-studio-integration-for-unity/). Integrate this package in to your Unity application during development and gain the ability to add more application awareness to Performance Advisor and Streamline profiling reports. This package exports key software counters from the Unity profiler to Streamline, and also exports a C# API to allow developers to export custom annotations and software counters that can be visualized in performance reports.

- [Unity System Metrics for Mali package](https://forum.unity.com/threads/introducing-system-metrics-mali-package.1126178/). Integrate this package in to your Unity application during development and visualize frame-based Arm GPU performance metrics using the Unity profiler. This allows efficient early triage of performance problems in-editor, allowing developers to switching to Streamline only when they need to investigate rendering performance issues in more detail.

- [Godot integration package](https://github.com/ARM-software/arm-performance-studio-integration-for-godot). This package provides an open-source Godot game engine integration for Streamline and Performance Advisor. It contains GDScript bindings for the Streamline annotation API, allowing users to export custom software counters, and event annotations.

- [Arm ASTC Encoder texture compressor](https://github.com/ARM-software/astc-encoder) is an open-source texture compressor for the Adaptive Scalable Texture Compression (ASTC) texture format. It supports all block sizes, all color profiles, as well as both 2D and volumetric 3D textures. The astcenc compressor can be built as either a standalone command-line application or a library that can be integrated into an existing asset creation pipeline.

- [libGPUInfo library](https://github.com/ARM-software/libGPUInfo) is an open-source utility that can be integrated into an application to query the configuration of the Arm GPU present in the system, including the GPU model, shader core count, shader core performance characteristics, and cache size. This information can be used to adjust the application workload at runtime to match the capabilities of the device being used.

- [libGPUCounters library](https://github.com/ARM-software/libGPUCounters) is an open-source utility that allows applications to select and sample a set of Arm GPU performance counters. This library provides access to the same counter data that can be visualized in the Streamline tool, allowing integration of Arm GPU data into custom tooling.

- [libGPULayers library](https://github.com/ARM-software/libGPULayers) is an open-source project that provides tooling to quickly create new Vulkan layers for Android, as well as some off-the-shelf layers that can be used during development.
