---
title: Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this Learning Path, you'll create an Azure Resource Manager template that deploys a Linux virtual machine powered by Azure Cobalt 100 processors. The template configures networking, security, and SSH authentication, providing a complete foundation for deploying Arm-based workloads on Azure.

You'll learn how to:

- Structure an Azure Resource Manager template with parameters, variables, and resources
- Specify Arm64 architecture and Cobalt 100 VM sizes
- Configure SSH key authentication for secure access
- Deploy the template using Azure CLI
- Verify and connect to your deployed Arm-based VM

By the end of this Learning Path, you'll have a reusable template for deploying Cobalt 100 VMs and the knowledge to customize it for your specific requirements.
Azure Resource Manager templates provide a declarative way to define and deploy Azure infrastructure as code. By using Resource Manager templates, you can automate the deployment of Arm-based Cobalt 100 virtual machines with consistent, repeatable results across different environments.

## What is an Azure Resource Manager template?

Azure Resource Manager templates are JSON files that define the infrastructure and configuration you want to deploy in Azure. Templates enable Infrastructure as Code (IaC), allowing you to version control your infrastructure alongside your application code. When you submit a template to Azure Resource Manager, it orchestrates the creation of all specified resources in the correct order, managing dependencies automatically. By using templates, you can achieve consistent, repeatable deployments across different environments while reducing configuration errors and enabling CI/CD automation.

## Before you begin

To complete this Learning Path, you need:

- An active Microsoft Azure subscription with permissions to:
  - Create resource groups
  - Deploy virtual machines
  - Create networking resources (virtual networks, network security groups, public IP addresses)
- Azure CLI installed on your local machine (see the [Azure CLI install guide](/install-guides/azure-cli/))
- An SSH key pair for authentication

## Generate an SSH key pair

If you don't already have an SSH key pair, create one now. On Linux or macOS, run:

```bash
ssh-keygen -t rsa -b 4096 -f ~/.ssh/azure_cobalt_key
```

When prompted, you can enter a passphrase for added security or press Enter to skip it.

This command creates two files:
- `~/.ssh/azure_cobalt_key` - Your private key (keep this secure)
- `~/.ssh/azure_cobalt_key.pub` - Your public key (you'll use this in the Azure Resource Manager template)

## Sign in to Azure

Before deploying resources, authenticate with Azure:

```bash
az login
```

This command opens your browser to complete the authentication process. After signing in, the Azure CLI displays your available subscriptions.

## Set your subscription

If you have multiple Azure subscriptions, set the one you want to use:

```bash
az account set --subscription "Your Subscription Name"
```

You can list your subscriptions with:

```bash
az account list --output table
```

## Verify Azure CLI is working

Confirm your Azure CLI is properly configured by checking your current subscription:

```bash
az account show --output table
```

The output displays details about your active subscription, including the subscription ID and tenant ID.

You're now ready to create the Azure Resource Manager template that will define your Arm-based Cobalt 100 VM infrastructure.
