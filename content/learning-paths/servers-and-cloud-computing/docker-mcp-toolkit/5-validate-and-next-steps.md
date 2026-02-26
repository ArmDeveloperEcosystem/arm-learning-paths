---
title: Validate the migration and explore further
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build and test on Arm

After the pull request is created, build and run the migrated benchmark on Arm:

```bash
docker buildx build --platform linux/arm64 -t benchmark:arm64 . --load
```

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

## Verify the architecture

Confirm the image was built for Arm:

```bash
docker inspect benchmark:arm64 | grep Architecture
```

Expected output:

```output
"Architecture": "arm64",
```

## Build a multi-architecture image

To support both x86 and Arm from the same Dockerfile:

```bash
docker buildx create --name multiarch --use
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  --tag your-registry/benchmark:latest \
  --push .
```

## Time comparison

| Approach | Time |
|----------|------|
| Manual migration (install tools, research intrinsics, rewrite code, debug, document) | 5-7 hours |
| Docker MCP Toolkit + GitHub Copilot (prompt, review, merge) | 25-30 minutes |

## Add CI/CD architecture validation

Prevent regressions by adding architecture checks to your CI pipeline:

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

## Important caveats

Not all AI models produce equal results for migration tasks. The Arm MCP Server provides deterministic context through its tools, but the AI model itself is stochastic. Keep these points in mind:

- Always use a current flagship model for best results.
- Test any performance predictions the model makes against actual benchmarks.
- Review the generated NEON code for correctness, especially horizontal reductions and lane indexing.
- NEON lane indices must be compile-time constants, not variables.

## Explore further

The Docker MCP Toolkit and Arm MCP Server support more than the demo shown here:

- **Multiple languages**: The `migrate_ease_scan` tool supports C++, Python, Go, JavaScript, and Java.
- **Performance analysis**: The `mca` (Machine Code Analyzer) tool predicts IPC and execution time on different CPU architectures.
- **Knowledge base**: The `knowledge_base_search` tool covers all content from [learn.arm.com](https://learn.arm.com) Learning Paths, intrinsics documentation, and software compatibility information.
- **Dynamic MCP**: AI agents can discover and add new MCP servers from the Docker MCP Catalog during a conversation without manual configuration.

## Summary

In this Learning Path, you:

1. Installed and configured the Docker MCP Toolkit with the Arm MCP Server, GitHub MCP Server, and Sequential Thinking MCP Server.
2. Connected VS Code with GitHub Copilot to the MCP Gateway.
3. Examined a legacy x86 application with AVX2 intrinsics to understand migration blockers.
4. Used a single AI prompt to automate the full migration: image analysis, code scanning, intrinsic conversion, Dockerfile updates, and pull request creation.
5. Built and validated the migrated application on Arm64.

The Docker MCP Toolkit turns what was previously a manual, multi-hour process into a conversational AI workflow running securely inside Docker containers.
