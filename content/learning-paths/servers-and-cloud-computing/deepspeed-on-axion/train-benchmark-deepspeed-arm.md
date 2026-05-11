---
title: Train and Benchmark AI Workloads on GCP Axion (Arm)
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Train and Benchmark AI Workloads on GCP Axion (Arm)

This section demonstrates neural network training and benchmarking on GCP Axion Arm64 processors using PyTorch.

## Learning Objectives

- Create AI training workloads
- Train neural network models
- Benchmark CPU workloads
- Measure Arm64 AI performance
- Validate large model execution


## Activate environment
Activate the Python virtual environment created during the installation setup.

```bash
source ~/deepspeed-env/bin/activate
```

Go to project directory:

```bash
cd ~/deepspeed-demo
```

## Baseline AI Training Workload

This section creates and executes a lightweight neural network training workload to validate the AI/ML environment on GCP Axion Arm64 processors.

### Create baseline training script

Create the baseline training script:

```bash
cat > train.py << 'EOF'
import torch
import torch.nn as nn
import torch.optim as optim
import time

class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()

        self.net = nn.Sequential(
            nn.Linear(128, 256),
            nn.ReLU(),
            nn.Linear(256, 64),
            nn.ReLU(),
            nn.Linear(64, 1)
        )

    def forward(self, x):
        return self.net(x)

model = SimpleModel()

optimizer = optim.Adam(model.parameters(), lr=0.001)

data = torch.randn(5000, 128)
target = torch.randn(5000, 1)

start = time.time()

for epoch in range(5):

    total_loss = 0

    for i in range(0, len(data), 32):

        x = data[i:i+32]
        y = target[i:i+32]

        output = model(x)

        loss = ((output - y) ** 2).mean()

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch {epoch+1}, Loss: {total_loss}")

end = time.time()

print("Total Training Time:", end - start)
EOF
```

### What this script does

The script performs the following tasks:

- Creates a multi-layer neural network using PyTorch
- Generates synthetic training data
- Executes forward and backward propagation
- Optimizes the model using Adam optimizer
- Measures total training execution time

The model architecture contains:

- Input layer: 128 features
- Hidden layers: 256 and 64 neurons
- Output layer: 1 neuron


### Execute baseline training

```bash
python train.py
```

Expected output:

```output
Epoch 1, Loss: 155.41862654685974
Epoch 2, Loss: 146.19861325621605
Epoch 3, Loss: 130.47488084435463
Epoch 4, Loss: 100.75305489450693
Epoch 5, Loss: 65.7514722738415
Total Training Time: 0.7545099258422852
```

### Analyze baseline results

Observe the following:

- Loss decreases continuously across epochs
- The model is learning successfully
- Training completes in less than one second
- Axion Arm64 processors efficiently execute small AI workloads

The decreasing loss confirms that:

- Gradient updates are working correctly
- CPU computation pipeline is stable
- PyTorch runtime is functioning properly on Arm64

### Benchmark baseline workload
Measure real execution time:

```bash
time python train.py | tee pytorch_baseline_result.txt
```

Example output:

```output
Epoch 1, Loss: 160.0170536339283
Epoch 2, Loss: 151.6725998222828
Epoch 3, Loss: 136.18832343816757
Epoch 4, Loss: 108.03106728196144
Epoch 5, Loss: 73.08194716647267
Total Training Time: 0.7314252853393555

real    0m2.172s
user    0m3.700s
sys     0m0.137s
```

The benchmark output provides:

| Metric | Description |
|---|---|
| real | Total wall-clock execution time |
| user | CPU execution time spent in user space |
| sys | CPU time spent in kernel operations |

The results indicate:

- Fast execution on Arm64 CPUs
- Efficient tensor computation
- Low system overhead

## Large Scale AI Benchmark

This section increases:

- dataset size
- model complexity
- CPU workload intensity

This helps evaluate scalable AI training performance on Axion Arm processors.


### Create large benchmark workload

```bash
cat > train_large.py << 'EOF'
import torch
import torch.nn as nn
import torch.optim as optim
import time
import os

torch.set_num_threads(os.cpu_count())

class LargeModel(nn.Module):
    def __init__(self):
        super().__init__()

        self.net = nn.Sequential(
            nn.Linear(512, 1024),
            nn.ReLU(),
            nn.Linear(1024, 512),
            nn.ReLU(),
            nn.Linear(512, 128),
            nn.ReLU(),
            nn.Linear(128, 1)
        )

    def forward(self, x):
        return self.net(x)

model = LargeModel()

optimizer = optim.Adam(model.parameters(), lr=0.001)

data = torch.randn(20000, 512)
target = torch.randn(20000, 1)

start = time.time()

for epoch in range(5):

    total_loss = 0

    for i in range(0, len(data), 64):

        x = data[i:i+64]
        y = target[i:i+64]

        output = model(x)

        loss = ((output - y) ** 2).mean()

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch {epoch+1}, Loss: {total_loss}")

end = time.time()

print("Total Training Time:", end - start)
EOF
```

### What this workload changes

Compared to the baseline workload:

| Component | Baseline | Large Benchmark |
|---|---|---|
| Features | 128 | 512 |
| Dataset Size | 5,000 | 20,000 |
| Batch Size | 32 | 64 |
| Model Complexity | Smaller | Larger |

The benchmark stresses:

- CPU compute capability
- Memory bandwidth
- Tensor operation throughput
- Multi-threaded execution


### Run large benchmark

```bash
time python train_large.py | tee pytorch_large_result.txt
```

Expected output:

```text
Epoch 1, Loss: 319.07712411880493
Epoch 2, Loss: 308.4675619006157
Epoch 3, Loss: 273.5877128839493
Epoch 4, Loss: 227.81050024926662
Epoch 5, Loss: 194.74351280927658
Total Training Time: 4.878139972686768

real    0m6.346s
user    0m19.630s
sys     0m0.251s
```

### Analyze large workload results

The large benchmark demonstrates:

- Stable execution under higher CPU load
- Increased training duration due to larger tensors
- Effective CPU thread utilization
- Successful Arm64 scaling behavior

Key observations:

- Training remains stable
- Loss decreases consistently
- CPU utilization increases significantly
- Multi-core execution improves performance

## Monitor CPU utilization

Open another terminal.

Run:

```bash
top
```

In the first terminal:

```bash
python train_large.py
```

Observe:

- CPU usage
- Memory utilization
- Python process behavior


## Verify generated files

```bash
ls -lh
```

The output is similar to:

```output
environment.txt
pytorch_baseline_result.txt
pytorch_large_result.txt
train.py
train_large.py
```

## Benchmark observations

| Workload | Approx Training Time |
|---|---|
| Baseline Model | ~0.8 seconds |
| Large Model | ~5.4 seconds |

These files contain:

| File | Purpose |
|---|---|
| train.py | Baseline training workload |
| train_large.py | Large benchmark workload |
| pytorch_baseline_result.txt | Baseline benchmark results |
| pytorch_large_result.txt | Large benchmark results |

## Benchmark Summary

| Workload | Training Time | Observation |
|---|---|---|
| Baseline Model | ~0.7–0.8 seconds | Fast lightweight execution |
| Large Benchmark | ~4.8–5.4 seconds | Higher CPU utilization and larger workload handling |


## Result Analysis

The benchmark validates that:

- GCP Axion Arm64 processors can efficiently execute AI workloads
- PyTorch runs successfully on Arm64 architecture
- CPU-only AI training is stable on SUSE Arm64
- Larger workloads scale predictably with increased compute demand

The benchmark also demonstrates:

- Multi-layer neural network execution
- Tensor computation stability
- Efficient CPU utilization on Arm64 processors


## What you've learned

You have learned how to:

- Create AI training workloads
- Train neural network models on Arm64
- Benchmark CPU-based AI workloads
- Measure training execution performance
- Validate scalable AI execution on GCP Axion
- Analyze workload scaling behavior
- Explore distributed AI training
