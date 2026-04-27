---
title: Run inference with vLLM
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up access to LLama3.1-8B models

To access the Llama models hosted by Hugging Face, you will need to install the Hugging Face CLI so that you can authenticate yourself and the harness can download what it needs. You should create an account on https://huggingface.co/ and follow the instructions [in the Hugging Face cli guide](https://huggingface.co/docs/huggingface_hub/en/guides/cli) to set up your access token. You can then install the CLI and login:
```bash
curl -LsSf https://hf.co/cli/install.sh | bash
hf auth login
```

Paste your access token into the terminal when prompted. To access Llama3.1-8B you need to request access on the Hugging Face website. Visit https://huggingface.co/meta-llama/Llama-3.1-8B and select "Expand to review and access". Complete the form and you should be granted access in a matter of minutes.

Now you can check that you are able to run inference on the non-quantised Llama model. 

## Run inference on LLama3.1-8B

We will use the vLLM bench CLI to measure the throughput of our models later on. Install the required library and use a limited number of prompts to validate your environment. This will run a little slow the first time through as you download the models.
```bash
pip install vllm[bench]
 
vllm bench throughput \
--num-prompts 10 \
--dataset-name random \
--model meta-llama/Llama-3.1-8B
```

This will report the number of requests per second, the total number of tokens generated per second and the number of output tokens generated per second.

You can do the same for the quantised model:
```bash
vllm bench throughput \
--num-prompts 10 \
--dataset-name random \
--model RedHatAI/Meta-Llama-3.1-8B-quantized.w8a8 
```

You now have the quantised and non-quantised Llama models on your local machine. You have installed vLLM and demonstrated you can run inference on both your models. Now you can move on to benchmarking these models and compare their performance.
