---
title: Understand pointer authentication on Arm

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for software developers interested in understanding Arm pointer authentication.

learning_objectives:
    - Create a simple application on an Arm server with pointer authentication.
    - Compile the application with and without pointer authentication to inspect the instructions generated.
    - Exploit the applications with and without pointer authentication to see how pointer authentication instructions enhance security.

prerequisites:
    - An Arm based instance from a [cloud service provider](/learning-paths/servers-and-cloud-computing/csp/), or an on-premise Arm server

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-18T20:22:02Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 389c20aec90a820d791237ed7444ec28dfb7334bb7fb0816134a76fc5ea60b8a
  summary_generated_at: '2026-11-18T20:22:02Z'
  summary_source_hash: 389c20aec90a820d791237ed7444ec28dfb7334bb7fb0816134a76fc5ea60b8a
  faq_generated_at: '2026-11-18T20:22:02Z'
  faq_source_hash: 389c20aec90a820d791237ed7444ec28dfb7334bb7fb0816134a76fc5ea60b8a
  summary: >-
    You'll compare an Arm application built with and without pointer authentication. First, you
    prepare a vulnerable C example and inspect the instructions in both builds. Then, you run an
    exploit against the unprotected binary and observe its effect. Finally, you try the same
    exploit against the protected binary to see how pointer authentication changes the outcome.
  faqs:
  - question: Which binary should I point the exploit at?
    answer: >-
      Use the unprotected build named `main_nopac`. If your build uses a different name, select
      the binary you built without pointer authentication.
  - question: What result should I expect when the exploit succeeds on the unprotected app?
    answer: >-
      When the payload diverts control to `func2`, you should see the message "Hello from
      func2!" and then an interactive shell.
  - question: How do I confirm that my PAC-enabled build includes pointer authentication?
    answer: >-
      Inspect the disassembly of both binaries and look for pointer authentication instructions in the
      protected build. Compare the instruction streams before you run the exploit.
  - question: How do I know that the exploit is blocked on the PAC-enabled binary?
    answer: >-
      Run the same exploit against the protected binary and check that you don't reach `func2`
      or spawn a shell.
  - question: What should I check if exploit.py fails to run or does nothing?
    answer: >-
      Confirm that `pwntools` is installed and that the script targets the correct path to
      the unprotected binary. Also verify that you're running on the Arm system where you built the
      application.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
platforms:
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
  - Oracle Cloud Infrastructure (OCI) Ampere Compute
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Runbook

further_reading:
    - resource:
        title: Learn the architecture - Providing protection for complex software
        link: https://developer.arm.com/documentation/102433
        type: documentation
    - resource:
        title: Code reuse attacks - the compiler story
        link: https://community.arm.com/arm-community-blogs/b/tools-software-ides-blog/posts/code-reuse-attacks-the-compiler-story
        type: blog
    - resource:
        title: Arm A-profile Instruction Set Architecture
        link: https://developer.arm.com/documentation/ddi0602
        type: documentation
    - resource:
        title: pwntools Documentation
        link: https://docs.pwntools.com/en/stable/
        type: documentation
    - resource:
        title: -mbranch-protection (armclang)
        link: https://developer.arm.com/documentation/101754/0620/armclang-Reference/armclang-Command-line-Options/-mbranch-protection
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

