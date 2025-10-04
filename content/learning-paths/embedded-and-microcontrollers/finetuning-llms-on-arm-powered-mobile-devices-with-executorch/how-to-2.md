---
title: Large Language Model - Setup Environment 
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Large Language Model - Setup Environment

#### Plartform Required 
- An AWS Graviton4 r8g.16xlarge instance to test Arm performance optimizations, or any [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider or an on-premise Arm server or Arm based laptop.
- An Arm-powered smartphone with the i8mm feature running Android, with 16GB of RAM.
- A USB cable to connect your smartphone to your development machine.

#### Set Up Required Libraries
The following commands install the necessary libraries for the task, including Hugging Face Transformers, Datasets, and fine-tuning methods. These libraries facilitate model loading, training, and fine-tuning

###### The transformers library (by Hugging Face) provides pre-trained LLMs
```python
!pip install transformers

```
###### This installs transformers along with PyTorch, ensuring that models are trained and fine-tuned using the Torch backend.
```python
!pip install transformers[torch]
```
###### The datasets library (by Hugging Face) provides access to a vast collection of pre-built datasets

```python
!pip install datasets
```
###### The evaluate library provides metrics for model performance assessment

```python
!pip install evaluate
```
###### Speed up fine-tuning of Large Language Models (LLMs)
Use a library designed to speed up fine-tuning of Large Language Models (LLMs) while reducing computational costs, optimizes training efficiency, particularly for LoRA (Low-Rank Adaptation) fine-tuning 


```
Used pre-fine-tuned customer support model
```

###### AWS Graviton3 Instance Setup
Launch EC2 Instance:


```
Recommended instance: c7g.xlarge or c7g.2xlarge
- c7g.xlarge: 4 vCPUs, 8 GB RAM 
- c7g.2xlarge: 8 vCPUs, 16 GB RAM 

Connect to your instance
ssh -i your-key.pem ubuntu@your-instance-ip
```

###### System Setup:
Launch EC2 Instance:


```
Update system
sudo apt update && sudo apt upgrade -y

Install essential packages
sudo apt install -y build-essential git wget curl \
    python3-pip python3-venv htop

Verify ARM architecture
uname -m  # Should show: aarch64
```

###### Python Environment Setup



```
Create virtual environment
python3 -m venv chatbot_env
source chatbot_env/bin/activate

Upgrade pip
pip install --upgrade pip

Install PyTorch for ARM/CPU
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

Install Transformers and utilities
pip install transformers==4.36.0
pip install datasets accelerate
pip install huggingface-hub
pip install flask psutil
pip install numpy pandas

Verify installation
python -c "import torch; print(f'PyTorch version: {torch.__version__}')"
python -c "import torch; print(f'CPU available: {torch.cpu.device_count()}')"
```