---
title: What about cache alignment?
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What about cache alignment?

In our previous example, we used a simple struct of only 20 bytes for the `buffer`, plus 8 more bytes for the 64-bit pointer `next`. Now typically the compiler will try to enforce 64-bit (8-byte) or 16-byte alignment on allocating objects. Perhaps we could enforce some kind of larger alignment and see if it has any effect?

Let's try the following changes in the `node` struct and `init_alloc`:

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

Basically, what we have done can be summarized in these steps:
* Align our allocator to start from a 64-byte address using `posix_memalign`. This is because in most CPUs a cache line is 64 bytes long.
* Use `__attribute__((packed))` in the struct definition so that it takes the smallest possible space in memory.
* Reorder the buffer and pointer elements of the struct, this is to help `memcpy()` later in `new_node` to copy to an aligned buffer.
* Increase the `buffer` size to 24 so that the node struct is exactly 32 bytes long.

Again, compile with `gcc -O3 -o memory-latency2 memory-latency2.c -Wall` and the output is:

```bash
$ ./memory-latency2
1000000 Nodes creation took 4092 us
```

This is a 31% performance increase mainly because of better alignment of the buffer we allocated for our simple allocator and subsequently the alignment of the objects that `simple_alloc()` will return. Furthermore, the fact that `memcpy()` will operate on aligned buffers also helped.

## When is memory alignment important?

For algorithms that are memory-bound and not CPU-bound, i.e. when the CPU is found waiting for data to arrive from memory most of the time rather than processing that data. We will show it with a slight modification to our previous example, where bad alignment hurts performance.

```C
typedef struct __attribute__((packed)) node {
    char pad;
    struct node *next;
    char pad2;
    char buffer[24];
} node_t;
```

The same elements exist in the struct, with the same sizes. However, we have added a single byte as padding to both `next` and `buffer`. Because of the `packed` attribute, the compiler will try to honour exactly this restriction and will be forced to use these elements with an offset of 1 and 10 bytes respectively. Compiling and running this example will give these numbers:

```bash
$ ./memory-latency2
1000000 Nodes creation took 5575 us
```

We see that the wrong memory alignment has a very bad effect on performance, our code is now 36% slower than our previous fastest example. This was an easy example, but rest assured there are plenty of opportunities in code out there that can be better optimized in terms of memory alignment!

Next we will show another trick to reduce latency.
