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
    - Recent toolchains that support SVE and SME (GCC 13+ or Clang 16+ recommended)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-29T16:49:08Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b1c43e1bf971db4582ca358c98dab2c7e6e047d6c79bfcc0db148bc575f33679
  summary_generated_at: '2026-07-29T16:49:08Z'
  summary_source_hash: b1c43e1bf971db4582ca358c98dab2c7e6e047d6c79bfcc0db148bc575f33679
  faq_generated_at: '2026-07-29T16:49:08Z'
  faq_source_hash: b1c43e1bf971db4582ca358c98dab2c7e6e047d6c79bfcc0db148bc575f33679
  summary: >-
    You'll use the SIMD Loops project to explore Arm Neon, SVE and SVE2, and
    SME2 kernels. First, you'll clone the repository, verify the Arm environment, and
    inspect `loops.inc`. You'll study loop 202 and `matmul_fp32` across scalar, Neon, SVE and SVE2, and SME2
    variants. Then, you'll build selected kernels, compare them with the C reference, and examine predication,
    vector-length-agnostic programming, gather/scatter, streaming mode, and ZA tiles.
  faqs:
  - question: How do I know I’m running on an Arm machine before using SIMD Loops?
    answer: >-
      Run `uname -m`. Expect `aarch64` on Linux or `arm64` on macOS. If you see another value, switch
      to an Arm-based system before continuing.
  - question: Where do I find the list of available loop kernels and their descriptions?
    answer: >-
      Browse the `loops` directory and open `loops.inc`. It lists the kernels with brief descriptions
      and the identifiers used by the project.
  - question: Which files should I open to study the matrix multiplication example?
    answer: >-
      Open `loops/loop_202.c` and locate `inner_loop_202()` around lines 60–70. Then open
      `loops/matmul_fp32.c`, which implements `C[M × N] = A[M × K] × B[K × N]`.
  - question: What SIMD features can I explore with the kernels in SIMD Loops?
    answer: >-
      You can explore predication, vector-length-agnostic (VLA) programming, gather/scatter,
      streaming mode, and ZA tiles. Implementations use C and Arm C Language Extensions (ACLE)
      intrinsics.
  - question: How do I validate a kernel and compare Neon, SVE and SVE2, and SME2 implementations?
    answer: >-
      Build and run the selected kernel with the project runner, then validate its results against
      the C reference implementation. Choose the build target for each variant to compare scalar,
      Neon, SVE and SVE2, and SME2 behavior.
# END generated_summary_faq

author:
    - Alejandro Martinez Vicente
    - Mohamad Najem

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
