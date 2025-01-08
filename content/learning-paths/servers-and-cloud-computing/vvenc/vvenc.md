---
layout: learningpathall
title: Build and run the H.266 VVenC encoder on Arm servers
weight: 2
---

## What is VVenC?

* [Versatile Video Coding](https://www.hhi.fraunhofer.de/en/departments/vca/technologies-and-solutions/h266-vvc/fraunhofer-versatile-video-encoder-vvenc.html) (VVC; officially approved as ITU-T H.266 | 23090-3) is the most recent international video compression standard of ITU-T and ISO/IEC.

* `vvenc` is an open-source H.266/VVC encoder that offers very high compression efficiency and performance.

* There have been significant efforts made to optimize the open-source implementation of the H.266 encoder on Arm Neoverse platforms that supports Neon and SVE/SVE2 instructions.

* You can find the optimized code for use with Arm Neoverse platforms in the [vvenc Github Repository](https://github.com/fraunhoferhhi/vvenc). 

## Install dependencies
On your Arm-based server instance running Ubuntu 22.04, install the dependencies to build and run vvenc:

```bash
sudo apt update
sudo apt install git wget cmake p7zip-full numactl -y
```
Install llvm compiler to compile the C++ code:
```bash
wget https://apt.llvm.org/llvm.sh
chmod +x llvm.sh
sudo ./llvm.sh 18 all
```

## Download and build vvenc source

You can now download the optimized vvenc source code and run cmake to configure the build:

```bash
git clone https://github.com/fraunhoferhhi/vvenc.git
cd vvenc
CXX=clang++-18 CC=clang-18 cmake -S . -B build/release-static -DVVENC_ENABLE_ARM_SIMD_SVE=1 -DVVENC_ENABLE_ARM_SIMD_SVE2=1
```
Confirm that sve/sve2 has been enabled in the Makefile by checking the output from the configuration step:

```output
root@iZuf61ixurqifmpxuji4viZ:~/vvenc-1.13.0# CXX=clang++-18 CC=clang-18 cmake -S . -B build/release-static -DVVENC_ENABLE_ARM_SIMD_SVE=1 -DVVENC_ENABLE_ARM_SIMD_SVE2=1
-- The C compiler identification is Clang 18.1.8
-- The CXX compiler identification is Clang 18.1.8
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/clang-18 - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/clang++-18 - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- CMAKE_MODULE_PATH: updating module path to: /root/vvenc-1.13.0/cmake/modules
-- normalized target architecture: AARCH64
-- Performing Test SUPPORTED_Werror_unused_command_line_argument
-- Performing Test SUPPORTED_Werror_unused_command_line_argument - Success
-- Performing Test SUPPORTED_march=armv8_2_a+sve
-- Performing Test SUPPORTED_march=armv8_2_a+sve - Success
-- Performing Test SVE_COMPILATION_C_TEST_COMPILED
-- Performing Test SVE_COMPILATION_C_TEST_COMPILED - Success
-- Performing Test SVE_COMPILATION_CXX_TEST_COMPILED
-- Performing Test SVE_COMPILATION_CXX_TEST_COMPILED - Success
-- Performing Test SVE_HEADER_C_TEST_COMPILED
-- Performing Test SVE_HEADER_C_TEST_COMPILED - Success
-- Performing Test SVE_HEADER_CXX_TEST_COMPILED
-- Performing Test SVE_HEADER_CXX_TEST_COMPILED - Success
-- Performing Test SUPPORTED_march=armv9_a+sve2
-- Performing Test SUPPORTED_march=armv9_a+sve2 - Success
-- Performing Test SUPPORTED_msse4_1
-- Performing Test SUPPORTED_msse4_1 - Failed
-- Performing Test SUPPORTED_mavx
-- Performing Test SUPPORTED_mavx - Failed
-- Performing Test HAVE_INTRIN_mm_storeu_si16
-- Performing Test HAVE_INTRIN_mm_storeu_si16 - Success
-- Performing Test HAVE_INTRIN_mm_storeu_si32
-- Performing Test HAVE_INTRIN_mm_storeu_si32 - Success
-- Performing Test HAVE_INTRIN_mm_storeu_si64
-- Performing Test HAVE_INTRIN_mm_storeu_si64 - Success
-- Performing Test HAVE_INTRIN_mm_loadu_si32
-- Performing Test HAVE_INTRIN_mm_loadu_si32 - Success
-- Performing Test HAVE_INTRIN_mm_loadu_si64
-- Performing Test HAVE_INTRIN_mm_loadu_si64 - Success
-- Performing Test HAVE_INTRIN_mm_cvtsi128_si64
-- Performing Test HAVE_INTRIN_mm_cvtsi128_si64 - Success
-- Performing Test HAVE_INTRIN_mm_cvtsi64_si128
-- Performing Test HAVE_INTRIN_mm_cvtsi64_si128 - Success
-- Performing Test HAVE_INTRIN_mm_extract_epi64
-- Performing Test HAVE_INTRIN_mm_extract_epi64 - Success
-- Performing Test HAVE_INTRIN_mm256_zeroupper
-- Performing Test HAVE_INTRIN_mm256_zeroupper - Failed
-- Performing Test HAVE_INTRIN_mm256_loadu2_m128i
-- Performing Test HAVE_INTRIN_mm256_loadu2_m128i - Success
-- Performing Test HAVE_INTRIN_mm256_set_m128i
-- Performing Test HAVE_INTRIN_mm256_set_m128i - Success
-- x86 SIMD intrinsics enabled (using SIMDE for non-x86 targets)
-- AArch64 Neon intrinsics enabled
-- AArch64 SVE intrinsics enabled
-- AArch64 SVE2 intrinsics enabled
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE
-- Performing Test SUPPORTED_mxsave
-- Performing Test SUPPORTED_mxsave - Failed
-- Performing Test SUPPORTED_msse4_2
-- Performing Test SUPPORTED_msse4_2 - Failed
-- Performing Test SUPPORTED_mavx2
-- Performing Test SUPPORTED_mavx2 - Failed
-- Configuring done
-- Generating done
-- Build files have been written to: /root/vvenc-1.13.0/build/release-static
```
Now run cmake to build:
```bash
cmake --build build/release-static -j
```
The project should build successfully and the end of the output should look like:

```output
[100%] Linking CXX executable ../../../../../bin/release-static/vvencapp
[100%] Built target vvencinterfacetest
[100%] Built target vvenclibtest
[100%] Built target vvencFFapp
[100%] Built target vvencapp
```

## Download sample video files

To benchmark the compression efficiency and performance of `vvenc`, you need a set of video streams to run the codec on. 

Download sample `1080P` video files and decompress them:
```bash
mkdir ../video && cd ../video
wget http://ultravideo.cs.tut.fi/video/Bosphorus_1920x1080_120fps_420_8bit_YUV_Y4M.7z
7z x Bosphorus_1920x1080_120fps_420_8bit_YUV_Y4M.7z
```

## Run vvenc on the sample video files

To benchmark the performance of `vvenc` over 100 frames of the `1080P` video file, run the command:
```console
cd ../vvenc
numactl -C 0-3 bin/release-static/vvencFFapp --preset faster --BitstreamFile stream.266 --Threads 4 --InputFile ~/video/Bosphorus_1920x1080_120fps_420_8bit_YUV.y4m --InputBitDepth 8 --InputChromaFormat 420 --fps 30 --FramesToBeEncoded 100 --SourceWidth 1920 --SourceHeight 1080 --Qp 22 --IntraPeriod 256 --NumPasses 1 --InternalBitDepth 10 --stats 1 --Verbosity 3
```

You can vary the preset settings and measure the impact on performance.


## View Results

The encoding Frame Rate, shown in fps (frames per second), for the video files is output at the end of each run.

This is an example output from running the VVenC H.266 encoding on a 1080P sample video file:

```output
vvencFFapp: VVenC, the Fraunhofer H.266/VVC Encoder, version 1.13.0 [Linux][clang 18.1.8][64 bit][SIMD=SVE2]
vvencFFapp [info]: started @ Wed Dec 25 16:06:03 2024
vvenc [info]: Input File                             : /root/video/Bosphorus_1920x1080_120fps_420_8bit_YUV.y4m
vvenc [info]: Bitstream File                         : stream.266
vvenc [info]: Real Format                            : 1920x1080  yuv420p  30 Hz  SDR  600 frames
vvenc [info]: Frames                                 : encode 100 frames
vvenc [info]: Internal format                        : 1920x1080  30 Hz  SDR
vvenc [info]: Threads                                : 4  (parallel frames: 4)
vvenc [info]: Rate control                           : QP 22
vvenc [info]: Perceptual optimization                : Disabled
vvenc [info]: Intra period (keyframe)                : 256
vvenc [info]: Decoding refresh type                  : CRA

vvenc [info]: stats:  30.0% frame=  30/100 fps=   4.7 avg_fps=   4.7 bitrate=  3174.97 kbps avg_bitrate=  3174.97 kbps elapsed= 00h:00m:07s left= 00h:00mvvenc [info]: stats:  60.0% frame=  60/100 fps=   7.2 avg_fps=   5.7 bitrate=  2405.72 kbps avg_bitrate=  2790.34 kbps elapsed= 00h:00m:11s left= 00h:00mvvenc [info]: stats:  90.0% frame=  90/100 fps=   7.2 avg_fps=   6.1 bitrate=  2445.71 kbps avg_bitrate=  2675.47 kbps elapsed= 00h:00m:15s left= 00h:00mvvenc [info]: stats: 100.0% frame= 100/100 fps=   6.6 avg_fps=   6.6 bitrate=  2490.95 kbps avg_bitrate=  2490.95 kbps elapsed= 00h:00m:16s left= 00h:00m:00s
vvenc [info]: stats summary: frame= 100/100 avg_fps= 6.6 avg_bitrate= 2490.95 kbps
vvenc [info]: stats summary: frame I:   1, kbps: 32874.48, AvgQP: 17.00
vvenc [info]: stats summary: frame P:   0, kbps:      nan, AvgQP: nan
vvenc [info]: stats summary: frame B:  99, kbps:  2184.04, AvgQP: 27.42


vvenc [info]:	Total Frames |   Bitrate     Y-PSNR    U-PSNR    V-PSNR    YUV-PSNR
vvenc [info]:	      100    a    2490.9480   43.7378   48.7096   47.9283   44.7472

vvencFFapp [info]: finished @ Wed Dec 25 16:06:19 2024
vvencFFapp [info]: Total Time:       58.962 sec. [user]       15.209 sec. [elapsed]
```

You have successfully run the VVenC H.266 encoder on an 1080P sample video file and measured the performance.
