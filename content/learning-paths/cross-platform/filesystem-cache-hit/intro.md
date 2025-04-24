---
title: Recap of Filesystems caching and Memory
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Recap of File Systems

A file system is the method an operating system uses to store, organize, and manage data on storage devices like hard drives or SSDs. Linux uses a virtual file system (VFS) layer to provide a uniform interface to different file system types (e.g., `ext4`, `xfs`, `btrfs`), allowing programs to interact with them in a consistent way. 

Developers typically interact with the file system through system calls or standard library functions—for example, using `open()`, `read()`, and `write()` in C to access files. For instance, reading a configuration file at `/etc/myapp/config.json` involves navigating the file system hierarchy and accessing the file’s contents through these interfaces. To speed up access to such files, the operating system creates a file system cache, managed by the kernel and resides in main memory (RAM). This cache temporarily stores recently accessed file data and metadata to speed up future reads and reduce disk I/O.


## Recap of Memory Usage

The hardware and operating system is responsible for managing the memory usage of the system.

The well-known command `free -wh` provides a snapshot of memory usage. The `cache` column includes the portion of memory used to store the file system cache. 

```output
               total        used        free      shared     buffers       cache   available
Mem:           7.6Gi       1.1Gi       5.8Gi       960Ki        22Mi       832Mi       6.5Gi
Swap:             0B          0B          0B
```

The command summarises the memory usage into the following columns. 

- `total`: Total installed memory
- `used`: Memory in use (excluding cache/buffers)
- `free`: Unused memory
- `shared`: Memory used by tmpfs and shared between processes
- `buffers`: Memory used by kernel buffers
- `cache`:  Memory used by file system cache
- `available`: An estimate of memory available (both free memory and memory that can be reclaimed) when a new process starts.


### What is the posix_fadvise syscall?

`posix_fadvise` is a Linux system call that allows a program to provide the kernel with hints about its expected file access patterns, such as sequential or random reads. These hints help the kernel optimize caching and I/O performance but are purely advisory—the system may choose to ignore them. It’s particularly useful for tuning performance when working with large files or when bypassing unnecessary caching.

### When the posix_fadvise syscall could be of use?

You should consider using `posix_fadvise` when:

- You're reading or writing large files that won't fit entirely in RAM.
- You want to avoid polluting the cache with data you won't reuse.
- You know the access pattern ahead of time and can optimize accordingly.

The syscall doesn’t guarantee behavior, but it influences how the kernel allocates caching resources.



