---
title: Prepared the Fine Tune Large Language Model for ExecuTorch and Mobile Deployment 
weight: 11 

### FIXED, DO NOT MODIFY
layout: learningpathall
---

####  Fine Tune Model Preparation

- From the [Huggingface](https://huggingface.co/) need to apply for Repo access [Meta's Llama 3.2 language models](https://huggingface.co/meta-llama/Llama-3.2-1B).
-   Download params.json and tokenizer.model from [Llama website](https://www.llama.com/llama-downloads/) or [Hugging Face](https://huggingface.co/meta-llama/Llama-3.2-1B). 
-   After fine-tuning the model, export the adapter_model.safetensors file locally and convert it to the adapter_model.pth format to .pte format.

```python
	python -m examples.models.llama.export_llama \
    --checkpoint <File name in .pth formet> \
	-p <params.json> \
	-kv \
	--use_sdpa_with_kv_cache \
	-X \
	-qmode 8da4w \
	--group_size 128 \
	-d fp32 \
	--metadata '{"get_bos_id":128000, "get_eos_ids":[128009, 128001]}' \
	--embedding-quantize 4,32 \
	--output_name="llama3_kv_sdpa_xnn_qe_4_32.pte"
```

-	Build the Llama Runner binary for [Android](/learning-paths/mobile-graphics-and-gaming/build-llama3-chat-android-app-using-executorch-and-xnnpack/5-run-benchmark-on-android/).
-	Build and Run [Android](/learning-paths/mobile-graphics-and-gaming/build-llama3-chat-android-app-using-executorch-and-xnnpack/6-build-android-chat-app/).
-	Open Android Studio and choose "Open an existing Android Studio project" to navigate to examples/demo-apps/android/LlamaDemo and Press Run (^R) to build and launch the app on your phone.
-	Tap the Settings widget to select a model, configure its parameters, and set any prompts.
-	After choosing the model, tokenizer, and model type, click "Load Model" to load it into the app and return to the main Chat activity.