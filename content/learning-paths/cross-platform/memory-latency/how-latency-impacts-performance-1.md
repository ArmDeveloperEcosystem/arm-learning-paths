---
title: How latency impacts performance - part 1
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How latency impacts software - part 1

We have the explanation of latency, we have the numbers, we know we have to "reduce the latencies" in our code, but that is still too vague, how can we do that exactly?

For you as a user, latency can impact your software in multiple ways. From UI aspects: mouse clicks/movements in software have a time lag, to CPU processing: an image processing filter takes way too long to complete, to loading/saving times: the word processor takes too long to load/store the changes from/to disk, even games: multi-player games have a lag with too many players online at the same time.

Now, some of these problems are too difficult to solve without a substantial rethinking and restructuring of the problem or even replacing the hardware. But some are due to software and algorithmic decisions, these can usually be fixed without the cost of replacing hardware. These are the ones we will tackle in this article.

Let's take an actual example of C code that demonstrates the general problem of latency, for example a program that creates a large number of C linked list nodes in a loop for use later. These might be graph objects used in ML/DL application, or texture element objects in a 3D environment for a game. Let's assume that these objects are created on the fly, so memory has to be allocated for them at runtime using a function like `malloc()`. We will measure the time to create a number of those objects in a loop as measuring time for a single one happens too fast and has a large statistical error margin.

```C
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stddef.h>
#include <sys/time.h>

typedef struct node {
    struct node *next;
    char buffer[20];
} node_t;

#define NODES                     1000000

node_t *new_node(node_t *prev, const char *payload, size_t size) {
    node_t *n = (node_t *) malloc(sizeof(node_t));
    if (n == NULL) {
        printf("Error allocating %ld bytes for struct node!", sizeof(node_t));
        exit(1);
    }
    // Copy the payload into the node
    memcpy(n->buffer, payload, size);
    n->next = NULL;

    if (prev) {
        prev->next = n;
    }
    return n;
}

void free_nodes(node_t *n) {
    if (!n) return;
    while (n->next) {
        node_t *next = n->next;
        free(n);
        n = next;
    }
}

int main() {
    const char text[] = "This is a sample text";
    node_t *node0 = new_node(NULL, text, strlen(text));

    node_t * node = node0;
    struct timeval start, end;
    gettimeofday(&start, NULL);
    for (int i=1; i < NODES; i++) {
        node = new_node(node, text, strlen(text));
    }
    gettimeofday(&end, NULL);

    int duration = ((end.tv_sec - start.tv_sec) * 1000000) + (end.tv_usec - start.tv_usec);
    printf("%d Nodes creation took %d us\n", NODES, duration);

    free_nodes(node0);
}
```

Compiling this with `gcc -O3 -o memory-latency1 memory-latency1.c -Wall` and running it on an SVE2 system, will give us the following output. This is actually totally portable code so you can test it on any architecture.

```bash
$ ./memory-latency1
1000000 Nodes creation took 29473 us
```

Out of curiosity, let's run our code through linux `perf` command, to do some simple profiling and see where those 30ms (30000us) are spent. We first run `sudo perf record ./memory-latency1` to gather the profiling information. It's a simple program so the output will be small. Afterwards we get the profiling output with `sudo perf report`:

```
# Overhead  Command          Shared Object          Symbol                                
# ........  ...............  .....................  ......................................
#
    24.62%  memory-latency1  libc.so.6              [.] malloc
    23.70%  memory-latency1  libc.so.6              [.] _int_malloc
    17.14%  memory-latency1  [kernel.kallsyms]      [k] __pi_clear_page
     5.77%  memory-latency1  [kernel.kallsyms]      [k] get_page_from_freelist
     4.01%  memory-latency1  [kernel.kallsyms]      [k] unmap_page_range
     3.34%  memory-latency1  [kernel.kallsyms]      [k] free_unref_page_list
     2.03%  memory-latency1  memory-latency1        [.] main
     ...
```

Surprisingly -or not for knowledgeable people- our `main()` is not even in the 5% of the time spent by the CPU on our program, the majority is spent on `malloc()` and kernel related functions!
This means that all the time was spent on routines that had almost nothing to do with the core of our program! Imagine this being at the heart of a 3D rendering pipeline!

Surely there is a way to improve this? Thankfully, there are, many!