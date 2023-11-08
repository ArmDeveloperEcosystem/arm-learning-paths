---
title: Motivation
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why do you need Infrastructure as Code?
Infrastructure as Code (IaC) provides a declarative approach for provisioning cloud resources. The idea is that instead of creating cloud resources using the Azure Portal or the Azure CLI, you declare the cloud environment using a text file of the specific format. This enables you to keep declarations in the source control system and deploy, update, and destroy all cloud resources using a single command.

Azure natively provides the Azure Resource Manager (ARM) as the IaC tool. However, using it might be difficult. Also, in many practical scenarios, you use multi-cloud environments. So, you would need a provider-specific IaC tool for automation. 

To solve this problem and accelerate IaC adoption, Pulumi offers the cross-platform IaC approach, in which you can use one of the most popular scripting or programming languages, including TypeScript, Python, Go, C#, and Java. With Pulumi, you declare and configure your cloud resources like you would create an application. So, Pulumi-based IaC can be quickly adopted.

In this learning path, you will see how to use Pulumi to create the Azure Container Instance, which will host the sample ASP.NET .NET Core application. By doing so, you will learn how such IaC-based automation can accelerate and simplify the deployment of cloud resources.