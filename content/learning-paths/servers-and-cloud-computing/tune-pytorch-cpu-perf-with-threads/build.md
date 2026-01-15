---
title: Set up the environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin

Before you can tune PyTorch threading for LLM inference on Arm CPUs, you need to set up your development environment with Docker, PyTorch, and access to the Gemma-3 models from Hugging Face. This section walks you through creating your Hugging Face account, configuring an Arm server, and running the PyTorch container with all necessary dependencies.

{{% notice Note %}}
This Learning Path uses Arm's downstream canary release of PyTorch, which includes ready-to-use examples and scripts. This release provides access to the latest features but is intended for experimentation rather than production use.
{{% /notice %}}

## Create a Hugging Face account

Create a [Hugging Face account](https://huggingface.co/) if you don't already have one. After creating your account, request access to the [1B](https://huggingface.co/google/gemma-3-1b-it) and [270M](https://huggingface.co/google/gemma-3-270m-it) variants of Google's Gemma-3 model. Access is typically granted within 15 minutes.

## Connect to an Arm system and install Docker

If this is your first time using Arm-based cloud instances, see the [getting started guide](/learning-paths/servers-and-cloud-computing/csp/).

The example code uses an AWS Graviton 4 (`m8g.24xlarge`) instance running Ubuntu 24.04 LTS, based on the Neoverse V2 architecture. You can use any Arm server with at least 16 cores. Keep note of your CPU count so you can adjust the example code as needed. 

Install Docker using the [Docker install guide](/install-guides/docker/) or the [official documentation](https://docs.docker.com/engine/install/ubuntu/). Follow the post-installation steps to configure Docker for non-root usage. 

## Run the PyTorch-aarch64 Docker container image

You have two options for the Docker container. You can use a container image from Docker Hub or you can build the container image from source. Using a ready-made container makes it easier to get started, and building from source provides the latest software. The container image on Docker Hub is updated about once a month.

Open a terminal or use SSH to connect to your Arm Linux system.

### Use container image from Docker Hub

Download the ready-made container image from Docker Hub:

```bash
docker pull armlimited/pytorch-arm-neoverse:latest
```

Create a new container:

```bash
docker run --rm -it armlimited/pytorch-arm-neoverse:latest
```

The shell prompt will appear, and you are ready to start. 

```output
aarch64_pytorch ~> 
```

### Build from source

To build from source, clone the repository.

```bash
git clone https://github.com/ARM-software/Tool-Solutions.git
cd Tool-Solutions/ML-Frameworks/pytorch-aarch64/
```

Build the container:

```bash
./build.sh -n $(nproc - 1)
```

On a 96-core instance such as AWS `m8g.24xlarge`, this build takes approximately 20 minutes.

After the build completes, create a Docker container. Replace `<version>` with the version of torch and torchao that was built:

```bash
./dockerize.sh ./results/torch-<version>-linux_aarch64.whl ./results/torchao-<version>-py3-none-any.whl 
```

The shell prompt will appear, and you are ready to start. 

```output
aarch64_pytorch ~> 
```

## Log in to Hugging Face

Create a new Read token on Hugging Face by navigating to [Create new Access Token](https://huggingface.co/settings/tokens/new?tokenType=read).

![Screenshot of Hugging Face token creation interface showing a dialog box with fields for token name and type, with the 'Read' option selected and a 'Create token' button visible alt-txt#center](./hf-access-token.jpg "Hugging Face token creation interface")

Provide a token name, create the token, and copy the generated value. From within the Docker container, run the following command and paste the token when prompted:

```bash
huggingface-cli login
```

Messages indicating the token is valid and login is successful are printed.

Be aware that the login doesn't persist after the Docker container exits. You'll need to log in again if you restart the container.

## What you've accomplished and what's next

You've set up your environment with:
- A Hugging Face account with access to the Gemma-3 models
- An Arm server or cloud instance with Docker installed
- The PyTorch-aarch64 container running and authenticated

You're now ready to run LLM inference experiments and measure how thread count affects performance.