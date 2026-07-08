---
title: Develop for Matter with Arm Virtual Hardware

description: Learn how to build Matter reference examples on Arm Virtual Hardware, demonstrate device communication, and automate testing with GitHub Actions CI/CD workflows.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for embedded software developers new to Arm Virtual Hardware.

learning_objectives: 
    - Instantiate Arm Virtual Hardware instances
    - Build and run Matter examples on Arm Virtual Hardware
    - Demonstrate communication between two virtual hardware targets
    - Use GitHub Actions to manage ongoing development in a CI/CD workflow

prerequisites:
    - Some familiarity with embedded programming is assumed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-08T15:23:00Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: bd39d50c93219201ead5de5da627447a91a82ea9c65e232350facd0c3516bedc
  summary_generated_at: '2026-07-08T15:23:00Z'
  summary_source_hash: bd39d50c93219201ead5de5da627447a91a82ea9c65e232350facd0c3516bedc
  faq_generated_at: '2026-07-08T15:23:00Z'
  faq_source_hash: bd39d50c93219201ead5de5da627447a91a82ea9c65e232350facd0c3516bedc
  summary: >-
    You'll set up Arm Virtual Hardware instances modeled
    as Raspberry Pi 4 targets, build and run Matter reference examples, and automate
    tests with GitHub Actions. First, you'll fork the Matter `connectedhomeip` repository, build the
    `lighting-app` on Arm Virtual Hardware, and exercise device communication by issuing `chip-tool`
    commands between two virtual targets. Then, you'll focus on CI/CD: removing unnecessary upstream
    workflows, adding a focused workflow in the fork, and setting up a self-hosted runner that drives
    builds on Arm Virtual Hardware. Finally, you'll integrate the Arm Virtual Hardware API using
    JavaScript and a GitHub secret so the pipeline can remotely control the instances and transmit
    `chip-tool` commands end-to-end.
  faqs:
  - question: Which repository do I fork, and where should the fork live?
    answer: >-
      Fork `project-chip/connectedhomeip` on GitHub. Create the fork under your personal account,
      then clone your fork on each Raspberry Pi 4 Arm Virtual Hardware instance.
  - question: Which Matter example is used during the steps?
    answer: >-
      The path uses the `lighting-app` example from the repository. Run it on the Arm Virtual Hardware
      instances and stop it with `Ctrl+C` when moving on to the CI/CD setup.
  - question: Why are the existing workflows removed from .github/workflows?
    answer: >-
      The upstream repository includes many workflows for different configurations. For this path,
      you'll remove them and add a single workflow so the fork builds and tests the targeted configuration
      on Arm Virtual Hardware.
  - question: What credentials or secrets are required for the automation steps?
    answer: >-
      You'll need a GitHub Personal Access Token that allows updating GitHub Actions workflows. You
      also create an Arm Virtual Hardware API token from **Profile > API** and add it as a GitHub
      secret used by the workflow.
  - question: What result should I expect after extending the workflow to use the AVH API?
    answer: >-
      The pipeline remotely controls the Arm Virtual Hardware instances and automatically transmits
      `chip-tool` commands. Expect to see successful GitHub Actions logs and command/response output
      in the lighting-app console demonstrating communication between the two virtual targets.
# END generated_summary_faq

author: Ronan Synnott

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: CI-CD
armips:
    - Cortex-A
operatingsystems:
    - Linux
tools_software_languages:
    - Matter
    - Arm Virtual Hardware
    - GitHub

further_reading:
    - resource:
        title: Matter GitHub repository
        link: https://github.com/project-chip/connectedhomeip/
        type: website
    - resource:
        title: Welcome to the Virtual Raspberry Pi 4 running on AWS Graviton processors
        link: https://dev.to/aws-builders/welcome-to-the-virtual-raspberry-pi-4-running-on-aws-graviton-processors-2o8e
        type: blog
    - resource:
        title: Matter
        link: https://buildwithmatter.com
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
