---
title: Review C code for security vulnerabilities with Arm Metis

description: Install Arm Metis, review vulnerable C code, and triage findings from a prepared libpng target.

minutes_to_complete: 45

who_is_this_for: This Learning Path is for developers who want to add AI-assisted security review to an existing code-review workflow. The code in the Learning Path is in C, but Metis is applicable to other languages as well.

learning_objectives:
    - Identify how Metis uses language-aware source analysis and model reasoning.
    - Install Metis and connect it to a supported model provider.
    - Review vulnerable C code, export JSON and SARIF reports, and inspect JSON findings.
    - Triage Metis findings against source code and a Magma-derived libpng diff.

prerequisites:
    - An Arm64 computer running macOS (Apple silicon) or Ubuntu or Debian Linux, or a Windows computer with an Ubuntu or Debian WSL2 environment
    - An API key and sufficient quota for a [Metis-supported model provider](https://github.com/arm/metis/blob/metis-v2.0.0/README.md#2-set-up-llm-provider)
    - Basic familiarity with C, Git, command-line tools, and security code-review procedures

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-23T19:15:21Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 1501d6fb44d16f60d1c2f13ca23c604bea65f2e457cacaa2d22a0c6ff3f243f5
  summary_generated_at: '2026-11-23T19:15:21Z'
  summary_source_hash: 1501d6fb44d16f60d1c2f13ca23c604bea65f2e457cacaa2d22a0c6ff3f243f5
  faq_generated_at: '2026-11-23T19:15:21Z'
  faq_source_hash: 1501d6fb44d16f60d1c2f13ca23c604bea65f2e457cacaa2d22a0c6ff3f243f5
  summary: >-
    You'll use Arm Metis to review vulnerable C code and triage a reported finding. First, you'll
    install Metis and connect a model provider. You'll then review a small C program, export JSON and
    SARIF reports, and compare JSON findings with known defects. Then, you'll prepare a Magma-derived
    libpng target and choose a live or captured report. Finally, you'll check a finding against
    source code, build conditions, and the Magma diff.
  faqs:
  - question: Which shell should I use on Windows to run the commands?
    answer: >-
      Use an Ubuntu or Debian terminal under WSL2. 
  - question: How do I verify that Metis can use my model provider?
    answer: >-
      Run `review_file check.c` in the provider check. Your connection works when the review
      completes without provider errors and Metis prints a token-usage summary. Zero findings
      is a valid result for this file.
  - question: What if Metis reports no findings for the small C target?
    answer: >-
      A valid review can report zero findings. Check your provider connection and Metis logs
      before judging the result. Don't treat an empty report as proof that the program is
      safe. When you have findings, compare their source locations with the known defects.
  - question: Which libpng report should I use for guided triage?
    answer: >-
      Use `results/libpng-live.json` to inspect your run. If it lacks the row-buffer finding,
      select `results/libpng-review-candidate.json` to follow the guided triage. You can also
      use the captured report to avoid the longer live review.
  - question: How does the Magma diff help me triage the libpng finding?
    answer: >-
      Use the diff to see that preparation removed the rejection from an architecture-width check in `png.c`.
      Check the ABI, width limits, and transforms of the application too. Keep the finding
      unconfirmed at runtime until you reproduce the path with the intended build and settings.
# END generated_summary_faq

author:
    - Matt Cossins
    - Michalis Spyrou
    - Michael Koslov

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Security
armips:
    - Neoverse
    - Cortex-A
operatingsystems:
    - Linux
    - macOS
    - Windows
tools_software_languages:
    - Arm Metis
    - C
    - Python
    - Git
    - JSON
    - SARIF

shared_path: true
shared_between:
    - laptops-and-desktops
    - servers-and-cloud-computing

further_reading:
    - resource:
        title: Arm Metis GitHub repository
        link: https://github.com/arm/metis
        type: website
    - resource:
        title: Empowering engineers with AI-enabled security code review
        link: https://developer.arm.com/community/arm-community-blogs/b/ai-blog/posts/empowering-engineers-with-ai-enabled-security-code-review
        type: blog
    - resource:
        title: Arm Metis brings agentic AI to software security
        link: https://newsroom.arm.com/blog/arm-metis-agentic-ai-security
        type: blog
    - resource:
        title: Magma ground-truth fuzzing benchmark
        link: https://hexhive.epfl.ch/magma/
        type: website
    - resource:
        title: Damn Vulnerable C Program repository
        link: https://github.com/hardik05/Damn_Vulnerable_C_Program
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
