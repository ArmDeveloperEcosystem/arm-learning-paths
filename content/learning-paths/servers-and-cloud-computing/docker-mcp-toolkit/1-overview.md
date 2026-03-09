---
title: Simplify Arm migration with the Docker MCP Toolkit and Arm MCP Server
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why migrate to Arm?

Arm-based cloud instances are now widely available across major providers, including AWS Graviton, Azure Cobalt, and Google Cloud Axion. These platforms deliver strong performance-per-watt characteristics and, for many workloads, measurable cost savings compared to equivalent x86 instances.

For containerized applications written in portable, architecture-neutral code, migration can be straightforward: rebuild the container for `linux/arm64` and redeploy.

However, many performance-sensitive applications are not architecture-neutral. They may include:

- x86-specific compiler flags (for example `-mavx2`)
- Hand-optimized assembly
- AVX2 intrinsics mapped directly to Intel vector instructions
- Assumptions about register width, alignment, or instruction semantics

In these cases, rebuilding the container is not enough. The source code itself must be adapted for Arm.

## Considerations when migrating from x86 to Arm

When architecture-specific optimizations are present, migration may involve:

- Identifying x86-specific intrinsics or assembly
- Updating compiler flags and build configurations
- Mapping AVX2 operations to appropriate NEON equivalents
- Rewriting vectorized code and adjusting loop structures
- Updating Dockerfiles, base images, and compiler flags
- Validating correctness and performance on Arm systems

These steps are well understood, but they can require careful review across code, build scripts, and container configurations.

## What the Docker MCP Toolkit provides

The Docker MCP Toolkit is a management interface in Docker Desktop that lets you discover, configure, and run containerized MCP (Model Context Protocol) servers. It connects these servers to AI coding assistants through a unified gateway.

## MCP servers for Arm migration

Three MCP servers work together to support the migration workflow:

**Arm MCP Server**

Provides migration-focused tools:
- `migrate_ease_scan` detects x86-specific code and compiler flags
- `check_image` and `skopeo` verify container architecture support
- `knowledge_base_search` accesses learning resources, Arm intrinsics, and software version compatibility
- `mca` performs microarchitectural performance analysis

**GitHub MCP Server**

Enables Git repository operations including creating pull requests, managing branches, and committing changes.

**Sequential Thinking MCP Server**

Helps the AI assistant break down complex migration decisions into logical steps.


## How AI-assisted migration works

When connected to the Docker MCP Toolkit, an AI coding assistant like GitHub Copilot can coordinate a structured migration workflow:

- Verify whether container base images support `linux/arm64` using `check_image` or `skopeo`
- Scan the codebase with `migrate_ease_scan` to identify AVX2 intrinsics, x86-specific flags, and other portability considerations
- Use `knowledge_base_search` to find appropriate Arm SIMD equivalents for every x86 intrinsic
- Refactor the code with architecture-specific accuracy
- Update Dockerfiles and build configurations for Arm compatibility
- Create a pull request with the proposed changes using the GitHub MCP Server

## The demo application

This Learning Path uses a real-world example: a matrix multiplication benchmark written in C++ with AVX2 intrinsics for x86. You'll migrate it to Arm64 using the AI-assisted workflow described above.

The demo repository is available at [github.com/JoeStech/docker-blog-arm-migration](https://github.com/JoeStech/docker-blog-arm-migration).

By the end of this Learning Path, you'll have a working Arm64 container with NEON-optimized code and an automated pull request containing all migration changes.

## What you've learned and what's next

You now understand:
- Why Arm migration requires more than rebuilding containers when architecture-specific code is present
- How the Docker MCP Toolkit connects AI assistants to specialized migration tools
- The structured workflow that GitHub Copilot uses to automate migration tasks

Next, you'll install and configure the Docker MCP Toolkit with the three required MCP servers.
