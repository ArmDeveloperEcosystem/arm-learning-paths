---
title: Background Information
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction


CPU thread pinning in Linux refers to explicitly binding a thread or an entire process identified by a PID to one or more specific CPU cores. By default the Linux scheduler dynamically migrates threads across cores to balance load and maximize overall throughput. Pinning overrides this behavior by constraining execution to a chosen set of cores.

Pinning is most often used as a fine-tuning technique for workloads that aim to consume as many CPU cycles as possible while running alongside other demanding applications. Scientific computing pipelines and real time style analytics frequently fall into this category. Typical applications that pin processes to specific cores are often sensitive to latency variation rather than just average throughput or have intricate memory access patterns. Pinning can reduce this noise and provide more consistent execution behavior or better memory access patterns under load.

Another important motivation is memory locality. On modern systems with Non Uniform Memory Access architectures (NUMA), different cores have memory access times and characteristics depending on where the data is fetched from. For example, in a server with 2 CPU sockets that, from a programmers view, appears as a single processor would have different memory access times depending on the core. By pinning threads to cores that are close to the memory they use and allocating memory accordingly, an application can reduce memory access latency and improve effective bandwidth. 

CPU affinity is the practice of binding a process or thread to a specific CPU core or set of cores, telling the operating system scheduler where that work is allowed to run. Developers can set affinity directly in source code using system calls. Many parallel frameworks expose higher level controls such as OpenMP affinity settings that manage thread placement automatically. Alternatively, at runtime system administrators can pin existing processes using utilities like `taskset` or launch applications with `NUMACTL` to control both CPU and memory placement without modifying code.

Pinning is a tradeoff. It can improve determinism and locality but it can also reduce flexibility and hurt performance if the chosen layout is suboptimal or if system load changes. Over constraining the scheduler may lead to idle cores while pinned threads contend unnecessarily. As a general rule it is best to rely on the operating system scheduler as a first pass and introduce pinning only after hypothesis and measurement shows a clear benefit. 
