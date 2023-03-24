---
additional_search_terms:
- cloud
layout: installtoolsall
minutes_to_complete: 15
multi_install: false
multitool_install_part: false
official_docs: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html
test_images:
- ubuntu:latest
test_link: https://github.com/armflorentlebeau/arm-learning-paths/actions/runs/4312122327
test_maintenance: true
test_status:
- passed
title: AWS CLI
tool_install: true
weight: 1
---

[AWS CLI](https://docs.aws.amazon.com/cli/index.html) is a cross-platform command-line tool that can be installed on development computers. The AWS Command Line Interface (AWS CLI) is a unified tool that provides a consistent interface for interacting with all parts of Amazon Web Services. 

It is available for a variety of operating systems and Linux distributions and has multiple ways to install it. 

## Introduction

This article provides a quick solution to install AWS CLI version 2 for Ubuntu on Arm.

Confirm you are using an Arm computer with 64-bit Linux by running:

```bash { target="ubuntu:latest" }
uname -m
```

The output should be:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

## Download and install AWS CLI version 2

Before starting, install `unzip`:

```bash { target="ubuntu:latest" }
sudo apt update
sudo apt install unzip -y
```

Download the zip file with `curl`, extract the installer, and run it.  

```bash { target="ubuntu:latest" }
curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

Confirm the CLI is available by invoking the `aws` command to print the version.

```bash { target="ubuntu:latest" }
aws --version
```

## Install AWS CLI version 1

AWS CLI version 2 is recommended, but version 1 can be installed using the Linux package manager.

Both versions should not be installed on the same computer.

```console
sudo apt update
sudo apt install awscli -y
```

Review [AWS CLI v2 is now generally available](https://aws.amazon.com/blogs/developer/aws-cli-v2-is-now-generally-available/) to review the new features in version 2. 

You are ready to use the AWS CLI.