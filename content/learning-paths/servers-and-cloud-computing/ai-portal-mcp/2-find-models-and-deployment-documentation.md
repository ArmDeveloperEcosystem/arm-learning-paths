---
title: Find models and deployment paths with natural-language prompts
description: Search, compare, and inspect Arm AI Portal models, then find documentation for deploying them on Arm-based targets.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---
<style>
pre.language-text,
code.language-text {
    white-space: pre-wrap;
    overflow-wrap: anywhere;
}
</style>

## Explore the model catalog

The Arm AI Portal MCP server translates natural-language questions into searches and filters. You can ask for anything that you'd normally search for in the AI Portal using a free-text query. Start with your goal, then add constraints such as the task, target, runtime, latency, and memory.

The following is an example of how you can query the AI Portal MCP server. Start with a broad question when you don't yet know which model task you need:

```text
What types of models are available on the Arm AI Portal?
```

The harness searches the AI Portal catalogue and groups the results by tasks such as image classification, object detection, text generation, and speech recognition. Follow up with a task to narrow the results.

You can ask for the model with the highest evaluation score:

```text
Which image classification model has the highest evaluation score?
```
The output is similar to:

```output
• The highest-scoring image-classification model is ViT-Base/16 (timm augreg) INT8 — LiteRT.

  - Evaluation score: 84.22% Top-1
  - Dataset: ImageNet-1k
  - Target hardware: Vivo X300
  - Runtime: LiteRT/TFLite
```
Evaluation scores are comparable only when the dataset, evaluation type, and unit match. A good response states these fields and avoids comparing results measured with different methods or on different targets.

## Add performance and target constraints

Ask for a sorted result when one metric matters most:

```text
Which image classification model has the lowest measured latency? Include the target, runtime, score, and memory usage.
```

Latency depends on the target hardware and benchmark configuration. For a useful comparison, include the target or ask the assistant to compare only results from the same target:

```text
Compare image classification models optimized for Raspberry Pi 5. Sort them by latency and show the Top-1 score and peak memory for each model.
```

You can also start with the device:

```text
Which models are optimized for Raspberry Pi 5? Group them by task and runtime.
```

The assistant applies the catalog's target filter and returns model-target combinations with published evidence. A target name in a model description isn't enough to establish compatibility, so ask for models that are explicitly optimized for that target.

Other useful metric prompts include:

```text
Find object-detection models for Raspberry Pi 5 that use less than 120 MB of peak memory. Sort the results by latency.
```

```text
Show text-generation models optimized for AWS Graviton G4. Include model size, runtime, MMLU evaluation settings, and measured latency.
```

## Inspect a specific model

For expanded information about a specific model, ask for its details using the full model name where possible:

```text
Give me more details about ResNet-18 INT8 with ExecuTorch and XNNPACK for Raspberry Pi 5. Include its artifact, license, runtime configuration, input resolution, and benchmark setup.
```
The output looks similar to:

```output
• ResNet-18 INT8 — ExecuTorch + XNNPACK is an INT8-quantized image-classification model optimized by Arm for Raspberry Pi 5.

  - Artifact: ExecuTorch .pte model (https://huggingface.co/Arm/resnet-18-int8-xnnpack-executorch/blob/main/resnet-18-int8-executorch.pte)
  - Artifact size: 11,784,945 bytes (about 11.24 MiB)
  - License: Apache 2.0 (https://spdx.org/licenses/Apache-2.0.html)
  - Base model: microsoft/resnet-18
  - Input: 224 × 224 RGB image with ImageNet normalization
  - Output: classification logits for top-k prediction

  Runtime configuration:

  - ExecuTorch 1.1.0
  - CPU backend
  - XNNPACK and KleidiAI optimizations
  - 100% operator delegation
  - Batch size: 1

  Benchmark setup:

  - Target: Raspberry Pi 5
  - CPU: 4-core Arm Cortex-A76 (arm64)
  - Dataset: ImageNet-1k validation set
  - Samples: 50,000
  - Warm-up runs: 10
  - Measured runs: 100
  - Latency: 8.818 ms
  - Accuracy: 69.57% Top-1
  - Average memory: 23.97 MB
  - Peak memory: 23.97 MB
```

The assistant first resolves the catalog model ID, then retrieves detailed metadata. Depending on the model, the response can include provenance, base models, licenses, training datasets, and Arm-optimized benchmark configurations.

Use a comparison prompt before choosing between similar models:

```text
Compare the Raspberry Pi 5 variants of ResNet-18 INT8 and MobileNetV3-Small INT8. Explain the latency, Top-1 score, peak-memory, and model-size trade-offs using matching evaluation data.
```

## Describe a use case

You can describe the task instead of naming a model:

```text
I need a vision model to detect agricultural objects at the edge. Which model and Arm target should I consider? Ask me for any missing accuracy, latency, power, camera, or connectivity constraints before recommending a deployment.
```

The catalogue might contain a general object detector rather than an agriculture-specific model. The assistant should distinguish a potential starting point from a verified fit and ask for the details needed to refine the recommendation.

For a more constrained recommendation, specify the environment and success criteria:

```text
Recommend an object-detection model for a Raspberry Pi 5 with less than 600 ms measured latency and less than 128 MB peak memory. Compare only COCO 2017 mAP results and explain the runtime requirements.
```

## Find deployment paths

The server can search AI Portal documentation for deployment paths that match a model, task, or target. Ask the assistant to summarize the deployment goal of each result so that you can identify the most relevant guide:

```text
Find relevant documentation for running Llama models on AWS Graviton. Summarize the deployment goal of each result and provide its link.
```

Refine the prompt with a runtime or framework when you need a more specific deployment path:

```text
Suggest a deployment path for running image classification model on Raspberry Pi 5 with ExecuTorch. 
```

The assistant recommends relevant deployment paths for you to review; it does not run the deployment steps. Before choosing a guide, confirm that its model, target, runtime, and prerequisites match your selected model-target pair.

## Use flexible search terms

The model and documentation searches use Typesense full-text search. Free-text queries are typo tolerant, so short forms and small spelling mistakes can still produce useful matches. For example:

```text
Find low-latency image classifiers for rpi.
```

## What you've accomplished

You've used the MCP server to explore models on the AI Portal, filter by deployment constraints, inspect a model, and find related documentation. 
