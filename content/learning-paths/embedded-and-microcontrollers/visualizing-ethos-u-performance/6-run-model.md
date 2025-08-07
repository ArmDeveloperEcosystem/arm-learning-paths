---
# User change
title: "Deploy and run Mobilenet V2 on the Corstone-320 FVP"

weight: 6 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
## Deploy Mobilenet V2 with ExecuTorch

With your environment and FVP now set up, you're ready to deploy and run a real TinyML model using ExecuTorch.

This example deploys the [MobileNet V2](https://pytorch.org/hub/pytorch_vision_mobilenet_v2/) computer vision model. The model is a convolutional neural network (CNN) that extracts visual features from an image. It is used for image classification and object detection.

The Python code for the MobileNet V2 model is in your local `executorch` repo: [executorch/examples/models/mobilenet_v2/model.py](https://github.com/pytorch/executorch/blob/main/examples/models/mobilenet_v2/model.py). You can deploy it using [run.sh](https://github.com/pytorch/executorch/blob/main/examples/arm/run.sh), just like you did in the previous step, with some extra parameters:

{{% notice Tip %}}

On macOS, make sure Docker is running. FVPs execute inside a Docker container.

{{% /notice %}}

```bash
./examples/arm/run.sh \
--aot_arm_compiler_flags="--delegate --quantize --intermediates mv2_u85/ --debug --evaluate" \
--output=mv2_u85 \
--target=ethos-u85-128 \
--model_name=mv2
```

The `--model_name=mv2` flag tells `run.sh` to use the Mobilenet V2 model defined in examples/models/mobilenet_v2/model.py.

**Explanation of run.sh Parameters**
|run.sh Parameter|Meaning / Context|
|--------------|-----------------|
|--aot_arm_compiler_flags|Passes a string of compiler options to the ExecuTorch Ahead-of-Time (AOT) compiler|
|--delegate|Enables backend delegation|
|--quantize|Converts the floating-point model to int8 quantized format using post-training quantization<br>**Essential for running on NPUs**|
|--intermediates mv2_u85/|Directory where intermediate files (e.g., TOSA, YAMLs, debug graphs) will be saved<br>Useful output files for **manual debugging**|
|--debug|Verbose debugging logging|
|--evaluate|Validates model output, provides timing estimates|

## What to expect

ExecuTorch will:

- Compile the PyTorch model to .pte format
- Generate intermediate files (YAMLs, graphs, etc.)
- Run the compiled model on the FVP
- Output execution timing, operator delegation, and performance stats

You should see output like:

```bash
Batch Inference time     4.94 ms,  202.34 inferences/s
Total delegated subgraphs: 1
Number of delegated nodes: 419
```

A high number of delegated nodes means the majority of model execution was successfully offloaded to the Ethos-U NPU for acceleration. This confirms that the model was successfully compiled, deployed, and run with NPU acceleration.

## Next steps
If you’d like to visualize instruction counts and performance using the GUI, continue to the next (optional) section.
