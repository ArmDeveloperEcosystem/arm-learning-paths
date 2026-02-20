---
title: An LTO Primer
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## A Brief Introduction to Link-Time Optimization

### Optimizations and Their Scope of Operation
Compiler optimizations can be categorized by the scope of code they are able to analyze and transform.

Some optimizations operate entirely within the scope of a single function. For example, dead code elimination removes variables or instructions that are unused within a function body, without requiring knowledge of how the rest of the program behaves.

Other optimizations require visibility beyond a single function. For instance, if a function is consistently called with a constant value for one of its parameters, the compiler can apply interprocedural constant propagation. Because such optimizations depend on assumptions about how code is used elsewhere, the compiler must apply them conservatively to avoid breaking correctness.

Functions that aren't visible outside the translation unit where they're defined (for example, those declared `static`) give the compiler enough information to make optimization decisions at compile time. Functions that are exported from a shared library may be called from unknown code, making it unsafe for the compiler to apply many interprocedural optimizations during compilation.

Between these two extremes are functions that are used across multiple translation units within a program, but whose complete usage becomes known only when the final executable is produced. These cases are where link-time optimization (LTO) is most effective, as it allows the compiler to analyze the whole program as a single unit and apply optimizations that would otherwise be unavailable.

### Link-Time Optimization and Intermediate Code Representation

Under normal compilation, once a translation unit has been processed, GCC emits an object file (.o). This object file contains machine code for the translation unit, along with relocation information, symbol metadata, and data required for linking. At this stage, the compiler has already committed to specific instruction sequences and discarded most of its internal analysis state.

By committing early to machine code, the compiler significantly limits its ability to perform optimizations that depend on cross-file visibility when the linker combines object files into a final executable.

When link-time optimization (LTO) is enabled, GCC changes this behavior. Instead of discarding its internal representation after compilation, GCC preserves an intermediate representation of the program. Specifically, GCC serializes its GIMPLE intermediate representation—a language-independent tree-based representation used internally by GCC—into a bytecode format and embeds it into special sections of the object file.

At link time, the compiler is invoked again, this time acting as an LTO-aware front end that reads the GIMPLE bytecode from all participating object files. With visibility into the entire program, GCC can perform whole-program optimizations, such as aggressive function inlining and interprocedural constant propagation, before generating the final machine code.

## What you've accomplished and what's next

You now understand how compiler optimizations differ in scope and why traditional compilation limits cross-file optimization opportunities. You also learned how LTO preserves intermediate representations at compile time to enable whole-program analysis at link time.

Next, you'll learn the practical steps to enable LTO in your builds.
