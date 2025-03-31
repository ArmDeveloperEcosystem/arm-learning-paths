---
title: Amazon Q Developer CLI

draft: true

author: Jason Andrews
minutes_to_complete: 10
official_docs: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line.html

test_maintenance: true
test_images:
- ubuntu:latest

layout: installtoolsall
multi_install: false
multitool_install_part: false
tool_install: true
weight: 1
---

Amazon Q Developer for the command line is a CLI tool for Amazon Q, a generative artificial intelligence (AI) powered assistant. You can use it to ask questions about AWS architecture and resources in addition to general developer tasks. 

It is available for a variety of operating systems and Linux distributions, supports the Arm architecture, and has multiple ways to install it.

## What should I do before installing Amazon Q Developer CLI?

You need a Builder ID to use the Amazon Q Developer CLI. If you don't have one, visit [Do more with AWS Builder ID](https://community.aws/builderid) and use the Sign up button to create your Builder ID. 

This guide explains how to install the latest version of the Amazon Q Developer CLI on computers running Arm Linux and macOS.

## How do I download and install Amazon Q Developer CLI?

The CLI is invoked with the `q` command, and you can install it on macOS and Arm Linux. 

### How do I install the Q CLI on macOS?

Install [Homebrew](https://brew.sh/) if it is not already available on your computer.

Install the Q CLI:

```console
brew install amazon-q
```

### How do I install the Q CLI on Arm Linux?

The easiest way to install the latest version of the Q CLI for any Arm Linux distribution is to download and run the installer. 

Before starting, make sure `curl` and `unzip` are available on your computer. 

The commands for Debian-based distributions such as Ubuntu are below. For other Linux distributions use the package manager to install `curl` and `unzip`. 

```bash { target="ubuntu:latest" }
sudo apt update
sudo apt install curl unzip -y
```

Download the zip file with `curl`:

```bash { target="ubuntu:latest" }
curl --proto '=https' --tlsv1.2 -sSf "https://desktop-release.codewhisperer.us-east-1.amazonaws.com/latest/q-aarch64-linux.zip" -o "q.zip"
```

Extract the installer and run it:

```console
unzip q.zip
bash ./q/install.sh
```

Answer the question about updating your shell config. 

```output
✔ Do you want q to modify your shell config (you will have to manually do this otherwise)? 
```

To automate the install add the `--no-confirm` flag to the `install.sh` command. 

{{% notice Note %}}
If you have a Linux distribution with an older version of the GNU C Library or one which does not use the GNU C Library such as Alpine Linux, you can download an alternative package which uses the musl C library and has no external dependencies. 

Substitute the `curl` command above with this one and use the same install instructions:

```bash { target="ubuntu:latest" }
curl "https://desktop-release.codewhisperer.us-east-1.amazonaws.com/latest/q-aarch64-linux-musl.zip" -o "q.zip"
```

{{% /notice %}}

### How do I confirm the Q CLI is working?

You now have the latest version of the Amazon Q Developer CLI installed. 

Confirm the CLI is available by invoking the `q` command to print the version.

```console
q version
```

The version is printed:

```output
q 1.7.2
```

## How can I configure my AWS account to get the most from the Q CLI?

The Q CLI can answer questions and solve problems related to your AWS resources and help you develop faster on AWS. To get the maximum benefit, you can configure the AWS CLI to use your account. 

Follow the [AWS CLI install guide](/install-guides/aws_access_keys/) and the [AWS Credentials install guide](/install-guides/aws_access_keys/) to set up the AWS CLI and generate and configure access keys. 

This allows you to use the Amazon Q Developer CLI to ask questions and solve issues specific to your AWS account. 

## What is an example of using the Q CLI? 

You can use `q chat` to find information about your AWS resources. 

```console
q chat
```

When the chat session starts you see:

```output
Hi, I'm Amazon Q. Ask me anything.

Things to try
• Fix the build failures in this project.
• List my s3 buckets in us-west-2.
• Write unit tests for my application.
• Help me understand my git status

/acceptall    Toggles acceptance prompting for the session.
/profile      (Beta) Manage profiles for the chat session
/context      (Beta) Manage context files for a profile
/help         Show the help dialogue
/quit         Quit the application
```

For example, you can ask for the IP address of an EC2 instance instead of going to the AWS console or looking up the AWS CLI command to get it. 

An example is shown below:

![Connect #center](/install-guides/_images/q.gif)

You are ready to use the Q CLI. 
