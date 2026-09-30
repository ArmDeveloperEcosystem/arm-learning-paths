---
title: Use Longhorn to deploy persistent storage for Kubernetes workloads on Arm-based Azure virtual machines

description: Learn how to install and configure Longhorn on an Arm64 Azure virtual machine powered by Azure Cobalt 100, deploy Kubernetes persistent storage using Longhorn on K3s, create persistent volumes, and benchmark storage performance for cloud-native workloads.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for developers, DevOps engineers, platform engineers, and Kubernetes administrators who want to deploy persistent storage for Kubernetes workloads using Longhorn on Arm-based cloud infrastructure.

learning_objectives:
    - Install and configure K3s Kubernetes on an Arm64 Azure virtual machine (VM) powered by Azure Cobalt 100.
    - Install and configure Longhorn distributed block storage on Arm64.
    - Create and manage Kubernetes persistent volumes using Longhorn.
    - Benchmark Kubernetes storage performance using fio.

prerequisites:
  - A [Microsoft Azure account](https://azure.microsoft.com/) with access to Cobalt 100-based instances (Dpsv6)
  - Basic knowledge of Linux command-line operations
  - Familiarity with SSH and remote server access
  - Basic understanding of Kubernetes and containerized workloads

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-28T19:45:18Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 7590b8208863bfffbdee5139c548a3c9e3e82b3c314ca003daeb31e1e7995190
  summary_generated_at: '2026-09-28T19:45:18Z'
  summary_source_hash: 7590b8208863bfffbdee5139c548a3c9e3e82b3c314ca003daeb31e1e7995190
  faq_generated_at: '2026-09-28T19:45:18Z'
  faq_source_hash: 7590b8208863bfffbdee5139c548a3c9e3e82b3c314ca003daeb31e1e7995190
  summary: >-
    You'll deploy Longhorn-backed persistent storage on an Azure VM powered by Cobalt 100. First, you'll provision
    a Dpsv6 VM, configure network access, and set up a single-node K3s cluster with the required
    iSCSI utilities. Then, you'll install Longhorn, attach a PersistentVolumeClaim to a workload, and verify
    that its data survives pod recreation. Finally, you'll run `fio` against the volume to capture
    baseline storage metrics.
  faqs:
  - question: How can I verify that data persists after I recreate the pod?
    answer: >-
      Write data to `/usr/share/nginx/html/index.html` in the running NGINX container. Delete and
      recreate the pod, then use `kubectl exec` to read the file. If the original content appears,
      the data persisted on the Longhorn-backed volume.
  - question: What network configuration do I need to access the Longhorn web UI?
    answer: >-
      Add an inbound network security group rule for TCP ports `80`, `8080`, and `6443`. Apply
      the rule to the VM’s network interface or subnet, then use the VM’s IP address and port
      `8080` while the Longhorn port-forward command is running.
  - question: How do I know K3s and Longhorn are ready to use?
    answer: >-
      Check that the Kubernetes node reports `Ready`, the Longhorn pods report `Running`, and
      the `longhorn` StorageClass is available. Confirm that the Longhorn interface also loads
      in your browser.
  - question: Which StorageClass name should I use in my PersistentVolumeClaim?
    answer: >-
      Set `storageClassName: longhorn` in your manifest. Your PersistentVolumeClaim should
      bind when the `longhorn` StorageClass is available.
  - question: What result should I expect when running fio on the Longhorn-backed volume?
    answer: >-
      Confirm that `fio` completes without errors and prints throughput, input/output operations
      per second (IOPS), and latency metrics. Use this output as a baseline for later runs in your
      environment.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
platforms:
  - Microsoft Azure Cobalt

armips:
    - Neoverse

tools_software_languages:
    - Longhorn
    - Kubernetes
    - K3s
    - fio

operatingsystems:
    - Linux

further_reading:
  - resource:
      title: Longhorn Official Website
      link: https://longhorn.io/
      type: website
  - resource:
      title: Longhorn Documentation
      link: https://longhorn.io/docs/
      type: documentation
  - resource:
      title: K3s Documentation
      link: https://docs.k3s.io/
      type: documentation
  - resource:
      title: Azure Cobalt 100 processors
      link: https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
