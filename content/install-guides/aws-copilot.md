---
additional_search_terms:
- cloud
- deploy


layout: installtoolsall
minutes_to_complete: 10
author_primary: Jason Andrews
multi_install: false
multitool_install_part: false
official_docs: https://aws.github.io/copilot-cli/
test_images:
- ubuntu:latest
test_link: null
test_maintenance: false
test_status:
- passed
title: AWS Copilot CLI
tool_install: true
weight: 1
---

AWS Copilot CLI is an open source command line interface for running containers on AWS App Runner, Amazon Elastic Container Service (ECS), and AWS Fargate.

It is available for a variety of operating systems and Linux distributions and supports the Arm architecture. 

## Before you begin

This article provides quick solutions to install the latest version of AWS Copilot CLI for Ubuntu on Arm and macOS.

Confirm you are using an Arm computer by running:

```bash { target="ubuntu:latest" }
uname -m
```

If you are on Arm Linux the output should be:

```output
aarch64
```

If you are on macOS with Apple Silicon the output should be:

```output
arm64
```

## Download and install AWS Copilot CLI

Copilot requires Docker. Refer to the [Docker](/install-guides/docker/) install guide for installation instructions. 

If you are using Docker on Linux you will need to install QEMU to build container images for both the `arm64` and the `amd64` architectures.

```console
sudo apt-get install qemu-user-static
```

Docker Desktop for macOS includes the ability to build for multiple architectures, so you don't need to do anything extra.

To install Copilot on Arm Linux:

```console
sudo curl -Lo /usr/local/bin/copilot https://github.com/aws/copilot-cli/releases/latest/download/copilot-linux-arm64 \
   && sudo chmod +x /usr/local/bin/copilot \
   && copilot --help
```

To install Copilot on macOS:

```console
curl -Lo copilot https://github.com/aws/copilot-cli/releases/latest/download/copilot-darwin && chmod +x copilot && sudo mv copilot /usr/local/bin/copilot && copilot --help
```

The help message is printed:

```output
👩‍✈️ Launch and manage containerized applications on AWS.

Commands
  Getting Started 🌱
    init        Create a new ECS or App Runner application.
    docs        Open the copilot docs.

  Develop ✨
    app         Commands for applications.
                Applications are a collection of services and environments.
    env         Commands for environments.
                Environments are deployment stages shared between services.
    svc         Commands for services.
                Services are long-running ECS or App Runner services.
    job         Commands for jobs.
                Jobs are tasks that are triggered by events.
    task        Commands for tasks.
                One-off Amazon ECS tasks that terminate once their work is done.
    run         Run the workload locally.

  Release 🚀
    pipeline    Commands for pipelines.
                Continuous delivery pipelines to release services.
    deploy      Deploy one or more Copilot jobs or services.

  Extend 🧸
    storage     Commands for working with storage and databases.
    secret      Commands for secrets.
                Secrets are sensitive information that you need in your application.

  Settings ⚙️
    version     Print the version number.
    completion  Output shell completion code.

Flags
  -h, --help      help for copilot
  -v, --version   version for copilot

Examples
  Displays the help menu for the "init" command.
  `$ copilot init --help`
```

Verify Copilot CLI is installed by running:

```console
copilot --version
```

The installed version is displayed:

```output
copilot version: v1.34.0
```