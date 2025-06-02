---
title: Learn how to write SIMD code on Arm using Rust

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for software developers who want take advantage of SIMD code on Arm systems using Rust.

learning_objectives: 
    - Learn how to write SIMD code with Rust on Arm.

prerequisites:
    - An Arm-based computer with recent versions of a C compiler (Clang or GCC) and a Rust compiler installed.

author: Konstantinos Margaritis

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Neoverse
tools_software_languages:
    - GCC
    - Clang
    - Coding
    - Rust
    - Runbook

operatingsystems:
    - Linux
shared_path: true
shared_between:
    - laptops-and-desktops
    - servers-and-cloud-computing
    - mobile-graphics-and-gaming


further_reading:
    - resource:
        title: Rust std::arch documentation
        link: https://doc.rust-lang.org/core/arch/aarch64/index.html
        type: documentation
    - resource:
        title: Rust std::simd documentation
        link: https://rust-lang.github.io/portable-simd/core_simd/index.html
        type: documentation
    - resource:
        title: Neon Intrinsics in Rust
        link: https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/rust-neon-intrinsics
        type: blog
    - resource:
        title: Testing SIMD instructions on ARM with Rust on Android
        link: https://gendignoux.com/blog/2023/01/05/rust-arm-simd-android.html#implicit-feature-detection-beware-of-target-feature
        type: blog


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
