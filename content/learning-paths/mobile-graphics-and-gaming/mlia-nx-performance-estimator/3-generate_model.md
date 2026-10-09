---
title: Download and convert a public baseline model
description: Download a public quantized MobileNet V1 classifier, verify its checksum, and convert the LiteRT model to TOSA before MLIA analysis.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Choose a pretrained baseline

Use `mobilenet_v1_0.25_224_quant.tflite` from the [TensorFlow MobileNet V1 model catalog](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md). It's a public pretrained image classifier with a width multiplier of `0.25` and a fixed input shape of `[1, 224, 224, 3]`.

The model has quantized eight-bit weights and activations, with unsigned eight-bit input and output tensors. It isn't a neural upscaling model, but provides a real convolutional workload for learning the MLIA analysis workflow. You download the existing quantized export rather than retraining or calibrating a model.

## Download and verify the model

From `mlia-demo`, create directories for models and reports, download the versioned public archive, and extract only the LiteRT model:

```bash
mkdir -p mlia-demo-models runs
curl --fail --location \
  https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_0.25_224_quant.tgz \
  --output mlia-demo-models/mobilenet_v1_0.25_224_quant.tgz
tar -xzf mlia-demo-models/mobilenet_v1_0.25_224_quant.tgz \
  -C mlia-demo-models ./mobilenet_v1_0.25_224_quant.tflite
printf '%s  %s\n' \
  ce8f61fe3e4e29560c4ea8038e4b91eb354be330fc428348b9645bd1e7de03bf \
  mlia-demo-models/mobilenet_v1_0.25_224_quant.tflite \
  | sha256sum --check
```

The expected final output is:

```output
mlia-demo-models/mobilenet_v1_0.25_224_quant.tflite: OK
```

Keep the model in your working directory. No model binaries need to be added to the Learning Paths repository.

## Convert the model before analysis

Use the converter installed with `mlia-converters-litert` to create a textual TOSA MLIR artifact. Preserve debug locations to help associate analysis results with source operators:

```bash
tosa-converter-for-tflite \
  mlia-demo-models/mobilenet_v1_0.25_224_quant.tflite \
  --text --emit-debug-info \
  -o mlia-demo-models/baseline.tosamlir
test -s mlia-demo-models/baseline.tosamlir
```

The output is similar to:

```output
[WARNING] Debug info emission is enabled; output size and conversion time may increase significantly for large models.
[INFO] TOSA MLIR (text) written to: mlia-demo-models/baseline.tosamlir
```

Use the `.tosamlir` extension for textual TOSA MLIR. A `.tosa` FlatBuffer is a different serialization; don't rename this text file to imply that it's a FlatBuffer. If conversion fails, resolve that failure before starting MLIA analysis.

## What you've accomplished and what's next

You've downloaded and verified a public quantized baseline, then converted it to TOSA. Next, you'll install the bundled estimator and check whether the model's operators are supported.
