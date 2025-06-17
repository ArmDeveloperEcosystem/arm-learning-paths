---

title: BOLT Merge :Feature-level and Library-level BOLTing with Profile Merging

minutes_to_complete: 30

who_is_this_for: >
  In networking and high-performance applications, a single execution path (e.g., one feature) often activates only a small portion of the binary. For example, 20% of the application may be exercised under one feature, while the remaining features and external libraries remain untouched.

  A single BOLT pass using one workload leads to partial optimization, typically benefiting only the code paths covered by that specific run.

  This learning path is intended for performance engineers and developers working on Arm-based systems who need to optimize large, feature-rich application binaries that depend on external libraries.

  It demonstrates how to bolt application features and shared libraries independently, then merge the resulting profiles to achieve full code coverage and deploy a fully optimized binary.


learning_objectives:
    - Instrument and optimize binaries for individual workload features using LLVM-BOLT
    - Collect separate BOLT profiles and merge them for comprehensive code coverage
    - Optimize shared libraries independently
    - Integrate these bolted libraries into applications at runtime
    - Compare performance across baseline, isolated, and merged optimization cases

prerequisites:
    - An Arm based system running Linux with BOLT and Linux Perf installed. The Linux kernel should be version 5.15 or later. Earlier kernel versions can be used, but some Linux Perf features may be limited or not available.
    - (Optional) A second, more powerful Linux system to build the software executable and run BOLT.

author: Gayathri Narayana Yegna Narayanan

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
    - Cortex-A
    
tools_software_languages:
    - BOLT
    - perf
    - Runbook
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: BOLT README
        link: https://github.com/llvm/llvm-project/tree/main/bolt
        type: documentation
    - resource:
        title: BOLT - A Practical Binary Optimizer for Data Centers and Beyond
        link: https://research.facebook.com/publications/bolt-a-practical-binary-optimizer-for-data-centers-and-beyond/
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---