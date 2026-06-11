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
title: AWS CDK CLI
description: Install the AWS CDK CLI on Arm Linux and macOS using npm, then verify the setup with the `cdk` command.
tool_install: true
weight: 1
---

The AWS Cloud Development Kit (CDK) is an open-source infrastructure as code (IaC) software development framework. You can use the AWS CDK to define and deploy applications on Arm-based cloud infrastructure powered by AWS Graviton. 

With the CDK, you can write applications in a supported programming language of your choice. You can then use the AWS CDK CLI to translate the code into an AWS CloudFormation template and deploy the application. 

In this guide, you'll learn how to install the CDK CLI and verify that the CLI installation was successful. 

## Before you begin

Before you can use the AWS CDK, you need to set up AWS credentials and install the AWS CLI. For more information about setting up AWS credentials and installing the AWS CLI, see the [AWS Credentials](/install-guides/aws_access_keys/) and [AWS CLI](/install-guides/aws-cli/) install guides. 

To install the AWS CDK CLI, you'll need Node.js 22 or later. You'll also need to install prerequisites specific to the programming languages that you want to use. For more information about Node.js and language-specific prerequisites, see [Install Node.js and programming language prerequisites](https://docs.aws.amazon.com/cdk/v2/guide/prerequisites.html#prerequisites-node) in the AWS CDK documentation.

## Install the AWS CDK CLI

Use `npm` to install the AWS CDK CLI:

```bash
npm install -g aws-cdk
```

## Verify the installation

After installing the AWS CDK CLI, check the version of the CLI:

```bash
cdk --version
```

The output is similar to:

```output
2.1125.0 (build 71fd29e)
```
## Next steps

You've now installed the AWS CDK CLI and verified that the installation was successful.

Next, you can use the AWS CDK to create and deploy applications on Arm-based compute powered by AWS Graviton. To learn how you can use the CDK and Amazon Elastic Container Service (ECS) to run containers on Arm-based compute, see [Deploy containers on Arm-based compute using Amazon ECS and the AWS CDK](/learning-paths/servers-and-cloud-computing/aws-cdk/).
