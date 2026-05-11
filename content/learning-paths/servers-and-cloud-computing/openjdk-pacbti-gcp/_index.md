---
title: Verify OpenJDK PAC/BTI using a Google Cloud C4A VM

description: Learn how to verify PAC/BTI support in OpenJDK on a Google Cloud C4A Arm-based VM and interpret the JVM readiness result.

draft: true
cascade:
    draft: true
    
minutes_to_complete: 30

who_is_this_for: This Learning Path is for developers who want to validate OpenJDK PAC/BTI support on Google Cloud C4A Arm-based virtual machines.

learning_objectives: 
    - Provision a Google Cloud C4A Arm-based virtual machine with SUSE Linux Enterprise Server.
    - Install OpenJDK on the Arm-based VM.
    - Verify PAC/BTI readiness in the installed JVM runtime.

prerequisites:
    - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled

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
      title: Google Cloud documentation
      link: https://cloud.google.com/docs
      type: documentation
  - resource:
      title: OpenJDK build documentation
      link: https://openjdk.org/groups/build/doc/building.html
      type: documentation
  - resource:
      title: OpenJDK source repository
      link: https://github.com/openjdk/jdk
      type: documentation
  - resource:
      title: Arm "Arm64" machine instruction reference
      link: https://developer.arm.com/documentation/100076/latest/
      type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---