---
title: Learn about MLflow and Google Axion C4A for machine learning
weight: 2

layout: "learningpathall"
---

## Google Axion C4A Arm instances for machine learning

Google Axion C4A is a family of Arm-based virtual machines built on Google’s custom Axion CPU, which is based on Arm Neoverse V2 cores. Designed for high-performance and energy-efficient computing, these virtual machines offer strong performance for modern cloud workloads such as CI/CD pipelines, microservices, media processing, and general-purpose applications.

The C4A series provides a cost-effective alternative to x86 virtual machines while using the scalability and performance benefits of the Arm architecture in Google Cloud.

To learn more, see the Google blog [Introducing Google Axion Processors, our new Arm-based CPUs](https://cloud.google.com/blog/products/compute/introducing-googles-new-arm-based-cpu).

## MLflow for ML lifecycle management on Arm

MLflow is an open-source platform designed to manage the end-to-end machine learning lifecycle. It's widely used for experiment tracking, model management, reproducibility, and deployment.

MLflow provides a unified platform with components such as:

* MLflow Tracking for logging parameters, metrics, and artifacts  
* MLflow Projects for packaging and reproducible execution  
* MLflow Models for standardized model formats and deployment  
* MLflow Model Registry for versioning, lifecycle management, and model governance  

Running MLflow on Google Axion C4A Arm-based infrastructure enables efficient execution of machine learning workflows by using multi-core CPUs and optimized memory performance. This results in improved performance per watt, reduced infrastructure costs, and better scalability for ML experimentation and deployment pipelines.

Common use cases include experiment tracking, model versioning, reproducible ML workflows, CI/CD integration for ML pipelines, and deploying models as scalable APIs for real-time inference.

To learn more, see the [MLflow documentation](https://mlflow.org/docs/latest/index.html) and the [MLflow GitHub repository](https://github.com/mlflow/mlflow).

## What you've learned and what's next

You've now learned about Google Axion C4A Arm-based virtual machines and their performance advantages for machine learning workflows. You were also introduced to core MLflow components including Tracking, Projects, Models, and Model Registry. 

Next, you'll create a firewall rule in Google Cloud Console to enable remote access to the MLflow UI and model serving APIs used in this Learning Path.
