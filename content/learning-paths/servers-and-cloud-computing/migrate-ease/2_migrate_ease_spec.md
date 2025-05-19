---
# User change
title: "Migrate-ease and supported programming languages"

weight: 3

layout: "learningpathall"

---

### What is migrate-ease?

[`Migrate-ease`](https://github.com/migrate-ease/) is a fork of [Porting Advisor](https://github.com/arm-hpc/porting-advisor), an open-source project developed by the Arm High Performance Computing Group. It is maintained by the [OpenAnolis](https://github.com/openanolis) Arm Working Group.


`Migrate-ease` is designed to analyze codebases targeting `x86_64` architectures and offers tailored suggestions to facilitate migration to AArch64. The tool currently only supports migration to Linux-based environments and can be run on either `x86_64` or Arm AArch64 Linux machines. 

`Migrate-ease` is a read-only tool - it does not modify your code. It analyzes your source tree and provides architecture-specific recommendations. It does not provide API-level guidance, and it does not transmit data back to OpenAnolis.

### Supported programming languages and checks

The tool scans all files in a source tree, whether or not they are included by the build system. The following programming languages and dependency types are supported. For each language, the types of portability checks performed are listed. 

#### C and C++
- Inline assembly with no corresponding AArch64 implementation.
- Architecture-specific assembly code.
- Use of architecture-specific intrinsics.
- Architecture-specific compilation options.
- Preprocessor errors triggered when compiling on AArch64.
- Compiler-specific code guarded by compiler-specific macros.
- Missing AArch64 detection logic in Makefile or `config.guess` scripts.
- Linking against libraries not available on AArch64.

#### Go
- Inline assembly with no corresponding AArch64 implementation.
- Architecture-specific assembly code.
- Use of architecture-specific intrinsics.
- Linking against libraries unavailable on AArch64.

#### Python
- Inline assembly with no corresponding AArch64 implementation.
- Use of architecture-specific intrinsics.
- Use of architecture-specific packages.
- Linking against libraries unavailable on AArch64.

#### Rust
- Inline assembly with no corresponding AArch64 implementation.
- Use of architecture-specific intrinsics.
- Linking against libraries unavailable on AArch64.

#### Java
- JAR dependency scanning.
- Version checks in `pom.xml` file.
- Detection of native method calls in Java source code.
- Recommendations for compatible versions.

#### Dockerfile
- Use of architecture-specific plugins.
- Base image does not support AArch64.

