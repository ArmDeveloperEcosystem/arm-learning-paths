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

# Sample prompts.
prompts = [
    "Write a hello world program in C",
    "Write a hello world program in Java",
    "Write a hello world program in Rust",
]

# Create a sampling params object.
sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=256)

# Create an LLM.
llm = LLM(model="Qwen/Qwen2.5-0.5B-Instruct", dtype="bfloat16")

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
INFO 12-12 22:52:57 config.py:441] This model supports multiple tasks: {'generate', 'reward', 'embed', 'score', 'classify'}. Defaulting to 'generate'.
WARNING 12-12 22:52:57 config.py:567] Async output processing is not supported on the current platform type cpu.
WARNING 12-12 22:52:57 cpu.py:56] CUDA graph is not supported on CPU, fallback to the eager mode.
WARNING 12-12 22:52:57 cpu.py:68] Environment variable VLLM_CPU_KVCACHE_SPACE (GB) for CPU backend is not set, using 4 by default.
INFO 12-12 22:52:57 importing.py:15] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 12-12 22:52:57 llm_engine.py:250] Initializing an LLM engine (v0.6.4.post2.dev322+g72ff3a96) with config: VllmConfig(model_config=<vllm.config.ModelConfig object at 0xe1e8054ef5e0>, cache_config=<vllm.config.CacheConfig object at 0xe1e84500d780>, parallel_config=ParallelConfig(pipeline_parallel_size=1, tensor_parallel_size=1, worker_use_ray=False, max_parallel_loading_workers=None, disable_custom_all_reduce=False, tokenizer_pool_config=None, ray_workers_use_nsight=False, placement_group=None, distributed_executor_backend=None, worker_cls='vllm.worker.cpu_worker.CPUWorker', sd_worker_cls='auto', world_size=1, rank=0), scheduler_config=SchedulerConfig(runner_type='generate', max_num_batched_tokens=32768, max_num_seqs=256, max_model_len=32768, num_lookahead_slots=0, delay_factor=0.0, enable_chunked_prefill=False, is_multimodal_model=False, preemption_mode=None, num_scheduler_steps=1, multi_step_stream_outputs=True, send_delta_data=False, policy='fcfs', chunked_prefill_enabled=False), device_config=<vllm.config.DeviceConfig object at 0xe1e845163f40>, load_config=LoadConfig(load_format=<LoadFormat.AUTO: 'auto'>, download_dir=None, model_loader_extra_config=None, ignore_patterns=['original/**/*']), lora_config=None, speculative_config=None, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), prompt_adapter_config=None, quant_config=None, compilation_config=CompilationConfig(level=0, debug_dump_path='', backend='', custom_ops=[], splitting_ops=['vllm.unified_attention', 'vllm.unified_attention_with_output'], use_inductor=True, candidate_compile_sizes=[], inductor_compile_config={}, inductor_passes={}, use_cudagraph=False, cudagraph_num_of_warmups=0, cudagraph_capture_sizes=None, cudagraph_copy_inputs=False, pass_config=PassConfig(dump_graph_stages=[], dump_graph_dir=PosixPath('.'), enable_fusion=True, enable_reshape=True), compile_sizes=[], capture_sizes=[256, 248, 240, 232, 224, 216, 208, 200, 192, 184, 176, 168, 160, 152, 144, 136, 128, 120, 112, 104, 96, 88, 80, 72, 64, 56, 48, 40, 32, 24, 16, 8, 4, 2, 1], enabled_custom_ops=Counter(), disabled_custom_ops=Counter(), compilation_time=0.0, static_forward_context={}), kv_transfer_config=None, instance_id='5c715'),use_cached_outputs=False, 
INFO 12-12 22:52:58 cpu.py:33] Cannot use _Backend.FLASH_ATTN backend on CPU.
INFO 12-12 22:52:58 selector.py:141] Using Torch SDPA backend.
INFO 12-12 22:52:58 weight_utils.py:243] Using model weights format ['*.safetensors']
INFO 12-12 22:52:58 weight_utils.py:288] No model.safetensors.index.json found in remote.
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00, 12.97it/s]

INFO 12-12 22:52:58 cpu_executor.py:186] # CPU blocks: 21845
INFO 12-12 22:52:59 llm_engine.py:447] init engine (profile, create kv cache, warmup model) took 0.25 seconds
Processed prompts: 100%|███████████████████████████████████████| 3/3 [00:33<00:00, 11.10s/it, est. speed input: 0.63 toks/s, output: 20.61 toks/s]
{
    "Prompt": "Write a hello world program in C",
    "Generated text": "\n\nHere's a simple \"Hello, World!\" program written in C:\n\n```c\n#include <stdio.h>\n\nint main() {\n    printf(\"Hello, World!\\n\");\n    return 0;\n}\n```\n\nThis program does the following:\n\n1. Includes the `<stdio.h>` header to use the `printf` function.\n2. Defines a `main` function, which is the entry point of the program.\n3. Uses `printf` to output the message \"Hello, World!\" to the console.\n4. Returns 0 to indicate that the program executed successfully.\n\nWhen you run this program, you should see the output:\n\n```\nHello, World!\n``` \n\nThis is the basic structure of a C program, providing a simple example of how to create, run, and display a basic program. Note that C is a high-level programming language, meaning that it provides low-level operations for users to interact with the hardware, but at the same time, it is a low-level language that needs to be compiled and linked into an executable file (.exe) that the computer's operating system can load and run. C, as a compiled language, often requires additional libraries and tools for use. For more information, you can refer to the C Programming Language documentation."
}
{
    "Prompt": "Write a hello world program in Java",
    "Generated text": "\n\nCertainly! Below is a simple `HelloWorld.java` file that prints \"Hello, World!\" to the console when you run it:\n\n```java\npublic class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, World!\");\n    }\n}\n```\n\nTo compile this program, you would use an integrated development environment (IDE) like IntelliJ IDEA, Eclipse, or NetBeans. Here is how you can compile it:\n\n1. Open a terminal or command prompt.\n2. Navigate to the directory where you saved the `HelloWorld.java` file.\n3. Compile the program using the following command:\n   ```bash\n   javac HelloWorld.java\n   ```\n4. Run the compiled program using the following command:\n   ```bash\n   java HelloWorld\n   ```\n\nThis will output:\n```\nHello, World!\n```"
}
{
    "Prompt": "Write a hello world program in Rust",
    "Generated text": "\n\nCertainly! Here is a simple example of a `HelloWorld` program in Rust:\n\n```rust\nfn main() {\n    println!(\"Hello, world!\");\n}\n```\n\n### Explanation:\n\n- `fn main()`: This is the entry point of the program.\n- `println!`: This function is used to print out the message `Hello, world!` to the console.\n- `println!`: The `println!` macro is used to print messages in Rust.\n\n### How to Run the Program:\n\n1. Make sure you have Rust installed on your system.\n2. Save the above code in a file with a `.rs` extension, e.g., `hello.rs`.\n3. Open a terminal or command prompt and navigate to the directory where the file is saved.\n4. Run the program by typing `rustc hello.rs` (if you're using `rustc`, you don't need to specify the file extension).\n5. After the program runs, it should print the message `Hello, world!` to the console.\n\n### Running in Development:\n\nIf you want to run the program in development mode to see the output in the terminal, you can use the `-o` flag:\n\n```sh\nrustc -o hello-dev hello.rs\n./"
}
```

You can try with other prompts and models such as `meta-llama/Llama-3.2-1B`. 

Continue to learn how to set up an OpenAI-compatible server.
