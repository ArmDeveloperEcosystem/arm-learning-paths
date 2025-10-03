---
title: Benchmarking via onnxruntime_perf_test
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Now that you have validated ONNX Runtime with Python-based timing (e.g., SqueezeNet baseline test), you can move to using a dedicated benchmarking utility called `onnxruntime_perf_test`. This tool is designed for systematic performance evaluation of ONNX models, allowing you to capture more detailed statistics than simple Python timing.
This helps evaluate the ONNX Runtime efficiency on Azure Arm64-based Cobalt 100 instances and other x86_64 instances. architectures.

## Run the performance tests using onnxruntime_perf_test
The `onnxruntime_perf_test` is a performance benchmarking tool included in the ONNX Runtime source code. It is used to measure the inference performance of ONNX models and supports multiple execution providers (like CPU, GPU, or other execution providers). on Arm64 VMs, CPU execution is the focus.

### Install Required Build Tools
Before building or running `onnxruntime_perf_test`, you will need to install a set of development tools and libraries. These packages are required for compiling ONNX Runtime and handling model serialization via Protocol Buffers.

```console
sudo apt update
sudo apt install -y build-essential cmake git unzip pkg-config
sudo apt install -y protobuf-compiler libprotobuf-dev libprotoc-dev git
```
Then verify protobuf installation:
```console
protoc --version
```
You should see output similar to:

```output
libprotoc 3.21.12
```
### Build ONNX Runtime from Source:

The benchmarking tool `onnxruntime_perf_test`, isn’t available as a pre-built binary for any platform. So, you will have to build it from the source, which is expected to take around 40 minutes. 

Clone onnxruntime repo:
```console
git clone --recursive https://github.com/microsoft/onnxruntime 
cd onnxruntime
```
Now, build the benchmark tool:

```console
./build.sh --config Release --build_dir build/Linux --build_shared_lib --parallel --build --update --skip_tests 
```
You should see the executable at:
```output
./build/Linux/Release/onnxruntime_perf_test
```

### Run the benchmark
Now that you have built the benchmarking tool, you can run inference benchmarks on the SqueezeNet INT8 model:

```console
./build/Linux/Release/onnxruntime_perf_test -e cpu -r 100 -m times -s -Z -I ../squeezenet-int8.onnx
```
Breakdown of the flags:
  -e cpu → Use the CPU execution provider.
  -r 100 → Run 100 inference passes for statistical reliability.
  -m times → Run in “repeat N times” mode. Useful for latency-focused measurement.
  -s → Show detailed per-run statistics (latency distribution).
  -Z → Disable intra-op thread spinning. Reduces CPU waste when idle between runs, especially on high-core systems like Cobalt 100.
  -I → Input the ONNX model path directly, skipping pre-generated test data.

You should see output similar to:

```output
Disabling intra-op thread spinning between runs
Session creation time cost: 0.0102016 s
First inference time cost: 2 ms
Total inference time cost: 0.185739 s
Total inference requests: 100
Average inference time cost: 1.85739 ms
Total inference run time: 0.18581 s
Number of inferences per second: 538.184
Avg CPU usage: 96 %
Peak working set size: 36696064 bytes
Avg CPU usage:96
Peak working set size:36696064
Runs:100
Min Latency: 0.00183404 s
Max Latency: 0.00190312 s
P50 Latency: 0.00185674 s
P90 Latency: 0.00187215 s
P95 Latency: 0.00187393 s
P99 Latency: 0.00190312 s
P999 Latency: 0.00190312 s
```
### Benchmark Metrics Explained  

  * Average Inference Time: The mean time taken to process a single inference request across all runs. Lower values indicate faster model execution.  
  * Throughput: The number of inference requests processed per second. Higher throughput reflects the model’s ability to handle larger workloads efficiently.  
  * CPU Utilization: The percentage of CPU resources used during inference. A value close to 100% indicates full CPU usage, which is expected during performance benchmarking.  
  * Peak Memory Usage: The maximum amount of system memory (RAM) consumed during inference. Lower memory usage is beneficial for resource-constrained environments. 
  * P50 Latency (Median Latency): The time below which 50% of inference requests complete. Represents typical latency under normal load.   
  * Latency Consistency: Describes the stability of latency values across all runs. "Consistent" indicates predictable inference performance with minimal jitter.  

### Benchmark summary on Arm64:
Here is a summary of benchmark results collected on an Arm64 **D4ps_v6 Ubuntu Pro 24.04 LTS virtual machine**.

| **Metric**                | **Value** |
|----------------------------|-------------------------------|
| **Average Inference Time** | 1.857 ms                     |
| **Throughput**             | 538.18 inferences/sec        |
| **CPU Utilization**        | 96%                          |
| **Peak Memory Usage**      | 36.70 MB                     |
| **P50 Latency**            | 1.857 ms                     |
| **P90 Latency**            | 1.872 ms                     |
| **P95 Latency**            | 1.874 ms                     |
| **P99 Latency**            | 1.903 ms                     |
| **P999 Latency**           | 1.903 ms                     |
| **Max Latency**            | 1.903 ms                     |
| **Latency Consistency**    | Consistent                   |


### Highlights from Benchmarking on Azure Cobalt 100 Arm64 VMs

The results on Arm64 virtual machines demonstrate:
- Low-Latency Inference: Achieved consistent average inference times of ~1.86 ms on Arm64.  
- Strong and Stable Throughput: Sustained throughput of over 538 inferences/sec using the `squeezenet-int8.onnx` model on D4ps_v6 instances.  
- Lightweight Resource Footprint: Peak memory usage stayed below 37 MB, with CPU utilization around 96%, ideal for efficient edge or cloud inference.  
- Consistent Performance: P50, P95, and Max latency remained tightly bound, showcasing reliable performance on Azure Cobalt 100 Arm-based infrastructure.

You have now successfully benchmarked inference time of ONNX models on an Azure Cobalt 100 Arm64 virtual machine.
