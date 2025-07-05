---
title: Going further
weight: 12

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you'll explore ways to optimize and extend the matrix multiplication algorithm beyond the current SME2 implementation. These improvements include generalization, loop unrolling, and strategic use of matrix properties.

## Generalize the algorithm for other data types

So far, this Learning Path has focused on multiplying floating-point matrices. In practice, matrix operations are also performed on various integer types.

The overall structure of the algorithm - preprocessing with tiling and outer product–based multiplication - remains the same across data types. You only need to adapt how the data is loaded, stored, and accumulated.

This pattern works well in languages that support [generic programming](https://en.wikipedia.org/wiki/Generic_programming), such as C++ with templates. Templates can also handle cases where accumulation uses a wider data type than the input matrices, which is a common requirement. SME2 supports this with widening multiply-accumulate instructions.

By expressing the algorithm generically, you let the compiler generate multiple variants while you focus on:

- Algorithm design
- Testing and verification
- SME2-specific optimization

## Unroll loops to compute multiple tiles

For clarity, the `matmul_intr_impl` function in this Learning Path processes one tile at a time. But SME2 supports multi-vector operations, and you can take advantage of them to improve performance.

For example, `preprocess_l_intr` uses:

```c
svld1_x2(...); // Load two vectors at once

---
title: Going further
weight: 12

### FIXED, DO NOT MODIFY
layout: learningpathall
---

---
title: Going further
weight: 12

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you'll explore ways to optimize and extend the matrix multiplication algorithm beyond the current SME2 implementation. These improvements include generalization, loop unrolling, and strategic use of matrix properties.

## Generalize the algorithm for other data types

So far, this Learning Path has focused on multiplying floating-point matrices. In practice, matrix operations are also performed on various integer types.

The overall structure of the algorithm - preprocessing with tiling and outer product–based multiplication - remains the same across data types. You only need to adapt how the data is loaded, stored, and accumulated.

This pattern works well in languages that support [generic programming](https://en.wikipedia.org/wiki/Generic_programming), such as C++ with templates. Templates can also handle cases where accumulation uses a wider data type than the input matrices, which is a common requirement. SME2 supports this with widening multiply-accumulate instructions.

By expressing the algorithm generically, you let the compiler generate multiple variants while you focus on:

- Algorithm design
- Testing and verification
- SME2-specific optimization

## Unroll loops to compute multiple tiles

For clarity, the `matmul_intr_impl` function in this Learning Path processes one tile at a time. But SME2 supports multi-vector operations, and you can take advantage of them to improve performance.

For example, `preprocess_l_intr` uses:

```c
svld1_x2(...); // Load two vectors at once
```
Loading two vectors at a time enables the simultaneous computing of more tiles,
and as the input matrices have been laid out in memory in a neat way, the
consecutive loading of the data is efficient. Implementing this approach can
make improvements to the ``macc`` to load ``ratio``.

In order to check your understanding of SME2, you can try to implement this
unrolling yourself in the intrinsic version (the asm version already has this
optimization). You can check your work by comparing your results to the expected
reference values.

## Apply strategies

One method for optimization is to use strategies that are flexible depending on
the matrices' dimensions. This is especially easy to set up when working in C or
C++, rather than directly in assembly language.

By playing with the mathematical properties of matrix multiplication and the
outer product, it is possible to minimize data movement as well as reduce the
overall number of operations to perform.

For example, it is common that one of the matrices is actually a vector, meaning
that it has a single row or column, and then it becomes advantageous to
transpose it. Can you see why?

The answer is that as the elements are stored contiguously in memory, an ``Nx1``
and ``1xN`` matrices have the exact same memory layout. The transposition
becomes a no-op, and the matrix elements stay in the same place in memory.

An even more *degenerated* case that is easy to manage is when one of the
matrices is essentially a scalar, which means that it is a matrix with one row
and one column.

Although our current code handles it correctly from a results point of view, a
different algorithm and use of instructions might be more efficient. Can you
think of another way?


In order to check your understanding of SME2, you can try to implement this
unrolling yourself in the intrinsic version (the asm version already has this
optimization). You can check your work by comparing your results to the expected
reference values.


