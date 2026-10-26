---
title: Validate Pointer Authentication and Branch Target Identification in OpenJDK on Google Cloud C4A

description: Test Pointer Authentication (PAC) and Branch Target Identification (BTI) support in OpenJDK on Google Cloud C4A. Learn to validate hardware security capabilities and verify JVM compiler support for Arm security features.
    
minutes_to_complete: 30

who_is_this_for: This is for Java developers running OpenJDK on Arm Neoverse platforms who want to verify  Pointer Authentication (PAC) and Branch Target Identification (BTI) security features are properly enabled. PAC cryptographically signs return addresses to detect tampering, while BTI restricts where indirect branches can land. 

learning_objectives: 
    - Provision a Google Cloud C4A Arm-based virtual machine (VM) with SUSE Linux Enterprise Server.
    - Install OpenJDK on the Arm-based VM.
    - Verify PAC and BTI readiness in the installed Java VM (JVM) runtime.

prerequisites:
    - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
    - Optionally, [install the gcloud CLI](/install-guides/gcloud/) to connect to the VM from a local terminal instead of using the browser-based SSH

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-01T19:43:54Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 1e27a00bafb12e1648af702e7eadeefc15ceefb119b7e6eb3e4824787d547271
  summary_generated_at: '2026-10-01T19:43:54Z'
  summary_source_hash: 1e27a00bafb12e1648af702e7eadeefc15ceefb119b7e6eb3e4824787d547271
  faq_generated_at: '2026-10-01T19:43:54Z'
  faq_source_hash: 1e27a00bafb12e1648af702e7eadeefc15ceefb119b7e6eb3e4824787d547271
  summary: >-
    You'll validate PAC and BTI support in Java
    on a Google Axion C4A VM. First, you'll provision a SUSE Linux Enterprise Server VM and install
    OpenJDK. You'll run a script that checks platform capabilities and JVM
    just-in-time (JIT) compiler support. Then, you'll install Oracle JDK 21, repeat the tests, and
    compare how each runtime reports branch-protection support.
  faqs:
  - question: How do I verify which JVM is active after installation?
    answer: >-
      Run `java --version`. The output should identify the distribution and version, for example
      OpenJDK 17 on `aarch64`.
  - question: How do I know that the C4A VM exposes PAC and BTI?
    answer: >-
      Run the provided test script and review its hardware checks. It should report that PAC and
      BTI are available before you evaluate JVM compiler behavior.
  - question: What result should I expect from the SUSE OpenJDK 17 tests?
    answer: >-
      The tests confirm the platform exposes PAC and BTI, but the SUSE-packaged OpenJDK 17 JIT
      doesn't emit PAC and BTI instructions. This distinguishes hardware capability from the compiler’s
      code generation.
  - question: How do I ensure that the tests run against Oracle JDK 21?
    answer: >-
      Run `JAVA=./jdk-21.0.11/bin/java ./test-pacbti.sh` to select the Oracle JDK for the
      test script. Replace `jdk-21.0.11` with your extracted directory name if it differs.
  - question: Which C4A machine type should I use for this validation?
    answer: >-
      Use the `c4a-standard-4` machine type.
# END generated_summary_faq

author: Doug Anson

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
platforms:
  - Google Axion

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
