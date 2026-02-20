---
title: Build a CCA Attestation Service on AWS with Veraison

minutes_to_complete: 90

who_is_this_for: This Learning Path is for developers familiar with CCA attestation and the Veraison project. You'll learn how to deploy a scalable CCA attestation verifier service on AWS.

learning_objectives:
    - Build an attestation service on AWS using the Veraison project's components.
    - Set up Veraison as a verifier for Arm CCA attestation tokens by provisioning CCA platform endorsements.

prerequisites:
    - An [AWS account](/learning-paths/servers-and-cloud-computing/csp/aws/) with access to AWS services.
    - An x86 computer running Ubuntu or Arch Linux, authorized for AWS access. If you're using another build environment, you'll need to configure the toolchains for cross-compilation.

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
