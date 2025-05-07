---
title:  Validate vLLM Inference on Arm
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run Single Inference

Once the server is running, open another terminal and verify it is running as expected with a basic single-prompt request using `curl`. This confirms the server is running correctly and that the OpenAI-compatible /v1/chat/completions API is responding as expected:

```bash
curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "/home/ubuntu/Llama-3.1-8B-Instruct-w8a8-channelwise",
        "temperature": "0.0",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "tell me a funny story"}
        ]
    }'
```
If the setup is working correctly, you'll receive a streaming response from the vLLM server.

The server logs will show that the request was processed successfully. You'll also see prompt and generation throughput metrics, which provide a lightweight benchmark of the model's performance in your environment.

The following log output was generated from a single-prompt test run using the steps in this learning path:

```output
INFO:     Started server process [201749]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO 04-10 18:13:14 chat_utils.py:332] Detected the chat template content format to be 'string'. You can set `--chat-template-content-format` to override this.
INFO 04-10 18:13:14 logger.py:39] Received request chatcmpl-a71fae48603c4d90a5d9aa6efd740fec: prompt: '<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nCutting Knowledge Date: December 2023\nToday Date: 26 Jul 2024\n\nYou are a helpful assistant.<|eot_id|><|start_header_id|>user<|end_header_id|>\n\ntell me a funny story<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.0, top_p=1.0, top_k=-1, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=131026, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None), prompt_token_ids: None, lora_request: None, prompt_adapter_request: None.
INFO 04-10 18:13:14 engine.py:275] Added request chatcmpl-a71fae48603c4d90a5d9aa6efd740fec.
WARNING 04-10 18:13:15 cpu.py:143] Pin memory is not supported on CPU.
INFO 04-10 18:13:17 metrics.py:455] Avg prompt throughput: 9.2 tokens/s, Avg generation throughput: 11.6 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.1%, CPU KV cache usage: 0.0%.
INFO 04-10 18:13:22 metrics.py:455] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 27.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.2%, CPU KV cache usage: 0.0%.
INFO 04-10 18:13:27 metrics.py:455] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 26.5 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.3%, CPU KV cache usage: 0.0%.
INFO:     127.0.0.1:45986 - "POST /v1/chat/completions HTTP/1.1" 200 OK

```

These results confirm that the model is running efficiently on the CPU, with stable prompt and generation throughput — a solid baseline before scaling to batch inference.

You can use these metrics to compare inference performance across different CPU configurations, quantization levels, or model sizes.

## Run Batch Inference

After confirming single-prompt inference, run batch testing to simulate concurrent load and measure server performance at scale.

Use the following Python script to simulate concurrent user interactions.

Save the content shown below in a file named `batch_test.py`:
```python
import requests
import json
import os
import time
import multiprocessing
import argparse

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# prompts (duplicate questions)
#  https://github.com/ggml-org/llama.cpp/blob/b4753/examples/parallel/parallel.cpp#L42-L52
prompts = [
    #"Tell me a joke about AI.",
    "What is the meaning of life?",
    "Tell me an interesting fact about llamas.",
    "What is the best way to cook a steak?",
    "Are you familiar with the Special Theory of Relativity and can you explain it to me?",
    "Recommend some interesting books to read.",
    "What is the best way to learn a new language?",
    "How to get a job at Google?",
    "If you could have any superpower, what would it be?",
    "I want to learn how to play the piano.",
    "What is the meaning of life?",
    "Tell me an interesting fact about llamas.",
    "What is the best way to cook a steak?",
    "Are you familiar with the Special Theory of Relativity and can you explain it to me?",
    "Recommend some interesting books to read.",
    "What is the best way to learn a new language?",
    "How to get a job at Google?",
]

def get_stream(url, prompt, index):
    s = requests.Session()
    print(bcolors.OKGREEN, "Sending request #{}".format(index), bcolors.ENDC)
    with s.post(url, headers=None, json=prompt, stream=True) as resp:
        print(bcolors.WARNING, "Waiting for the reply #{} to the prompt '".format(index) + prompt["messages"][0]["content"] + "'", bcolors.ENDC)
        for line in resp.iter_lines():
            if line:
                print(line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # this is a mandatory parameter
    parser.add_argument("server", help="llama server IP ir DNS address", type=str)
    parser.add_argument("port", help="llama server port", type=int)
    parser.add_argument("-s", "--stream", help="stream the reply", action="store_true")
    parser.add_argument("-b", "--batch", help="concurrent request batch size", type=int, default=1)
    parser.add_argument("--max_tokens", help="maximum output tokens", type=int, default=128)
    parser.add_argument("--schema", help="enndpoint schema (http/https)", type=str, default="http", choices=["http", "https"])
    parser.add_argument("-m", "--model", help="model name", type=str)
    args = parser.parse_args()

    # by default, OpenAI-compatible API is used for the tests, which is supported by both llama.cpp and vllm
    openAPI_endpoint = "/v1/chat/completions"
    server = args.schema + "://" + args.server + ":" + str(args.port) + openAPI_endpoint

    print(server)
    start = time.time()

    proc = []
    for i in range(args.batch):
        prompt = {
            "messages": [
                {"role": "user", "content": prompts[i]}
            ],
            "model": args.model,
            "temperature": 0,
            "max_tokens": args.max_tokens,    # for vllm, it ignores n_predict
            "n_predict": args.max_tokens,     # for llama.cpp (will be ignored by vllm)
            "stream": False  # streaming
        }

        proc.append(multiprocessing.Process(target=get_stream, args=(server, prompt, i)))

    # start the processes
    for p in proc:
        p.start()

    # wait for all the processes to finish
    for p in proc:
        p.join()

    end = time.time()
    print("done!")
    print(end - start)
```
Then, run it using:

```bash
python3 batch_test.py localhost 8000 --schema http --batch 16 -m $HOME/Llama-3.1-8B-Instruct-w8a8-channelwise
```
This simulates multiple users interacting with the model in parallel and helps validate server-side performance under load.
You can modify the number of requests using the --batch flag or review and edit `batch_test.py` to customize prompt content and concurrency logic.

When the test completes, server logs will display a summary including average prompt throughput and generation throughput. This helps benchmark how well the model performs under concurrent load on your Arm-based system.

### Sample Output
Your logs should display successful responses and performance stats, confirming the model handles concurrent requests as expected.

The following log output was generated from a batch inference run using the steps in this learning path:

```output
INFO 04-10 18:20:55 metrics.py:455] Avg prompt throughput: 144.4 tokens/s, Avg generation throughput: 153.4 tokens/s, Running: 16 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 1.2%, CPU KV cache usage: 0.0%.
INFO 04-10 18:21:00 metrics.py:455] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 239.9 tokens/s, Running: 16 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 2.1%, CPU KV cache usage: 0.0%.
INFO:     127.0.0.1:57558 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:57574 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:57586 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:57600 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:57604 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:57620 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:57634 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:57638 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:57644 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:57654 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:57660 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:57676 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:57684 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:57696 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:57712 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     127.0.0.1:57718 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO 04-10 18:21:10 metrics.py:455] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 7.7 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0
```

This output confirms the server is handling concurrent requests effectively, with consistent generation throughput across 16 requests — a strong indication of stable concurrent inference performance on Arm-based CPUs.

### Go Beyond: Power Up Your vLLM Workflow
Now that you’ve successfully quantized and served a model using vLLM on Arm, here are some further ways to explore:

* **Try different models:** Apply the same steps to other [Hugging Face models](https://huggingface.co/models) like Qwen or Gemma.

* **Connect a chat client:**  Link your server with OpenAI-compatible UIs like [Open WebUI](https://github.com/open-webui/open-webui) or explore [OpenAI-compatible clients](https://github.com/topics/openai-api-client).
