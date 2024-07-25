---
title: Background
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Rust: a safe programming language

Even if you have never programmed or looked at Rust code before, you will probably have heard of some of its characteristics:

* A modern, strong-typed language.
* Memory-safe by design: bugs like a buffer overflow are rare in Rust.
* The compiler is very strict and doesn't permit easy mistakes as C does, therefore there can be is a steep learning curve to learn Rust.
* It is quickly evolving to many architectures and operating systems.

This Learning Path is not about learning how to write Rust. There are plenty of resources for this online. You will however learn the basics of how to program SIMD code on Arm using Rust.

## SIMD on Rust

In contrast with C and C++, SIMD support for a particular architecture is not added in a monolithic way. SIMD support for those languages is typically added by the compiler teams of each vendor, so for example, Arm compiler teams are responsible for adding support for Arm ISA intrinsics in a way that each company sees fit.

Rust is somewhat different. While vendors are still heavily involved in providing the support for SIMD intrinsics in the compiler, there are also multiple other proposed schemes to provide SIMD abstraction or even alternatives to the official SIMD intrinsics.

Currently there are two alternative programming interfaces:
1. An interface under `std::arch` that follows the C intrinsics as much as possible.
2. An interface that tries to provide a portable abstraction to SIMD programming so that code can be recompiled across different architectures with more or less the same results. While there are similar libraries for C and C++, this is a different scenario as the intent is to get merged as an official extension to the Rust standard library under `std::simd`.

In this Learning Path, you will discover how to use either of those extensions to write code that uses ASIMD/Neon on an Arm CPU.

Before you begin with examples, ensure that you have a working Rust environment. Depending on your environment, it may be as simple as running:

```bash
sudo apt install rustc
```

You can check if you have a working `rustc` compiler installed by running:

```bash
$ rustc --version
rustc 1.63.0
```

Now that you have a working Rust compiler, you can continue to the examples. Note that the Rust code in this Learning Path is not idiomatic nor optimally written Rust. To do this you would have to use `cargo`, find the proper `crates` to do specific tasks - for example for 2D arrays - and this would increase the size of the scope of this Learning Path significantly.


