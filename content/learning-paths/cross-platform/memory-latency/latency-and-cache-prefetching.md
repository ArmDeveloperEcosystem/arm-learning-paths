---
title: Cache prefetching
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---


Cache prefetching is another way to increase performance without changing the algorithm much and without rewriting the code in assembly. 

Remember, that the original problem of memory latency exists because the CPU must wait for data to arrive from memory. Cache prefetching is a way to instruct the CPU to prefetch data to arrive in the L1 cache so that it is already close to the CPU when needed. Keep in mind that typical RAM latency is about 100 ns, so it is not enough to prefetch the data that will be processed in the _next_ iteration of a loop, but it needs to be done a few iterations before. 

You can try cache prefetching on the example. 

The first step is to determine the right place to tell the CPU to prefetch data. Although all CPUs have their own cache prefetching assembly instructions, it is recommended to use a GCC builtin that has become the de facto standard for portability. Unless you are writing assembly code or code that requires particular cache prefetching instructions, you should use the builtin `__builtin_prefetch()` in your code. 

Add the cache prefetching builtin to the `init_alloc()` function as shown below:

```C
static void init_alloc() {
    if (start_ == NULL) {
        ...
        __builtin_prefetch(start_);
        memset(start_, 0, SIMPLE_ALLOCATOR_SIZE);
        ...
    }
}
```

Compiling and running the example code doesn't show any benefit. 

There are two reasons:
- You need to prefetch the data that will be used in the iterations ahead, not immediately before use.
- Prefetching tells the CPU to prefetch data just once, but it would benefit to do this as part of the loop. 

To counter the first argument, try increasing the prefetching by a multiple of the cache line size, 16 * 64.

```C
static void init_alloc() {
    if (start_ == NULL) {
        ...
        __builtin_prefetch(start_ + 16 * 64);
        memset(start_, 0, SIMPLE_ALLOCATOR_SIZE);
        ...
    }
}

```

Compile and run the application again:

```bash
gcc -O3 -o memory-latency2 memory-latency2.c -Wall
./memory-latency2
```

The output shows the program takes long than the previous version. 

```output
1000000 Nodes creation took 3800 us
```

Prefetching eliminates additional time from the program. 

This is because the CPU is able to load the first 16 * 64 bytes directly from cache in the first iteration.

Next, add the prefetch command in the loop, the place to do it is inside `simple_alloc()` function. 

Add a similar call to `__builtin_prefetch()` as shown below in `simple_alloc()`:

```C
static void* simple_alloc(size_t size) {
    if (cur_ + size <= end_) {
      void *ptr = cur_;
      cur_ += size;
      counter_++;
      __builtin_prefetch(cur_ + 16 * 64);
      return ptr;
    } else {
       printf("Error allocating %ld bytes!", size);
    }
    return NULL;
}
```

Compile and run the application again:

```bash
gcc -O3 -o memory-latency2 memory-latency2.c -Wall
./memory-latency2
```

Here is the new output, the lowest value so far:

```output
1000000 Nodes creation took 2772 us
```

Using cache prefetching, you have doubled the performance of the code, without changing the data structure or the algorithm. 

The changes make it easier for the CPU to find the data in the L1 cache when needed. 

Cache prefetching is an essential part of the software optimization process. In some cases the CPU is smart enough to recognize a data transfer pattern and start the prefetch on its own, especially in the latest Arm CPUs. Sometimes a manual nudge is needed to improve performance. 
