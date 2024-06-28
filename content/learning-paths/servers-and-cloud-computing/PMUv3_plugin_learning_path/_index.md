---
title: Learn to use PMUV3_PLUGIN to do performance analysis at a code level and analyse hotspots

minutes_to_complete: 60

who_is_this_for: Engineers working on a workload/codebase to carry out performance analysis at code block level.

learning_objectives: 
    - Get a fine-grained and precise measurement of functions handling a specific task. 
    - The plugin is grouped into 15 categories also known as bundles, and each bundle has a set of PMU events. The values of the same can be obtained in one shot.   
    - Apart from raw PMU event values, the backend tool also provides the KPI/metric values like MPKI, stalls, IPC and many more, thus helping in performance analysis tasks. 

prerequisites:
    - Some familiarity with performance analysis.

author_primary: Gayathri Narayana Yegna Narayanan

### Tags
skilllevels: Advanced
subjects: Performance Analysis at code level
armips:
    - Neoverse
tools_software_languages:
    - C
    - C++
    - Python
operatingsystems:
    - Linux


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
