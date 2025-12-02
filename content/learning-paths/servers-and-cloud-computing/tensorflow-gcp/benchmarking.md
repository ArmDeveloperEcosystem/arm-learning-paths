---
title: Benchmark TensorFlow model performance using tf.keras
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Benchmark TensorFlow models

This section benchmarks multiple TensorFlow models (ResNet50, MobileNetV2, and InceptionV3) using dummy input data. You'll measure average inference time and throughput for each model running on the CPU.

tf.keras is TensorFlow's high-level API for building, training, and benchmarking deep learning models. It provides access to predefined architectures such as ResNet, MobileNet, and Inception, making it easy to evaluate model performance on different hardware setups.

### Activate your virtual environment

Enable your isolated Python environment where TensorFlow is installed:

```console
source ~/tf-venv/bin/activate
python -c "import tensorflow as tf; print(tf.__version__)"
```

This ensures that all TensorFlow-related packages run in a clean, controlled setup without affecting system-wide Python installations.

### Install required packages

Install TensorFlow and NumPy for model creation and benchmarking:

```console
pip install tensorflow==2.20.0 numpy
```

These packages are likely already installed from the previous installation steps. NumPy supports efficient numerical operations, while TensorFlow handles deep learning workloads.

### Create the benchmark script

Use an editor to create a Python script named `tf_cpu_benchmark.py` that will run TensorFlow model benchmarking tests.

Add the following code to benchmark three different model architectures:

```python
import tensorflow as tf
import time

# List of models to benchmark
models = {
    "ResNet50": tf.keras.applications.ResNet50,
    "MobileNetV2": tf.keras.applications.MobileNetV2,
    "InceptionV3": tf.keras.applications.InceptionV3
}

batch_size = 32
num_runs = 50

for name, constructor in models.items():
    print(f"\nBenchmarking {name}...")
    # Create model without pretrained weights
    model = constructor(weights=None, input_shape=(224,224,3))
    # Generate dummy input
    dummy_input = tf.random.uniform([batch_size, 224, 224, 3])
    # Warm-up
    _ = model(dummy_input)
    # Benchmark
    start = time.time()
    for _ in range(num_runs):
        _ = model(dummy_input)
    end = time.time()
    avg_time = (end - start) / num_runs
    throughput = batch_size / avg_time
    print(f"{name} average inference time per batch: {avg_time:.4f} seconds")
    print(f"{name} throughput: {throughput:.2f} images/sec")
```

This script creates model instances without pretrained weights for fair CPU testing, generates random image data for inference, includes a warm-up phase to stabilize model performance, and measures inference time over 50 runs to calculate average performance and throughput.

### Run the benchmark

Execute the benchmarking script:

```console
python tf_cpu_benchmark.py
```

The output is similar to:

```output
Benchmarking ResNet50...
ResNet50 average inference time per batch: 1.2051 seconds
ResNet50 throughput: 26.55 images/sec

Benchmarking MobileNetV2...
MobileNetV2 average inference time per batch: 0.2909 seconds
MobileNetV2 throughput: 110.02 images/sec

Benchmarking InceptionV3...
InceptionV3 average inference time per batch: 0.8971 seconds
InceptionV3 throughput: 35.67 images/sec
```

### Understand the results

The benchmark provides key performance metrics. Average inference time per batch measures how long it takes to process one batch of input data, with lower values indicating faster performance. Throughput shows how many images the model can process per second, with higher values indicating better efficiency.

### Performance summary

The following table shows results from running the benchmark on a `c4a-standard-4` (4 vCPU, 16 GB memory) aarch64 VM in GCP using SUSE:

| Model       | Average Inference Time per Batch (seconds) | Throughput (images/sec) |
|-------------|-------------------------------------------:|------------------------:|
| ResNet50    | 1.2051                                     | 26.55                   |
| MobileNetV2 | 0.2909                                     | 110.02                  |
| InceptionV3 | 0.8971                                     | 35.67                   |

The results demonstrate strong performance for lightweight CNNs like MobileNetV2, achieving over 110 images/sec on the aarch64 platform. Medium-depth models like InceptionV3 maintain balanced performance between accuracy and latency. Heavier architectures such as ResNet50 show longer inference times but deliver stable throughput, confirming that TensorFlow workloads run efficiently on Arm processors and provide a cost-effective alternative for AI inference tasks.
