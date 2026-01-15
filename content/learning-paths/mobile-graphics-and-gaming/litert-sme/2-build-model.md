---
title: Create LiteRT models
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## KleidiAI SME2 support in LiteRT

LiteRT uses XNNPACK as its default CPU backend. KleidiAI micro-kernels are integrated through XNNPACK in LiteRT. Only a subset of KleidiAI SME2 micro-kernels has been integrated into XNNPACK. These micro-kernels support operators using the following data types and quantization configurations in the LiteRT model. Other operators use XNNPACK's default implementation during inference.

### Supported operator configurations

#### Fully Connected:

| Activations                  | Weights                                 | Output                       |
| ---------------------------- | --------------------------------------- | ---------------------------- |
| FP32                         | FP32                                    | FP32                         |
| FP32                         | FP16                                    | FP32                         |
| FP32                         | Per-channel symmetric INT8 quantization | FP32                         |
| Asymmetric INT8 quantization | Per-channel symmetric INT8 quantization | Asymmetric INT8 quantization |
| FP32                         | Per-channel symmetric INT4 quantization | FP32                         |

#### Batch matrix multiply:

| Input A | Input B                                 |
| ------- | --------------------------------------- |
| FP32    | FP32                                    |
| FP16    | FP16                                    |   
| FP32    | Per-channel symmetric INT8 quantization |

#### Conv2D:

| Activations                  | Weights                                               | Output                       |
| ---------------------------- | ----------------------------------------------------- | ---------------------------- |
| FP32                         | FP32                                                  | FP32                         |
| FP32                         | FP16                                                  | FP32                         |
| FP32                         | Per-channel or per-tensor symmetric INT8 quantization | FP32                         |
| Asymmetric INT8 quantization | Per-channel or per-tensor symmetric INT8 quantization | Asymmetric INT8 quantization |

#### TransposeConv:

| Activations                  | Weights                                               | Output                       |
| ---------------------------- | ----------------------------------------------------- | ---------------------------- |
| Asymmetric INT8 quantization | Per-channel or per-tensor symmetric INT8 quantization | Asymmetric INT8 quantization |


## Create LiteRT models using Keras

To demonstrate SME2 acceleration on Android, you will construct simple single-layer models (for example, fully connected) using Keras and convert them into LiteRT (`.tflite`) format. This allows you to benchmark isolated operators and directly observe SME2 improvements.

Install the TensorFlow package dependency for your script:

```bash
sudo pip3 install tensorflow
```

Save the following script as `model.py`:

```python
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

Run the script:

```bash
python3 model.py
```

The model `fc_fp32.tflite` is created in FP32 format. As mentioned above, this operator can invoke the KleidiAI SME2 micro-kernel for acceleration.

You can then use Android Debug Bridge (ADB) to push the model for benchmarking to your Android device:

```bash
adb push fc_fp32.tflite /data/local/tmp/
adb shell chmod +x /data/local/tmp/fc_fp32.tflite
```

You can also optimize this Keras model using post-training quantization to create a LiteRT model that suits your requirements.

## Post-training quantization options

**Post-training FP16 quantization**

```python
# Convert to model with FP16 weights and FP32 activations
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.target_spec.supported_types = [tf.float16]
converter.target_spec._experimental_supported_accumulation_type = tf.dtypes.float16
fc_fp16 = converter.convert()
save_litert_model(fc_fp16, "fc_fp16.tflite")
```

This method applies FP16 quantization to a model with FP32 operators. In practice, this optimization adds metadata to the model to indicate that the model is compatible with FP16 inference. At runtime, XNNPACK replaces the FP32 operators with their FP16 equivalents and inserts additional operators to convert the model inputs from FP32 to FP16 and outputs from FP16 back to FP32.

KleidiAI provides FP16 packing micro-kernels for both the activations and weights matrix, as well as FP16 matrix multiplication micro-kernels.

**Post-training INT8 dynamic range quantization**

```python
# Convert to dynamically quantized INT8 model (INT8 weights, FP32 activations)
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
fc_int8_dynamic = converter.convert()
save_litert_model(fc_int8_dynamic, "fc_dynamic_int8.tflite")
```

This quantization method optimizes operators with large parameter sizes by quantizing their weights to INT8 while keeping the activations in the FP32 data format.

KleidiAI provides micro-kernels that dynamically quantize activations to INT8 at runtime, as well as packing micro-kernels for the weights matrix and INT8 matrix multiplication micro-kernels that produce FP32 outputs.

**Post-training INT8 static quantization**

```python
def fake_dataset():
    for _ in range(100):
        sample = np.random.rand(input_size).astype(np.float32)
        yield [sample]
# Convert to statically quantized INT8 model (INT8 weights and activations)
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

## What you've accomplished and what's next
You have now created several LiteRT models with different quantization options, ready for benchmarking on your Arm-based Android device. You have:

- Built a simple Keras model and converted it to LiteRT (`.tflite`) format
- Generated models with different quantization types: FP32, FP16, INT8 dynamic, and INT8 static
- Learned how each quantization method affects model size, performance, and compatibility with KleidiAI SME2 micro-kernels

Now that you have created and converted your models, you can benchmark them on your Android device to measure the performance gains from SME2 acceleration. Consider experimenting with additional layers such as Conv2D, BatchMatMul, or TransposeConv to further explore SME2 support for different operators. You can also apply more quantization and optimization techniques to enhance model efficiency. Finally, integrate your optimized models into your Android applications to leverage Arm SME2 acceleration in real-world use cases.

By following these steps, you can maximize the performance of your machine learning models on Arm-based devices using LiteRT and KleidiAI SME2.
