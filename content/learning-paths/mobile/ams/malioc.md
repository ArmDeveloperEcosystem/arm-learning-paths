---
# User change
title: "Mali Offline Compiler"

weight: 6 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
Mali Offline Compiler is a command-line tool that you can use to compile all shaders and kernels from OpenGL ES and Vulkan, and generate a performance report for the GPU of interest.

## Supported GPUs

To see the full list of supported GPUs use:
```console
malioc --list
```
To get information on API support for a given GPU, use:
```console
malioc --list --core <GPU_name>
```
## Compile your shader

You can compile OpenGL ES (`--opengles`) and Vulkan (`--vulkan`) shader programs, as well as Open GL (`--opengl <version>`) C kernels (Linux only). A performance report will be generated.

The available options are documented in the [User Guide](https://developer.arm.com/documentation/101863/latest/Using-Mali-Offline-Compiler), else can be seen with:
```console
malioc --help
```
# Analyze the report

The report will provide an approximate cycle cost breakdown for the major functional units in the design. Use this information to optimize your shader.

Understanding the output of the report is key to the usefulness of the Mali Offline Compiler. This brief [video tutorial](https://www.youtube.com/watch?v=zEybNlwd7SI) is an excellent starter.
