---
title: Page Size Overview
weight: 2
### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How the CPU Locates Your Data

When your program asks for a memory address, the CPU doesn’t directly reach into RAM or swap space for it; that would be slow, unsafe, and inefficient.
 
Instead, it goes through the **virtual memory** system, where it asks for a specific chunk of memory called a **page**. Pages map virtual memory location to physical memory locations in RAM or swap space.

### Page Table Entries (PTEs)

Virtual address translation is performed via a multi-level page table lookup. The **leaf-level** entry, commonly called the **Page-Table Entry (PTE)**:

1. Maps the **Virtual Page Number (VPN)** to a **Physical Frame Number (PFN)**.  
2. Indicates whether the page is resident or needs to be read from swap or RAM.

On a 4K page size system, each leaf PTE is 8 bytes, so one 4 KiB page of page-table memory holds 512 PTEs (512 × 8 B = 4 KB). When you dereference a virtual address, the system performs operations on the data to compute the **physical address** of the data being looked up.

![PTE Flow](images/pte.png)
    

## Page Size Differences Illustrated

To help make page sizing more clear, assume you have created a database system that can store and retrieve either images, OR tweets, based on the mode set at install-time.

### 4K Page Size
With our system set to a 4K page size, the system can only store a small amount of data in each page. At around 300 bytes per tweet, when the system retrieves a tweet from memory, it will most likely be retrieved in a single page load. This is very efficient, since the CPU has to do less work to find the data it needs, and the structure size (page) is optimized for the size of the data its storing (tweet).  At 4K, best-case, the system can store about 13 tweets in a single 4K page.  

When the system is set to "Image Only" mode, since an image is a larger amount of data (assume 1MB or more for this example), it will most likely be retrieved in multiple 4K page loads.  This is less efficient, as the CPU has to do more work to retrieve all bytes of the image.  If the image is 1MB, the system will have to reserve 256 4K pages (256 * 4K = 1MB). 

Given this info, you decide to set the page size to 64K to see how performance changes.

### 64K Page Size
With our system now set to 64K page size, the system reserves pages in 64K chunks.  In our tweet example, we can now store about 218 tweets per page.  If we're working with groupings of the same tweets over and over, the system needs to reserve and load fewer pages to get the data it needs to run the application, resulting in a fast and efficient system.  This is because the CPU has to do less page loads to find the data it needs.

When the system is set to "Image Only" mode, since an image is a larger amount of data (1MB or more), the image will still need to be retrieved in multiple 64K page loads.  However, this is more inefficient than the 4K page size; if the image is 1MB, the system will only need to load and store 16 pages at a 64K page size (16 * 64K = 1MB) vs 256 pages of memory (256 * 4K = 1MB) at a 4K page size.

### Inefficiencies
Inefficiencies occur when the system is set to a page size that does not consistently match the data size of the objects you are working with.  For example, if the system is set to 64K page size, and the application only needs one tweet, the system loaded more data (a 64K page) than was actually needed.

When loading a single image, with the page size is larger, the page size is better rightsized for the data the application works with -- it may need to load 16 pages of 64K each, but it is still less than the 256 pages of 4K each that it would need to load if the system was set to 4K page size.

In addition to the amount of page loading the CPU has to do, the system also has to reserve memory to store and track metadata for each page.  For 4 KiB pages, each page-table page holds 512 entries (8 B each), so tracking 256 pages only consumes one 4 KiB page of metadata..  Internal fragmentation can occur when the system reserves memory for pages that are not used and/or modified, and this can lead to wasted memory and performance issues especially with larger page sizes.  

To add further complexity, if you choose to add the ability for the system to store BOTH images and tweets (not one at a time), the system will need to load both types of data, and the page size will need to be set to a size that is best suited to accommodate both types of data and their retrieval patterns.  

This leads to more performance hits, as the system will most likely now always load fewer or more pages than necessary for each type of data.

It may be difficult to determine the best page size for your application, as it will depend on the data size and retrieval patterns of the data you are working with.  In addition, the page size may need to be adjusted over time as the application and data size changes.  

This learning path will guide you how to change the page size, so you can begin experimenting to see which fits best.

## Choose Your OS

To begin, select the OS you are using.  The steps to install the 64K page size kernel are different for each OS, so be sure to select the correct one.

- [Ubuntu](../ubuntu)
- [Debian](../debian)
- [CentOS](../centos)

---
