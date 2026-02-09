---
title: Setup your NVIDIA DGX Spark
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

The following section comes from the [NVIDIA Developer Program](https://build.nvidia.com/spark/pytorch-fine-tune/instructions) site.

## Configure Docker permissions

Before you can run containerized workloads, you need to ensure your user account has the necessary permissions to interact with Docker. By default, Docker requires root privileges in Ubuntu, which means you would need to prefix every Docker command with `sudo`. Adding your user to the `docker` group eliminates this requirement and streamlines your workflow.

Open a terminal and test your current Docker access:

```bash
docker ps
```

If you see a permission denied error (something like `permission denied while trying to connect to the Docker daemon socket`), you need to add your user to the docker group:

```bash
sudo usermod -aG docker $USER
newgrp docker
```

The `usermod` command adds your user to the docker group, while `newgrp docker` activates the group membership immediately without requiring you to log out and back in. After running these commands, you should be able to execute Docker commands without sudo.

## Download PyTorch container

NVIDIA provides pre-built PyTorch containers that include all the necessary frameworks, libraries, and dependencies optimized for NVIDIA GPUs. These containers are regularly updated and maintained, ensuring you have access to the latest stable versions without the complexity of manual dependency management.

Pull the latest PyTorch container from NVIDIA's container registry:

```bash
docker pull nvcr.io/nvidia/pytorch:25.11-py3
```

This command downloads the November 2025 release of the PyTorch container, which includes PyTorch, CUDA libraries, cuDNN, and other essential tools pre-configured for optimal performance on NVIDIA hardware. The download size is several gigabytes, so this step might take a few minutes depending on your internet connection.

## Launch container instance

Now that you have the container image downloaded, you can launch an interactive container session. This creates an isolated environment where you'll perform all your fine-tuning work.

Run the following command to start the container:

```bash
docker run --gpus all -it --rm --ipc=host \
-v $HOME/.cache/huggingface:/root/.cache/huggingface \
-v ${PWD}:/workspace -w /workspace \
nvcr.io/nvidia/pytorch:25.11-py3
```

This command includes several important flags:

- `--gpus all` gives the container access to all available GPUs on your system
- `--ipc=host` enables shared memory between the host and container, which is essential for multi-GPU training and data loading
- `-v $HOME/.cache/huggingface:/root/.cache/huggingface` mounts your Hugging Face cache directory, preventing repeated downloads of models and datasets
- `-v ${PWD}:/workspace -w /workspace` mounts your current directory into the container and sets it as the working directory, this will allow you to access the fine-tuned model you will be making from another environment later.

After running this command, you'll be inside the container with a root shell prompt.

## Install dependencies

The base PyTorch container doesn't include all the specialized libraries needed for efficient model fine-tuning. You need to install several additional Python packages that provide transformer models, parameter-efficient fine-tuning methods, dataset utilities, and training frameworks.

Inside the running container, install the required dependencies:

```bash
pip install transformers peft datasets trl bitsandbytes
```

These packages serve specific purposes:

- `transformers` provides access to pre-trained language models and tokenizers from Hugging Face
- `peft` (Parameter-Efficient Fine-Tuning) enables techniques like LoRA and QLoRA that reduce memory requirements
- `datasets` offers a standardized interface for loading and processing training datasets
- `trl` (Transformer Reinforcement Learning) includes training utilities and recipes for language models
- `bitsandbytes` enables 4-bit and 8-bit quantization for memory-efficient training

The installation typically takes a few minutes as pip downloads and installs each package along with their dependencies.

## Authenticate with Hugging Face

Many of the models you'll fine-tune are hosted on Hugging Face's model hub. Some models, particularly larger ones like Llama, require authentication to download. Even for public models, authentication provides better rate limits and tracking.

First, obtain a Hugging Face access token from [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens). Then authenticate:

```bash
huggingface-cli login
```

When prompted, paste your token and press Enter. When asked about git credentials, enter `n` since you don't need git integration for this workflow. This authentication persists across sessions because you mounted your Hugging Face cache directory, so you won't need to repeat this step.

## Download NVIDIA DGX Spark playbook

NVIDIA provides a collection of ready-to-use fine-tuning scripts specifically optimized for DGX systems. These scripts implement best practices for various model sizes and fine-tuning techniques, saving you from writing training code from scratch.

Clone the playbooks repository:

```bash
git clone https://github.com/NVIDIA/dgx-spark-playbooks
cd dgx-spark-playbooks/nvidia/pytorch-fine-tune/assets
```

The repository contains scripts for different model architectures and training strategies. The `assets` directory includes the fine-tuning scripts you'll use in the next steps. Each script is preconfigured with sensible defaults but also accepts command-line arguments for customization.

