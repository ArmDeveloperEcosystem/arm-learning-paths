---
title: Benchmark Rust performance using Criterion
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Benchmark Rust performance

This section demonstrates how to benchmark Rust performance using `cargo bench` and the Criterion library to measure code execution speed and performance consistency on aarch64 hardware.

### Create a benchmark project

Create a new Rust project specifically for benchmarking:

```console
cargo new rust-benchmark
cd rust-benchmark
```

### Configure Criterion as a dependency

Criterion is the recommended benchmarking crate for Rust. Edit the `Cargo.toml` file in your project root directory and replace the existing content with:

```toml
[dependencies]
criterion = "0.5"

[[bench]]
name = "my_benchmark"
harness = false
```

This configuration enables Criterion for high-precision benchmarking and disables the default test harness.

### Create the benchmark directory and file

Create the benchmark structure that Cargo expects:

```console
mkdir benches
```

Create a new benchmark file in the `benches/` directory:

```console
edit benches/my_benchmark.rs
```

Add the following benchmark code to measure Fibonacci number calculation performance:

```rust
use criterion::{black_box, Criterion, criterion_group, criterion_main};

// Example benchmark function
fn fibonacci(n: u64) -> u64 {
    match n {
        0 => 0,
        1 => 1,
        n => fibonacci(n - 1) + fibonacci(n - 2),
    }
}

fn benchmark_fibonacci(c: &mut Criterion) {
    c.bench_function("fibonacci 20", |b| b.iter(|| fibonacci(black_box(20))));
}

criterion_group!(benches, benchmark_fibonacci);
criterion_main!(benches);
```

This code implements a recursive Fibonacci function and measures how efficiently Rust computes the 20th Fibonacci number. The `black_box` function prevents the compiler from optimizing away the benchmark.

### Run the benchmark

Execute the benchmark using Cargo:

```console
cargo bench
```

Cargo compiles your code with optimizations enabled and runs the Criterion benchmarks, providing detailed performance metrics.

The output is similar to:

```output
Running benches/my_benchmark.rs (target/release/deps/my_benchmark-f40a307ef9cad515)
Gnuplot not found, using plotters backend
fibonacci 20            time:   [12.026 µs 12.028 µs 12.030 µs]
Found 1 outliers among 100 measurements (1.00%)
  1 (1.00%) low mild
```

### Benchmark Metrics Explanation

- **Average Time:** Mean execution time across benchmark runs.  
- **Outliers:** Represent runs significantly slower or faster than average.  
- **Plotting Backend:** Used `plotters` since Gnuplot was not found.  
- The results show **consistent performance** with only slight variation across 100 measurements.

### Understand the results

The benchmark output provides several key metrics:

- **Average time**: Mean execution time across benchmark runs
- **Outliers**: Runs significantly slower or faster than average  
- **Plotting backend**: Uses plotters since Gnuplot wasn't found

The results show consistent performance with only slight variation across 100 measurements.

### Performance summary

The following table shows results from running the benchmark on a `c4a-standard-4` (4 vCPU, 16 GB memory) aarch64 VM in GCP using SUSE:

| Benchmark     | Average Time (µs) | Min (µs) | Max (µs) | Outliers (%) | Remarks |
|---------------|------------------:|---------:|---------:|-------------:|---------|
| fibonacci 20  | 12.028           | 12.026   | 12.030   | 1.00%        | Stable performance with minimal variation |

The Fibonacci benchmark demonstrates consistent performance on the aarch64 platform. The average execution time of 12.028 µs indicates efficient CPU computation, while only 1% of measurements were outliers. This low variance confirms Rust's reliable execution speed and performance stability on aarch64 architecture.
