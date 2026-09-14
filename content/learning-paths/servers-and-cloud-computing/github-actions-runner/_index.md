---
title: Use RunsOn to deploy managed, self-hosted Arm runners for GitHub Actions 
description: Learn how to install RunsOn self-hosted runner manager in your AWS account to execute GitHub Actions workflows on Arm runners.

minutes_to_complete: 15

who_is_this_for: This Learning Path is for developers who want to use Arm runners offered by AWS to execute GitHub Actions workflows.

learning_objectives:
    - Install RunsOn, a self-hosted runner manager, in your AWS account.
    - Execute GitHub Actions workflows on Arm runners.

prerequisites:
    - An [Amazon Web Services account](/learning-paths/servers-and-cloud-computing/csp/aws/)
    - A GitHub account (personal or organizational)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-10T22:06:17Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 966ea2cad187300a8768f94009ab1da042a8e51b48fcec32e646697d9265bc56
  summary_generated_at: '2026-09-10T22:06:17Z'
  summary_source_hash: 966ea2cad187300a8768f94009ab1da042a8e51b48fcec32e646697d9265bc56
  faq_generated_at: '2026-09-10T22:06:17Z'
  faq_source_hash: 966ea2cad187300a8768f94009ab1da042a8e51b48fcec32e646697d9265bc56
  summary: >-
    You'll deploy RunsOn in AWS with CloudFormation and use it to run GitHub Actions on Arm-based runners. First, you'll connect the AWS account, configure the GitHub app and license, and target an Arm64 runner with `runs-on`. RunsOn provisions a Graviton-based EC2 instance, so that you can verify an on-demand self-hosted runner.
  faqs:
  - question: How do I trigger a test workflow in a new repository?
    answer: >-
      Save the workflow as `test.yml` in the `.github/workflows/` directory, then add and commit the
      file. Push the commit to GitHub to trigger the GitHub Actions workflow.
  - question: Which AWS account or sub-account should I use to install RunsOn?
    answer: >-
      Sign in to the AWS account where you want to manage runners. For better isolation and security,
      install RunsOn in its own AWS sub-account if possible.
  - question: How do I modify my GitHub Actions workflow to use an Arm runner?
    answer: >-
      Update the `runs-on` section to request a RunsOn-managed Arm64 runner, for example:
      `runs-on: [self-hosted, runner=1cpu-linux-arm64, run-id=${{ github.run_id }}]`. This change
      instructs RunsOn to launch
      an Arm-based EC2 instance for the job.
  - question: What result should I expect to confirm that RunsOn is working?
    answer: >-
      After pushing a workflow with the updated `runs-on` value, the job should start in about 30
      seconds. In the Actions UI, the job runs on an Arm-based Amazon EC2 instance.
  - question: How do I customize the Arm runner's EC2 instance type?
    answer: >-
      Update the `runs-on` labels to select the required runner size, such as
      `runner=2cpu-linux-arm64`. Add a `family` label, such as `family=r8g`, when you want to select
      a specific Graviton family. Use the [RunsOn job-label documentation](https://runs-on.com/configuration/job-labels/)
      for additional CPU, memory, and disk customization options.
# END generated_summary_faq

author: Cyril Rohr

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

##### Tags
skilllevels: Introductory
subjects: CI-CD
platforms:
  - AWS Graviton

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
