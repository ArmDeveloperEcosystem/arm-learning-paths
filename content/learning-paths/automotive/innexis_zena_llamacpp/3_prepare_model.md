---
title: Prepare and verify a text model
description: Download a pinned GGUF text model and verify its size and SHA-256 checksum in the Zena CSS guest.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare and verify a text model

Use one small GGUF text model so you can focus on application bring-up. The tested Zena run used the [Qwen2.5 0.5B Instruct Q4_0 GGUF file](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF/blob/main/qwen2.5-0.5b-instruct-q4_0.gguf). The publisher lists an Apache-2.0 license and SHA-256 value for this file. The downloaded file matched that hash before inference.

Use the file's [full upload commit](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF/commit/6dd44a1fb35d11b5d1b28902876ce3cc9e882d0e) instead of the moving `main` branch. The file in the tested Zena run was 428,730,208 bytes. Verify its hash in your guest before loading it.

## Choose the model location

Use the work filesystem checked on the first page. Make sure it still has room for a temporary download and the complete model:

```bash
LP2_MODEL_DIR="$LP2_WORK_DIR/models"
mkdir -p "$LP2_MODEL_DIR"
df -h "$LP2_MODEL_DIR"
LP2_MODEL_FILE="$LP2_MODEL_DIR/qwen2.5-0.5b-instruct-q4_0.gguf"
```

In the tested Zena guest, the model directory was created and its filesystem reported:

```output
Filesystem      Size  Used Avail Use% Mounted on
/dev/root        28G  2.9G   23G  12% /
```

These figures describe the guest before the model download.

## Obtain the fixed model file

If this guest can reach Hugging Face, download the file from the fixed repository revision:

```bash
LP2_MODEL_REV=6dd44a1fb35d11b5d1b28902876ce3cc9e882d0e
wget -q -O "$LP2_MODEL_FILE.part" \
    "https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF/resolve/$LP2_MODEL_REV/qwen2.5-0.5b-instruct-q4_0.gguf?download=true" &&
    mv "$LP2_MODEL_FILE.part" "$LP2_MODEL_FILE"
printf 'Download exit status: %s\n' "$?"
```

The fixed-revision download in the tested Zena guest completed with:

```output
Download exit status: 0
```

Continue only if the download exit status is `0`. A successful download command does not establish that the file has the expected contents; check it below.

If the guest cannot download directly, obtain the same approved file through a transfer route configured for this VP. The [Zena CSS onboarding Learning Path](../innexis_ana_zena/) describes ANA Host Access and an authorized SSH tunnel; each new VP needs its own access configuration. Set `LP2_MODEL_FILE` to the transferred file's actual path and verify its hash before continuing.

## Check the file identity

Compare the downloaded or transferred file with the SHA-256 published for this Q4_0 file:

```bash
LP2_MODEL_SHA256=7671c0c304e6ce5a7fc577bcb12aba01e2c155cc2efd29b2213c95b18edaf6ed
test -s "$LP2_MODEL_FILE" && wc -c "$LP2_MODEL_FILE"
printf '%s  %s\n' "$LP2_MODEL_SHA256" "$LP2_MODEL_FILE" | sha256sum -c -
printf 'Hash check exit status: %s\n' "$?"
```

In the tested Zena guest, the file size and hash check returned:

```output
428730208 /root/zena-llamacpp/models/qwen2.5-0.5b-instruct-q4_0.gguf
/root/zena-llamacpp/models/qwen2.5-0.5b-instruct-q4_0.gguf: OK
Hash check exit status: 0
```

If your check fails, stop before inference. Investigate the file source, revision, partial download, or expected hash rather than accepting a changed artifact silently.

## What you have learned

You have identified a model artifact separately from the runtime binary. Keep `LP2_MODEL_FILE` available in the same guest shell for inference.
