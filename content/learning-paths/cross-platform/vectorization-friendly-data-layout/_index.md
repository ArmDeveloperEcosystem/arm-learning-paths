---
title: Optimize SIMD code with vectorization-friendly data layout

minutes_to_complete: 45

description: Learn how to optimize SIMD performance on Arm by restructuring data layouts from Array-of-Structures to Structure-of-Arrays, with practical examples using Neon and SVE intrinsics.

who_is_this_for: This is an advanced topic for C/C++ developers who are interested in improving the performance of SIMD code.

learning_objectives: 
    - Comprehend the importance of data layout when writing SIMD code

prerequisites:
    - An Arm computer running Linux and a recent version of Clang or the GNU compiler (gcc) installed.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-04T20:53:47Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b9aaf0eafd5333e78f15993bada3ac33ddb55f72af0b773a970ab71a392ab8b5
  summary_generated_at: '2026-08-04T20:53:47Z'
  summary_source_hash: b9aaf0eafd5333e78f15993bada3ac33ddb55f72af0b773a970ab71a392ab8b5
  faq_generated_at: '2026-08-04T20:53:47Z'
  faq_source_hash: b9aaf0eafd5333e78f15993bada3ac33ddb55f72af0b773a970ab71a392ab8b5
  summary: >-
    You'll learn how data layout affects SIMD vectorization on Arm. Starting with an Array-of-Structures
    model that stores x, y, and z values in 12-byte triplets, you'll examine how strided access limits
    four-wide floating-point operations. You'll add padding for four-element vectors, handle boundary
    checks, and write a hand-optimized Arm NEON version when auto-vectorization is insufficient. Then, you'll compare a Structure-of-Arrays layout with contiguous component arrays and explore an SVE
    implementation using the simulation examples.
  faqs:
  - question: How do I know the current data layout is blocking SIMD vectorization?
    answer: >-
      If your structure stores 3-element vectors (x, y, and z), the 12-byte grouping creates
      strided access that can make 4-wide SIMD vectorization of 32-bit floats difficult. Use compiler output and the example programs to see how this layout affects vectorization.
  - question: What should I change in the object struct to improve SIMD access?
    answer: >-
      Replace the three-element `vec3` fields with four-element `vec4` fields and initialize the
      additional element as padding. The 16-byte layout makes four-wide operations easier for the
      compiler. The later Structure-of-Arrays example stores each component contiguously instead.
  - question: Which files do I modify as complexity increases?
    answer: >-
      Copy `simulation1.c` to `simulation2.c` to add bounding-box logic, including the updated
      `simulate_objects()` function, the `ctr4` structure, and the `box` constant. Then copy
      `simulation2.c` to `simulation3.c` for the hand-written NEON version. Create `simulation4.c`
      for the Structure-of-Arrays approach, or `simulation4_sve.c` for the SVE example.
  - question: What should I expect to see in the hand-optimized SIMD version?
    answer: >-
      `simulation3.c` includes `arm_neon.h` and uses types such as `float32x4_t` to process data in
      4-wide chunks. The math is expressed with NEON intrinsics, so vector operations are explicit
      in the source.
  - question: How does the Structure-of-Arrays version change the way the code runs?
    answer: >-
      The Structure-of-Arrays version stores each component, such as all x values, in its own contiguous array. This improves
      sequential access and makes 4-wide operations straightforward, reducing the penalties of
      interleaved fields.
# END generated_summary_faq

author: Konstantinos Margaritis

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
    - Cortex-A
tools_software_languages:
    - GCC
    - Clang
    - Runbook

operatingsystems:
    - Linux
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - mobile-graphics-and-gaming

further_reading:
    - resource:
        title: Array of Structures (AoS), Structure of Arrays (SoA)
        link: https://en.wikipedia.org/wiki/AoS_and_SoA
        type: documentation
    - resource:
        title: Intrinsics
        link: https://developer.arm.com/architectures/instruction-sets/intrinsics/
        type: documentation
    - resource:
        title: Arm Neon Intrinsics Reference
        link: https://arm-software.github.io/acle/neon_intrinsics/advsimd.html 
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
