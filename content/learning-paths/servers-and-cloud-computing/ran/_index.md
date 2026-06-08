---
title: Get started with the Arm 5G RAN Acceleration Library (ArmRAL)

minutes_to_complete: 15

who_is_this_for: This is an introductory topic for software developers new to the
  Arm RAN Acceleration Library (ArmRAL).


learning_objectives:
- Build and install the Arm RAN Acceleration Library
- Test the capabilities of your platform

prerequisites:
- An Arm computer running Linux. Cloud instances can be used, refer to the list of
  [Arm cloud service providers](/learning-paths/servers-and-cloud-computing/csp/).

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:57:23Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 2b329c566f7fea90010c52f1ce1cb11bccf9d32cf604aaa720bfca5ef1f85fae
  summary_generated_at: '2026-06-02T04:55:40Z'
  summary_source_hash: 2b329c566f7fea90010c52f1ce1cb11bccf9d32cf604aaa720bfca5ef1f85fae
  faq_generated_at: '2026-06-03T01:57:23Z'
  faq_source_hash: 2b329c566f7fea90010c52f1ce1cb11bccf9d32cf604aaa720bfca5ef1f85fae
  summary: >-
    This introductory Learning Path shows how to build and install the Arm RAN Acceleration Library
    (ArmRAL) on an Arm-based Linux system and then exercise it to test your platform’s capabilities.
    You will use a development machine—either a local Arm server, laptop, or desktop, or an Arm-based
    cloud instance—compile the open-source BSD-licensed library with GCC, and run it to validate
    the environment. The path is designed for developers new to ArmRAL and 5G RAN acceleration
    and focuses on practical build-and-run steps that take about 15 minutes. No additional prerequisites
    are explicitly listed beyond access to an Arm computer running Linux.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an Arm computer running Linux and a development environment on that machine. You
      can use a local Arm server, laptop, or desktop, or an Arm-based cloud instance.
  - question: Can I use an Arm-based cloud instance instead of local hardware?
    answer: >-
      Yes. You can use an Arm-based instance from a cloud service provider; see the list of Arm
      cloud service providers referenced in the prerequisites.
  - question: Which operating system do the instructions target?
    answer: >-
      Linux on Arm. A specific distribution is not explicitly listed in the provided context.
  - question: Which compiler is used to build ArmRAL in this path?
    answer: >-
      GCC is used to build the library according to the tools listed for this Learning Path.
  - question: What result should I expect after completing the steps?
    answer: >-
      You will have ArmRAL built and installed, and you will run basic tests to check your platform’s
      capabilities. A successful outcome is a clean build and tests completing without errors.
# END generated_summary_faq

author: Ronan Synnott

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

