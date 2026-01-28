---
title: Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Azure Resource Manager templates provide a declarative way to define and deploy Azure infrastructure as code. By using Resource Manager templates, you can automate the deployment of Arm-based Cobalt 100 virtual machines with consistent, repeatable results across different environments.

## What is an Azure Resource Manager template?

Azure Resource Manager templates are JSON files that define the infrastructure and configuration you want to deploy in Azure. Templates enable Infrastructure as Code (IaC), allowing you to version control your infrastructure alongside your application code. When you submit a template to Azure, Resource Manager orchestrates the creation of all specified resources in the correct order, managing dependencies automatically.

## Why use Resource Manager templates for Cobalt 100 VMs?

Resource Manager templates offer several advantages for deploying Cobalt 100 virtual machines:

- **Repeatability**: Deploy identical Arm-based environments across development, testing, and production
- **Version control**: Track infrastructure changes using Git or other version control systems
- **Consistency**: Reduce configuration drift and human error through standardized deployments
- **Automation**: Integrate VM deployments into CI/CD pipelines for automated infrastructure provisioning
- **Documentation**: Templates serve as living documentation of your infrastructure

## What you'll learn

In this Learning Path, you'll create a Resource Manager template that deploys a Linux virtual machine powered by Azure Cobalt 100 processors. The template configures networking, security, and SSH authentication, providing a complete foundation for deploying Arm-based workloads on Azure.

You'll learn how to:

- Structure a Resource Manager template with parameters, variables, and resources
- Specify Arm64 architecture and Cobalt 100 VM sizes
- Configure SSH key authentication for secure access
- Deploy the template using Azure CLI
- Verify and connect to your deployed Arm-based VM

By the end of this Learning Path, you'll have a reusable template for deploying Cobalt 100 VMs and the knowledge to customize it for your specific requirements.
