---
title: Download a public baseline model
description: Download a public quantized MobileNet V1 classifier, verify its checksum, and prepare it for direct analysis with MLIA.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Choose a pretrained baseline

Use `mobilenet_v1_0.25_224_quant.tflite` from the [TensorFlow MobileNet V1 model catalog](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md). It's a public pretrained image classifier with a width multiplier of `0.25` and a fixed input shape of `[1, 224, 224, 3]`.

The model has quantized eight-bit weights and activations, with unsigned eight-bit input and output tensors. It isn't a neural upscaling model. However, it provides a real convolutional workload for learning the Arm ML Inference Advisor (MLIA) analysis workflow. You download the existing quantized export rather than retraining or calibrating a model.

## Download and verify the model

From `mlia-demo`, download the versioned public archive, and extract the LiteRT model. Name your local copy `baseline.tflite`:

```bash
mkdir -p models runs
curl -fL https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_0.25_224_quant.tgz -o models/baseline.tgz
tar -xzf models/baseline.tgz -C models ./mobilenet_v1_0.25_224_quant.tflite
mv models/mobilenet_v1_0.25_224_quant.tflite models/baseline.tflite
echo "ce8f61fe3e4e29560c4ea8038e4b91eb354be330fc428348b9645bd1e7de03bf  models/baseline.tflite" | sha256sum --check
```

The expected final output is:

```output
models/baseline.tflite: OK
```

MLIA runs the installed converter and saves the intermediate artifacts with its reports. Keep the downloaded model in your working directory. 

## What you've accomplished and what's next

You've downloaded and verified the quantized MobileNet baseline. 

Next, you'll check whether its operators are supported by passing `models/baseline.tflite` directly to MLIA.
