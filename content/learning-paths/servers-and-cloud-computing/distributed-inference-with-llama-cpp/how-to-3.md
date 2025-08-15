---
title: Configuring Master Node
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Master node setup
In this learning path, we will use the following two IP addresses for the worker nodes. Replace these with your own node IPs.

```bash
export worker_ips = "172.31.110.11:50052,172.31.110.12:50052"
```
You can find the IP addresses of your AWS instances in the AWS console.

You can verify communication with the worker nodes using the following command on master node:
```bash
telnet 172.31.110.11 50052
```
If the backend server is set up correctly, the output of the `telnet` command should look like the following:
```bash
Trying 172.31.110.11...
Connected to 172.31.110.11.
Escape character is '^]'.
```
Finally, you can execute the following command, to execute distributed inference:
```bash
bin/llama-cli -m ../../model.gguf -p "Tell me a joke" -n 128 --rpc "$worker_ips" -ngl 999
```

{{% notice Note %}}
It will take a significant amount of time (~30 minutes) to load the tensors on the worker nodes. Pre-loaded tensors are a current development request for llama.cpp.
{{% /notice %}}

Here are short definitions of the flags used in above command:
-n => Number of maximum output tokens
--rpc => list of backend workers
-ngl => Number of layers to be placed on backend workers (999 means offload all layers on workers)

{{% notice Note %}}At the time of publication, llama.cpp only supports up to 16 backend workers.{{% /notice %}}

The output:
```output
build: 5935 (2adf8d83) with cc (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 for aarch64-linux-gnu
main: llama backend init
main: load the model and apply lora adapter, if any
llama_model_load_from_file_impl: using device RPC[172.31.110.11:50052] (RPC[172.31.110.11:50052]) - 126497 MiB free
llama_model_load_from_file_impl: using device RPC[172.31.110.12:50052] (RPC[172.31.110.12:50052]) - 126497 MiB free
llama_model_loader: loaded meta data with 30 key-value pairs and 1138 tensors from /home/ubuntu/Llama-3.1-405B_Q4_0.gguf (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.type str              = model
llama_model_loader: - kv   2:                               general.name str              = Llama Hf
llama_model_loader: - kv   3:                         general.size_label str              = 406B
llama_model_loader: - kv   4:                            general.license str              = llama3.1
llama_model_loader: - kv   5:                               general.tags arr[str,6]       = ["facebook", "meta", "pytorch", "llam...
llama_model_loader: - kv   6:                          general.languages arr[str,8]       = ["en", "de", "fr", "it", "pt", "hi", ...
llama_model_loader: - kv   7:                          llama.block_count u32              = 126
llama_model_loader: - kv   8:                       llama.context_length u32              = 131072
llama_model_loader: - kv   9:                     llama.embedding_length u32              = 16384
llama_model_loader: - kv  10:                  llama.feed_forward_length u32              = 53248
llama_model_loader: - kv  11:                 llama.attention.head_count u32              = 128
llama_model_loader: - kv  12:              llama.attention.head_count_kv u32              = 8
llama_model_loader: - kv  13:                       llama.rope.freq_base f32              = 500000.000000
llama_model_loader: - kv  14:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  15:                 llama.attention.key_length u32              = 128
llama_model_loader: - kv  16:               llama.attention.value_length u32              = 128
llama_model_loader: - kv  17:                           llama.vocab_size u32              = 128256
llama_model_loader: - kv  18:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv  19:                       tokenizer.ggml.model str              = gpt2
llama_model_loader: - kv  20:                         tokenizer.ggml.pre str              = llama-bpe
llama_model_loader: - kv  21:                      tokenizer.ggml.tokens arr[str,128256]  = ["!", "\"", "#", "$", "%", "&", "'", ...
llama_model_loader: - kv  22:                  tokenizer.ggml.token_type arr[i32,128256]  = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...
llama_model_loader: - kv  23:                      tokenizer.ggml.merges arr[str,280147]  = ["Ġ Ġ", "Ġ ĠĠĠ", "ĠĠ ĠĠ", "...
llama_model_loader: - kv  24:                tokenizer.ggml.bos_token_id u32              = 128000
llama_model_loader: - kv  25:                tokenizer.ggml.eos_token_id u32              = 128001
llama_model_loader: - kv  26:               tokenizer.ggml.add_bos_token bool             = true
llama_model_loader: - kv  27:               tokenizer.ggml.add_sep_token bool             = false
llama_model_loader: - kv  28:               general.quantization_version u32              = 2
llama_model_loader: - kv  29:                          general.file_type u32              = 2
llama_model_loader: - type  f32:  254 tensors
llama_model_loader: - type q4_0:  883 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 213.13 GiB (4.51 BPW)
load: special tokens cache size = 256
load: token to piece cache size = 0.7999 MB
print_info: arch             = llama
print_info: vocab_only       = 0
print_info: n_ctx_train      = 131072
print_info: n_embd           = 16384
print_info: n_layer          = 126
print_info: n_head           = 128
print_info: n_head_kv        = 8
print_info: n_rot            = 128
print_info: n_swa            = 0
print_info: is_swa_any       = 0
print_info: n_embd_head_k    = 128
print_info: n_embd_head_v    = 128
print_info: n_gqa            = 16
print_info: n_embd_k_gqa     = 1024
print_info: n_embd_v_gqa     = 1024
print_info: f_norm_eps       = 0.0e+00
print_info: f_norm_rms_eps   = 1.0e-05
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 53248
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: causal attn      = 1
print_info: pooling type     = 0
print_info: rope type        = 0
print_info: rope scaling     = linear
print_info: freq_base_train  = 500000.0
print_info: freq_scale_train = 1
print_info: n_ctx_orig_yarn  = 131072
print_info: rope_finetuned   = unknown
print_info: model type       = ?B
print_info: model params     = 405.85 B
print_info: general.name     = Llama Hf
print_info: vocab type       = BPE
print_info: n_vocab          = 128256
print_info: n_merges         = 280147
print_info: BOS token        = 128000 '<|begin_of_text|>'
print_info: EOS token        = 128001 '<|end_of_text|>'
print_info: EOT token        = 128009 '<|eot_id|>'
print_info: EOM token        = 128008 '<|eom_id|>'
print_info: LF token         = 198 'Ċ'
print_info: EOG token        = 128001 '<|end_of_text|>'
print_info: EOG token        = 128008 '<|eom_id|>'
print_info: EOG token        = 128009 '<|eot_id|>'
print_info: max token length = 256
load_tensors: loading model tensors, this can take a while... (mmap = true)
....................................................................................................
llama_context: constructing llama_context
llama_context: non-unified KV cache requires ggml_set_rows() - forcing unified KV cache
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 4096
llama_context: n_ctx_per_seq = 4096
llama_context: n_batch       = 2048
llama_context: n_ubatch      = 512
llama_context: causal_attn   = 1
llama_context: flash_attn    = 0
llama_context: kv_unified    = true
llama_context: freq_base     = 500000.0
llama_context: freq_scale    = 1
llama_context: n_ctx_per_seq (4096) < n_ctx_train (131072) -- the full capacity of the model will not be utilized
llama_context:        CPU  output buffer size =     0.49 MiB
llama_kv_cache_unified: RPC[172.31.110.11:50052] KV buffer size =   800.00 MiB
llama_kv_cache_unified: RPC[172.31.110.12:50052] KV buffer size =   784.00 MiB
llama_kv_cache_unified:        CPU KV buffer size =   432.00 MiB
llama_kv_cache_unified: size = 2016.00 MiB (  4096 cells, 126 layers,  1/ 1 seqs), K (f16): 1008.00 MiB, V (f16): 1008.00 MiB
llama_kv_cache_unified: LLAMA_SET_ROWS=0, using old ggml_cpy() method for backwards compatibility
llama_context: RPC[172.31.110.11:50052] compute buffer size =  1160.00 MiB
llama_context: RPC[172.31.110.12:50052] compute buffer size =  1160.00 MiB
llama_context:        CPU compute buffer size =  1160.01 MiB
llama_context: graph nodes  = 4668
llama_context: graph splits = 4
common_init_from_params: added <|end_of_text|> logit bias = -inf
common_init_from_params: added <|eom_id|> logit bias = -inf
common_init_from_params: added <|eot_id|> logit bias = -inf
common_init_from_params: setting dry_penalty_last_n to ctx_size = 4096
common_init_from_params: warming up the model with an empty run - please wait ... (--no-warmup to disable)
main: llama threadpool init, n_threads = 64

system_info: n_threads = 64 (n_threads_batch = 64) / 64 | CPU : NEON = 1 | ARM_FMA = 1 | FP16_VA = 1 | MATMUL_INT8 = 1 | SVE = 1 | DOTPROD = 1 | SVE_CNT = 16 | OPENMP = 1 | REPACK = 1 |

sampler seed: 4077122424
sampler params:
	repeat_last_n = 64, repeat_penalty = 1.000, frequency_penalty = 0.000, presence_penalty = 0.000
	dry_multiplier = 0.000, dry_base = 1.750, dry_allowed_length = 2, dry_penalty_last_n = 4096
	top_k = 40, top_p = 0.950, min_p = 0.050, xtc_probability = 0.000, xtc_threshold = 0.100, typical_p = 1.000, top_n_sigma = -1.000, temp = 0.800
	mirostat = 0, mirostat_lr = 0.100, mirostat_ent = 5.000
sampler chain: logits -> logit-bias -> penalties -> dry -> top-n-sigma -> top-k -> typical -> top-p -> min-p -> xtc -> temp-ext -> dist
generate: n_ctx = 4096, n_batch = 2048, n_predict = 128, n_keep = 1

Tell me a joke! (or a funny story)
Thread starter Fiver
This thread is for any jokes you may want to share with other members. Please keep them clean!
Reactions: Fiver
A duck walks into a bar, and asks the bartender, "Have you got any bread?"
The bartender says, "No, we don't have any bread."
The duck leaves.
A few minutes later, the duck returns, and asks the bartender, "Have you got any bread?"
The bartender says, "No, I told you, we don't have any bread."
A few minutes later, the duck returns, and asks the bartender,

llama_perf_sampler_print:    sampling time =       9.48 ms /   133 runs   (    0.07 ms per token, 14032.50 tokens per second)
llama_perf_context_print:        load time = 1796754.73 ms
llama_perf_context_print: prompt eval time =    1925.98 ms /     5 tokens (  385.20 ms per token,     2.60 tokens per second)
llama_perf_context_print:        eval time =   77429.95 ms /   127 runs   (  609.68 ms per token,     1.64 tokens per second)
llama_perf_context_print:       total time =   79394.06 ms /   132 tokens
llama_perf_context_print:    graphs reused =          0
```
That's it! You have successfully run the llama-3.1-8B model on CPUs with the power of llama.cpp RPC functionality. The following table provides brief description of the metrics from `llama_perf`: 


| Log Line          | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| sampling time     | Time spent choosing next tokens using sampling strategy (e.g., top-k, top-p). |
| load time         | Time to load the model into memory and initialize weights/buffers.          |
| prompt eval time  | Time to process the input prompt tokens before generation (fills KV cache). |
| eval time         | Time to generate output tokens by forward-passing through the model.        |
| total time        | Total time for both prompt processing and token generation (excludes model load). |

Lastly to set up OpenAI compatible API, you can use the `llama-server` functionality. The process of implementing this is described [here](/learning-paths/servers-and-cloud-computing/llama-cpu) under the "Access the chatbot using the OpenAI-compatible API" section. Here is a snippet, for how to set up llama-server for distributed inference:
```bash
bin/llama-server -m ../../model.gguf --port 8080 --rpc "$worker_ips" -ngl 99
```
At the very end of the output to the above command, you will see something like the following:
```output
main: server is listening on http://127.0.0.1:8080 - starting the main loop
srv  update_slots: all slots are idle
```