---
title: Verify OpenJDK PAC/BTI on Google Cloud C4A
description: Validate PAC/BTI support in OpenJDK on a Google Cloud C4A Arm-based VM and interpret JVM security readiness.

minutes_to_complete: 30

who_is_this_for: This Learning Path is for developers who want to validate OpenJDK PAC/BTI support on Google Cloud C4A Arm-based virtual machines.

learning_objectives: 
    - Provision a Google Cloud C4A Arm-based virtual machine with SUSE Linux Enterprise Server.
    - Install OpenJDK on the Arm-based VM.
    - Verify PAC/BTI readiness in the installed JVM runtime.

prerequisites:
    - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
    - Optionally, [install the gcloud CLI](/install-guides/gcloud/) to connect to the VM from a local terminal instead of using the browser-based SSH

author:
    - Doug Anson

##### Tags
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

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================

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

weight: 1                       
layout: "learningpathall"       
learning_path_main_page: "yes"  
---
