---
title: Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Azure Resource Manager templates provide a declarative way to define and deploy Azure infrastructure as code. In this Learning Path, you'll create a template that deploys a Linux virtual machine powered by Azure Cobalt 100 processors, including networking, security, and SSH authentication.

Using Resource Manager templates enables consistent, repeatable deployments across different environments while reducing configuration errors and enabling CI/CD automation.

## What is an Azure Resource Manager template?

Azure Resource Manager templates are JSON files that define the infrastructure and configuration you want to deploy in Azure. Templates enable Infrastructure as Code (IaC), allowing you to version control your infrastructure alongside your application code. When you submit a template to Azure Resource Manager, it orchestrates the creation of all specified resources in the correct order, managing dependencies automatically. Templates achieve consistent, repeatable deployments across different environments while reducing configuration errors and enabling CI/CD automation.

## Before you begin

To complete this Learning Path, you need:



## Generate an SSH key pair

If you don't have an SSH key pair, create one now. On Linux or macOS, run:

```bash
ssh-keygen -t rsa -b 4096 -f ~/.ssh/azure_cobalt_key
```

When prompted, you can enter a passphrase for added security or press Enter to skip it.

This creates two files:
- `~/.ssh/azure_cobalt_key` (private key - keep this secure)
- `~/.ssh/azure_cobalt_key.pub` (public key - you'll use this in the template)

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

## What you've accomplished and what's next

You've authenticated with Azure, configured your active subscription, and generated SSH keys for secure VM access. Your development environment is ready for creating Azure Resource Manager templates.

Next, you'll create the Resource Manager template that defines your Cobalt 100 VM infrastructure.
