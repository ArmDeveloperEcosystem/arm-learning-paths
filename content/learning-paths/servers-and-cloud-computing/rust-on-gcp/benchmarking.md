---
title: Rust Benchmarking
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Rust Benchmarking by cargo bench
This section demonstrates how to benchmark Rust performance using **official Rust benchmarking tools** — `cargo bench` and the **Criterion** library — to measure code execution speed, stability, and performance consistency on Arm64 hardware.

### Verify Rust and Cargo
Ensure that Rust and Cargo are properly installed before running benchmarks

```console
rustc --version
cargo --version
```

### Create a New Rust Project
Create a new Rust project for benchmarking:

```console
cargo new rust-benchmark
cd rust-benchmark
```
### Add Criterion Benchmarking Dependency
**Criterion** is the officially recommended benchmarking crate for Rust. Add it to your project by editing the `Cargo.toml` file located inside your project root directory (for example, rust-benchmark/Cargo.toml):

```toml
[dependencies]
criterion = "0.5"

[[bench]]
name = "my_benchmark"
harness = false
```
This enables Criterion for high-precision benchmarking.

### Create the Benchmark File
Create a new benchmark file inside the `benches/` directory:

```console
mkdir benches
vi benches/my_benchmark.rs
```
Benchmark files in this directory are automatically detected by Cargo.

**Add the Benchmark Code**

Paste the following benchmark code:

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
This code measures how efficiently Rust computes the 20th Fibonacci number.

### Run the Benchmark
Now run the benchmark using Cargo:

```console
cargo bench
```
Cargo compiles your code in optimized mode and runs the Criterion benchmarks, showing execution time, performance deviation, and stability metrics for your Rust functions.

You should see an output similar to:
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

### Benchmark summary on x86_64
To compare the benchmark results, the following results were collected by running the same benchmark on a `x86 - c4-standard-4` (4 vCPUs, 15 GB Memory) x86_64 VM in GCP, running SUSE:

| **Benchmark**     | **Average Time (µs)** | **Min (µs)** | **Max (µs)** | **Outliers (%)** | **Remarks**                     |
|--------------------|----------------------:|--------------:|--------------:|-----------------:|----------------------------------|
| **fibonacci 20**   | 19.152               | 19.100        | 19.205        | 6.00%            | Minor outliers, stable overall.  |

### Benchmark summary on Arm64
Results from the earlier run on the `c4a-standard-4` (4 vCPU, 16 GB memory) Arm64 VM in GCP (SUSE):

| **Benchmark**     | **Average Time (µs)** | **Min (µs)** | **Max (µs)** | **Outliers (%)** | **Remarks**                     |
|--------------------|----------------------:|--------------:|--------------:|-----------------:|----------------------------------|
| **fibonacci 20**   | 12.028               | 12.026        | 12.030        | 1.00%            | Very stable performance, minimal variation. |

### Rust benchmarking comparison on Arm64 and x86_64

- The **Fibonacci (n=20)** benchmark demonstrated **consistent performance** with minimal deviation.  
- **Average execution time** was around **12.028 µs**, indicating efficient CPU computation on **Arm64**.  
- Only **1% outliers** were detected, showing **high stability** and **repeatability** of results.  
- Overall, the test confirms **Rust’s reliable execution speed** and **low variance** on the Arm64 platform.
