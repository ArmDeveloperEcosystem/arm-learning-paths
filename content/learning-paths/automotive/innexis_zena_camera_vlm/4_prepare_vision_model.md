---
title: Prepare a vision-capable model
description: Check the llama.cpp binary from the preceding Learning Path and download matching model and projector files in the Zena CSS guest.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up the vision-language model

Now that you've established an input image, you can prepare the vision-language model (VLM) to analyze the image. 

Use the `llama-cli` binary that you built in the [llama.cpp Learning Path](/learning-paths/automotive/innexis_zena_llamacpp/) and verified earlier. You'll add the two files needed for image inference: a vision-language model and its matching multimodal projector (`mmproj`). For more information, see the [llama.cpp multimodal documentation](https://github.com/ggml-org/llama.cpp/blob/master/docs/multimodal.md).

### Check guest capacity

Prepare the model and results directories, then report available guest storage and memory:

```bash
WORK_DIR=/root/zena-camera-vlm
LLAMA_CLI=/root/zena-llamacpp/llama.cpp/build/bin/llama-cli
mkdir -p "$WORK_DIR/models" "$WORK_DIR/results" &&
df -h "$WORK_DIR" &&
grep -E '^(MemTotal|MemAvailable):' /proc/meminfo
```

The output is similar to:

```output
Filesystem      Size  Used Avail Use% Mounted on
/dev/root        28G  5.4G   21G  21% /
MemTotal:        8120232 kB
MemAvailable:    7812240 kB
```
Ensure that you have at least 0.6G of free capacity to download the models.

### Download the model and projector

Use the Q8_0 model and projector from the [SmolVLM2-500M GGUF repository](https://huggingface.co/ggml-org/SmolVLM2-500M-Video-Instruct-GGUF/tree/ccd7aae53bcb1997355c2f094959e72b3642ce17), which lists Apache-2.0 licensing. Both downloads are pinned to revision `ccd7aae53bcb1997355c2f094959e72b3642ce17`, which contains the matching pair. The repository provides SHA-256 values for the [model](https://huggingface.co/ggml-org/SmolVLM2-500M-Video-Instruct-GGUF/blob/ccd7aae53bcb1997355c2f094959e72b3642ce17/SmolVLM2-500M-Video-Instruct-Q8_0.gguf) and [projector](https://huggingface.co/ggml-org/SmolVLM2-500M-Video-Instruct-GGUF/blob/ccd7aae53bcb1997355c2f094959e72b3642ce17/mmproj-SmolVLM2-500M-Video-Instruct-Q8_0.gguf).

Download the model inside the Linux guest OS:

```bash
WORK_DIR=/root/zena-camera-vlm ; MODEL_REV=ccd7aae53bcb1997355c2f094959e72b3642ce17 ; MODEL_FILE="$WORK_DIR/models/SmolVLM2-500M-Video-Instruct-Q8_0.gguf" ; mkdir -p "$WORK_DIR/models" && wget -nv -O "$MODEL_FILE.part" "https://huggingface.co/ggml-org/SmolVLM2-500M-Video-Instruct-GGUF/resolve/$MODEL_REV/SmolVLM2-500M-Video-Instruct-Q8_0.gguf" && printf '6f67b8036b2469fcd71728702720c6b51aebd759b78137a8120733b4d66438bc  %s\n' "$MODEL_FILE.part" | sha256sum -c - && mv "$MODEL_FILE.part" "$MODEL_FILE" && ls -lh "$MODEL_FILE" ; printf 'Model download status: %s\n' "$?"
```
The command verifies the `.part` file before giving it the final filename.

The output is similar to:

```output
Model download status: 0
```

Download the matching projector in the same Linux guest OS:

```bash
WORK_DIR=/root/zena-camera-vlm ; MODEL_REV=ccd7aae53bcb1997355c2f094959e72b3642ce17 ; MMPROJ_FILE="$WORK_DIR/models/mmproj-SmolVLM2-500M-Video-Instruct-Q8_0.gguf" ; wget -nv -O "$MMPROJ_FILE.part" "https://huggingface.co/ggml-org/SmolVLM2-500M-Video-Instruct-GGUF/resolve/$MODEL_REV/mmproj-SmolVLM2-500M-Video-Instruct-Q8_0.gguf" && printf '921dc7e259f308e5b027111fa185efcbf33db13f6e35749ddf7f5cdb60ef520b  %s\n' "$MMPROJ_FILE.part" | sha256sum -c - && mv "$MMPROJ_FILE.part" "$MMPROJ_FILE" && ls -lh "$MMPROJ_FILE" ; printf 'Projector download status: %s\n' "$?"
```

The output is similar to:

```output
Projector download status: 0
```

## What you've accomplished and what's next

You've set up a vision-capable binary and a verified model and projector pair. 

Next, you'll run inference on the captured frame.
