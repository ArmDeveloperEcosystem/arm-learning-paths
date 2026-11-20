---
title: Build and run the Arm 5G RAN Acceleration Library 

minutes_to_complete: 15

who_is_this_for: This is an introductory topic for software developers new to the
  Arm RAN Acceleration Library (ArmRAL).

learning_objectives:
- Build and install the Arm RAN Acceleration Library.
- Test the capabilities of your platform.

prerequisites:
- An Arm computer running Linux, or a [cloud instance](/learning-paths/servers-and-cloud-computing/csp/)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-19T16:01:59Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3496670e85ea5fd32e280256d6bb5b45a5fd873dba57aacb053ae69d293afd2f
  summary_generated_at: '2026-11-19T16:01:59Z'
  summary_source_hash: 3496670e85ea5fd32e280256d6bb5b45a5fd873dba57aacb053ae69d293afd2f
  faq_generated_at: '2026-11-19T16:01:59Z'
  faq_source_hash: 3496670e85ea5fd32e280256d6bb5b45a5fd873dba57aacb053ae69d293afd2f
  summary: >-
    You'll build and test the Arm RAN Acceleration Library on an Arm-based Linux system. First, you'll
    prepare the development environment, obtain the source, and compile the library with GCC.
    You'll then run `make check` to exercise its test suite and inspect the results. Finally, you'll end with a working ArmRAL build to explore telecommunications functions that are used in radio access
    networks.
  faqs:
  - question: Which compiler and build command do I use?
    answer: >-
      Use GCC on an Arm-based Linux system to build the source. You can
      then run `make check` in the build directory.
  - question: Can I use an Arm cloud virtual machine instead of local hardware?
    answer: >-
      Yes, you can follow the build on an Arm-based cloud virtual machine running Linux.
  - question: How do I verify the ArmRAL build?
    answer: >-
      Run `make check` after building. You should see the test suite complete without
      failures.
  - question: How do I choose the ArmRAL build target for my CPU?
    answer: >-
      Run `cat /proc/cpuinfo` and check the flags for `asimd`, `sve`, or `sve2`.
      Set `ARMRAL_ARCH` to `NEON`, `SVE`, or `SVE2` to match a feature that your CPU supports.
  - question: What should I do if the check fails?
    answer: >-
      Review the failing test in the `make check` output. Check that you built with the
      required compiler and dependencies on your Arm Linux system.
# END generated_summary_faq

author: Ronan Synnott

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

test_images:
- ubuntu:latest
test_link: null
test_maintenance: true

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
- Neoverse
operatingsystems:
- Linux
tools_software_languages:
- ArmRAL
- 5G
- GCC
- Runbook

further_reading:
    - resource:
        title: 5G Infrastructure
        link: https://www.arm.com/en/markets/5g/infrastructure
        type: website
    - resource:
        title: Arm RAN Acceleration Library Reference Guide
        link: https://developer.arm.com/documentation/102249
        type: documentation
    - resource:
        title: 5G RAN for Dummies
        link: https://www.arm.com/resources/dummies-guide/5g-ran
        type: documentation
    - resource:
        title: The next chapter for Arm RAN Acceleration Library Open-sourcing the code base & accelerating adoption
        link: https://developer.arm.com/community/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/arm-ral-is-now-open-source
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

