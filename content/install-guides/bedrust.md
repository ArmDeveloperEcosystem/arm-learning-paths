---
title: Bedrust - invoke models on Amazon Bedrock
minutes_to_complete: 10
author: Jason Andrews

additional_search_terms:
- rust
- aws

layout: installtoolsall

multi_install: false
multitool_install_part: false
official_docs: https://github.com/darko-mesaros/bedrust
test_images:
- ubuntu:latest
test_maintenance: true
tool_install: true
weight: 1
---

Bedrust is a command-line program that you can use to invoke models on Amazon Bedrock. Amazon Bedrock is a managed service on Amazon Web Services (AWS) that allows developers to build and scale generative AI applications using foundation models (FMs) from leading AI model providers.

Bedrust is available as Rust source code, and you can build and run it on an Arm Linux computer. 

## Before you begin

You'll need an [AWS account](https://aws.amazon.com) to access Bedrock. To learn how to create an AWS account, see [Create an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html).

To use Bedrust, you need to:

- Configure your AWS account credentials to talk to the Bedrock service
- Enable foundation model access in the Bedrock console

### Configure credentials

To connect to Bedrock, you need to install the [AWS CLI](/install-guides/aws-cli/), generate an access key ID and secret access key, and use the `aws configure` command to enter your credentials. 

For more information about configuring credentials, see [AWS Credentials](/install-guides/aws_access_keys/). 

### Enable model access in Bedrock

To use Bedrock models, you need to request access to specific foundation models through the Amazon Bedrock console. 

In your AWS account, navigate to **Model access** in the Bedrock console and select the models you want to use. 

For more information, see [Access Amazon Bedrock foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html).

## Download and install Bedrust

One way to install Bedrust is by using Cargo, the Rust package manager. 

### Install Rust

Ensure you have Rust and Cargo installed on your computer. If not, install them using the following commands: 

```bash
sudo apt install curl gcc -y
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
source "$HOME/.cargo/env"
```

For more information, see the [Rust install guide](/install-guides/rust/).

### Clone the repository and install Bedrust

Get the Bedrust source code:

```bash
git clone https://github.com/darko-mesaros/bedrust.git
cd bedrust
```

With Rust and Cargo installed, you can install Bedrust:

```bash
cargo install bedrust
```

### Verify the installation

After installation, confirm that Bedrust is installed and available in your search path by checking the version:

```bash
bedrust --version
```

The output is similar to:

```output
bedrust 0.8.8
```

## Configure Bedrust

You can set the default foundation model you want to use:

```console
bedrust --init
```

Use the menu to select the default model:

```output
📜 | Initializing Bedrust configuration.
? Select a default model to use press <enter> to skip ›
  meta.llama2-70b-chat-v1
  meta.llama3-1-405b-instruct-v1:0
  meta.llama3-1-70b-instruct-v1:0
  meta.llama3-1-8b-instruct-v1:0
  cohere.command-text-v14
  anthropic.claude-v2
  anthropic.claude-v2:1
  anthropic.claude-3-opus-20240229-v1:0
  anthropic.claude-3-sonnet-20240229-v1:0
  anthropic.claude-3-haiku-20240307-v1:0
  anthropic.claude-3-5-sonnet-20240620-v1:0
  anthropic.claude-3-5-sonnet-20241022-v2:0
  us.anthropic.claude-3-7-sonnet-20250219-v1:0
  anthropic.claude-3-5-haiku-20241022-v1:0
  ai21.j2-ultra-v1
  us.deepseek.r1-v1:0
  amazon.titan-text-express-v1
  mistral.mixtral-8x7b-instruct-v0:1
  mistral.mistral-7b-instruct-v0:2
  mistral.mistral-large-2402-v1:0
  mistral.mistral-large-2407-v1:0
  us.amazon.nova-micro-v1:0
  us.amazon.nova-lite-v1:0
  us.amazon.nova-pro-v1:0
```

## How to use Bedrust

Run `bedrust` to invoke the CLI with the default model.

```console
bedrust 
```

You'll see the prompt and can start asking questions such as `how do I install the AWS CLI?` to see how it works.

```output
bedrust
██████╗ ███████╗██████╗ ██████╗ ██╗   ██╗███████╗████████╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██║   ██║██╔════╝╚══██╔══╝
██████╔╝█████╗  ██║  ██║██████╔╝██║   ██║███████╗   ██║
██╔══██╗██╔══╝  ██║  ██║██╔══██╗██║   ██║╚════██║   ██║
██████╔╝███████╗██████╔╝██║  ██║╚██████╔╝███████║   ██║
╚═════╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝


----------------------------------------
Currently supported chat commands:
/c	 - Clear current chat history
/s	 - (BETA) Save chat history
/r	 - (BETA) Recall and load a chat history
/h	 - (BETA) Export history as HTML(saves in current dir)
/q	 - Quit
----------------------------------------

----------------------------------------
🤖 | What would you like to know today?
😎 | Human:
```

## Change foundation models

You can use `-m` to change the model:

```console
bedrust -m nova-micro
```

Your queries are now sent to the Amazon Nova Micro model.

## Identify which models you can use

Use `--help` to see your models. 

```console
bedrust --help
```

The output is similar to:

```output
A command-line tool to invoke and work with Large Language models on AWS, using Amazon Bedrock

Usage: bedrust [OPTIONS]

Options:
      --init
  -m, --model-id <MODEL_ID>  [possible values: llama270b, llama31405b-instruct, llama3170b-instruct, llama318b-instruct, cohere-command, claude-v2, claude-v21, claude-v3-opus, claude-v3-sonnet, claude-v3-haiku, claude-v35-sonnet, claude-v352-sonnet, claude-v37-sonnet, claude-v35-haiku, jurrasic2-ultra, deep-seek-r1, titan-text-express-v1, mixtral8x7b-instruct, mistral7b-instruct, mistral-large, mistral-large2, nova-micro, nova-lite, nova-pro]
  -c, --caption <CAPTION>
  -s, --source <SOURCE>
  -x
  -h, --help                 Print help
  -V, --version              Print version
```

The output shows the model strings you can use. Make sure to enable the models you want to use in the Bedrock console. 

You are now ready to use Bedrust as a quick way to explore many Bedrock models and compare them.



