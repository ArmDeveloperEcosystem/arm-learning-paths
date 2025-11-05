---
title: Verify your Grace Blackwell system readiness for AI inference
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up your Grace Blackwell environment

Before building and running quantized LLMs on your DGX Spark, you need to verify that your system is fully prepared for AI workloads. This includes checking your Arm-based Grace CPU configuration, confirming your operating system, ensuring the Blackwell GPU and CUDA drivers are active, and validating that the CUDA toolkit is installed. These steps provide a solid foundation for efficient LLM inference and development on Arm.

This section is organized into three main steps: verifying your CPU, checking your operating system, and confirming your GPU and CUDA toolkit setup. You'll also find additional context and technical details throughout, should you wish to explore the platform's capabilities more deeply.

## Step 1: Verify your CPU configuration

Before running LLM workloads, it's helpful to understand more about the CPU you're working with. The DGX Spark uses Arm-based Grace processors, which bring some unique advantages for AI inference.

Start by checking your system's CPU configuration:

```bash
lscpu
```

The output is similar to:

```output
Architecture:             aarch64
  CPU op-mode(s):         64-bit
  Byte Order:             Little Endian
CPU(s):                   20
  On-line CPU(s) list:    0-19
Vendor ID:                ARM
  Model name:             Cortex-X925
    Model:                1
    Thread(s) per core:   1
    Core(s) per socket:   10
    Socket(s):            1
    Stepping:             r0p1
    CPU(s) scaling MHz:   89%
    CPU max MHz:          4004.0000
    CPU min MHz:          1378.0000
    BogoMIPS:             2000.00
    Flags:                fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma lrcpc dcpop sha3 sm3 sm4 as
                          imddp sha512 sve asimdfhm dit uscat ilrcpc flagm sb paca pacg dcpodp sve2 sveaes svepmull svebitperm svesha3 svesm4 f
                          lagm2 frint svei8mm svebf16 i8mm bf16 dgh bti ecv afp wfxt
  Model name:             Cortex-A725
    Model:                1
    Thread(s) per core:   1
    Core(s) per socket:   10
    Socket(s):            1
    Stepping:             r0p1
    CPU(s) scaling MHz:   99%
    CPU max MHz:          2860.0000
    CPU min MHz:          338.0000
    BogoMIPS:             2000.00
    Flags:                fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma lrcpc dcpop sha3 sm3 sm4 as
                          imddp sha512 sve asimdfhm dit uscat ilrcpc flagm sb paca pacg dcpodp sve2 sveaes svepmull svebitperm svesha3 svesm4 f
                          lagm2 frint svei8mm svebf16 i8mm bf16 dgh bti ecv afp wfxt
Caches (sum of all):      
  L1d:                    1.3 MiB (20 instances)
  L1i:                    1.3 MiB (20 instances)
  L2:                     25 MiB (20 instances)
  L3:                     24 MiB (2 instances)
NUMA:                     
  NUMA node(s):           1
  NUMA node0 CPU(s):      0-19
Vulnerabilities:          
  Gather data sampling:   Not affected
  Itlb multihit:          Not affected
  L1tf:                   Not affected
  Mds:                    Not affected
  Meltdown:               Not affected
  Mmio stale data:        Not affected
  Reg file data sampling: Not affected
  Retbleed:               Not affected
  Spec rstack overflow:   Not affected
  Spec store bypass:      Mitigation; Speculative Store Bypass disabled via prctl
  Spectre v1:             Mitigation; __user pointer sanitization
  Spectre v2:             Not affected
  Srbds:                  Not affected
  Tsx async abort:        Not affected
```

If you have seen this message your system is using Armv9 cores, great! These are ideal for quantized LLM workloads. The Grace CPU implements the Armv9-A instruction set and supports advanced vector extensions, making it ideal for quantized LLM inference and tensor operations.

### Grace CPU specification 

The following table provides more information about the key specifications of the Grace CPU and explains their relevance to quantized LLM inference:

| **Category** | **Specification** | **Description/Impact for LLM Inference** |
|---------------|-------------------|---------------------------------------------|
| Architecture | Armv9-A (64-bit, aarch64) | Modern Arm architecture supporting advanced vector and AI extensions|
| Core Configuration | 20 cores total - 10× Cortex-X925 (performance) + 10× Cortex-A725 (efficiency) | Heterogeneous CPU design balancing high performance and power efficiency |
| Threads per Core | 1 | Optimized for deterministic scheduling and predictable latency |
| Clock Frequency | Up to **4.0 GHz** (Cortex-X925)<br>Up to **2.86 GHz** (Cortex-A725) | High per-core speed ensures strong single-thread inference for token orchestration. |
| Cache Hierarchy | L1: 1.3 MiB × 20<br>L2: 25 MiB × 20<br>L3: 24 MiB × 2 | Large shared L3 cache enhances data locality for multi-threaded inference workloads |
| Instruction Set Features** | SVE / SVE2, BF16, I8MM, AES, SHA3, SM4, CRC32 | Vector and mixed-precision instructions accelerate quantized (Q4/Q8) math operations |
| NUMA Topology | Single NUMA node (node0: 0–19) | Simplifies memory access pattern for unified memory workloads |
| Security and Reliability | Not affected by Meltdown, Spectre, Retbleed, or similar vulnerabilities | Ensures stable and secure operation for long-running inference tasks |

Its SVE2, BF16, and INT8 matrix multiplication (I8MM) capabilities are what make it ideal for quantized LLM workloads, as these provide a power-efficient foundation for both CPU-only inference and CPU-GPU hybrid processing.

### Verify OS

You can also verify the operating system running on your DGX Spark by using the following command:

```bash
lsb_release -a
```

The expected output is something similar to:

```log
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 24.04.3 LTS
Release:	24.04
Codename:	noble
```
This shows you that your DGX Spark runs on Ubuntu 24.04 LTS, a developer-friendly Linux distribution that provides excellent compatibility with AI frameworks, compiler toolchains, and system utilities. This makes it an ideal environment for building and deploying quantized LLM workloads.

Nice work! You've confirmed your operating system is Ubuntu 24.04 LTS, so you can move on to the next step.

## Step 2: Verify the Blackwell GPU and driver

After confirming your CPU configuration, verify that the Blackwell GPU inside the GB10 Grace Blackwell Superchip is available and ready for CUDA workloads by using the following:

```bash
nvidia-smi
```

You will see output similar to:

```output
Wed Oct 22 09:26:54 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.95.05              Driver Version: 580.95.05      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GB10                    On  |   0000000F:01:00.0 Off |                  N/A |
| N/A   32C    P8              4W /  N/A  | Not Supported          |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A            3094      G   /usr/lib/xorg/Xorg                       43MiB |
|    0   N/A  N/A            3172      G   /usr/bin/gnome-shell                     16MiB |
+-----------------------------------------------------------------------------------------+
```

The `nvidia-smi` tool reports GPU hardware specifications and provides valuable runtime information, including driver status, temperature, power usage, and GPU utilization. This information helps verify that the system is ready for AI workloads.

### Further information about the output from the nvidia-smi tool

The table below provides more explanation of the `nvidia-smi` output:
| **Category** | **Specification (from nvidia-smi)** | **Description / impact for LLM inference** |
|---------------|--------------------------------------|---------------------------------------------|
| GPU name | NVIDIA GB10 | Confirms the system recognizes the Blackwell GPU integrated into the Grace Blackwell Superchip |
| Driver version | 580.95.05 | Indicates that the system is running the latest driver package required for CUDA 13 compatibility |
| CUDA version | 13.0 | Confirms that the CUDA runtime supports GB10 (sm_121) and is ready for accelerated quantized LLM workloads |
| Architecture / Compute capability | Blackwell (sm_121) | Supports FP4, FP8, and BF16 Tensor Core operations optimized for LLMs |
| Memory | Unified 128 GB LPDDR5X (shared with CPU via NVLink-C2C) | Enables zero-copy data access between Grace CPU and GPU for unified inference memory space |
| Power & Thermal status | ~4W at idle, 32°C temperature | Confirms the GPU is powered on and thermally stable while idle |
| GPU-utilization | 0% (Idle) | Indicates no active compute workloads; GPU is ready for new inference jobs |
| Memory usage | Not Supported (headless GPU configuration) | DGX Spark operates in headless compute mode; display memory metrics may not be exposed |
| Persistence mode | On | Ensures the GPU remains initialized and ready for rapid inference startup |

Excellent! Your Blackwell GPU is recognized and ready for CUDA workloads. This means your system is set up for GPU-accelerated LLM inference.


## Step 3: Check the CUDA toolkit

To build the CUDA version of llama.cpp, the system must have a CUDA toolkit installed.

The `nvcc --version` command confirms that the CUDA compiler is available and compatible with CUDA 13.
This ensures that CMake can correctly detect and compile the GPU-accelerated components.

```bash
nvcc --version
```
You're almost ready! Verifying the CUDA toolkit ensures you can build GPU-enabled versions of llama.cpp for maximum performance.

You will see output similar to:

```output
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2025 NVIDIA Corporation
Built on Wed_Aug_20_01:57:39_PM_PDT_2025
Cuda compilation tools, release 13.0, V13.0.88
Build cuda_13.0.r13.0/compiler.36424714_0
```

{{% notice Note %}}
The nvcc compiler is required only during the CUDA-enabled build process; it is not needed at runtime for inference.
{{% /notice %}}

This confirms that the CUDA 13 toolkit is installed and ready for GPU compilation.
If the command is missing or reports an older version (e.g., 12.x), you should update to CUDA 13.0 or later to ensure compatibility with the Blackwell GPU (sm_121).

At this point, you have verified that:
- The Grace CPU (Arm Cortex-X925 / A725) is correctly recognized and supports Armv9 extensions
- The Blackwell GPU is active with driver 580.95.05 and CUDA 13 runtime
- The CUDA toolkit 13.0 is available for building the GPU-enabled version of llama.cpp

Your DGX Spark environment is now fully prepared for the next section,  where you will build and configure both CPU and GPU versions of llama.cpp, laying the foundation for running quantized LLMs efficiently on the Grace Blackwell platform.

## What you have accomplished

In this entire setup section, you have achieved the following:

- Verified your Arm-based Grace CPU and its capabilities by confirming that your system is running Armv9 cores with SVE2, BF16, and INT8 matrix multiplication support, which are perfect for quantized LLM inference
- Confirmed your Blackwell GPU and CUDA driver are ready by seeing that the GB10 GPU is active, properly recognized, and set up with CUDA 13, so you're all set for GPU-accelerated workloads
- Checked your operating system and CUDA toolkit - Ubuntu 24.04 LTS provides a solid foundation, and the CUDA compiler is installed and ready for building GPU-enabled inference tools

You're now ready to move on to building and running quantized LLMs on your DGX Spark. The next section walks you through compiling llama.cpp for both CPU and GPU, so you can start running AI inference on this platform.
