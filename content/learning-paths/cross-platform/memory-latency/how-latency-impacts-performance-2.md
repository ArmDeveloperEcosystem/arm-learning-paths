---
title: How latency impacts performance - part 2
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How latency impacts software - part 2


Let's copy the original `memory-latency1.c` to `memory-latency2.c` and add the following code after the first `#define`:

```C
...
#define NODES                     1000000
#define SIMPLE_ALLOCATOR_SIZE     100000000UL

static void *start_ = NULL;
static void *cur_ = NULL;
static void *end_ = NULL;
static size_t counter_ = 0;

static void init_alloc() {
    if (start_ == NULL) {
        start_ = malloc(SIMPLE_ALLOCATOR_SIZE);
        if (start_ == NULL) {
            printf("Error allocating %ld bytes for allocator!", SIMPLE_ALLOCATOR_SIZE);
            exit(1);
        }
        memset(start_, 0, SIMPLE_ALLOCATOR_SIZE);
        cur_ = start_;
        end_ = start_ + SIMPLE_ALLOCATOR_SIZE;
        printf("start_: %p, end_: %p\n", start_, end_);
    }
}

static void* simple_alloc(size_t size) {
    if (cur_ + size <= end_) {
      void *ptr = cur_;
      cur_ += size;
      counter_++;
      return ptr;
    } else {
       printf("Error allocating %ld bytes!", size);
    }
    return NULL;
}
```

and let's replace the `malloc()` with the new function `simple_alloc()` in `new_node()`:
```C
node_t *new_node(node_t *prev, const char *payload, size_t size) {
    node_t *n = (node_t *) simple_alloc(sizeof(node_t));
    if (n == NULL) {
    ...
}
```

Function `free_node()` is not needed right now, we can remove it, and add the `init_alloc()` in the start of `main()` and `free(start_)` at the end to free the buffer allocated by our simple allocator:

```C
int main() {
    init_alloc();
    ...

    free(start_);
}
```

Now let's compile this new file again with `gcc -O3 -o memory-latency2 memory-latency2.c -Wall` and run it. On an SVE2 system this will give us the following output. This is actually totally portable code so you can test it on any architecture.


```bash
$ ./memory-latency2
1000000 Nodes creation took 5374 us
```

Let's do the profiling trick again with `./memory-latency2`, the output of the `perf report` will be:

```
# Overhead  Command          Shared Object          Symbol                    
# ........  ...............  .....................  ..........................
#
    49.68%  memory-latency2  memory-latency2        [.] main
    29.03%  memory-latency2  [kernel.kallsyms]      [k] __pi_clear_page
     3.38%  memory-latency2  [kernel.kallsyms]      [k] free_unref_page
     3.32%  memory-latency2  [kernel.kallsyms]      [k] rcu_all_qs
     3.18%  memory-latency2  [kernel.kallsyms]      [k] folio_batch_move_lru
     3.01%  memory-latency2  [kernel.kallsyms]      [k] __cond_resched
     2.89%  memory-latency2  [kernel.kallsyms]      [k] get_page_from_freelist
     1.83%  memory-latency2  [kernel.kallsyms]      [k] crng_make_state
     1.55%  memory-latency2  [kernel.kallsyms]      [k] ptep_clear_flush
     1.07%  memory-latency2  ld-linux-aarch64.so.1  [.] __tunable_get_val
```

Just replacing the memory allocator for a simpler allocator gives us a very significant speed gain of at least 5x! This method of using custom allocators is very popular in performance-critical applications and libraries where the default system allocators are too generic or slow for the needs of the particular usecase. A Linear Allocator like the one we used here, is one of the simplest form of memory allocators and it's quite popular in systems with known fixed size objects or known constrained size limits. Of course there are many more allocators for different sizes and quite a few of them are much faster than the default `malloc()`.