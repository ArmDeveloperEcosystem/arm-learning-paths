---
title: Study more examples
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Study more examples

The [CMSIS-DSP python example folder](https://github.com/ARM-software/CMSIS-DSP/tree/main/PythonWrapper/examples) contains many tests, examples, and some Jupyter notebooks.

You can study these examples to gain a better understanding of how to use the Python package.

The [CMSIS-DSP python package](https://pypi.org/project/cmsisdsp/) describes the differences between the Python API and the C API.


## Remaining issues

The CMSIS-DSP Python package helps to design and translate a DSP function working on a block of samples from Python to C.
But in a real application, you don’t receive blocks of samples, but rather a continuous stream.

The stream of samples must be split into blocks before the DSP function can be used. The processed blocks may need to be recombined to reconstruct a signal.

Part of the difficulty in this learning path comes from splitting and recombining the signal. Translating this part of the Python code to C adds further complexity.

[CMSIS-Stream](https://github.com/ARM-software/CMSIS-Stream) may help for this. It is a platform-independent technology designed to simplify the use of block-processing functions with sample streams. It is a low-overhead solution.
