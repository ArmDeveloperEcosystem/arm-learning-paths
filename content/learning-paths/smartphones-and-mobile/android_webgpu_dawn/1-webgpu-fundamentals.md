---
title: Introduction to WebGPU
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is WebGPU?

WebGPU is the successor to WebGL, a well adopted modern API standard for interfacing with GPUs. WebGPU provides better compatibility with modern GPUs, support for general-purpose GPU computations, faster operations, and access to more advanced GPU features. It is designed to provide a _unified access_ to GPUs, agnostic to GPU vendors and operating systems.

WebGPU is a Render Hardware Interface built on top of various backend APIs like Vulkan, DirectX, and Metal (depending on the operating system). 

WebGPU is available through web browsers using the webgpu.h header file. 

The high level view of WebGPU is shown below:

![WebGPU high level view #center](images/webgpu_highlevel.png "WebGPU High Level View")

## What are the benefits of WebGPU?

WebGPU takes into account learnings from older standards like WebGL and OpenGL and provides the following benefits: 

* A reasonable level of abstraction
* Good performance
* Cross-platform
* Backed by W3C standards group
* Future-proof design

WebGPU is a standard and not a true API, so the implementation can be adopted and developed as an interface between native applications developed in any programming language.

The performance requirements for web pages is actually the same as for native application.

{{% notice Note %}}
When designing an API for the Web, the two key constraints are portability and privacy. 

The limitations of the API due to privacy considerations can be disabled when using WebGPU as a native API.
{{% /notice %}}

## What are the benefits of using C++ for WebGPU?

The initial target for WebGPU was JavaScript.  The initial `webgpu.h` header file is written in C. 

This Learning Path uses C++ rather than JavaScript or C because for the following reasons:

* C++ is still the primary language used for high performance graphics applications, such as video games, render engines, and modeling tools.
* The level of abstraction and control of C++ is well suited for interacting with graphics APIs in general.
* Graphics programming is a good way to learn more C++.

## Dawn: the Google WebGPU implementation

Since WebGPU is a standard and not an implementation, there are different implementations. 

[Dawn](https://github.com/google/dawn) is an open-source, cross-platform implementation of the WebGPU standard. 

It implements the WebGPU functionality specified in `webgpu.h`. Dawn is meant to be integrated as part of a larger system like Chromium or a native Android Application.

Dawn provides several WebGPU building blocks:

* WebGPU C/C++ headers that applications and other building blocks use, including a header file and C++ wrapper.
* A "native" implementation of WebGPU using appropriate APIs: D3D12, Metal, Vulkan and OpenGL. 
* A client-server implementation of WebGPU for applications that are in a sandbox without access to native drivers.
* Tint, a compiler for the WebGPU Shader Language (WGSL), that converts shaders to and from WGSL.

Because it is written in C++, Dawn provides better error messages and logging. Because it is open-source, it is easier to inspect stack traces when applications crash.

Dawn is usually ahead of `wgpu-native`, another WebGPU implementation, when it comes to new functionalities and standards changes. 
