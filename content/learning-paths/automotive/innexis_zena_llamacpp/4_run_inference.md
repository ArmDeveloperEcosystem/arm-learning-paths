---
title: Run CPU inference and inspect the result
description: Run llama.cpp with a verified model and confirm that the Zena CSS guest generates text on its CPU.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run CPU inference and inspect the result

Run a short text prompt with the binary and model you prepared. 

## Run a text-generation smoke test

Create a results directory and save the prompt beside the application output:

Run the following command on the **Zena Linux guest**. It requests zero GPU layers with `-ngl 0` and saves both the log and exit code:

```bash
LP2_LLAMA_CLI="$LP2_WORK_DIR/llama.cpp/build/bin/llama-cli"

"$LP2_LLAMA_CLI" \
    -m "$LP2_MODEL_FILE" \
    -t 4 -tb 4 -ngl 0 -c 512 -n 128 --temp 0 --seed 42 \
    --single-turn --simple-io \
    -p 'Write one short sentence about a virtual platform.'
```

The standard output should show a message similar to the following.

```output
build      : b12790-436d7e81c
model      : /root/zena-llamacpp/models/qwen2.5-0.5b-instruct-q4_0.gguf
ftype      : Q4_0
modalities : text

> Write one short sentence about a virtual platform.
A virtual platform is a platform that allows users to create and share digital content, such as images, videos, and documents, in a virtual environment.

Exiting...
```

If either option is missing you may need to rebuild llama.cpp from an earlier commit as per the commented instruction in the build llama.cpp section.

The CPU-only build also reported that no usable GPU was found. This warning did not prevent inference. This request is a functional smoke test. The recorded answer used the general meaning of "virtual platform", so it is not a definition of an automotive Virtual SoC or a test of answer quality.

If model loading fails, check the hash and available memory before changing model or runtime settings. Save the failing log and exit code; a changed model or command is a new test condition.

## Change the prompt

Keep the same Zena virtual platform, llama.cpp binary, GGUF file, and runtime flags. Change only the prompt, then compare the two recorded requests. This is a controlled input iteration, not a source-code modification or a performance comparison.

## Run the second request

Save the changed prompt and run the same CPU command in the **guest shell**:

```bash
"$LP2_LLAMA_CLI" \
    -m "$LP2_MODEL_FILE" \
    -t 4 -tb 4 -ngl 0 -c 512 -n 128 --temp 0 --seed 42 \
    --single-turn --simple-io \
    -p 'Write one short sentence about an automotive dashboard.'
```

The second tested Zena request used the same command options and model path with only the prompt changed. Its saved exit code was `0`, and the standard output included:

```output
build      : b12790-436d7e81c
model      : /root/zena-llamacpp/models/qwen2.5-0.5b-instruct-q4_0.gguf
ftype      : Q4_0
modalities : text

> Write one short sentence about an automotive dashboard.
An automotive dashboard is a crucial component of a vehicle's interface, displaying crucial information such as speed, distance, fuel consumption, and other critical data to the driver.

Exiting...
```

The two requests demonstrate that the guest application accepted different prompts and generated text. Their output does not establish answer quality or provide a controlled performance comparison. Your generated wording may differ.

## What you have learned

You built and ran a CPU text workload and preserved evidence for two controlled requests. The result supports functional bring-up on the tested ANA Zena CSS configuration. It does not predict physical-silicon throughput, prove model-answer quality, or show GPU or NPU execution.

