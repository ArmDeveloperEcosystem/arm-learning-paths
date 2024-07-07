---
title: Intro to Rust
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Rust, a safe programming language

Even if you have never programmed or looked at Rust code, you will probably have heard of some of its advantages and disadvantages:

* modern, strong-typed language
* memory safe by design: it's extremely difficult to have an bug like a buffer overflow in Rust
* steep learning curve: because the compiler is very strict and doesn't let you make easy mistakes like in C
* fast-expanding to many architectures and operating systems

In this Learning Path you will not learn how to write Rust. There are plenty of such resources online. You will however learn the basics of how to program SIMD code on Arm using Rust.

## SIMD on Rust in general

In contrast with C and C++, SIMD support for a particular architecture is not added in a monolithic way. SIMD support for those languages is typically added by the compiler teams of each vendor, so for example, Arm compiler teams are responsible for adding support for Arm ISA intrinsics in a way that each company sees fit.

Rust is somewhat different. While vendors are still heavily involved in providing the support for SIMD intrinsics in the compiler, there are also multiple other proposed schemes to provide SIMD abstraction or even alternatives to the official SIMD intrinsics.

Currently there are 2 alternative programming interfaces:
* one under `std::arch` that follows the C intrinsics as much as possible
* one that tries to provide a portable abstraction to SIMD programming so that code can just be recompiled across different architectures with more or less the same results. While there are similar libraries for C and C++, this is different as the intent is to get merged as an official extension to the Rust standard library under `std::simd`.

In this Learning Path, you will find how to use either of those extensions to write code that uses ASIMD/Neon on an Arm CPU.

Before you start with actual examples, first make sure you have a working Rust environment. Depending on your environment, it may be as simple as

```bash
sudo apt install rustc
```

You can check if you have a working `rustc` compiler installed by running:

```bash
$ rustc --version
rustc 1.63.0
```

Now that you have a working Rust compiler, you may continue to the examples. Note that the Rust code in this Learning Path is not idiomatic nor optimally written Rust. To do that you would have to use `cargo`, find the proper `crates` to do specific tasks, for example for 2D arrays, which would increase the size of this Learning Path significantly.
