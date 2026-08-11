---
title: Implement CI/CD with Windows on Arm host

description: Get started with GitHub CI/CD development flow on a Windows on Arm machine (or virtual machine).

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers interested in running their CI flows on Windows on Arm machines.

learning_objectives: 
    - Setup a CI/CD flow with GitHub Actions to use Windows on Arm as the self-hosted runner host
    - Run a simple GitHub Actions workflow

prerequisites:
    - Some familiarity with CI/CD concepts is assumed
    - Valid GitHub account
    - Microsoft Azure account (if using virtual machine)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-11T16:25:57Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: cbf7645f312a08a1400d74f819be3655369d835d037ffff69aac29b2119df899
  summary_generated_at: '2026-08-11T16:25:57Z'
  summary_source_hash: cbf7645f312a08a1400d74f819be3655369d835d037ffff69aac29b2119df899
  faq_generated_at: '2026-08-11T16:25:57Z'
  faq_source_hash: cbf7645f312a08a1400d74f819be3655369d835d037ffff69aac29b2119df899
  summary: >-
    You'll configure a GitHub Actions CI/CD flow that runs on a Windows on Arm host. You'll create
    a fresh repository to isolate test changes, prepare a
    self-hosted runner on a Windows on Arm machine or cloud instance, and add a minimal workflow
    using the **Simple workflow** template. When executed, the GitHub Actions workflow runs a hello world task, providing
    a quick check that jobs execute on the self-hosted runner. You'll finish with a working
    pipeline anchored to a Windows on Arm environment that can support subsequent projects.
  faqs:
  - question: Why should I create a new GitHub repository for this exercise?
    answer: >-
      A new repository provides a clean space to test a simple hello world command with GitHub
      Actions without impacting existing code or workflows.
  - question: Which option should I choose in the repository to start the minimal workflow?
    answer: >-
      Select **Actions** in the repository and start with the **Simple workflow**, then select
      **Configure** to generate the starter file.
  - question: Where does GitHub create the workflow file, and can I rename it?
    answer: >-
      GitHub creates `blank.yml` under `<your-repo-name>/.github/workflows/`. You can optionally rename
      it to something more meaningful, such as `hello.yml`.
  - question: What result should I expect when the workflow runs successfully?
    answer: >-
      The run completes with the minimal steps executing, including the hello world command, and
      the job status shows **success**. This confirms the CI/CD workflow is operational on the Windows
      on Arm host.
  - question: Can I use a virtual machine instead of a physical Windows on Arm device?
    answer: >-
      Yes. You can host the runner on a Windows on Arm virtual machine or cloud instance.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: CI-CD
armips:
    - Neoverse
operatingsystems:
    - Windows
tools_software_languages:
    - GitHub

further_reading:
    - resource:
        title: GitHub Actions
        link: https://docs.github.com/en/actions
        type: documentation
    - resource:
        title: GitHub Actions self-hosted runners
        link: https://docs.github.com/en/actions/hosting-your-own-runners/about-self-hosted-runners
        type: documentation
    - resource:
        title: Continuous Integration for Windows on Arm
        link: https://azure.microsoft.com/en-us/blog/azure-virtual-machines-with-ampere-altra-arm-based-processors-generally-available/
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
