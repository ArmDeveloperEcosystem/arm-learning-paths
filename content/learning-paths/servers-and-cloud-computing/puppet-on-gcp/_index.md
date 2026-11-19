---
title: Deploy Puppet on Google Cloud C4A 

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers deploying and optimizing Puppet workloads on Arm Linux environments, specifically using Google Cloud C4A virtual machines powered by Axion processors. 

learning_objectives:
  - Provision an Arm-based SUSE SLES (SUSE Linux Enterprise Server) virtual machine (VM) on Google Cloud C4A with Axion processors.
  - Install Puppet on a SUSE Arm64 C4A instance.
  - Verify Puppet by applying a test manifest and confirming successful resource creation on Arm64.
  - Benchmark Puppet by measuring catalog compile time, apply speed, and resource usage on Arm64.

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled  
  - Basic familiarity with [Puppet](https://www.puppet.com/)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-19T15:57:44Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: ed729f599b63ca1094a46c3e2623e876345f833c37bc265a985acc718df8ffde
  summary_generated_at: '2026-11-19T15:57:44Z'
  summary_source_hash: ed729f599b63ca1094a46c3e2623e876345f833c37bc265a985acc718df8ffde
  faq_generated_at: '2026-11-19T15:57:44Z'
  faq_source_hash: ed729f599b63ca1094a46c3e2623e876345f833c37bc265a985acc718df8ffde
  summary: >-
    You'll install and validate Puppet on a Google Axion C4A VM running SUSE Linux. After
    provisioning a `c4a-standard-4` instance, you'll install dependencies and build Ruby before
    installing Puppet. You'll then check Puppet and Facter versions, apply a test manifest, and
    inspect the created resource. Finally, you'll run a standalone benchmark to measure local
    catalog compilation and apply performance.
  faqs:
  - question: Which machine type and image should I select?
    answer: >-
      Choose `c4a-standard-4` and a SUSE Linux Enterprise Server arm64 image.
  - question: Which command do I use to run the standalone Puppet benchmark?
    answer: >-
      Run `time puppet apply benchmark.pp --verbose` from `~/puppet-benchmark`.
      You can review the catalog compilation and elapsed time in the output.
  - question: How do I verify Puppet and Facter before applying a manifest?
    answer: >-
      Run `puppet --version` and `facter --version`. You should see a version from each
      command.
  - question: How do I verify that the test manifest worked?
    answer: >-
      Apply the manifest, then run `cat /tmp/puppet_test.txt` to inspect the file that it creates.
      You can also review the Puppet resource change output.
  - question: Where do I put the benchmark manifest?
    answer: >-
      Create `~/puppet-benchmark` and place the provided manifest there. You can then run the
      benchmark and record its catalog compile time, apply speed, and resource usage.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

##### Tags
skilllevels: Introductory
subjects: Performance and Architecture
platforms:
  - Google Axion

armips:
  - Neoverse

tools_software_languages:
  - Puppet
  - Ruby
  - Facter
  - Hiera

operatingsystems:
  - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
  - resource:
      title: Google Cloud documentation
      link: https://cloud.google.com/docs
      type: documentation

  - resource:
      title: Puppet documentation
      link: https://www.puppet.com/docs/index.html
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

