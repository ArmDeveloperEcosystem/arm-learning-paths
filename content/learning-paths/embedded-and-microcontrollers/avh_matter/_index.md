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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:04:34Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: bd39d50c93219201ead5de5da627447a91a82ea9c65e232350facd0c3516bedc
  summary_generated_at: '2026-06-01T21:27:33Z'
  summary_source_hash: bd39d50c93219201ead5de5da627447a91a82ea9c65e232350facd0c3516bedc
  faq_generated_at: '2026-06-02T22:04:34Z'
  faq_source_hash: bd39d50c93219201ead5de5da627447a91a82ea9c65e232350facd0c3516bedc
  summary: >-
    This introductory Learning Path guides embedded developers through building and running Matter
    reference examples on Arm Virtual Hardware, demonstrating communication between two Raspberry
    Pi 4 virtual targets, and automating development with GitHub Actions on Linux. You will instantiate
    AVH instances, fork and clone the connectedhomeip repository, run an example application,
    and configure a self-hosted runner with a simplified workflow. You will also integrate the
    AVH API—using JavaScript in this path—and add a GitHub secret to drive chip-tool commands
    automatically. Prerequisites include an Arm Virtual Hardware 3rd Party Hardware account, a
    GitHub account, and a Personal Access Token enabled to update GitHub Action workflows. Some
    familiarity with embedded programming is assumed.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an Arm Virtual Hardware 3rd Party Hardware user account and a GitHub account. Generate
      a GitHub Personal Access Token with permission to Update GitHub Action workflows and save
      it locally. Some familiarity with embedded programming is assumed.
  - question: Which Arm Virtual Hardware targets should I create, and how many?
    answer: >-
      Prepare Raspberry Pi 4 instances of Arm Virtual Hardware. You will use multiple instances
      to demonstrate communication between two virtual hardware targets.
  - question: How do I get the Matter sources into my AVH instances?
    answer: >-
      Fork the public connectedhomeip repository to your personal GitHub account. From the console
      of each AVH instance, clone your fork so you can build and run the examples there.
  - question: What should I do before configuring GitHub Actions in the repository?
    answer: >-
      If the lighting-app is still running, stop it with Ctrl+C. Then in .github/workflows, remove
      the existing workflow files so you can add the new workflow used by this path with a self-hosted
      runner.
  - question: How do I enable API-based control of AVH in the workflow, and what result should
      I expect?
    answer: >-
      Generate an AVH API Token from Profile > API and add it as a GitHub secret. The workflow
      is extended (using JavaScript) to transmit chip-tool commands to your virtual devices via
      the AVH API.
# END generated_summary_faq

author: Ronan Synnott

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

