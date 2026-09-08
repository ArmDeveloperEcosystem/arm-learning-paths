---
title: Verify on-device text generation
description: Check generated responses, record the deployment configuration, and confirm that inference still works offline.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Check two different prompts

Run the loaded model with two short prompts:

```text
What is the capital of France?
```

```text
Summarize this in one sentence: Solar panels convert sunlight into electricity and can reduce household energy bills.
```

The responses should be relevant and readable. Generated wording can vary, so validate the meaning rather than expecting an exact string. The result shouldn't include prompt echoes, role markers, tokenizer control tokens, or runtime diagnostics.

## Confirm offline execution

Enable airplane mode or otherwise disconnect the phone from the network, then run another prompt. The application should still load the package from application-private storage and generate text.

This confirms that the application isn't sending prompts to a remote inference service. Re-enable the network after completing the check if you need it for other applications.

## Record the deployment

Record the information needed to reproduce or compare the result:

- Model repository and artifact filename
- Runtime and pinned Android dependency version
- Adapter example and model catalog entry
- Android phone model and Android version
- Prompt, generated response, model load time, and run time
- Whether the offline check passed

Don't compare the timings of the supplied examples as if only the runtime changed. Their model architecture, size, quantization, tokenizer, and runtime also differ.

## Resolve common problems

Use the following reference to resolve common problems:

| Problem | Check |
| --- | --- |
| Model file reports missing | Confirm that the application-private directory name matches the catalog `id` and that every required file was copied. |
| Model fails during load | Confirm the artifact matches the adapter and pinned runtime dependency. |
| Generated text is empty or malformed | Check the tokenizer, prompt template, stop tokens, and output sanitization. |
| ONNX model reports missing data | Preserve `model.onnx`, its external data, runtime configuration, tokenizer files, and chat template in one directory. |
| Application runs out of memory | Use the smaller SmolLM2 default, reduce the input or output length, or use a phone with more available memory. |
| Runtime initialization fails | Confirm the Android version, device ABI, native libraries, and backend requirements from the model card. |

## What you've accomplished and what's next

You've validated more than one generated response and confirmed that inference runs locally without network access. Additionally, you've recorded the model, runtime, device, and timing information needed to reproduce the deployment.

Next, you'll learn how to extend the application for another model.
