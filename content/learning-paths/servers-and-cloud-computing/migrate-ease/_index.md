---
title: Migrate applications to Arm servers using migrate-ease


minutes_to_complete: 45

who_is_this_for: This is an introductory topic for developers looking to migrate applications to Arm-based servers using migrate-ease, a code analysis tool that scans source code repositories to identify architecture-specific porting issues before migration.

description: Scan source code for architecture-specific portability issues using migrate-ease to identify and resolve AArch64 porting challenges before migration.

learning_objectives:
    - Identify architecture-specific dependencies in your application's source code
    - Recognize common migration challenges and how to resolve them
    - Use migrate-ease to detect and address AArch64 portability issues

prerequisites:
    - Access to an [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/) for testing and validation.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:29:38Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 56a38d1d742dd301d48e9ad61ff00e07048559f3f646815e22937113243adcdb
  summary_generated_at: '2026-06-02T04:24:02Z'
  summary_source_hash: 56a38d1d742dd301d48e9ad61ff00e07048559f3f646815e22937113243adcdb
  faq_generated_at: '2026-06-03T01:29:38Z'
  faq_source_hash: 56a38d1d742dd301d48e9ad61ff00e07048559f3f646815e22937113243adcdb
  summary: >-
    Use migrate-ease to scan your source code for architecture-specific issues before migrating
    applications to Arm-based servers. This introductory, Linux-focused path shows how to set
    up dependencies, clone the migrate-ease repository, and run a code scan that targets AArch64,
    including an example that analyzes Protobuf v2.5.0 and writes a JSON report. Migrate-ease
    is a read-only tool designed to examine x86_64-oriented code and suggest changes for AArch64
    on Linux, and it runs on either x86_64 or Arm AArch64 machines. The path emphasizes identifying
    architecture-dependent code and common migration challenges. An Arm-based instance is required
    for testing and validation. Estimated completion time is about 45 minutes.
  faqs:
  - question: What do I need before running migrate-ease?
    answer: >-
      You need access to an Arm-based instance for testing and validation. You also need a Linux
      machine (x86_64 or Arm AArch64) to run the tool, with Git and Python 3 available as shown
      in the setup steps.
  - question: Can I run migrate-ease on x86_64, or do I need an Arm machine?
    answer: >-
      You can run migrate-ease on either x86_64 or Arm AArch64 Linux systems. The tool targets
      migration to AArch64 but does not require Arm hardware to perform the analysis.
  - question: Which packages should I install on my distro before cloning the tool?
    answer: >-
      On Ubuntu 22.04 or Debian 13: python3, python3-pip, python3-venv, unzip, libmagic1, and
      git. On Fedora 42: python3, python3-pip, unzip, and git.
  - question: Which command does the path use to scan the Protobuf v2.5.0 source and write a report?
    answer: >-
      Run: python3 -m cpp --git-repo https://github.com/protocolbuffers/protobuf.git --branch
      v2.5.0 --output result.json --march armv8-a protobuf. This analyzes the specified branch
      and writes findings to a JSON file.
  - question: What result should I expect, and how do I verify it?
    answer: >-
      Expect a JSON report named result.json containing AArch64-related findings. Verify the file
      was created and populated; migrate-ease is read-only and will not modify your source code.
# END generated_summary_faq

author: 
    - Odin Shen
    - Jun He

### Tags
skilllevels: Introductory
subjects: Libraries
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Neon
    - SVE
    - Go
    - Runbook

further_reading:
    - resource:
        title: AWS Graviton Getting Started
        link: https://github.com/aws/aws-graviton-getting-started
        type: documentation
    - resource:
        title: Arm Cloud Migration Program
        link: https://www.arm.com/markets/computing-infrastructure/arm-cloud-migration
        type: website
    - resource:
        title: Migrating Applications to Arm Servers
        link: /learning-paths/servers-and-cloud-computing/migration/
        type: website


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

