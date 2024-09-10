---
title: Porting Process
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Using SIMD.info to Find NEON Equivalents
Now that you have a clear view of the example, you can start the process of porting the code to NEON. This is where [SIMD.info](https://simd.info/) comes in. In SIMD programming, the primary concern is usually the calculations, as they constitute the core workload of the program. Ensuring that these calculations are correctly ported and optimized is crucial for maintaining performance and correctness.

For the operations in your SSE4.2 example, you have the following intrinsics:

- **_mm_cmpgt_ps** 
- **_mm_add_ps** 
- **_mm_mul_ps** 
- **_mm_sqrt_ps** 

To gain a deeper understanding of how these intrinsics work and to get detailed descriptions, you can use the search feature on SIMD.info. Simply enter the intrinsic's name into the search bar. You can either select from the suggested results or perform a direct search to find detailed information about each intrinsic. 

1. By searching [_mm_add_ps](https://staging.simd.info/c_intrinsic//var/www/html/simdai/data_test/Arithmetic/Vector%20Add/Vector%20Add%2032-bit%20floats/SSE4.2_c__mm_add_ps.yaml/) you get information about it's purpose, result-type, assembly instruction, prototype and an example about it. By clicking the **engine** option **"NEON"** you can find it's [equivalents](https://staging.simd.info/eq/var/www/html/simdai/data_test/Arithmetic/Vector%20Add/Vector%20Add%2032-bit%20floats/SSE4.2_c__mm_add_ps.yaml/NEON/) for this engine. The equivalents are: **vaddq_f32**, **vadd_f32**. Now you are trying to choose which one to use. [Intrinsic comparison](https://staging.simd.info/c-intrinsics-compare?compare=var/www/html/simdai/data_test/Arithmetic/Vector%20Add/Vector%20Add%2032-bit%20floats/NEON_c_vaddq_f32.yaml:var/www/html/simdai/data_test/Arithmetic/Vector%20Add/Vector%20Add%2032-bit%20floats/NEON_c_vadd_f32.yaml) will help you get through this. Based on the prototype provided, you should choose [**vaddq_f32**](https://staging.simd.info/c_intrinsic//var/www/html/simdai/data_test/Arithmetic/Vector%20Add/Vector%20Add%2032-bit%20floats/NEON_c_vaddq_f32.yaml/) because it works with 128-bit vectors which is the same as SSE4.2.

2. Moving to the next intrinsic, **_mm_mul_ps**, you will use the [intrinsics tree](https://staging.simd.info/tag-tree) on SIMD.info to find the equivalent. Start by expanding the **Arithmetic** folder and then navigate to the subfolder **Vector Multiply**. Since you are working with 32-bit floats, open the **Vector Multiply 32-bit floats** subfolder, where you will several options. The recommended choice is [**vmulq_f32**](https://staging.simd.info/c_intrinsic//var/www/html/simdai/data_test/Arithmetic/Vector%20Multiply/Vector%20Multiply%2032-bit%20floats/NEON_c_vmulq_f32.yaml/), following the same reasoning as before—it operates on 128-bit vectors, just like in SSE4.2.

3. For the third intrinsic, **_mm_sqrt_ps**, the easiest way to find the corresponding NEON intrinsic is by typing **"Square Root"** into the search bar on SIMD.info. From the [search results](https://staging.simd.info/search?search=square+root&simd_engines=1&simd_engines=2&simd_engines=3&simd_engines=4&simd_engines=5), look for the float-specific version and select [**vsqrtq_f32**](https://staging.simd.info/c_intrinsic//var/www/html/simdai/data_test/Math%20Functions/Vector%20Square%20Root/NEON_c_vsqrtq_f32.yaml/), which, like the others, works with 128-bit vectors. In the equivalents section regarding SSE4.2, you can clearly see that **_mm_sqrt_ps** has its place as a direct match for this operation.

4. For the last intrinsic, **_mm_cmpgt_ps**, follow a similar approach as before. Using the intrinsics tree on SIMD.info, start by expanding the **Comparison** folder. Navigate to the subfolder **Vector Compare Greater Than**, and since you are working with 32-bit floats, proceed to **Vector Compare Greater Than 32-bit floats**. The recommended choice is [**vcgtq_f32**](https://staging.simd.info/c_intrinsic//var/www/html/simdai/data_test/Comparison/Vector%20Compare%20Greater%20Than/NEON_c_vcgtq_f32.yaml/), as it operates on 128-bit vectors, just like in SSE4.2.

Now that you have found the NEON equivalents for each SSE4.2 intrinsic, you're ready to begin porting the code. Understanding these equivalents is key to ensuring that the performance and correctness of the calculations remain intact as you switch between SIMD engines.

## Step-by-Step Porting
1. The first step is to change the loading process to follow NEON's method for initializing vectors. Unlike SSE4.2, where we use intrinsics like _mm_set_ps, in NEON, we can directly define the vector using curly braces {}. This is simpler and aligns with how NEON works with floating-point vectors.
2. Next, you will replace the SSE4.2 intrinsics with the NEON equivalents we identified earlier. The key is to ensure that the operations perform the same tasks, such as comparison, addition, multiplication, and square root calculations.
3. Finally, modify the storing process to match NEON’s way of moving data from vectors to memory. In NEON, you use functions like vst1q_f32 for storing 128-bit floating-point vectors and [**vst1q_u32**](https://staging.simd.info/c_intrinsic//var/www/html/simdai/data_test/Memory%20Operations/Vector%20Store/Vector%20Store%2032-bit%20unsigned%20integers/NEON_c_vst1q_u32.yaml/) for storing 128-bit integer vectors.