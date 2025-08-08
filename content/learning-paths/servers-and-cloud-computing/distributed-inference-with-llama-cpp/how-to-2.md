---
title: Overview and Worker Node Configuration
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Before you begin
The instructions in this Learning Path are for any Arm server running Ubuntu 24.04.2 LTS. You will need at least three Arm server instances with at least 64 cores and 128GB of RAM to run this example. The instructions have been tested on an AWS Graviton4 c8g.16xlarge instance.

## Overview
llama.cpp is a C++ library that enables efficient inference of LLaMA and similar large language models on CPUs, optimized for local and embedded environments. Just over a year ago from the publication date of this article, rgerganov’s RPC code was merged into llama.cpp, enabling distributed inference of large LLMs across multiple CPU-based machines—even when the models don’t fit into the memory of a single machine. In this learning path, we’ll explore how to run a 405B parameter model on Arm-based CPUs.

For the purposes of this demonstration, the following experimental setup will be used:
- Total number of instances: 3
- Instance type: c8g.16xlarge
- Model: Llama-3.1-405B_Q4_0.gguf

One of the three nodes will serve as the master node, which physically hosts the model file. The other two nodes will act as worker nodes. In llama.cpp, remote procedure calls (RPC) are used to offload both the model and the computation over TCP connections between nodes. The master node forwards inference requests to the worker nodes, where all the actual computation is performed.

## Implementation

1. Once you have the model.gguf ready and llama.cpp cloned (described on previous page), you can proceed to step 2.

2. Now we can build the llama.cpp library with the RPC feature enabled by compiling it with the -DLLAMA_RPC=ON flag
```bash
apt install -y cmake build-essential
apt install -y g++
apt install -y libcurl4-openssl-dev
cd llama.cpp
mkdir -p build-rpc
cd build-rpc
cmake .. -DGGML_RPC=ON -DLLAMA_BUILD_SERVER=ON
cmake --build . --config Release
```

`llama.cpp` is now built in the `build-rpc/bin` directory.
Check that `llama.cpp` has built correctly by running the help command:
```bash
cd build-rpc
bin/llama-cli -h
```
If everything was built correctly, you should see a list of all the available flags that can be used with llama-cli.

3. Now, choose two of the three devices to act as backend workers. If the devices had varying compute capacities, the ones with the highest compute should be selected—especially for a 405B model. However, since all three devices have identical compute capabilities in this case, you can select any two to serve as backend workers.

Communication between the master node and the worker nodes occurs through a socket created on each worker. This socket listens for incoming data from the master—such as model parameters, tokens, hidden states, and other inference-related information.
{{% notice Note %}}The RPC feature in llama.cpp is not secure by default, so you should never expose it to the open internet. To mitigate this risk, ensure that the security groups for all your EC2 instances are properly configured—restricting access to only trusted IPs or internal VPC traffic. This helps prevent unauthorized access to the RPC endpoints.{{% /notice %}}
Use the following command to start the listening on the worker nodes:
```bash
bin/rpc-server -p 50052 -H 0.0.0.0 -t 64
```
Below are the available flag options that can be used with the rpc-server functionality:

```output
-h, --help                show this help message and exit
-t,      --threads        number of threads for the CPU backend (default: 6)
-d DEV,  --device         device to use
-H HOST, --host HOST      host to bind to (default: 127.0.0.1)
-p PORT, --port PORT      port to bind to (default: 50052)
-m MEM,  --mem MEM        backend memory size (in MB)
-c,      --cache          enable local file cache
```
Setting the host to 0.0.0.0 might seem counterintuitive given the earlier security warning, but it’s acceptable in this case because the security groups have been properly configured to block any unintended or unauthorized access.