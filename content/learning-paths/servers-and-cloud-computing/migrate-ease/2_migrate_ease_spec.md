---
# User change
title: "Supported Programming Languages and Common Issues Identified"

weight: 3

layout: "learningpathall"

---

### migrate-ease

This is a fork of [Porting advisor](https://github.com/arm-hpc/porting-advisor), an open source project by the Arm engineering team. Migrate-ease is maintained by the [OpenAnolis](https://github.com/openanolis) Arm Working Group.


It is an innovative project designed to analyze codebases specifically for x86_64 architectures and offers tailored suggestions aimed at facilitating the migration process to aarch64. 
This tool streamlines the transition, ensuring a smooth and efficient evolution of your software to leverage the benefits of aarch64 architecture. 
At present, this tool only supports codebase migration to Linux. It can be run on Arm or non-Arm based machines. The tool does not modify any code, it does not provide API level recommendations, and it does not send any data back to OpenAnolis.

{{% notice Note %}}
Even though Arm software team do our best to identify known incompatibilities, that's still recommend performing appropriate tests on your application before going to Production.
{{% /notice %}}

### List of Supported Programming Languages

This tool scans all files in a source tree, regardless of whether they are included by the build system or not. Currently, the tool supports the following languages/dependencies:

#### C, C++
- Inline assembly with no corresponding aarch64 inline assembly
- Assembly code with no corresponding aarch64 assembly code
- Use of architecture specific intrinsic
- Use of architecture specific compilation options
- Preprocessor errors that trigger when compiling on aarch64
- Compiler specific code guarded by compiler specific pre-defined macros
- Missing aarch64 architecture detection in Makefile, Config.guess scripts
- Linking against libraries that are not available on the aarch64 architecture

#### Go
- Inline assembly with no corresponding aarch64 inline assembly
- Assembly code with no corresponding aarch64 assembly code
- Use of architecture specific intrinsic
- Linking against libraries that are not available on the aarch64 architecture

#### Python
- Inline assembly with no corresponding aarch64 inline assembly
- Use of architecture specific intrinsic
- Linking against libraries that are not available on the aarch64 architecture
- Use of architecture specific packages

#### Rust
- Inline assembly with no corresponding aarch64 inline assembly
- Use of architecture specific intrinsic
- Linking against libraries that are not available on the aarch64 architecture

#### Java
- JAR scanning
- Dependency versions in pom.xml file
- A feature to detect native calls in Java source code
- Compatible version recommendation

#### Dockerfile
- Use of architecture specific plugin
- The base image that dockfile is based on does not support aarch64

