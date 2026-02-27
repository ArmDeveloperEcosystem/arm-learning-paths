---
title: Validate the migration and explore further
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build and test on Arm

After reviewing and merging the pull request, build the migrated benchmark for Arm64:

```bash
docker buildx build --platform linux/arm64 -t benchmark:arm64 . --load
```
This command builds the image using the Arm64 target platform and loads it into your local Docker image cache.

Run the benchmark:

```bash
docker run --rm benchmark:arm64
```

Expected output:

```output
SIMD Matrix Operations Benchmark
================================
Running on Arm64 architecture with NEON optimizations
=== Matrix Multiplication Benchmark ===
Matrix size: 200x200
Time: 17 ms
Result sum: 1.98888e+08
```
Your timing results may vary depending on the underlying hardware.

## Verify the image architecture

Confirm the image was built for Arm:

```bash
docker inspect benchmark:arm64 | grep Architecture
```

Expected output:

```output
"Architecture": "arm64",
```
This verifies that the container is built for the correct target architecture.

## Build a multi-architecture image

To support both x86 and Arm from the same Dockerfile, use `docker buildx`:

```bash
docker buildx create --name multiarch --use
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  --tag your-registry/benchmark:latest \
  --push .
```
This produces a multi-architecture manifest that allows Docker to automatically pull the correct image for the host platform.

## Comparing approaches

AI-assisted workflows streamline repetitive discovery and mapping tasks, particularly when architecture-specific intrinsics are involved.

| Approach | Effort |
|----------|--------|
| Manual migration (install tools, research intrinsics, rewrite code, debug, document) | Several hours to days, depending on complexity |
| Docker MCP Toolkit + GitHub Copilot (prompt, review, merge) | Reduced to minutes for initial migration, plus review time |

Actual time savings depend on codebase size and complexity, but structured tool invocation reduces the need for manual documentation lookup and repetitive edits.

## Add CI/CD architecture validation

To prevent regressions, add architecture validation to your CI pipeline.
Example GitHub Actions workflow:

```yaml
name: Validate Arm64 Support
on: [push, pull_request]

jobs:
  check-arm64:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Build for arm64
        run: |
          docker buildx build \
            --platform linux/arm64 \
            -t benchmark:arm64-test .
```
This ensures future changes remain compatible with Arm64 builds.

## Validation considerations

Not all AI models produce equal results for migration tasks. While the Arm MCP Server provides structured migration context, AI-generated code should always be reviewed and validated.

- Always use a current foundational model for best results.
- Test any performance predictions the model makes against actual benchmarks.
- Review the generated NEON code for correctness, especially horizontal reductions and lane indexing.
- NEON lane indices must be compile-time constants, not variables.

## Explore further

The Docker MCP Toolkit and Arm MCP Server support more than the example migration shown here:

- **Multiple languages**: The `migrate_ease_scan` tool supports C++, Python, Go, JavaScript, and Java.
- **Performance analysis**: The `mca` (Machine Code Analyzer) tool predicts IPC and execution time on different CPU architectures.
- **Knowledge base**: The `knowledge_base_search` tool covers all content from [learn.arm.com](https://learn.arm.com) Learning Paths, intrinsics documentation, and software compatibility information.
- **Dynamic MCP**: AI agents can discover and add new MCP servers from the Docker MCP Catalog during a conversation without manual configuration.

## Summary

In this Learning Path, you:

1. Installed and configured the Docker MCP Toolkit with the Arm MCP Server, GitHub MCP Server, and Sequential Thinking MCP Server.
2. Connected VS Code with GitHub Copilot to the MCP Gateway.
3. Examined architecture-specific elements in a legacy x86 AVX2 application.
4. Used AI-assisted MCP tools to analyze, refactor, and update the codebase for Arm64.
5. Built and validated the migrated application on Arm64.

The Docker MCP Toolkit enables AI assistants to invoke structured migration tools inside the containerized Arm MCP server. This approach reduces manual lookup and repetitive refactoring work while keeping developers in control of review and validation.
