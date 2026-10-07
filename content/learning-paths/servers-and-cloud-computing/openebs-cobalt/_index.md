---
title: Use OpenEBS for Kubernetes-native persistent storage on Azure Cobalt 100-based Arm64 virtual machines 

description: Learn how to install and configure OpenEBS LocalPV on an Arm64 virtual machine powered by Azure Cobalt 100 using K3s Kubernetes, provision persistent storage dynamically, deploy stateful applications, and validate persistent storage functionality.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for DevOps engineers, platform engineers, cloud-native developers, and Kubernetes administrators who want to deploy lightweight Kubernetes-native persistent storage on Arm-based cloud infrastructure.

learning_objectives:
    - Install and configure K3s Kubernetes on Arm64 virtual machines (VMs) powered by Azure Cobalt 100.
    - Deploy OpenEBS LocalPV using Helm.
    - Configure Kubernetes storage classes and PersistentVolumeClaims (PVCs).
    - Deploy and validate stateful Kubernetes workloads with persistent storage.

prerequisites:
  - A [Microsoft Azure account](https://azure.microsoft.com/) with access to Cobalt 100-based instances (Dpsv6)
  - Basic knowledge of Linux command-line operations
  - Familiarity with SSH and remote server access
  - Basic understanding of Kubernetes concepts and containerized applications

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-01T19:43:29Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 33e9470ccc06f4835028050615832b7200164ec6ba1fdbc26689e6f4fd43bfa4
  summary_generated_at: '2026-10-01T19:43:29Z'
  summary_source_hash: 33e9470ccc06f4835028050615832b7200164ec6ba1fdbc26689e6f4fd43bfa4
  faq_generated_at: '2026-10-01T19:43:29Z'
  faq_source_hash: 33e9470ccc06f4835028050615832b7200164ec6ba1fdbc26689e6f4fd43bfa4
  summary: >-
    You'll add Kubernetes-native persistent storage to a workload on an Arm64 Azure VM powered by Cobalt 100. First, you'll create a single-node K3s cluster, install OpenEBS LocalPV with Helm, and configure
    its storage class. You'll then create a PersistentVolumeClaim, mount it in an NGINX application,
    and verify that test data survives pod recreation. Finally, you'll expose the application through
    a NodePort and update the Azure network security group for inbound access.
  faqs:
  - question: How can I install a specific version of the OpenEBS Helm chart?
    answer: >-
      Run `helm search repo openebs/openebs --versions` to list available chart versions, then add
      `--version <version>` to the provided `helm install` command. Without this option, you install
      the latest available chart.
  - question: How do I expose the sample application so I can reach it from my browser?
    answer: >-
      Expose the NGINX deployment as a NodePort service and run `kubectl get svc` to see the assigned
      port. Then add an inbound rule for that NodePort in the VM’s Network Security Group.
  - question: What storage configuration should I use for the PersistentVolumeClaim?
    answer: >-
      Use `storageClassName: openebs-hostpath` and `accessModes: ReadWriteOnce` as shown in the PersistentVolumeClaim
      manifest. This configuration targets OpenEBS LocalPV for dynamic provisioning.
  - question: How do I know persistent storage is working before I move on?
    answer: >-
      Write data to the mounted volume in the NGINX pod, delete the pod, and let it recreate.
      If the data is still present after the pod comes back, the volume is persisting as expected.
  - question: Do I need a multi-node cluster?
    answer: >-
      No. Use a lightweight single-node Kubernetes cluster with K3s on the VM. 
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
    - Kubernetes
    - K3s
    - OpenEBS
    - Helm

operatingsystems:
    - Linux

further_reading:
  - resource:
      title: OpenEBS Official Website
      link: https://openebs.io/
      type: website
  - resource:
      title: OpenEBS Documentation
      link: https://openebs.io/docs
      type: documentation
  - resource:
      title: K3s Documentation
      link: https://docs.k3s.io/
      type: documentation
  - resource:
      title: Kubernetes Documentation
      link: https://kubernetes.io/docs/
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
