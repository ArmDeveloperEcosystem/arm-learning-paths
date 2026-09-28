---
title: Migrate applications to Arm servers using migrate-ease

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for developers looking to migrate applications to Arm-based servers using migrate-ease, a code analysis tool that scans local source trees or Git repositories to identify architecture-specific porting issues before migration.

description: Scan source code for architecture-specific portability issues using migrate-ease to identify and resolve AArch64 porting challenges before migration.

learning_objectives:
    - Identify architecture-specific dependencies in your application's source code
    - Recognize common migration challenges and how to resolve them
    - Use migrate-ease to detect and address AArch64 portability issues

prerequisites:
    - Access to an [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/) for testing and validation.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-28T19:49:15Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 060dab4deb1f972d937b093b61e66eb4efdf11ea12736865f22eaf910a26aa70
  summary_generated_at: '2026-09-28T19:49:15Z'
  summary_source_hash: 060dab4deb1f972d937b093b61e66eb4efdf11ea12736865f22eaf910a26aa70
  faq_generated_at: '2026-09-28T19:49:15Z'
  faq_source_hash: 060dab4deb1f972d937b093b61e66eb4efdf11ea12736865f22eaf910a26aa70
  summary: >-
    Assess source code for Arm migration issues with the read-only `migrate-ease` analyzer. You
    prepare a Linux environment, scan a local source tree or Git branch for AArch64 concerns,
    and generate a JSON report. You target Armv8-A and analyze an older Protobuf release to see
    how missing architecture support appears in the findings. You can then apply the same process
    before rebuilding and testing your own workloads on Arm servers.
  faqs:
  - question: Can I run migrate-ease on macOS or Windows?
    answer: >-
      No. Use an `x86_64` or Arm AArch64 Linux host to run the analysis.
  - question: How do I know the example scan finished correctly?
    answer: >-
      Confirm that the command creates `result.json`, then review the report for AArch64 portability
      issues.
  - question: What do the `--git-repo` and `--branch` options do in the example?
    answer: >-
      Use `--git-repo` and `--branch` to analyze a specific repository and branch without cloning
      it first. The example targets Protobuf `v2.5.0` to illustrate missing AArch64 support.
  - question: Can I scan a local source tree instead of a remote Git repository?
    answer: >-
      Yes. You can run `migrate-ease` against your existing local source tree or a Git repository.
  - question: Does migrate-ease modify my code or dependencies?
    answer: >-
      No. You can run `migrate-ease` as a read-only analysis; it doesn’t change your source tree.
# END generated_summary_faq

author: 
    - Odin Shen
    - Jun He

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
