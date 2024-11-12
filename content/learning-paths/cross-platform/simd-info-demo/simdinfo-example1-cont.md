---
title: Porting Process
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Using SIMD.info to find NEON Equivalents
Now that you have a clear view of the example, you can start the process of porting the code to Arm **Neon/ASIMD**.

This is where [SIMD.info](https://simd.info/) comes in.

In SIMD programming, the primary concern is the integrity and accuracy of the calculations. Ensuring that these calculations are done correctly is crucial. Performance almost always comes second.

For the operations in your **SSE4.2** example, you have the following intrinsics:

- **`_mm_cmpgt_ps`**
- **`_mm_add_ps`**
- **`_mm_mul_ps`**
- **`_mm_sqrt_ps`**

To gain a deeper understanding of how these intrinsics work and to get detailed descriptions, you can use the search feature on **SIMD.info**. Simply enter the intrinsic's name into the search bar. You can either select from the suggested results or perform a direct search to find detailed information about each intrinsic.

1. By searching [**`_mm_add_ps`**](https://simd.info/c_intrinsic/_mm_add_ps/) you get information about it's purpose, result-type, assembly instruction, prototype and an example about it. By clicking the **engine** option **"NEON"** you can find it's [equivalents](https://simd.info/eq/_mm_add_ps/NEON/) for this engine. The equivalents are: **`vaddq_f32`**, **`vadd_f32`**. [Intrinsics comparison](https://simd.info/c-intrinsics-compare?compare=vaddq_f32:vadd_f32) will help you find the right one. Based on the prototype provided, you would choose [**`vaddq_f32`**](https://simd.info/c_intrinsic/vaddq_f32/) because it works with 128-bit vectors which is the same as **SSE4.2**.

2. Moving to the next intrinsic, **`_mm_mul_ps`**, you will use the [Intrinsics Tree](https://simd.info/tag-tree) on **SIMD.info** to find the equivalent. Start by expanding the **Arithmetic** branch and then navigate to the branch **Vector Multiply**. Since you are working with 32-bit floats, open the **Vector Multiply 32-bit floats** branch, where you will find several options. The recommended choice is [**`vmulq_f32`**](https://simd.info/c_intrinsic/vmulq_f32/), following the same reasoning as before—it operates on 128-bit vectors.

3. For the third intrinsic, **`_mm_sqrt_ps`**, the easiest way to find the corresponding **NEON** intrinsic is by typing **"Square Root"** into the search bar on SIMD.info. From the [search results](https://simd.info/search?search=Square+Root&simd_engines=1&simd_engines=2&simd_engines=3&simd_engines=4&simd_engines=5), look for the float-specific version and select [**`vsqrtq_f32`**](https://simd.info/c_intrinsic/vsqrtq_f32/), which, like the others, works with 128-bit vectors. In the equivalents section regarding **SSE4.2**, you can clearly see that **`_mm_sqrt_ps`** has its place as a direct match for this operation.

4. For the last intrinsic, **`_mm_cmpgt_ps`**, follow a similar approach as before. Inside the intrinsics tree, start by expanding the **Comparison** folder. Navigate to the subfolder **Vector Compare Greater Than**, and since you are working with 32-bit floats, proceed to **Vector Compare Greater Than 32-bit floats**. The recommended choice is again the 128-bit variant [**`vcgtq_f32`**](https://simd.info/c_intrinsic/vcgtq_f32/).

Now that you have found the **NEON** equivalents for each **SSE4.2** intrinsic, you're ready to begin porting the code. Understanding these equivalents is key to ensuring that the code produces the correct results in the calculations as you switch between SIMD engines.
