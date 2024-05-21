---
title: Quantizing and packing micro-kernels
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

This section will probe into the intricate details of what KlediAI is doing and how it is beneficial to AI performance optimization. 

## KleidiAI C++ example file
To unpack what specifically KlediAI does, and how it does it, you will review the example released alongside KleidiAI. Navigate to the KlediAI GitLab repository and view the example file [here](https://gitlab.arm.com/kleidi/kleidiai).

Note that this example is intended to illustrite KleidiAI microkernel performance. In practice you will not interact with KleidiAI's microkernels as your ML framework will leverage it automatically if supported. 


The example code is structured to take in two matricies and compare KleidiAI's micro-kernel results to a reference implementation. This reference code is functionally identical to KleidiAI's micro-kernels, and is present for two reasons:
1. To check for KleidiAI micro-kernel output validity as a sanity check, and
2. To explain how KleidiAI micro-kernels work. The implementation within KleidiAI's micro-kernels use hand-optimized C and Arm Assembly code, naturally being difficult to interpret.



### Build and run the KleidiAI example

Follow these steps to build and run the KleidiAI library and example script:

1. Create an Ubuntu 24 Arm Linux machine on an AWS EC2 instance. Use an M7g-medium, which uses the Graviton 3 SoC supporting the *i8mm* Arm architecture feature. The 1 CPU and 4 GB of RAM in the M7g-medium are sufficient for this basic example run.

2. Initialize your system by installing essential packages.
```bash
sudo apt update
sudo apt install cmake g++ make
```

3. Clone the KleidiAI directory to your server.
```bash
git clone _______________________
```
4. Build. The KleidiAI micro-kernels will compile into a library alongside an executable example. KleidiAI uses the CMake build system and is already confiured for building with a few CLI commands. After running these commands you should see a library file named `kleidiai.a` and the compiled example executable named `???????`.
```bash
cd ____________
mkdir build
cd build
cmake ..
make
```
5. Run the example with the below command. You should see a reference matrix multiplication output, then output from each KleidiAI matrix multipication micro-kernel, followed by confirmation that all output matricies are numerically equal (signalling success).
```bash
./????????????name_of_final_example_executable
```

Again, this manual interaction with KleidiAI is for example purposes. In real-world applications your supported ML Framework will handle interfacing with KleidiAI.

For the rest of this walk-through you will look over the reference kernel functions to understand what KleidiAI is doing before viewing under the hood snippets of hand-coded Arm instructions.


### Matrix Initalization
Open the example C++ file in your favorite text editor and locate the start of the `main` function. The example's first step is to define the dimensions of the input matricies, noted as the variables `m`, `n`, and `k`. The two matricies are then populated with random values at runtime.

```C
const size_t m = 17;
const size_t n = 32; 
const size_t k = 64; 
.
.
.
fill_uniform_random(m, k, (float*)lhs_native_mtx_f32, seed_lhs);
fill_uniform_random(n, k, (float*)rhs_native_mtx_f32, seed_rhs);
```

The two input matricies are labeled 'LHS' and 'RHS', standing for Left-Hand Side and Right-Hand Side respectively. This is a common way to label input matricies for neural network operations. In KleidiAI, LHS matricies represent the input activations from the previous network layer, and RHS matricies represent the connecting weights.

To perform a valid matrix multiplication, the number of row in LHS must match the number of columns in RHS. That is why the same variable `k` is used as a dimension for both matricies.

So in the example, the 17x64 LHS matrix and 32x64 RHS matrix are initalized with random 32-bit floating point numbers between [-1,1]. Note that at the time of matrix multiplication the RHS matrix is transposed to switch its row and column dimensions, ensuring valid matrix multiplication. 

### Initalization of variables
Both matricies need some variable sizes to be set and memory allocated:

```C
const size_t lhs_native_size_f32 = m * k * sizeof(float);
const size_t rhs_native_size_f32 = n * k * sizeof(float);
const size_t rhs_native_size_qs4cx = n * (k / 2) * sizeof(uint8_t);
const size_t rhs_scales_size_f32 = n * sizeof(float);

uint8_t* lhs_native_mtx_f32 = new uint8_t[lhs_native_size_f32];
uint8_t* rhs_native_mtx_f32 = new uint8_t[rhs_native_size_f32];
uint8_t* rhs_native_mtx_qs4cx = new uint8_t[rhs_native_size_qs4cx];
uint8_t* rhs_scales_f32 = new uint8_t[rhs_scales_size_f32];

quant_qs4cx_f32(n, k, (const float*)rhs_native_mtx_f32, (uint8_t*)rhs_native_mtx_qs4cx, (float*)rhs_scales_f32);
```


The `lhs_native_size_f32` allocates space in memory for the full LHS matrix to store 1088 FP32 numbers in a 1D space in memory (1088=17*32). Same goes for `rhs_native_size_f32`, for its nxk dimensions. The use of 'native' here is intentional, marking these sizes and matricies as the original input matricies without quantization.

The RHS matrix is quantized first. The number `rhs_native_size_qs4cx` is calculated to properly size the `rhs_native_mtx_qs4cx`, the 1D matrix storing INT4 numbers. 

{{% notice Naming - qs4cx %}}
You can tell the target is of the INT4 type based on the naming, `qs4cx`, which translates to quantized (q), symmetric (s), 4-bit integres (4) per channel (cx). 

Each 'channel' in this matrix refers to all the weights feeding into a given channel (ie. a given neuron). Because the weights feeding into different neurons may vary significantly, quantizing by channel offers improved percision and flexibility.
{{% /notice %}}


You may be asking: "Why does the `rhs_native_size_qs4cx` calculation use `sizeof(uint8_t)` as the data-type instead of `sizeof(uint4_t)`?" As mentioned in the overview section, this is where the packing concept comes in, fitting two INT4 numbers into a single INT8 memory location. This is done to fully leverage the i8mm Arm instructions that perform matrix multiplication across INT8 numbers. This packing of two INT4 numbers into one INT8 memory space explains why `rhs_native_size_qs4cx` is calculated by multiplying the space of an INT8 number and also dividing the matrix dimensions by 2.

### RHS Quantizing/Packing micro-kernel
The code snippets below are taken from the reference RHS quantizing/packing function, `quant_qs4cx_f32`. As mentioned previously, this reference function code is functionally representative of what KleidiAI's packing/quantizing micro-kernels are doing.

The function takes in the RHS matrix dimentions (`n` columns and `k` rows), the pointer to the native RHS matrix (`rhs_f32`), the pointer to where the quantized and packed RHS matrix will be stored (`rhs_qs4cx`), and the pointer to where the row scale factors will be stored (`rhs_scales_f32`).

```C
    static void quant_qs4cx_f32(size_t n, size_t k, const float* rhs_f32, uint8_t* rhs_qs4cx, float* rhs_scales_f32) {
```


Next the 'stride' is defined for the destination matrix, `dst_stride`. The stride variable is how a 2D matrix can be properly stored in 1D physical memory without overlapping. It stores the distance in memory that rows are seperated from one another. The stride is a function of the row dimension (`k`) taking into account number packing (`/2`) and the data type storage length (`sizeof(int8_t)`).

```C
    const size_t dst_stride = (k / 2) * sizeof(int8_t);
```

Then the micro-kernel iterates over each of the RHS native matrix's rows and finds the min and max value for each row in the RHS matrix, `rmin0` and `rmax0`. This step maximizes the quantization range for this matrix row when translating FP32 numbers to INT4. Uniquely quantizing each row minimize data loss and ultimately increases matrix multipilcation accuracy. A more lossy alternative would be to quantize the entire matrix at once with its global min/max, or defaulting min=-1 and max=1 for every matrix.

```C
    float max0 = -FLT_MAX;
    float min0 = FLT_MAX;

    // Find min/max for each channel
    for (size_t k_idx = 0; k_idx < k; ++k_idx) {
        const float src0_0 = src_ptr[k_idx];

        max0 = std::max(src0_0, max0);
        min0 = std::min(src0_0, min0);
    }

    // Maximum/minimum int8 values
    const float qmin = (float)INT4_MIN;
    const float qmax = (float)INT4_MAX;

    const float rmin0 = std::min(0.0f, min0);
    const float rmax0 = std::max(0.0f, max0);
```


Next the micro-kernel defines the quantizing 'scale' factor for each row, `scale0`. The scale factor provides the exact number used to quantize the FP32 numbers in this row to INT4. All row scale factors are stored as their reciprical (`recip_scale0`) in the `rhs_scales_f32` array to be used in de-scaling the output of matrix multiplication back into the native number data type.

```C
    const float scale0 = rmin0 == rmax0 ? 1.f : (qmax - qmin) / (rmax0 - rmin0);

    // Reciprocal to quantize
    const float recip_scale0 = scale0 ? 1.0f / scale0 : 0.0f;
```


Now the micro-kernel quantizes two numbers at a time and packs them into the destination matrix. Each number in the matrix is scaled via the calculated `scale0` factor, ensured to fit properly by clamping within the min/max range of INT4 numbers [-7,8] and packed into the a single INT8 memory space, `rhs_v0`.

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

After the RHS quantizing/packing micro-kernel is complete, the destination RHS matrix `rhs_native_mtx_qs4cx` is populated and ready to be used for matrix multiplication. In addition, the scale factors used to quantize the matrix are stored in `rhs_scales_f32` to de-quantize the matrix multiplication back into the native number format.


### LHS Quantizing/Packing micro-kernel

Next is an overview of the LHS quantizing/packing micro-kernel, which is very similar to the RHS version with less steps. 

Instead of quantizing to INT4, this LHS micro-kernel quantizes to INT8 format. As mentioned previously, this is done to maximize both compute performance and model accuracy. LHS input matricies commonly store model weights, wherease RHS input matricies commonly store input values. Model accuracy is more susceptible weight innaccuracies as opposed to input values, so KleidiAI keeps the LHS matrix quantized to INT8 and RHS quantized to INT4.

Like the RHS matrix, the code snippets below are taken from the reference LHS quantizing/packing function, `ref_quant_qa8dx_f32`. Again note that this function is representative of KleidiAI's' LHS packing/quantizing micro-kernel functionality.

{{% notice Naming - qa8dx %}}
You can tell the target is of the INT8 type based on the naming, `qa8dx`, which translates to quantized (q), asymmetric (a), 8-bit integres (8) per dimension (dx). 

Each 'dimension' in this matrix refers to a different feature in the input data (ie. in image processing, input dimensions being RGB - red, green, and blue). Because each input dimension can have a different distribution of values, quantizing by dimension offers improved percision and consistency.
{{% /notice %}}

The function takes in the LHS matrix dimentions (`m` columns and `k` rows), the pointer to the native LHS matrix (`lhs_f32`), and the pointer to where the quantized and packed LHS matrix will be stored (`lhs_qa8dx`).

```C
    static void ref_quant_qa8dx_f32(size_t m, size_t k, const float* lhs_f32, int8_t* lhs_qa8dx) {
```

The next few steps in this LHS micro-kernel are functionally equal to the RHS micro-kernel:
* The `stride` length is calculated.
* The `rmin0` and `rmax0` are calculated, this time for INT8 range.
* The `scale0` and its reciprical are calculated


Before the quantization takes place, the LHS matrix calculates where the appropriate zero point should be to handle a wider range of input values not centred around zero with more flexibility. This is refered to as 'asymmetric' quantization, allowing for different scale and zero points for each matrix row.

```C
    const float zero_point_from_min_error0 = qmin + descaled_min0;
    const float zero_point_from_max_error0 = qmax + descaled_max0;

    float zero_point0 =
        zero_point_from_min_error0 + zero_point_from_max_error0 > 0 ? qmin - descaled_min0 : qmax - descaled_max0;

    zero_point0 = std::max(zero_point0, qmin);
    zero_point0 = std::min(zero_point0, qmax);

    // Round to nearest integer
    const int32_t nudged_zero_point0 = lrintf(zero_point0);

    int8_t* dst_ptr = (int8_t*)lhs_qa8dx + row_idx * dst_stride;
```


Both the scale and new zero point numbers, both refered to as the 'LHS offset' are stored at the beginning of each row.

```C
        *((float*)(dst_ptr)) = recip_scale0;
        dst_ptr += sizeof(float);
        *((int32_t*)(dst_ptr)) = -nudged_zero_point0;
        dst_ptr += sizeof(int32_t);
```

Lastely the numbers are quantized and packed into memory. Note that during the packing step, only one INT8 number is placed into the `int8_t` memory location, as opposed to the RHS micro-kernel that packed two INT4 numbers into the same memory length.

```C
    dst_ptr[0] = (int8_t)v0_s32;
    dst_ptr += sizeof(int8_t);
```

### Next - Matrix Multiplication
After running the LHS and RHS quantizing/packing micro-kernels, the last step for KleidiAI is to perform the matrix multiplication operations. The next section details the different matrix multiplication micro-kernels and how they work.
