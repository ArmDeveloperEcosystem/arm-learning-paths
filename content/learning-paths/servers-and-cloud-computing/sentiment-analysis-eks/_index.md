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

author_primary: Pranay Bakre, Masoud Koleini, Nobel Chowdary Mandepudi, Na Li

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
cloud_service_providers: AWS
armips:
    - Neoverse
tools_software_languages:
    - Kubernetes
    - AWS Elastic Kubernetes Service (EKS)
operatingsystems:
    - Linux


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
