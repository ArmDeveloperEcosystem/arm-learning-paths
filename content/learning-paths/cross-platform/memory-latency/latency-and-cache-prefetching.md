---
title: Cache Prefetching
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Cache prefetching

So, our previous result -without the padding counter-example- shows a nice performance increase, but could we improve this further without changing our algorithm too much or resorting to rewriting the code in assembly? Remember that the original problem of memory latency exists because the CPU has to wait for data to arrive from memory to cache and from there to the registers. There is a way to actually do that, it's called _Cache Prefetching_ and essentially it instructs the CPU to prefetch some data to arrive to L1 cache so that it is available when the next instruction(s) request it. You have to keep in mind that typical RAM latency is ~100ns, so it is not enough to prefetch the data that will be processed in the _next_ iteration of a loop, but a few iterations _ahead_.

Let's try prefetching in our example, where would be the right place to tell the CPU to prefetch data? Although all CPUs have their own cache prefetching assembly instructions, it is usually recommended to use a GCC builtin that has become the defacto standard in this case, due to its portability. Unless you are writing assembly code or code that requires particular cache prefetching instructions, we recommend you use the builtin `__builtin_prefetch()` in your code. In this particular case we will add it in `init_alloc`:

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

Compiling with `gcc -O3 -o memory-latency2 memory-latency2.c -Wall` and running the example, doesn't show any benefit, and there are two reasons for that. First, remember that you have to prefetch the data that will be used in the iterations ahead and not just the data that is going to be used immedieately. Secondly, prefetching tells the CPU to prefetch data just this once, but it would benefit us to do this as part of the loop. To counter the first argument, let's try increasing the prefetching by multiples of the cache line size, eg. 8 * 64 or 16 * 64:

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

And this is the result:

```bash
$ ./memory-latency2
1000000 Nodes creation took 3800 us
```

Not bad, an extra ~300ms shaved off the total latency. This is because the CPU was able to load the first 16 * 64 bytes directly from cache in the first iterations, but what about the rest? For that we have to add the prefetch command in the loop, the place to do it is inside `simple_alloc()`, let's add a similar call to `__builtin_prefetch()`:

```C
static void* simple_alloc(size_t size) {
    if (cur_ + size <= end_) {
      void *ptr = cur_;
      cur_ += size;
      counter_++;
      __builtin_prefetch(cur_ + 16*64);
      return ptr;
    } else {
       printf("Error allocating %ld bytes!", size);
    }
    return NULL;
}
```

After compiling our code we get the following:

```bash
$ ./memory-latency2
1000000 Nodes creation took 2772 us
```

We essentially doubled the performance of our code, without changing our data structure or our algorithm, the only thing we did was make it easier for the CPU to find the data in the L1 cache when it needs it. Cache prefetching is an essential part of software optimization process, in some cases the CPU is smart enough to recognize a data transfer pattern and start the prefetch on its own, especially in more modern CPUs, but many times a manual nudge is needed. Remember that we ran this code on a bleeding edge SVE2 CPU, though the results should not differ that much from an Ampere CPU or a Raspberry Pi or even another architecture.