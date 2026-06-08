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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:35:23Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 828e4022f387698d2736d94010de5d93efa9f38ffd3a2e4f15252410e9ccedb2
  summary_generated_at: '2026-06-01T22:22:06Z'
  summary_source_hash: 828e4022f387698d2736d94010de5d93efa9f38ffd3a2e4f15252410e9ccedb2
  faq_generated_at: '2026-06-02T23:35:23Z'
  faq_source_hash: 828e4022f387698d2736d94010de5d93efa9f38ffd3a2e4f15252410e9ccedb2
  summary: >-
    Set up a GitHub self-hosted runner on a Windows on Arm machine or cloud instance and run a
    minimal GitHub Actions workflow to validate a basic CI/CD flow on this platform. You will
    create a new GitHub repository, configure the runner on Windows on Arm, and use the Actions
    Simple workflow to generate a minimal blank.yml under .github/workflows (optionally renamed,
    for example to hello.yml) that executes a hello world command on the Windows Arm VM. Prerequisites
    are a valid GitHub account, a Microsoft Azure account if you use a virtual machine, and some
    familiarity with CI/CD concepts. This introductory path is intended for developers interested
    in running CI on Windows on Arm and can be completed in about 30 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a valid GitHub account and some familiarity with CI/CD concepts. If you plan to
      use a virtual machine, you also need a Microsoft Azure account.
  - question: Can I use a virtual machine instead of physical Windows on Arm hardware?
    answer: >-
      Yes. You can use a cloud instance as the Windows on Arm host; if you choose a virtual machine,
      an Azure account is required.
  - question: How do I create the repository used for testing the workflow?
    answer: >-
      Log in to GitHub in your browser, select New to create a repository, give it a name, and
      click Create Repository. This repo will host the workflow you run on the Windows on Arm
      runner.
  - question: How do I set up the Windows on Arm self-hosted runner, and what does it do?
    answer: >-
      Follow the path’s runner preparation steps to configure a GitHub self-hosted runner on your
      Windows on Arm machine or cloud instance. The runner is the machine that executes your GitHub
      Actions jobs.
  - question: How do I create and run the sample GitHub Actions workflow, and what file should
      I expect?
    answer: >-
      In your repository, select Actions, choose the Simple workflow option, and click Configure.
      GitHub creates .github/workflows/blank.yml, which you can optionally rename (for example,
      hello.yml); this minimal workflow runs a hello world command to validate the setup.
# END generated_summary_faq

author: Pareena Verma

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

