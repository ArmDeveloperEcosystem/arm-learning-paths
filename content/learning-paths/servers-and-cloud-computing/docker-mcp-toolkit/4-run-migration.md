---
title: Run the AI-driven Arm migration
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Open the project in VS Code

Open the cloned `docker-blog-arm-migration` directory in VS Code:

```bash
cd docker-blog-arm-migration
code .
```

Make sure the MCP_DOCKER server is running in VS Code ( Use **Extensions** > **MCP_DOCKER** > **Start Server** if needed).

This allows GitHub Copilot to invoke the configured MCP servers through the MCP Gateway.

## Provide migration instructions to GitHub Copilot

Open GitHub Copilot Chat in VS Code and paste the following prompt:

```text
Your goal is to migrate this codebase from x86 to Arm64. Use the Arm MCP
Server tools to help you with this migration.

Steps to follow:
1. Check all Dockerfiles - use check_image and/or skopeo tools to verify
   Arm compatibility, changing the base image if necessary
2. Scan the codebase - run migrate_ease_scan with the appropriate language
   scanner and apply the suggested changes
3. Use knowledge_base_search when you need Arm architecture guidance or
   intrinsic equivalents
4. Update compiler flags and dependencies for Arm64 compatibility
5. Create a pull request with all changes using GitHub MCP Server

Important notes:
- Your current working directory is mapped to /workspace on the MCP server
- NEON lane indices must be compile-time constants, not variables
- If unsure about Arm equivalents, use knowledge_base_search to find docs
- Be sure to find out from the user or system what the target machine is,
  and use the appropriate intrinsics. For instance, if neoverse (Graviton,
  Axion, Cobalt) is targeted, use the latest SME/SME2.

After completing the migration:
- Create a pull request with a detailed description of changes
- Include performance predictions and cost savings in the PR description
- List all tools used and validation steps needed
```
This prompt instructs Copilot to use structured MCP tools rather than relying purely on generated suggestions.

## Observe the migration workflow

Copilot now orchestrates the migration using the configured MCP servers. The workflow typically proceeds in several phases.

### Phase 1: Container Image analysis

Copilot invokes `check_image` or `skopeo` from the Arm MCP Server:

```text
Checking centos:6 for arm64 support...
```

The tool reports that `centos:6` has no `linux/arm64` build available. Copilot proposes replacing the base image with a modern multi-architecture alternative.
This step ensures the container can build and run on Arm hardware before addressing source-level changes.

### Phase 2: Source Code scanning

Copilot runs the `migrate_ease_scan` tool with the C++ scanner:

```text
Running migrate_ease_scan with scanner: cpp
```

The scan detects:

- AVX2 intrinsics (`_mm256_*` functions) in `matrix_operations.cpp`.
- The `-mavx2` compiler flag in the Dockerfile.
- The x86-specific header `<immintrin.h>`.

Each finding includes file locations and recommended actions. This structured scan avoids manually searching through the codebase.

### Phase 3: Knowledge base lookup and refactoring code

For each x86 intrinsic found, Copilot queries the Arm MCP Server knowledge base:

```text
Searching knowledge base for: AVX2 to NEON intrinsic conversion
```

The Arm MCP knowledge base provides documented guidance on intrinsic mapping and architecture considerations.
Example mappings:

| x86 AVX2 Intrinsic | Arm NEON Equivalent |
|---------------------|---------------------|
| `_mm256_setzero_pd()` | Two `vdupq_n_f64(0.0)` operations |
| `_mm256_loadu_pd()` | Two `vld1q_f64()` loads |
| `_mm256_add_pd()` | Two `vaddq_f64()` operations |
| `_mm256_mul_pd()` | Two `vmulq_f64()` operations |

Because AVX2 operates on 256-bit vectors (four doubles) and NEON operates on 128-bit vectors (two doubles), Copilot adjusts:
  - Loop stride
  - Accumulation logic
  - Horizontal reduction pattern
  - 
The refactoring typically includes:
  - Guarding architecture-specific code with #ifdef __aarch64__
  - Replacing <immintrin.h> with <arm_neon.h> where appropriate
  - Updating compiler flags (for example replacing -mavx2)
  - Selecting an Arm-compatible base image such as ubuntu:22.04
  - Supporting multi-architecture builds using TARGETARCH
    
All proposed changes should be reviewed before merging.

### Phase 4: Pull request creation

Once modifications are complete, Copilot invokes the GitHub MCP Server to:
  - Create a branch
  - Commit changes
  - Open a pull request

The PR typically includes:
  - Updated Dockerfile
  - Refactored source files
  - A description of the changes
  - A summary of MCP tools used
  - Suggested validation steps for Arm hardware

You can see an example PR at [github.com/JoeStech/docker-blog-arm-migration/pull/1](https://github.com/JoeStech/docker-blog-arm-migration/pull/1).

## Summary of changes

After migration, you should see:

**Dockerfile updates**:
- Replaced `centos:6` with `ubuntu:22.04`.
- Added `TARGETARCH` for multi-architecture builds.
- Changed `-mavx2` to `-march=armv8-a+simd` for Arm builds.

**Source code updates**:
- Added `#ifdef __aarch64__` architecture guards.
- Replaced all `_mm256_*` AVX2 intrinsics with NEON equivalents (`vld1q_f64`, `vaddq_f64`, `vmulq_f64`).
- Adjusted loop strides from 4 (AVX2) to 2 (NEON).
- Rewrote horizontal reduction using NEON pair-wise addition.

In the next section, you will build, test, and validate the migrated application on Arm.
