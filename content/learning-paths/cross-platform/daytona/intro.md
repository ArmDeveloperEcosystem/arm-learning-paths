---
title: "Welcome to Daytona"
weight: 2

layout: "learningpathall"
---

## Development Environment Manager

[Daytona](https://www.daytona.io/) is a powerful open-source tool for managing development environments. It enables you to easily create, manage, and switch between both local and remote environments. 

Daytona is based on dev containers, which provide isolated and reproducible development environments.

Dev containers are lightweight, portable, and consistent environments that you can use across different development setups. They ensure that your development environment remains the same regardless of your work location. 

For more information about dev containers, see the following resources:
- [Introduction to Dev Containers](https://code.visualstudio.com/docs/remote/containers/).
- [Development Containers Specification and dev container resources](https://github.com/devcontainers/).

Daytona is a single executable that runs on a variety of computers, including Windows on Arm, Arm Linux, and macOS. It's a great way to develop on Arm as you can use it to access local and remote Arm hardware. 

You can use Daytona to create development environments on the following setups:

* On a local computer.
* On remote computers running on your local network.
* On remote computers from cloud service providers such as AWS and Azure. 

## Daytona terminology

Taking time to learn some the basic Daytona definitions will enable you to get started easily. You can find some of these terms described below. 

#### Git Providers

A Git provider hosts Git repositories and provides tools for managing and collaborating on source code. Examples of Git providers include GitHub, GitLab, Bitbucket, and Azure Repos. With Daytona, a Git provider supplies the source code for your development environments.

#### Providers

In Daytona, providers supply the resources needed to run development environments. These can be virtual machines (VMs) from AWS or Azure, or container providers such as Docker. Providers abstract away the details of the underlying compute, networking, and storage.

#### Targets

A target in Daytona is the specific configuration of the development environment, including the provider, operating system, CPU and memory resources, and development tools. 

The combination of a code repository from a Git provider, and a target from a provider, bring a development environment to life. 

## Before you begin

To try out Daytona, you need one or more Arm-based computers running Windows, macOS, or Linux. Each computer must have Docker installed. See the [Docker install guide](/install-guides/docker/) for installation options. 

In the next section, you can learn how to install and configure Daytona.