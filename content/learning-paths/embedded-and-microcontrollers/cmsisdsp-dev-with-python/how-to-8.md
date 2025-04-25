---
title: Study more examples
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Now that you’ve seen how to build and port a complete DSP function using the CMSIS-DSP Python package, it’s a good idea to expand your understanding by looking at more examples. The CMSIS-DSP project provides many resources to help you deepen your knowledge.

## Study more examples

The [CMSIS-DSP python example folder](https://github.com/ARM-software/CMSIS-DSP/tree/main/PythonWrapper/examples) contains many tests, examples, and some Jupyter notebooks.

You can study these examples to gain a better understanding of how to use the Python package.

The [CMSIS-DSP python package](https://pypi.org/project/cmsisdsp/) describes the differences between the Python API and the C API.

In addition to the examples themselves, the CMSIS-DSP Python package documentation offers important details about differences between the Python and C APIs. Studying these differences will help you write more portable and efficient DSP code.

## Remaining issues

While the CMSIS-DSP Python package makes prototyping and conversion to C relatively easy, there are additional challenges when moving toward real-world applications. Let’s discuss a few of the remaining issues you should be aware of.

This learning path has showed how the package helps to design and translate a DSP function working on a block of samples from Python to C. But in a real application, you don’t receive blocks of samples, but rather a continuous stream. The stream of samples must be split into blocks before the DSP function can be used. The processed blocks may need to be recombined to reconstruct a signal.

Part of the difficulty in this learning path comes from splitting and recombining the signal. Translating this part of the Python code to C adds further complexity.

[CMSIS-Stream](https://github.com/ARM-software/CMSIS-Stream) may help for this. It is a platform-independent technology designed to simplify the use of block-processing functions with sample streams. If you are planning to deploy your DSP algorithms in streaming, real-time systems, it is worth exploring CMSIS-Stream. It can greatly simplify handling streams of data with block-based processing, offering a clean and efficient way to bridge the gap between theory and deployment.
