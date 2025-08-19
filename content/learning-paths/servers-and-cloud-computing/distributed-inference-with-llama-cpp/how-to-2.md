---
title: Worker Node Configuration
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Cluster overview
llama.cpp is a C++ library that enables efficient inference of LLaMA and similar large language models on CPUs, optimized for local and embedded environments. Just over a year ago from the publication date of this article, rgerganov’s RPC code was merged into llama.cpp, enabling distributed inference of large LLMs across multiple CPU-based machines—even when the models don’t fit into the memory of a single machine. In this learning path, we’ll explore how to run a 70B parameter model on Arm-based CPUs.

For the purposes of this demonstration, the following experimental setup will be used:
- Total number of instances: 3
- Instance type: c8g.4xlarge
- Model: model.gguf (Llama-3.1-70B_Q4_0, ~38GB when quantized to 4 bits)

One of the three nodes will serve as the master node, which physically hosts the model file. The other two nodes will act as worker nodes. In llama.cpp, remote procedure calls (RPC) are used to offload both the model and the computation over TCP connections between nodes. The master node forwards inference requests to the worker nodes, where all the actual computation is performed.

## Cluster setup

Choose two of the three devices to act as backend workers. If the devices had varying compute capacities, the ones with the highest compute should be selected. However, since all three devices have identical compute capabilities in this case, you can select any two to serve as backend workers.

Communication between the master node and the worker nodes occurs through a socket created on each worker. This socket listens for incoming data from the master—such as model parameters, tokens, hidden states, and other inference-related information.
{{% notice Note %}}The RPC feature in llama.cpp is not secure by default, so you should never expose it to the open internet. To mitigate this risk, ensure that the security groups for all your EC2 instances are properly configured—restricting access to only trusted IPs or internal VPC traffic. This helps prevent unauthorized access to the RPC endpoints.{{% /notice %}}
Use the following command to start the listening on the worker nodes:
```bash
bin/rpc-server -c -p 50052 -H 0.0.0.0 -t 64
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

There is currently no way to pre-load tensors onto the workers, the `-c` option will cache tensors during runtime. The first time inference runs the tensors will be distributed to the workers.