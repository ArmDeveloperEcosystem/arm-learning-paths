---
title: About memory latency
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Memory latency is one of the key factors impacting application performance. Developers benefit from having a good understanding of memory latency, how to measure it, and knowing when it can be improved.

Latency is the time between a request and the response. In the context of computer architecture, memory latency refers to the communication from the CPU to memory devices. A request is either a load (read) or a store (write) and the response is the loaded data or an acknowledgement that the store took place. The faster this communication happens the better the performance.

Computer hardware is constructed using multiple types of storage. In the area of memory latency, "memory devices" can be caches, external RAM, and storage devices such as solid state drives (SDD) or hard disk drives (HDD). 

In computer architecture, a CPU executes instructions, and some instructions use registers to transfer data to and from memory. The memory system is designed with caches which are close to the CPU and faster to access. Instructions are also placed in caches to improve performance by eliminating the need to fetch the same instructions from memory multiple times. 

In theory, a CPU can operate without any caches at all, but it would be much slower. 

How much slower would it be?

You can look at the list from [Latency Numbers Every Programmer Should Know](https://gist.github.com/jboner/2841832?permalink_comment_id=4123064#gistcomment-4123064) to learn about the time it takes to access various types of memory in a computer system.



| Operation                          |        ns       |      µs    |   ms   |  note                       |
| ---------------------------------- | --------------- | ---------- | ------ | --------------------------- |
| L1 cache reference                 |         0.5 ns  |            |        |                             |
| Branch mispredict                  |           5 ns  |            |        |                             |
| L2 cache reference                 |           7 ns  |            |        | 14x L1 cache                |
| Mutex lock/unlock                  |          25 ns  |            |        |                             |
| Main memory reference              |         100 ns  |            |        | 20x L2 cache, 200x L1 cache |
| Send 1K bytes over 1 Gbps network  |      10,000 ns  |      10 µs |        |                             |		
| Read 4K randomly from SSD*         |     150,000 ns  |     150 µs |        | ~1GB/sec SSD                |
| Read 1 MB sequentially from memory |     250,000 ns  |     250 µs |        |                             |
| Round trip within same datacenter  |     500,000 ns  |     500 µs |        |                             |
| Read 1 MB sequentially from SSD* 	 |   1,000,000 ns  |   1,000 µs |   1 ms | ~1GB/sec SSD, 4X memory     |
| Disk seek (HDD)                    |  10,000,000 ns  |  10,000 µs |  10 ms | 20x datacenter roundtrip    |
| Read 1 MB sequentially from disk   |  20,000,000 ns  |  20,000 µs |  20 ms | 80x memory, 20X SSD         |
| Send packet CA -> Netherlands -> CA| 150,000,000 ns  | 150,000 µs | 150 ms |                             |


Modern CPUs and RAM have very different latencies compared to those from 30, 20, or even 10 years ago. Even so, the improvements generally scale uniformly over the evolution of the CPUs. A Cortex-A15 CPU from 15 years ago might be based on a very different implementation of the Arm architecture compared to a current Neoverse-V2 CPU, but the orders of magnitude of latencies between the CPU and memory devices is similar.

A great visualization of how latencies have been reduced over the years of CPU evolution is given in [Colin Scott's Interactive latencies page](https://colin-scott.github.io/personal_website/research/interactive_latency.html). Use the slider the the top to change the year and see how the latency numbers change.

