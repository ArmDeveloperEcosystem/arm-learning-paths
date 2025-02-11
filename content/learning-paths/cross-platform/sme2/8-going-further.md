---
title: Going further
weight: 10

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Generalize the algorithms

In this Learning Path, you focused on using SME2 for matrix
multiplication with floating point numbers. However in practice, any library or framework supporting matrix multiplication should
also handle various integer types.

You can see that the algorithm structure for matrix preprocessing as well
as multiplication with the outer product does not change at all for other data
types - they only need to be adapted. 

This is suitable for languages with [generic
programming](https://en.wikipedia.org/wiki/Generic_programming) like C++ with
templates. You can even make the template manage a case where the value
accumulated during the product uses a larger type than the input matrices. SME2 has the instructions to deal efficiently with this common case scenario.

This enables the library developer to focus on the algorithm, testing, and optimizations, while allowing the compiler to generate multiple variants.

## Unroll further

You might have noticed that ``matmul_intr_impl`` computes only one tile at a time, for the sake of simplicity. 

SME2 does support multi-vector instructions, and some were used in ``preprocess_l_intr``, for example, ``svld1_x2``. 

Loading two vectors at a time enables the simultaneous computing of more tiles, and as the input matrices have been laid out in memory in a neat way, the consecutive
loading of the data is efficient. Implementing this approach can make improvements to the ``macc`` to load ``ratio``.

In order to check your understanding of SME2, you can try to implement this unrolling yourself. You can check your work by comparing your results to the expected
reference values.

## Apply strategies

One method for optimization is to use strategies that are flexible depending on the matrices' dimensions. This is especially easy to set up when working in C or C++,
rather than directly in assembly language. 

By playing with the mathematical properties of matrix multiplication and the outer product, it is possible to minimize data movement as well as reduce the overall number of operations to perform.

For example, it is common that one of the matrices is actually a vector, meaning that it has a single row or column, and then it becomes advantageous to transpose it. Can you see why? 

The answer is that as the elements are stored contiguously in memory, an ``Nx1`` and ``1xN`` matrices have the exact same memory layout. The transposition becomes a no-op, and the matrix elements stay in the same place in memory.

An even more *degenerated* case that is easy to manage is when one of the matrices is essentially a scalar, which means that it is a matrix with one row and one column.

Although our current code handles it correctly from a results point of view, a different algorithm and use of instructions might be more efficient. Can you think of another way?
