---
title: Test the Kleidicv and verify SME backend support
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run the Test

Once the build steps are complete, run the KleidiCV and OpenCV tests.

* Run the KleidiCV test

The KleidiCV API test verifies the public C++ API. You can run it as shown below, though the full test log is not included:

```output
./test/api/kleidicv-api-test
Vector length is set to 16 bytes.
Seed is set to 2542467924.
[==========] Running 3703 tests from 141 test suites.
[----------] Global test environment set-up.
[----------] 9 tests from SaturatingAddAbsWithThresholdTest/0, where TypeParam = short
[ RUN      ] SaturatingAddAbsWithThresholdTest/0.TestPositive
[       OK ] SaturatingAddAbsWithThresholdTest/0.TestPositive (0 ms)
[ RUN      ] SaturatingAddAbsWithThresholdTest/0.TestNegative
[       OK ] SaturatingAddAbsWithThresholdTest/0.TestNegative (0 ms)
[ RUN      ] SaturatingAddAbsWithThresholdTest/0.TestMin
[       OK ] SaturatingAddAbsWithThresholdTest/0.TestMin (0 ms)
[ RUN      ] SaturatingAddAbsWithThresholdTest/0.TestZero
[       OK ] SaturatingAddAbsWithThresholdTest/0.TestZero (0 ms)
[ RUN      ] SaturatingAddAbsWithThresholdTest/0.TestMax
[       OK ] SaturatingAddAbsWithThresholdTest/0.TestMax (0 ms)
[ RUN      ] SaturatingAddAbsWithThresholdTest/0.NullPointer
[       OK ] SaturatingAddAbsWithThresholdTest/0.NullPointer (0 ms)
[ RUN      ] SaturatingAddAbsWithThresholdTest/0.Misalignment
[       OK ] SaturatingAddAbsWithThresholdTest/0.Misalignment (0 ms)
[ RUN      ] SaturatingAddAbsWithThresholdTest/0.ZeroImageSize
[       OK ] SaturatingAddAbsWithThresholdTest/0.ZeroImageSize (0 ms)
[ RUN      ] SaturatingAddAbsWithThresholdTest/0.OversizeImage
[       OK ] SaturatingAddAbsWithThresholdTest/0.OversizeImage (0 ms)
[----------] 9 tests from SaturatingAddAbsWithThresholdTest/0 (0 ms total)

[----------] 4 tests from BitwiseAnd/0, where TypeParam = unsigned char
[ RUN      ] BitwiseAnd/0.API
[       OK ] BitwiseAnd/0.API (0 ms)
[ RUN      ] BitwiseAnd/0.Misalignment
[       OK ] BitwiseAnd/0.Misalignment (0 ms)
[ RUN      ] BitwiseAnd/0.ZeroImageSize
[       OK ] BitwiseAnd/0.ZeroImageSize (0 ms)
[ RUN      ] BitwiseAnd/0.OversizeImage
[       OK ] BitwiseAnd/0.OversizeImage (0 ms)
[----------] 4 tests from BitwiseAnd/0 (0 ms total)```
```
{{% notice Note %}}
Currently Apple xcode is built on clang17, and clang-1700.3.19.1 has an SME related code generation bug which causes float ResizeLinear API tests to fail.
{{% /notice %}}


* Run the OpenCV test

Upon completing the build steps for OpenCV with KleidiCV, the test binaries will be located in the "build-opencv-kleidicv-sme/bin/" directory. For example, `opencv_perf_imgproc` serves as OpenCV’s performance benchmark suite for the image processing (imgproc) module, evaluating both execution speed and throughput.

Testing can be customized by selecting specific test filters and parameters using the "`--gtest_filter`" and "`--gtest_param_filter`" options, respectively. For instance, to run the Gaussian blur 5×5 performance tests three times with the following parameter settings:
- Image size: 1920x1080 (Full HD)
- Image type: 8UC1 (8-bit unsigned, single channel, grayscale)
- Border type: BORDER_REPLICATE

Additional test cases are available in [benchmarks.txt](https://gitlab.arm.com/kleidi/kleidicv/-/blob/0.6.0/scripts/benchmark/benchmarks.txt?ref_type=tags).

The command for running the test is as follows:

```bash
./opencv_perf_imgproc \
  --gtest_filter='*gaussianBlur5x5/*' \
  --gtest_param_filter='(1920x1080, 8UC1, BORDER_REPLICATE)' \
  --gtest_repeat=3
```

The output will appear as follows:

```output
./opencv_perf_imgproc --gtest_filter='*gaussianBlur5x5/*' --gtest_param_filter='(1920x1080, 8UC1, BORDER_REPLICATE)' --gtest_repeat=3
[ERROR:0@0.001] global persistence.cpp:566 open Can't open file: 'imgproc.xml' in read mode
TEST: Skip tests with tags: 'mem_6gb', 'verylong'
CTEST_FULL_OUTPUT
OpenCV version: 4.12.0
OpenCV VCS version: 4.12.0-2-g2eea907534
Build type: Release
Compiler: /usr/bin/c++  (ver 17.0.0.17000013)
Algorithm hint: ALGO_HINT_ACCURATE
HAL: YES (carotene (ver 0.0.1) KleidiCV (ver 0.6.0))
Parallel framework: gcd (nthreads=12)
CPU features: NEON FP16 NEON_DOTPROD NEON_FP16 *NEON_BF16
OpenCL Platforms:
    Apple
        iGPU: Apple M4 Pro (OpenCL 1.2 )
Current OpenCL device:
    Type = iGPU
    Name = Apple M4 Pro
    Version = OpenCL 1.2
    Driver version = 1.2 1.0
    Address bits = 64
    Compute units = 16
    Max work group size = 256
    Local memory size = 32 KB
    Max memory allocation size = 3 GB
    Double support = No
    Half support = No
    Host unified memory = Yes
    Device extensions:
        cl_APPLE_SetMemObjectDestructor
        cl_APPLE_ContextLoggingFunctions
        cl_APPLE_clut
        cl_APPLE_query_kernel_names
        cl_APPLE_gl_sharing
        cl_khr_gl_event
        cl_khr_byte_addressable_store
        cl_khr_global_int32_base_atomics
        cl_khr_global_int32_extended_atomics
        cl_khr_local_int32_base_atomics
        cl_khr_local_int32_extended_atomics
        cl_khr_3d_image_writes
        cl_khr_image2d_from_buffer
        cl_khr_depth_images
    Has AMD Blas = No
    Has AMD Fft = No
    Preferred vector width char = 1
    Preferred vector width short = 1
    Preferred vector width int = 1
    Preferred vector width long = 1
    Preferred vector width float = 1
    Preferred vector width double = 1
    Preferred vector width half = 0

Repeating all tests (iteration 1) . . .

Note: Google Test filter = *gaussianBlur5x5/*
Note: Google Test parameter filter = (1920x1080, 8UC1, BORDER_REPLICATE)
[==========] Running 1 test from 1 test case.
[----------] Global test environment set-up.
[----------] 1 test from Size_MatType_BorderType_gaussianBlur5x5
[ RUN      ] Size_MatType_BorderType_gaussianBlur5x5.gaussianBlur5x5/80, where GetParam() = (1920x1080, 8UC1, BORDER_REPLICATE)
[ PERFSTAT ]    (samples=100   mean=0.18   median=0.18   min=0.16   stddev=0.02 (12.7%))
[       OK ] Size_MatType_BorderType_gaussianBlur5x5.gaussianBlur5x5/80 (22 ms)
[----------] 1 test from Size_MatType_BorderType_gaussianBlur5x5 (22 ms total)

[----------] Global test environment tear-down
[==========] 1 test from 1 test case ran. (22 ms total)
[  PASSED  ] 1 test.

Repeating all tests (iteration 2) . . .

Note: Google Test filter = *gaussianBlur5x5/*
Note: Google Test parameter filter = (1920x1080, 8UC1, BORDER_REPLICATE)
[==========] Running 1 test from 1 test case.
[----------] Global test environment set-up.
[----------] 1 test from Size_MatType_BorderType_gaussianBlur5x5
[ RUN      ] Size_MatType_BorderType_gaussianBlur5x5.gaussianBlur5x5/80, where GetParam() = (1920x1080, 8UC1, BORDER_REPLICATE)
[ PERFSTAT ]    (samples=100   mean=0.18   median=0.17   min=0.16   stddev=0.04 (23.7%))
[       OK ] Size_MatType_BorderType_gaussianBlur5x5.gaussianBlur5x5/80 (22 ms)
[----------] 1 test from Size_MatType_BorderType_gaussianBlur5x5 (22 ms total)

[----------] Global test environment tear-down
[==========] 1 test from 1 test case ran. (22 ms total)
[  PASSED  ] 1 test.

Repeating all tests (iteration 3) . . .

Note: Google Test filter = *gaussianBlur5x5/*
Note: Google Test parameter filter = (1920x1080, 8UC1, BORDER_REPLICATE)
[==========] Running 1 test from 1 test case.
[----------] Global test environment set-up.
[----------] 1 test from Size_MatType_BorderType_gaussianBlur5x5
[ RUN      ] Size_MatType_BorderType_gaussianBlur5x5.gaussianBlur5x5/80, where GetParam() = (1920x1080, 8UC1, BORDER_REPLICATE)
[ PERFSTAT ]    (samples=100   mean=0.19   median=0.17   min=0.15   stddev=0.07 (36.1%))
[       OK ] Size_MatType_BorderType_gaussianBlur5x5.gaussianBlur5x5/80 (23 ms)
[----------] 1 test from Size_MatType_BorderType_gaussianBlur5x5 (23 ms total)

[----------] Global test environment tear-down
[==========] 1 test from 1 test case ran. (23 ms total)
[  PASSED  ] 1 test.
```



## KleidiCV Multiversion Backend Support

The KleidiCV library detects the platform hardware at runtime and selects the backend implementation based on the following priority:

* SME2 backend implementation
* SME backend implementation
* SVE backend implementation
* NEON backend implementation

```C { line_numbers = "true" }
#define KLEIDICV_MULTIVERSION_C_API(api_name, neon_impl, sve2_impl, sme_impl, \
                                    sme2_impl)                                \
  static decltype(neon_impl) api_name##_resolver() {                          \
    [[maybe_unused]] KLEIDICV_TARGET_NAMESPACE::HwCaps hwcaps =               \
        KLEIDICV_TARGET_NAMESPACE::get_hwcaps();                              \
    KLEIDICV_SME2_RESOLVE(sme2_impl);                                         \
    KLEIDICV_SME_RESOLVE(sme_impl);                                           \
    KLEIDICV_SVE2_RESOLVE(sve2_impl);                                         \
    return neon_impl;                                                         \
  }                                                                           \
  extern "C" {                                                                \
  decltype(neon_impl) api_name = api_name##_resolver();                       \
  }
```
It verifies SME support using the query "hw.optional.arm.FEAT_SME" as follows:

```C { line_numbers = "true" }
#define KLEIDICV_SME_RESOLVE(sme_impl)                                       \
  if (!std::is_null_pointer_v<decltype(sme_impl)> &&                         \
      KLEIDICV_TARGET_NAMESPACE::query_sysctl("hw.optional.arm.FEAT_SME")) { \
    return sme_impl;                                                         \
  }
```
It verifies SME2 support using the query "hw.optional.arm.FEAT_SME2" as follows:

```C { line_numbers = "true" }
#define KLEIDICV_SME2_RESOLVE(sme2_impl)                                      \
  if (!std::is_null_pointer_v<decltype(sme2_impl)> &&                         \
      KLEIDICV_TARGET_NAMESPACE::query_sysctl("hw.optional.arm.FEAT_SME2")) { \
    return sme2_impl;                                                         \
  }
```


## Enable debug information for backend implementation at runtime

To incorporate dump information for multi-version backend support during runtime testing, please update "kleidicv/include/kleidicv/dispatch.h" as outlined below:


```C { line_numbers = "true" }
diff --git a/kleidicv/include/kleidicv/dispatch.h b/kleidicv/include/kleidicv/dispatch.h
index cc6ee01..44c98a5 100644
--- a/kleidicv/include/kleidicv/dispatch.h
+++ b/kleidicv/include/kleidicv/dispatch.h
@@ -1,10 +1,11 @@
-// SPDX-FileCopyrightText: 2023 - 2025 Arm Limited and/or its affiliates <open-source-office@arm.com>
+// SPDX-FileCopyrightText: 2024 - 2025 Arm Limited and/or its affiliates <open-source-office@arm.com>
 //
 // SPDX-License-Identifier: Apache-2.0

 #ifndef KLEIDICV_DISPATCH_H
 #define KLEIDICV_DISPATCH_H

+#include <stdio.h>
 #include "kleidicv/config.h"

 #if KLEIDICV_ENABLE_SME2 || KLEIDICV_ENABLE_SME || KLEIDICV_ENABLE_SVE2
@@ -33,6 +34,7 @@ static bool query_sysctl(const char* attribute_name) {
 #define KLEIDICV_SVE2_RESOLVE(sve2_impl)                                      \
   if (!std::is_null_pointer_v<decltype(sve2_impl)> &&                         \
       KLEIDICV_TARGET_NAMESPACE::query_sysctl("hw.optional.arm.FEAT_SVE2")) { \
+    printf("kleidicv API:: %s,SVE2 backend. \n", __func__);                    \
     return sve2_impl;                                                         \
   }
 #else
@@ -43,6 +45,7 @@ static bool query_sysctl(const char* attribute_name) {
 #define KLEIDICV_SME_RESOLVE(sme_impl)                                       \
   if (!std::is_null_pointer_v<decltype(sme_impl)> &&                         \
       KLEIDICV_TARGET_NAMESPACE::query_sysctl("hw.optional.arm.FEAT_SME")) { \
+    printf("kleidicv API:: %s,SME backend. \n", __func__);                  \
     return sme_impl;                                                         \
   }
 #else
@@ -53,6 +56,7 @@ static bool query_sysctl(const char* attribute_name) {
 #define KLEIDICV_SME2_RESOLVE(sme2_impl)                                      \
   if (!std::is_null_pointer_v<decltype(sme2_impl)> &&                         \
       KLEIDICV_TARGET_NAMESPACE::query_sysctl("hw.optional.arm.FEAT_SME2")) { \
+    printf("kleidicv API:: %s,SME2 backend. \n", __func__);                   \
     return sme2_impl;                                                         \
   }
 #else
@@ -67,6 +71,7 @@ static bool query_sysctl(const char* attribute_name) {
     KLEIDICV_SME2_RESOLVE(sme2_impl);                                         \
     KLEIDICV_SME_RESOLVE(sme_impl);                                           \
     KLEIDICV_SVE2_RESOLVE(sve2_impl);                                         \
+    printf("kleidicv API:: %s,NEON backend. \n", __func__);                   \
     return neon_impl;                                                         \
   }                                                                           \
   extern "C" {                                                                \
```

## Neon or SME backend data extraction on a MacBook

After making the change and rebuilding for testing, you can display the SME backend usage summary as follows:

```output
./kleidicv-benchmark
kleidicv API:: kleidicv_min_max_u8_resolver,SME backend.
kleidicv API:: kleidicv_min_max_s8_resolver,SME backend.
kleidicv API:: kleidicv_min_max_u16_resolver,SME backend.
kleidicv API:: kleidicv_min_max_s16_resolver,SME backend.
kleidicv API:: kleidicv_min_max_s32_resolver,SME backend.
kleidicv API:: kleidicv_min_max_f32_resolver,SME backend.
kleidicv API:: kleidicv_min_max_loc_u8_resolver,NEON backend.
kleidicv API:: kleidicv_saturating_absdiff_u8_resolver,NEON backend.
kleidicv API:: kleidicv_saturating_absdiff_s8_resolver,NEON backend.
kleidicv API:: kleidicv_saturating_absdiff_u16_resolver,NEON backend.
kleidicv API:: kleidicv_saturating_absdiff_s16_resolver,NEON backend.
kleidicv API:: kleidicv_saturating_absdiff_s32_resolver,NEON backend.
kleidicv API:: kleidicv_saturating_add_abs_with_threshold_s16_resolver,SME backend.
kleidicv API:: kleidicv_saturating_add_s8_resolver,NEON backend.
kleidicv API:: kleidicv_saturating_add_u8_resolver,NEON backend.
kleidicv API:: kleidicv_saturating_add_s16_resolver,NEON backend.
kleidicv API:: kleidicv_saturating_add_u16_resolver,NEON backend.
kleidicv API:: kleidicv_saturating_add_s32_resolver,NEON backend.
kleidicv API:: kleidicv_saturating_add_u32_resolver,NEON backend.
kleidicv API:: kleidicv_saturating_add_s64_resolver,NEON backend.
kleidicv API:: kleidicv_saturating_add_u64_resolver,NEON backend.
kleidicv API:: kleidicv_compare_equal_u8_resolver,NEON backend.
kleidicv API:: kleidicv_compare_greater_u8_resolver,NEON backend.
kleidicv API:: kleidicv_exp_f32_resolver,SME backend.
kleidicv API:: kleidicv_in_range_u8_resolver,NEON backend.
kleidicv API:: kleidicv_in_range_f32_resolver,NEON backend.
kleidicv API:: kleidicv_saturating_multiply_u8_resolver,NEON backend.
kleidicv API:: kleidicv_saturating_multiply_s8_resolver,NEON backend.
kleidicv API:: kleidicv_saturating_multiply_u16_resolver,NEON backend.
kleidicv API:: kleidicv_saturating_multiply_s16_resolver,NEON backend.
kleidicv API:: kleidicv_saturating_multiply_s32_resolver,NEON backend.
kleidicv API:: kleidicv_rotate_resolver,NEON backend.
kleidicv API:: kleidicv_scale_u8_resolver,NEON backend.
kleidicv API:: kleidicv_scale_f32_resolver,NEON backend.
kleidicv API:: kleidicv_saturating_sub_s8_resolver,NEON backend.
kleidicv API:: kleidicv_saturating_sub_u8_resolver,NEON backend.
kleidicv API:: kleidicv_saturating_sub_s16_resolver,NEON backend.
kleidicv API:: kleidicv_saturating_sub_u16_resolver,NEON backend.
kleidicv API:: kleidicv_saturating_sub_s32_resolver,NEON backend.
kleidicv API:: kleidicv_saturating_sub_u32_resolver,NEON backend.
kleidicv API:: kleidicv_saturating_sub_s64_resolver,NEON backend.
kleidicv API:: kleidicv_saturating_sub_u64_resolver,NEON backend.
kleidicv API:: kleidicv_sum_f32_resolver,SME backend.
kleidicv API:: kleidicv_threshold_binary_u8_resolver,SME backend.
kleidicv API:: kleidicv_transpose_resolver,NEON backend.
kleidicv API:: kleidicv_f32_to_s8_resolver,SME backend.
kleidicv API:: kleidicv_f32_to_u8_resolver,SME backend.
kleidicv API:: kleidicv_s8_to_f32_resolver,SME backend.
kleidicv API:: kleidicv_u8_to_f32_resolver,SME backend.
kleidicv API:: kleidicv_gray_to_rgb_u8_resolver,SME backend.
kleidicv API:: kleidicv_gray_to_rgba_u8_resolver,SME backend.
kleidicv API:: kleidicv_merge_resolver,NEON backend.
kleidicv API:: kleidicv_rgb_to_bgr_u8_resolver,SME backend.
kleidicv API:: kleidicv_rgba_to_bgra_u8_resolver,SME backend.
kleidicv API:: kleidicv_rgb_to_bgra_u8_resolver,SME backend.
kleidicv API:: kleidicv_rgb_to_rgba_u8_resolver,SME backend.
kleidicv API:: kleidicv_rgba_to_bgr_u8_resolver,SME backend.
kleidicv API:: kleidicv_rgba_to_rgb_u8_resolver,SME backend.
kleidicv API:: kleidicv_rgb_to_yuv420_p_stripe_u8_resolver,SME backend.
kleidicv API:: kleidicv_rgba_to_yuv420_p_stripe_u8_resolver,SME backend.
kleidicv API:: kleidicv_bgr_to_yuv420_p_stripe_u8_resolver,SME backend.
kleidicv API:: kleidicv_bgra_to_yuv420_p_stripe_u8_resolver,SME backend.
kleidicv API:: kleidicv_rgb_to_yuv420_sp_stripe_u8_resolver,SME backend.
kleidicv API:: kleidicv_rgba_to_yuv420_sp_stripe_u8_resolver,SME backend.
kleidicv API:: kleidicv_bgr_to_yuv420_sp_stripe_u8_resolver,SME backend.
kleidicv API:: kleidicv_bgra_to_yuv420_sp_stripe_u8_resolver,SME backend.
kleidicv API:: kleidicv_rgb_to_yuv_u8_resolver,SME backend.
kleidicv API:: kleidicv_bgr_to_yuv_u8_resolver,SME backend.
kleidicv API:: kleidicv_rgba_to_yuv_u8_resolver,SME backend.
kleidicv API:: kleidicv_bgra_to_yuv_u8_resolver,SME backend.
kleidicv API:: kleidicv_split_resolver,NEON backend.
kleidicv API:: kleidicv_yuv_p_to_rgb_stripe_u8_resolver,SME backend.
kleidicv API:: kleidicv_yuv_p_to_bgr_stripe_u8_resolver,SME backend.
kleidicv API:: kleidicv_yuv_p_to_rgba_stripe_u8_resolver,SME backend.
kleidicv API:: kleidicv_yuv_p_to_bgra_stripe_u8_resolver,SME backend.
kleidicv API:: kleidicv_yuv_sp_to_rgb_u8_resolver,SME backend.
kleidicv API:: kleidicv_yuv_sp_to_bgr_u8_resolver,SME backend.
kleidicv API:: kleidicv_yuv_sp_to_rgba_u8_resolver,SME backend.
kleidicv API:: kleidicv_yuv_sp_to_bgra_u8_resolver,SME backend.
kleidicv API:: kleidicv_yuv_to_rgb_u8_resolver,SME backend.
kleidicv API:: kleidicv_yuv_to_bgr_u8_resolver,SME backend.
kleidicv API:: kleidicv_yuv_to_bgra_u8_resolver,SME backend.
kleidicv API:: kleidicv_yuv_to_rgba_u8_resolver,SME backend.
kleidicv API:: kleidicv_blur_and_downsample_stripe_u8_resolver,SME backend.
kleidicv API:: kleidicv_gaussian_blur_fixed_stripe_u8_resolver,SME backend.
kleidicv API:: kleidicv_gaussian_blur_arbitrary_stripe_u8_resolver,NEON backend.
kleidicv API:: kleidicv_median_blur_sorting_network_stripe_s8_resolver,SME backend.
kleidicv API:: kleidicv_median_blur_sorting_network_stripe_u8_resolver,SME backend.
kleidicv API:: kleidicv_median_blur_sorting_network_stripe_u16_resolver,SME backend.
kleidicv API:: kleidicv_median_blur_sorting_network_stripe_s16_resolver,SME backend.
kleidicv API:: kleidicv_median_blur_sorting_network_stripe_u32_resolver,SME backend.
kleidicv API:: kleidicv_median_blur_sorting_network_stripe_s32_resolver,SME backend.
kleidicv API:: kleidicv_median_blur_sorting_network_stripe_f32_resolver,SME backend.
kleidicv API:: kleidicv_median_blur_small_hist_stripe_u8_resolver,NEON backend.
kleidicv API:: kleidicv_median_blur_large_hist_stripe_u8_resolver,NEON backend.
kleidicv API:: kleidicv_scharr_interleaved_stripe_s16_u8_resolver,SME backend.
kleidicv API:: kleidicv_separable_filter_2d_stripe_u8_resolver,SME backend.
kleidicv API:: kleidicv_separable_filter_2d_stripe_u16_resolver,SME backend.
kleidicv API:: kleidicv_separable_filter_2d_stripe_s16_resolver,SME backend.
kleidicv API:: kleidicv_sobel_3x3_horizontal_stripe_s16_u8_resolver,SME backend.
kleidicv API:: kleidicv_sobel_3x3_vertical_stripe_s16_u8_resolver,SME backend.
kleidicv API:: kleidicv_bitwise_and_resolver,NEON backend.
kleidicv API:: kleidicv_dilate_u8_resolver,SME backend.
kleidicv API:: kleidicv_erode_u8_resolver,SME backend.
kleidicv API:: kleidicv_resize_to_quarter_u8_resolver,SME backend.
kleidicv API:: kleidicv_resize_linear_stripe_u8_resolver,SME backend.
kleidicv API:: kleidicv_resize_linear_stripe_f32_resolver,SME backend.
kleidicv API:: kleidicv_remap_s16_u8_resolver,NEON backend.
kleidicv API:: kleidicv_remap_s16_u16_resolver,NEON backend.
kleidicv API:: kleidicv_remap_s16point5_u8_resolver,NEON backend.
kleidicv API:: kleidicv_remap_s16point5_u16_resolver,NEON backend.
kleidicv API:: kleidicv_remap_f32_u8_resolver,NEON backend.
kleidicv API:: kleidicv_remap_f32_u16_resolver,NEON backend.
kleidicv API:: kleidicv_warp_perspective_stripe_u8_resolver,NEON backend.
```

## Use lldb to check SME backend implementation

To perform source-level debugging during the build process, you should change the build type from "Release" to "Debug," as demonstrated in the following example:

```bash
cmake -S $WORKSPCE/kleidicv \ 
      -B build-kleidicv-benchmark-SME \
      -DKLEIDICV_ENABLE_SME2=ON \ 
      -DKLEIDICV_LIMIT_SME2_TO_SELECTED_ALGORITHMS=OFF \
      -DKLEIDICV_BENCHMARK=ON \
      -DCMAKE_BUILD_TYPE=Debug

cmake --build build-kleidicv-benchmark-SME --parallel
```

Use the lldb debug tool to set breakpoints during API testing and verify if the SME backend implementation is invoked. To view the function call backtrace, run the "bt" command as shown below:

```C

lldb kleidicv-api-test
(lldb) target create "kleidicv-api-test"
Current executable set to '/Users/Shared/workspace/build-kleidicv-benchmark-SME-debug/test/api/kleidicv-api-test' (arm64).
(lldb) b saturating_add_abs_with_threshold
Breakpoint 1: 2 locations.
(lldb) run
Process 82381 launched: '/Users/Shared/workspace/build-kleidicv-benchmark-SME-debug/test/api/kleidicv-api-test' (arm64)
Vector length is set to 16 bytes.
Seed is set to 3168213869.
[==========] Running 3703 tests from 141 test suites.
[----------] Global test environment set-up.
[----------] 9 tests from SaturatingAddAbsWithThresholdTest/0, where TypeParam = short
[ RUN      ] SaturatingAddAbsWithThresholdTest/0.TestPositive
Process 82381 stopped
* thread #1, queue = 'com.apple.main-thread', stop reason = breakpoint 1.2
    frame #0: 0x0000000100695554 kleidicv-api-test`kleidicv_error_t kleidicv::sme::saturating_add_abs_with_threshold<short>(src_a=0x0000600002796762, src_a_stride=46, src_b=0x00006000027967f2, src_b_stride=46, dst=0x0000600002796912, dst_stride=46, width=23, height=3, threshold=50) at add_abs_with_threshold_sme.cpp:15:47
   12  	                                  const T *src_b, size_t src_b_stride, T *dst,
   13  	                                  size_t dst_stride, size_t width,
   14  	                                  size_t height, T threshold) {
-> 15  	  return saturating_add_abs_with_threshold_sc(src_a, src_a_stride, src_b,
   16  	                                              src_b_stride, dst, dst_stride,
   17  	                                              width, height, threshold);
   18  	}
(lldb) bt
* thread #1, queue = 'com.apple.main-thread', stop reason = breakpoint 1.2
  * frame #0: 0x0000000100695554 kleidicv-api-test`kleidicv_error_t kleidicv::sme::saturating_add_abs_with_threshold<short>(src_a=0x0000600002796762, src_a_stride=46, src_b=0x00006000027967f2, src_b_stride=46, dst=0x0000600002796912, dst_stride=46, width=23, height=3, threshold=50) at add_abs_with_threshold_sme.cpp:15:47
    frame #1: 0x0000000100009930 kleidicv-api-test`SaturatingAddAbsWithThresholdTestBase<short>::call_api(this=0x000000016fdfe670) at test_add_abs_with_threshold.cpp:17:12
    frame #2: 0x00000001000090c8 kleidicv-api-test`OperationTest<short, 2ul, 1ul>::test(this=0x000000016fdfe670) at operation.h:90:11
    frame #3: 0x0000000100008870 kleidicv-api-test`SaturatingAddAbsWithThresholdTest_TestPositive_Test<short>::TestBody(this=0x000060000179e270) at test_add_abs_with_threshold.cpp:135:58
    frame #4: 0x00000001008417cc kleidicv-api-test`void testing::internal::HandleSehExceptionsInMethodIfSupported<testing::Test, void>(object=0x000060000179e270, method=0x00000000000000010000000000000020, location="the test body") at gtest.cc:2599:10
    frame #5: 0x0000000100810908 kleidicv-api-test`void testing::internal::HandleExceptionsInMethodIfSupported<testing::Test, void>(object=0x000060000179e270, method=0x00000000000000010000000000000020, location="the test body") at gtest.cc:2635:14
    frame #6: 0x0000000100810858 kleidicv-api-test`testing::Test::Run(this=0x000060000179e270) at gtest.cc:2674:5
    frame #7: 0x000000010081163c kleidicv-api-test`testing::TestInfo::Run(this=0x000000011fe04290) at gtest.cc:2853:11
    frame #8: 0x00000001008126bc kleidicv-api-test`testing::TestSuite::Run(this=0x000000011fe049d0) at gtest.cc:3012:30
    frame #9: 0x000000010081fdec kleidicv-api-test`testing::internal::UnitTestImpl::RunAllTests(this=0x000000011fe04780) at gtest.cc:5870:44
    frame #10: 0x0000000100845750 kleidicv-api-test`bool testing::internal::HandleSehExceptionsInMethodIfSupported<testing::internal::UnitTestImpl, bool>(object=0x000000011fe04780, method=(kleidicv-api-test`testing::internal::UnitTestImpl::RunAllTests() at gtest.cc:5748), location="auxiliary test code (environments or event listeners)") at gtest.cc:2599:10
    frame #11: 0x000000010081f804 kleidicv-api-test`bool testing::internal::HandleExceptionsInMethodIfSupported<testing::internal::UnitTestImpl, bool>(object=0x000000011fe04780, method=(kleidicv-api-test`testing::internal::UnitTestImpl::RunAllTests() at gtest.cc:5748), location="auxiliary test code (environments or event listeners)") at gtest.cc:2635:14
    frame #12: 0x000000010081f6fc kleidicv-api-test`testing::UnitTest::Run(this=0x00000001009c92f0) at gtest.cc:5444:10
    frame #13: 0x00000001004e8600 kleidicv-api-test`RUN_ALL_TESTS() at gtest.h:2293:73
    frame #14: 0x00000001004e83a8 kleidicv-api-test`main(argc=1, argv=0x000000016fdff3b0) at test_main.cpp:82:10
    frame #15: 0x000000019f492b98 dyld`start + 6076
```

In the meantime, the "disassemble --frame" command can be used to display the assembly instructions in SME streaming mode, as shown below:


```C
disassemble --frame
kleidicv-api-test`kleidicv::sme::saturating_add_abs_with_threshold<short>:
    0x100695510 <+0>:   sub    sp, sp, #0xa0
    0x100695514 <+4>:   stp    d15, d14, [sp, #0x50]
    0x100695518 <+8>:   stp    d13, d12, [sp, #0x60]
    0x10069551c <+12>:  stp    d11, d10, [sp, #0x70]
    0x100695520 <+16>:  stp    d9, d8, [sp, #0x80]
    0x100695524 <+20>:  stp    x29, x30, [sp, #0x90]
    0x100695528 <+24>:  smstart sm
    0x10069552c <+28>:  ldrsh  w8, [sp, #0xa0]
    0x100695530 <+32>:  str    x0, [sp, #0x48]
    0x100695534 <+36>:  str    x1, [sp, #0x40]
    0x100695538 <+40>:  str    x2, [sp, #0x38]
    0x10069553c <+44>:  str    x3, [sp, #0x30]
    0x100695540 <+48>:  str    x4, [sp, #0x28]
    0x100695544 <+52>:  str    x5, [sp, #0x20]
    0x100695548 <+56>:  str    x6, [sp, #0x18]
    0x10069554c <+60>:  str    x7, [sp, #0x10]
    0x100695550 <+64>:  strh   w8, [sp, #0xe]
->  0x100695554 <+68>:  ldr    x0, [sp, #0x48]
    0x100695558 <+72>:  ldr    x1, [sp, #0x40]
    0x10069555c <+76>:  ldr    x2, [sp, #0x38]
    0x100695560 <+80>:  ldr    x3, [sp, #0x30]
    0x100695564 <+84>:  ldr    x4, [sp, #0x28]
    0x100695568 <+88>:  ldr    x5, [sp, #0x20]
    0x10069556c <+92>:  ldr    x6, [sp, #0x18]
    0x100695570 <+96>:  ldr    x7, [sp, #0x10]
    0x100695574 <+100>: ldrh   w8, [sp, #0xe]
    0x100695578 <+104>: mov    x9, sp
    0x10069557c <+108>: strh   w8, [x9]
    0x100695580 <+112>: bl     0x10087b8d0    ; symbol stub for: kleidicv_error_t kleidicv::sme::saturating_add_abs_with_threshold_sc<short>(short const*, unsigned long, short const*, unsigned long, short*, unsigned long, unsigned long, unsigned long, short)
    0x100695584 <+116>: smstop sm
    0x100695588 <+120>: ldp    x29, x30, [sp, #0x90]
    0x10069558c <+124>: ldp    d9, d8, [sp, #0x80]
    0x100695590 <+128>: ldp    d11, d10, [sp, #0x70]
    0x100695594 <+132>: ldp    d13, d12, [sp, #0x60]
    0x100695598 <+136>: ldp    d15, d14, [sp, #0x50]
    0x10069559c <+140>: add    sp, sp, #0xa0
    0x1006955a0 <+144>: ret
(lldb)
```

