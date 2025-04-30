---
title: Build ONNX Runtime
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build ONNX Runtime for Windows on Arm
Now that your environment is set up, you're ready to build the ONNX Runtime inference engine. 

ONNX Runtime is an open-source engine for accelerating machine learning model inference, especially those in the Open Neural Network Exchange (ONNX) format. 

ONNX Runtime is optimized for high performance and low latency, and is widely used in production deployments. 

{{% notice Learning Tip %}}
You can learn more about ONNX Runtime by reading the [ONNX Runtime Overview](https://onnxruntime.ai/).
{{% /notice %}}

### Clone the ONNX Runtime repository

Open a command prompt for Visual Studio to set up the environment, which includes paths to the compiler, linker, utilities, and header files. 

Then, create your workspace and clone the repository:

```bash
cd C:\Users\%USERNAME%
mkdir repos\lp
cd repos\lp
git clone --recursive https://github.com/Microsoft/onnxruntime.git
cd onnxruntime
git checkout 4eeefd7260b7fa42a71dd1a08b423d5e7c722050
```

{{% notice Note %}}
You might be able to use a later commit. These steps have been tested with the commit `4eeefd7260b7fa42a71dd1a08b423d5e7c722050`.
{{% /notice %}}

### Build ONNX Runtime

To build the ONNX Runtime shared library, use one of the following configurations:

* **Release** configuration, for a build optimized for performance but without debug information:


```bash
.\build.bat --config Release --build_shared_lib --parallel --compile_no_warning_as_error --skip_submodule_sync  --skip_tests
```

* **RelWithDebInfo** configuration, which includes debug symbols for profiling or inspection:

```bash
.\build.bat --config RelWithDebInfo  --build_shared_lib --parallel --compile_no_warning_as_error --skip_submodule_sync  --skip_tests
```


### Resulting Dynamic Link Library
When the build is complete, you'll find the `onnxruntime.dll` dynamic linked library in the following respective directories: 

* For **Release** build:

```
dir .\build\Windows\Release\Release\onnxruntime.dll
```

* For **RelWithDebInfo** build:

```
dir .\build\Windows\RelWithDebInfo\RelWithDebInfo\onnxruntime.dll
```
