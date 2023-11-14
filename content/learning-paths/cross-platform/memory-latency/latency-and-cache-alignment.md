---
title: Cache alignment
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In the previous example, a node is represented by a simple struct of only 20 bytes for the `buffer`, plus 8 more bytes for the 64-bit pointer `next`. 

Typically, the compiler will try to enforce 64-bit (8-byte) or 16-byte alignment when allocating objects. 

To learn about cache alignment, you can enforce larger alignment and see if it has any impact on performance. 

Make the following changesi to the `node` struct and `init_alloc` in the `memory-latency2.c` file:

```C
typedef struct __attribute__((packed)) node {
    char buffer[24];
    struct node *next;
} node_t;

...

static void init_alloc() {
    if (start_ == NULL) {
        int rc = posix_memalign(&start_, 64, SIMPLE_ALLOCATOR_SIZE);
        if (rc != 0) {
            printf("Error allocating %ld bytes for allocator!", SIMPLE_ALLOCATOR_SIZE);
            exit(1);
        }
        ...
}
```

Here is a summary of the changes:
* Align the allocator to start from a 64-byte address using `posix_memalign`. This is because most CPUs have a 64 byte cache line size.
* Use `__attribute__((packed))` in the struct definition so that it takes the smallest possible space in memory.
* Reorder the buffer and pointer elements of the struct. This helps `memcpy()` later in `new_node` to copy to an aligned buffer.
* Increase the `buffer` size to 24 so that the node struct is exactly 32 bytes long.

As before, compile the new file:

```bash
gcc -O3 -o memory-latency2 memory-latency2.c -Wall
```

Run the application:

```bash
./memory-latency2
```

The output will print the time taken to run the application:

```output
1000000 Nodes creation took 4092 us
```

Your results may be slightly different, but this is a 31% performance increase. The increase is due to better alignment of the allocated buffer and the alignment of the objects that `simple_alloc()` returns. 

Furthermore, `memcpy()` operating on aligned buffers also improves performance.


## When is memory alignment important?

Memory alignment is important for algorithms that are memory-bound (when the CPU is mostly waiting for data to arrive from memory rather than processing data).

To demonstrate decreased performance, make a change to `node` structure as shown below:

```C
typedef struct __attribute__((packed)) node {
    char pad;
    struct node *next;
    char pad2;
    char buffer[24];
} node_t;
```

The same elements exist in the struct, with the same sizes. However, a single byte of padding is added to both `next` and `buffer`. 

Because of the `packed` attribute, the compiler honors this restriction and is forced to use these elements with an offset of 1 and 10 bytes respectively. 

Compile and run again:

```bash
gcc -O3 -o memory-latency2 memory-latency2.c -Wall
./memory-latency2
```

The output shows the program takes long than the previous version. 

```output
1000000 Nodes creation took 5575 us
```

Poor memory alignment has a negative impact on performance. The code is now 36% slower than the previous version. 

This was an easy example, but there are plenty of opportunities to optimize code using memory alignment.

The next section shows another way to reduce memory latency, cache prefetching. 

To prepare, remove the padding fields from the `node` structure so it is back to the best performance. 
