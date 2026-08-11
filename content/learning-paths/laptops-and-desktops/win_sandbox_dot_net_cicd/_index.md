---
title: Deploy GitHub Actions workflows using Windows Sandbox

description: Learn how to configure Windows Sandbox as a self-hosted GitHub Actions runner to build and run .NET 8 WPF applications in CI/CD workflows.

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for software developers who are developing applications on Windows on Arm computers.

learning_objectives:
    - Configure Windows Sandbox as a self-hosted GitHub Actions runner.
    - Build and run a .NET 8 Windows Presentation Foundation (WPF) application using a self-hosted GitHub Actions runner in your CI/CD workflow. 

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 Version 22H2 which has [Windows Sandbox enabled](/install-guides/windows-sandbox-woa/).
    - A valid [GitHub account](https://github.com/) to complete this Learning Path.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-11T16:22:15Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 53127ee82aeebbb8df3feb552bc5b0e5200aeeed6d37f191ab2ce0888f3748ed
  summary_generated_at: '2026-08-11T16:22:15Z'
  summary_source_hash: 53127ee82aeebbb8df3feb552bc5b0e5200aeeed6d37f191ab2ce0888f3748ed
  faq_generated_at: '2026-08-11T16:22:15Z'
  faq_source_hash: 53127ee82aeebbb8df3feb552bc5b0e5200aeeed6d37f191ab2ce0888f3748ed
  summary: >-
    You'll configure Windows Sandbox on a Windows on Arm device as a self-hosted Arm64 GitHub Actions
    runner and use it to build and publish a .NET 8 Windows Presentation Foundation (WPF) sample
    that solves the Traveling Salesman Problem. First, you'll prepare the sandboxed
    environment, register it as a runner, and execute a CI/CD workflow defined in the repository
    to build and run the application. Then, you'll trigger the pipeline and verify that the job executes
    on the sandboxed runner. By the end, you'll be able to confirm successful builds and published
    outputs produced by the workflow configuration.
  faqs:
  - question: Where is the workflow defined and how is it triggered?
    answer: >-
      The workflow is defined at `.github/workflows/dotnet_sandbox.yml`. It triggers on pushes to
      the main branch and can also be started manually from the **Actions** tab.
  - question: How do I know the job ran on my Windows Sandbox self-hosted runner?
    answer: >-
      Open the workflow run details and check the job’s runner information. It should indicate
      that a self-hosted runner executed the job from your sandboxed environment.
  - question: What result should I expect when the .NET WPF build and run steps succeed?
    answer: >-
      The workflow run shows a success status, and the logs for the build and run steps complete
      without errors. If the workflow includes a publish step, you'll also see published outputs
      listed in the run summary.
  - question: What should I check if the workflow does not start after pushing?
    answer: >-
      Confirm you pushed to the main branch and that `.github/workflows/dotnet_sandbox.yml` exists
      in the repository. If needed, start the workflow manually from the **Actions** tab.
  - question: What do I need to confirm before configuring the self-hosted runner in Windows Sandbox?
    answer: >-
      Verify that Windows Sandbox is enabled on your Windows 11 device as described in the [Windows
      Sandbox install guide](/install-guides/windows-sandbox-woa/). This ensures the sandbox environment is available to register as
      a runner.
# END generated_summary_faq

author: Pareena Verma

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
    - dotnet
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
