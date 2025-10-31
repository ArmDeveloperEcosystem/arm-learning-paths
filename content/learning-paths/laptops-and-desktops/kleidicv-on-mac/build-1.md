---
title: Download and Build for the Kleidicv Software 
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction

Arm KleidiCV is an open-source library of optimized performance-critical routines for Arm CPUs. It is designed for integrating into any CV framework to enable best performance for CV workloads on Arm, with no action needed by application developers.

Each KleidiCV function has three different implementations targeting Neon, SVE2 (Scalable Vector Extension) or Streaming SVE & SME2 (Scalable Matrix Extension). KleidiCV will automatically detect what hardware it's running on and select the best implementation accordingly.KleidiCV can be used as a lightweight standalone image processing library. Alternatively KleidiCV can be used seamlessly as part of the extremely popular OpenCV library. 

Since the Apple M4 family is based on the ARMv9.2‑A architecture, it supports the Scalable Matrix Extension (SME) (or a variant thereof) for matrix-compute acceleration. we will demostrate the build and do run test of the kleidicv, understand how the backend implementation is called for the KleidiCV functions.  

## Host Environment

The host machine utilized is a MacBook Pro (Apple M4 Pro), and the operating system version is detailed below:

```bash
ProductName:		macOS
ProductVersion:		15.5
BuildVersion:		24F74
```

CMake is available for installation through Homebrew if it is not already installed on the host machine.

```bash
brew install cmake
```

The host architecture feature can be verified as outlined below, confirming that FEAT_SME is supported:

```bash
sysctl -a | grep hw.optional.arm.FEAT
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

## Download the Software

To set up KleidiCV and OpenCV, first download the source code from GitLab. In your $WORKSPACE directory, clone KleidiCV using the v0.6.0 release tag.

```bash
cd $WORKSPACE
git clone -b 0.6.0 https://git.gitlab.arm.com/kleidi/kleidicv.git
```

Clone the OpenCV repository into $WORKSPACE using the v4.12.0 release tag.

```bash
cd $WORKSPACE
git clone https://github.com/opencv/opencv.git
git checkout 4.12.0
```

Apply the patch for OpenCV version 4.12.

```bash
patch -p1 < ../kleidicv/adapters/opencv/opencv-4.12.patch
patch -p1 < ../kleidicv/adapters/opencv/extra_benchmarks/opencv-4.12.patch
```


## Build Options

* KLEIDICV_ENABLE_SVE2 - Enable Scalable Vector Extension 2 code paths. This is on by default for some popular compilers known to support SVE2 but otherwise off by default.
  - KLEIDICV_LIMIT_SVE2_TO_SELECTED_ALGORITHMS - Limit Scalable Vector Extension 2 code paths to cases where it is expected to provide a benefit over other code paths. On by default. Has no effect if KLEIDICV_ENABLE_SVE2 is off.
* KLEIDICV_BENCHMARK - Enable building KleidiCV benchmarks. The benchmarks use Google Benchmark which will be downloaded automatically. Off by default.
* KLEIDICV_ENABLE_SME2 - Enable Scalable Matrix Extension 2 and Streaming Scalable Vector Extension code paths. Off by default while the ACLE SME specification is in beta.
  - KLEIDICV_LIMIT_SME2_TO_SELECTED_ALGORITHMS - Limit Scalable Matrix Extension 2 code paths to cases where it is expected to provide a benefit over other code paths. On by default. Has no effect if KLEIDICV_ENABLE_SME2 is off.

{{% notice Note %}}
Normally, if our tests show SVE2 or SME2 are slower than NEON, we default to NEON (unless overridden with -DKLEIDICV_LIMIT_SVE2_TO_SELECTED_ALGORITHMS=OFF or -DKLEIDICV_LIMIT_SME2_TO_SELECTED_ALGORITHMS=OFF).
{{% /notice %}}

## Build the KleidiCV standalone

Use the following command to build kleidicv natively:

```bash
cmake -S $WORKSPCE/kleidicv \ 
      -B build-kleidicv-benchmark-SME \
      -DKLEIDICV_ENABLE_SME2=ON \ 
      -DKLEIDICV_LIMIT_SME2_TO_SELECTED_ALGORITHMS=OFF \
      -DKLEIDICV_BENCHMARK=ON \
      -DCMAKE_BUILD_TYPE=Release 

cmake --build build-kleidicv-benchmark-SME --parallel
```
Once the build completes, the kleidicv API and framework tests appear below:

```bash
./build-kleidicv-benchmark-SME/test/framework/kleidicv-framework-test
./build-kleidicv-benchmark-SME/test/api/kleidicv-api-test
```

The Kleidicv benchmark test is available as follows:

```bash
./build-kleidicv-benchmark-SME/benchmark/kleidicv-benchmark
```
## Build the OpenCV with KleidiCV

The following command can be used to build OpenCV with kleidicv:

```bash
cmake -S $workspace/opencv /
      -B build-opencv-kleidicv-sme /
      -DWITH_KLEIDICV=ON / 
      -DKLEIDICV_ENABLE_SME2=ON / 
      -DKLEIDICV_SOURCE_PATH=$workspace/kleidicv /
      -DBUILD_LIST=imgproc,core,ts /
      -DBUILD_SHARED_LIBS=OFF /
      -DBUILD_TESTS=ON /
      -DBUILD_PERF_TEST=ON /
      -DWITH_PNG=OFF

cmake --build build-opencv-kleidicv-sme --parallel --target opencv_perf_imgproc opencv_perf_core
```

Upon completion of the build process, the OpenCV test binary will be available at the following location:

```bash
build-opencv-kleidicv-sme/bin/opencv_perf_core
build-opencv-kleidicv-sme/bin/opencv_perf_imgproc
```

