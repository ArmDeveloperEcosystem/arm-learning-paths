---
title: Validate PAC/BTI security features in OpenJDK on Google Cloud C4A

description: Test Pointer Authentication (PAC) and Branch Target Identification (BTI) support in OpenJDK on Google Cloud C4A. Learn to validate hardware security capabilities and verify JVM compiler support for Arm security features.
    
minutes_to_complete: 30

who_is_this_for: This is for Java developers running OpenJDK on Arm Neoverse platforms who want to verify PAC/BTI security features are properly enabled. Pointer Authentication (PAC) cryptographically signs return addresses to detect tampering, while Branch Target Identification (BTI) restricts where indirect branches can land. You'll learn to test both hardware capabilities and JVM compiler support for these Armv9 security features.

learning_objectives: 
    - Provision a Google Cloud C4A Arm-based virtual machine with SUSE Linux Enterprise Server.
    - Install OpenJDK on the Arm-based VM.
    - Verify PAC/BTI readiness in the installed JVM runtime.

prerequisites:
    - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
    - Optionally, [install the gcloud CLI](/install-guides/gcloud/) to connect to the VM from a local terminal instead of using the browser-based SSH

author: Doug Anson

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
  - Google Cloud

armips:
    - Neoverse

tools_software_languages:
    - Java
    - OpenJDK
    - Bash

operatingsystems:
    - Linux

further_reading:
  - resource:
      title: Understand Arm Pointer Authentication
      link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/pac/
      type: website
  - resource:
      title: Google Axion C4A machine series
      link: https://cloud.google.com/compute/docs/general-purpose-machines#c4a_series
      type: documentation
  - resource:
      title: OpenJDK 17 project page
      link: https://openjdk.org/projects/jdk/17/
      type: documentation
  - resource:
      title: Arm A64 instruction set architecture reference
      link: https://developer.arm.com/documentation/100076/latest/
      type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---