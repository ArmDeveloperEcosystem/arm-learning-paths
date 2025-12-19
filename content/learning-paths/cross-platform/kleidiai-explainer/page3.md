---
title: Quantizing and packing micro-kernels
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## KleidiAI GitLab Repo
This section probes the intricate details of what KleidiAI is doing and how it is beneficial to AI performance optimization. 

Navigate to the [KleidiAI GitLab repository](https://gitlab.arm.com/kleidi/kleidiai) and view the [example file](https://gitlab.arm.com/kleidi/kleidiai/-/blob/main/examples/matmul_clamp_f32_qai8dxp_qsi4cxp/matmul_clamp_f32_qai8dxp_qsi4cxp.cpp?ref_type=heads) that you will be running. This example highlights the *i8mm* matrix multiplication micro-kernel, alongside the enabling packing/quantization micro-kernels.

{{% notice Note %}}This example illustrates KleidiAI microkernel performance. In practice, you will not interact with KleidiAI's microkernels as your ML framework will leverage it automatically, if supported.{{% /notice %}} 

The example code is structured to take in two matrices and compare KleidiAI's micro-kernel results to a reference implementation. 

This reference code is functionally-identical to KleidiAI's micro-kernels, and is present for two reasons:
1. To check for KleidiAI micro-kernel output validity as a sanity check.
2. To explain how KleidiAI micro-kernels work. The implementation within KleidiAI's micro-kernels use hand-optimized C and Arm Assembly code, which can be difficult to interpret.


## Build and Run the KleidiAI C++ example (i8mm micro-kernel)

Follow these steps to build and run the KleidiAI library and example script:

1. Create an Ubuntu 24.04 Arm Linux machine on an AWS EC2 instance. 
For more details view the Learning Path on [setting up AWS EC2 Graviton instances](/learning-paths/servers-and-cloud-computing/csp/aws/). Use an M7g-medium instance type, which uses the Graviton 3 SoC supporting the *i8mm* Arm architecture feature. The 1 CPU and 4 GB of RAM in the M7g-medium are sufficient for this basic example run.

2. Initialize your system by installing essential packages:
```bash
sudo apt update
sudo apt install cmake g++ make
```

3. Clone the KleidiAI directory to your server:
```bash
git clone https://git.gitlab.arm.com/kleidi/kleidiai.git
```

4. Build KleidiAI library with CMake. After running these commands you should see a library file named `libkleidiai.a`:
```bash
cd kleidiai
mkdir build
cd build
cmake ..
make
```

5. Build the example file with CMake. From the /kleidiai/build directory:
```bash
cd ../examples/matmul_clamp_f32_qai8dxp_qsi4cxp/
mkdir build
cd build
cmake ..
make
```
If you get an error that looks like `#error "Dotprod and I8mm extensions required to compile this example"` then you need to signal to KleidiAI that your machine supports the Dotprod and i8mm extensions. 

Do this by adding the following add_compile_options line to the `CMakeLists.txt` file in the `/examples/matmul_clamp_f32_qai8dxp_qsi4cxp/` directory:

```
cmake_minimum_required(VERSION 3.16)

set(CMAKE_CXX_STANDARD 17)
set(KLEIDIAI_PATH ../../)
set(MATMUL_PACK_PATH ${KLEIDIAI_PATH}/kai/ukernels/matmul/pack/)
set(MATMUL_PATH ${KLEIDIAI_PATH}/kai/ukernels/matmul/matmul_clamp_f32_qai8dxp_qsi4cxp/)

######## Add this command
add_compile_options(-march=armv8.6-a+dotprod+i8mm)
```

Then clear your build directory and build again.


6. Run the example. You will see each micro-kernel being tested, followed by confirmation that the reference implementation and KleidiAI's implementation are numerically equal - signaling success!
```bash
./matmul_clamp_f32_qai8dxp_qsi4cxp
```

```output
Testing matmul_clamp_f32_qai8dxp1x8_qsi4cxp4x8_1x4x32_neon_dotprod
TEST[0] = PASSED
Testing matmul_clamp_f32_qai8dxp1x8_qsi4cxp8x8_1x8x32_neon_dotprod
TEST[1] = PASSED
Testing matmul_clamp_f32_qai8dxp4x8_qsi4cxp4x8_4x4x32_neon_i8mm
TEST[2] = PASSED
Testing matmul_clamp_f32_qai8dxp4x8_qsi4cxp4x8_8x4x32_neon_i8mm
TEST[3] = PASSED
Testing matmul_clamp_f32_qai8dxp4x8_qsi4cxp8x8_4x8x32_neon_i8mm
TEST[4] = PASSED
Testing matmul_clamp
```

Again, this manual interaction with KleidiAI is for demonstration purposes. In real-world applications, your supported ML Framework handles interfacing with the KleidiAI library.

For the rest of this walk-through, you will look over the reference kernel functions to understand what KleidiAI is doing before viewing under-the-hood snippets of hand-coded Arm instructions.

## Understand KleidiAI's operation

Next you will look at the KleidiAI's reference implementation in the example file to understand with the micro-kernels do to accelerate AI inference. The reference implementation is easier to understand by looking at the code and is functionally equivalent to KleidiAI's actual micro-kernels. Links to KleidiAI's specific micro-kernel routines are also included.

You will now look at the three main routines:
1. Quantizing & Packing the RHS matrix.
2. Quantizing & Packing the LHS matrix.
3. Matrix multiplication.

### Quantizing & Packing the RHS matrix code (model weights)

Recall that the RHS matrix is populated by the AI model weights, which are dynamically quantized to INT4 format - if they are not in that format already. The RHS quantizing and packing function is defined in the example file as this:
```C
static void quant_qs4cx_f32(size_t n, size_t k, const float* rhs_f32, uint8_t* rhs_qs4cx, float* rhs_scales_f32)
```

The function takes in the following parameters:
* Input matrix dimensions (`n`, `k`). 
* Input matrix location (`rhs_f32`).
* Output matrix location (`rhs_qs4cx`). This is a 1-dimensional matrix that packs the INT4 numbers into 8-bit chunks of memory.
* Scale factors (`rhs_scales_f32`). This provides the exact number used to quantize the incoming model weight numbers (up to FP32 format) to INT4. Each channel is quantized independently and thus has a unique scale factor.

You can tell the target is of the INT4 type based on the naming, `qs4cx`, which translates to quantized (q), symmetric (s), 4-bit integers (4) per channel (cx). Each 'channel' in this matrix refers to all the weights feeding into a given channel (ie. a given neuron). Because the weights feeding into different neurons may vary significantly, quantizing by channel offers improved precision and flexibility.

After calculating variables like the destination matrix stride length and scale factors, the quantization and packing occurs:

```C
    uint8_t* dst_ptr = (uint8_t*)rhs_qs4cx + row_idx * dst_stride;

    // Quantize the channels
    for (size_t k_idx = 0; k_idx < k; k_idx += 2) {
        const float src0_0 = src_ptr[k_idx + 0];
        const float src0_1 = src_ptr[k_idx + 1];

        // Scale the values
        int32_t v0_s32 = (int32_t)(round(src0_0 * scale0));
        int32_t v1_s32 = (int32_t)(round(src0_1 * scale0));

        // Maximum/minimum int4 values
        v0_s32 = std::max(v0_s32, INT4_MIN);
        v0_s32 = std::min(v0_s32, INT4_MAX);
        v1_s32 = std::max(v1_s32, INT4_MIN);
        v1_s32 = std::min(v1_s32, INT4_MAX);

        int32_t v0_u8 = (uint8_t)(v0_s32 + 8);
        int32_t v1_u8 = (uint8_t)(v1_s32 + 8);

        const uint8_t rhs_v0 = (v1_u8 << 4) | v0_u8;

        dst_ptr[0] = rhs_v0;
        dst_ptr += sizeof(uint8_t);
    }
}
```

Next, the LHS matrix is quantized and packed into memory. 

### Quantizing & Packing LHS matrix code (inputs)

The LHS matrix will be populated by the inputs flowing through the model layers. They are also dynamically quantized, this time to the INT8 format. The LHS quantizing and packing function looks like:
```C
static void ref_quant_qa8dx_f32(size_t m, size_t k, const float* lhs_f32, int8_t* lhs_qa8dx) {
```

The function takes in the following parameters:
* Input matrix dimensions (`m`, `k`). Note that `k` is a shared dimension between RHS and LHS, ensuring matrix multiplication is possible.
* Input matrix location (`lhs_f32`).
* Output matrix location (`lhs_qa8xd`). This is a 1-dimensional matrix.

Scale factors are also required in the LHS quantization, but for computational efficiency are stored in the LHS output matrix directly. 

You can tell the target is of the INT8 type based on the naming, qa8dx, which translates to quantized (q), asymmetric (a), 8-bit integers (8) per dimension (dx). Each ‘dimension’ in this matrix refers to a different feature in the input data (ie. in image processing, input dimensions being RGB - red, green, and blue). Because each input dimension can have a different distribution of values, quantizing by dimension offers improved precision and consistency.

The next few steps in this LHS micro-kernel are functionally equal to the RHS micro-kernel: Calculating the stride length and scale factor. However, before the quantization takes place, the LHS matrix calculates where the appropriate zero point should be to handle a wider range of input values not centered around zero with more flexibility. This is referred to as ‘asymmetric’ quantization, allowing for different scale and zero points for each matrix row.

The zero point is calculated here:
```C
const float zero_point_from_min_error0 = qmin + descaled_min0;
const float zero_point_from_max_error0 = qmax + descaled_max0;

float zero_point0 =
    zero_point_from_min_error0 + zero_point_from_max_error0 > 0 ? qmin - descaled_min0 : qmax - descaled_max0;

zero_point0 = std::max(zero_point0, qmin);
zero_point0 = std::min(zero_point0, qmax);

// Round to nearest integer
const int32_t nudged_zero_point0 = lrintf(zero_point0);
```

After quantizing and packing the LHS matrix (similar to the RHS matrix process), the numbers are prepared for efficient matrix multiplication.


### Matrix Multiplication code

The LHS matrix will be populated by the inputs flowing through the model layers. They are also dynamically quantized, this time to the INT8 format. The LHS quantizing and packing function looks like:
```C
static void ref_quant_qa8dx_f32(size_t m, size_t k, const float* lhs_f32, int8_t* lhs_qa8dx) {
```

The function takes in the following parameters:
* Input matrix dimensions (`m`, `k`). Note that `k` is a shared dimension between RHS and LHS, ensuring matrix multiplication is possible.
* Input matrix location (`lhs_f32`).
* Output matrix location (`lhs_qa8xd`). This is a 1-dimensional matrix.



The reference matrix multiplication takes place in the function `ref_matmul_f32_qa8dx_qs4cx`.
```C
    ref_matmul_f32_qa8dx_qs4cx(
        m, n, k, (const int8_t*)lhs_ref_mtx_qa8dx, (const uint8_t*)rhs_native_mtx_qs4cx, (const float*)rhs_scales_f32,
        (float*)dst_ref_mtx_f32, -FLT_MAX, FLT_MAX);
```

The function takes in the following parameters:
* Input matrix dimensions (`m`, `n`, `k`).
* Input matrices, quantized and packed (`lhs_ref_matx_qa8xd`, `rhs_native_mtx_qs4cx`)
* The scale factor for the RHS matrix (`rhs_scales_f32`). Recall that the LHS offsets are stored in the matrix itself.
* The pointer to the output matrix (`dst_ref_mtx_f32`).
* Upper and lower bounds on floating point numbers for easier processing (`-FLT_MAX`, `FLT_MAX`).

The function's name describes what it does and its input/output formats. It is the reference (ref) matrix multiplication (matmul), outputting in floating-point 32-bit format (f32), taking in two matrices of previously described formats.

The implementation of the matrix multiplication is relatively straightforward to understand. First the function calculates how far to stride to move over each input matrix's rows while iterating: 

```C
    const size_t lhs_stride = k * sizeof(int8_t) + sizeof(float) + sizeof(int32_t);
    const size_t rhs_stride = (k / 2) * sizeof(uint8_t);
```

Next the main loop begins, incrementing row and column indexes to obtain the correct pointers (`lhs_ptr` and `rhs_ptr`) to access individual rows in each input matrix. This is the loop where matrix multiplication actually takes place. The loop iterates over the input matrices' shared dimension `k`. It steps in increments of 2 (`b += 2`) as the LHS matrix needs to get two INT8 numbers to multiply against the two INT4 numbers from the RHS matrix's INT8 memory location. The numbers from each matrix are multiplied and added to the FP32 sized `iacc` variable. 

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
These dot product calculations, `iacc += lhs_v0 * rhs_v0;  iacc += lhs_v1 * rhs_v1;`, is the operation that the *i8mm* architecture feature substantially accelerates. These calculations are performed using *SMMLA* instructions. You can view the hand-coded assembly implementation of this function in [this KleidiAI micro-kernel](https://gitlab.arm.com/kleidi/kleidiai/-/blob/main/kai/ukernels/matmul/matmul_clamp_f32_qai8dxp_qsi4cxp/kai_matmul_clamp_f32_qai8dxp4x8_qsi4cxp8x8_4x8x32_neon_i8mm.c?ref_type=heads).
{{% /notice %}}

The last step is to convert the result back into the native number format, using the LHS and RHS scale factors. The final result is `dst_ref_mtx_f32`, the output matrix in the native number format. This matrix is represented in 1D, and is the ultimate output of the KleidiAI micro-kernels.

#### KleidiAI micro-kernel variants explained

If you navigate to the [/kleidiai/kai/ukernels/matmul/matmul_clamp_f32_qai8dxp_qsi4cxp](https://gitlab.arm.com/kleidi/kleidiai/-/tree/main/kai/ukernels/matmul/matmul_clamp_f32_qai8dxp_qsi4cxp?ref_type=heads) directory where the KleidiAI INT8/INT4 micro-kernel implementation is located, you can see multiple variants of the same micro-kernel. The difference between them lies in the in/out matrix processing block size. Instead of performing matrix multiplication on the entire `m`x`k` and `n`x`k` matrices at once, KleidiAI provides matmul variants that perform smaller operations using hand-optimized assembly code. This leads to more efficient matrix multiplication. 

Different ML workloads and models have a varying performance across the KleidiAI matmul variants. Your ML framework selects the correct micro-kernel to maximize workload performance.

## KleidiAI enhances AI workload performance
You now have an understanding of how KleidiAI accelerates matrix multiplication, and ultimately how GenAI models can run efficiently on Arm CPUs from servers to smartphones.

Integrating KleidiAI to software frameworks is leading to significant performance boosts in real world generative AI workloads. For instance, Meta's Llama 3 and Microsoft's Phi-3 LLMs experience a 190 percent faster time-to-first token on the new [Arm Cortex-X925 CPU](https://newsroom.arm.com/blog/arm-kleidi). Additionally, KleidiAI improved the time-to-first token for Gemma 2B on the Google Pixel 8 Pro by 25 percent.


