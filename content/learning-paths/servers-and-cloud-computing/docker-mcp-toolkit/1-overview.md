---
title: The Arm migration challenge and how Docker MCP Toolkit solves it
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why migrate to Arm?

Moving workloads from x86 to Arm64 has become a priority for organizations looking to reduce cloud costs and improve performance. AWS Graviton, Azure Cobalt, and Google Cloud Axion have made Arm-based computing mainstream, offering 20-40% cost savings and improved performance-per-watt for many workloads.

The challenge is that migration is not always straightforward. For most containerized applications, rebuilding a Docker image for Arm64 is enough. But when you encounter legacy applications with hand-optimized x86 assembly, AVX2 intrinsics, or architecture-specific compiler flags, the migration becomes significantly more complex.

## What makes x86-to-Arm migration hard?

Traditional migration approaches require:

- Manual code analysis for x86-specific dependencies.
- Tedious compatibility checks across multiple tools.
- Researching Arm NEON equivalents for each x86 intrinsic.
- Rewriting vectorized code and adjusting loop structures.
- Updating Dockerfiles, base images, and compiler flags.
- Debugging compilation errors on the new architecture.

For a single application with SIMD-optimized code, this can take 5-7 hours of manual work.

## What the Docker MCP Toolkit provides

The Docker MCP Toolkit is a management interface in Docker Desktop that lets you discover, configure, and run containerized MCP (Model Context Protocol) servers. It connects these servers to AI coding assistants through a unified gateway.

For Arm migration, three MCP servers work together:

- **Arm MCP Server**: Provides code scanning (`migrate_ease_scan`), Docker image architecture checking (`check_image`, `skopeo`), Arm knowledge base search (`knowledge_base_search`), and assembly performance analysis (`mca`).
- **GitHub MCP Server**: Enables repository operations including creating pull requests, managing branches, and committing changes.
- **Sequential Thinking MCP Server**: Helps the AI assistant break down complex migration decisions into logical steps.

## How AI-assisted migration works

When connected to the Docker MCP Toolkit, an AI coding assistant like GitHub Copilot can execute the entire migration workflow:

1. Use `check_image` or `skopeo` to verify if base images support `linux/arm64`.
2. Run `migrate_ease_scan` on the codebase to find x86-specific code, intrinsics, and compiler flags.
3. Use `knowledge_base_search` to find correct Arm SIMD equivalents for every x86 intrinsic.
4. Convert the code with architecture-specific accuracy.
5. Update the Dockerfile with Arm-compatible base images and compiler flags.
6. Create a pull request with all changes using the GitHub MCP Server.

What normally takes 5-7 hours of manual work takes about 25-30 minutes.

## What you will build in this Learning Path

In this Learning Path, you will migrate a real-world legacy application - a matrix multiplication benchmark written with AVX2 intrinsics for x86 - to Arm64 using GitHub Copilot and Docker MCP Toolkit.

The demo repository is available at [github.com/JoeStech/docker-blog-arm-migration](https://github.com/JoeStech/docker-blog-arm-migration).

You will:

1. Set up Docker MCP Toolkit with the Arm, GitHub, and Sequential Thinking MCP servers.
2. Connect VS Code with GitHub Copilot to the MCP Gateway.
3. Analyze the legacy x86 codebase to understand what blocks Arm migration.
4. Use AI-driven tools to automate the full migration.
5. Review the pull request created by the AI agent.

In the next section, you will install and configure the Docker MCP Toolkit.
