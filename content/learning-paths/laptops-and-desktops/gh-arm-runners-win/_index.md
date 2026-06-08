---
title: Automate Windows on Arm Builds with GitHub Arm-hosted Runners

description: Learn how to automate Windows application builds on Arm architecture using GitHub Arm-hosted runners and GitHub Actions workflows.

minutes_to_complete: 20

who_is_this_for: This introductory tutorial is for software developers looking to automate Windows application builds on Arm architecture using GitHub Actions.

learning_objectives:
    - Describe GitHub Arm-hosted Windows runners.
    - Configure workflows to run on Arm-hosted runners.
    - Automate Windows application builds with GitHub Actions.

prerequisites: 
    - A GitHub account. 
    - Familiarity with GitHub Actions.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:06:25Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 7e108d774eb0fd0b2b72fa8b5d65e1efec0ff4ecf3d80d4e511e82cdf3862284
  summary_generated_at: '2026-06-01T22:05:42Z'
  summary_source_hash: 7e108d774eb0fd0b2b72fa8b5d65e1efec0ff4ecf3d80d4e511e82cdf3862284
  faq_generated_at: '2026-06-02T23:06:25Z'
  faq_source_hash: 7e108d774eb0fd0b2b72fa8b5d65e1efec0ff4ecf3d80d4e511e82cdf3862284
  summary: >-
    This introductory Learning Path shows how to automate Windows application builds on Arm architecture
    using GitHub Arm-hosted runners and GitHub Actions. You will learn what Arm-hosted Windows
    runners are, how to target them in your workflows, and how to automate builds for a sample
    rotating 3D cube application that is also used in the Optimize Windows applications using
    Arm Performance Libraries Learning Path. The steps emphasize running CI on Arm hardware without
    operating your own infrastructure and introduce options for configuring a larger runner if
    required. Prerequisites are a GitHub account and familiarity with GitHub Actions. Estimated
    time to complete is about 20 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a GitHub account and familiarity with GitHub Actions. No other explicit prerequisites
      are listed.
  - question: How do I target a GitHub Arm-hosted Windows runner in my workflow?
    answer: >-
      Configure your GitHub Actions workflow to run on the Arm-hosted Windows runner as described
      in the path steps. The workflow will then execute on Arm architecture without additional
      infrastructure.
  - question: Do I need to provide my own server or a self-hosted runner?
    answer: >-
      No. An Arm-hosted runner is managed by GitHub, so you do not need to provide or manage a
      server to run your Actions workflows.
  - question: Which application is used as the example, and where are the detailed build instructions?
    answer: >-
      The example is a rotating 3D cube application used in the “Optimize Windows applications
      using Arm Performance Libraries” Learning Path. This path provides a basic overview; see
      the referenced Learning Path for detailed build instructions.
  - question: Can I configure a larger runner if my build needs more resources?
    answer: >-
      Yes. The introduction covers how to configure your own larger runner.
# END generated_summary_faq

author: 
    - Pareena Verma

### Tags
skilllevels: Introductory
subjects: CI-CD
armips:
    - Cortex-A
operatingsystems:
    - Windows
tools_software_languages:
    - GitHub
    - Visual Studio
    - MSBuild
    - Arm Performance Libraries

further_reading:
    - resource:
        title: GitHub Actions Partner Images Repository
        link: https://github.com/actions/partner-runner-images/
        type: documentation
    - resource:
        title: GitHub Actions now supports Windows on Arm runners for all public repos
        link: https://blogs.windows.com/windowsdeveloper/2025/04/14/github-actions-now-supports-windows-on-arm-runners-for-all-public-repos/
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

