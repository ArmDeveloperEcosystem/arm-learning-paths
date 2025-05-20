---
title: Page Size Overview
weight: 2
### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How the CPU Locates Your Data

When your program asks for a memory address, the CPU doesn’t directly reach into RAM or swap space for it; that would be slow, unsafe, and inefficient.
 
Instead, it goes through the **virtual memory** system, where it asks for a specific chunk of memory called a **page**. Pages map virtual memory location to physical memory locations in RAM or swap space.

## What’s a Memory “Page”?

Think of your computer’s memory like a big sheet of graph paper. Each **page** is one square on that sheet. The **page table** is the legend that tells the computer which square (virtual address) maps to which spot in real RAM.

---

## Small Pages (4 KB) vs. Big Pages (64 KB)

| Aspect          | 4 KB Pages                             | 64 KB Pages                              |
|-----------------|----------------------------------------|------------------------------------------|
| **Size**        | Small “bricks” (4 KB each)             | Big “bricks” (64 KB each)                |
| **Flexibility** | Very flexible—good for lots of tiny bits of data | Less flexible—best when data comes in large chunks |
| **Efficiency**  | Needs more entries (more bookkeeping)  | Needs fewer entries (less bookkeeping)   |
| **Waste**       | At most 4 KB unused per page           | Up to 64 KB unused if not fully used     |

---

## When to Choose Which

- **4 KB pages** are the safe, default choice. They let you use memory in small slices and keep waste low.  Since they are smaller, you need more of them when handling larger memory footprint applications.  This creates more overhead for the CPU to manage, but may be worth it for the flexibility.  They are great for applications that need to access small bits of data frequently, like web servers or databases with lots of small transactions.

- **64 KB pages** shine when you work with big, continuous data—like video frames or large database caches—because they cut down on management overhead.  They can waste more memory if you don’t use the whole page, but they can also speed up access times for large data sets.

When rightsizing your page size, its important to **try both** under real-world benchmarking conditions, as it will depend on the data size and retrieval patterns of the data you are working with.  In addition, the page size may need to be adjusted over time as the application, usage patterns, and data size changes.  

## Choose the OS to experiment with

{{% notice Do not test on Production%}}
Modifying the Linux kernel page size can lead to system instability or failure. Perform testing in a non-production environment before applying to production systems.
{{% /notice %}}

This learning path will guide you how to change (and revert back) the page size, so you can begin experimenting to see which fits best. The steps to install the 64K page size kernel are different for each OS, so be sure to select the correct one.


- [Ubuntu](../ubuntu)
- [Debian](../debian)
- [CentOS](../centos)

---
