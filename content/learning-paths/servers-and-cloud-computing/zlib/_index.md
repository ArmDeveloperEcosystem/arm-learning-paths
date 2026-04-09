---
title: Improve data compression performnce on Arm servers with zlib-ng

description: Learn how to build and use zlib-ng on Arm servers, using its Neon SIMD and ARMv8 CRC32 optimizations to improve compression performance compared to the system default zlib.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers who want to improve data compression performance on Arm servers by replacing the default zlib with zlib-ng, an actively maintained fork that includes Neon SIMD and ARMv8 CRC32 optimizations.

learning_objectives:
- Build zlib-ng in zlib-compatible mode on an Arm server
- Run example applications using zlib-ng as a drop-in replacement
- Measure and analyze performance improvements with zlib-ng

prerequisites:
- An Arm Linux computer or an [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider running Ubuntu 22.04 or Ubuntu 24.04.

author: Pareena Verma

test_images:
- ubuntu:latest
test_link:
test_maintenance: true

### Tags
armips:
- Neoverse
skilllevels: Introductory
subjects: Libraries
operatingsystems:
- Linux
tools_software_languages:
- zlib

further_reading:
    - resource:
        title: zlib-ng on GitHub
        link: https://github.com/zlib-ng/zlib-ng
        type: documentation
    - resource:
        title: Improving zlib-cloudflare and comparing performance with other zlib forks
        link: https://aws.amazon.com/blogs/opensource/improving-zlib-cloudflare-and-comparing-performance-with-other-zlib-forks/
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
