---
title: Benchmark ONNX runtime performance with onnxruntime_perf_test
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Benchmark ONNX model inference on Azure Cobalt 100
Now that you have validated ONNX Runtime with Python-based timing (for example, the SqueezeNet baseline test), you can move to using a dedicated benchmarking utility called `onnxruntime_perf_test`. This tool is designed for systematic performance evaluation of ONNX models, allowing you to capture more detailed statistics than simple Python timing.

This approach helps you evaluate ONNX Runtime efficiency on Azure Arm64-based Cobalt 100 instances and compare results with other architectures if needed.

You are ready to run benchmarks, which is a key skill for optimizing real-world deployments.


## Run the performance tests using onnxruntime_perf_test
The `onnxruntime_perf_test` tool is included in the ONNX Runtime source code. You can use it to measure the inference performance of ONNX models and compare different execution providers (such as CPU or GPU). On Arm64 VMs, CPU execution is the focus.


## Install required build tools
Before building or running `onnxruntime_perf_test`, you need to install a set of development tools and libraries. These packages are required for compiling ONNX Runtime and handling model serialization via Protocol Buffers.

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
## Build ONNX Runtime from source

The benchmarking tool `onnxruntime_perf_test` isn’t available as a pre-built binary for any platform, so you will need to build it from source. This process can take up to 40 minutes.

Clone the ONNX Runtime repository:
```console
git clone --recursive https://github.com/microsoft/onnxruntime 
cd onnxruntime
```

Now, build the benchmark tool:

```console
./build.sh --config Release --build_dir build/Linux --build_shared_lib --parallel --build --update --skip_tests 
```
If the build completes successfully, you should see the executable at:
```output
./build/Linux/Release/onnxruntime_perf_test
```


## Run the benchmark
Now that you have built the benchmarking tool, you can run inference benchmarks on the SqueezeNet INT8 model:

```console
./build/Linux/Release/onnxruntime_perf_test -e cpu -r 100 -m times -s -Z -I ../squeezenet-int8.onnx
```

Breakdown of the flags:

- `-e cpu`: use the CPU execution provider.
- `-r 100`: run 100 inference passes for statistical reliability.
- `-m times`: run in “repeat N times” mode for latency-focused measurement.
- `-s`: print summary statistics after the run.
- `-Z`: disable memory arena for more consistent timing.
- `-I ../squeezenet-int8.onnx`: path to your ONNX model file.

You should see output with latency and throughput statistics. If you encounter build errors, check that you have enough memory (at least 8 GB recommended) and all dependencies are installed. For missing dependencies, review the installation steps above.

If the benchmark runs successfully, you are ready to analyze and optimize your ONNX model performance on Arm-based Azure infrastructure.

Well done! You have completed a full benchmarking workflow. Continue to the next section to explore further optimizations or advanced deployment scenarios.
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
## Benchmark Metrics Explained  

  * Average inference time: the mean time taken to process a single inference request across all runs. Lower values indicate faster model execution.  
  * Throughput: the number of inference requests processed per second. Higher throughput reflects the model’s ability to handle larger workloads efficiently.  
  * CPU utilization: the percentage of CPU resources used during inference. A value close to 100% indicates full CPU usage, which is expected during performance benchmarking.  
  * Peak Memory Usage: the maximum amount of system memory (RAM) consumed during inference. Lower memory usage is beneficial for resource-constrained environments. 
  * P50 Latency (Median Latency): the time below which 50% of inference requests complete. Represents typical latency under normal load.   
  * Latency Consistency: describes the stability of latency values across all runs. "Consistent" indicates predictable inference performance with minimal jitter.  

## Benchmark summary on Arm64:
Here is a summary of benchmark results collected on an Arm64 D4ps_v6 Ubuntu Pro 24.04 LTS virtual machine.

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


## Highlights from Benchmarking on Azure Cobalt 100 Arm64 VMs


These results on Arm64 virtual machines demonstrate low-latency inference, with consistent average inference times of approximately 1.86 ms. Throughput remains strong and stable, sustaining over 538 inferences per second using the `squeezenet-int8.onnx` model on D4ps_v6 instances. The resource footprint is lightweight, as peak memory usage stays below 37 MB and CPU utilization is around 96%, making this setup ideal for efficient edge or cloud inference. Performance is also consistent, with P50, P95, and maximum latency values tightly grouped, showcasing reliable results on Azure Cobalt 100 Arm-based infrastructure.

You have now successfully benchmarked inference time of ONNX models on an Azure Cobalt 100 Arm64 virtual machine.
