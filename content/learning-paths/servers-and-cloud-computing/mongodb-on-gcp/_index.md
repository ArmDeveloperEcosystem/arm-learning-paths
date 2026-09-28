---
title: Deploy MongoDB on an Arm-based Google Axion C4A VM

minutes_to_complete: 15

who_is_this_for: This introductory topic is for software developers who want to migrate MongoDB workloads from x86_64 to Arm-based platforms, specifically on Google Axion-based C4A virtual machines.

description: Deploy MongoDB on Google Cloud Axion C4A virtual machines and benchmark database performance with Yahoo Cloud Serving Benchmark (YCSB).

learning_objectives:
  - Create an Arm virtual machine on Google Cloud (C4A Axion family)
  - Install and run MongoDB on the Arm-based C4A instance
  - Benchmark MongoDB performance with Yahoo Cloud Serving Benchmark (YCSB)

prerequisites:
     - A [Google Cloud Platform (GCP)](https://cloud.google.com/free?utm_source=google&hl=en) account with billing enabled

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-28T19:52:41Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 07462f1137ad04b397ae04d075b5b5307ba23b8a621d19916bcfd38057400db9
  summary_generated_at: '2026-09-28T19:52:41Z'
  summary_source_hash: 07462f1137ad04b397ae04d075b5b5307ba23b8a621d19916bcfd38057400db9
  faq_generated_at: '2026-09-28T19:52:41Z'
  faq_source_hash: 07462f1137ad04b397ae04d075b5b5307ba23b8a621d19916bcfd38057400db9
  summary: >-
    Deploy and benchmark MongoDB on a Google Axion C4A virtual machine. You provision the VM in
    Google Cloud, install Arm64 MongoDB binaries on Red Hat Enterprise Linux, and validate local
    access with `mongosh`. You create a test database and exercise basic CRUD operations for a
    baseline. You then build Yahoo Cloud Serving Benchmark (YCSB), load its initial dataset, run
    workloads, and review the resulting output.
  faqs:
  - question: Which machine type should I select for the VM?
    answer: >-
      Select the C4A series and the `c4a-standard-4` machine type, which provides four vCPUs and
      16 GB of memory.
  - question: Which MongoDB binaries do I download for this VM?
    answer: >-
      Download the Arm64 (`aarch64`) MongoDB binaries for RHEL 9.3 and extract them on your C4A
      instance.
  - question: How do I verify that MongoDB is running locally?
    answer: >-
      Run `mongosh mongodb://127.0.0.1:27017`. A successful connection and `mongosh` prompt confirm
      that the server accepts local connections.
  - question: What quick baseline should I capture before running YCSB?
    answer: >-
      Use `mongosh` to create the `baselineDB` database and `test` collection. Perform the CRUD
      checks and record the insert timings shown by the commands.
  - question: What should I check after building YCSB?
    answer: >-
      Confirm that Maven builds the MongoDB binding without errors. Then run the load phase and
      verify that it inserts the default 1,000 records and prints results to the terminal.
# END generated_summary_faq

author: Annie Tallund

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

##### Tags
skilllevels: Introductory
subjects: Databases
platforms:
  - Google Axion

armips:
    - Neoverse

tools_software_languages:
  - MongoDB
  - YCSB

operatingsystems:
    - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
    - resource:
        title: MongoDB Manual
        link: https://www.mongodb.com/docs/manual/
        type: documentation
    - resource:
        title: MongoDB Performance Tool
        link: https://github.com/idealo/mongodb-performance-test#readme
        type: documentation
    - resource:
        title: YCSB
        link: https://github.com/brianfrankcooper/YCSB/wiki/
        type: documentation

weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
