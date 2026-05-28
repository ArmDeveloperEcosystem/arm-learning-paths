---
additional_search_terms:
- cloud
- deploy
layout: installtoolsall
minutes_to_complete: 15
author: Anupras Mohapatra
multi_install: false
multitool_install_part: false
official_docs: https://docs.aws.amazon.com/cdk/v2/guide/home.html
test_images:
- ubuntu:latest
test_maintenance: true
draft: true
title: AWS CDK 
tool_install: true
weight: 1
---

The AWS Cloud Development Kit (CDK) is an open-source software development framework that you can use to define and deploy cloud infrastructure such as AWS Graviton-based Amazon EC2 instances programmatically. 

In this guide, you'll set up the AWS CDK by installing the CDK CLI and verify that the CLI installation was successful. 

## Before you begin

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
If you see a different result, you are not using an Arm computer running 64-bit Linux. 

Before you can use the AWS CDK, you need to set up AWS credentials and install the AWS CLI. For more information about setting up AWS credentials and installing the AWS CLI, see the [AWS Credentials](/install-guides/aws_access_keys) and [AWS CLI](/install-guides/aws-cli) install guides. 

You'll also need to install Node.js 22 or later, and prerequisites specific to the programming languages you want to use. For more information about Node.js and language-specific prerequisites, see [Install Node.js and programming language prerequisites](https://docs.aws.amazon.com/cdk/v2/guide/prerequisites.html#prerequisites-node) in the AWS CDK documentation.

## Install the AWS CDK CLI

Use `npm` to install the AWS CDK CLI:

```bash
npm install -g aws-cdk
```

## Verify the installation

After installing the CDK CLI, check the version of the AWS CDK CLI that you installed:

```bash
cdk --version
```

The output is similar to:

```output
2.1125.0 (build 71fd29e)
```
## Next steps

You've now installed the AWS CDK CLI and verified that the installation was successful.

Next, you can use the CLI to deploy AWS Graviton-based Amazon EC2 instances. 
