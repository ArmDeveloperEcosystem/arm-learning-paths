---
title: Fundamentals of storage systems
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction

Ideally, your system's storage activity should be zero—meaning all application data and instructions are available in memory or cache, with no reads or writes to hard disk drives (HDDs) or solid-state drives (SSDs) required. However, due to physical capacity limits, data volatility, and the need to store large amounts of data, most applications frequently access storage media.

## High-Level Flow of Data

The diagram below provides a high-level overview of how data is written to or read from a storage device. It illustrates a multi-disk I/O architecture, where each disk (Disk 1 to Disk N) has its own I/O queue and optional disk cache, communicating with a central CPU via a disk controller. Memory, not explicitly shown, sits between the CPU and storage, offering fast but volatile access. File systems, also not depicted, operate at the OS/kernel level to handle file access metadata and provide a user-friendly interface through files and directories.

![disk i/o](./diskio.jpeg)

## Key Terms

#### Sectors and Blocks

Sectors are the basic physical units on a storage device. Traditional hard drives typically use a sector size of 512 bytes, while many modern disks use 4096 bytes (4K sectors) for improved error correction and efficiency.

Blocks are logical groupings of one or more sectors used by filesystems for data organization. A common filesystem block size is 4096 bytes, meaning each block might consist of eight 512-byte sectors, or map directly to a 4096-byte physical sector if supported by the disk.

#### Input/Output Operations per Second (IOPS)

IOPS measures how many random read or write requests your storage system can handle per second. IOPS can vary by block size and storage medium (e.g., flash drives). Traditional HDDs often do not specify IOPS; for example, AWS does not show IOPS values for HDD volumes.

![iops_hdd](./IOPS.png)

#### Throughput and Bandwidth

Throughput is the data transfer rate, usually measured in MB/s. Bandwidth specifies the maximum amount of data a connection can transfer. You can calculate storage throughput as IOPS × block size.

#### Queue Depth

Queue depth is the number of simultaneous I/O operations that can be pending on a device. Consumer SSDs typically have a queue depth of 32–64, while enterprise-class NVMe drives can support hundreds or thousands of concurrent requests per queue. Higher queue depth allows more parallelism and can improve I/O performance.

#### I/O Engine

The I/O engine is the software component in Linux that manages I/O requests between applications and the storage subsystem. For example, the Linux kernel’s block I/O scheduler queues and dispatches requests to device drivers, using multiple queues to optimize disk access. In benchmarking tools like fio, you can select I/O engines such as sync (synchronous I/O), `libaio` (Linux native asynchronous I/O), or `io_uring` (which uses newer Linux kernel features for asynchronous I/O).

#### I/O Wait

I/O wait is the time a CPU core spends waiting for I/O operations to complete.
