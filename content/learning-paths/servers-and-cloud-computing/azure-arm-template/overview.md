---
title: Getting started with Azure Resource Manager
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this Learning Path, you’ll create an Azure Resource Manager template that deploys a Linux virtual machine powered by Azure Cobalt 100 processors. The template defines the virtual machine, networking, security settings, and SSH authentication required for deployment.

By using Azure Resource Manager templates, you can deploy infrastructure consistently across environments, reduce configuration errors, and integrate infrastructure provisioning into CI/CD workflows.

## What is an Azure Resource Manager template?

An Azure Resource Manager template is a JSON file that defines the infrastructure and configuration you want to deploy in Azure. This approach is known as Infrastructure as Code (IaC).

When you deploy a template, Azure Resource Manager:
- Creates resources in the correct order
- Manages dependencies automatically
- Ensures deployments are consistent and repeatable

Using templates allows you to version control infrastructure alongside application code and automate deployments across environments.

## Set up your environment 

To complete this Learning Path, you need:

- An Azure account with an active subscription
- Azure CLI installed and configured
- A local terminal on Linux, macOS, or Windows (with WSL)
- An SSH key pair for secure access to the virtual machine

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

## Verify your Azure CLI configuration

Confirm your Azure CLI is properly configured by checking your current subscription:

```bash
az account show --output table
```

The output displays details about your active subscription, including the subscription ID and tenant ID.

## What you've accomplished and what's next

You've authenticated with Azure, configured your active subscription, and generated SSH keys for secure VM access. Your development environment is ready for creating Azure Resource Manager templates.

Next, you'll create the Resource Manager template that defines your Cobalt 100 VM infrastructure.
