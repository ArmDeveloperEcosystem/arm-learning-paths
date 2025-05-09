---
title: Develop your knowledge
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Now that you’ve seen how to build and port a complete DSP function using the CMSIS-DSP Python package, it's a good idea to expand your understanding by looking at more examples. The CMSIS-DSP project provides many resources to help you deepen your knowledge.

## Study further examples

The [CMSIS-DSP python package](https://pypi.org/project/cmsisdsp/) and its [CMSIS-DSP python example folder](https://github.com/ARM-software/CMSIS-DSP/tree/main/PythonWrapper/examples) include tests, Jupyter notebooks, and documentation that highlight key differences between the Python and C APIs, helping you write more portable and efficient DSP code.

## Remaining issues

While the CMSIS-DSP Python package makes prototyping and conversion to C relatively easy, there are additional challenges when moving toward real-world applications. Here are a few remaining challenges to consider.

This Learning Path has shown how the package helps to design and translate a DSP function working on a block of samples from Python to C. But in a real application, you receive a continuous stream of samples, not predefined blocks. You'll need to split the stream into blocks before processing, and later recombine them to reconstruct the signal.

Part of the difficulty in this Learning Path comes from splitting and recombining the signal. Porting the block-handling logic from Python to C introduces additional complexity.

[CMSIS-Stream](https://github.com/ARM-software/CMSIS-Stream) may help with this. It is a platform-independent technology designed to simplify the use of block-processing functions with sample streams. If you are planning to deploy your DSP algorithms in streaming, real-time systems, it is worth exploring CMSIS-Stream. It can greatly simplify handling streams of data with block-based processing, offering a clean and efficient way to bridge the gap between theory and deployment.

You should now have a better idea of what the CMSIS-DSP Python package is capable of, and how it relates to its C equivalent.
