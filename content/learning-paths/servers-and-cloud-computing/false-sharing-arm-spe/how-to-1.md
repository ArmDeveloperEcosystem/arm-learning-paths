---
title: Introduction to Arm_SPE and False Sharing
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction to Arm Statistical Profiling Extension (SPE)

Traditional performance tracing relies on counting whole instructions, capturing only architectural instructions without revealing the actual memory addresses, pipeline latencies, or micro-operations in flight; moreover, the “skid” phenomenon where events are falsely attributed to later instructions can mislead developers. 

The Arm Statistical Profiling Extension (SPE) integrates sampling directly into the CPU pipeline, triggering on individual micro-operations rather than retired instructions, thereby eliminating skid and blind spots. Each SPE sample record includes relevant meta data, such as data addresses, per-µop pipeline latency, triggered PMU event masks, and the memory hierarchy source (L1 cache, last-level cache, or remote socket), enabling fine-grained and precise cache analysis. 

This enables software developers to tune user-space software for characteristics such as memory latency, and cache statistics. Importantly, it is the mechanism on Arm to enable cache statistics with the Linux `perf` cache-to-cache utility, referred to as `perf c2c`. Please refer to the [Arm_SPE whitepaper](https://developer.arm.com/documentation/109429/latest/) for more details. 

In this learning path we will use the `arm_spe` and `perf c2c` to diagnose a cache issue for an application running on a Neoverse server.

## False Sharing within the Cache

Even when two threads touch entirely separate variables, modern processors move data in fixed-size cache lines (nominally 64-bytes). If those distinct variables happen to occupy bytes within the same line, every time one thread writes its variable the core’s cache must gain exclusive ownership of the whole line, forcing the other core’s copy to be invalidated. The second thread, still working on its own variable, then triggers a coherence miss to fetch the line back, and the ping-pong repeats. Please see the illustration below, taken from the [Arm_SPE whitepaper](https://developer.arm.com/documentation/109429/latest/), for a visual explanation.

![false_sharing_diagram](./false_sharing_diagram.png)

Because false sharing hides behind ordinary writes, the easiest time to eliminate it is while reading or refactoring the source code—padding or realigning the offending variables before compilation. In large, highly concurrent code-bases, however, data structures are often accessed through several layers of abstraction, and many threads touch memory via indirection, so the subtle cache-line overlap may not surface until profiling or performance counters reveal unexpected coherence misses.

From a source-code perspective nothing is “shared,” but at the hardware level both variables are implicitly coupled by their physical colocation.

## Alignment to Cache Lines

In C++11, we can manually specify the alignment of an object using the `alignas` function. For example, in the C++11 source code below, we manually align the the `struct` every 64 bytes (typical cache line size on a modern processor). This ensures that each instance of `AlignedType` is on a separate cache line. 

```c++
#include <atomic>
#include <iostream>

struct alignas(64) AlignedType {
  AlignedType() { val = 0; }
  std::atomic<int> val;
};


int main() {
  // If we create four atomic integers like this, there's a high probability
  // they'll wind up next to each other in memory
  std::atomic<int> a;
  std::atomic<int> b;
  std::atomic<int> c;
  std::atomic<int> d;

  std::cout << "\n\nWithout Alignment can occupy same cache line\n\n";
  // Print out the addresses
  std::cout << "Address of atomic<int> a - " << &a << '\n';
  std::cout << "Address of atomic<int> b - " << &b << '\n';
  std::cout << "Address of atomic<int> c - " << &c << '\n';
  std::cout << "Address of atomic<int> d - " << &d << '\n';

  AlignedType e{};
  AlignedType f{};
  AlignedType g{};
  AlignedType h{};

  std::cout << "\n\nMin 1 cache-line* spacing between variables";
  std::cout << "\n*64 bytes = minimum 0x40 address increments\n\n";

  std::cout << "Address of AlignedType e - " << &e << '\n';
  std::cout << "Address of AlignedType f - " << &f << '\n';
  std::cout << "Address of AlignedType g - " << &g << '\n';
  std::cout << "Address of AlignedType h - " << &h << '\n';

  return 0;
}
```

Example output below shows the variables e, f, g and h occur at least 64-bytes addreses apart in our byte-addressable architecture. Whereas variables a, b, c and d occur 8 bytes apart (i.e. occupy the same cache line). 

Although this is a contrived example, in a production workload there may be several layers of indirection that unintentionally result in false sharing. For these complex cases, to understand the root cause we will use `perf c2c`.

```output
Without Alignment can occupy same cache line

Address of atomic<int> a - 0xffffeb6c61b8
Address of atomic<int> b - 0xffffeb6c61b0
Address of atomic<int> c - 0xffffeb6c61a8
Address of atomic<int> d - 0xffffeb6c61a0


Min 1 cache-line* spacing between variables
*64 bytes = minimum 0x40 address increments

Address of AlignedType e - 0xffffeb6c6140
Address of AlignedType f - 0xffffeb6c6100
Address of AlignedType g - 0xffffeb6c60c0
Address of AlignedType h - 0xffffeb6c6080
```