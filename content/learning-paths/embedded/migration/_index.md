---
title: Migrating x86_64 workloads to aarch64

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for embedded software developers looking at migrating containerized workload to aarch64.

learning_objectives: 
    - Software migration methodology
    - Arm compiler ecosystem and libraries
    - Porting compiler intrinsics

prerequisites:
    - Knowledge about software containers
    - Understanding of building workflows
    - Access to an aarch64 or x86_64 machine 

author_primary: Kasper Mecklenburg, Florent Lebeau

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - GCC
    - ACfL
    - Docker

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
# ================================================================================

# Prereqs
---
