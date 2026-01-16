---
title: Thread pinning fundamentals
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## CPU affinity

CPU affinity is the practice of binding a process or thread to a specific CPU core or set of cores. This tells the operating system scheduler where that work is allowed to run. By default, the Linux scheduler dynamically migrates threads across cores to balance load and maximize overall throughput. Pinning overrides this behavior by constraining execution to a chosen set of cores.

## Pinning

Pinning is most often used as a fine-tuning technique for workloads that aim to consume as many CPU cycles as possible while running alongside other demanding applications. Scientific computing pipelines and real-time analytics frequently fall into this category. 

Applications that pin processes to specific cores are often sensitive to latency variation rather than just average throughput. They may also have intricate memory access patterns. Pinning can reduce execution noise and provide more consistent behavior or better memory access patterns under load.

## Memory locality 

Memory locality provides another important motivation for pinning. On modern systems with Non-Uniform Memory Access (NUMA) architectures, different cores have varying memory access times and characteristics. The performance depends on where the data is fetched from.

For example, in a server with two CPU sockets that appears as a single processor, memory access times differ depending on which core you use. By pinning threads to cores that are close to the memory they use and allocating memory accordingly, you can reduce memory access latency and improve bandwidth.

## Setting affinity

You can set affinity directly in source code using system calls. Many parallel frameworks expose higher-level controls, such as OpenMP affinity settings, that manage thread placement automatically. 

Alternatively, at runtime, system administrators can pin existing processes using utilities like `taskset` or launch applications with `numactl` to control both CPU and memory placement without modifying code.

## Conclusion

Pinning is a tradeoff. It can improve determinism and locality, but it can also reduce flexibility and hurt performance if the chosen layout isn't optimal or if system load changes. Over-constraining the scheduler may lead to idle cores while pinned threads contend unnecessarily. 

As a general rule, rely on the operating system scheduler initially and introduce pinning only when you're looking to fine-tune performance after measuring baseline behavior.
