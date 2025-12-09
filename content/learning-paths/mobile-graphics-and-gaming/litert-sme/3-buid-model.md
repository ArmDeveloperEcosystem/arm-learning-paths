---
title: Create LiteRT models
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### KleidiAI SME2 support in LiteRT

LiteRT uses XNNPACK as its default CPU backend. KleidiAI micro-kernels are integrated through XNNPACK in LiteRT.
Only a subset of KleidiAI SME, SME2 micro-kernels has been integrated into XNNPACK.
These micro-kernels support operators using the following data types and quantization configurations in the LiteRT model.
Other operators are using XNNPACK’s default implementation during the inference.

* Fully connected 
| Activations                  | Weights                                 | Output                       |
| ---------------------------- | --------------------------------------- | ---------------------------- |
| FP32                         | FP32                                    | FP32                         |
| FP32                         | FP16                                    | FP32                         |
| FP32                         | Per-channel symmetric INT8 quantization | FP32                         |
| Asymmetric INT8 quantization | Per-channel symmetric INT8 quantization | Asymmetric INT8 quantization |
| FP32                         | Per-channel symmetric INT4 quantization | FP32                         |

* Batch Matrix Multiply
| Input A | Input B                                 |
| ------- | --------------------------------------- |
| FP32    | FP32                                    |
| FP16    | FP16                                    |   
| FP32    | Per-channel symmetric INT8 quantization |


* Conv2D
| Activations                  | Weights                                               | Output                       |
| ---------------------------- | ----------------------------------------------------- | ---------------------------- |
| FP32                         | FP32, pointwise (kernerl size is 1)                   | FP32                         |
| FP32                         | FP16, pointwise (kernerl size is 1)                   | FP32                         |
| FP32                         | Per-channel or per-tensor symmetric INT8 quantization | FP32                         |
| Asymmetric INT8 quantization | Per-channel or per-tensor symmetric INT8 quantization | Asymmetric INT8 quantization |


* TransposeConv
| Activations                  | Weights                                               | Output                       |
| ---------------------------- | ----------------------------------------------------- | ---------------------------- |
| Asymmetric INT8 quantization | Per-channel or per-tensor symmetric INT8 quantization | Asymmetric INT8 quantization |


### Create LiteRT models using Keras
To demonstrate SME2 acceleration on Android, you will construct simple single-layer models (e.g., Fully Connected) using Keras and convert them into LiteRT (.tflite) format.
This allows you to benchmark isolated operators and directly observe SME2 improvements.
The following script is provided as an example:

``` python
import tensorflow as tf
import numpy as np
import os

batch_size = 100
input_size = 640
output_size = 1280

def save_litert_model(model_bytes, filename):
    if os.path.exists(filename):
        print(f"Warning: {filename} already exists and will be overwritten.")
    with open(filename, "wb") as f:
        f.write(model_bytes)

model = tf.keras.Sequential([
     tf.keras.layers.InputLayer(input_shape=(input_size,), batch_size=batch_size),
     tf.keras.layers.Dense(output_size)
])

# Convert to FP32 model
converter = tf.lite.TFLiteConverter.from_keras_model(model)
fc_fp32 = converter.convert()
save_litert_model(fc_fp32, "fc_fp32.tflite")
```

The model above is created in FP32 format. As mentioned in the previous section, this operator can invoke the KleidiAI SME2 micro-kernel for acceleration.

You can also optimize this Keras model using post-training quantization to create a LiteRT model that suits your requirements.

## Post-Training Quantization Options

* Post-training FP16 quantization
``` python
# Convert to model with FP16 weights and FP32 activations
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.target_spec.supported_types = [tf.float16]
converter.target_spec._experimental_supported_accumulation_type = tf.dtypes.float16
fc_fp16 = converter.convert()
save_litert_model(fc_fp16, "fc_fp16.tflite")
```

This method applies FP16 quantization to a model with FP32 operators. In practice, this optimization adds metadata to the model to indicate that the model is compatible with FP16 inference. With this hint, at runtime, XNNPACK replaces the FP32 operators with their FP16 equivalents. It also inserts additional operators that convert the model inputs from FP32 to FP16, and convert the model outputs from FP16 back to FP32. 

KleidiAI provides FP16 packing micro-kernels for both the activations and weights matrix, as well as FP16 matrix multiplication micro-kernels.

* Post-training INT8 dynamic range quantization
``` python
# Convert to Dynamically Quantized INT8 model (INT8 weights, FP32 activations)
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
fc_int8_dynamic = converter.convert()
save_litert_model(fc_int8_dynamic, "fc_dynamic_int8.tflite")
```

This quantization method optimizes operators with large parameter sizes by quantizing their weights to INT8 while keeping the activations in the FP32 data format.

KleidiAI provides micro-kernels that dynamically quantize activations to INT8 at runtime. KleidiAI also provides packing micro-kernels for the weights matrix, as well as INT8 matrix multiplication micro-kernels that produce FP32 outputs.


* Post-training INT8 static quantization
``` python
def fake_dataset():
    for _ in range(100):
        sample = np.random.rand(input_size).astype(np.float32)
        yield [sample]
# Convert to Statically Quantized INT8 model (INT8 weights and activations)
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter.target_spec.supported_types = [tf.int8]
converter.inference_input_type = tf.int8
converter.inference_output_type = tf.int8
converter.representative_dataset = fake_dataset
fc_int8_static = converter.convert()
save_litert_model(fc_int8_static, "fc_static_int8.tflite")
```

This quantization method quantizes both the activations and the weights to INT8.

KleidiAI provides INT8 packing micro-kernels for both the activations and weights matrix, as well as INT8 matrix multiplication micro-kernels.
