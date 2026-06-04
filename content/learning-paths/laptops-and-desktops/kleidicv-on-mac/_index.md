---
title: Build and test KleidiCV on macOS

description: Learn how to build, test, and verify KleidiCV with Scalable Matrix Extensions (SME) on Apple Silicon Macs for accelerated computer vision performance.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers who want to build and test KleidiCV on macOS.

learning_objectives: 
- Install and compile KleidiCV on macOS
- Run KleidiCV example tests
- Enable Scalable Matrix Extensions (SME) and verify increased SME performance

prerequisites:
- A Mac with Apple Silicon (M4 generation or newer)
- Xcode command line tools installed
- Basic familiarity with using the Terminal and command-line tools

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:07:54Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3e93048b46c24514a89ccc2f277b53111a419c049b53662e1461be38a22e83f7
  summary_generated_at: '2026-06-01T22:06:52Z'
  summary_source_hash: 3e93048b46c24514a89ccc2f277b53111a419c049b53662e1461be38a22e83f7
  faq_generated_at: '2026-06-02T23:07:54Z'
  faq_source_hash: 3e93048b46c24514a89ccc2f277b53111a419c049b53662e1461be38a22e83f7
  summary: >-
    This introductory path shows how to download, build, and test Arm KleidiCV on macOS using
    an Apple Silicon Mac (M4 generation or newer). You will compile the library, run its API tests,
    and verify Scalable Matrix Extensions (SME) backend support, including checking for increased
    SME performance where available. KleidiCV provides optimized implementations for Arm Neon,
    SVE2, and SME2 and automatically selects the fastest path for your hardware, so you do not
    need to change existing CV code. Prerequisites are Xcode command line tools and basic Terminal
    familiarity. In about 30 minutes, you will confirm a working KleidiCV build and execute example
    tests on macOS.
  faqs:
  - question: What do I need before running the build steps?
    answer: >-
      You need a Mac with Apple Silicon (M4 generation or newer), Xcode command line tools installed,
      and basic familiarity with using the Terminal and command-line tools. No other prerequisites
      are explicitly listed.
  - question: How do I run the KleidiCV API test and what result should I expect?
    answer: >-
      Run the API test binary at ./build-kleidicv-benchmark-SME/test/api/kleidicv-api-test. The
      output shows the number of tests run and their results, with lines similar to “Vector length
      is set to 16 bytes,” a seed value, and test progress markers.
  - question: How do I verify that the SME backend is enabled and see its impact?
    answer: >-
      Follow the steps to enable SME and then run the tests to confirm SME backend support. The
      Learning Path guides you to verify increased SME performance after enabling SME.
  - question: Do I need to change my code to use Neon, SVE2, or SME2 with KleidiCV?
    answer: >-
      No. KleidiCV automatically detects your hardware and selects the fastest available implementation,
      so you do not need to adjust your application code.
  - question: Do I need a specific computer vision framework to complete this path?
    answer: >-
      No. You can use KleidiCV with any CV framework, and this path focuses on building and testing
      KleidiCV itself. The steps also include running KleidiCV and OpenCV tests.
# END generated_summary_faq

author: Jett Zhou

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
tools_software_languages:
    - KleidiCV 
    - C 
armips:
    - Cortex-A
operatingsystems:
    - macOS

further_reading:
    - resource:
        title: KleidiCV documentation
        link: https://gitlab.arm.com/kleidi/kleidicv/-/tree/0.6.0/doc?ref_type=tags
        type: documentation
    - resource:
        title: Announcing Arm KleidiCV 0.1
        link: https://developer.arm.com/community/arm-community-blogs/b/ai-blog/posts/kleidicv
        type: blog
    - resource:
        title: Learn about function multiversioning
        link: /learning-paths/cross-platform/function-multiversioning/
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

