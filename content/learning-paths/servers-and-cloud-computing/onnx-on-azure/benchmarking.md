---
title: Benchmarking via onnxruntime_perf_test
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Now that you’ve set up and run the ONNX model (e.g., SqueezeNet), you can use it to benchmark inference performance using Python-based timing or tools like **onnxruntime_perf_test**. This helps evaluate the ONNX Runtime efficiency on Azure Arm64-based Cobalt 100 instances.

You can also compare the inference time between Cobalt 100 (Arm64) and similar D-series x86_64-based virtual machine on Azure.

## Run the performance tests using onnxruntime_perf_test
The **onnxruntime_perf_test** is a performance benchmarking tool included in the ONNX Runtime source code. It is used to measure the inference performance of ONNX models under various runtime conditions (like CPU, GPU, or other execution providers).

### Install Required Build Tools

```console
sudo apt update
sudo apt install -y build-essential cmake git unzip pkg-config
sudo apt install -y protobuf-compiler libprotobuf-dev libprotoc-dev git
```
Then verify:
```console
protoc --version
```
You should see an output similar to:

```output
libprotoc 3.21.12
```
### Build ONNX Runtime from Source:

The benchmarking tool, **onnxruntime_perf_test**, isn’t available as a pre-built binary artifact for any platform. So, you have to build it from the source, which is expected to take around 40-50 minutes. 

Clone onnxruntime:
```console
git clone --recursive https://github.com/microsoft/onnxruntime 
cd onnxruntime
```
Now, build the benchmark as below:

```console
./build.sh --config Release --build_dir build/Linux --build_shared_lib --parallel --build --update --skip_tests 
```
This will build the benchmark tool inside ./build/Linux/Release/onnxruntime_perf_test. 

### Run the benchmark
Now that the benchmarking tool has been built, you can benchmark the **squeezenet-int8.onnx** model, as below:

```console
./build/Linux/Release/onnxruntime_perf_test -e cpu -r 100 -m times -s -Z -I <path-to-squeezenet-int8.onnx>
```
- **e cpu**: Use the CPU execution provider (not GPU or any other backend). 
- **r 100**: Run 100 inferences. 
- **m times**: Use "repeat N times" mode. 
- **s**: Show detailed statistics. 
- **Z**: Disable intra-op thread spinning (reduces CPU usage when idle between runs). 
- **I**: Input the ONNX model path without using input/output test data.

You should see an output similar to:

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

- **Average Inference Time**: The mean time taken to process a single inference request across all runs. Lower values indicate faster model execution.  
- **Throughput**: The number of inference requests processed per second. Higher throughput reflects the model’s ability to handle larger workloads efficiently.  
- **CPU Utilization**: The percentage of CPU resources used during inference. A value close to 100% indicates full CPU usage, which is expected during performance benchmarking.  
- **Peak Memory Usage**: The maximum amount of system memory (RAM) consumed during inference. Lower memory usage is beneficial for resource-constrained environments. 
- **P50 Latency (Median Latency)**: The time below which 50% of inference requests complete. Represents typical latency under normal load.   
- **Latency Consistency**: Describes the stability of latency values across all runs. "Consistent" indicates predictable inference performance with minimal jitter.  

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


### Benchmark summary on x86
Here is a summary of benchmark results collected on x86 **D4s_v6 Ubuntu Pro 24.04 LTS virtual machine**.

| **Metric**                | **Value on Virtual Machine** |
|----------------------------|-------------------------------|
| **Average Inference Time** | 1.413 ms                     |
| **Throughput**             | 707.48 inferences/sec        |
| **CPU Utilization**        | 100%                         |
| **Peak Memory Usage**      | 38.80 MB                     |
| **P50 Latency**            | 1.396 ms                     |
| **P90 Latency**            | 1.501 ms                     |
| **P95 Latency**            | 1.520 ms                     |
| **P99 Latency**            | 1.794 ms                     |
| **P999 Latency**           | 1.794 ms                     |
| **Max Latency**            | 1.794 ms                     |
| **Latency Consistency**    | Consistent                   |


### Highlights from Ubuntu Pro 24.04 Arm64 Benchmarking

When comparing the results on Arm64 vs x86_64 virtual machines:
- **Low-Latency Inference:** Achieved consistent average inference times of ~1.86 ms on Arm64.  
- **Strong and Stable Throughput:** Sustained throughput of over 538 inferences/sec using the `squeezenet-int8.onnx` model on D4ps_v6 instances.  
- **Lightweight Resource Footprint:** Peak memory usage stayed below 37 MB, with CPU utilization around 96%, ideal for efficient edge or cloud inference.  
- **Consistent Performance:** P50, P95, and Max latency remained tightly bound, showcasing reliable performance on Azure Cobalt 100 Arm-based infrastructure.

You have now benchmarked ONNX on an Azure Cobalt 100 Arm64 virtual machine and compared results with x86_64.
