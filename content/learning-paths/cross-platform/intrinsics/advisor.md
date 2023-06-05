---
layout: learningpathall
title: Find intrinsics in large code bases
weight: 6
---

Porting applications to Arm is easier when you identify architecture specific code before you start to build or run.

## Porting Advisor

[Porting Advisor for Graviton](https://github.com/aws/porting-advisor-for-graviton/) is a command line tool for assessing the portability of software to AWS Graviton processors. 

Supported operating systems include Linux, Windows, and macOS.

## Install Porting Advisor

Use the [Porting Advisor for Graviton](/install-guides/porting-advisor/) install guide to set it up on your machine.

There are multiple ways to run Porting Advisor. The example below assumes you are running Porting Advisor as an executable and it is in your search path.

## Run Porting Advisor

You can run Porting Advisor on a realistic application such as the open source [KasmVNC](https://github.com/kasmtech/KasmVNC) project.

Use `git` to retrieve the source code:

```console
git clone https://github.com/kasmtech/KasmVNC.git
```

Specify the directory containing the source code to be analyzed.

The Porting Advisor executable name may differ based on your computer architecture and operating system. 

The command below is for an Arm Linux machine. Substitute your executable name if you have a different platform.

Run Porting Advisor:

```console
porting-advisor-linux-aarch64 KasmVNC
```

Porting Advisor scans the directory and detects any architecture specific extensions. 

The output will be similar to: 

```output
Porting Advisor for Graviton v1.0.2
Report date: 2023-06-02 11:36:02

465 files scanned.
detected python code. if you need pip, version 19.3 or above is recommended. we detected that you have version 22.0.2.
detected python code. min version 3.7.5 is required. we detected that you have version 3.10.6. see https://github.com/aws/aws-graviton-getting-started/blob/main/python.md for more details.
KasmVNC/common/rfb/scale_sse2.cxx: 55 other issues
KasmVNC/common/rfb/scale_sse2.cxx:74 (SSE2_halve): architecture-specific intrinsic: _mm_loadu_si128
KasmVNC/common/rfb/scale_sse2.cxx:75 (SSE2_halve): architecture-specific intrinsic: _mm_loadu_si128
KasmVNC/common/rfb/scale_sse2.cxx:62 (SSE2_halve): architecture-specific intrinsic: _mm_set_epi32
KasmVNC/common/rfb/scale_sse2.cxx:63 (SSE2_halve): architecture-specific intrinsic: _mm_set_epi32
KasmVNC/common/rfb/scale_sse2.cxx:64 (SSE2_halve): architecture-specific intrinsic: _mm_set_epi32
KasmVNC/common/rfb/scale_sse2.cxx:61 (SSE2_halve): architecture-specific intrinsic: _mm_setzero_si128
KasmVNC/common/rfb/scale_sse2.cxx:78 (SSE2_halve): architecture-specific intrinsic: _mm_unpackhi_epi8
KasmVNC/common/rfb/scale_sse2.cxx:80 (SSE2_halve): architecture-specific intrinsic: _mm_unpackhi_epi8
KasmVNC/common/rfb/scale_sse2.cxx:77 (SSE2_halve): architecture-specific intrinsic: _mm_unpacklo_epi8
KasmVNC/common/rfb/scale_sse2.cxx:79 (SSE2_halve): architecture-specific intrinsic: _mm_unpacklo_epi8

Report generated successfully. Hint: you can use --output FILENAME.html to generate an HTML report.
```

Porting Advisor saves times by quickly identifying architecture specific code in a project. 