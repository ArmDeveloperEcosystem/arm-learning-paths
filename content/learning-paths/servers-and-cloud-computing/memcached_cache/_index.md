---
title: Deploy Memcached as a cache for MySQL and PostgreSQL on Arm-based servers

description: Deploy Memcached as a cache for MySQL and PostgreSQL on Arm servers

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for developers who want to use memcached as their in-memory key-value store.

learning_objectives:
- Deploy memcached as a cache for MySQL on AWS, Azure and GCP Arm based Instance
- Deploy memcached as a cache for PostgreSQL on AWS, Azure and GCP Arm based Instance

prerequisites:
- An Amazon Web Services (AWS) [account](https://aws.amazon.com/)
- An Azure portal [account](https://azure.microsoft.com/en-in/get-started/azure-portal)
- A Google Cloud [account](https://console.cloud.google.com/)
- A machine with [Terraform](/install-guides/terraform/), [AWS CLI](/install-guides/aws-cli), [Google Cloud CLI](/install-guides/gcloud), [Azure CLI](/install-guides/azure-cli), [AWS IAM authenticator](https://docs.aws.amazon.com/eks/latest/userguide/install-aws-iam-authenticator.html), and [Ansible](/install-guides/ansible/) installed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-28T19:47:31Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 949c6c4ad60a99b6a028f1fe184f80a683b40042b8a461ed539c7ae7fed217f1
  summary_generated_at: '2026-09-28T19:47:31Z'
  summary_source_hash: 949c6c4ad60a99b6a028f1fe184f80a683b40042b8a461ed539c7ae7fed217f1
  faq_generated_at: '2026-09-28T19:47:31Z'
  faq_source_hash: 949c6c4ad60a99b6a028f1fe184f80a683b40042b8a461ed539c7ae7fed217f1
  summary: >-
    You'll deploy Memcached as a cache for MySQL or PostgreSQL on Arm-based cloud servers. First, you'll use Terraform to provision a Linux
    instance on AWS Graviton, Azure Cobalt, or Google Axion. Then, you'll run the corresponding Ansible
    automation to install and configure Memcached. Successful Terraform and Ansible runs confirm
    that your cache is ready for the selected database.
  faqs:
  - question: Which cloud provider should I use for my database?
    answer: >-
      For MySQL, you can use AWS, Azure, or Google Cloud. For PostgreSQL, you can use AWS or Azure.
  - question: Do I need to edit the Ansible inventory file?
    answer: >-
      No. Terraform generates `/tmp/inventory` automatically. Use the file when you run `ansible-playbook
      playbook.yaml -i /tmp/inventory`.
  - question: Can I run Terraform and Ansible from any computer?
    answer: >-
      Yes. You can run Terraform and Ansible from any computer that has the prerequisite tools
      installed.
  - question: How do I know that the deployment succeeded?
    answer: >-
      Confirm that Terraform completes without errors and that the cloud instance appears in your
      account. Then, verify that Ansible finishes successfully after installing and configuring
      Memcached.
  - question: How do I remove the cloud resources after I finish?
    answer: >-
      Run `terraform destroy` to delete the resources created by your deployment.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

test_images:
- ubuntu:latest
test_link: https://github.com/armflorentlebeau/arm-learning-paths/actions/runs/4312122327
test_maintenance: true

### Tags
skilllevels: Advanced
subjects: Web
platforms:
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
armips:
- Neoverse
tools_software_languages:
- Memcached
- SQL
- MySQL
- PostgreSQL
operatingsystems:
- Linux

further_reading:
    - resource:
        title: Memcached Wiki
        link: https://github.com/memcached/memcached/wiki
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
