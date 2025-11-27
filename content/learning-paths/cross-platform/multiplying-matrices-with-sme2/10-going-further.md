---
title: Going further
weight: 12

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Beyond this implementation

There are many different ways that you can extend and optimize the matrix multiplication algorithm beyond the specific SME2 implementation that you've explored in this Learning Path. While the current approach is tuned for performance on a specific hardware target, further improvements can make your code more general, more efficient, and better suited to a wider range of applications.

Advanced optimization techniques are essential when adapting algorithms to real-world scenarios. These often include processing matrices of different shapes and sizes, handling mixed data types, or maximizing throughput for large batch operations. The ability to generalize and fine-tune your implementation opens the door to more scalable and reusable code that performs well across workloads.

Whether you're targeting different data types, improving parallelism, or adapting to unusual matrix shapes, these advanced techniques give you more control over both correctness and performance.

Some ideas of improvements that you might like to test out include:

- Generalization
- Loop unrolling
- The strategic use of matrix properties

## Generalize the algorithm for different data types

So far, you've focused on multiplying floating-point matrices. In practice, matrix operations often involve integer types as well.

The structure of the algorithm (the core logic - tiling, outer product, and accumulation) remains consistent across data types. It uses preprocessing with tiling and outer product–based multiplication. To adapt it for other data types, you only need to change how values are:

- Loaded from memory
- Accumulated (often with widening)
- Stored to the output

Languages that support [generic programming](https://en.wikipedia.org/wiki/Generic_programming),  such as C++ with templates, make this easier.

Templates allow you to:

- Swap data types flexibly
- Handle accumulation in a wider format when needed
- Reuse algorithm logic across multiple matrix types

By expressing the algorithm generically, you benefit from the compiler generating multiple optimized variants, allowing you the opportunity to focus on:

- Creating efficient algorithm design
- Testing and verification
- SME2-specific optimization

## Unroll loops to compute multiple tiles

For clarity, the `matmul_intr_impl` function in this Learning Path processes one tile at a time. However SME2 supports multi-vector operations that enable better performance through loop unrolling.

For example, the `preprocess_l_intr` function uses:

```c
svld1_x2(...); // Load two vectors at once
```
Loading two vectors at a time enables the simultaneous computing of more tiles.  Since the matrices are already laid out efficiently in memory, consecutive loading is fast. Implementing this approach can make improvements to the `macc` to load `ratio`.

In order to check your understanding of SME2, you can try to implement this unrolling yourself in the intrinsic version (the assembly version already has this optimization). You can check your work by comparing your results to the expected reference values.

## Optimize for special matrix shapes

One method for optimization is to use strategies that are flexible depending on the matrices' dimensions. This is especially easy to set up when working in C or C++, rather than directly in assembly language.

By playing with the mathematical properties of matrix multiplication and the outer product, it is possible to minimize data movement as well as reduce the overall number of operations to perform.

For example, it is common that one of the matrices is actually a vector, meaning that it has a single row or column, and then it becomes advantageous to transpose it. Can you see why?

The answer is that as the elements are stored contiguously in memory, an `Nx1`and `1xN` matrices have the exact same memory layout. The transposition becomes a no-op, and the matrix elements stay in the same place in memory.

An even more *degenerated* case that is easy to manage is when one of the matrices is essentially a scalar, which means that it is a matrix with one row and one column.

Although the current code used here handles it correctly from a results point of view, a different algorithm and use of instructions might be more efficient. Can you think of another way?

In order to check your understanding of SME2, you can try to implement this optimization for special cases yourself in the intrinsic version. You can check your work by comparing your results to the expected reference values.
