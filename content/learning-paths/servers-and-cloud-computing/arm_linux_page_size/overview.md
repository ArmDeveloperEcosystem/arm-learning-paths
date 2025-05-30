---
title: Why does page size matter?
weight: 2
### FIXED, DO NOT MODIFY
layout: learningpathall
---
Before you modify the Linux kernel page size on an Arm system, it's essential to understand what a memory page is - and why its size affects performance.

## What’s a memory page?

Think of your computer’s memory like a big sheet of graph paper. In modern systems, memory is divided into chunks called pages. Each page is one square on that sheet. 

The page table is the legend that identifies which square (virtual address) maps to which spot in physical RAM.  Each page represents a fixed-size block of virtual memory that maps to physical memory through the page table. This mapping is managed by the operating system and the CPU’s Memory Management Unit (MMU).

To keep track of these mappings efficiently, CPUs use a fast lookup cache called the Translation Lookaside Buffer (TLB). Every memory access requires a TLB hit or a page table lookup. If the page isn't already in the TLB, the CPU must fetch the mapping from memory—a process that adds latency and stalls execution.

On x86 systems, 4K pages are the standard, while Arm-based systems support multiple page sizes - typically 4K, 16K, or 64K. This flexibility allows developers to fine tune performance for specific workloads. 

This Learning Path explains how to switch between 4K and 64K pages on different Linux distributions.

## How does the CPU locate data in memory?

When your program accesses a memory address, the CPU doesn’t directly fetch data from RAM or swap space for it. That would be slow, unsafe, and inefficient.
 
Instead, it goes through the virtual memory system, where it asks for a specific chunk of memory called a page. Pages map virtual memory locations to physical memory locations in RAM or swap space.

## How page size affects performance
Changing the page size has a cascading effect on system performance:

TLB Pressure: With smaller pages (e.g., 4K), more entries are needed to map the same amount of memory. This increases TLB misses and lookup overhead. Larger pages (e.g., 64K) reduce the number of entries and can lower TLB pressure.

Memory Fragmentation: Smaller pages reduce internal fragmentation (wasted memory per allocation). Larger pages can increase waste if your workloads don’t use the full page.

I/O Efficiency: Disk I/O and DMA operations often perform better with larger pages, because fewer page boundaries are crossed during transfers.

## How should I select the memory page size?

Points to consider when thinking about page size:

- **4K pages** are the safe, default choice. They let you use memory in small slices and keep waste low. Since they are smaller, you need more of them when handling larger memory footprint applications. This creates more overhead for the operating system to manage, but it may be worth it for the flexibility. They are great for applications that need to access small bits of data frequently, like web servers or databases with lots of small transactions.

- **64K pages** shine when you work with large, continuous data such as video frames or large database caches because they cut down on management overhead. They will use more memory if you don’t use the whole page, but they can also speed up access times for large data sets.

Choosing the right page size depends on how your application uses memory, as both the data size and retrieval patterns of the data you are working with are influencing factors. Benchmark different options under real-world workloads to determine which delivers better performance.

In addition, the page size may need to be reviewed over time as the application, memory usage patterns, and data sizes may change.  


### Trade-offs to consider

| Aspect          | 4K Pages                             | 64K Pages                              |
|-----------------|--------------------------------------|----------------------------------------|
| **Size**        | Small “bricks” (4 KB each)           | Big “bricks” (64 KB each)              |
| **Flexibility** | Best for flexibility and compatibility | Best for large, contiguous memory workloads |
| **Efficiency**  | Needs more entries (more bookkeeping) | Needs fewer entries (less bookkeeping) |
| **Waste**       | At most 4 KB unused per page         | Up to 64 KB unused if not fully used   |

This Learning Path covers switching between 4K and 64K page sizes because these are supported by most Arm Linux distributions. In some cases, you may find that 16K page size is a sweet spot for your application, but Linux kernel, hardware, and software support is limited. One example of 16k page size is [Asahi Linux](https://asahilinux.org/).

## Experiment to see which works best for your workload

The best way to determine the impact of page size on application performance is to experiment with both options.

{{% notice Do not test on Production%}}
Modifying the Linux kernel page size can lead to system instability or failure. Perform testing in a non-production environment before applying to production systems.
{{% /notice %}}

Select the Arm Linux distribution you are using to find out how to install the 64K page size kernel.

- [Ubuntu](/learning-paths/servers-and-cloud-computing/arm_linux_page_size/ubuntu/)
- [Debian](/learning-paths/servers-and-cloud-computing/arm_linux_page_size/debian/)
- [CentOS](/learning-paths/servers-and-cloud-computing/arm_linux_page_size/centos/)
