---
title: Baseline Testing
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Baseline testing using ONNX Runtime: 

This test measures the inference latency of the ONNX Runtime by timing how long it takes to process a single input using the `squeezenet-int8.onnx model`. It helps evaluate how efficiently the model runs on the target hardware.

Create a **baseline.py** file with the below code for baseline test of ONNX:

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

Run the baseline test:

```console
python3 baseline.py
```
You should see an output similar to:
```output
Inference time: 0.02060103416442871
```
{{% notice Note %}}Inference time is the amount of time it takes for a trained machine learning model to make a prediction (i.e., produce output) after receiving input data. 
input tensor of shape (1, 3, 224, 224): 
- 1: batch size 
- 3: color channels (RGB) 
- 224 x 224: image resolution (common for models like SqueezeNet)
{{% /notice %}}

#### Output summary:

- Single inference latency: ~2.60 milliseconds (0.00260 sec) 
- This shows the initial (cold-start) inference performance of ONNX Runtime on CPU using an optimized int8 quantized model. 
- This demonstrates that the setup is fully working, and ONNX Runtime efficiently executes quantized models on Arm64. 
