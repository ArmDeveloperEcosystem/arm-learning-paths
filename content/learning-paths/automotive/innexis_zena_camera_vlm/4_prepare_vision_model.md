---
title: Prepare a vision-capable model
description: Check the llama.cpp binary from the preceding Learning Path and download matching model and projector files in the Zena CSS guest.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare a vision-capable model

Use the llama.cpp binary you checked on page 1. This page adds the two files needed for image inference: a vision-language model and its matching multimodal projector (`mmproj`). See the [llama.cpp multimodal documentation](https://github.com/ggml-org/llama.cpp/blob/master/docs/multimodal.md).

### Check image support and guest capacity

The binary check on page 1 confirmed that `llama-cli` runs. In the **same guest**, check that it accepts image and projector options, then check free storage and memory:

```bash
WORK_DIR=/root/zena-camera-vlm ; LLAMA_CLI=/root/zena-llamacpp/llama.cpp/build/bin/llama-cli ; mkdir -p "$WORK_DIR/models" "$WORK_DIR/results" && test -x "$LLAMA_CLI" && "$LLAMA_CLI" --help > "$WORK_DIR/results/llama-help.txt" 2>&1 && grep -F -- '--image' "$WORK_DIR/results/llama-help.txt" && grep -F -- '--mmproj' "$WORK_DIR/results/llama-help.txt" && grep -F -- '--no-mmproj-offload' "$WORK_DIR/results/llama-help.txt" ; printf 'Vision option check status: %s\n' "$?" ; df -h "$WORK_DIR" ; grep -E '^(MemTotal|MemAvailable):' /proc/meminfo
```

The reported check returned status `0` and found all three options. That guest had 23 GB free on `/` and `MemAvailable: 7810760 kB`. These values confirm the tested environment; check the values in your current guest before downloading.

If an option is missing, stop and record the binary version and help output. The two downloads total about 546 MB.

### Download the model and projector

Use the Q8_0 model and projector from the [SmolVLM2-500M GGUF repository](https://huggingface.co/ggml-org/SmolVLM2-500M-Video-Instruct-GGUF/tree/ccd7aae53bcb1997355c2f094959e72b3642ce17), which lists Apache-2.0 licensing. Both downloads are pinned to revision `ccd7aae53bcb1997355c2f094959e72b3642ce17`, which contains the matching pair. The repository provides SHA-256 values for the [model](https://huggingface.co/ggml-org/SmolVLM2-500M-Video-Instruct-GGUF/blob/ccd7aae53bcb1997355c2f094959e72b3642ce17/SmolVLM2-500M-Video-Instruct-Q8_0.gguf) and [projector](https://huggingface.co/ggml-org/SmolVLM2-500M-Video-Instruct-GGUF/blob/ccd7aae53bcb1997355c2f094959e72b3642ce17/mmproj-SmolVLM2-500M-Video-Instruct-Q8_0.gguf).

Download the model **inside the guest**. The command verifies the `.part` file before giving it the final filename:

```bash
WORK_DIR=/root/zena-camera-vlm ; MODEL_REV=ccd7aae53bcb1997355c2f094959e72b3642ce17 ; MODEL_FILE="$WORK_DIR/models/SmolVLM2-500M-Video-Instruct-Q8_0.gguf" ; mkdir -p "$WORK_DIR/models" && wget -nv -O "$MODEL_FILE.part" "https://huggingface.co/ggml-org/SmolVLM2-500M-Video-Instruct-GGUF/resolve/$MODEL_REV/SmolVLM2-500M-Video-Instruct-Q8_0.gguf" && printf '6f67b8036b2469fcd71728702720c6b51aebd759b78137a8120733b4d66438bc  %s\n' "$MODEL_FILE.part" | sha256sum -c - && mv "$MODEL_FILE.part" "$MODEL_FILE" && ls -lh "$MODEL_FILE" ; printf 'Model download status: %s\n' "$?"
```

The reported model download passed its hash check and exited `0`; `ls -lh` showed 417 MiB.

Download the matching projector in the **same guest**:

```bash
WORK_DIR=/root/zena-camera-vlm ; MODEL_REV=ccd7aae53bcb1997355c2f094959e72b3642ce17 ; MMPROJ_FILE="$WORK_DIR/models/mmproj-SmolVLM2-500M-Video-Instruct-Q8_0.gguf" ; wget -nv -O "$MMPROJ_FILE.part" "https://huggingface.co/ggml-org/SmolVLM2-500M-Video-Instruct-GGUF/resolve/$MODEL_REV/mmproj-SmolVLM2-500M-Video-Instruct-Q8_0.gguf" && printf '921dc7e259f308e5b027111fa185efcbf33db13f6e35749ddf7f5cdb60ef520b  %s\n' "$MMPROJ_FILE.part" | sha256sum -c - && mv "$MMPROJ_FILE.part" "$MMPROJ_FILE" && ls -lh "$MMPROJ_FILE" ; printf 'Projector download status: %s\n' "$?"
```

The projector also passed its hash check and exited `0`; `ls -lh` showed 104 MiB. Continue only when both files have passed.

## What you have learned

You have a vision-capable binary and a verified model/projector pair. Next, run inference on the captured frame.
