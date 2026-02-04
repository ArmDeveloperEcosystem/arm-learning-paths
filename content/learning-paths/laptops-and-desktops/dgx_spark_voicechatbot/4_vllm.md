---
title: Real-Time Offline Voice Chatbot Using STT and vLLM
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Real-Time Offline Voice Chatbot Using STT and vLLM

In the previous module, you built a complete Speech-to-Text (STT) engine using ***faster-whisper***, running efficiently on Arm-based CPUs. Now it’s time to add the next major building block: a local large language model (LLM) that can generate intelligent responses from user input.

In this module, you'll integrate ***[vLLM](https://vllm.ai/)*** — a high-performance LLM inference engine that runs on GPU and supports advanced features such as continuous batching, OpenAI-compatible APIs, and quantized models like GPTQ and AWQ.

### Why vLLM?

When building a real-time AI assistant, low latency and high throughput are critical. vLLM offers several advantages:
- ***GPU-accelerated inference***: Designed for modern GPUs, including CUDA and TensorRT backends.
- ***OpenAI-compatible API***: Allows you to use existing prompt structures and client code.
- ***Support for GPTQ, AWQ, FP16, and other formats***: Flexible deployment of open-source models.
- ***Efficient memory usage***: Enables serving large models such as LLaMA 2, Mistral, and more, even on constrained devices.

vLLM is especially effective in hybrid systems like the DGX Spark, where CPU cores handle STT and preprocessing, while the GPU focuses on fast, scalable text generation.

### Install and Launch vLLM with GPU Acceleration

In this section, you’ll install and launch vLLM—an optimized large language model (LLM) inference engine that runs efficiently on GPU. This component will complete your local speech-to-response pipeline by transforming transcribed text into intelligent replies.

#### Step 1: Install Docker and Pull vLLM Image

The most efficiency way to install vLLM on DGX Spark is using Nvidia offical docker image.

Before you pull the image, ensure [Docker](https://docs.nvidia.com/dgx/dgx-spark/nvidia-container-runtime-for-docker.html) is installed and functioning on DGX Spark. Then enable Docker GPU access and pull the latest NVIDIA vLLM container:

```bash
sudo usermod -aG docker $USER
newgrp docker

docker ps  # check Docker is working

export LATEST_VLLM_VERSION=25.11-py3
docker pull nvcr.io/nvidia/vllm:${LATEST_VLLM_VERSION}
```

Confirm the image was downloaded:

```
docker images

nvcr.io/nvidia/vllm      25.11-py3                 d33d4cadbe0f   2 months ago   14.1GB
```

#### Step 2: Download a Quantized Model (GPTQ)

We will use Hugging Face CLI to download a pre-quantized LLM such as ***Mistral-7B-Instruct-GPTQ*** and ***Meta-Llama-3-70B-Instruct-GPTQ*** models for following Real-Time AI Conversations.

```bash
pip install huggingface_hub
hf auth login  # log in to Hugging Face with your token
```

After logining in scussfully, you can download the specific models.

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

```log
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

#### Step 3: Run the vLLM Server with GPU

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
Tip: The first launch will compile and cache the model. To reduce startup time in future runs, consider creating a Docker snapshot with docker commit.
{{% /notice %}}

You can also check your NVIDIA driver and CUDA compatibility during the vLLM launch.


```log
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


#### Step 4: Verify the Server is Running

Once you see the message "Application startup complete." in guest OS, vLLM is ready to run the model.
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

If successful, you'll see the response will include a text reply from the model.

```log
{"id":"chatcmpl-19aee139aabc474c93a3d211ee89d2c8","object":"chat.completion","created":1769183473,"model":"/models/mistral-7b","choices":[{"index":0,"message":{"role":"assistant","content":" RISC (Reduced Instruction Set Computing) is a computer architecture design where the processor has a simpler design and a smaller instruction set compared to CISC (Complex Instruction Set Computing) processors. RISC processors execute a larger number of simpler, more fundamental instructions. Here are some key features of RISC architecture:\n\n1. **Reduced Instruction Set:** RISC processors use a small set of basic instructions that can be combined in various ways to perform complex tasks. This is in contrast to CISC processors, which have a larger instruction set that includes instructions for performing complex tasks directly.\n2. **Register-based:** RISC processors often make extensive use of registers to store data instead of memory. They have a larger number of registers compared to CISC processors, and instructions typically operate directly on these registers. This reduces the number of memory accesses, resulting in faster execution.\n3. **Immediate addressing:** RISC instruction format includes immediate addressing, meaning some instruction operands are directly encoded within the instruction itself, like an add instruction with a constant value. This eliminates the need for additional memory fetch operations, which can save clock cycles.\n4.","refusal":null,"annotations":null,"audio":null,"function_call":null,"tool_calls":[],"reasoning_content":null},"logprobs":null,"finish_reason":"length","stop_reason":null,"token_ids":null}],"service_tier":null,"system_fingerprint":null,"usage":{"prompt_tokens":14,"total_tokens":270,"completion_tokens":256,"prompt_tokens_details":null},"prompt_logprobs":null,"prompt_token_ids":null,"kv_transfer_params":null}
```


### Connect Speech Recognition Output to vLLM

Now that both ***faster-whisper*** and ***vLLM*** are working independently, it’s time to connect them into a real-time speech-to-response pipeline. Your system will listen to live audio, transcribe it, and send the transcription to vLLM to generate an intelligent reply—all running locally without cloud services.


#### Dual Process Architecture: vLLM and STT

For a robust and production-aligned architecture, you will separating the system into two independent processes:
- ***vLLM Server (in Docker)***: Hosts the large language model, optimized for GPU inference. It can run standalone and be reused across multiple services.
- ***STT Client (Python)***: A lightweight CPU-based process that captures microphone input, runs transcription, and sends queries to the vLLM server over HTTP.

This separation has several advantages:

- ***Modularity***: – STT and LLM logic can be developed, updated, or debugged independently.
- ***Flexibility***: – Restart or refine your STT pipeline without touching the model backend.
- ***Performance Isolation***: – GPU-heavy inference doesn’t block audio input or local UI logic.
- ***Production Alignment***: – Mirrors real-world architectures like client-server or microservices.


#### Step 1: Lauch vLLM (in Docker)

Although vLLM can be started with a single docker run command in previous session, that will be a good idea to separating container startup from model launch. This provides greater control and improves development experience.

The reason is that separating docker run from the vllm serve command provides clearer control and flexibility during development.
By launching the container first, you can troubleshoot errors like model path issues or GPU memory limits directly inside the environment — without the container shutting down immediately. It also speeds up iteration: you avoid reloading the entire image each time you tweak settings or restart the model.

This structure also improves visibility. You can inspect files, monitor GPU usage, or run diagnostics like ***curl*** and ***nvidia-smi*** inside the container. For learners and developers alike, breaking these steps apart makes the process easier to understand, debug, and extend.

1. Start the Docker container

```bash
export LATEST_VLLM_VERSION=25.11-py3

sudo docker run --gpus all \
    -p 8000:8000 \
    -v $HOME/models:/models \
    -e NVIDIA_VISIBLE_DEVICES=all \
    -it nvcr.io/nvidia/vllm:${LATEST_VLLM_VERSION} bash
```

2. Inside the container, launch vLLM

```bash
vllm serve /models/mistral-7b \
    --quantization gptq \
    --gpu-memory-utilization 0.9 \
    --max-num-seqs 8 \
    --dtype float16
```

Once you see the message:
```
(APIServer pid=1) INFO:     Started server process [1]
(APIServer pid=1) INFO:     Waiting for application startup.
(APIServer pid=1) INFO:     Application startup complete.
```

The vLLM server is now live and ready to accept HTTP requests.

#### Step 2: Extend STT Python to Connect vLLM for Instant AI Responses

Now that you’ve implemented a real-time speech recognizer, it’s time to extend the pipeline by connecting it to a local language model (LLM) powered by vLLM.

In this step, you’ll:
- Convert the STT result into a message prompt
- Send it to the running vLLM server via HTTP
- Dynamically estimate max_tokens based on input length
- Print the model’s reply next to the transcribed speech


1. Set up the LLM endpoint and model reference:

Send STT output to vLLM
Parse and display vLLM response

Define LLM endpoint and model path, add the following variables at the top of your script:

```python
VLLM_ENDPOINT = "http://localhost:8000/v1/chat/completions"
MODEL_NAME = "/models/mistral-7b"
```

Make sure these match the vLLM server you launched in the previous step.


2. Format Transcription and Send to vLLM:

After transcribing the user’s speech, send the result to the vLLM server by formatting it as a chat prompt.

```python
user_text = " ".join([seg.text.strip() for seg in segments]).strip()
```

Estimate token length and send the request:

```python
max_tokens = min(256, max(64, len(user_text.split()) * 5))
response = requests.post(VLLM_ENDPOINT, json={
    "model": MODEL_NAME,
    "messages": [{"role": "user", "content": user_text}],
    "max_tokens": max_tokens
})
```

Extract the assistant’s reply from the vLLM API response:

```python
result = response.json()
reply = result["choices"][0]["message"]["content"].strip()
```

3. Extract and display the model’s response:

Display both the transcribed input and the model’s response:
```python
...
print(f"\n User: {user_text}\n")
...
print(f" AI  : {reply}\n")
```

This architecture mirrors the OpenAI Chat API design, enabling future enhancements like system-level prompts, multi-turn history, or role-specific behavior.

{{% notice tip %}}
If you encounter a "model does not exist" error, double-check the model path you used when launching vLLM. It must match MODEL_NAME exactly.
{{% /notice %}}

Switch to another terminal to execute following Python code.

```python
import pyaudio
import numpy as np
import webrtcvad
import time
import torch
import threading
import queue
import requests
from faster_whisper import WhisperModel
from collections import deque

# --- Parameters ---
SAMPLE_RATE = 16000
FRAME_DURATION_MS = 30
FRAME_SIZE = int(SAMPLE_RATE * FRAME_DURATION_MS / 1000)
VAD_MODE = 3
SILENCE_LIMIT_SEC = 1.0
MIN_SPEECH_SEC = 2.0
VLLM_ENDPOINT = "http://localhost:8000/v1/chat/completions"
MODEL_NAME = "/models/mistral-7b"

# --- Init VAD and buffers ---
vad = webrtcvad.Vad(VAD_MODE)
speech_buffer = deque()
speech_started = False
last_speech_time = time.time()

# --- Init Thread and Queue ---
audio_queue = queue.Queue()
stop_event = threading.Event()

# --- Init Whisper model ---
device = "cpu"  # "cpu" or "gpu"
compute_type = "int8"  # "int8" or "float16", "int8", "int4"
model = WhisperModel("medium.en", device=device, compute_type=compute_type)

# --- Audio capture thread ---
def audio_capture():
    pa = pyaudio.PyAudio()
    stream = pa.open(format=pyaudio.paInt16,
                     channels=1,
                     rate=SAMPLE_RATE,
                     input=True,
                     frames_per_buffer=FRAME_SIZE)
    print(" Listening... Press Ctrl+C to stop")
    try:
        while not stop_event.is_set():
            frame = stream.read(FRAME_SIZE, exception_on_overflow=False)
            audio_queue.put(frame)
    finally:
        stream.stop_stream()
        stream.close()
        pa.terminate()

# --- Start audio capture thread ---
threading.Thread(target=audio_capture, daemon=True).start()

# --- Main loop: process queue and transcribe ---
try:
    while True:
        if audio_queue.empty():
            time.sleep(0.01)
            continue

        frame = audio_queue.get()
        is_speech = vad.is_speech(frame, SAMPLE_RATE)

        if is_speech:
            speech_buffer.append(frame)
            speech_started = True
            last_speech_time = time.time()
        elif speech_started:
            speech_duration = len(speech_buffer) * (FRAME_DURATION_MS / 1000.0)
            silence_duration = time.time() - last_speech_time

            if silence_duration > SILENCE_LIMIT_SEC:
                if speech_duration >= MIN_SPEECH_SEC:
                    print(" Transcribing buffered speech...")
                    audio_bytes = b"".join(speech_buffer)
                    audio_np = np.frombuffer(audio_bytes, dtype=np.int16).astype(np.float32) / 32768.0

                    segments, _ = model.transcribe(audio_np, language="en")
                    user_text = " ".join([seg.text.strip() for seg in segments]).strip()
                    print(f"\n User: {user_text}\n")

                    max_tokens = 128
                    response = requests.post(VLLM_ENDPOINT, json={
                        "model": MODEL_NAME,
                        "messages": [
                            {"role": "user", "content": user_text}
                        ],
                        "max_tokens": max_tokens
                    })
                    result = response.json()
                    if "choices" not in result:
                        print(" Error from vLLM:", result.get("error", "Unknown error"))
                        continue
                    reply = result["choices"][0]["message"]["content"].strip()
                    print(f" AI  : {reply}\n")
                else:
                    print(f" Skipped short segment ({speech_duration:.2f}s < {MIN_SPEECH_SEC}s)")

                speech_buffer.clear()
                speech_started = False
except KeyboardInterrupt:
    print(" Stopped")
finally:
    stop_event.set()
```


#### Step 3: Interact with the Chat Bot.

Once both your vLLM server and Python STT script are running correctly, you’ll see output like the following in your terminal.

Each time you speak a full sentence (based on your silence/segment thresholds), the system will:
1. Transcribe your speech
2. Display the recognized text
3. Show the model’s reply in natural language


If your input is too short (e.g. a false trigger or a background noise spike), you’ll see a message like:

```
Skipped short segment (1.32s < 2.0s)
```

This means your speech did not meet the MIN_SPEECH_SEC threshold. You can adjust this value in the next module to make the system more or less sensitive.


Here’s a real example when asking the assistant for a joke:

```
 Listening... Press Ctrl+C to stop
 Skipped short segment (0.39s < 2.0s)
 Skipped short segment (1.44s < 2.0s)
 Skipped short segment (1.89s < 2.0s)
 Skipped short segment (1.77s < 2.0s)
 Skipped short segment (0.36s < 2.0s)
 Transcribing buffered speech...

 Listening... Press Ctrl+C to stop
 Transcribing buffered speech...

 User: Hello, please tell me the joke.

 AI  : Of course, I'd be happy to tell you a joke! Here's a classic one:

Why don't libraries smell like popcorn?

Because they are full of books, not movies!

I hope that brings a smile to your face. If you have any other requests, feel free to ask!
```

If your input is too short, you’ll see:

```
Skipped short segment (1.32s < 2.0s)
```

{{% notice tip %}}
You can fine-tune these parameters in future modules to better fit your speaking style or environment.
{{% /notice %}}

### Summary

At this session, you’ve successfully built a complete voice-to-AI-response loop:
- Microphone input captured in real time
- Transcribed locally using faster-whisper on CPU
- Forwarded to a local vLLM server running on GPU
- Received intelligent responses with low latency

This foundation supports a wide range of customizations in the next module, where you’ll build customer-specific workflows with prompt engineering and multi-turn memory.

In the next module, you’ll adapt this core pipeline for real-world assistant scenarios like customer service.