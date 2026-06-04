---
title: Deploy MySQL and WordPress on an always free tier Arm shape

minutes_to_complete: 30

prerequisites:
    - An OCI account
    - An Arm compute instance deployed on OCI with Oracle Linux

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:17:46Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 46f2645fb6ef298508af93569554315cfa2564be9891acabf1c874c94e52d70d
  summary_generated_at: '2026-06-02T05:27:17Z'
  summary_source_hash: 46f2645fb6ef298508af93569554315cfa2564be9891acabf1c874c94e52d70d
  faq_generated_at: '2026-06-03T02:17:46Z'
  faq_source_hash: 46f2645fb6ef298508af93569554315cfa2564be9891acabf1c874c94e52d70d
  summary: >-
    This introductory Learning Path shows how to install MySQL Community Server and WordPress
    on an Arm virtual machine running Oracle Linux in Oracle Cloud Infrastructure (OCI), targeting
    an always free tier Arm shape. You will follow practical steps to set up the database and
    application stack on an Arm (Ampere) compute instance. The path notes that an Arm instance
    can be deployed through the OCI Console or Terraform. Prerequisites are an OCI account and
    an Arm compute instance on OCI with Oracle Linux. On completion, you will have MySQL and WordPress
    installed on your OCI Arm server. The estimated time to complete is about 30 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an Oracle Cloud Infrastructure (OCI) account and an Arm compute instance deployed
      on OCI with Oracle Linux. The path suggests reviewing “Getting Started with Oracle OCI”
      if you want a quick orientation before you begin.
  - question: Which OCI shape and operating system should I use for the instance?
    answer: >-
      Use an always free tier Arm shape in OCI targeting an Arm (Ampere) compute instance. The
      prerequisite specifies Oracle Linux as the operating system.
  - question: How can I provision the Arm compute instance?
    answer: >-
      You can deploy the instance through the OCI Console or by using Terraform. The Learning
      Path supports either approach.
  - question: Which software will I install during this Learning Path?
    answer: >-
      You will install MySQL Community Server and WordPress on the Arm virtual machine. These
      are the only tools explicitly listed.
  - question: What result should I expect, and how long will it take?
    answer: >-
      Plan for about 30 minutes to complete. By the end, MySQL Community Server and WordPress
      will be installed on your Arm server running in OCI.
# END generated_summary_faq

author: Frédéric -lefred- Descamps

who_is_this_for: This is an introductory topic for developers who want to install WordPress on Oracle Cloud Infrastructure (OCI) using always free tier.

learning_objectives: 
    - Install MySQL and WordPress on an Arm server running in OCI

### Tags
skilllevels: Introductory
subjects: Databases
cloud_service_providers:
  - Oracle

armips:
    - Neoverse

operatingsystems:
    - Linux

tools_software_languages:
    - MySQL
    - WordPress


further_reading:
    - resource:
        title: Learn Faster to Grow Faster
        link: https://wordpress.com/learn/
        type: website
    - resource:
        title: Deploy Wordpress on OCI with Terraform
        link: https://blogs.oracle.com/mysql/post/wordpress-with-mysql-on-oci-always-free
        type: blog



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

