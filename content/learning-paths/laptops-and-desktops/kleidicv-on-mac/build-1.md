---
title: Download and build KleidiCV software 
weight: 2

layout: learningpathall
---

## Introduction

Arm KleidiCV is an open-source library that provides fast, optimized routines for Arm CPUs. You can use KleidiCV with any computer vision (CV) framework to boost performance for CV workloads on Arm systems. 

KleidiCV includes multiple optimized implementations for each function, targeting Arm Neon, SVE2 (Scalable Vector Extension 2), and SME2 (Scalable Matrix Extension 2) instruction sets. The library automatically detects your hardware and chooses the fastest available code path, so you don't need to adjust your code for different Arm CPUs. 

You can use KleidiCV as a standalone image processing library or integrate it with OpenCV for broader computer vision support. On Apple M4 processors, which use the Armv9.2‑A architecture and support SME, you'll see improved performance for matrix operations. In this Learning Path, you'll build and test KleidiCV to observe how it selects the best backend for your hardware.  

## Set up your environment 

To follow this example you'll need a MacBook Pro with an Apple Silicon M4 processor. To check your operating system version, select the **Apple menu ()** in the top-left corner of your screen and choose **About This Mac**. Alternatively, open a terminal and run:

```console
sw_vers
```
The output is similar to:

```output
ProductName:		macOS
ProductVersion:		15.5
BuildVersion:		24F74
```

You also need CMake. If CMake is not already installed on your host machine, you can install it using Homebrew:

```bash
brew install cmake
```
To check which Arm architecture features your Mac supports, run the following command in your terminal:

```bash
sysctl -a | grep hw.optional.arm.FEAT
```

Look for `hw.optional.arm.FEAT_SME: 1` in the output. If you see this line, your system supports SME (Scalable Matrix Extension). If the value is `0`, SME is not available on your hardware.

The output is:

```output
hw.optional.arm.FEAT_CRC32: 1
hw.optional.arm.FEAT_FlagM: 1
hw.optional.arm.FEAT_FlagM2: 1
hw.optional.arm.FEAT_FHM: 1
hw.optional.arm.FEAT_DotProd: 1
hw.optional.arm.FEAT_SHA3: 1
hw.optional.arm.FEAT_RDM: 1
hw.optional.arm.FEAT_LSE: 1
hw.optional.arm.FEAT_SHA256: 1
hw.optional.arm.FEAT_SHA512: 1
hw.optional.arm.FEAT_SHA1: 1
hw.optional.arm.FEAT_AES: 1
hw.optional.arm.FEAT_PMULL: 1
hw.optional.arm.FEAT_SPECRES: 0
hw.optional.arm.FEAT_SPECRES2: 0
hw.optional.arm.FEAT_SB: 1
hw.optional.arm.FEAT_FRINTTS: 1
hw.optional.arm.FEAT_PACIMP: 1
hw.optional.arm.FEAT_LRCPC: 1
hw.optional.arm.FEAT_LRCPC2: 1
hw.optional.arm.FEAT_FCMA: 1
hw.optional.arm.FEAT_JSCVT: 1
hw.optional.arm.FEAT_PAuth: 1
hw.optional.arm.FEAT_PAuth2: 1
hw.optional.arm.FEAT_FPAC: 1
hw.optional.arm.FEAT_FPACCOMBINE: 1
hw.optional.arm.FEAT_DPB: 1
hw.optional.arm.FEAT_DPB2: 1
hw.optional.arm.FEAT_BF16: 1
hw.optional.arm.FEAT_EBF16: 0
hw.optional.arm.FEAT_I8MM: 1
hw.optional.arm.FEAT_WFxT: 1
hw.optional.arm.FEAT_RPRES: 1
hw.optional.arm.FEAT_CSSC: 0
hw.optional.arm.FEAT_HBC: 0
hw.optional.arm.FEAT_ECV: 1
hw.optional.arm.FEAT_AFP: 1
hw.optional.arm.FEAT_LSE2: 1
hw.optional.arm.FEAT_CSV2: 1
hw.optional.arm.FEAT_CSV3: 1
hw.optional.arm.FEAT_DIT: 1
hw.optional.arm.FEAT_FP16: 1
hw.optional.arm.FEAT_SSBS: 0
hw.optional.arm.FEAT_BTI: 1
hw.optional.arm.FEAT_SME: 1
hw.optional.arm.FEAT_SME2: 1
hw.optional.arm.FEAT_SME_F64F64: 1
hw.optional.arm.FEAT_SME_I16I64: 1
```

If your Mac does not have an M4 processor, you won't see the `FEAT_SME` flags set to `1`. In that case, SME (Scalable Matrix Extension) features are not available on your hardware, and KleidiCV will use other optimized code paths instead.

## Create a workspace

You can use an environment variable to define your workspace:

```bash
export WORKSPACE=<your-workspace-directdory>
```

For example, 

```bash
mkdir $HOME/kleidi
export WORKSPACE=$HOME/kleidi
```

## Download the software

To set up KleidiCV and OpenCV, first download the source code from GitLab. 

In your $WORKSPACE directory, clone KleidiCV using the v0.6.0 release tag.

```bash
cd $WORKSPACE
git clone -b 0.6.0 https://git.gitlab.arm.com/kleidi/kleidicv.git
```

Clone the OpenCV repository into $WORKSPACE using the v4.12.0 release tag:

```bash
cd $WORKSPACE
git clone https://github.com/opencv/opencv.git
cd opencv
git checkout 4.12.0
```

Apply the patch for OpenCV version 4.12:

```bash
patch -p1 < ../kleidicv/adapters/opencv/opencv-4.12.patch
patch -p1 < ../kleidicv/adapters/opencv/extra_benchmarks/opencv-4.12.patch
```


## Build options

KleidiCV provides several CMake options to control which instruction sets and features are enabled during the build. Here are the most important options for Arm systems:

- **KLEIDICV_ENABLE_SVE2**  
  Enables Scalable Vector Extension 2 (SVE2) code paths. This is on by default for popular compilers that support SVE2, but off otherwise.

    - **KLEIDICV_LIMIT_SVE2_TO_SELECTED_ALGORITHMS**  
      Limits SVE2 code paths to algorithms where SVE2 is expected to outperform other options. This is on by default. It has no effect if SVE2 is disabled.

- **KLEIDICV_BENCHMARK**  
  Enables building KleidiCV benchmarks. The benchmarks use Google Benchmark, which is downloaded automatically. This is off by default.

- **KLEIDICV_ENABLE_SME2**  
  Enables Scalable Matrix Extension 2 (SME2) and Streaming SVE code paths. This is off by default while the ACLE SME specification is in beta.

    - **KLEIDICV_LIMIT_SME2_TO_SELECTED_ALGORITHMS**  
      Limits SME2 code paths to cases where SME2 is expected to provide a benefit. This is on by default. It has no effect if SME2 is disabled.

You can set these options when running `cmake` to customize your build for your hardware and use case.

{{% notice Note %}}
KleidiCV automatically selects the fastest available code path for your hardware. If the library detects that SVE2 (Scalable Vector Extension 2) or SME2 (Scalable Matrix Extension 2) is slower than NEON for a specific function, it defaults to NEON—unless you explicitly turn off this behavior by setting `-DKLEIDICV_LIMIT_SVE2_TO_SELECTED_ALGORITHMS=OFF` or `-DKLEIDICV_LIMIT_SME2_TO_SELECTED_ALGORITHMS=OFF`.
{{% /notice %}}

## Build the KleidiCV standalone

Use the following command to build KleidiCV natively:

```bash
cmake -S $WORKSPACE/kleidicv \ 
      -B build-kleidicv-benchmark-SME \
      -DKLEIDICV_ENABLE_SME2=ON \ 
      -DKLEIDICV_LIMIT_SME2_TO_SELECTED_ALGORITHMS=OFF \
      -DKLEIDICV_BENCHMARK=ON \
      -DCMAKE_BUILD_TYPE=Release 
cmake --build build-kleidicv-benchmark-SME --parallel
```
Once the build completes, the KleidiCV API and framework tests appear below:

```bash
ls ./build-kleidicv-benchmark-SME/test/framework/kleidicv-framework-test 
ls ./build-kleidicv-benchmark-SME/test/api/kleidicv-api-test
```

The KleidiCV benchmark test is available as follows:

```bash
ls ./build-kleidicv-benchmark-SME/benchmark/kleidicv-benchmark
```
## Build the OpenCV with KleidiCV

The following command can be used to build OpenCV with KleidiCV:

```bash
cmake -S $WORKSPACE/opencv \
      -B build-opencv-kleidicv-sme \
      -DWITH_KLEIDICV=ON \ 
      -DKLEIDICV_ENABLE_SME2=ON \ 
      -DKLEIDICV_SOURCE_PATH=$WORKSPACE/kleidicv \
      -DBUILD_LIST=imgproc,core,ts \
      -DBUILD_SHARED_LIBS=OFF \
      -DBUILD_TESTS=ON \
      -DBUILD_PERF_TEST=ON \
      -DWITH_PNG=OFF
cmake --build build-opencv-kleidicv-sme --parallel --target opencv_perf_imgproc opencv_perf_core
```

Upon completion of the build process, the OpenCV test binary will be available at the following location:

```bash
ls build-opencv-kleidicv-sme/bin/opencv_perf_core
ls build-opencv-kleidicv-sme/bin/opencv_perf_imgproc
```

## What you've accomplished and what's next

You've successfully set up your development environment, downloaded the KleidiCV and OpenCV source code, and built both libraries with SME2 support on your Apple Silicon Mac. At this point, you have all the tools you need to explore how KleidiCV optimizes for Arm architectures.

In the next section, you'll run benchmarks to see SME in action and learn how KleidiCV automatically selects the best code paths for your hardware. This will help you understand the performance benefits of Arm's advanced instruction sets for computer vision workloads.
