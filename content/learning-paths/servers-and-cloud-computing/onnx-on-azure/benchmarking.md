---
title: Benchmarking via onnxruntime_perf_test
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Test the ONNX based application for Performance
Now that you’ve set up and run the ONNX model (e.g., SqueezeNet), you can use it to benchmark inference performance using Python-based timing or tools like onnxruntime_perf_test. This helps evaluate the ONNX Runtime efficiency on Azure Arm64-based Cobalt 100 instances.
You can also compare the inference time between Cobalt 100 (Arm64) and similar D-series x86_64-based VMs on Azure.
As noted before, the steps to benchmark remain the same, whether it's a Docker container or a custom VM.

## Run the performance tests using onnxruntime_perf_test
The onnxruntime_perf_test is a performance benchmarking tool included in the ONNX Runtime source code. It is used to measure the inference performance of ONNX models under various runtime conditions (like CPU, GPU, or other execution providers). 

### Install Required Build Tools

```console
$ tdnf install -y cmake make gcc-c++ git
```
#### Install Protobuf

```console
$ tdnf install -y protobuf protobuf-devel
```
Then verify:
```console
$ protoc --version
```
You should see something like:

```output
libprotoc x.x
```
If installation fails, or the version is too old for ONNX Runtime; then proceed with [installing Protobuf using the Aarch64 pre-built zip artifact](https://github.com/protocolbuffers/protobuf/releases), as discussed below.

####  Install Protobuf using the Pre-built Aarch64 ZIP Artifact

```console
$ wget https://github.com/protocolbuffers/protobuf/releases/download/vx.x/protoc-x.x-linux-aarch_64.zip -O protoc-x.x.zip
$ mkdir -p $HOME/tools/protoc-x.x
$ unzip protoc-x.x.zip -d $HOME/tools/protoc-x.x
$ echo 'export PATH="$HOME/tools/protoc-x.x/bin:$PATH"' >> ~/.bashrc
$ source ~/.bashrc
```

Then verify:
```console
$ protoc --version
```
Output:
```output
libprotoc x.x
```

### Clone and Build ONNX Runtime from Source:

The benchmarking tool, onnxruntime_perf_test, isn’t available as a pre-built binary artifact for any platform. So, you have to build it from the source, which is expected to take around 40-50 minutes.
Follow the below to build onnxruntime from the source code, and hence benchmark the module. 

Install the required tools and clone onnxruntime:
```console
$ tdnf install -y protobuf-compiler libprotobuf-dev libprotoc-dev 
$ git clone --recursive https://github.com/microsoft/onnxruntime 
$ cd onnxruntime
```
Now, build the benchmark as below:

```console
$ ./build.sh --config Release --build_dir build/Linux --build_shared_lib --parallel --build --update --skip_tests 
```
This will build the benchmark tool inside `./build/Linux/Release/onnxruntime_perf_test`. 

### Run the benchmark
Now that the benchmarking tool has been built, you can benchmark the **squeezenet-int8.onnx** model, as below:

```console
$ ./build/Linux/Release/onnxruntime_perf_test -e cpu -r 100 -m times -s -Z -I <path-to-squeezenet-int8.onnx>
```

- **e cpu**: Use the CPU execution provider (not GPU or any other backend). 
- **r 100**: Run 100 inferences. 
- **m times**: Use "repeat N times" mode. 
- **s**: Show detailed statistics. 
- **Z**: Disable intra-op thread spinning (reduces CPU usage when idle between runs). 
- **I**: Input the ONNX model path without using input/output test data.

### Benchmark summary on x86_64:

The following benchmark results are collected on two different x86_64 environments: a **Docker container running Azure Linux 3.0 hosted on a D4s_v6 Ubuntu-based Azure VM**, and a **D4s_v4 Azure VM created from the Azure Linux 3.0 image published by Ntegral Inc**.

| **Metric**               | **Value on Docker Container** | **Value on Virtual Machine** |
|--------------------------|----------------------------------------|-----------------------------------------|
| **Average Inference Time** | 1.4713 ms                             | 1.8961 ms                                |
| **Throughput**             | 679.48 inferences/sec                 | 527.25 inferences/sec                    |
| **CPU Utilization**        | 100%                                  | 95%                                      |
| **Peak Memory Usage**      | 39.8 MB                              | 36.1 MB                |
| **P50 Latency**            | 1.4622 ms                             | 1.8709 ms                                |
| **Max Latency**            | 2.3384 ms                             | 2.7826 ms                                |
| **Latency Consistency**    | Consistent                            | Consistent                               |


### Benchmark summary on Arm64:

The following benchmark results are collected on two different Arm64 environments: a **Docker container running Azure Linux 3.0 hosted on a D4ps_v6 Ubuntu-based Azure VM**, and a **D4ps_v6 Azure VM created from the Azure Linux 3.0 custom image using the Aarch64 ISO**.

| **Metric**                | **Value on Docker Container**         | **Value on Virtual Machine**                |
|---------------------------|---------------------------------------|---------------------------------------------|
| **Average Inference Time**| 1.9183 ms                              | 1.9169 ms                                    |
| **Throughput**            | 521.09 inferences/sec                  | 521.41 inferences/sec                        |
| **CPU Utilization**       | 98%                                   | 100%                                         |
| **Peak Memory Usage**     | 35.36 MB                               | 33.57 MB                    |
| **P50 Latency**           | 1.9165 ms                              | 1.9168 ms                                    |
| **Max Latency**           | 2.0142 ms                              | 1.9979 ms                                    |
| **Latency Consistency**   | Consistent                             | Consistent                                   |


### Highlights from Azure Linux Arm64 Benchmarking (ONNX Runtime with SqueezeNet)
- **Low-Latency Inference:** Achieved consistent average inference times of ~1.92 ms across both Docker and VM environments on Arm64.
- **Strong and Stable Throughput:** Sustained throughput of over 521 inferences/sec using the squeezenet-int8.onnx model on D4ps_v6 instances.
- **Lightweight Resource Footprint:** Peak memory usage stayed below 36 MB, with CPU utilization reaching ~98–100%, ideal for efficient edge or cloud inference.
- **Consistent Performance:** P50 and Max latency remained tightly bound across both setups, showcasing reliable performance on Azure Cobalt 100 Arm-based infrastructure.
