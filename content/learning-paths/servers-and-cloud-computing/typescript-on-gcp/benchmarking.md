---
title: TypeScript Benchmarking
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## JMH-style Custom Benchmarking

This section demonstrates how to **benchmark TypeScript functions** using a JMH-style approach with Node.js `perf_hooks`. Unlike simple `console.time` timing, this method performs **repeated iterations**, calculates the **average execution time**, and provides more **reliable and stable performance measurements** on your Arm64 SUSE VM.

### Create the Benchmark Script
Create a file named `benchmark_jmh.ts` in your project folder:

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

- **`performance.now()`** → Provides a high-resolution timestamp in milliseconds for precise timing measurements.  
- **`sumArray`** → A sample CPU-bound function that sums numbers from 0 to `n`.  
- **`iterations`** → Defines how many times the benchmark should run to stabilize results and minimize random variations.  
- **`for` loop** → Executes the target function multiple times and records the duration of each run.  
- **`totalTime / iterations`** → Calculates the **average execution time** across all runs, similar to how **JMH (Java Microbenchmark Harness)** operates in Java.  

This JMH-style benchmarking approach provides **more accurate and repeatable performance metrics** than a single execution, making it ideal for performance testing on Arm-based systems.

### Compile the TypeScript Benchmark
Compile the TypeScript benchmark file into JavaScript:

```console
tsc benchmark_jmh.ts
```
This generates a `benchmark_jmh.js` file that can be executed by Node.js.

### Run the Benchmark
Execute the compiled JavaScript file:

```console
node benchmark_jmh.js
```
You should see an output similar to:

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

- **Iteration times** → Each iteration shows the **time taken for a single execution** of the function being benchmarked.  
- **Average execution time** → Calculated as the sum of all iteration times divided by the number of iterations. This provides a **stable measure of typical performance**.  
- **Why multiple iterations?**  
  - Single-run timing can be inconsistent due to factors such as CPU scheduling, memory allocation, or caching.  
  - Repeating the benchmark multiple times and averaging reduces variability and gives **more reliable performance results**, similar to Java’s JMH benchmarking approach.  
**Interpretation:**  
- The average execution time reflects how efficient the function is under normal conditions.  
- Initial iterations may take longer due to **initialization overhead**, which is common in Node.js performance tests.  

### Benchmark summary on x86_64
To compare the benchmark results, the following results were collected by running the same benchmark on a `x86 - c4-standard-4` (4 vCPUs, 15 GB Memory) x86_64 VM in GCP, running SUSE:

| Iteration | 1     | 2     | 3     | 4     | 5     | 6     | 7     | 8     | 9     | 10    | Average |
|-----------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|---------|
| Time (ms) | 3.217 | 0.631 | 0.632 | 0.611 | 0.612 | 0.614 | 0.614 | 0.611 | 0.606 | 0.532 | 0.868   |

### Benchmark summary on Arm64
Results from the earlier run on the `c4a-standard-4` (4 vCPU, 16 GB memory) Arm64 VM in GCP (SUSE):

| Iteration | 1     | 2     | 3     | 4     | 5     | 6     | 7     | 8     | 9     | 10    | Average |
|-----------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|---------|
| Time (ms) | 2.286 | 0.749 | 1.145 | 0.674 | 0.671 | 0.671 | 0.672 | 0.667 | 0.667 | 0.673 | 0.888   |

### TypeScript performance benchmarking comparison on Arm64 and x86_64

When you compare the benchmarking results, you will notice that on the Google Axion C4A Arm-based instances:

- The average execution time on Arm64 (~0.888 ms) shows that CPU-bound TypeScript operations run efficiently on Arm-based VMs.
- Initial iterations may show slightly higher times due to runtime warm-up and optimization overhead, which is common across architectures.  
- Arm64 demonstrates stable iteration times after the first run, indicating consistent performance for repeated workloads.  
- Compared to typical x86_64 VMs, Arm64 performance is comparable for lightweight TypeScript computations, with potential advantages in power efficiency and cost for cloud deployments.
