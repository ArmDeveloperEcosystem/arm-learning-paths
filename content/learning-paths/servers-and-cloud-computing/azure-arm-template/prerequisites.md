---
title: Prerequisites and setup
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin

To complete this Learning Path, you need:

- An active Microsoft Azure subscription with permissions to:
  - Create resource groups
  - Deploy virtual machines
  - Create networking resources (virtual networks, network security groups, public IP addresses)
- Azure CLI installed on your local machine (see the [Azure CLI install guide](/install-guides/azure-cli/)
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

## What you've accomplished and what's next

You've prepared your local environment with Azure CLI installed and authenticated, created an SSH key pair for secure VM access, and configured your Azure subscription. You're now ready to create the Azure Resource Manager template that will define your Arm-based Cobalt 100 VM infrastructure.
