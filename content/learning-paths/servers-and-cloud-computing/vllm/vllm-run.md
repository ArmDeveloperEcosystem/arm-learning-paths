---
title: Run batch inference using vLLM
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Use a model from Hugging Face

vLLM is designed to work seamlessly with models from the Hugging Face Hub.

The first time you run vLLM, it downloads the required model. This means that you do not have to explicitly download any models. 

If you want to use a model that requires you to request access or accept the terms, you need to log in to Hugging Face using a token.

```bash
huggingface-cli login
```

Enter your Hugging Face token. You can generate a token from [Hugging Face Hub](https://huggingface.co/) by clicking your profile on the top right corner and selecting **Access Tokens**. 

You also need to visit the Hugging Face link printed in the login output and accept the terms by clicking the **Agree and access repository** button or filling out the request-for-access form, depending on the model.

To run batched inference without the need for a login, you can use the `Qwen/Qwen2.5-0.5B-Instruct` model.

## Create a batch script

To run inference with multiple prompts, you can create a simple Python script to load a model and run the prompts. 

Use a text editor to save the Python script below in a file called `batch.py`:

```python
import json
from vllm import LLM, SamplingParams

if __name__ == '__main__':
    # Sample prompts.
    prompts = [
        "Write a hello world program in C",
        "Write a hello world program in Java",
        "Write a hello world program in Rust",
    ]

    # Modify model here
    MODEL = "Qwen/Qwen2.5-0.5B-Instruct"

    # Create a sampling params object.
    sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=256)

    # Create an LLM.
    llm = LLM(model=MODEL, dtype="bfloat16", max_num_batched_tokens=32768)

    # Generate texts from the prompts. The output is a list of RequestOutput objects
    # that contain the prompt, generated text, and other information.
    outputs = llm.generate(prompts, sampling_params)

    # Print the outputs.
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        result = {
            "Prompt": prompt,
            "Generated text": generated_text
        }
        print(json.dumps(result, indent=4))
```

The script uses `bfloat16` precision. 

You can also change the length of the output using the `max_tokens` value.

Run the Python script:

```bash
python ./batch.py
```

The output shows vLLM starting, the model loading, and the batch processing of the three prompts:

```output
INFO 10-23 18:38:40 [__init__.py:216] Automatically detected platform cpu.
INFO 10-23 18:38:42 [utils.py:233] non-default args: {'dtype': 'bfloat16', 'max_num_batched_tokens': 32768, 'disable_log_stats': True, 'model': 'Qwen/Qwen2.5-0.5B-Instruct'}
INFO 10-23 18:38:42 [model.py:547] Resolved architecture: Qwen2ForCausalLM
`torch_dtype` is deprecated! Use `dtype` instead!
INFO 10-23 18:38:42 [model.py:1510] Using max model len 32768
WARNING 10-23 18:38:42 [cpu.py:117] Environment variable VLLM_CPU_KVCACHE_SPACE (GiB) for CPU backend is not set, using 4 by default.
INFO 10-23 18:38:42 [arg_utils.py:1166] Chunked prefill is not supported for ARM and POWER and S390X CPUs; disabling it for V1 backend.
INFO 10-23 18:38:44 [__init__.py:216] Automatically detected platform cpu.
(EngineCore_DP0 pid=8933) INFO 10-23 18:38:46 [core.py:644] Waiting for init message from front-end.
(EngineCore_DP0 pid=8933) INFO 10-23 18:38:46 [core.py:77] Initializing a V1 LLM engine (v0.11.0) with config: model='Qwen/Qwen2.5-0.5B-Instruct', speculative_config=None, tokenizer='Qwen/Qwen2.5-0.5B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=cpu, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=Qwen/Qwen2.5-0.5B-Instruct, enable_prefix_caching=True, chunked_prefill_enabled=False, pooler_config=None, compilation_config={"level":2,"debug_dump_path":"","cache_dir":"","backend":"inductor","custom_ops":["none"],"splitting_ops":null,"use_inductor":true,"compile_sizes":null,"inductor_compile_config":{"enable_auto_functionalized_v2":false,"dce":true,"size_asserts":false,"nan_asserts":false,"epilogue_fusion":true},"inductor_passes":{},"cudagraph_mode":0,"use_cudagraph":true,"cudagraph_num_of_warmups":0,"cudagraph_capture_sizes":[],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"use_inductor_graph_partition":false,"pass_config":{},"max_capture_size":null,"local_cache_dir":null}
(EngineCore_DP0 pid=8933) INFO 10-23 18:38:46 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
(EngineCore_DP0 pid=8933) WARNING 10-23 18:38:47 [cpu.py:316] Pin memory is not supported on CPU.
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
(EngineCore_DP0 pid=8933) INFO 10-23 18:38:47 [parallel_state.py:1208] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
(EngineCore_DP0 pid=8933) INFO 10-23 18:38:47 [cpu_model_runner.py:106] Starting to load model Qwen/Qwen2.5-0.5B-Instruct...
(EngineCore_DP0 pid=8933) INFO 10-23 18:38:47 [cpu.py:104] Using Torch SDPA backend.
(EngineCore_DP0 pid=8933) INFO 10-23 18:38:47 [weight_utils.py:392] Using model weights format ['*.safetensors']
(EngineCore_DP0 pid=8933) INFO 10-23 18:38:47 [weight_utils.py:450] No model.safetensors.index.json found in remote.
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00, 14.03it/s]
(EngineCore_DP0 pid=8933) 
(EngineCore_DP0 pid=8933) INFO 10-23 18:38:47 [default_loader.py:267] Loading weights took 0.10 seconds
(EngineCore_DP0 pid=8933) INFO 10-23 18:38:47 [kv_cache_utils.py:1087] GPU KV cache size: 349,520 tokens
(EngineCore_DP0 pid=8933) INFO 10-23 18:38:47 [kv_cache_utils.py:1091] Maximum concurrency for 32,768 tokens per request: 10.67x
(EngineCore_DP0 pid=8933) INFO 10-23 18:38:48 [cpu_model_runner.py:117] Warming up model for the compilation...
(EngineCore_DP0 pid=8933) WARNING 10-23 18:38:48 [cudagraph_dispatcher.py:106] cudagraph dispatching keys are not initialized. No cudagraph will be used.
(EngineCore_DP0 pid=8933) INFO 10-23 18:38:52 [cpu_model_runner.py:121] Warming up done.
(EngineCore_DP0 pid=8933) INFO 10-23 18:38:52 [core.py:210] init engine (profile, create kv cache, warmup model) took 4.12 seconds
(EngineCore_DP0 pid=8933) WARNING 10-23 18:38:52 [cpu.py:117] Environment variable VLLM_CPU_KVCACHE_SPACE (GiB) for CPU backend is not set, using 4 by default.
INFO 10-23 18:38:52 [llm.py:306] Supported_tasks: ['generate']
Adding requests: 100%|████████████████████████████████████████████████████████████████████████| 3/3 [00:00<00:00, 2043.01it/s]
Processed prompts: 100%|███████████████████| 3/3 [00:18<00:00,  6.05s/it, est. speed input: 1.16 toks/s, output: 35.22 toks/s]
{
    "Prompt": "Write a hello world program in C",
    "Generated text": "++ to print \"Hello, World!\" on the console.\n\n```cpp\n#include <iostream>\n\nint main() {\n    std::cout << \"Hello, World!\" << std::endl;\n    return 0;\n}\n```\n\nThis program demonstrates the use of the `std::cout` stream object in C++ to output text to the console. The `<<` operator is used to print the text \"Hello, World!\" to the console, followed by a newline character (`std::endl`). The `return 0;` statement indicates that the program should exit with a success code. The `main` function is the entry point of the program. When executed, the `main` function will invoke the `std::cout` object and print \"Hello, World!\" to the console. The `return 0;` statement indicates that the program is successful and should not throw any errors."
}
{
    "Prompt": "Write a hello world program in Java",
    "Generated text": "\n\nSure! Here is a simple \"Hello World\" program in Java:\n\n```java\npublic class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println(\"Hello World!\");\n    }\n}\n```\n\nTo run this program, simply compile it using the Java compiler:\n\n```\njavac HelloWorld.java\n```\n\nThen run it using the `java` command:\n\n```\njava HelloWorld\n```\n\nYou should see the message \"Hello World!\" printed to the console. \n\nThis is a basic example of how to write a Java program. Java is a popular programming language and there are many other examples and libraries available for more advanced programming tasks. \n\nIf you're new to Java, you might want to start with the official Java tutorials or the official Java documentation. There are also many online resources and communities that can help you learn Java. For a complete introduction, I recommend checking out the Java Tutorial on Codecademy. \n\nLet me know if you have any more questions!"
}
{
    "Prompt": "Write a hello world program in Rust",
    "Generated text": ".\nCertainly! Here's a simple \"Hello, World!\" program in Rust:\n\n```rust\nfn main() {\n    println!(\"Hello, World!\");\n}\n```\n\nThis program defines a `main` function that runs when the program is executed. Inside the `main` function, the `println!` macro is used to print the string \"Hello, World!\" to the console. \n\nYou can save this code in a file with a `.rs` extension, for example `hello.rs`, and run it using the command `rustc hello.rs`, which will compile and run the program. When you run the program, you should see the output \"Hello, World!\" printed to the console. \n\nIn Rust, the `main` function is the entry point of the program, and the program starts executing from there. The `println!` macro is a function that prints a string to the console. Other important functions in Rust include `println!`, `printlnln`, `println!`, `printlnln`, `println!`, and `printlnln`, which provide similar functionality for different purposes. \n\nYou can also use the `println!` macro to print more complex data structures to the console, such as arrays, slices, strings, numbers, booleans, and"
}
```

You can try with other prompts and models such as `meta-llama/Llama-3.2-1B`. Continue to learn how to set up an OpenAI-compatible server.
