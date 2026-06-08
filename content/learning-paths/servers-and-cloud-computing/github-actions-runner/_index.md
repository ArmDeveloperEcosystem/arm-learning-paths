---
title: Managed, self-hosted Arm runners for GitHub Actions
description: Learn how to install RunsOn self-hosted runner manager in your AWS account to execute GitHub Actions workflows on Arm runners.
 
minutes_to_complete: 15

who_is_this_for: This Learning Path is for developers who want to use Arm runners offered by AWS to execute GitHub Actions workflows.

learning_objectives:
    - Install RunsOn, a self-hosted runner manager, in your AWS account.
    - Execute GitHub Actions workflows on Arm runners.

prerequisites:
    - An [Amazon Web Services account](/learning-paths/servers-and-cloud-computing/csp/aws/).
    - A GitHub account (personal or organizational).

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:02:59Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: cc72ef1fe1fde9f4f9ea0769c0e04d749731b8073b2efc0e65d7f608665abc2d
  summary_generated_at: '2026-06-02T04:01:04Z'
  summary_source_hash: cc72ef1fe1fde9f4f9ea0769c0e04d749731b8073b2efc0e65d7f608665abc2d
  faq_generated_at: '2026-06-03T01:02:59Z'
  faq_source_hash: cc72ef1fe1fde9f4f9ea0769c0e04d749731b8073b2efc0e65d7f608665abc2d
  summary: >-
    This Learning Path shows how to install RunsOn, a self-hosted runner manager, in your AWS
    account to run GitHub Actions on Arm-based AWS EC2 instances. You will set up RunsOn using
    AWS CloudFormation and a GitHub App, then modify your workflow files to target Arm runners,
    including AWS Graviton instances based on Arm Neoverse processors. The steps highlight account
    setup, installation flow, and the minimal workflow changes needed to launch Arm runners, which
    typically come online in under 30 seconds. Prerequisites are an AWS account and a GitHub account.
    The path is introductory and designed to be completed in about 15 minutes on Linux.
  faqs:
  - question: What do I need before running the installation?
    answer: >-
      You need an AWS account and a GitHub account. It is best to install RunsOn in its own AWS
      sub-account for isolation and security.
  - question: How do I install RunsOn in my AWS account?
    answer: >-
      Log in to the AWS console for the target account, then follow the official RunsOn installation
      guide to create the CloudFormation stack and the GitHub app. Use the link at the top of
      the guide to obtain your license key before proceeding.
  - question: Which EC2 instance types and Arm processors can I use for runners?
    answer: >-
      You can select any instance types offered by AWS, including Arm instances with AWS Graviton
      processors. With Graviton, you can run on Neoverse N1, Neoverse V1, and Neoverse V2 processors.
  - question: How do I change my GitHub Actions workflow to target an Arm runner?
    answer: >-
      Edit the runs-on setting in your workflow file. For example, replace runs-on: ubuntu-22.04
      with runs-on entries that include runner=1cpu-linux-arm64 and run-id=${{ github.run_id }}
      to invoke a new Arm runner in your AWS account.
  - question: What outcome and timing should I expect after triggering a workflow?
    answer: >-
      After installation, new runners launch in less than 30 seconds and your job should start
      shortly. The runner will be an AWS EC2 Arm instance with 1 vCPU running Ubuntu 22.04.
# END generated_summary_faq

author: Cyril Rohr

##### Tags
skilllevels: Introductory
subjects: CI-CD
cloud_service_providers:
  - AWS

armips:
    - Neoverse

tools_software_languages:
    - AWS Cloud Formation
    - GitHub
    - AWS EC2

operatingsystems:
    - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
    - resource:
        title: RunsOn official website and documentation
        link: https://runs-on.com/
        type: documentation

    - resource:
        title: RunsOn installation guide
        link: https://runs-on.com/guides/install/
        type: documentation

    - resource:
        title: GitHub Actions runners benchmark for Arm
        link: https://runs-on.com/benchmarks/github-actions-runners/#arm64-runners
        type: website


weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

