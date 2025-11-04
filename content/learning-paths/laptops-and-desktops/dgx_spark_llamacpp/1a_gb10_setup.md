---
title: Verify Grace Blackwell system readiness for AI inference
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Verify your GB10 development environment

Let's verify that your DGX Spark system is configured and ready for building and running quantized LLMs.

## Check the CPU information

To check the CPU information, run the following command to print the CPU information:

```bash
lscpu
```

Expected output:

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

Great! You've checked your CPU configuration. Your system is using Armv9 cores, which are ideal for quantized LLM workloads. The Grace CPU implements the Armv9-A instruction set and supports advanced vector extensions, making it ideal for quantized LLM inference and tensor operations.

The following table summarizes the key specifications of the Grace CPU and explains their relevance to quantized LLM inference.

| **Category** | **Specification** | **Description / Impact for LLM Inference** |
|---------------|-------------------|---------------------------------------------|
| Architecture | Armv9-A (64-bit, aarch64) | Modern Arm architecture supporting advanced vector and AI extensions. |
| Core Configuration | 20 cores total — 10× Cortex-X925 (Performance) + 10× Cortex-A725 (Efficiency) | Heterogeneous CPU design balancing high performance and power efficiency. |
| Threads per Core | 1 | Optimized for deterministic scheduling and predictable latency. |
| Clock Frequency | Up to **4.0 GHz** (Cortex-X925)<br>Up to **2.86 GHz** (Cortex-A725) | High per-core speed ensures strong single-thread inference for token orchestration. |
| Cache Hierarchy | L1: 1.3 MiB × 20<br>L2: 25 MiB × 20<br>L3: 24 MiB × 2 | Large shared L3 cache enhances data locality for multi-threaded inference workloads. |
| Instruction Set Features** | SVE / SVE2, BF16, I8MM, AES, SHA3, SM4, CRC32 | Vector and mixed-precision instructions accelerate quantized (Q4/Q8) math operations. |
| NUMA Topology | Single NUMA node (node0: 0–19) | Simplifies memory access pattern for unified memory workloads. |
| Security & Reliability | Not affected by Meltdown, Spectre, Retbleed, or similar vulnerabilities | Ensures stable and secure operation for long-running inference tasks. |

Its SVE2, BF16, and INT8 matrix multiplication (I8MM) capabilities make it ideal for quantized LLM workloads, providing power-efficient foundation for both CPU-only inference and CPU–GPU hybrid processing.

You can also verify the operating system running on your DGX Spark by using the following command:

```bash
lsb_release -a
```

Expected output:

```log
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 24.04.3 LTS
Release:	24.04
Codename:	noble
```
As shown above, DGX Spark runs on Ubuntu 24.04 LTS, a developer-friendly Linux distribution.
It provides excellent compatibility with AI frameworks, compiler toolchains, and system utilities—making it an ideal environment for building and deploying quantized LLM workloads.

Nice work! You've confirmed your operating system is Ubuntu 24.04 LTS, which is well-supported for AI development on Arm.

## Step 2: Verify Blackwell GPU and driver

After confirming your CPU configuration, verify that the Blackwell GPU inside the GB10 Grace Blackwell Superchip is available and ready for CUDA workloads.

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

The table below provides more explanation of the `nvidia-smi` output:

| **Category** | **Specification (from nvidia-smi)** | **Description / Impact for LLM Inference** |
|---------------|--------------------------------------|---------------------------------------------|
| GPU Name** | NVIDIA GB10 | Confirms the system recognizes the Blackwell GPU integrated into the Grace–Blackwell Superchip. |
| Driver Version | 580.95.05 | Indicates that the system is running the latest driver package required for CUDA 13 compatibility. |
| CUDA Version | 13.0 | Confirms that the CUDA runtime supports GB10 (sm_121) and is ready for accelerated quantized LLM workloads. |
| Architecture / Compute Capability | Blackwell (sm_121) | Supports FP4, FP8, and BF16 Tensor Core operations optimized for LLMs. |
| Memory | Unified 128 GB LPDDR5X (shared with CPU via NVLink-C2C) | Enables zero-copy data access between Grace CPU and GPU for unified inference memory space. |
| Power & Thermal Status | ~4W at idle, 32°C temperature | Confirms the GPU is powered on and thermally stable while idle. |
| GPU-Utilization | 0% (Idle) | Indicates no active compute workloads; GPU is ready for new inference jobs. |
| Memory Usage | Not Supported (headless GPU configuration) | DGX Spark operates in headless compute mode; display memory metrics may not be exposed. |
| Persistence Mode | On | Ensures the GPU remains initialized and ready for rapid inference startup. |

Excellent! Your Blackwell GPU is recognized and ready for CUDA workloads. This means your system is set up for GPU-accelerated LLM inference.


## Step 3: Check the CUDA Toolkit

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
- The Grace CPU (Arm Cortex-X925 / A725) is correctly recognized and supports Armv9 extensions.
- The Blackwell GPU is active with driver 580.95.05 and CUDA 13 runtime.
- The CUDA toolkit 13.0 is available for building the GPU-enabled version of llama.cpp.

Your DGX Spark environment is now fully prepared for the next section,  where you will build and configure both CPU and GPU versions of llama.cpp, laying the foundation for running quantized LLMs efficiently on the Grace Blackwell platform.

## What have I achieved?

You have:
- Verified your Arm-based Grace CPU and its capabilities
- Confirmed your Blackwell GPU and CUDA driver are ready
- Checked your operating system and CUDA toolkit

You're now ready to move on to building and running quantized LLMs on your DGX Spark!
