---
title: Train and benchmark AI workloads on an Arm-based Google Axion virtual machine
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare training and benchmarking AI workloads

In this section, you'll run neural network training and benchmarking workloads on an Arm-based Google Axion C4A VM using PyTorch. You'll run two workloads: a small baseline model to verify the environment, and a larger benchmark to evaluate CPU scaling behavior.

If you're continuing in the same SSH session from the previous section, the `deepspeed-env` virtual environment is already active and your working directory is `~/deepspeed-demo`. If you've opened a new session, re-activate the environment and navigate to the project directory:

```bash
source ~/deepspeed-env/bin/activate
cd ~/deepspeed-demo
```
## Set up a baseline

First, create and run a baseline model to verify the environment.

### Create a baseline training workload

Create a lightweight neural network training script to verify the environment. The script defines a three-layer feedforward network and generates synthetic training data. It runs five epochs of mini-batch gradient descent using the Adam optimizer, and prints the total training time:

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

### Run the baseline training workload

Run the training script:

```bash
python train.py
```

The output is similar to:

```output
Epoch 1, Loss: 155.41862654685974
Epoch 2, Loss: 146.19861325621605
Epoch 3, Loss: 130.47488084435463
Epoch 4, Loss: 100.75305489450693
Epoch 5, Loss: 65.7514722738415
Total Training Time: 0.7545099258422852
```

The loss decreases across all five epochs, confirming that gradient updates are working correctly and PyTorch is running properly on Arm64.

### Run the baseline with timing

Run the same script under `time` and save the output for comparison:

```bash
time python train.py | tee pytorch_baseline_result.txt
```

The output is similar to:

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

The `real` time is the total wall-clock duration. The `user` time exceeds `real` time here because PyTorch uses multiple threads across all 4 vCPUs, so CPU time is summed across cores.

## Set up a large-scale benchmark

After creating and running the baseline workload, create a large-scale benchmark to evaluate CPU behavior.

### Create a large-scale benchmark

This workload increases dataset size, input dimensionality, batch size, and model depth to stress CPU compute, memory bandwidth, and tensor operation throughput. It also calls `torch.set_num_threads(os.cpu_count())` to explicitly pin PyTorch to all available cores:

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

To observe CPU utilization while this runs, open a second terminal and run `top`. Look for the Python process — the CPU percentage reflects multi-threaded utilization across all 4 vCPUs.

### Run the large benchmark with timing

Run the benchmark script under `time`:

```bash
time python train_large.py | tee pytorch_large_result.txt
```

The output is similar to:

```output
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

Training time scales roughly linearly with dataset size and model depth. The `user` time being approximately 4x `real` time indicates that PyTorch is distributing work across all 4 vCPUs effectively.

## Review benchmark outputs

After both scripts complete, review the timing outputs and compare the two workloads.

### Verify generated files for both workloads

Confirm that the output files are present:

```bash
ls -lh
```

The output is similar to:

```output
-rw-r--r-- 1 user user  12K May 15 13:50 pytorch_baseline_result.txt
-rw-r--r-- 1 user user  12K May 15 13:55 pytorch_large_result.txt
-rw-r--r-- 1 user user 1.1K May 15 13:48 train.py
-rw-r--r-- 1 user user 1.2K May 15 13:48 train_large.py
```

### Compare training times

The following table describes approximate training times:

| Workload | Approximate training time |
|---|---|
| Baseline model (5K samples, 128 features) | ~0.7–0.8 seconds |
| Large benchmark (20K samples, 512 features) | ~4.8–5.4 seconds |

Both workloads trained to completion with steadily decreasing loss, indicating stable PyTorch CPU execution on Google Axion C4A. Your results may vary depending on VM load at the time of the run.

## What you've accomplished

You've run two PyTorch training workloads on a Google Axion Arm64 VM, measured wall-clock and CPU execution time, and confirmed stable multi-threaded neural network training on SUSE Linux.
