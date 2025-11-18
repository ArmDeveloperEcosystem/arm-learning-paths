---
title: Test Rust baseline performance on Google Axion C4A Arm virtual machines
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Perform baseline testing

You can perform baseline testing of Rust on GCP SUSE aarch64 VMs to verify installation, build functionality, and compilation performance on the Arm-based Axion C4A platform.

### Create a sample Rust program

Create and build a simple "Hello, World" application to verify that Rust is working correctly:

```console
mkdir rust-baseline
cd rust-baseline
cargo new hello
cd hello
cargo run
```

This creates a new Rust project and runs it immediately. The `cargo new hello` command generates a default Rust project with the necessary files including `main.rs` and `Cargo.toml`.

The output is similar to:

```output
   Compiling hello v0.1.0 (/home/gcpuser/rust-baseline/hello)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.19s
     Running `target/debug/hello`
Hello, world!
```

This confirms that Rust and Cargo are properly configured on your aarch64 VM.

### Measure compilation performance

Use the `time` command to measure compilation performance on the Arm64 processor:

```console
cargo clean
time cargo build
```

The `cargo clean` command removes all build artifacts, ensuring you measure a complete compilation from scratch.

The output is similar to:

```output
Removed 21 files, 7.7MiB total
   Compiling hello v0.1.0 (/home/gcpuser/rust-baseline/hello)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.14s

real    0m0.186s
user    0m0.118s
sys     0m0.071s
```

The timing results show that Rust compilation performs well on the Arm64 architecture, with the "real" time indicating the total elapsed time for the build process.
