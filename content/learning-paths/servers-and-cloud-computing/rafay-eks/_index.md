---
title: Deploy an Amazon EKS cluster with AWS Graviton-based nodes using Rafay

description: Use the Rafay Kubernetes Operations Platform to provision an Amazon EKS cluster with an AWS Graviton-based node group and deploy NGINX to verify the setup.


minutes_to_complete: 60

who_is_this_for: >
    This is an advanced topic for software developers familiar with Kubernetes and AWS who want to learn how to use the Rafay platform to provision and manage EKS clusters backed by AWS Graviton-based instances.

learning_objectives:
    - Connect your AWS account to the Rafay platform using a cross-account IAM role
    - Provision an Amazon EKS cluster with an AWS Graviton-based node group using Rafay
    - Deploy and verify workloads on arm64 nodes and clean up all cloud resources

prerequisites:
    - An Amazon Web Services (AWS) [account](https://aws.amazon.com/) with sufficient IAM permissions to create roles, EKS clusters, EC2 instances, CloudFormation stacks, and related resources.
    - A [Rafay account](https://rafay.co).
    - The [AWS CLI](/install-guides/aws-cli/) installed and configured.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-24T20:45:31Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 76cbd5e4b3a61e9604e0df9b3ba2a5e5af4aa9a0c295ece3c4ee5a98ec365630
  summary_generated_at: '2026-06-24T20:45:31Z'
  summary_source_hash: 76cbd5e4b3a61e9604e0df9b3ba2a5e5af4aa9a0c295ece3c4ee5a98ec365630
  faq_generated_at: '2026-06-24T20:45:31Z'
  faq_source_hash: 76cbd5e4b3a61e9604e0df9b3ba2a5e5af4aa9a0c295ece3c4ee5a98ec365630
  summary: >-
    You'll provision an Amazon EKS cluster on Arm using
    the Rafay Kubernetes Operations Platform and validate workloads on AWS Graviton-based nodes.
    First, you'll define a declarative cluster manifest in Rafay referencing an existing project,
    blueprint, and cloud credential. Then, you'll create the EKS cluster and deploy NGINX pinned to arm64 
    to confirm scheduling on Graviton-based instances. Finally, you'll remove the NGINX workload and deprovision the EKS resources to avoid ongoing cloud costs.
  faqs:
  - question: How do I know the AWS connection to Rafay is set up correctly before creating the
      cluster?
    answer: >-
      Ensure the cross-account IAM role is configured in AWS and added to Rafay as a cloud credential.
      In the cluster manifest, reference this credential by name. If it's missing or has insufficient
      permissions, cluster creation will fail.
  - question: Which fields in the Rafay cluster manifest must match existing configuration?
    answer: >-
      The project, blueprint name and version, and the cloud credential must already exist in
      Rafay. If any of these don't match, the cluster won't be created.
  - question: What result should I expect when the EKS cluster is ready to use?
    answer: >-
      A running cluster with a Graviton-based (`arm64`) node group will be available for workloads.
      Nodes should advertise the label `kubernetes.io/arch=arm64`, indicating they can run `arm64`
      pods.
  - question: How do I verify that the NGINX deployment is running on Graviton nodes?
    answer: >-
      The provided manifest pins the pods using `nodeSelector: kubernetes.io/arch: arm64`. After
      deployment, the pod should schedule and run on nodes labeled `arm64`. If it remains `Pending`,
      verify the node group is active and the selector matches node labels.
  - question: What should I clean up to avoid ongoing AWS charges?
    answer: >-
      Delete the NGINX workload and namespace created for the test, then deprovision the EKS cluster
      from Rafay. This releases the associated AWS resources.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
cloud_service_providers:
    - AWS
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Kubernetes
    - AWS Elastic Kubernetes Service (EKS)
    - Rafay
    - NGINX
    - rctl

#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
    - resource:
        title: Rafay CLI overview
        link: https://docs.rafay.co/cli/overview/
        type: documentation
    - resource:
        title: Amazon EKS documentation
        link: https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html
        type: documentation
    - resource:
        title: AWS Graviton processors
        link: https://aws.amazon.com/ec2/graviton/
        type: documentation
    - resource:
        title: Kubernetes documentation
        link: https://kubernetes.io/docs/home/
        type: documentation

weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

