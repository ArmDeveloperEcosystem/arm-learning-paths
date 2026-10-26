---
title: (Optional) Explore other cloud LLM deployment options
description: Compare runtimes, model formats, and Arm cloud machines when the ONNX Runtime GenAI workflow does not fit your deployment.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Identify the components you might replace

You've run an Arm AI Portal model using ONNX Runtime GenAI and inspected the scripts behind the workflow. That stack is one way to deploy text generation on an Arm cloud machine, but another model format, serving requirement, or operational constraint might lead you to a different runtime.

The supplied adapter uses ONNX Runtime GenAI, but the same deployment components apply to packages that use other model formats and runtimes. Assess which application components need to change for an alternative package.

A cloud text-generation application needs more than model weights. The model format must match the inference runtime. The tokenizer must match the model, and the host must provide enough memory and supported CPU instructions. You also need a way to submit prompts and return generated tokens.

The ONNX Runtime GenAI example supplies one choice for each component in the deployment. If you adapt the application, identify which parts can stay and which parts need to change:

| Component | Purpose | Where to get it |
| --- | --- | --- |
| Model artifact | Contains the trained weights in a runtime-compatible format such as ONNX, GGUF, or Safetensors | Select and download the model from the [Arm AI Portal](https://developer.arm.com/ai/models) |
| Model configuration | Describes the model architecture, tensor names, generation settings, and special tokens | Included with the selected Arm AI Portal model package |
| Tokenizer and prompt template | Converts text to token IDs and formats prompts for instruction-tuned or base models | Included with the selected Arm AI Portal model package |
| Inference runtime | Loads the model, manages token generation, and selects the CPU execution path | The runtime project's package registry, container registry, or source repository |
| Serving interface | Exposes the model through a command line, web application, or HTTP API | Included with the runtime or added by your application |
| Arm compute | Supplies CPU cores, memory, storage, and network access | An Arm-based cloud virtual machine or Arm Neoverse server |
| Operational controls | Add authentication, health checks, logging, metrics, and request limits | Your application and cloud platform services |

The selected Arm AI Portal package supplies the model artifact, configuration, tokenizer, and prompt template. Keep these files together because a tokenizer or chat template from a different model revision can generate incorrect token IDs or prompt formatting even when the runtime loads the weights successfully.

## Compare alternative self-managed runtimes

The inference runtime is the component that's most likely to change when you select another model format. Each runtime expects a particular artifact format and package layout.

| Runtime | Compatible Arm AI Portal package | Where to get the runtime | Common use |
| --- | --- | --- | --- |
| ONNX Runtime GenAI | ONNX graph, `genai_config.json`, tokenizer files, and an optional chat template | [ONNX Runtime GenAI installation documentation](https://onnxruntime.ai/docs/genai/howto/install.html) | Quantized CPU inference with explicit control over prompt preparation and token generation |
| `llama.cpp` | A GGUF model and tokenizer metadata, when offered for the selected model | [`llama.cpp` source, binaries, and server](https://github.com/ggml-org/llama.cpp) | Lightweight local or cloud CPU inference with a command line or OpenAI-compatible server |
| vLLM | A model package supported by vLLM, when offered for the selected model | [vLLM CPU installation documentation](https://docs.vllm.ai/en/stable/getting_started/installation/cpu/) | Throughput-oriented serving and concurrent API requests |
| Transformers | Model weights, configuration, tokenizer, and optional chat template, when offered for the selected model | [Transformers installation documentation](https://huggingface.co/docs/transformers/installation) | Prototyping, compatibility checks, and direct Python inference |

Artifact formats aren't interchangeable. For example, an ONNX Runtime GenAI application can't load a GGUF file directly, and `llama.cpp` doesn't use an ONNX model bundle. In the Arm AI Portal, select a package prepared for the runtime that you plan to use.

## Compare Arm CPU optimization support

The supplied ONNX Runtime path can select KleidiAI kernels automatically for compatible operations. Other runtimes handle KleidiAI differently:

- For `llama.cpp`, build with `GGML_CPU_KLEIDIAI=ON` to include the KleidiAI CPU backend. The runtime then [selects applicable kernels based on detected CPU features](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md#arm-kleidiai).
- For PyTorch, supported low-bit TorchAO operators can use [dynamic kernel selection with KleidiAI](https://pytorch.org/blog/advancing-low-bit-operators-in-pytorch-and-executorch-dynamic-kernel-selection-kleidiai-and-quantized-tied-embeddings/).

Runtime support alone doesn't guarantee KleidiAI dispatch. The following additional factors need to be compatible:

- Runtime build
- Model operators
- Quantization
- Tensor shapes
- Processor features

Check the selected runtime and package before making performance assumptions.

## What you've learned

You can now compare the completed ONNX Runtime GenAI workflow with other self-managed runtimes. You can identify which model, runtime, serving, or operational component needs to change for another cloud LLM deployment.

Using that information, you can extend the workflow to use other runtimes.
