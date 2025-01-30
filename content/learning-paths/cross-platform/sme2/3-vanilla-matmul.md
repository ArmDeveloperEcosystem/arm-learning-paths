---
title: Vanilla matrix multiplication
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this chapter, you will write a by-the-book matrix multiplication in C.

## Vanilla matrix multiplication

### Algorithm description

The vanilla matrix multiplication operation takes two input matrices, A [Al
rows x Ac columns] and B [Bl rows x Bc columns], to produce an output matrix C
[Cl rows x Cc columns]. The operation consists of iterating on each row of A
and each column of B, multiplying each element of the A row with its corresponding
element in the B column then summing all these products, as depicted in figure 2 below.

![example image alt-text#center](matmul.png "Figure 2. By the book matrix multiplication")

This implies that the A, B and C matrices have some constraints on their
dimensions:

- A's number of columns needs to match B's number of lines: Ac == Bl
- C will have dimensions Cl == Al and Cc == Bc

You can learn more about matrix multiplication, including its history,
properties and use, with this [wikipedia
article](https://en.wikipedia.org/wiki/Matrix_multiplication)

In this learning path, we will use the following variable names:

- ``matLeft`` corresponds to the left hand side argument of the matrix
  multiplication,
- ``matRight``corresponds to the right-hand side of the matrix multiplication,
- ``M`` is ``matleft`` number of rows,
- ``K`` is ``matleft`` number of columns (and ``matRight`` number of rows),
- ``N`` is ``matRight`` number of columns,
- ``matResult``corresponds to the result of the matrix multiplication, with
  ``M`` rows and ``N`` columns.

### C implementation

A literal implementation of the textbook matrix multiplication algorithm, as
described above, can be found in file ``matmul_vanilla.c``:

```C
void matmul(uint64_t M, uint64_t K, uint64_t N,
            const float *restrict matLeft, const float *restrict matRight,
            float *restrict matResult) {
    for (uint64_t m = 0; m < M; m++) {
        for (uint64_t n = 0; n < N; n++) {

            float acc = 0.0;

            for (uint64_t k = 0; k < K; k++)
                acc += matLeft[m * K + k] * matRight[k * N + n];

            matResult[m * N + n] = acc;
        }
    }
}
```

In this learning path, the matrices are laid out in memory as contiguous
sequences of elements, in [row major
order](https://en.wikipedia.org/wiki/Row-_and_column-major_order). The
``matmul`` function performs the algorithm that was described above. The
pointers to ``matLeft``, ``matRight`` and ``matResult`` have been annotated as
``restrict``, which informs the compiler that the memory areas designated by
those pointers do not alias (i.e. they do not overlap in any way), so the
compiler does not need to insert extra instructions to deal with those cases.
The pointers to ``matLeft`` and ``matRight`` are marked as ``const`` because
none of these 2 matrices are modified by ``matmul``.

You now have a reference matrix multiplication function. It will be used later
on in this learning path to ensure that the assembly version and the intrinsics
version of the multiplication algorithm do not contain errors.