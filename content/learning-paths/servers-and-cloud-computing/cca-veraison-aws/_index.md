---
title: Build a CCA Attestation Service in AWS with Veraison

draft: true
cascade:
    draft: true

minutes_to_complete: 90

who_is_this_for: This Learning Path is for developers who understand the basics of CCA attestation and the Veraison project, and who wish to progress onto creating a more scalable deployment of a CCA attestation verifier service in the cloud.


learning_objectives:
    - Create an attestation service in the AWS cloud using components from the Veraison project.
    - Prepare the Veraison service to act as a verifier for Arm CCA attestation tokens by provisioning CCA platform endorsements.


prerequisites:
    - An [AWS account](/learning-paths/servers-and-cloud-computing/csp/aws/) for accessing AWS cloud services.
    - An x86 computer running Ubuntu or Arch Linux, which is authorised to use the AWS account. Other build environments might be possible, but will require the configuration of toolchains for cross-compilation.


author: Paul Howard

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Cortex-A
operatingsystems:
    - Linux
tools_software_languages:
    - CCA
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
