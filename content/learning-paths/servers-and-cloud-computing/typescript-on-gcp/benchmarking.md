---
title: TypeScript Benchmarking
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## JMH-style Custom Benchmarking

This section demonstrates how to benchmark TypeScript functions using a JMH-style (Java Microbenchmark Harness) methodology implemented with Node.js’s built-in `perf_hooks` module.
Unlike basic `console.time()` measurements, this approach executes multiple iterations, computes the average runtime, and produces stable and repeatable performance data, useful for evaluating workloads on your Google Cloud C4A (Axion Arm64) VM running SUSE Linux.

### Create the Benchmark Script
Create a file named `benchmark_jmh.ts` inside your project directory with the content below:

```typescript
import { performance } from 'perf_hooks';

// Function to benchmark
const sumArray = (n: number) => {
    let sum = 0;
    for (let i = 0; i < n; i++) sum += i;
    return sum;
};

// Benchmark parameters
const iterations = 10;           // Number of repeated runs
const arraySize = 1_000_000;     // Size of array
let totalTime = 0;

// JMH-style repeated runs
for (let i = 0; i < iterations; i++) {
    const start = performance.now();
    sumArray(arraySize);
    const end = performance.now();
    const timeTaken = end - start;
    totalTime += timeTaken;
    console.log(`Iteration ${i + 1}: ${timeTaken.toFixed(3)} ms`);
}

// Compute average execution time
const averageTime = totalTime / iterations;
console.log(`\nAverage execution time over ${iterations} iterations: ${averageTime.toFixed(3)} ms`);
```
Code explanation:

| Component               | Description                                                                                                                                                |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`performance.now()`** | Provides high-resolution timestamps (sub-millisecond precision) for accurate timing.                                                                       |
| **`sumArray(n)`**       | A simple CPU-bound function that sums integers from 0 to `n`. This simulates a computational workload suitable for benchmarking raw arithmetic throughput. |
| **`iterations`**        | Defines how many times the test runs. Multiple repetitions reduce noise and help average out one-off delays or GC pauses.                                  |
| **Loop and averaging**  | Each run’s duration is recorded; the mean execution time is then reported, mirroring how JMH computes stable results in Java microbenchmarks.          |


This JMH-style benchmarking approach provides more accurate and repeatable performance metrics than a single execution, making it ideal for performance testing on Arm-based systems.

### Compile the TypeScript Benchmark
First, compile the benchmark file from TypeScript to JavaScript using the TypeScript compiler (tsc):

```console
tsc benchmark_jmh.ts
```
This command transpiles your TypeScript code into standard JavaScript, generating a file named `benchmark_jmh.js` in the same directory.
The resulting JavaScript can be executed by Node.js, allowing you to measure performance on your Google Cloud C4A (Arm64) virtual machine.

### Run the Benchmark
Now, execute the compiled JavaScript file with Node.js:

```console
node benchmark_jmh.js
```
You should see output similar to:

```output
Iteration 1: 2.286 ms
Iteration 2: 0.749 ms
Iteration 3: 1.145 ms
Iteration 4: 0.674 ms
Iteration 5: 0.671 ms
Iteration 6: 0.671 ms
Iteration 7: 0.672 ms
Iteration 8: 0.667 ms
Iteration 9: 0.667 ms
Iteration 10: 0.673 ms

Average execution time over 10 iterations: 0.888 ms
```

### Benchmark Metrics Explained

  * Iteration times → Each iteration represents the time taken for one complete execution of the benchmarked function.
  * Average execution time → Calculated as the total of all iteration times divided by the number of iterations. This gives a stable measure of real-world performance.
  * Why multiple iterations?
    A single run can be affected by transient factors such as CPU scheduling, garbage collection, or memory caching.
    Running multiple iterations and averaging the results smooths out variability, producing more repeatable and statistically meaningful data, similar to Java’s JMH benchmarking methodology.
    
### Interpretation

The average execution time reflects how efficiently the function executes under steady-state conditions.
The first iteration often shows higher latency because Node.js performing initial JIT (Just-In-Time) compilation and optimization, a common warm-up behavior in JavaScript/TypeScript benchmarks.

### Benchmark summary on Arm64
Results from the earlier run on the `c4a-standard-4` (4 vCPU, 16 GB memory) Arm64 VM in GCP (SUSE):

| Iteration | 1     | 2     | 3     | 4     | 5     | 6     | 7     | 8     | 9     | 10    | Average |
|-----------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|---------|
| Time (ms) | 2.286 | 0.749 | 1.145 | 0.674 | 0.671 | 0.671 | 0.672 | 0.667 | 0.667 | 0.673 | 0.888   |

### TypeScript performance benchmarking summary on Arm64

When you look at the benchmarking results, you will notice that on the Google Axion C4A Arm-based instances:

- The average execution time on Arm64 (~0.888 ms) shows that CPU-bound TypeScript operations run efficiently on Arm-based VMs.
- Initial iterations may show slightly higher times due to runtime warm-up and optimization overhead, which is common across architectures.  
- Arm64 demonstrates stable iteration times after the first run, indicating consistent performance for repeated workloads.  

This demonstrates that Google Cloud C4A Arm64 virtual machines provide production-grade stability and throughput for TypeScript workloads, whether used for application logic, scripting, or performance-critical services.
