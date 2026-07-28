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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-28T16:17:49Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 7e108d774eb0fd0b2b72fa8b5d65e1efec0ff4ecf3d80d4e511e82cdf3862284
  summary_generated_at: '2026-07-28T16:17:49Z'
  summary_source_hash: 7e108d774eb0fd0b2b72fa8b5d65e1efec0ff4ecf3d80d4e511e82cdf3862284
  faq_generated_at: '2026-07-28T16:17:49Z'
  faq_source_hash: 7e108d774eb0fd0b2b72fa8b5d65e1efec0ff4ecf3d80d4e511e82cdf3862284
  summary: >-
    This Learning Path introduces GitHub Arm-hosted Windows runners and shows how to use them
    to automate a Windows application build with GitHub Actions. You configure a workflow to run
    on Arm-hosted infrastructure, understand how runners execute jobs, and make basic decisions
    about build tooling using Visual Studio or MSBuild based on the project. The path uses a rotating
    3D cube application as the build target and points to a related path for detailed build instructions
    and later optimization work. After completing the steps, you trigger a workflow, confirm it
    executed on an Arm-hosted Windows runner, review logs, and recognize the expected Windows
    build outputs.
  faqs:
  - question: How do I target an Arm-hosted Windows runner in my workflow?
    answer: >-
      Configure the job to run on a GitHub Arm-hosted Windows runner as described in the steps.
      Update the workflow so the job selects the Arm-hosted Windows environment instead of a different
      runner type.
  - question: How do I know the job actually ran on an Arm-hosted Windows runner?
    answer: >-
      Open the workflow run and check the job details, which list the runner that executed the
      job. The logs and summary page identify the runner environment so you can verify it used
      an Arm-hosted Windows runner.
  - question: Which build tool should I configure, Visual Studio or MSBuild?
    answer: >-
      Use the toolchain that matches the project’s existing build files. Follow the guidance for
      the rotating 3D cube application referenced in this path to choose the correct build step.
  - question: Where can I find the sample application and detailed build steps?
    answer: >-
      The rotating 3D cube application and its build instructions are provided in the Optimize
      Windows applications using Arm Performance Libraries Learning Path. Follow that resource
      when you need step-by-step build details.
  - question: What result should I expect after a successful workflow run?
    answer: >-
      The workflow shows a successful job status and the logs indicate a completed build. You
      should see the Windows build outputs for the sample application, and any configured artifacts
      appear on the run’s summary page.
# END generated_summary_faq

author: 
    - Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

