---
layout: learningpathall
title: Finding intrinsics in large code bases
weight: 6
---

## Porting Advisor

The [aarch64 Porting Advisor](https://github.com/arm-hpc/porting-advisor) is a very useful tool to quickly identify architecture specific code in a code base.

## Install dependencies

If necessary, install `git`, `python3` and `setuptools`:

```bash { target="amd64/ubuntu:latest" }
sudo apt install -y git python3 python3-setuptools
```

## Install Porting Advisor

Install `Porting Advisor` with the commands below:

```bash { target="amd64/ubuntu:latest" }
git clone https://github.com/arm-hpc/porting-advisor.git
cd porting-advisor
sudo python3 setup.py install
```

## Run Porting Advisor

Specify the directory containing the source code to be analyzed.

A more realistic example than the previous would be to use on the open source [KasmVNC](https://github.com/kasmtech/KasmVNC) project:

```bash { target="amd64/ubuntu:latest" }
git clone https://github.com/kasmtech/KasmVNC.git
porting-advisor KasmVNC 
```

Porting Advisor scans the directory and detects any architecture specific extensions. The output will be similar to: 

```output
413 files scanned.
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
```

See the [usage instructions](https://github.com/arm-hpc/porting-advisor/blob/master/README.md#Usage) for more information.
