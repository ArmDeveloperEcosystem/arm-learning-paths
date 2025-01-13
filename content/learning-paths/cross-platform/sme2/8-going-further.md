---
title: Going further
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Generalize the algorithms

In this learning path, in order to show how to use SME2 for matrix
multiplication, we have only covered the case for floating point multiplication.
In practice, a library or framework that supports matrix multiplication should
also be implemented it for the double type (64-bit floating point number) as
well as all kinds of integers (8-bit, 16-bit, ...).

One can note that the algorithm structure for the matrix preprocessing as well
as the multiplication with the outer product do not change at all for other data
types --- they only need to be adapted to deal with other types. This is
perfectly suited for languages with [generic
programming](https://en.wikipedia.org/wiki/Generic_programming) like C++ with
templates. One could even make the template deal with the case where the value
accumulated during the product uses a larger type than the input matrices, as
SME2 has the instructions to deal efficiently with this common case.

This would enable the library writer to focus on the algorithm and the testing
--- and other optimizations (see below) --- while letting the compiler generate
the many variants.

## Unroll further

You might have noticed that ``matmul_intr_impl`` computes only one tile at a
time --- for the sake of simplicity. SME2 supports multi vector instructions ---
and some were actually used in ``preprocess_l_intr``, e.g. ``svld1_x2``. Loading
2 vectors at a time would allow computing more tiles at the same time, and as the
input matrices have been laid out in memory in a nice way, the consecutive
loading of the data is very efficient ; implementing this would improve yet
again the ``macc`` to load ``ratio``.

In order to check your understanding of SME2, you should try to implement this
unrolling yourself ! Fear not, your results will be compared to the expected
reference values, so you have an easy way to check your work.

## Apply strategies

An avenue for optimization is to use strategies depending on the matrices'
dimensions. This is especially easy to setup when working at the C or C++ level
rather than directly in assembly language. By playing with the mathematical
properties of matrix multiplication and the outer product, it is possible to
minimize data movement as well as the overall number of operations to perform.
For example, it is a very common case that one of the matrices is actually a
vector (it has a single row or column) ; it then becomes very advantageous to
transpose it... Can you see why ? (Answer: as the elements are stored
contiguously in memory, an ``Nx1`` and ``1xN`` matrices have the exact same
memory layout. The transposition becomes a no-op, the matrix elements will stay
at the same place in memory).

An even more *degenerated* case that is very easy to deal with is when one of
the matrices is essentially a scalar, i.e. a matrix with 1 row and 1 column.
Although our current code deals with it correctly from a result point of view, a
different algorithm / use of instructions would be significantly more efficient.
Can you think of an implementation ?
