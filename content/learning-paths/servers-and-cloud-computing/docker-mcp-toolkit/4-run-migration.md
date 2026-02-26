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

Make sure the MCP_DOCKER server is running in VS Code (check **Extensions** > **MCP_DOCKER** > **Start Server** if needed).

## Give GitHub Copilot migration instructions

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

## Watch the migration execute

GitHub Copilot orchestrates the migration through four phases using the Docker MCP Toolkit.

### Phase 1: Image analysis

Copilot uses the `skopeo` tool from the Arm MCP Server to analyze the base image:

```text
Checking centos:6 for arm64 support...
```

The tool reports that `centos:6` has no `linux/arm64` build available. This is the first blocker identified. Copilot determines that the base image must be replaced.

### Phase 2: Code scanning

Copilot runs the `migrate_ease_scan` tool with the C++ scanner:

```text
Running migrate_ease_scan with scanner: cpp
```

The scan detects:

- AVX2 intrinsics (`_mm256_*` functions) in `matrix_operations.cpp`.
- The `-mavx2` compiler flag in the Dockerfile.
- The x86-specific header `<immintrin.h>`.

Each issue includes the file location, line number, and specific code requiring modification.

### Phase 3: Knowledge base lookup and code conversion

For each x86 intrinsic found, Copilot queries the Arm MCP Server knowledge base:

```text
Searching knowledge base for: AVX2 to NEON intrinsic conversion
```

The knowledge base returns Arm documentation with the conversions:

| x86 AVX2 Intrinsic | Arm NEON Equivalent |
|---------------------|---------------------|
| `_mm256_setzero_pd()` | Two `vdupq_n_f64(0.0)` operations |
| `_mm256_loadu_pd()` | Two `vld1q_f64()` loads |
| `_mm256_add_pd()` | Two `vaddq_f64()` operations |
| `_mm256_mul_pd()` | Two `vmulq_f64()` operations |

The knowledge base also explains that AVX2 uses 256-bit vectors processing 4 doubles at once, while NEON uses 128-bit vectors processing 2 doubles. Loop strides must be adjusted accordingly.

Copilot rewrites the code using this information:

- Replaces `<immintrin.h>` with `<arm_neon.h>` inside `#ifdef __aarch64__` guards.
- Converts the AVX2 loop structure (stride 4) to NEON (stride 2).
- Rewrites the horizontal reduction for NEON.
- Updates the Dockerfile to use `ubuntu:22.04` with `TARGETARCH` for multi-arch builds.
- Changes the compiler flag from `-mavx2` to `-march=armv8-a+simd`.

### Phase 4: Create the pull request

Copilot uses the GitHub MCP Server to create a pull request with:

- All code changes (source files and Dockerfile).
- A detailed description of what was changed and why.
- Performance predictions for Arm.
- A list of all MCP tools used during the migration.

You can see an example PR at [github.com/JoeStech/docker-blog-arm-migration/pull/1](https://github.com/JoeStech/docker-blog-arm-migration/pull/1).

## Summary of changes

The migration produces these key changes:

**Dockerfile**:
- Replaced `centos:6` with `ubuntu:22.04`.
- Added `TARGETARCH` for multi-architecture builds.
- Changed `-mavx2` to `-march=armv8-a+simd` for Arm builds.

**Source code**:
- Added `#ifdef __aarch64__` architecture guards.
- Replaced all `_mm256_*` AVX2 intrinsics with NEON equivalents (`vld1q_f64`, `vaddq_f64`, `vmulq_f64`).
- Adjusted loop strides from 4 (AVX2) to 2 (NEON).
- Rewrote horizontal reduction using NEON pair-wise addition.

In the next section, you will build, test, and validate the migrated application on Arm.
