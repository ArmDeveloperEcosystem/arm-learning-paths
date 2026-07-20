---
title: Integrate Arm Virtual Hardware into CI/CD workflow 1

description: Learn how to integrate Arm Virtual Hardware into a GitHub Actions CI/CD workflow for automated embedded software testing and validation.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for embedded software developers new to Arm Virtual Hardware and its features.

learning_objectives: 
    - Prepare a GitHub repository
    - Integrate AVH into a CI/CD flow with GitHub Actions

prerequisites:
    - Some familiarity with CI/CD concepts is assumed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-02T17:13:33Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b6a7439a701f6ae09ce8c61f02150a61fa6ecc1151050e903492e16794999676
  summary_generated_at: '2026-07-02T17:13:33Z'
  summary_source_hash: b6a7439a701f6ae09ce8c61f02150a61fa6ecc1151050e903492e16794999676
  faq_generated_at: '2026-07-02T17:13:33Z'
  faq_source_hash: b6a7439a701f6ae09ce8c61f02150a61fa6ecc1151050e903492e16794999676
  summary: >-
    You'll connect Arm Virtual Hardware (AVH) to a GitHub Actions CI/CD
    workflow for embedded software. First, you'll prepare a GitHub repository by forking an example
    project, generate a Personal Access Token with permission to update workflow files, and set
    up an AVH instance using the Arm Virtual Hardware install guide. Then, you'll enable GitHub
    Actions on the fork and add a self-hosted runner on an AWS host, selecting a Linux image
    and x64 architecture to match the instance. By the end, you'll configure the repository to use
    an AVH-backed self-hosted runner so workflows can drive automated testing and validation for
    bare‑metal targets.
  faqs:
  - question: Which permission should I enable on the GitHub Personal Access Token?
    answer: >-
      Enable the token to update GitHub Action workflows. Generate it under **Settings > Developer
      settings > Personal access tokens** and save it locally.
  - question: Where do I run the self-hosted runner setup commands?
    answer: >-
      Run the commands shown after selecting **New self-hosted runner** on the machine that will host
      the runner. Use the AWS instance where Arm Virtual Hardware is set up.
  - question: Which runner image and architecture should I choose?
    answer: >-
      Set **Runner image** to **Linux** and **Architecture** to **x64**. This matches the AWS instance as specified
      in the steps.
  - question: How do I enable GitHub Actions on my fork?
    answer: >-
      Open the **Actions** tab in your fork. If workflows are disabled, click **I understand my workflows,
      go ahead and enable them**.
  - question: How do I verify that the self-hosted runner is available to the repository?
    answer: >-
      Open **Settings > Actions > Runners** in the repository and confirm the runner appears in the
      list. If it doesn't, re-check the setup commands on the instance.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: CI-CD
armips:
    - Cortex-M
operatingsystems:
    - Baremetal
tools_software_languages:
    - Arm Virtual Hardware
    - GitHub

### Cross-platform metadata only
shared_path: true
shared_between:
    - embedded-and-microcontrollers

further_reading:
    - resource:
        title: GitHub Actions
        link: https://docs.github.com/en/actions
        type: documentation
    - resource:
        title: Arm Virtual Hardware
        link: https://arm-software.github.io/AVH/main/examples/html/GetStarted.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

