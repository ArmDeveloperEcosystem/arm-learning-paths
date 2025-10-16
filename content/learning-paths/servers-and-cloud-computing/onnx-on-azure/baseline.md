---
title: Baseline Testing
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Baseline Testing using ONNX Runtime: 

The purpose of this test is to measure the inference latency of ONNX Runtime on your Azure Cobalt 100 VM. By timing how long it takes to process a single input through the SqueezeNet INT8 model, you can validate that ONNX Runtime is functioning correctly and get a baseline performance measurement for your target hardware.

Create a file named `baseline.py` with the following code:
```python
import onnxruntime as ort
import numpy as np
import time

session = ort.InferenceSession("squeezenet-int8.onnx")
input_name = session.get_inputs()[0].name
data = np.random.rand(1, 3, 224, 224).astype(np.float32)

start = time.time()
outputs = session.run(None, {input_name: data})
end = time.time()

print("Inference time:", end - start)
```

Run the baseline script to measure inference time:

```console
python3 baseline.py
```
You should see output similar to:
```output
Inference time: 0.0026061534881591797
{{% notice Note %}}
Inference time is how long it takes for a trained machine learning model to make a prediction after it receives input data.

The input tensor shape `(1, 3, 224, 224)` means:
- `1`: One image is processed at a time (batch size)
- `3`: Three color channels (red, green, blue)
- `224 x 224`: Each image is 224 pixels wide and 224 pixels tall (standard for SqueezeNet)
{{% /notice %}}

This indicates the model successfully executed a single forward pass through the SqueezeNet INT8 ONNX model and returned results.

## Output summary:

Single inference latency(0.00260 sec): This is the time required for the model to process one input image and produce an output. The first run includes graph loading, memory allocation, and model initialization overhead.
Subsequent inferences are usually faster due to caching and optimized execution.

This demonstrates that the setup is fully working, and ONNX Runtime efficiently executes quantized models on Arm64. 

Great job! You've completed your first ONNX Runtime inference on Arm-based Azure infrastructure. This baseline test confirms your environment is set up correctly and ready for more advanced benchmarking.

Next, you'll use a dedicated benchmarking tool to capture more detailed performance statistics and further optimize your deployment.
