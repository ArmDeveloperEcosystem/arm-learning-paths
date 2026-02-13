---
title: Set up your NVIDIA DGX Spark
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

The NVIDIA DGX Spark pairs an Arm-based Grace CPU with a Blackwell GPU in a compact desktop form factor. The GPU handles the compute-intensive training passes while the Grace CPU manages data preprocessing and orchestration, making the system well suited for fine-tuning large language models locally without sending data to the cloud.

To get started, you'll configure Docker, pull a pre-built PyTorch container, and install the libraries you need for fine-tuning.

## Configure Docker permissions

Docker is pre-installed on the DGX Spark, so you don't need to install it yourself. However, your user account might not have permission to run Docker commands without `sudo`.

Check whether Docker is accessible by opening a terminal and running:

```bash
docker images
```

If this prints a table (even an empty one), you're all set and can skip ahead to the next section. If you see a `permission denied` error, add your user to the `docker` group:

```bash
sudo usermod -aG docker $USER
newgrp docker
```

The first command grants your user Docker access, and `newgrp docker` activates the new group membership in your current shell so you don't need to log out and back in. Verify that it worked by running `docker images` again. You should now see the table without any errors.

## Download PyTorch container

NVIDIA provides pre-built PyTorch containers that include all the necessary frameworks, libraries, and dependencies optimized for NVIDIA GPUs. These containers are regularly updated and maintained, ensuring you have access to the latest stable versions without the complexity of manual dependency management.

Pull the latest PyTorch container from NVIDIA's container registry:

```bash
docker pull nvcr.io/nvidia/pytorch:25.11-py3
```

This command downloads the November 2025 release of the PyTorch container, which includes PyTorch, CUDA libraries, cuDNN, and other essential tools pre-configured for optimal performance on NVIDIA hardware. The download size is several gigabytes, so this step might take a few minutes depending on your internet connection.

## Launch container instance

Now that you have the container image, you can launch an interactive session where you'll perform all your fine-tuning work.

Run the following command to start the container:

```bash
docker run --gpus all -it --rm --ipc=host \
-v $HOME/.cache/huggingface:/root/.cache/huggingface \
-v ${PWD}:/workspace -w /workspace \
nvcr.io/nvidia/pytorch:25.11-py3
```

Here's what each flag does:

- `--gpus all` gives the container access to all available GPUs on your system
- `--ipc=host` enables shared memory between the host and container, which is essential for multi-GPU training and data loading
- `-v $HOME/.cache/huggingface:/root/.cache/huggingface` mounts your Hugging Face cache directory, preventing repeated downloads of models and datasets
- `-v ${PWD}:/workspace -w /workspace` mounts your current directory into the container and sets it as the working directory, so you can access the fine-tuned model from outside the container later

After running the command, you'll be inside the container with a root shell prompt.

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

First, obtain an access token from your [Hugging Face token settings](https://huggingface.co/settings/tokens) page. Then authenticate:

```bash
hf auth login
```

When prompted, paste your token and press Enter. When asked about git credentials, enter `n` since you don't need git integration for this workflow. This authentication persists across sessions because you mounted your Hugging Face cache directory, so you won't need to repeat this step.

## Download NVIDIA DGX Spark playbook

NVIDIA provides a collection of ready-to-use fine-tuning scripts optimized for DGX systems. These scripts implement best practices for various model sizes and fine-tuning techniques, so you can focus on your dataset and model selection rather than training boilerplate.

Clone the playbooks repository:

```bash
git clone https://github.com/NVIDIA/dgx-spark-playbooks
cd dgx-spark-playbooks
git checkout e51dae47ec9233ccd722dd465be87a984fd97d61
cd nvidia/pytorch-fine-tune/assets
```

The repository contains scripts for different model architectures and training strategies. The `assets` directory includes the fine-tuning scripts you'll use in the next steps. Each script is preconfigured with sensible defaults but also accepts command-line arguments for customization.

## What you've accomplished and what's next

In this section you:

- Configured Docker permissions on DGX Spark
- Pulled the NVIDIA PyTorch container and launched an interactive session
- Installed fine-tuning libraries and authenticated with Hugging Face
- Cloned the DGX Spark playbooks repository

In the next section, you'll learn how supervised fine-tuning works and what makes it effective for adapting pre-trained models to specific tasks.
