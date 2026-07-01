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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-30T21:43:42Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 55b8032ceaf735d53b1157102a3a1da5aa5cb686e9ec51cf4896ded66d9bf263
  summary_generated_at: '2026-06-30T21:43:42Z'
  summary_source_hash: 55b8032ceaf735d53b1157102a3a1da5aa5cb686e9ec51cf4896ded66d9bf263
  faq_generated_at: '2026-06-30T21:43:42Z'
  faq_source_hash: 55b8032ceaf735d53b1157102a3a1da5aa5cb686e9ec51cf4896ded66d9bf263
  summary: >-
    You'll deploy Veraison on AWS to serve as the Verifier
    in the RATS (RFC9334) model for Arm CCA attestation. After preparing an AWS account and authenticating,
    you'll create a Route53 domain and an HTTPS certificate so the Veraison REST APIs can be
    published on the internet. You'll deploy from the Veraison GitHub repository and
    use a bootstrap process to clone sources and set up the build environment. With the services running, you'll provision CCA
    platform endorsements using the Linaro endorsement tool so Veraison can verify CCA attestation
    tokens.
  faqs:
  - question: What should I have in place on AWS before starting the deployment?
    answer: >-
      Use an active AWS account with administrator-level privileges and install the AWS CLI. Set
      up authentication in your local environment following the AWS documentation before proceeding.
  - question: Why do I need a Route53 domain and a certificate for this deployment?
    answer: >-
      The Veraison services are published on the internet and accessed over HTTPS using RESTful
      APIs. A Route53-managed domain and a valid certificate allow clients to reliably reach the
      services via DNS and establish secure connections.
  - question: How do I begin the automated Veraison deployment and how long will it take?
    answer: >-
      Start with the Bootstrap process from the Veraison GitHub repository to clone the source
      and set up the build environment, which also installs required dependencies. The AWS resource
      creation typically takes 30 to 60 minutes.
  - question: Where do I get the tool to add CCA platform endorsements?
    answer: >-
      Clone the Linaro endorsement tool from the Linaro Git server using: `git clone https://git.codelinaro.org/linaro/dcap/cca-demos/poc-endorser`.
      Configure the tool for AWS as described in the steps to provide the CCA platform endorsements
      to Veraison.
  - question: What indicates the verifier is ready to handle CCA tokens after deployment?
    answer: >-
      After the Veraison services are running and CCA platform endorsements have been provisioned,
      the deployment is set up for CCA attestation verification. The services are exposed via
      HTTPS on your configured domain.
# END generated_summary_faq

author: Paul Howard

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

