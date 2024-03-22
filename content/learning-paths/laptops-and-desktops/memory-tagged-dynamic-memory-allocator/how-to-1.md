---
title: Why Use Memory Tagging?
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## The Memory Tagging Extension (MTE)

The purpose of the Memory Tagging Extension (MTE) is to decrease the likelihood of memory misuse due to
programmer mistakes or deliberate attacks on software.

MTE does the following:
* Adds a 4 bit "logical tag" to pointers.
* Adds a 4 bit "allocation tag" to every 16 bytes of memory (referred to as a "granule").
* On accessing that memory, MTE compares the logical tag and the allocation tag. If there is a mismatch, an exception is raised.

When and how to tag memory is a choice made by software. In some cases
existing software can be relinked with libraries that already use MTE to get
extra protection. Sometimes the software itself will have to be modified to
handle tagged memory.

In the case of this learning path, applications using the memory allocator will likely need no changes. However, the memory allocator itself will need changes as it must manage the memory tags.

## Memory Tagging For a Dynamic Memory Allocator

The source code shown in this path is based on the allocator from the
[Write a Dynamic Memory Allocator](/learning-paths/cross-platform/dynamic-memory-allocator/) learning path. Subsequent modifications have been made to the code to support MTE.

The main operations for a dynamic memory allocator are as follows:
* To allocate some amounts of memory and structures to manage that memory
* To mark some portion of that memory as used by a program (usually called `malloc` in C)
* To mark some portion of that memory as not used by a program (usually called `free` in C)

All of these are low level operations which need to be aware of memory tagging.

Understanding how and why these operations protect memory requires some understanding of the potential attacks on the allocator.

Therefore, we will first present the source code of the allocator and guide you through building it. Then you can use it to understand the example attacks that are shown
later.
