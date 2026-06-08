---
title: Perform Sentiment Analysis on X on Arm-based EKS clusters

minutes_to_complete: 60

who_is_this_for: This Learning Path is for software developers who want to build an end-to-end ML sentiment analysis solution on an Arm-based Amazon EKS cluster to analyze live posts on X .

learning_objectives: 
    - Deploy a text classification model on Amazon EKS with Apache Spark.
    - Use Elasticsearch and a Kibana dashboard to analyze the posts on X.
    - Deploy Prometheus and Grafana dashboards to monitor CPU and RAM usage of Kubernetes nodes.

prerequisites:
    - An AWS account.
    - A computer with Docker, Terraform, the Amazon eksctl command-line interface, and kubectl installed.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:04:23Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3d9b35d09c97557dcde807bb83f994f8c3701c0d109c0a9bb388acc603d81b16
  summary_generated_at: '2026-06-02T05:07:57Z'
  summary_source_hash: 3d9b35d09c97557dcde807bb83f994f8c3701c0d109c0a9bb388acc603d81b16
  faq_generated_at: '2026-06-03T02:04:23Z'
  faq_source_hash: 3d9b35d09c97557dcde807bb83f994f8c3701c0d109c0a9bb388acc603d81b16
  summary: >-
    Build an end-to-end sentiment analysis workflow on an Arm-based Amazon EKS cluster. You will
    deploy a text classification model with Apache Spark, index and analyze posts from X using
    Elasticsearch, and explore results through a Kibana dashboard. The path also adds cluster
    observability by deploying Prometheus and Grafana dashboards to track CPU and RAM usage of
    Kubernetes nodes. Prerequisites include an AWS account and a Linux workstation with Docker,
    Terraform, eksctl, and kubectl installed; the steps also use the AWS CLI (configured with
    access keys) and Java. You will clone a provided GitHub repository to bootstrap the environment
    and validate results in Kibana and Grafana.
  faqs:
  - question: What do I need before running the setup commands?
    answer: >-
      You need an AWS account and a Linux computer with Docker, Terraform, eksctl, kubectl, the
      AWS CLI, and Java installed. The path assumes these tools are available on your machine.
  - question: How do I provide AWS credentials for the deployment tools?
    answer: >-
      Generate AWS access keys and configure the AWS CLI following the AWS Credentials Install
      Guide. The CLI must be authenticated before creating or managing EKS resources.
  - question: Where do I get the code and configurations used in this path?
    answer: >-
      Clone the repository: git clone https://github.com/koleini/spark-sentiment-analysis.git.
      Work from the cloned directory as the Learning Path steps reference files from that repo.
  - question: Which dashboards will I use and what data should I expect to see?
    answer: >-
      Use Kibana to explore posts on X stored in Elasticsearch through customizable visualizations.
      Use Grafana, backed by Prometheus, to view Kubernetes metrics such as CPU and memory usage
      of nodes.
  - question: How do I know the deployment succeeded?
    answer: >-
      You should have a text classification model running on EKS with Apache Spark, a Kibana dashboard
      to analyze X posts, and Grafana dashboards showing CPU and RAM usage. If any part is missing,
      repeat the corresponding deployment step in the path.
# END generated_summary_faq

author: 
    - Pranay Bakre
    - Masoud Koleini
    - Nobel Chowdary Mandepudi
    - Na Li

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
cloud_service_providers:
  - AWS
armips:
    - Neoverse
tools_software_languages:
    - Kubernetes
    - AWS Elastic Kubernetes Service (EKS)
operatingsystems:
    - Linux


further_reading:
    - resource:
        title: EKS documentation
        link: https://aws.amazon.com/eks/
        type: documentation
    - resource:
        title: How to Enable Real-Time Sentiment Analysis on Arm Neoverse-Based Kubernetes Clusters
        link: https://developer.arm.com/community/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/-arm-neoverse-based-kubernetes-clusters
        type: documentation




### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

