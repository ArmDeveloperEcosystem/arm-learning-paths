---
title: Run Java applications on Google Axion processors

minutes_to_complete: 20

description: Deploy and optimize Java applications on Google Cloud Axion processors by testing JDK versions and performance optimization flags.
who_is_this_for: This is an introductory topic for software developers who want to learn how to run their Java-based applications on Arm-based Google Axion processors in Google Cloud. Most Java applications will run on Axion with no changes needed, but there are optimizations that can help improve application performance on Axion.
learning_objectives: 
    - Create an Arm-based VM instance with Google Axion CPU
    - Deploy a Java application on Axion
    - Understand Arm performance for different JDK versions
    - Test common performance optimization flags

prerequisites:
    - A [Google Cloud](https://cloud.google.com/) account with access to Axion based instances (C4A).

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:12:09Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e6f73fbca45a1be1644f79bbcfbaaec964e31f1aab236e9a872c72a6fd5e4b66
  summary_generated_at: '2026-06-02T04:09:25Z'
  summary_source_hash: e6f73fbca45a1be1644f79bbcfbaaec964e31f1aab236e9a872c72a6fd5e4b66
  faq_generated_at: '2026-06-03T01:12:09Z'
  faq_source_hash: e6f73fbca45a1be1644f79bbcfbaaec964e31f1aab236e9a872c72a6fd5e4b66
  summary: >-
    Learn how to deploy and evaluate a Java workload on Google Cloud Axion instances built on
    Armv9 Neoverse V2. You will create an Arm-based VM using the gcloud CLI, install Java on Ubuntu
    24.04, and build and deploy the Spring Petclinic application. The path then uses jmeter (with
    a provided JMX file) to exercise the application, compare JDK versions, and test common JVM
    performance optimization flags. You can also compare Axion results with previous-generation
    Google Cloud Arm instances. This introductory path targets developers running Java on Arm
    in Google Cloud. Prerequisite: a Google Cloud account with access to Axion-based (C4A) instances.
  faqs:
  - question: What do I need before creating the VM?
    answer: >-
      You need a Google Cloud account with access to Axion-based instances (C4A). No other explicit
      prerequisites are listed.
  - question: Which method should I use to create the Axion VM?
    answer: >-
      There are multiple options: Google Cloud console, the gcloud CLI, or Infrastructure as Code.
      This guide uses the gcloud CLI.
  - question: How do I connect to the instance, and which OS is used?
    answer: >-
      Use the Google Cloud console’s SSH button to open a shell to the VM. The guide uses an Ubuntu
      24.04 image on the Axion instance.
  - question: Which Java package should I install and how do I verify it?
    answer: >-
      Install the default JRE using apt and verify with java -version. The example output shows
      an OpenJDK 21.x release.
  - question: What application and tool are used for performance testing, and how should I run
      the tests?
    answer: >-
      You deploy the Spring Petclinic application and test it with jmeter using the JMX file in
      the spring-petclinic repo. Open a new SSH terminal so the running application is not interrupted,
      then compare results across JDK versions and common JVM flags; comparing Axion to previous-generation
      Arm instances is optional.
# END generated_summary_faq

author: Joe Stech

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
  - Google Cloud
armips:
    - Neoverse V2
tools_software_languages:
    - Java
    - Google Axion
    - Runbook

operatingsystems:
    - Linux


further_reading:
    - resource:
        title: Exploring JVM Tuning Flags
        link: https://www.baeldung.com/jvm-tuning-flags
        type: blog
    - resource:
        title: The java Command 
        link: https://docs.oracle.com/en/java/javase/21/docs/specs/man/java.html
        type: blog



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

