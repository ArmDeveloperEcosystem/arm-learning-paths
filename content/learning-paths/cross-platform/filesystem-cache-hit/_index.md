---
title: Improve File System Cache hit rate with the posix_fadvise function 

minutes_to_complete: 15

who_is_this_for: Developers who want to boost performance of applications limited by file system cache misses. 

learning_objectives: 
    - Basic understanding of memory usage in a system
    - Learn how to measure cache miss rates
    - Learn how to use the posix_fadvise() function to provide hints to the kernel about file access patterns 

prerequisites:
    - Basic understanding of C++ and Linux
    - Understanding of File Systems and Memory Usage

author: Kieran Hejmadi

### Tags
skilllevels: Introductory
subjects: Runbook
armips:
    - Neoverse
tools_software_languages:
    - C++
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: posix_fadvise documentation 
        link: https://man7.org/linux/man-pages/man2/posix_fadvise.2.html
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
