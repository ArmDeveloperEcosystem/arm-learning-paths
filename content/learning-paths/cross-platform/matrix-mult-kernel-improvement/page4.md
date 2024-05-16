---
title: Deep-dive - Matrix Multiplication kernels
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

This section will cover the following:
1. A breakdown of the matrix multiplication reference implementation
2. An explination of the different variations of KleidiAI matrix multiplicaiton
3. A look into KleidiAI's matrix multiplication implementation in Arm Assembly

### Matrix Multiplication reference implementation

The actual matrix multiplication takes place in the function `ref_matmul_f32_qa8dx_qs4cx`.

{{% notice Naming - ref_matmul_f32_qa8dx_qs4cx %}}
    The function's name describes what it does and its input/output formats. It is the reference (ref) matrix multiplication (matmul), outputing in floating-point 32-bit format (f32), taking in two matricies of the following formats:
    * `qa8dx` = quantized (q), asymmetric (a), 8-bit integers (8) per dimension, ie per row (dx).
    * `qs4cx` = quantized (q), symmetric (s), 4-bit integers (8) per channel (cx).
{{% /notice %}}


The function takes in the following parameters:
* Input matrix dimensions (`m`, `n`, `k`).
* Input matricies, quantized and packed (`lhs_ref_matx_qa8xd`, `rhs_native_mtx_qs4cx`)
* The scale factor for the RHS matrix (`rhs_scales_f32`). Recall that the LHS offsets are stored in the matrix itself.
* The pointer to the output matrix (`dst_ref_mtx_f32`).
* Upper and lower bounds on floating point numbers for easier processing (`FLT_MAX`).

Note that both input matricies use INT8 number format, with the RHS matrix including two INT4 numbers in each INT8 memory location. The matrix multiplication function will unpack these INT4 numbers during run-time for proper calculation. The output matrix will store numbers in their native format, up to FP32.

```C
    ref_matmul_f32_qa8dx_qs4cx(
        m, n, k, (const int8_t*)lhs_ref_mtx_qa8dx, (const uint8_t*)rhs_native_mtx_qs4cx, (const float*)rhs_scales_f32,
        (float*)dst_ref_mtx_f32, -FLT_MAX, FLT_MAX);
```


The implementation of the matrix multiplication is relatively straightforward to understand. First the function calculates how far to stride to move over each input matrix's rows:

```C
    const size_t lhs_stride = k * sizeof(int8_t) + sizeof(float) + sizeof(int32_t);
    const size_t rhs_stride = (k / 2) * sizeof(uint8_t);
```

Next the main loop begins, incrementing row and column indexes to obtain the correct pointers (`lhs_ptr` and `rhs_ptr`) to access individual rows in each input matrix:

```C
    for (size_t row_idx = 0; row_idx < m; ++row_idx) {

        const int8_t* lhs_ptr_start = lhs_qa8dx + row_idx * lhs_stride;
        for (size_t col_idx = 0; col_idx < n; ++col_idx) {

            // Main f32 accumulator
            int32_t iacc = 0;

            const int8_t* lhs_ptr = lhs_ptr_start;
            const uint8_t* rhs_ptr = rhs_qs4cx + col_idx * rhs_stride;
```

The row-specific LHS quantization offsets are obtained. Recall the RHS quantization scale is already sent into the matrix multiplication kernel as a parameter.

```C
    const float lhs_scale = *(const float*)lhs_ptr;
    lhs_ptr += sizeof(float);

    const int32_t lhs_offset = *(const int32_t*)lhs_ptr;
    lhs_ptr += sizeof(int32_t);
```


Next is the loop where matrix multiplication actually takes place. The loop iterates over the input matrcies' shared dimension `k`. It steps in increments of 2 (`b += 2`) as the LHS matrix needs to get two INT8 numbers to multiply against the two INT4 numbers from the RHS matrix's INT8 memory location. The numbers from each matrix are multiplied and added to the FP32 sized `iacc` variable. 

```C
    for (size_t b = 0; b < k; b += 2) {
        // Get the LHS values
        const int32_t lhs_v0 = (int32_t)lhs_ptr[0];
        const int32_t lhs_v1 = (int32_t)lhs_ptr[1];

        // Get the RHS values
        const uint8_t rhs_byte = rhs_ptr[0];

        // Unpack the RHS values
        const int32_t rhs_v0 = (((int32_t)(rhs_byte & 0x0F)) - 8);
        const int32_t rhs_v1 = (((int32_t)(rhs_byte >> 4)) - 8);

        iacc += lhs_v0 * rhs_v0;
        iacc += lhs_v1 * rhs_v1;
```


{{% notice KleidiAI i8mm acceleration step %}}
    These dot product calculations, `iacc += lhs_v0 * rhs_v0;  iacc += lhs_v1 * rhs_v1;`, is the operation that the `i8mm` architecture feature substantially accelerates. These calculations are performed using `SMMLA` instructions that you will observe near the end of this walk-through.
{{% /notice %}}

The last step is to convert the result back into the native number format, before the KleidiAI quantizing/packing operations. This involves the offsets and scales from both matricies (`lhs_offset` / `rhs_scales_f32[col_idx]` and `rhs_scale` / `lhs_scale`) and clamping the output to ensure it fits in the FP32 range.

```C
        iacc += lhs_offset * rhs_v0;
        iacc += lhs_offset * rhs_v1;
        .
        .
        .
    }

    const float rhs_scale = rhs_scales_f32[col_idx];
    float main_acc = iacc * rhs_scale;

    main_acc = main_acc * lhs_scale;

    main_acc = std::max(main_acc, scalar_min);
    main_acc = std::min(main_acc, scalar_max);

    dst_f32[0] = main_acc;
    dst_f32 += 1;
```


The final result is `dst_ref_mtx_f32`, the output matrix in the native number format. This matrix is represented in 1D, and is the ultimate output of the KleidiAI micro-kernels.

The above code is functionally representative of KleidiAI's matrix multiplication micro-kernels, but there are two last questions to address:
* What Arm instructions does KleidiAI leverage to accelerate matrix multiplication?
* Why are there multiple matrix multiplication micro-kernels in KleidiAI?

## KleidiAI MatMul variations

Stepping outside of the example C++ file now, into the matrix multiplication micro-kernel directory. It is located in `/src/matmul/matmul_clip_f32_qa8dxP_qs4cxP` directory.

![KleidiAI matrix multiplication micro-kernels](KleidiAI-src-matmul.jpg "Figure 3. KleidiAI src/matmul directory")

As stated earlier in this tutorial, only one matrix multiply micro-kernel will be used during AI inference of a given AI workload. The varients perform the same operation in subtly different ways, each offering a unique speed-up across different AI workload types. Here is one micro-kernel's name explained:

`kai_matmul_clamp_f32_qai8dxp4x8_qsu4cxp4x8_8x4x32_neon_i8mm.c`
* `kai` = stands for KleidiAI
* `matmul` = stands for matrix multiplication
* `clamp_f32` = communicates the output numbers are floating-point 32-bit format, and clamped to ensure they stay in that range.
* `qai8dxp4x8` = represents the first input matrix details, LHS. Quantized (q) Asymmetric (a) Signed (i) 8-bit (8) Per-Dimension (dx) quantization parameters, pre-packed in memory (p), processing a 4x8 subsection of the LHS matrix at a time (4x8).
* `qsu4cxp4x8` = represents the second input matrix details, RHS. Quantized (q) Symmetric (s) Unsigned (u) 4-bit (4) Per-Channel (cx) quantization parameters, pre-packed in memory (p), processing a 4x8 subsection of the RHS matrix at a time (4x8).
* `8x4x32` = represents the output matrix dimensions (8x4) and the block size being processed at once (x32). The 'block size' indicates operations are batched to compute 32 elements at once, parallizing computation.
* `neon_i8mm` = indicates the Arm technology (NEON) and architecture feature (i8mm) being leveraged in this micro-kernel.

The key difference between the different KleidiAI matrix multiplication micro-kernel varients are in the in/out matrix dimensions and processing block size. Different ML workloads and models will perform better/worse across the KleidiAI matmul varients, and the correct micro-kernel should be selected to maximize performance. ==========????????? Do ML Frameworks make this decision automatically, or are we expecting users to specify this? ===========??????????????

{{% notice Matrix dimension clarification %}}
    KleidiAI processes the incoming matrcies into smaller chunks to perform more efficient matrix multiplication operations, represented by the `4x8` input matrix dimensions noted above. KleidiAI can handel a wide range of input matrix dimensions, set by the `m`, `n`, and `k` parameters at the start of the example C++ file's main function.

    The suggested restriction on `n` to be a multiple of 8 is because =========I don't know why, fill in answer when recieved on page 3========.

    The hard requirement on `k` to be a multiple of 64 is because =========I don't know why but almost certainly related to block size, fill in answer when recieved on page 3========.
{{% /notice %}}


## KleidiAI MatMul assembly instructions

Open the `kai_matmul_clamp_f32_qai8dxp4x8_qsu4cxp4x8_8x4x32_neon_i8mm.c` to see the hand-optimized Arm assembly code executing matrix multiplication with the *i8mm* architecture feature.

Zooming in on one *SMMLA* instruction:
```
    ".inst 0x4e91a68a  // smmla v10.4s, v20.16b, v17.16b\n"
```

Here is an analysis of this instruction:
* v10.4s: The destination register (v10), a vector of 4 signed 32-bit integers (4s). This is where the result of the matrix multiplication is stored.
* v20.16b: The first source register (v20), a vector of 16 signed 8-bit integers (16b).
* v17.16b: The second source register (v17), a vector of 16 signed 8-bit integers (16b).

The intrecices of how this *SMMLA* fits into the larger matrix multiplication micro-kernel is beyond the scope of this write-up. This one instruction is equivalent to performing an 8-way dot product. This instruction fits alongside many other *SMMLA* instructions and other organizing instructions to efficently compute the larger input matrix multiplication required.

You now have an understanding of how KleidiAI accelerates matrix multiplication, and ultimately how GenAI models can run efficiently on Arm CPUs from servers to smartphones.