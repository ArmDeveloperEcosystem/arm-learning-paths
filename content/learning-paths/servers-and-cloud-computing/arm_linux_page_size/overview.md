---
title: Page Size Overview
weight: 2
### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How does the CPU locate data in memory?

When your program asks for a memory address, the CPU doesn’t directly reach into RAM or swap space for it; that would be slow, unsafe, and inefficient.
 
Instead, it goes through the virtual memory system, where it asks for a specific chunk of memory called a page. Pages map virtual memory locations to physical memory locations in RAM or swap space.

## What’s a memory page?

Think of your computer’s memory like a big sheet of graph paper. Each page is one square on that sheet. The page table is the legend that identifies which square (virtual address) maps to which spot in physical RAM. On x86, 4K is the only page size option, but Arm-based systems allow you to use 4K, 16K, or 64K page sizes to fine tune the performance of your applications. 

This Learning Path explains how to switch between 4K and 64K pages on different Linux distributions.

## How should I select the memory page size?

Points to consider when thinking about page size:

- **4K pages** are the safe, default choice. They let you use memory in small slices and keep waste low. Since they are smaller, you need more of them when handling larger memory footprint applications. This creates more overhead for the operating system to manage, but it may be worth it for the flexibility. They are great for applications that need to access small bits of data frequently, like web servers or databases with lots of small transactions.

- **64K pages** shine when you work with large, continuous data such as video frames or large database caches because they cut down on management overhead. They will use more memory if you don’t use the whole page, but they can also speed up access times for large data sets.

When selecting your page size, it's important to try both options under real-world conditions, as it will depend on the data size and retrieval patterns of the data you are working with.  

In addition, the page size may need to be reviewed over time as the application, memory usage patterns, and data sizes may change.  


### Summary of page size differences

| Aspect          | 4K Pages                             | 64K Pages                              |
|-----------------|--------------------------------------|----------------------------------------|
| **Size**        | Small “bricks” (4 KB each)           | Big “bricks” (64 KB each)              |
| **Flexibility** | Very flexible—good for lots of tiny bits of data | Less flexible—best when data comes in large chunks |
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
