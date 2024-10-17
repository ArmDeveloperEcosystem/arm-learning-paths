---
review:
    - questions:
        question: >
            Which instance type denotes an Axion processor?
        answers:
            - T2A
            - C4A
        correct_answer: 2                
        explanation: >
            C4A denotes an Axion processor. T2A refers to the older Ampere Altra processors.

    - questions:
        question: >
            Which flag is best for long running applications with predictable workloads?
        answers:
            - -XX:InitialCodeCacheSize
            - -XX:-TieredCompilation
            - -XX:ReservedCodeCacheSize
        correct_answer: 2                   
        explanation: >
            Turning off tiered compilation is best for long running applications with predictable workloads.
    - questions:
        question: >
            What is the purpose of running the following command when creating an Axion instance on Google Cloud Platform?

            gcloud compute instances create test-app-instance --image-family=ubuntu-2404-lts-arm64  --image-project=ubuntu-os-cloud  --machine-type=c4a-standard-2 --scopes userinfo-email,cloud-platform  --zone [YOUR ZONE] --tags http-server
        answers:
            - To configure the Google Cloud project ID.
            - To create a new virtual machine instance with specific configurations.
            - To configure firewall rules to allow HTTP traffic on port 8080.
            - To obtain the external IP address of the virtual machine instance.
        correct_answer: 2
        explanation: >
            This is a gcloud CLI command to create a new Ubuntu virtual machine instance.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
