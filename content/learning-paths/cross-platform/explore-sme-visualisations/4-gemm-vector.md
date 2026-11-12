---
title: Multiply matrices with vector outer products
description: See how Arm SME outer products build a matrix multiplication from partial results, and why transposing matrix A makes its memory access sequential.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Matrix multiplication recap

When you multiply input matrix A by input matrix B, you get a resulting matrix C. Matrix C is the sum of products of pairs of values from the rows of A and the columns of B.

![Scalar matrix multiplication: each element of output C sums products from one row of A and one column of B. Highlighted cells show two such calculations.#center](images/gemm_scalar.png "Scalar multiplication")


## Vectorize matrix multiplication

Calculating the successive terms of each element of matrix C isn't a good candidate for two dimensional vectorization. Instead, decompose the operation to calculate partial results for many rows and columns at a time.

![First outer-product contribution to C: the first column of A combines with the first row of B to update all 16 output cells at once.#center](images/gemm_vector_first_partial.png "Vector first partial result")

This is efficient because a Scalable Matrix Extension (SME) Matrix Outer Product instruction calculates all these values at the same time. It can accumulate the result by adding it to or subtracting it from the value that's already in the ZA tile.

After completing this step, move on to the second partial result.

![Second outer-product contribution to C: the second column of A combines with the second row of B and adds to each output cell.#center](images/gemm_vector_second_partial.png "Vector second partial result")

The pattern continues for the third partial result, using the third column of A and the third row of B.

![Third outer-product contribution to C: the third column of A combines with the third row of B, adding another term to each output cell.#center](images/gemm_vector_third_partial.png "Vector third partial result")

After you accumulate the fourth partial result, you've fully calculated the result values for 16 elements of the output matrix.

![Fourth outer-product contribution to C: the fourth column of A combines with the fourth row of B to complete all 16 output values.#center](images/gemm_vector_fourth_partial.png "Vector fourth partial result")

More results would have been calculated from the same number of instructions in the following circumstances:

- If smaller data types were used
- If the device used had a larger scalable vector length 

## Optimize memory access

The input matrix B is accessed sequentially, which is efficient. However, with input matrix A, you access columns of data whose elements are separated in memory by one row length. This is less efficient and can result in multiple cache misses, particularly if the row length is large. To avoid this, it's preferable to transform the input matrix A data so that it can be read sequentially. Do this by transposing strips of the matrix. Each strip contains the same number of rows as the ZA tiles of the element size that you're working with.


![Input matrix A is divided into colored horizontal strips. Transposing each strip places values from its columns together for sequential access.#center](images/transform_input_matrix.png "Transforming the input matrix A")


It's best if the input matrix data can naturally arise in this form. That way, there's no computational cost to transform the data. If that isn't possible, it might be desirable to manually transform the data.

Where the final strip doesn't contain the same number of rows as the others, pad the missing rows with `0`.


## Use multiple ZA tiles

For data element size larger than 8 bits, there are multiple ZA tiles available. Using all of them allows you to achieve the greatest data reuse and minimize memory system access.

In the diagram that follows, four tiles of results are processed at a time. Matrix B data is accessed sequentially from memory. Matrix A data is accessed as columns within horizontal strips, shown as a blue strip and a yellow strip. The height of each strip depends on the scalable vector length.

The ZA0 partial results are generated from an outer product of the blue and green data. The ZA1 partial results are generated from an outer product of the blue and red data. For the remaining tiles, you also need to load the yellow data. The ZA2 partial results are generated from an outer product of the yellow and green data. The ZA3 partial results are generated from an outer product of the yellow and red data.

As a result, the access pattern for matrix A is to alternate reading a column of blue data followed by a column of yellow data. Therefore, in addition to transposing strips of matrix A, an optimal arrangement involves interleaving the transposed rows from each strip.

![Two colored strips of matrix A feed four ZA tiles with rows of matrix B. The output layout alternates values from the two transposed A strips for sequential access.#center](images/transform_input_matrix_interleave.png "Transforming the input matrix A with interleave")

Other tiling arrangements are possible. For example, you can process four tiles arranged horizontally, instead of two rows of two. However, this arrangement is slightly less efficient. This is because it would require five vector loads from memory for every four tiles of partial results processed. The two-by-two arrangement requires only four vector loads from memory per four tiles.

## What you've learned and what's next

You've reviewed how matrix multiplication works, and how it can be decomposed into vector operations. You've seen how matrix A input data can be transposed so that it's accessed sequentially in memory. You've learned how to use multiple ZA tiles to increase data reuse and minimize memory system access.

Next, you'll view a visualization that prepares matrix A for multiplication.
