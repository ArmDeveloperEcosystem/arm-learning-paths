---
title: Memory Latency & Caches
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is Latency?

You can find plenty of detailed explanation on latency in computer memory online, but we will not be providing textbook definitions here. 
The goal is to make Arm developers -but developers for other platforms might also benefit- understand what exactly is latency and how it affects the performance of their software.

In short, latency is the time passed between the request and its response. In particular, in the context of computer architectures, memory latency refers to the communication from the CPU to memory devices, the request is either a load or a store and the response is the content of the load or an acknowledgement that the store actually took place. Obviously, the faster this happens the better.

Now "memory devices" is mentioned here in the broader sense, as memory can be internal (L1, L2, L3 cache) or external (RAM) or even a storage device like an SSD or HDD.

Strictly speaking, when we refer to the CPU in computer architecture terms, we usually mean only the units that perform some form of operations, and the registers. The caches are of course part of the CPU and the CPU die, but they are operating in a transparent way to the user. In theory the CPU could operate just fine without any cache at all -of course much much slower. So, how much slower?

Let's take a look at the current list from [Latency Numbers Every Programmer Should Know](https://gist.github.com/jboner/2841832?permalink_comment_id=4123064#gistcomment-4123064)

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

These devices have different ways to connect to the main CPU.

Modern CPUs and RAM have very different latencies than the ones from 30, 20 or even 10 years ago. Even so, the differences sort of scale uniformly over the evolution of the CPUs. An Armv7-a iMX515 CPU from 15 years ago might be based on a very different implementation of the Arm architecture compared to an Ampere and a Graviton3, but the orders of magnitude of latencies between the CPU and memory devices will be similar.

A great visualization of the how the latencies have been reduced over the years of CPU evolution is given in [Colin Scott's Interactive latencies page](https://colin-scott.github.io/personal_website/research/interactive_latency.html).

