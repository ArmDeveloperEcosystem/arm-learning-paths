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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:32:03Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b6a7439a701f6ae09ce8c61f02150a61fa6ecc1151050e903492e16794999676
  summary_generated_at: '2026-06-01T21:01:24Z'
  summary_source_hash: b6a7439a701f6ae09ce8c61f02150a61fa6ecc1151050e903492e16794999676
  faq_generated_at: '2026-06-02T21:32:03Z'
  faq_source_hash: b6a7439a701f6ae09ce8c61f02150a61fa6ecc1151050e903492e16794999676
  summary: >-
    This introductory path shows embedded developers how to integrate Arm Virtual Hardware (AVH)
    into a GitHub Actions CI/CD workflow for automated testing and validation of bare‑metal Cortex‑M
    software. You will prepare a GitHub repository, generate and scope a Personal Access Token
    to update GitHub Actions workflows, and set up an AVH instance following the Arm Virtual Hardware
    install guide. The steps cover enabling Actions in your fork and creating a Linux x64 self‑hosted
    runner that matches your AWS instance. An AWS account and a GitHub account are required, and
    some familiarity with CI/CD concepts is assumed. By the end, you will have AVH wired into
    a GitHub Actions flow using a self‑hosted runner.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a GitHub account, an AWS account, and an Arm Virtual Hardware instance set up using
      the Arm Virtual Hardware install guide. Some familiarity with CI/CD concepts is assumed.
  - question: How do I create the required GitHub Personal Access Token?
    answer: >-
      In GitHub, go to Settings > Developer Settings > Personal access tokens, select Generate
      new token, and enable the permission to Update GitHub Action workflows. Generate and save
      the token locally for use during the setup.
  - question: How do I enable GitHub Actions in my forked repository?
    answer: >-
      Open your fork, navigate to Actions, and if workflows are disabled, click the prompt I understand
      my workflows, go ahead and enable them. This allows the repository’s workflows to run.
  - question: Which options should I choose when creating the self-hosted runner?
    answer: >-
      In the repository, go to Settings > Actions > Runners and create a New self-hosted runner
      with Runner image set to Linux and Architecture set to x64. These settings should match
      your AWS instance.
  - question: Where do I run the commands shown when adding the self-hosted runner?
    answer: >-
      Run the displayed registration commands on your AWS instance where Arm Virtual Hardware
      is set up. These commands connect that instance as the self-hosted runner for your repository.
# END generated_summary_faq

author: Pareena Verma

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

