---
title: Build ONNX Runtime
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build ONNX Runtime for Windows on Arm
Now that your environment is set up, you're ready to build the ONNX Runtime inference engine. 

ONNX Runtime is an open-source inference engine for accelerating the deployment of machine learning models, particularly those in the Open Neural Network Exchange (ONNX) format. ONNX Runtime is optimized for high performance and low latency, widely used in the production deployment of AI models. 

{{% notice Learning Tip %}}
You can learn more about ONNX Runtime by reading the [ONNX Runtime Overview](https://onnxruntime.ai/).
{{% /notice %}}

### Clone the ONNX Runtime repository

Open a developer command prompt for Visual Studio to set up the environment including path to compiler, linker, utilities and header files. 

Create your workspace and check out the source tree:

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

### Build for Windows

You can build the "Release" configuration for a build optimized for performance but without debug information.


```bash
.\build.bat --config Release --build_shared_lib --parallel --compile_no_warning_as_error --skip_submodule_sync  --skip_tests
```


As an alternative, you can build with "RelWithDebInfo" configuration for a release-optimized build with debug information.

```bash
.\build.bat --config RelWithDebInfo  --build_shared_lib --parallel --compile_no_warning_as_error --skip_submodule_sync  --skip_tests
```


### Resulting Dynamic Link Library
When the build is complete, the `onnxruntime.dll` dynamic linked library can be found in: 

```
dir .\build\Windows\Release\Release\onnxruntime.dll
```

or if you build with debug information it can be found in:

```
dir .\build\Windows\RelWithDebInfo\RelWithDebInfo\onnxruntime.dll
```
