---
title: Fundamentals of storage systems
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction

Ideally, performance-sensitive application data should reside in memory or cache, minimizing reads and writes to disk-based storage. However, due to physical memory limits, data volatility, and the need for persistent storage, most applications frequently access SSDs or HDDs.

## High-level flow of data

The diagram below provides a high-level overview of how data is written to or read from a storage device. It illustrates a multi-disk I/O architecture, where each disk (Disk 1 to Disk N) has its own I/O queue and optional disk cache, communicating with a central CPU via a disk controller. While memory is not shown in this diagram, it plays a central role in the data path - offering fast but volatile access between the CPU and persistent storage. File systems, also not depicted, operate at the OS/kernel level to handle file access metadata and provide a user-friendly interface through files and directories.

![disk i/o](./diskio.jpeg)

## Key Terms

#### Sectors and Blocks

Sectors are the smallest physical storage units, typically 512 or 4096 bytes. Many modern drives use 4K sectors for better error correction and efficiency.

Blocks are logical groupings of one or more sectors used by file systems to organize data. A typical block size is 4096 bytes. It might span multiple 512-byte sectors or align directly with a 4K physical sector if supported by the device.


#### Input/Output Operations per Second (IOPS)

IOPS measures how many random read or write requests your storage system can perform per second. It varies based on block size and device type. For example, AWS does not show IOPS values for traditional HDD volumes.

![iops_hdd](./IOPS.png)

#### Throughput and Bandwidth

Throughput is the data transfer rate, usually measured in MB/s. Bandwidth specifies the maximum amount of data a connection can transfer. You can calculate storage throughput as IOPS × block size.

#### Queue Depth

Queue depth is the number of simultaneous I/O operations that can be pending on a device. Consumer SSDs typically have a queue depth of 32–64, while enterprise-class NVMe drives can support hundreds or thousands of concurrent requests per queue. Higher queue depths allow more operations to be handled simultaneously, which can significantly boost throughput on high-performance drives — especially NVMe SSDs with advanced queuing capabilities.
 
#### I/O Engine

The I/O engine is the software component in Linux that manages I/O requests between applications and the storage subsystem. For example, the Linux kernel's block I/O scheduler queues and dispatches requests to device drivers, using multiple queues to optimize disk access. In benchmarking tools like `fio`, you can select I/O engines such as `sync` (synchronous I/O), `libaio` (Linux native asynchronous I/O), or `io_uring` (which uses newer Linux kernel features for asynchronous I/O).

#### I/O Wait

I/O wait is the time a CPU core spends waiting for I/O operations to complete. Tools like `pidstat`, `top`, and `iostat` can help monitor I/O wait, allowing you to identify storage-related CPU bottlenecks.
