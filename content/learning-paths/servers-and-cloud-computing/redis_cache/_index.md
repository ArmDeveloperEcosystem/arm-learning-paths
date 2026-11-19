---
title: Deploy Redis as a cache for MySQL and PostgreSQL on Arm servers

minutes_to_complete: 90   

who_is_this_for: This is an advanced topic for developers who want to deploy Redis as a cache on Arm-based virtual machines (VMs).

learning_objectives: 
    - Deploy Redis as a cache for MySQL on AWS, Azure and GCP Arm based instance.
    - Deploy Redis as a cache for Postgres on AWS, Azure and GCP Arm based instance.

prerequisites:
    - An Amazon Web Services (AWS) [account](https://aws.amazon.com/)
    - An Azure portal [account](https://azure.microsoft.com/en-in/get-started/azure-portal)
    - A Google Cloud [account](https://console.cloud.google.com/)
    - A machine with [Terraform](/install-guides/terraform/), [AWS CLI](/install-guides/aws-cli), [Google Cloud CLI](/install-guides/gcloud), [Azure CLI](/install-guides/azure-cli), [AWS IAM authenticator](https://docs.aws.amazon.com/eks/latest/userguide/install-aws-iam-authenticator.html), and [Ansible](/install-guides/ansible/) installed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-19T16:04:26Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: ea2a08e991d4de8363d55711b8f0984b977c395cee4840e31524cad2973e613f
  summary_generated_at: '2026-11-19T16:04:26Z'
  summary_source_hash: ea2a08e991d4de8363d55711b8f0984b977c395cee4840e31524cad2973e613f
  faq_generated_at: '2026-11-19T16:04:26Z'
  faq_source_hash: ea2a08e991d4de8363d55711b8f0984b977c395cee4840e31524cad2973e613f
  summary: >-
    You'll deploy Redis as a cache for MySQL or PostgreSQL on Arm-based AWS, Microsoft Azure, and Google Cloud VMs. You'll use
    Terraform to provision infrastructure and Ansible to configure Redis with the selected
    database. Finally, you'll run the example application for your provider and database pairing
    to check cached data access.
  faqs:
  - question: How do I confirm that a query result came from Redis?
    answer: >-
      Run the example Python query twice with the same key. On the first run, you should see
      a message that Redis was updated. On the second, look for `Loaded data from redis`.
  - question: How do I check that the provisioned virtual machine uses Arm?
    answer: >-
      Check the instance type shown by the cloud provider after provisioning. You should see
      the Arm-based family selected in the corresponding section.
  - question: How do I configure the database after provisioning the virtual machines?
    answer: >-
      After using `terraform apply` to create the instances, run
      `ansible-playbook playbook.yaml -i /tmp/inventory` to install and configure MySQL or
      PostgreSQL.
  - question: Can I cache PostgreSQL queries on Google Cloud?
    answer: >-
      Yes. Follow `redis_psql_gcp.md` to provision the Google Cloud environment and configure
      Redis as a cache for PostgreSQL.
  - question: How long do the examples keep a query result in Redis?
    answer: >-
      You get a cached result for up to 120 seconds. The example Python scripts set that
      expiration when they store a database query result in Redis.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Databases
platforms:
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Terraform
    - Ansible
    - Redis
    - SQL
    - MySQL
    - Runbook

further_reading:
    - resource:
        title: Redis documentation
        link: https://redis.io/docs/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

