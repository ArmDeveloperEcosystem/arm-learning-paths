---
title: Overview
weight: 2
### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Page size fundamentals

Before you modify the Linux kernel page size on an Arm system, you need to know what a page is, why size matters, and how size affects performance.

## What’s a memory page?

Think of your computer’s memory like a big sheet of graph paper. Each page is one square on that sheet. 

The page table acts like a legend on the map, showing which virtual address square corresponds to a specific location in physical RAM. This mapping is managed by the operating system and the CPU’s Memory Management Unit (MMU).

To keep track of these mappings efficiently, CPUs use a fast lookup cache called the Translation Lookaside Buffer (TLB). Every access first attempts a TLB hit; a miss forces a page table lookup. If the page isn't already in the TLB, the CPU must fetch the mapping from memory—a process that adds latency and stalls execution.

On x86 systems, 4K pages are the standard, while Arm-based systems support multiple page sizes - typically 4K, 16K, or 64K. This flexibility allows developers to fine-tune performance for specific workloads. 

You'll learn how to switch between 4K, 16K, and 64K pages on different Linux distributions.

## How does the CPU locate data in memory?

When your program accesses a memory address, the CPU doesn’t directly fetch data from RAM or swap space for it. That would be slow, unsafe, and inefficient. Direct physical access would bypass isolation and invalidate caches.
 
Instead, it goes through the virtual memory system, where it asks for a specific chunk of memory called a page. Pages map virtual memory locations to physical memory locations in RAM or swap space.

## How does page size affect performance?

Changing the page size has a cascading effect on system performance:

**Memory Fragmentation**: Smaller pages reduce internal fragmentation, which is the wasted memory per allocation. Larger pages can increase waste if your workloads don’t use the full page.

**TLB Pressure**: With smaller pages such as 4K, more entries are needed to map the same amount of memory. This increases TLB misses and page-table-walk overhead. Larger pages, such as 64K, reduce the number of entries and can lower TLB pressure.

**I/O Efficiency**: Disk I/O and DMA operations often perform better with larger pages, because fewer page boundaries are crossed during transfers (fewer interrupts, larger DMA bursts).

### Trade-offs to consider

| Aspect | 4K pages | 16K pages | 64K pages |
|---|---|---|---|
| **Flexibility** | Highest compatibility | Balance of compatibility and reach | Best for large, contiguous memory workloads |
| **Efficiency** | Needs the most page table entries | Needs fewer entries than 4K pages | Needs the fewest entries |
| **Internal fragmentation** | Up to about 4 KB per partly used page | Up to about 16 KB per partly used page | Up to about 64 KB per partly used page |
| **TLB reach** | Lowest | Higher than 4K pages | Highest |

Linux distribution support varies. Debian 12 and later provide a packaged 16K kernel, while the Ubuntu and CentOS instructions use packaged 64K kernels. Debian users can also build a 64K kernel from source.

## How do I select the memory page size?

Points to consider when thinking about page size:

- **4K pages** are the safe, default choice. They let you use memory in small slices and keep waste low. Since they are smaller, you need more of them when handling larger memory footprint applications. This creates more overhead for the operating system to manage, but it may be worth it for the flexibility. They are great for applications that need to access small bits of data frequently, like web servers or databases with lots of small transactions.

- **16K pages** provide a middle ground. They increase TLB reach compared with 4K pages while reducing the internal fragmentation risk of 64K pages.

- **64K pages** shine when you work with large, contiguous data such as video frames or large database caches because they cut down on management overhead. They will use more memory if you don’t use the whole page, but they can also speed up access times for large data sets.

Choosing the right page size depends on how your application uses memory, as both the data size and retrieval patterns of the data you are working with are influencing factors. Benchmark different options under real-world workloads to determine which delivers better performance.

In addition, the page size might need to be reviewed over time as the application, memory usage patterns, and data sizes might change. 

## Try out a page size for your workload

The best way to determine the impact of page size on application performance is to experiment with both options.

{{% notice Warning%}}
Do not modify the Linux kernel page size in a production environment. It can lead to system instability or failure. Perform testing in a non-production environment before applying to production systems.
{{% /notice %}}

Select your Arm Linux distribution to install an available larger-page kernel. The Debian instructions cover both 16K and 64K page sizes.

- [Ubuntu](/learning-paths/servers-and-cloud-computing/arm_linux_page_size/ubuntu/)
- [Debian](/learning-paths/servers-and-cloud-computing/arm_linux_page_size/debian/)
- [CentOS](/learning-paths/servers-and-cloud-computing/arm_linux_page_size/centos/)
