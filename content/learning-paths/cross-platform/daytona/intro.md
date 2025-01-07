---
title: "Welcome to Daytona"
weight: 2

layout: "learningpathall"
---

[Daytona](https://www.daytona.io/) is a powerful open-source tool for managing development environments. It enables you to easily create, manage, and switch between different environments, both local and remote. 

Daytona is based on dev containers, which provide isolated and reproducible development environments.

Dev containers are lightweight, portable, and consistent environments that can be used across different development setups. They ensure that your development environment is the same regardless of where you are working. 

For more information about dev containers, you can refer to the following resources:
- [Introduction to Dev Containers](https://code.visualstudio.com/docs/remote/containers/)
- [Development Containers Specification and dev container resources](https://github.com/devcontainers/)

Daytona is a single executable that runs on a variety of computers, including Windows on Arm, Arm Linux, and macOS with Apple Silicon. It's a great way to develop on Arm as it can be used to access local and remote Arm hardware. 

You can use Daytona to create development environments on your local computer, on remote computers running on your local network, and on remote computers from cloud service providers such as AWS and Azure. 

## Daytona terminology

Understanding basic Daytona definitions makes it easier to get started.

### What are Git providers?

A Git provider hosts Git repositories and provides tools for managing and collaborating on source code. Examples of Git providers include GitHub, GitLab, Bitbucket, and Azure Repos. With Daytona, a Git provider supplies the source code for your development environments.

### What are providers?

In Daytona, providers supply the resources needed to run development environments, these can be virtual machines (VMs) from AWS or Azure or container providers such as Docker. Providers abstract away the details of the underlying compute, networking, and storage.

### What are targets?

A target in Daytona is the specific configuration of the development environment, including the provider, operating system, CPU and memory resources, and development tools. 

The combination of a code repository from a Git provider and a target from a provider bring a development environment to life. 

## Before you begin

To try out Daytona, you need one or more Arm-based computers running Windows, macOS, or Linux. Each computer must have Docker installed. Refer to the [Docker install guide](/install-guides/docker/) for installation options. 

Next, learn how to install and configure Daytona.