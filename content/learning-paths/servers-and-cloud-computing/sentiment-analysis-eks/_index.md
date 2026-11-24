---
title: Perform sentiment analysis on X on Arm-based EKS clusters

minutes_to_complete: 60

who_is_this_for: This Learning Path is for software developers who want to build an end-to-end ML sentiment analysis solution on an Arm-based Amazon EKS cluster to analyze live posts on X .

learning_objectives: 
    - Deploy a text classification model on Amazon EKS with Apache Spark.
    - Use Elasticsearch and a Kibana dashboard to analyze the posts on X.
    - Deploy Prometheus and Grafana dashboards to monitor CPU and RAM usage of Kubernetes nodes.

prerequisites:
    - An AWS account
    - A computer with Docker, Terraform, the Amazon eksctl command-line interface, and kubectl installed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-23T20:58:33Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 94256bedb694a75ea5b50d201e1b8c7a38fd89fbac073392f9947c76c2d834fb
  summary_generated_at: '2026-11-23T20:58:33Z'
  summary_source_hash: 94256bedb694a75ea5b50d201e1b8c7a38fd89fbac073392f9947c76c2d834fb
  faq_generated_at: '2026-11-23T20:58:33Z'
  faq_source_hash: 94256bedb694a75ea5b50d201e1b8c7a38fd89fbac073392f9947c76c2d834fb
  summary: You'll build a sentiment analysis pipeline on an Arm-based Amazon EKS cluster. First,
    you'll prepare the cluster and deploy an Apache Spark text classification workload with Elasticsearch
    and Kibana. You'll fetch posts from X and send them through the pipeline, then inspect sentiment
    results in Kibana. Finally, you'll deploy Prometheus and Grafana to monitor node CPU and memory
    usage during the workload.
  faqs:
  - question: How do I configure access to the new EKS cluster?
    answer: After `terraform apply`, run `aws eks update-kubeconfig` with the `region` and
      `cluster_name` values from `terraform output` and your AWS profile. This updates your `kubeconfig` so that you can use `kubectl` with the cluster.
  - question: Where are the deployment files for this Learning Path?
    answer: Clone the [spark sentiment analysis repository](https://github.com/koleini/spark-sentiment-analysis.git),
      then use its EKS and workload configuration files.
  - question: How do I get posts into the sentiment pipeline?
    answer: After starting the Spark job, set your X bearer token and run `python3 scripts/xapi_tweets.py`
      to fetch posts. Then, run `python3 csv_to_kinesis.py` to send the processed data through
      the pipeline for Elasticsearch and Kibana.
  - question: What should I check in Kibana?
    answer: Look for new documents from X and inspect the dashboard views that classify their
      sentiment as positive, negative, or neutral.
  - question: Do I need to install Prometheus and Grafana separately?
    answer: No. The Terraform setup installs both in your EKS cluster. Install them manually and separately
      only if you want more control over their versions.
# END generated_summary_faq

author: 
    - Pranay Bakre
    - Masoud Koleini
    - Nobel Chowdary Mandepudi
    - Na Li

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
platforms:
  - AWS Graviton
armips:
    - Neoverse
tools_software_languages:
    - Kubernetes
    - Amazon EKS
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

