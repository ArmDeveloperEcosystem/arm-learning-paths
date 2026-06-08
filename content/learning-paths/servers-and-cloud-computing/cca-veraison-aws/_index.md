---
title: Build a CCA Attestation Service on AWS with Veraison
description: Learn how to deploy a scalable Arm CCA attestation verifier service on AWS using Veraison components with platform endorsement provisioning.

minutes_to_complete: 90

who_is_this_for: This Learning Path is for developers familiar with CCA attestation and the Veraison project. You'll learn how to deploy a scalable CCA attestation verifier service on AWS.

learning_objectives:
    - Build an attestation service on AWS using the Veraison project's components.
    - Set up Veraison as a verifier for Arm CCA attestation tokens by provisioning CCA platform endorsements.

prerequisites:
    - An [AWS account](/learning-paths/servers-and-cloud-computing/csp/aws/) with access to AWS services.
    - An x86 computer running Ubuntu or Arch Linux, authorized for AWS access. If you're using another build environment, you'll need to configure the toolchains for cross-compilation.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:32:36Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 55b8032ceaf735d53b1157102a3a1da5aa5cb686e9ec51cf4896ded66d9bf263
  summary_generated_at: '2026-06-02T03:21:13Z'
  summary_source_hash: 55b8032ceaf735d53b1157102a3a1da5aa5cb686e9ec51cf4896ded66d9bf263
  faq_generated_at: '2026-06-03T00:32:36Z'
  faq_source_hash: 55b8032ceaf735d53b1157102a3a1da5aa5cb686e9ec51cf4896ded66d9bf263
  summary: >-
    This advanced Learning Path shows how to build and deploy a scalable Arm CCA attestation verifier
    on AWS using Veraison. You will prepare your AWS account, install and authenticate the AWS
    CLI, create a public domain in Route 53 and an HTTPS certificate, then use Veraison’s bootstrap
    process to clone sources and launch an automated deployment that typically completes in 30–60
    minutes. After the services are online, you will provision Arm CCA platform endorsements using
    the Linaro endorsement tool so Veraison can verify CCA attestation tokens. The path targets
    Linux and assumes an active AWS account and an x86 machine running Ubuntu or Arch Linux; other
    build environments require cross-compilation setup.
  faqs:
  - question: What do I need before starting the deployment?
    answer: >-
      You need an AWS account with access to AWS services and an x86 computer running Ubuntu or
      Arch Linux that is authorized for AWS access. The path assumes administrator-level privileges
      for your AWS account.
  - question: How should I authenticate the AWS CLI before deploying Veraison?
    answer: >-
      Set up your local environment to authenticate with AWS before you begin the deployment.
      Follow the AWS documentation to install the latest AWS CLI and configure authentication.
  - question: Do I need a public domain, and how is it used?
    answer: >-
      Yes. You create a domain in Route53 because the Veraison services are published on the internet
      over HTTPS using RESTful APIs, and they need a domain to be accessible. You also create
      a certificate for the chosen domain.
  - question: What should I expect when running the Veraison deployment?
    answer: >-
      The process is highly automated and typically takes 30 to 60 minutes as several AWS resources
      are created. You start with a bootstrap step that clones the Veraison source from GitHub
      and sets up your build environment, including dependencies.
  - question: How do I add CCA platform endorsements so the verifier can process tokens?
    answer: >-
      Clone the Linaro endorsement tool from the provided Git server, configure it for AWS, and
      use it to provision the CCA platform endorsements. This enables the deployed Veraison services
      to act as a verifier for Arm CCA attestation tokens.
# END generated_summary_faq

author: Paul Howard

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
cloud_service_providers:
  - AWS
armips:
    - Neoverse
    - Cortex-A
operatingsystems:
    - Linux
tools_software_languages:
    - CCA
    - RME
    - Runbook

further_reading:
    - resource:
        title: RATS architecture (RFC 9334) 
        link: https://datatracker.ietf.org/doc/rfc9334/
        type: documentation
    - resource:
        title: The Realm Management Monitor Specification
        link: https://developer.arm.com/documentation/den0137/latest/
        type: documentation
    - resource:
        title: The Attestation Results for Secure Interactions (AR4SI) 
        link: https://datatracker.ietf.org/doc/draft-ietf-rats-ar4si/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

