---
title: Learn SVE and SME programming with SIMD Loops

description: Learn how to write high-performance SIMD code using the SIMD Loops project, with hands-on examples demonstrating SVE, SVE2, and SME2 features on Arm processors.

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for software developers who want to learn how to use the full range of features available in SVE, SVE2, and SME2 to improve software performance on Arm processors.

learning_objectives:
     - Improve SIMD code performance using Scalable Vector Extension (SVE) and Scalable Matrix Extension (SME)
     - Describe what SIMD Loops contains and how kernels are organized across scalar, Neon, SVE, SVE2, and SME2 variants
     - Build and run a selected kernel with the provided runner and validate correctness against the C reference
     - Choose the appropriate build target to compare Neon, SVE/SVE2, and SME2 implementations

prerequisites:
    - An AArch64 computer running Linux or macOS. You can use cloud instances, refer to [Get started with Arm-based cloud instances](/learning-paths/servers-and-cloud-computing/csp/) for a list of cloud service providers
    - Some familiarity with SIMD programming and Neon intrinsics
    - Recent toolchains that support SVE/SME (GCC 13+ or Clang 16+ recommended)

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:51:17Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b1c43e1bf971db4582ca358c98dab2c7e6e047d6c79bfcc0db148bc575f33679
  summary_generated_at: '2026-06-01T21:18:06Z'
  summary_source_hash: b1c43e1bf971db4582ca358c98dab2c7e6e047d6c79bfcc0db148bc575f33679
  faq_generated_at: '2026-06-02T21:51:17Z'
  faq_source_hash: b1c43e1bf971db4582ca358c98dab2c7e6e047d6c79bfcc0db148bc575f33679
  summary: >-
    This advanced Learning Path shows how to use Arm’s Scalable Vector Extension (SVE), SVE2,
    and Scalable Matrix Extension (SME/SME2) with the SIMD Loops project. You will clone the repository,
    explore how kernels are organized across scalar, Neon, SVE/SVE2, and SME2 variants, and study
    loop 202, a single-precision matrix multiplication example that ties inner_loop_202 to matmul_fp32.
    You then build and run selected kernels with the provided runner, validate results against
    the C reference, and choose build targets to compare Neon, SVE/SVE2, and SME2 implementations.
    The path targets AArch64 systems on Linux or macOS and expects recent GCC or Clang toolchains
    with SVE/SME support.
  faqs:
  - question: What do I need before running the examples?
    answer: >-
      Use an AArch64 computer running Linux or macOS, with a recent toolchain that supports SVE/SME
      (GCC 13+ or Clang 16+ recommended). Some familiarity with SIMD programming and Neon intrinsics
      is expected. You can use Arm-based cloud instances if local hardware is not available.
  - question: How do I know my machine is Arm-based?
    answer: >-
      Run uname -m. On Linux, the expected output is aarch64; on macOS, the expected output is
      arm64.
  - question: Where are the loop kernels listed, and how are they organized?
    answer: >-
      The source for loops is under the loops directory. The complete list of loops, with brief
      descriptions, is documented in the loops.inc file.
  - question: Which example does this path use to explain the project structure, and what does
      it compute?
    answer: >-
      It uses loop 202, which implements single-precision floating-point matrix multiplication
      C[M×N] = A[M×K] × B[K×N]. You will examine inner_loop_202() in loops/loop_202.c and the
      matmul_fp32 routine in loops/matmul_fp32.c.
  - question: How do I build, run, and validate a kernel implementation?
    answer: >-
      Build and run a selected kernel using the project's runner and validate correctness against
      the C reference implementation. Choose the appropriate build target to compare Neon, SVE/SVE2,
      and SME2 variants as demonstrated in the Learning Path.
# END generated_summary_faq

author:
    - Alejandro Martinez Vicente
    - Mohamad Najem

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
    - Cortex-A
operatingsystems:
    - Linux
    - macOS
tools_software_languages:
  - C
  - CPP
  - GCC
  - Clang
  - SME2
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - mobile-graphics-and-gaming
    - automotive

further_reading:
    - resource:
        title: SVE Programming Examples
        link: https://developer.arm.com/documentation/dai0548/latest
        type: documentation
    - resource:
        title: SIMD Loops Repository
        link: https://gitlab.arm.com/architecture/simd-loops
        type: documentation
    - resource:
        title: Scalable Vector Extensions Resources
        link: https://developer.arm.com/Architectures/Scalable%20Vector%20Extensions
        type: documentation
    - resource:
        title: Port Code to Arm Scalable Vector Extension (SVE)
        link: /learning-paths/servers-and-cloud-computing/sve
        type: website
    - resource:
        title: Introducing the Scalable Matrix Extension for the Armv9-A Architecture
        link: https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/scalable-matrix-extension-armv9-a-architecture
        type: website
    - resource:
        title: Arm Scalable Matrix Extension (SME) Introduction (Part 1)
        link: https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction
        type: blog
    - resource:
        title: Arm Scalable Matrix Extension (SME) Introduction (Part 2)
        link: https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction-p2
        type: blog
    - resource:
        title: (Part 3) Matrix-matrix multiplication. Neon, SVE, and SME compared
        link: https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/matrix-matrix-multiplication-neon-sve-and-sme-compared
        type: blog
    - resource:
        title: Build adaptive libraries with multiversioning
        link: /learning-paths/cross-platform/function-multiversioning/
        type: website
    - resource:
        title: SME Programmer's Guide
        link: https://developer.arm.com/documentation/109246/latest
        type: documentation
    - resource:
        title: Compiler Intrinsics
        link: https://en.wikipedia.org/wiki/Intrinsic_function
        type: website
    - resource:
        title: ACLE - Arm C Language Extension
        link: https://github.com/ARM-software/acle
        type: website
    - resource:
        title: Application Binary Interface for the Arm Architecture
        link: https://github.com/ARM-software/abi-aa
        type: website


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

