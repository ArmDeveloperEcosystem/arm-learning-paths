---
review:
    - questions:
        question: >
            When is software affected by memory latency?
        answers:
            - When RAM is slower than the CPU
            - When you type faster than the CPU can copy to RAM
            - When the CPU has to wait for data to arrive most of the time
            - When your computer uses latent RAM DIMMs
        correct_answer: 3
        explanation: >
            Memory latency problems are mostly apparent on algorithms that are memory-bound, or in other words, the CPU spends most of the time waiting for data to transfer from/to RAM.

    - questions:
        question: >
            How can we help fix memory latency problems?
        answers:
            - We replace our RAM with faster RAM
            - We use a combination of methods, restrict data transfers in critical loops to a minimum, align data with L1 cache line size, use cache prefetching
            - We use padding bytes of size equal to the CPU's cache line in all our structs
            - We increase the cache size of our CPU
        correct_answer: 2
        explanation: >
            Although sometimes we can indeed remedy the problem with faster RAM, we will still hit the upper limit of maximum RAM frequency supported by our CPU/motherboard.
            The proper solution is to minimize and group memory access in our algorithm so that our CPU is not stalled waiting from data to arrive from memory.
            Proper alignment and cache prefetching also help greatly.
               
    - questions:
        question: >
            How far ahead should we prefetch data into cache?
        answers:
            - 256 bytes
            - 1MB
            - It depends on our algorithm, but data that will take at least 100ns to arrive in the cache from RAM
            - We have to fill the L1/L2 caches completely
        correct_answer: 3
        explanation: >
            All that matters is that our data is in the L1 cache when the CPU needs it, taking into account that memory loads can take up to 100ns to complete,
            we should do a rough count of cycles each iteration takes and use that. If we cannot do that, testing multiples of cache line size is a decent alternative.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
