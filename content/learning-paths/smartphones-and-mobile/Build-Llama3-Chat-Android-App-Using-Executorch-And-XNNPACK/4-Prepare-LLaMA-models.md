---
title: Prepare Llama models for ExecuTorch
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Download and export the Llama 3.2 1B model

To get started with Llama 3, you can obtain the pre-trained parameters by visiting [Meta's Llama Downloads](https://llama.meta.com/llama-downloads/) page. Request access by filling out your details, and read through and accept the Responsible Use Guide. This grants you a license and a download link which is valid for 24 hours. The Llama 3.2 1B Instruct model is used for this exercise, but the same instructions apply to other options as well with minimal modification.

Install the `llama-stack` package from `pip`.
```bash
pip install llama-stack
```
Run the command to download, and paste the download link from the email when prompted.
```bash
llama model download --source meta --model-id Llama3.2-1B-Instruct
```

When the download is finished, the installation path is printed as output.
```output
Successfully downloaded model to /<path-to-home>/.llama/checkpoints/Llama3.2-1B-Instruct
```

Verify by viewing the downloaded files under this path:

```bash
ls $HOME/.llama/checkpoints/Llama3.2-1B-Instruct
checklist.chk           consolidated.00.pth     params.json             tokenizer.model
```

{{% notice Working Directory %}}
The rest of the instructions should be executed from the ExecuTorch base directory.
{{% /notice %}}

Export model and generate `.pte` file. Run the Python command to export the model to your current directory.

```bash
python3 -m examples.models.llama.export_llama \
--checkpoint $HOME/.llama/checkpoints/Llama3.2-1B-Instruct/consolidated.00.pth \
--params $HOME/.llama/checkpoints/Llama3.2-1B-Instruct/params.json \
-kv --use_sdpa_with_kv_cache -X --xnnpack-extended-ops -qmode 8da4w \
--group_size 64 -d fp32 \
--metadata '{"get_bos_id":128000, "get_eos_ids":[128009, 128001, 128006, 128007]}' \
--embedding-quantize 4,32 \
--output_name="llama3_1B_kv_sdpa_xnn_qe_4_64_1024_embedding_4bit.pte" \
--max_seq_length 1024
```

Due to the larger vocabulary size of Llama 3, you should quantize the embeddings with `--embedding-quantize 4,32` to further reduce the model size.

