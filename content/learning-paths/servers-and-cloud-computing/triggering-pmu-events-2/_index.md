---
title: Triggering common non-cache PMU events for Neoverse CPUs using C and Assembly 

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for software and hardware engineers who want to understand why and how common non-cache PMU events are triggered.

learning_objectives: 
    - Understand common non-cache PMU events
    - Understand why some code triggers certain PMU events on the Neoverse N2 Core
    - Understand which events are triggered during common scenarios

prerequisites:
    - Please note that to run the code and collect the output, your software or debug environment needs some sort of printf() and console support. This example was created on an Arm internal simulation environment but could be run on any simulation environment with printf() support, or on actual hardware (with printf() support in the runtime software). Also please note that this code was run in a bare-metal environment in EL3 with minimal software overhead. If you are running this code on an operating system, like Linux, you may see slight variations in the PMU event counts due to potential software overhead with OS functionality.

author_primary: Johanna Skinnider

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - C
    - Assembly


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
