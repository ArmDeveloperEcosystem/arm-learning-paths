---
title: Arm Statistical Profiling Extension and false sharing
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is the Arm Statistical Profiling Extension (SPE), and what does it do?

{{% notice Learning goal%}}
In this section, you will learn how the Arm Statistical Profiling Extension (SPE) gives you deeper visibility into how your applications interact with the CPU. It covers how to detect and fix false sharing, which is a hidden performance problem in multithreaded code, by using cache line alignment in C++ and tools like Perf C2C.
{{% /notice %}}

Arm’s Statistical Profiling Extension (SPE) gives you a powerful way to understand what’s really happening inside your applications at the microarchitecture level. Introduced in Armv8.2, SPE captures a statistical view of how instructions move through the CPU, which allows you to dig into issues like memory access latency, cache misses, and pipeline behavior.

Most Linux profiling tools focus on retired instruction counts, which means they miss key details like memory addresses, cache latency, and micro-operation behavior. This can lead to misleading results — especially due to a phenomenon called “skid,” where events are falsely attributed to later instructions.

SPE integrates sampling directly into the CPU pipeline, triggering on individual micro-operations instead of retired instructions. This approach eliminates skid and blind spots. Each SPE sample record includes relevant metadata, such as data addresses, per-µop pipeline latency, triggered PMU event masks, and the memory hierarchy source, enabling fine-grained, precise cache analysis. 

SPE helps developers optimize user-space applications by showing where cache latency or memory access delays are happening. Importantly, cache statistics are enabled with the Linux Perf cache-to-cache (C2C) utility.

For more information, see the [*Arm Statistical Profiling Extension: Performance Analysis Methodology White Paper*](https://developer.arm.com/documentation/109429/latest/). 

In this Learning Path, you will use SPE and Perf C2C to diagnose a cache issue for an application running on a Neoverse server.

## What is false sharing and why should I care about it?

In large-scale, multithreaded applications, false sharing can degrade performance by introducing hundreds of unnecessary cache line invalidations per second - often with no visible red flags in the source code.

Even when two threads touch entirely separate variables, modern processors move data in fixed-size cache lines, which is typically 64 bytes. If those distinct variables happen to occupy bytes within the same line, every time one thread writes its variable the core’s cache must gain exclusive ownership of the whole line, forcing the other core’s copy to be invalidated. 

The second thread, still working on its own variable, then triggers a coherence miss to fetch the line back, and the ping-pong pattern repeats. 

The diagram below, taken from the Arm SPE white paper, provides a visual representation of two threads on separate cores alternately gaining exclusive access to the same cache line.

![false_sharing_diagram alt-text#center](./false_sharing_diagram.png "Two threads on separate cores alternately gain exclusive access to the same cache line.")

Because false sharing hides behind ordinary writes, the easiest time to eliminate it is while reading or refactoring the source code by padding or realigning the offending variables before compilation. In large, highly concurrent codebases, however, data structures are often accessed through several layers of abstraction, and many threads touch memory via indirection, so the subtle cache-line overlap may not surface until profiling or performance counters reveal unexpected coherence misses.

From a source-code perspective nothing is “shared,” but at the hardware level both variables are implicitly coupled by their physical location.

## Alignment to cache lines

In C++11, you can manually specify the alignment of an object with the `alignas` specifier. For example, the C++11 source code below manually aligns the `struct` every 64 bytes (typical cache line size on a modern processor). This ensures that each instance of `AlignedType` is on a separate cache line. 

```cpp
#include <atomic>
#include <iostream>

struct alignas(64) AlignedType {
  AlignedType() { val = 0; }
  std::atomic<int> val;
};


int main() {
  // If you create four atomic integers like this, there's a high probability
  // they'll wind up next to each other in memory
  std::atomic<int> a;
  std::atomic<int> b;
  std::atomic<int> c;
  std::atomic<int> d;

  std::cout << "\n\nWithout alignment, variables can occupy the same cache line\n\n";
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

The output below shows that the variables e, f, g and h occur at least 64 bytes apart in the byte-addressable architecture. Whereas variables a, b, c, and d occur 8 bytes apart, occupying the same cache line. 

Although this is a contrived example, in a production workload there might be several layers of indirection that unintentionally result in false sharing. For these complex cases, to understand the root cause, you can use Perf C2C.

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

## Summary

In this section, you explored what Arm SPE is and why it offers a deeper, more accurate view of application performance. You also examined how a subtle issue like false sharing can impact multithreaded code, and how to mitigate it using data alignment techniques in C++.

Next, you'll set up your environment and use Perf C2C to capture and analyze real cache behavior on an Arm Neoverse system.


