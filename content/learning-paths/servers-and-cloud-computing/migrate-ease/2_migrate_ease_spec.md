---
# User change
title: "Supported Programming Languages and Common Issues Identified"

weight: 3

layout: "learningpathall"

---

### What is migrate-ease?

[Migrate-ease](https://github.com/migrate-ease/) is a fork of [Porting advisor](https://github.com/arm-hpc/porting-advisor), an open-source project developed by Arm. Migrate-ease is maintained by the [OpenAnolis](https://github.com/openanolis) Arm Working Group.


It is designed to analyze codebases specifically for `x86_64` architectures and offers tailored suggestions to facilitate the migration process to aarch64. 
At present, this tool only supports codebase migration to Linux. The tool can be run on Arm or `x86_64` Linux machines. The tool does not modify any code, it inspects your code and provides recommendations.
It does not provide API level recommendations, and it does not send any data back to OpenAnolis.

### List of Supported Programming Languages

This tool scans all files in a source tree, regardless of whether they are included by the build system or not. Currently, the tool supports the following languages/dependencies and the types of checks available for each launguage are shown:

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
- Dependency versions in `pom.xml` file
- A feature to detect native calls in Java source code
- Compatible version recommendations

#### Dockerfile
- Use of architecture specific plugin
- The base image that dockerfile is based on does not support aarch64

