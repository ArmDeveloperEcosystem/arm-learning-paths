---
title: Run Java applications on Google Axion processors

minutes_to_complete: 20

description: Deploy and optimize Java applications on Google Cloud Axion processors by testing JDK versions and performance optimization flags.
who_is_this_for: This is an introductory topic for software developers who want to learn how to run their Java-based applications on Arm-based Google Axion processors in Google Cloud. Most Java applications will run on Axion with no changes needed, but there are optimizations that can help improve application performance on Axion.
learning_objectives: 
    - Create an Arm-based VM instance with Google Axion CPU.
    - Deploy a Java application on Axion.
    - Understand Arm performance for different JDK versions.
    - Test common performance optimization flags.

prerequisites:
    - A [Google Cloud](https://cloud.google.com/) account with access to Axion based instances (C4A)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-15T21:17:46Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 6a44ac216373b4d69cf72962caf6a255b06b062e2e665a11af9cd8638ec7be1c
  summary_generated_at: '2026-09-15T21:17:46Z'
  summary_source_hash: 6a44ac216373b4d69cf72962caf6a255b06b062e2e665a11af9cd8638ec7be1c
  faq_generated_at: '2026-09-15T21:17:46Z'
  faq_source_hash: 6a44ac216373b4d69cf72962caf6a255b06b062e2e665a11af9cd8638ec7be1c
  summary: >-
    You'll provision an Arm-based Google Axion VM with `gcloud`, install Java on Ubuntu 24.04,
    and deploy an example application called Spring Petclinic. First, you'll verify the runtime, drive load with JMeter and the
    included JMX plan, and experiment with JVM optimization flags. You can repeat the
    workload on an earlier-generation Arm-based instance to compare Java behavior on Axion’s Armv9
    Neoverse V2 CPU.
  faqs:
  - question: How do I connect to the instance to start installing Java?
    answer: >-
      Use the Google Cloud console SSH button for your VM. It opens a browser-based shell connected
      to the instance.
  - question: What output should I expect after installing Java?
    answer: >-
      Running `java -version` after installing Java should print an OpenJDK 21.x release similar to: `openjdk version "21.0.3"`
      `2024-04-16`. If the command isn't found, recheck that `default-jre` installed successfully.
  - question: Why should I open a new SSH terminal before running JMeter?
    answer: >-
      Running JMeter in a separate terminal avoids interrupting the Spring Petclinic process.
      Keep the terminal that started the application open so that the service stays available during
      the test.
  - question: Which test plan do I use with JMeter for Spring Petclinic?
    answer: >-
      Use the `.jmx` file provided in the `spring-petclinic` repository. The file defines a workload that
      exercises the application endpoints for the performance tests.
  - question: How should I compare configurations or instance generations fairly?
    answer: >-
      Keep the workload, application build, and test plan identical and change only one variable
      at a time, such as a JVM flag or instance type. Run the JMeter plan for each
      case and compare the resulting metrics.
# END generated_summary_faq

author: Joe Stech

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
