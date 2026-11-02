---
title: Deploy MinIO on a virtual machine powered by Azure Cobalt 100

description: Learn how to deploy and configure MinIO on an Azure Cobalt 100 virtual machine, benchmark object storage throughput, and validate S3 compatibility using the boto3 Python SDK.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers, DevOps engineers, and platform engineers who want to deploy MinIO object storage on virtual machines (VMs) powered by Microsoft Azure Cobalt 100.

learning_objectives:
    - Provision a VM powered by Azure Cobalt 100 and deploy MinIO.
    - Benchmark MinIO storage throughput for large object transfers.
    - Validate S3 API compatibility using the boto3 Python SDK.
    - Store and retrieve AI and ML datasets, as well as model artifacts, using MinIO.

prerequisites:
  - A [Microsoft Azure account](https://azure.microsoft.com/) with access to Cobalt 100-based instances (Dpsv6)
  - Familiarity with SSH and remote server access
  - Basic understanding of cloud storage concepts

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-28T19:50:39Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d560db2da86f62f3e2f0d9bf8f232d51971d21fceb398a288f59388dd5821c96
  summary_generated_at: '2026-09-28T19:50:39Z'
  summary_source_hash: d560db2da86f62f3e2f0d9bf8f232d51971d21fceb398a288f59388dd5821c96
  faq_generated_at: '2026-09-28T19:50:39Z'
  faq_source_hash: d560db2da86f62f3e2f0d9bf8f232d51971d21fceb398a288f59388dd5821c96
  summary: >-
    You'll deploy and validate a single-node MinIO object store on an Azure Cobalt 100-based VM.
    First, you'll create a Dpsv6 instance, open ports `9000` and `9001`, and connect through SSH to configure
    MinIO with local storage. You'll generate a 1 GB test file and time its upload with the MinIO Client.
    Finally, you'll use Python and `boto3` to confirm S3 API compatibility.
  faqs:
  - question: Which ports should I open in Azure for MinIO, and where do I add the rule?
    answer: >-
      Open TCP ports `9000` for the S3 API and `9001` for the MinIO Console. Add the inbound rules
      to the network security group attached to your VM’s network interface or subnet.
  - question: How do I SSH into the VM after provisioning it?
    answer: >-
      Run `ssh -i <your-key>.pem azureuser@<VM-IP>` with the private key that you downloaded during
      VM creation. Verify the VM’s public IP in the Azure portal before you connect.
  - question: How do I verify that MinIO is running and reachable?
    answer: >-
      Open `http://<VM-IP>:9001` to access the MinIO Console. You can also run MinIO Client commands
      and confirm that the server returns successful responses.
  - question: When generating test data and running the upload benchmark, what should I see?
    answer: >-
      Confirm that `dd` creates `dataset/file1.bin` at about 1 GB. Your timed `mc cp` upload should
      finish without errors, report its duration, and display the object in the MinIO Console.
  - question: How do I know that S3 API validation with boto3 worked?
    answer: >-
      Confirm that your `boto3` operations complete without exceptions and list the expected bucket
      or objects. Verify that the uploaded objects also appear in the MinIO Console.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Databases 
platforms:
  - Microsoft Azure Cobalt

armips:
    - Neoverse

tools_software_languages:
    - MinIO
    - Python
    - boto3

operatingsystems:
    - Linux

further_reading:
  - resource:
      title: MinIO Documentation
      link: https://min.io/docs/minio/linux/index.html
      type: documentation
  - resource:
      title: MinIO GitHub Repository
      link: https://github.com/minio/minio
      type: documentation
  - resource:
      title: Azure Cobalt 100 processors
      link: https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353
      type: documentation
  - resource:
      title: Deploy a Cobalt 100 virtual machine on Azure
      link: /learning-paths/servers-and-cloud-computing/cobalt/
      type: learning-path

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
