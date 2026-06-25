---
# User change
title: Analyze shader program performance with Mali Offline Compiler

weight: 10 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Before you begin 

Mali Offline Compiler is a command-line tool that you can use to compile shaders and kernels from OpenGL ES and Vulkan. The tool generates a performance report for the GPU of interest.

To test that Mali Offline Compiler is installed correctly, run:

```
malioc --help
```

The `--help` option returns usage instructions and the full list of available options for the malioc command.

{{% notice Note %}}
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

You can compile OpenGL ES (`--opengles`) and Vulkan (`--vulkan`) shader programs. On Linux hosts, you can also compile OpenGL (`--opengl <version>`) C kernels.

A performance report will be generated.

If your frame analysis points to shader cost, compile one of your shaders. You can also use this sample shader to learn how to read the report. 

An example (`OpenGL ES`) shader is provided in [Compile your shader](https://developer.arm.com/documentation/102468/latest/Compile-your-shader) in the Arm documentation:
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

To view the full list of available options, run:

```console
malioc --help
```

For more information, see [Compiling OpenGL ES shaders](https://developer.arm.com/documentation/101863/latest/Using-Mali-Offline-Compiler/Compiling-OpenGL-ES-shaders) and [Compiling Vulkan shaders](https://developer.arm.com/documentation/101863/latest/Using-Mali-Offline-Compiler/Compiling-Vulkan-shaders) in the Mali Offline Compiler User Guide.

## Interpret the report

The report will provide an approximate cycle cost breakdown for the major functional units in the design. Use this information to optimize your shader.

For example, compiling the unoptimized implementation for `Mali-G76` reports the following cycle information:
```output
                                A      LS       V       T    Bound
Total instruction cycles:    4.53    0.00    0.25    2.50        A
Shortest path cycles:        1.00    0.00    0.25    2.50        T
Longest path cycles:         4.53    0.00    0.25    2.50        A
A = Arithmetic, LS = Load/Store, V = Varying, T = Texture
```

An example optimization is described in [Optimize your shader](https://developer.arm.com/documentation/102468/latest/Optimize-your-shader) in the Arm documentation:

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
Observe that the number of total `Arithmetic` cycles has been significantly reduced from 4.53 to 0.96.

To learn more about interpreting Mali Offline Compiler reports, see the [Arm GPU Training - Episode 3.5: Mali Offline Compiler](https://developer.arm.com/Additional%20Resources/Video%20Tutorials/Arm%20Mali%20GPU%20Training%20-%20EP3-5) video tutorial.

## What you've accomplished

You've used Mali Offline Compiler to analyze shader performance on a Mali-based GPU of interest. 

You can use the components and workflows described in this Learning Path to profile your applications and analyze performance using Arm Performance Studio.

You can also explore the following supporting tools:

- [Unity Integration package](https://github.com/ARM-software/mobile-studio-integration-for-unity/) to add more application awareness — in the form of custom annotations and software counters — to Performance Advisor and Streamline profiling reports.
- [Unity System Metrics for Mali package](https://forum.unity.com/threads/introducing-system-metrics-mali-package.1126178/) to visualize frame-based Arm GPU performance metrics using the Unity profiler for efficient early triage of performance problems.
- [Godot integration package](https://github.com/ARM-software/arm-performance-studio-integration-for-godot) to export custom software counters and event annotations in Godot.
- [Arm ASTC Encoder texture compressor](https://github.com/ARM-software/astc-encoder) to compress and decompress textures using the Adaptive Scalable Texture Compression (ASTC) texture format.
- [libGPUInfo library](https://github.com/ARM-software/libGPUInfo) to query the configuration of the Arm GPU present in the system to adjust the application workload at runtime.
- [libGPUCounters library](https://github.com/ARM-software/libGPUCounters) to select and sample a set of Arm GPU performance counters for integration of Arm GPU data into custom tooling.
- [libGPULayers library](https://github.com/ARM-software/libGPULayers) to create new Vulkan layers for Android development.
