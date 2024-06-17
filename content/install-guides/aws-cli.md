---
additional_search_terms:
- cloud
- deploy


layout: installtoolsall
minutes_to_complete: 15
author_primary: Jason Andrews
multi_install: false
multitool_install_part: false
official_docs: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html
test_images:
- ubuntu:latest
test_link: null
test_maintenance: false
test_status:
- passed
title: AWS CLI
tool_install: true
weight: 1
---

[AWS CLI](https://docs.aws.amazon.com/cli/index.html) is a cross-platform command-line tool that can be installed on development computers. The AWS Command Line Interface (AWS CLI) is a unified tool that provides a consistent interface for interacting with all parts of Amazon Web Services. 

It is available for a variety of operating systems and Linux distributions, supports the Arm architecture and has multiple ways to install it. 

## What should I do before installing AWS CLI?

This article provides quick solutions to install the latest version of AWS CLI, version 2, for Ubuntu on Arm.

Confirm you are using an Arm computer with 64-bit Linux by running:

```bash { target="ubuntu:latest" }
uname -m
```

The output should be:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

## How do I download and install AWS CLI version 2?

The easiest way to install the latest version of the AWS CLI for Ubuntu on Arm is to download and run the installer from AWS.

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

Confirm the CLI version 2 is available by invoking the `aws` command to print the version.

```bash { target="ubuntu:latest" }
aws --version
```

Review [AWS CLI v2 is now generally available](https://aws.amazon.com/blogs/developer/aws-cli-v2-is-now-generally-available/) to review the new features in version 2. 

You now have the latest version of the AWS CLI installed. Follow [this guide](/install-guides/aws_access_keys/) to generate and configure access keys needed to use the AWS CLI.
