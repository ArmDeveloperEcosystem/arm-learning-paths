---
# User change
title: Set up the AWS environment

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## What Amazon ECS Managed Instances is

Amazon ECS Managed Instances is a compute option for deploying containers on AWS. Compared to AWS Fargate, you can maintain greater control over the type of Amazon EC2 instances used. 

Some of the compute attributes that you can control include the following:

- vCPU count
- Memory
- Accelerator type
- Local storage
- Instance type and family
- CPU manufacturer


AWS handles infrastructure management, such as software and OS patching, instance scaling, and maintenance, on your behalf. 

For more information, see [Architect for Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ManagedInstances.html) in the Amazon ECS documentation. 

You'll use the available compute attributes to select Arm-based instances powered by AWS Graviton. 

## Create IAM roles
## Register a task definition
## Create VPC and security group?