---
title: Configure the worker nodes
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview of the cluster

`llama.cpp` is a C++ library that enables efficient inference of LLaMA and similar large language models on CPUs, optimized for local and embedded environments. 

Just over a year before this Learning Path was published, Radoslav Gerganov's (rgerganov) RPC code was merged into `llama.cpp`. This feature enables distributed inference of large LLMs across multiple CPU-based machines, even when the models don’t fit into the memory of a single machine. 

In this Learning Path, you’ll explore how to run a 70B parameter model on Arm-based CPUs.

For this demonstration, the experimental setup includes:

- Total number of instances: 3
- Instance type: c8g.4xlarge
- Model: model.gguf (llama-3.1-70B_Q4_0, ~38GB when quantized to 4 bits)

One of the three nodes serves as the master node, which physically hosts the model file. The other two nodes act as worker nodes. In `llama.cpp`, remote procedure calls (RPC) offload both the model and the computation over TCP connections between nodes. The master node forwards inference requests to the worker nodes, where computation is performed.

## Set up the worker nodes

Choose two of the three devices to act as backend workers. If the devices have varying compute capacities, select the ones with the highest compute. Because all three devices in this setup are identical, you can select any two to serve as backend workers.

Communication between the master node and the worker nodes occurs through a socket created on each worker. This socket listens for incoming data from the master, such as model parameters, tokens, hidden states, and other inference-related information.

{{% notice Note %}}
The RPC feature in `llama.cpp` is not secure by default, so you should never expose it to the open internet. To reduce this risk, ensure that the security groups for all your EC2 instances are configured to restrict access to trusted IPs or internal VPC traffic only. This prevents unauthorized access to the RPC endpoints.
{{% /notice %}}

Start the worker nodes with the following command:

```bash
bin/rpc-server -c -p 50052 -H 0.0.0.0 -t 64
```

## Review RPC server options

The following flags are available with the `rpc-server` command:

```output
-h, --help                show this help message and exit
-t,      --threads        number of threads for the CPU backend (default: 6)
-d DEV,  --device         device to use
-H HOST, --host HOST      host to bind to (default: 127.0.0.1)
-p PORT, --port PORT      port to bind to (default: 50052)
-m MEM,  --mem MEM        backend memory size (in MB)
-c,      --cache          enable local file cache
```

Although setting the host to `0.0.0.0` might seem counterintuitive given the earlier security warning, it is acceptable here because the EC2 security groups are configured to block unintended or unauthorized access.
