---
title: CMSIS-DSP Python package
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is CMSIS-DSP?

CMSIS-DSP is a general-purpose computation library focused on digital signal processing (DSP). Originally developed for Cortex-M processors, it now also supports Cortex-A.

The library is optimized for each architecture:

- DSP extensions on Cortex-M4 and M7.
- Helium on M55 and M85.
- Neon on Cortex-A55 and other Cortex-A cores.

## What is the CMSIS-DSP Python package?

The CMSIS-DSP Python package provides a Python API for CMSIS-DSP. Its goal is to make it easier to develop a C solution using CMSIS-DSP by bridging the gap between a Python-based design environment  and a final C implementation.

he API is designed to closely mirror the C version in both function and structure.

Fixed-point arithmetic is rarely provided by Python packages, which generally focus on floating-point operations. The CMSIS-DSP Python package provides the same fixed-point arithmetic functions as the C version: Q31, Q15 and Q7. The package also provides floating-point functions and will also support half-precision floats in the future, like the C API.

The package is compatible with NumPy and integrates well with scientific and AI libraries such as SciPy and PyTorch.

