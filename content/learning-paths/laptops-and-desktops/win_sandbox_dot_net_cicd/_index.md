---
title: Deploy GitHub Actions workflows using Windows Sandbox

description: Learn how to configure Windows Sandbox as a self-hosted GitHub Actions runner to build and run .NET 8 WPF applications in CI/CD workflows.

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for software developers who are developing applications on Windows on Arm computers.

learning_objectives:
    - Configure Windows Sandbox as a self-hosted GitHub Actions runner.
    - Build and run a .NET 8 Windows Presentation Foundation (WPF) application using a self-hosted GitHub Actions runner in your CI/CD workflow. 

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 Version 22H2 which has [Windows Sandbox enabled](/install-guides/windows-sandbox-woa).
    - A valid [GitHub account](https://github.com/) to complete this Learning Path.
    

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:31:07Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 055e3a3d8c0dc717e2246e3e8e7ebb00c7d2cea3ff9faabf7125ca1ebfff7a31
  summary_generated_at: '2026-06-01T22:19:03Z'
  summary_source_hash: 055e3a3d8c0dc717e2246e3e8e7ebb00c7d2cea3ff9faabf7125ca1ebfff7a31
  faq_generated_at: '2026-06-02T23:31:07Z'
  faq_source_hash: 055e3a3d8c0dc717e2246e3e8e7ebb00c7d2cea3ff9faabf7125ca1ebfff7a31
  summary: >-
    This Learning Path shows how to use Windows Sandbox on a Windows on Arm PC as a self-hosted
    Arm64 GitHub Actions runner, then run a CI/CD workflow that builds and runs a .NET 8 Windows
    Presentation Foundation (WPF) sample solving the Traveling Salesman Problem. You will configure
    the sandboxed runner and use the workflow definition in .github/workflows/dotnet_sandbox.yml
    to trigger builds manually or on pushes to the main branch. The focus is on getting a working
    pipeline that executes inside Windows Sandbox. Prerequisites are a Windows on Arm computer
    (for example, a Lenovo ThinkPad X13s) running Windows 11 Version 22H2 with Windows Sandbox
    enabled, and a GitHub account.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 Version
      22H2 with Windows Sandbox enabled, and a valid GitHub account. Follow the Windows Sandbox
      enablement guide linked in the prerequisites.
  - question: Which GitHub Actions runner is configured in this Learning Path?
    answer: >-
      You will configure a self-hosted Arm64 runner inside Windows Sandbox on your Windows on
      Arm machine. This runner executes the jobs defined in your workflow.
  - question: Where is the workflow file located and how is it triggered?
    answer: >-
      The workflow is defined in .github/workflows/dotnet_sandbox.yml. It runs on push events
      to the main branch and can also be triggered manually from the Actions tab.
  - question: What result should I expect when I run the pipeline?
    answer: >-
      The pipeline builds a .NET 8 WPF sample application and verifies it runs on your Windows
      Sandbox self-hosted runner. The workflow should complete successfully with jobs executed
      on the self-hosted Arm64 runner, and it may publish the app as configured.
  - question: What should I check if my jobs are queued and do not run in Windows Sandbox?
    answer: >-
      Confirm Windows Sandbox is enabled and that you have configured and started the self-hosted
      runner in the Sandbox as described in the steps. Also ensure the repository contains .github/workflows/dotnet_sandbox.yml
      and you triggered the workflow as specified.
# END generated_summary_faq

author: Pareena Verma

### Tags
skilllevels: Introductory
subjects: CI-CD
armips:
    - Cortex-A
operatingsystems:
    - Windows
tools_software_languages:
    - .NET
    - Visual Studio
    - Windows Sandbox

further_reading:
    - resource:
        title: Windows Sandbox Documentation
        link: https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview
        type: documentation
    - resource:
        title: GitHub Actions support Windows Arm Hardware
        link: https://github.blog/changelog/2022-09-28-github-actions-self-hosted-runners-now-support-windows-arm-hardware/
        type: blog


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

