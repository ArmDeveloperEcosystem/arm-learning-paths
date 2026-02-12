---
title: Build a real-time offline voice chatbot using STT and vLLM
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In the previous section, you built a complete Speech-to-Text (STT) engine using faster-whisper, running efficiently on Arm-based CPUs. Now it's time to add the next building block: a local large language model (LLM) that can generate intelligent responses from user input.

You'll integrate [vLLM](https://vllm.ai/), a high-performance LLM inference engine that runs on GPU and supports advanced features such as continuous batching, OpenAI-compatible APIs, and quantized models.

### Why vLLM?

When building a real-time AI assistant, low latency and high throughput are critical. vLLM is designed for modern GPUs, including CUDA and TensorRT backends. It provides an OpenAI-compatible API, allowing you to use existing prompt structures and client code. It supports GPTQ, AWQ, FP16, and other formats for flexible deployment of open-source models, and enables serving large models such as LLaMA 2 and Mistral with efficient memory usage, even on constrained devices.

vLLM is especially effective in hybrid systems like the DGX Spark, where CPU cores handle STT and preprocessing, while the GPU focuses on fast, scalable text generation.

### Install and launch vLLM with GPU acceleration

In this section, you’ll install and launch vLLM—an optimized large language model (LLM) inference engine that runs efficiently on GPU. This component will complete your local speech-to-response pipeline by transforming transcribed text into intelligent replies.

#### Install Docker and pull vLLM image

The most efficient way to install vLLM on DGX Spark is using the NVIDIA official Docker image.

Before you pull the image, ensure [Docker](https://docs.nvidia.com/dgx/dgx-spark/nvidia-container-runtime-for-docker.html) is installed and functioning on DGX Spark. Then enable Docker GPU access and pull the latest NVIDIA vLLM container:

```bash
export LATEST_VLLM_VERSION=25.11-py3
docker pull nvcr.io/nvidia/vllm:${LATEST_VLLM_VERSION}
```

Confirm the image was downloaded:

```bash
docker images
```

The image is shown in the output:

```output
nvcr.io/nvidia/vllm      25.11-py3                 d33d4cadbe0f   2 months ago   14.1GB
```

#### Download a quantized model (GPTQ)

Use Hugging Face CLI to download a pre-quantized LLM such as Mistral-7B-Instruct-GPTQ and Meta-Llama-3-70B-Instruct-GPTQ models for real-time AI conversations.

```bash
pip install huggingface_hub
hf auth login  # log in to Hugging Face with your token
```

After logging in successfully, download the specific models:

```bash
mkdir -p ~/models
# Mistral 7B GPTQ
hf download TheBloke/Mistral-7B-Instruct-v0.2-GPTQ --local-dir ~/models/mistral-7b
# (Optional) LLaMA3 70B GPTQ (requires more GPU memory)
hf download TechxGenus/Meta-Llama-3-70B-Instruct-GPTQ --local-dir ~/models/llama3-70b
```

Check model contents to ensure download success:

```bash
tree ~/models/mistral-7b -L 1
```

The files should include config.json, tokenizer.model, model.safetensors, etc.

```output
├── config.json
├── generation_config.json
├── model.safetensors
├── quantize_config.json
├── README.md
├── special_tokens_map.json
├── tokenizer_config.json
├── tokenizer.json
└── tokenizer.model

1 directory, 9 files
```

#### Run the vLLM server with GPU

Mount your local ~/models directory and start the vLLM inference server with your downloaded model:

```bash
docker run -it --gpus all -p 8000:8000 \
  -v ~/models:/models \
  nvcr.io/nvidia/vllm:${LATEST_VLLM_VERSION} \
  vllm serve /models/mistral-7b \
  --quantization gptq \
  --gpu-memory-utilization 0.9 \
  --dtype float16
```

{{% notice Note %}}
The first launch compiles and caches the model. To reduce startup time in future runs, consider creating a Docker snapshot with docker commit.
{{% /notice %}}

You can also check your NVIDIA driver and CUDA compatibility during the vLLM launch by looking at the output.

```output
NVIDIA Release 25.11 (build 231063344)
vLLM Version 0.11.0+582e4e37
Container image Copyright (c) 2025, NVIDIA CORPORATION & AFFILIATES. All rights reserved.

Various files include modifications (c) NVIDIA CORPORATION & AFFILIATES.  All rights reserved.

GOVERNING TERMS: The software and materials are governed by the NVIDIA Software License Agreement
(found at https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-software-license-agreement/)
and the Product-Specific Terms for NVIDIA AI Products
(found at https://www.nvidia.com/en-us/agreements/enterprise-software/product-specific-terms-for-ai-products/).

NOTE: The SHMEM allocation limit is set to the default of 64MB.  This may be
   insufficient for vLLM.  NVIDIA recommends the use of the following flags:
   docker run --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 ...

INFO 01-23 15:48:28 [__init__.py:216] Automatically detected platform cuda.
(APIServer pid=1) INFO 01-23 15:48:29 [api_server.py:1842] vLLM API server version 0.11.0+582e4e37.nv25.11
(APIServer pid=1) INFO 01-23 15:48:29 [utils.py:233] non-default args: {'model_tag': '/models/mistral-7b', 'model': '/models/mistral-7b', 'dtype': 'float16', 'quantization': 'gptq'}
(APIServer pid=1) INFO 01-23 15:48:33 [model.py:547] Resolved architecture: MistralForCausalLM
(APIServer pid=1) `torch_dtype` is deprecated! Use `dtype` instead!
(APIServer pid=1) WARNING 01-23 15:48:33 [model.py:1733] Casting torch.bfloat16 to torch.float16.
(APIServer pid=1) INFO 01-23 15:48:33 [model.py:1510] Using max model len 32768
(APIServer pid=1) INFO 01-23 15:48:33 [gptq_marlin.py:195] Detected that the model can run with gptq_marlin, however you specified quantization=gptq explicitly, so forcing gptq. Use quantization=gptq_marlin for faster inference
(APIServer pid=1) INFO 01-23 15:48:33 [scheduler.py:205] Chunked prefill is enabled with max_num_batched_tokens=2048.
INFO 01-23 15:48:34 [__init__.py:216] Automatically detected platform cuda.
(EngineCore_DP0 pid=164) INFO 01-23 15:48:36 [core.py:644] Waiting for init message from front-end.
(EngineCore_DP0 pid=164) INFO 01-23 15:48:36 [core.py:77] Initializing a V1 LLM engine (v0.11.0+582e4e37.nv25.11) with config: model='/models/mistral-7b', speculative_config=None, tokenizer='/models/mistral-7b', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=False, quantization=gptq, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=/models/mistral-7b, enable_prefix_caching=True, chunked_prefill_enabled=True, pooler_config=None, compilation_config={"level":3,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":[],"splitting_ops":["vllm.unified_attention","vllm.unified_attention_with_output","vllm.mamba_mixer2","vllm.mamba_mixer","vllm.short_conv","vllm.linear_attention","vllm.plamo2_mamba_mixer","vllm.gdn_attention","vllm.sparse_attn_indexer"],"use_inductor":true,"compile_sizes":[],"inductor_compile_config":{"enable_auto_functionalized_v2":false},"inductor_passes":{},"cudagraph_mode":[2,1],"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[512,504,496,488,480,472,464,456,448,440,432,424,416,408,400,392,384,376,368,360,352,344,336,328,320,312,304,296,288,280,272,264,256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"use_inductor_graph_partition":false,"pass_config":{},"max_capture_size":512,"local_cache_dir":null}
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
(EngineCore_DP0 pid=164) INFO 01-23 15:48:47 [parallel_state.py:1208] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
(EngineCore_DP0 pid=164) INFO 01-23 15:48:47 [topk_topp_sampler.py:55] Using FlashInfer for top-p & top-k sampling.
(EngineCore_DP0 pid=164) INFO 01-23 15:48:47 [gpu_model_runner.py:2602] Starting to load model /models/mistral-7b...
(EngineCore_DP0 pid=164) INFO 01-23 15:48:47 [gpu_model_runner.py:2634] Loading model from scratch...
(EngineCore_DP0 pid=164) INFO 01-23 15:48:47 [cuda.py:366] Using Flash Attention backend on V1 engine.
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:19<00:00, 19.47s/it]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:19<00:00, 19.47s/it]
(EngineCore_DP0 pid=164) 
(EngineCore_DP0 pid=164) INFO 01-23 15:49:07 [default_loader.py:267] Loading weights took 19.62 seconds
(EngineCore_DP0 pid=164) INFO 01-23 15:49:08 [gpu_model_runner.py:2653] Model loading took 3.8844 GiB and 20.442057 seconds
(EngineCore_DP0 pid=164) INFO 01-23 15:49:11 [backends.py:548] Using cache directory: /root/.cache/vllm/torch_compile_cache/d865434b5b/rank_0_0/backbone for vLLM's torch.compile
(EngineCore_DP0 pid=164) INFO 01-23 15:49:11 [backends.py:559] Dynamo bytecode transform time: 3.29 s
(EngineCore_DP0 pid=164) INFO 01-23 15:49:13 [backends.py:197] Cache the graph for dynamic shape for later use
(EngineCore_DP0 pid=164) INFO 01-23 15:49:22 [backends.py:218] Compiling a graph for dynamic shape takes 10.00 s
(EngineCore_DP0 pid=164) INFO 01-23 15:49:41 [monitor.py:34] torch.compile takes 13.29 s in total
(EngineCore_DP0 pid=164) INFO 01-23 15:50:05 [gpu_worker.py:298] Available KV cache memory: 102.56 GiB
(EngineCore_DP0 pid=164) INFO 01-23 15:50:06 [kv_cache_utils.py:1087] GPU KV cache size: 840,160 tokens
(EngineCore_DP0 pid=164) INFO 01-23 15:50:06 [kv_cache_utils.py:1091] Maximum concurrency for 32,768 tokens per request: 25.64x
(EngineCore_DP0 pid=164) 2026-01-23 15:50:10,030 - INFO - autotuner.py:256 - flashinfer.jit: [Autotuner]: Autotuning process starts ...
(EngineCore_DP0 pid=164) 2026-01-23 15:50:11,056 - INFO - autotuner.py:262 - flashinfer.jit: [Autotuner]: Autotuning process ends
Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 100%|█████████████████████████████████████████████████| 67/67 [00:12<00:00,  5.43it/s]
Capturing CUDA graphs (decode, FULL): 100%|████████████████████████████████████████████████████████████████████| 35/35 [00:05<00:00,  6.23it/s]
(EngineCore_DP0 pid=164) INFO 01-23 15:50:29 [gpu_model_runner.py:3480] Graph capturing finished in 18 secs, took -0.03 GiB
(EngineCore_DP0 pid=164) INFO 01-23 15:50:29 [core.py:210] init engine (profile, create kv cache, warmup model) took 81.30 seconds
(APIServer pid=1) INFO 01-23 15:50:32 [loggers.py:147] Engine 000: vllm cache_config_info with initialization after num_gpu_blocks is: 52510
(APIServer pid=1) INFO 01-23 15:50:32 [api_server.py:1637] Supported_tasks: ['generate']
(APIServer pid=1) INFO 01-23 15:50:32 [api_server.py:1915] Starting vLLM API server 0 on http://0.0.0.0:8000
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:34] Available routes are:
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /openapi.json, Methods: HEAD, GET
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /docs, Methods: HEAD, GET
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /docs/oauth2-redirect, Methods: HEAD, GET
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /redoc, Methods: HEAD, GET
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /health, Methods: GET
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /load, Methods: GET
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /ping, Methods: POST
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /ping, Methods: GET
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /tokenize, Methods: POST
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /detokenize, Methods: POST
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /v1/models, Methods: GET
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /version, Methods: GET
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /v1/responses, Methods: POST
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /v1/responses/{response_id}, Methods: GET
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /v1/responses/{response_id}/cancel, Methods: POST
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /v1/chat/completions, Methods: POST
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /v1/completions, Methods: POST
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /v1/embeddings, Methods: POST
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /pooling, Methods: POST
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /classify, Methods: POST
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /score, Methods: POST
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /v1/score, Methods: POST
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /v1/audio/transcriptions, Methods: POST
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /v1/audio/translations, Methods: POST
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /rerank, Methods: POST
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /v1/rerank, Methods: POST
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /v2/rerank, Methods: POST
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /scale_elastic_ep, Methods: POST
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /is_scaling_elastic_ep, Methods: POST
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /invocations, Methods: POST
(APIServer pid=1) INFO 01-23 15:50:32 [launcher.py:42] Route: /metrics, Methods: GET
(APIServer pid=1) INFO:     Started server process [1]
(APIServer pid=1) INFO:     Waiting for application startup.
(APIServer pid=1) INFO:     Application startup complete.
```

{{% notice Note %}}
You don’t need to read every log line. As long as you see Application startup complete, your model server is ready.
{{% /notice %}}

#### Verify the server is running

Once you see the message "Application startup complete." vLLM is ready to run the model.

Send a test request with curl on other terminal:

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "/models/mistral-7b",
    "messages": [{"role": "user", "content": "Explain RISC architecture"}],
    "max_tokens": 256
  }'
```

If successful, the response includes a text reply from the model.

```output
{"id":"chatcmpl-19aee139aabc474c93a3d211ee89d2c8","object":"chat.completion","created":1769183473,"model":"/models/mistral-7b","choices":[{"index":0,"message":{"role":"assistant","content":" RISC (Reduced Instruction Set Computing) is a computer architecture design where the processor has a simpler design and a smaller instruction set compared to CISC (Complex Instruction Set Computing) processors. RISC processors execute a larger number of simpler, more fundamental instructions. Here are some key features of RISC architecture:\n\n1. **Reduced Instruction Set:** RISC processors use a small set of basic instructions that can be combined in various ways to perform complex tasks. This is in contrast to CISC processors, which have a larger instruction set that includes instructions for performing complex tasks directly.\n2. **Register-based:** RISC processors often make extensive use of registers to store data instead of memory. They have a larger number of registers compared to CISC processors, and instructions typically operate directly on these registers. This reduces the number of memory accesses, resulting in faster execution.\n3. **Immediate addressing:** RISC instruction format includes immediate addressing, meaning some instruction operands are directly encoded within the instruction itself, like an add instruction with a constant value. This eliminates the need for additional memory fetch operations, which can save clock cycles.\n4.","refusal":null,"annotations":null,"audio":null,"function_call":null,"tool_calls":[],"reasoning_content":null},"logprobs":null,"finish_reason":"length","stop_reason":null,"token_ids":null}],"service_tier":null,"system_fingerprint":null,"usage":{"prompt_tokens":14,"total_tokens":270,"completion_tokens":256,"prompt_tokens_details":null},"prompt_logprobs":null,"prompt_token_ids":null,"kv_transfer_params":null}
```

## What you've accomplished and what's next

You've successfully installed and launched vLLM on DGX Spark using Docker, downloaded a quantized LLM model (GPTQ format), and verified the server responds to API requests. Your GPU-accelerated language model is now ready to generate intelligent responses.

In the next section, you'll connect this vLLM server to the STT pipeline you built earlier, creating a complete voice-to-response system.

