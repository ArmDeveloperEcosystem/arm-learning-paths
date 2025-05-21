---
# User change
title: "Why Code Scanning Matters for Arm Migration"

weight: 2

layout: "learningpathall"

---

### Overview of the Common Arm Migration Challenge

Migrating applications to Arm-based architectures is increasingly common across cloud, data center, and edge environments. Arm-powered servers and instances, such as AWS Graviton processors or Ampere Altra-based systems available on platforms like Google Cloud Platform, Microsoft Azure, Alibaba Cloud and Oracle Cloud Infrastructure (OCI), deliver significant performance-per-watt advantages and compelling cost-efficiency.

However, porting workloads to new CPU architecture often involves more than just recompiling. While many applications transition smoothly, others contain architecture-specific code or dependencies – developed originally for x86 – that can lead to build failures, runtime errors, or performance degradation on Arm systems.

Common challenges include detecting:
* Hardcoded x86 SIMD intrinsics
* Inline assembly
* Platform-specific system calls
* Unsupported compiler flags
* Non-portable build scripts or logic

In large or legacy codebases, these issues are often buried in third-party libraries or auto-generated components, making manual inspection slow and unreliable.

### Automated Analysis for Portability
To address these challenges proactively, automated static analysis tools play a critical role. Tools specifically designed for portability analysis enable developers to scan local codebases or remote repositories (e.g., GitHub) —and pinpoint architecture-specific constructs before attempting compilation or deployment on Arm. By surfacing portability concerns early in the development cycle, code scanning reduces time-to-first-build and helps prevent complex failures later.

In this learning path, we will introduce `migrate-ease`, a tool which allows developers to move beyond trial-and-error debugging. It provides clear, actionable insights into potential portability issues, detecting problematic patterns across many mainstream programming languages. These insights, combined with targeted refactoring, accelerate the process of making code portable, maintainable, and production-ready on Arm.

