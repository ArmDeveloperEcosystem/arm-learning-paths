---
# User change
title: "Enable Arm specific flags"

weight: 3

# Do not modify these elements
layout: "learningpathall"
---

## Use the Arm specific flags:

### Enable Fast Math GEMM Kernels

To accelerate fp32 inference with bfloat16 GEMM, enable the fast math GEMM kernels by exporting the following flag:

```bash
    export DNNL_DEFAULT_FPMATH_MODE=BF16
```

{{% notice Note %}}
BF16 support is merged into PyTorch versions greater than 2.3.0.
{{% /notice %}}

### Enable Linux Transparent Huge Page (THP) Allocations

To reduce the tensor memory allocation latency, enable Linux Transparent Huge Page (THP) allocations by exporting the following flag:

```bash
    export THP_MEM_ALLOC_ENABLE=1
```

### Set LRU Cache Capacity

To cache efficiently avoid redundant memory allocations, set the LRU Cache capacity by exporting the following flag:

```bash
    export LRU_CACHE_CAPACITY=1024
```

### Set OMP_NUM_THREADS

To utilize the number of vCPUs efficiently, set the number of OpenMP threads by exporting the following flag:

```bash
    export OMP_NUM_THREADS=32
```

### Enable Logs to Confirm Kernel

To show logs and confirm the kernel is enabled, export the following flag:

```bash
    export DNNL_VERBOSE=1
```