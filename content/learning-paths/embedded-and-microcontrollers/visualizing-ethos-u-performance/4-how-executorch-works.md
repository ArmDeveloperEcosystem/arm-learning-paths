---
# User change
title: "Understand the ExecuTorch workflow"

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

Before setting up your environment, it helps to understand how ExecuTorch processes a model and runs it on Arm-based hardware.

To get a better understanding of [How ExecuTorch Works](https://docs.pytorch.org/executorch/stable/intro-how-it-works.html) refer to the official PyTorch Documentation. A summary is provided here for your reference:

## ExecuTorch pipeline overview

ExecuTorch works in three main stages:

1. **Export the model:**
   * Convert a trained PyTorch model into an operator graph.
   * Identify operators that can be offloaded to the Ethos-U NPU (for example, ReLU, conv, quantize).
2. **Compile with the AOT compiler:**
   * Translate the operator graph into an optimized, quantized format.
   * Use `--delegate` to move eligible operations to the Ethos-U accelerator.
   * Save the compiled output as a `.pte` file.
3. **Deploy and run:**
   * Deploy the ML model to a Fixed Virtual Platform (FVP) or physical device
   * Execute operators on the CPU and delegated operators on the Ethos-U NPU

**Diagram of How ExecuTorch Works**
![How ExecuTorch works#center](./how-executorch-works-high-level.png)

## Deploy a TinyML Model

With your development environment set up, you can deploy a simple PyTorch model.

This example deploys the [MobileNet V2](https://pytorch.org/hub/pytorch_vision_mobilenet_v2/) computer vision model. The model is a convolutional neural network (CNN) that extracts visual features from an image. It is used for image classification and object detection.

The actual Python code for the MobileNet V2 model is in your local `executorch` repo: [executorch/examples/models/mobilenet_v2/model.py](https://github.com/pytorch/executorch/blob/main/examples/models/mobilenet_v2/model.py). You can deploy it using [run.sh](https://github.com/pytorch/executorch/blob/main/examples/arm/run.sh), just like you did in the previous step, with some extra parameters:

{{% notice macOS %}}

**Start Docker:** on macOS, FVPs run inside a Docker container.

{{% /notice %}}

```bash
./examples/arm/run.sh \
--aot_arm_compiler_flags="--delegate --quantize --intermediates mv2_u85/ --debug --evaluate" \
--output=mv2_u85 \
--target=ethos-u85-128 \
--model_name=mv2
```

**Explanation of run.sh Parameters**
|run.sh Parameter|Meaning / Context|
|--------------|-----------------|
|--aot_arm_compiler_flags|Passes a string of compiler options to the ExecuTorch Ahead-of-Time (AOT) compiler|
|--delegate|Enables backend delegation|
|--quantize|Converts the floating-point model to int8 quantized format using post-training quantization<br>**Essential for running on NPUs**|
|--intermediates mv2_u85/|Directory where intermediate files (e.g., TOSA, YAMLs, debug graphs) will be saved<br>Useful output files for **manual debugging**|
|--debug|Verbose debugging logging|
|--evaluate|Validates model output, provides timing estimates|
