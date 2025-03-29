---
title: Run a DeepSeek-R1 chatbot on Arm servers
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin
The instructions in this Learning Path are for any Arm server running Ubuntu 24.04 LTS. You need an Arm server instance with at least 64 cores and 512GB of RAM to run this example. Configure disk storage up to at least 400 GB. The instructions have been tested on an AWS Graviton4 r8g.24xlarge instance.


## Overview

Arm CPUs are widely used in traditional ML and AI use cases. In this Learning Path, you learn how to run generative AI inference-based use cases like a LLM chatbot on Arm-based CPUs. You do this by deploying the [DeepSeek-R1 GGUF models](https://huggingface.co/bartowski/DeepSeek-R1-GGUF) on your Arm-based CPU using `llama.cpp`.

[llama.cpp](https://github.com/ggerganov/llama.cpp) is an open source C/C++ project developed by Georgi Gerganov that enables efficient LLM inference on a variety of hardware - both locally, and in the cloud. 

## About the DeepSeek-R1 model and GGUF model format

The [DeepSeek-R1 model](https://huggingface.co/deepseek-ai/DeepSeek-R1) from DeepSeek-AI available on Hugging Face, is released under the [MIT License](https://github.com/deepseek-ai/DeepSeek-R1/blob/main/LICENSE) and free to use for research and commercial purposes. 

The DeepSeek-R1 model has 671 billion parameters, based on Mixture of Experts(MoE) architecture. This improves inference speed and maintains model quality. For this example, the full 671 billion (671B) model is used for retaining quality chatbot capability while also running efficiently on your Arm-based CPU. 

Traditionally, the training and inference of LLMs has been done on GPUs using full-precision 32-bit (FP32) or half-precision 16-bit (FP16) data type formats for the model parameter and weights. Recently, a new binary model format called GGUF was introduced by the `llama.cpp` team. This new GGUF model format uses compression and quantization techniques that remove the dependency on using FP32 and FP16 data type formats. For example, GGUF supports quantization where model weights that are generally stored as FP16 data types are scaled down to 4-bit integers. This significantly reduces the need for computational resources and the amount of RAM required. These advancements made in the model format and the data types used make Arm CPUs a great fit for running LLM inferences.   
 
## Install dependencies 

Install the following packages on your Arm based server instance:

```bash
sudo apt update
sudo apt install make cmake -y
```

You also need to install `gcc` on your machine:

```bash
sudo apt install gcc g++ -y
sudo apt install build-essential -y
```

## Download and build llama.cpp

You are now ready to start building `llama.cpp`. 

Clone the source repository for llama.cpp:

```bash
git clone https://github.com/ggerganov/llama.cpp
```

By default, `llama.cpp` builds for CPU only. You don't need to provide any extra switches to build it for the Arm CPU that you run it on.

Run `cmake` to build it:

```bash
cd llama.cpp
mkdir build
cd build
cmake .. -DCMAKE_CXX_FLAGS="-mcpu=native" -DCMAKE_C_FLAGS="-mcpu=native"
cmake --build . -v --config Release -j `nproc`
```

`llama.cpp` is now built in the `bin` directory.
Check that `llama.cpp` has built correctly by running the help command:

```bash
cd bin
./llama-cli -h
```

If `llama.cpp` has built correctly on your machine, you will see the help options being displayed. A snippet of the output is shown below:

```output
usage: ./llama-cli [options]

general:

  -h,    --help, --usage          print usage and exit
         --version                show version and build info
  -v,    --verbose                print verbose information
         --verbosity N            set specific verbosity level (default: 0)
         --verbose-prompt         print a verbose prompt before generation (default: false)
         --no-display-prompt      don't print prompt at generation (default: false)
  -co,   --color                  colorise output to distinguish prompt and user input from generations (default: false)
  -s,    --seed SEED              RNG seed (default: -1, use random seed for < 0)
  -t,    --threads N              number of threads to use during generation (default: 4)
  -tb,   --threads-batch N        number of threads to use during batch and prompt processing (default: same as --threads)
  -td,   --threads-draft N        number of threads to use during generation (default: same as --threads)
  -tbd,  --threads-batch-draft N  number of threads to use during batch and prompt processing (default: same as --threads-draft)
         --draft N                number of tokens to draft for speculative decoding (default: 5)
  -ps,   --p-split N              speculative decoding split probability (default: 0.1)
  -lcs,  --lookup-cache-static FNAME
                                  path to static lookup cache to use for lookup decoding (not updated by generation)
  -lcd,  --lookup-cache-dynamic FNAME
                                  path to dynamic lookup cache to use for lookup decoding (updated by generation)
  -c,    --ctx-size N             size of the prompt context (default: 0, 0 = loaded from model)
  -n,    --predict N              number of tokens to predict (default: -1, -1 = infinity, -2 = until context filled)
  -b,    --batch-size N           logical maximum batch size (default: 2048)
```


## Install Hugging Face Hub

There are a few different ways you can download the DeepSeek-R1 model. In this Learning Path, you download the model from Hugging Face.

[Hugging Face](https://huggingface.co/) is an open source AI community where you can host your own AI models, train them and collaborate with others in the community. You can browse through the thousands of models that are available for a variety of use cases like NLP, audio, and computer vision.

The `huggingface_hub` library provides APIs and tools that let you easily download and fine-tune pre-trained models. You will use `huggingface-cli` to download the [DeepSeek-R1 model](https://huggingface.co/bartowski/DeepSeek-R1-GGUF).

Install the required Python packages:

```bash
sudo apt install python-is-python3 python3-pip python3-venv -y
```

Create and activate a Python virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Your terminal prompt now has the `(venv)` prefix indicating the virtual environment is active. Use this virtual environment for the remaining commands.

Install the `huggingface_hub` python library using `pip`:

```bash
pip install huggingface_hub
```

You can now download the model using the huggingface cli:

```bash
huggingface-cli download bartowski/DeepSeek-R1-GGUF --include "*DeepSeek-R1-Q4_0*"  --local-dir DeepSeek-R1-Q4_0
```
Before you proceed and run this model, take a quick look at what `Q4_0` in the model name denotes.

## Quantization format

`Q4_0` in the model name refers to the quantization method the model uses. The goal of quantization is to reduce the size of the model (to reduce the memory space required) and faster (to reduce memory bandwidth bottlenecks transferring large amounts of data from memory to a processor). The primary trade-off to keep in mind when reducing a model's size is maintaining quality of performance. Ideally, a model is quantized to meet size and speed requirements while not having a negative impact on performance. 

This model is `DeepSeek-R1-Q4_0-00001-of-00010.gguf`, so what does each component mean in relation to the quantization level? The main thing to note is the number of bits per parameter, which is denoted by 'Q4' in this case or 4-bit integer. As a result, by only using 4 bits per parameter for 671 billion parameters, the model drops to be 354 GB in size.

## Run the pre-quantized DeepSeek-R1 LLM model weights on your Arm-based server

As of [llama.cpp commit 0f1a39f3](https://github.com/ggerganov/llama.cpp/commit/0f1a39f3), Arm has contributed code for performance optimization with three types of GEMV/GEMM kernels corresponding to three processor types:

* AWS Graviton2, where you only have NEON support (you will see less improvement for these GEMV/GEMM kernels),
* AWS Graviton3, where the GEMV/GEMM kernels exploit both SVE 256 and MATMUL INT8 support, and
* AWS Graviton4, where the GEMV/GEMM kernels exploit NEON/SVE 128 and MATMUL_INT8 support

With the latest commits in `llama.cpp` you will see improvements for these Arm optimized kernels directly on your Arm-based server. You can run the pre-quantized Q4_0 model as is and do not need to re-quantize the model.

Run the pre-quantized DeepSeek-R1 model exactly as the weights were downloaded from huggingface:

```bash
./llama-cli -m DeepSeek-R1-Q4_0/DeepSeek-R1-Q4_0/DeepSeek-R1-Q4_0-00001-of-00010.gguf -no-cnv --temp 0.6 -t 64 --prompt "<|User|>Building a visually appealing website can be done in ten simple steps:<｜Assistant｜>" -n 512
```

This command will use the downloaded model (`-m` flag), disable conversation mode explicitly (`-no-cnv` flag), adjust the randomness of the generated text (`--temp` flag),  with the specified prompt (`-p` flag), and target a 512 token completion (`-n` flag), using 64 threads (`-t` flag).

You may notice there are many gguf files downloaded, llama.cpp can load all series of files by passing the first one with `-m` flag.

You will see lots of interesting statistics being printed from llama.cpp about the model and the system, followed by the prompt and completion. The tail of the output from running this model on an AWS Graviton4 r8g.24xlarge instance is shown below:

```output
build: 4963 (02082f15) with cc (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 for aarch64-linux-gnu
main: llama backend init
main: load the model and apply lora adapter, if any
llama_model_loader: additional 9 GGUFs metadata loaded.
llama_model_loader: loaded meta data with 51 key-value pairs and 1025 tensors from /home/ubuntu/DeepSeek-R1-Q4_0/DeepSeek-R1-Q4_0/DeepSeek-R1-Q4_0-00001-of-00010.gguf (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = deepseek2
llama_model_loader: - kv   1:                               general.type str              = model
llama_model_loader: - kv   2:                               general.name str              = DeepSeek R1
llama_model_loader: - kv   3:                         general.size_label str              = 256x20B
llama_model_loader: - kv   4:                               general.tags arr[str,1]       = ["text-generation"]
llama_model_loader: - kv   5:                      deepseek2.block_count u32              = 61
llama_model_loader: - kv   6:                   deepseek2.context_length u32              = 163840
llama_model_loader: - kv   7:                 deepseek2.embedding_length u32              = 7168
llama_model_loader: - kv   8:              deepseek2.feed_forward_length u32              = 18432
llama_model_loader: - kv   9:             deepseek2.attention.head_count u32              = 128
llama_model_loader: - kv  10:          deepseek2.attention.head_count_kv u32              = 128
llama_model_loader: - kv  11:                   deepseek2.rope.freq_base f32              = 10000.000000
llama_model_loader: - kv  12: deepseek2.attention.layer_norm_rms_epsilon f32              = 0.000001
llama_model_loader: - kv  13:                deepseek2.expert_used_count u32              = 8
llama_model_loader: - kv  14:        deepseek2.leading_dense_block_count u32              = 3
llama_model_loader: - kv  15:                       deepseek2.vocab_size u32              = 129280
llama_model_loader: - kv  16:            deepseek2.attention.q_lora_rank u32              = 1536
llama_model_loader: - kv  17:           deepseek2.attention.kv_lora_rank u32              = 512
llama_model_loader: - kv  18:             deepseek2.attention.key_length u32              = 192
llama_model_loader: - kv  19:           deepseek2.attention.value_length u32              = 128
llama_model_loader: - kv  20:       deepseek2.expert_feed_forward_length u32              = 2048
llama_model_loader: - kv  21:                     deepseek2.expert_count u32              = 256
llama_model_loader: - kv  22:              deepseek2.expert_shared_count u32              = 1
llama_model_loader: - kv  23:             deepseek2.expert_weights_scale f32              = 2.500000
llama_model_loader: - kv  24:              deepseek2.expert_weights_norm bool             = true
llama_model_loader: - kv  25:               deepseek2.expert_gating_func u32              = 2
llama_model_loader: - kv  26:             deepseek2.rope.dimension_count u32              = 64
llama_model_loader: - kv  27:                deepseek2.rope.scaling.type str              = yarn
llama_model_loader: - kv  28:              deepseek2.rope.scaling.factor f32              = 40.000000
llama_model_loader: - kv  29: deepseek2.rope.scaling.original_context_length u32              = 4096
llama_model_loader: - kv  30: deepseek2.rope.scaling.yarn_log_multiplier f32              = 0.100000
llama_model_loader: - kv  31:                       tokenizer.ggml.model str              = gpt2
llama_model_loader: - kv  32:                         tokenizer.ggml.pre str              = deepseek-v3
llama_model_loader: - kv  33:                      tokenizer.ggml.tokens arr[str,129280]  = ["<｜begin▁of▁sentence｜>", "<�...
llama_model_loader: - kv  34:                  tokenizer.ggml.token_type arr[i32,129280]  = [3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...
llama_model_loader: - kv  35:                      tokenizer.ggml.merges arr[str,127741]  = ["Ġ t", "Ġ a", "i n", "Ġ Ġ", "h e...
llama_model_loader: - kv  36:                tokenizer.ggml.bos_token_id u32              = 0
llama_model_loader: - kv  37:                tokenizer.ggml.eos_token_id u32              = 1
llama_model_loader: - kv  38:            tokenizer.ggml.padding_token_id u32              = 1
llama_model_loader: - kv  39:               tokenizer.ggml.add_bos_token bool             = true
llama_model_loader: - kv  40:               tokenizer.ggml.add_eos_token bool             = false
llama_model_loader: - kv  41:                    tokenizer.chat_template str              = {% if not add_generation_prompt is de...
llama_model_loader: - kv  42:               general.quantization_version u32              = 2
llama_model_loader: - kv  43:                          general.file_type u32              = 2
llama_model_loader: - kv  44:                      quantize.imatrix.file str              = /models_out/DeepSeek-R1-GGUF/DeepSeek...
llama_model_loader: - kv  45:                   quantize.imatrix.dataset str              = /training_data/calibration_datav3.txt
llama_model_loader: - kv  46:             quantize.imatrix.entries_count i32              = 720
llama_model_loader: - kv  47:              quantize.imatrix.chunks_count i32              = 124
llama_model_loader: - kv  48:                                   split.no u16              = 0
llama_model_loader: - kv  49:                        split.tensors.count i32              = 1025
llama_model_loader: - kv  50:                                split.count u16              = 10
llama_model_loader: - type  f32:  361 tensors
llama_model_loader: - type q4_0:  652 tensors
llama_model_loader: - type q4_1:   11 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 353.00 GiB (4.52 BPW) 
load: special_eos_id is not in special_eog_ids - the tokenizer config may be incorrect
load: special tokens cache size = 818
load: token to piece cache size = 0.8223 MB
print_info: arch             = deepseek2
print_info: vocab_only       = 0
print_info: n_ctx_train      = 163840
print_info: n_embd           = 7168
print_info: n_layer          = 61
print_info: n_head           = 128
print_info: n_head_kv        = 128
print_info: n_rot            = 64
print_info: n_swa            = 0
print_info: n_swa_pattern    = 1
print_info: n_embd_head_k    = 192
print_info: n_embd_head_v    = 128
print_info: n_gqa            = 1
print_info: n_embd_k_gqa     = 24576
print_info: n_embd_v_gqa     = 16384
print_info: f_norm_eps       = 0.0e+00
print_info: f_norm_rms_eps   = 1.0e-06
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 18432
print_info: n_expert         = 256
print_info: n_expert_used    = 8
print_info: causal attn      = 1
print_info: pooling type     = 0
print_info: rope type        = 0
print_info: rope scaling     = yarn
print_info: freq_base_train  = 10000.0
print_info: freq_scale_train = 0.025
print_info: n_ctx_orig_yarn  = 4096
print_info: rope_finetuned   = unknown
print_info: ssm_d_conv       = 0
print_info: ssm_d_inner      = 0
print_info: ssm_d_state      = 0
print_info: ssm_dt_rank      = 0
print_info: ssm_dt_b_c_rms   = 0
print_info: model type       = 671B
print_info: model params     = 671.03 B
print_info: general.name     = DeepSeek R1
print_info: n_layer_dense_lead   = 3
print_info: n_lora_q             = 1536
print_info: n_lora_kv            = 512
print_info: n_ff_exp             = 2048
print_info: n_expert_shared      = 1
print_info: expert_weights_scale = 2.5
print_info: expert_weights_norm  = 1
print_info: expert_gating_func   = sigmoid
print_info: rope_yarn_log_mul    = 0.1000
print_info: vocab type       = BPE
print_info: n_vocab          = 129280
print_info: n_merges         = 127741
print_info: BOS token        = 0 '<｜begin▁of▁sentence｜>'
print_info: EOS token        = 1 '<｜end▁of▁sentence｜>'
print_info: EOT token        = 1 '<｜end▁of▁sentence｜>'
print_info: PAD token        = 1 '<｜end▁of▁sentence｜>'
print_info: LF token         = 201 'Ċ'
print_info: FIM PRE token    = 128801 '<｜fim▁begin｜>'
print_info: FIM SUF token    = 128800 '<｜fim▁hole｜>'
print_info: FIM MID token    = 128802 '<｜fim▁end｜>'
print_info: EOG token        = 1 '<｜end▁of▁sentence｜>'
print_info: max token length = 256
load_tensors: loading model tensors, this can take a while... (mmap = true)
load_tensors:  CPU_AARCH64 model buffer size = 350606.64 MiB
load_tensors:   CPU_Mapped model buffer size = 38134.87 MiB
load_tensors:   CPU_Mapped model buffer size = 35048.27 MiB
load_tensors:   CPU_Mapped model buffer size = 35048.27 MiB
load_tensors:   CPU_Mapped model buffer size = 35048.27 MiB
load_tensors:   CPU_Mapped model buffer size = 35048.27 MiB
load_tensors:   CPU_Mapped model buffer size = 35048.27 MiB
load_tensors:   CPU_Mapped model buffer size = 35048.27 MiB
load_tensors:   CPU_Mapped model buffer size = 35048.27 MiB
load_tensors:   CPU_Mapped model buffer size = 35048.27 MiB
load_tensors:   CPU_Mapped model buffer size = 22690.15 MiB
....................................................................................................
llama_context: constructing llama_context
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 4096
llama_context: n_ctx_per_seq = 4096
llama_context: n_batch       = 2048
llama_context: n_ubatch      = 512
llama_context: causal_attn   = 1
llama_context: flash_attn    = 0
llama_context: freq_base     = 10000.0
llama_context: freq_scale    = 0.025
llama_context: n_ctx_per_seq (4096) < n_ctx_train (163840) -- the full capacity of the model will not be utilized
llama_context:        CPU  output buffer size =     0.49 MiB
init: kv_size = 4096, offload = 1, type_k = 'f16', type_v = 'f16', n_layer = 61, can_shift = 0
init:        CPU KV buffer size = 19520.00 MiB
llama_context: KV self size  = 19520.00 MiB, K (f16): 11712.00 MiB, V (f16): 7808.00 MiB
llama_context:        CPU compute buffer size =  1186.01 MiB
llama_context: graph nodes  = 5086
llama_context: graph splits = 1
common_init_from_params: KV cache shifting is not supported for this context, disabling KV cache shifting
common_init_from_params: setting dry_penalty_last_n to ctx_size = 4096
common_init_from_params: warming up the model with an empty run - please wait ... (--no-warmup to disable)
main: llama threadpool init, n_threads = 64

system_info: n_threads = 64 (n_threads_batch = 64) / 96 | CPU : NEON = 1 | ARM_FMA = 1 | FP16_VA = 1 | MATMUL_INT8 = 1 | SVE = 1 | DOTPROD = 1 | SVE_CNT = 16 | OPENMP = 1 | AARCH64_REPACK = 1 | 

sampler seed: 1356072442
sampler params: 
        repeat_last_n = 64, repeat_penalty = 1.000, frequency_penalty = 0.000, presence_penalty = 0.000
        dry_multiplier = 0.000, dry_base = 1.750, dry_allowed_length = 2, dry_penalty_last_n = 4096
        top_k = 40, top_p = 0.950, min_p = 0.050, xtc_probability = 0.000, xtc_threshold = 0.100, typical_p = 1.000, top_n_sigma = -1.000, temp = 0.600
        mirostat = 0, mirostat_lr = 0.100, mirostat_ent = 5.000
sampler chain: logits -> logit-bias -> penalties -> dry -> top-k -> typical -> top-p -> min-p -> xtc -> temp-ext -> dist 
generate: n_ctx = 4096, n_batch = 2048, n_predict = 512, n_keep = 1

<|User|>Building a visually appealing website can be done in ten simple steps:<think>
Okay, so I need to figure out how to build a visually appealing website in ten simple steps. Let me start by brainstorming what I know about web design. First, I remember that a website's purpose is important. You need to know if it's for a business, a blog, or a portfolio. Without knowing the purpose, the design might not be effective. So maybe the first step is defining the website's goal and target audience. That makes sense.

Next, planning the structure. I think this involves creating a sitemap or wireframes. Wireframes are like blueprints for the website, right? They outline where each section goes without any design elements. So the second step could be planning the layout and structure with wireframes.

Choosing a color scheme and typography. Colors and fonts are crucial for visual appeal. They should align with the brand. Maybe using tools like Adobe Color or Coolors could help pick a cohesive palette. Typography should be readable and match the site's tone. So step three might be selecting colors and fonts.

Responsive design is a must nowadays. The website has to look good on all devices. Bootstrap or CSS frameworks can help with that. So step four could be ensuring responsive design.

High-quality visuals. Using good images and icons can make a site look professional. Maybe using stock photos from Unsplash or icons from Font Awesome. Also, optimizing images for fast loading times. So step five is about visuals and media.

Navigation should be intuitive. Menus and links need to be easy to find. Maybe a sticky header or a hamburger menu for mobile. Step six: user-friendly navigation.

Whitespace and balance. Cluttered websites are hard to look at. Using whitespace effectively to let content breathe. Aligning elements properly for visual harmony. Step seven: balance and spacing.

Consistency in design elements like buttons, headings, and CTAs. Keeping the same style throughout. Step eight: consistent UI elements.

Speed and performance. Even a beautiful site is bad if it's slow. Optimizing images, minifying CSS/JS, using a CDN. Step nine: optimizing performance.

Testing and iterating. Checking across browsers and devices, getting feedback, making adjustments. Step ten: testing and refining.

Wait, does that cover all ten steps? Let me count. 1. Define purpose, 2. Plan structure, 3. Colors and typography, 4. Responsive design, 5. Visuals, 6. Navigation, 7

llama_perf_sampler_print:    sampling time =      39.05 ms /   532 runs   (    0.07 ms per token, 13622.86 tokens per second)
llama_perf_context_print:        load time =  169556.41 ms
llama_perf_context_print: prompt eval time =     477.65 ms /    20 tokens (   23.88 ms per token,    41.87 tokens per second)
llama_perf_context_print:        eval time =   41756.98 ms /   511 runs   (   81.72 ms per token,    12.24 tokens per second)
llama_perf_context_print:       total time =   42340.53 ms /   531 tokens
```

The `system_info` printed from llama.cpp highlights important architectural features present on your hardware that improve the performance of the model execution. In the output shown above from running on an AWS Graviton4 instance, you will see:

  * NEON = 1 This flag indicates support for Arm's Neon technology which is an implementation of the Advanced SIMD instructions
  * ARM_FMA = 1 This flag indicates support for Arm Floating-point Multiply and Accumulate instructions 
  * MATMUL_INT8 = 1 This flag indicates support for Arm int8 matrix multiplication instructions
  * SVE = 1 This flag indicates support for the Arm Scalable Vector Extension


The end of the output shows several model timings:

* load time refers to the time taken to load the model.
* prompt eval time refers to the time taken to process the prompt before generating the new text. 
* eval time refers to the time taken to generate the output. Generally anything above 10 tokens per second is faster than what humans can read.

You have successfully run a LLM chatbot with Arm KleidiAI optimizations, all running on your Arm AArch64 CPU on your server. You can continue experimenting and trying out the model with different prompts.

