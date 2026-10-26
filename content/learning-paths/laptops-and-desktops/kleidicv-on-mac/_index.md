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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-28T16:20:10Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3e93048b46c24514a89ccc2f277b53111a419c049b53662e1461be38a22e83f7
  summary_generated_at: '2026-07-28T16:20:10Z'
  summary_source_hash: 3e93048b46c24514a89ccc2f277b53111a419c049b53662e1461be38a22e83f7
  faq_generated_at: '2026-07-28T16:20:10Z'
  faq_source_hash: 3e93048b46c24514a89ccc2f277b53111a419c049b53662e1461be38a22e83f7
  summary: >-
    You'll build Arm KleidiCV from source on macOS and run its bundled tests. You'll compile the
    library, execute the API test, and inspect vector-length and test-count output. KleidiCV selects
    Neon, SVE2, or SME2 implementations based on Apple silicon, so you can validate hardware-specific
    backends without changing application code.
  faqs:
  - question: Where do I find and run the KleidiCV API test after the build?
    answer: >-
      Run the test binary at `./build-kleidicv-benchmark-SME/test/api/kleidicv-api-test`. It prints
      the number of tests executed and their results to confirm the build works.
  - question: What result should I expect from the API test to confirm success?
    answer: >-
      Expect output similar to a vector length report and a summary of tests run and passed. A
      clean pass indicates the build and public API are functioning.
  - question: How do I verify that the SME backend is being used?
    answer: >-
      KleidiCV auto-detects your CPU and selects the fastest path: Neon, SVE2, or SME2. Review
      the test output in the SME verification step. On supported Apple silicon, SME support is
      exercised during the tests.
  - question: Do I need to change my application code to target Neon, SVE2, or SME2?
    answer: >-
      No. KleidiCV automatically detects the hardware and chooses the optimal implementation,
      so your code doesn't need to change.
  - question: What should I check if the tests fail to run or report errors?
    answer: >-
      Confirm the build finished without errors and run the binary from the path shown. If issues
      persist, confirm that you installed the required tools, then rebuild and rerun the tests.
# END generated_summary_faq

author: Jett Zhou

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
