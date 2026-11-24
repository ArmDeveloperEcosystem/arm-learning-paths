---
title: Deploy Spark on AWS Graviton2

minutes_to_complete: 60   

who_is_this_for: This is an advanced topic for anyone who wants to deploy Spark on AWS Graviton2.

learning_objectives: 
    - Automate Spark EC2 instance creation using Terraform and Ansible.
    - Deploy a single instance of Spark on AWS Graviton2. 

prerequisites:
    - An Amazon Web Services (AWS) [account](https://aws.amazon.com/)
    - A machine with [Terraform](/install-guides/terraform/), [AWS CLI](/install-guides/aws-cli/), [AWS IAM authenticator](https://docs.aws.amazon.com/eks/latest/userguide/install-aws-iam-authenticator.html), and [Ansible](/install-guides/ansible/) installed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-23T21:01:27Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 4a960d8d932b33ff534ad4884bb252ae5afb2b68910b2a2cb9edb998499738da
  summary_generated_at: '2026-11-23T21:01:27Z'
  summary_source_hash: 4a960d8d932b33ff534ad4884bb252ae5afb2b68910b2a2cb9edb998499738da
  faq_generated_at: '2026-11-23T21:01:27Z'
  faq_source_hash: 4a960d8d932b33ff534ad4884bb252ae5afb2b68910b2a2cb9edb998499738da
  summary: You'll deploy a single-node Apache Spark environment on an AWS Graviton2-based EC2 instance.
    First, you'll define and provision the instance with Terraform. You'll then choose either
    manual commands or an Ansible playbook to install Spark and its dependencies. Finally, you'll
    connect to a Jupyter Notebook using the public address of the instance, and the printed token. You
    can remove the created resources with `terraform destroy`.
  faqs:
  - question: Where do I find the public IP address of the instance?
    answer: After `terraform apply`, read the `Master_public_IP` value in the Terraform output.
      Use that address when connecting to the EC2 instance.
  - question: What instance settings should I specify in Terraform?
    answer: Specify a `t4g.small` instance type and Arm Ubuntu AMI in the Terraform
      configuration. Use an Amazon Machine Image (AMI) for your selected AWS region.
  - question: Do I need to use Ansible to configure Spark?
    answer: No. After Terraform creates the instance, you can complete either the manual installation steps
      or the Ansible playbook to configure Spark.
  - question: What should I check if provisioning fails in another region?
    answer: Check that the Arm Ubuntu AMI in the Terraform configuration is valid for your selected
      region. AMI identifiers are region specific.
  - question: How do I remove the resources after testing?
    answer: Run `terraform destroy` from the Terraform project directory. Confirm the prompt
      to delete resources.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Databases
platforms:
  - AWS Graviton

armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Terraform

further_reading:
    - resource:
        title: Optimize Spark on AWS Graviton2
        link: https://developer.arm.com/community/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/optimize-spark-on-aws-graviton2-best-practices-k-means-clustering
        type: blog

    - resource:
        title: Achieve better performance for Spark workloads
        link: https://aws.amazon.com/blogs/big-data/achieve-up-to-27-better-price-performance-for-spark-workloads-with-aws-graviton2-on-amazon-emr-serverless/
        type: blog 

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

