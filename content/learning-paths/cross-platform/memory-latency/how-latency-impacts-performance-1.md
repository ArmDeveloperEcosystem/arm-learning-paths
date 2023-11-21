---
title: How latency impacts performance - part 1
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

{{% notice Note %}}
The results you will see are likely be different than those in the sample output. The processor and system you use impact the results, but the learning is useful for any Arm processor.
{{% /notice %}}

We have the explanation about latency, we have the numbers and we know we have to "reduce the latencies" in our code, but how can we do that exactly?
You can learn more about how to reduce latency in applications by studying the below example software. 

Latency impacts software in multiple ways. In user interfaces, mouse clicks and movements may have a time lag. In CPU processing, an image processing filter may take too long to complete. In applications, a word processor make take too long to save or load files from disk. In games, multi-player games may have a lag when many players are online at the same time.

Some of these latency problems are difficult to solve without a substantial restructuring of the application or even replacing the hardware. However, some latency issues are caused by software and algorithmic decisions. These problems can often be fixed without replacing the hardware. 

Below is an example of a software application which can be improved by changes to the software algorithm and where the example C program demonstrates the general problem of latency. 

The program creates a large number of C linked list nodes in a loop for later use. These might be graph objects in an ML application or texture element objects in a 3D game. 

Assume these objects are created on the fly, so memory has to be allocated for them at runtime using the `malloc()` function. 

You can measure the time it takes to loop and create the objects. Because the loop count is large, you get a good idea of the average time to allocate nodes. 

Use a text editor to copy the code below into a file named `memory-latency1.c`

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

You need a C compiler to build the code examples (GCC or Clang can be used). The examples below were built with `gcc` but `clang` can be substituted in any of the commands. 

Compile the code using GCC:

```bash
gcc -O3 -o memory-latency1 memory-latency1.c -Wall 
```

Run the application:

```bash
./memory-latency1
```

The output prints the time taken to run the application:

```output
1000000 Nodes creation took 29473 us
```

Your results will differ based on the type of machine and the compiler you use. 

You can use `perf` to understand where the time is spend. 

If you don't have `perf` installed or need help to configure your computer to run `perf` refer to the [Perf for Linux on Arm install guide](/install-guides/perf/).

We first run `sudo perf record ./memory-latency1` to gather the profiling information. It's a simple program so the output is small. Afterwards we get the profiling output with `sudo perf report`:

Run the application again with `perf` using:

```bash
perf record ./memory-latency1
```

When the application completes, generate the report using:

```bash
perf report
```

The output will be similar to:

```output
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

Surprisingly, the `main()` function is less than 5% of the run time. The majority of time is spent in `malloc()` and kernel related functions.

This means that most of the time is spent on routines that have almost nothing to do with the behavior of the program.

The next section presents ways to improve performance. 
