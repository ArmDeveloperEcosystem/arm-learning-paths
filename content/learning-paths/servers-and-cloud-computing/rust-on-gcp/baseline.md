---
title: Rust Baseline Testing on Google Axion C4A Arm Virtual Machine
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Rust Baseline Testing on GCP SUSE VMs
This guide demonstrates how to perform baseline testing of Rust on GCP SUSE Arm64 VMs, verifying installation, build functionality, and compilation performance on the Arm-based Axion C4A platform.

### Verify Installation
Check the Rust version and toolchain setup:

```console
rustc --version
cargo --version
```

### Create a Sample Rust Program
Create and build a simple “Hello, World” application to ensure everything is functioning properly:

```console
mkdir rust-baseline
cd rust-baseline
cargo new hello
cd hello
cargo run
```
- **`mkdir rust-baseline`** – Creates a new directory named `rust-baseline`.  
- **`cd rust-baseline`** – Enters the `rust-baseline` directory.  
- **`cargo new hello`** – Creates a new Rust project named `hello` with default files (`main.rs`, `Cargo.toml`).  
- **`cd hello`** – Moves into the newly created `hello` project directory.  
- **`cargo run`** – Compiles and runs the Rust program, printing **“Hello, world!”**, confirming that Rust and Cargo are properly set up.

You should see an output similar to:
```output
   Compiling hello v0.1.0 (/home/gcpuser/rust-baseline/hello)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.19s
     Running `target/debug/hello`
Hello, world!
```

### Measure Compilation Speed
Use the time command to measure how long Rust takes to compile a small program:

```console
cargo clean
time cargo build
```
This gives a rough idea of compilation performance on the Arm64 CPU.

You should see an output similar to:
```output
Removed 21 files, 7.7MiB total
   Compiling hello v0.1.0 (/home/gcpuser/rust-baseline/hello)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.14s

real    0m0.186s
user    0m0.118s
sys     0m0.071s
```
This confirms that Rust is working properly on your Arm64 VM.
