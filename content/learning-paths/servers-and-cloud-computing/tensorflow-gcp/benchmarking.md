---
title: TensorFlow Benchmarking
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## TensorFlow Benchmarking with tf.keras
This guide benchmarks multiple TensorFlow models (ResNet50, MobileNetV2, and InceptionV3) using dummy input data. It measures average inference time and throughput for each model running on the CPU.

`tf.keras` is **TensorFlow’s high-level API** for building, training, and benchmarking deep learning models. It provides access to **predefined architectures** such as **ResNet**, **MobileNet**, and **Inception**, making it easy to evaluate model performance on different hardware setups like **CPU**, **GPU**, or **TPU**.

### Activate your TensorFlow virtual environment
This step enables your isolated Python environment (`tf-venv`) where TensorFlow is installed. It ensures that all TensorFlow-related packages and dependencies run in a clean, controlled setup without affecting system-wide Python installations:

```console
source ~/tf-venv/bin/activate
python -c "import tensorflow as tf; print(tf.__version__)"
```
### Install required packages for the benchmark
Here, you install TensorFlow 2.20.0 and NumPy, the core libraries needed for model creation, computation, and benchmarking. NumPy supports efficient numerical operations, while TensorFlow handles deep learning workloads (these packages are likely already installed FYI):

```console
pip install tensorflow==2.20.0 numpy
```

### Create a Python file named tf_cpu_benchmark.py:
This step creates a Python script (`tf_cpu_benchmark.py`) using your favorite editor (showing "edit" as an example below) that will run TensorFlow model benchmarking tests:

```console
edit tf_cpu_benchmark.py
```

Paste the following code:
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
- **Import libraries** – Loads TensorFlow and `time` for model creation and timing.  
- **Define models** – Lists three TensorFlow Keras models: **ResNet50**, **MobileNetV2**, and **InceptionV3**.  
- **Set parameters** – Configures `batch_size = 32` and runs each model **50 times** for stable benchmarking.  
- **Create model instances** – Initializes each model **without pretrained weights** for fair CPU testing.  
- **Generate dummy input** – Creates random data shaped like real images **(224×224×3)** for inference.  
- **Warm-up phase** – Runs one inference to **stabilize model graph and memory usage**.  
- **Benchmark loop** – Measures total time for 50 runs and calculates **average inference time per batch**.  
- **Compute throughput** – Calculates how many **images per second** the model can process.  
- **Print results** – Displays **average inference time and throughput** for each model.  

### Run the benchmark
Execute the benchmarking script:

```console
python tf_cpu_benchmark.py
```

You should see an output similar to:
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

### Benchmark Metrics Explanation

- **Average Inference Time per Batch (seconds):** Measures how long it takes to process one batch of input data. Lower values indicate faster inference performance.
- **Throughput (images/sec):** Indicates how many images the model can process per second. Higher throughput means better overall efficiency.
- **Model Type:** Refers to the neural network architecture used for testing (e.g., ResNet50, MobileNetV2, InceptionV3). Each model has different computational complexity.

### Benchmark summary
Results from the earlier run on the `c4a-standard-4` (4 vCPU, 16 GB memory) Arm64 VM in GCP (SUSE):

| **Model**       | **Average Inference Time per Batch (seconds)** | **Throughput (images/sec)** |
|------------------|-----------------------------------------------:|-----------------------------:|
| **ResNet50**     | 1.2051                                         | 26.55                        |
| **MobileNetV2**  | 0.2909                                         | 110.02                       |
| **InceptionV3**  | 0.8971                                         | 35.67                        |

- **Arm64 VMs show strong performance** for lightweight CNNs like **MobileNetV2**, achieving over **110 images/sec**, indicating excellent optimization for CPU-based inference. 
- **Medium-depth models** like **InceptionV3** maintain a **balanced trade-off between accuracy and latency**, confirming consistent multi-core utilization on Arm.  
- **Heavier architectures** such as **ResNet50** show expected longer inference times but still deliver **stable throughput**, reflecting good floating-point efficiency.  
- **Arm64 provides energy-efficient yet competitive performance**, particularly for **mobile, quantized, or edge AI workloads**.  
- **Overall**, Arm64 demonstrates that **TensorFlow workloads can run efficiently on cloud-native ARM processors**, making them a **cost-effective and power-efficient alternative** for AI inference and model prototyping.
