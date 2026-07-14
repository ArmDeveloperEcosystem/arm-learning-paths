---
title: Accelerate with KleidiAI
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## KleidiAI packing and tiling

Getting close to peak matmul performance is complex, especially in transformer inference where one kernel runs many times per token. Raw SIMD intrinsics can accelerate execution, but higher-level algorithms can improve matrix multiplication through techniques such as packing and tiling.

- *Packing* is a preprocessing step which rearranges matrix data into a layout that matches the compute kernel, which reduces cache misses and improves contiguous vector loads. 

- *Tiling* breaks large matrices into smaller blocks that fit better in cache, so data is reused more often and memory bandwidth pressure is lower.
Arm created [KleidiAI](https://github.com/ARM-software/kleidiai) to provide the fastest Arm CPU microkernels on packing and tiled matrix multiplication so you can use these optimizations without writing and tuning every low-level kernel yourself.

## KleidiAI integration in the GPT-2 example

The file `src/kernels/matmul_kai_sve.cpp` is the runtime bridge between your model code and a KleidiAI float32 SVE microkernel. Since packing is a preprocessing step, this workflow uses a slightly modified inference engine, `gpt2_kai_sve.cpp`. It builds a `kai_matmul_clamp_f32_f32_f32p_ukernel` function table and binds function pointers such as:

- `kai_get_n_step_matmul_clamp_f32_f32_f32p4vlx1b_6x4vl_sve_mla`
- `kai_get_rhs_packed_offset_matmul_clamp_f32_f32_f32p4vlx1b_6x4vl_sve_mla`
- `kai_run_matmul_clamp_f32_f32_f32p4vlx1b_6x4vl_sve_mla`

The `kai_run_matmul_clamp_f32_f32_f32p4vlx1b_6x4vl_sve_mla` is our entry. As per [the naming convention](https://github.com/ARM-software/kleidiai/blob/main/kai/ukernels/matmul/README.md), this kernel performs an FP32 matrix multiplication, computing output tiles of 6 × 4VL (6 rows by four SVE vector lengths of columns) using SVE (multiply–accumulate) MLA instructions on prepacked RHS weights for efficient cache and SIMD utilization.

For more details on KleidiAI, please refer to the [official GitLab repository](https://gitlab.arm.com/kleidi/kleidiai).

## Key source code

All matmul implementations in `src/kernels/` follow the same high-level pattern from `matmul.h`: they compute float32 output from float32 input vectors and weights. The KleidiAI variant keeps this behavior but changes the RHS argument to a packed buffer (`const uint8_t* rhs_packed`) so the compute path can consume prepacked tiles.

The header interface in KleidiAI defines the core run method through the ukernel function table, and this path uses the float32-to-float32 kernel family (`f32_f32_f32p`).

```cpp
static const kai_matmul_clamp_f32_f32_f32p_ukernel ukernel = {
	/* geometry helpers */
	kai_get_n_step_matmul_clamp_f32_f32_f32p4vlx1b_6x4vl_sve_mla,
	kai_get_rhs_packed_offset_matmul_clamp_f32_f32_f32p4vlx1b_6x4vl_sve_mla,
	/* core compute */
	kai_run_matmul_clamp_f32_f32_f32p4vlx1b_6x4vl_sve_mla,
};

const size_t n_step = ukernel.get_n_step();
const size_t n_blocks = ((size_t)n_out + n_step - 1) / n_step;
const size_t rhs_offset = ukernel.get_rhs_packed_offset(n_start, k);

ukernel.run_matmul(m, n_step, k, x, lhs_stride,
				   rhs_packed + rhs_offset,
				   out + n_start, dst_stride_row, dst_stride_col,
				   -FLT_MAX, FLT_MAX);
```

The execution flow is:

1. Query kernel tile size (`n_step`) from the ukernel interface.
2. Split output columns into `n_step` blocks, which are smaller sub-matrices.
3. Use `get_rhs_packed_offset(...)` to locate the packed RHS chunk for each block.
4. Call `run_matmul(...)` for each block, with optional thread-level parallelism.

In `src/gpt2_kai_sve.cpp`, runtime code prepares packed weights once with `kai_run_rhs_pack_kxn_x32p4vlx1b_x32_x32_sve`, stores them in `PackedWeights`, and calls `kernels::matmul_kai_sve(...)` at runtime. This is why the runtime file and `matmul_kai_sve.cpp` must match: the runtime produces packed buffers in the format expected by the same f32 ukernel family.


## SVE intrinsics versus KleidiAI

Run the comparison script from the repository root with the following command.

```bash { command_line="ubuntu@ip | 2-30"}
./compare_gpt2_variants.sh kai
Model: gpt2-medium
Prompt: Once upon a time
Tokens: 20
Runs: 1
KleidiAI matmul threads (--matmul-threads): 1

== gpt2 ==
run 1: 3.04907 tok/s
avg: 3.049070 tok/s

== gpt2_neon ==
run 1: 11.4139 tok/s
avg: 11.413900 tok/s

== gpt2_sve ==
run 1: 13.7321 tok/s
avg: 13.732100 tok/s

== gpt2_kai_sve ==
run 1: 15.9847 tok/s
avg: 15.984700 tok/s

== gpt2_user ==
run 1: 3.04784 tok/s
avg: 3.047840 tok/s
```

`gpt2_sve` uses SVE intrinsics directly but does not use KleidiAI packing and microkernel dispatch. `gpt2_kai_sve` adds those optimized packing and ukernel paths, which is why throughput is higher in this workload. Compared to the non-vectorized baseline (`gpt2`), this FP32 KleidiAI microkernel path achieves about a 5.4x speedup in this example, without quantization.


### Run with multiple threads

You can increase throughput by running the KleidiAI path with multiple matmul threads. For this 355M model, tune `--matmul-threads` heuristically on your target system to find the optimal value. For our Graviton 3 instance, we observe a max token generation speed of 34.5 token/s with 4 threads.


``` bash { command_line="ubuntu@ip | 3-50"}
cd build
./gpt2_kai_sve --model gpt2-medium "Once upon a time" -n 150 --matmul-threads 4
Weights path: /home/ubuntu/GPT-2-DEMO/GPT-2-Example/models/gpt2-medium/weights.bin
Vocab path: /home/ubuntu/GPT-2-DEMO/GPT-2-Example/models/gpt2-medium/vocab.bin
Matmul threads: 4
GPT-2  embd=1024  layers=24  heads=16  vocab=50257
  loaded wte (51463168)
  loaded wpe (1048576)
  loaded ln1_w (24576)
  loaded ln1_b (24576)
  loaded c_attn_w (75497472)
  loaded c_attn_b (73728)
  loaded c_proj_w (25165824)
  loaded c_proj_b (24576)
  loaded ln2_w (24576)
  loaded ln2_b (24576)
  loaded mlp_fc_w (100663296)
  loaded mlp_fc_b (98304)
  loaded mlp_pj_w (100663296)
  loaded mlp_pj_b (24576)
  loaded ln_f_w (1024)
  loaded ln_f_b (1024)
Packed weights for 24 layers + logit projection
Tokeniser: 50257 tokens, 50000 merges
[4 prompt tokens]
Once upon a time, there was a village with three boys running around. They were starting to want to be strong, go out into the town and fight. As the boys were growing up, they wanted to become the strongest of all the boys in the village. The trouble was that the village elders told them that if they didn't go out into the village to participate in the weekly martial arts training, they would suffer the wrath of God.

They would be kicked out of the village, and they would suffer and die as punishment. So the boys created a forest village, then entered the forest to start training. They, one by one, went out into the forest, and from day to day, they put more and more effort into their martial arts.

[150 tokens, 34.5787 tok/s]

```

## Summary

You used Arm Performix Instruction Mix to detect scalar-heavy hot paths, validated vectorization changes with static and dynamic evidence, and compared baseline, Neon, SVE, and KleidiAI-backed matmul implementations. Starting from roughly 3 tok/s with scalar code, you reached about 15 tok/s with SVE intrinsics and 35 tok/s with KleidiAI packing, tiling, and multithreading.

This workflow is transferable to your own codebase: use instruction mix to detect missed vectorization and other unexpected instruction-balance patterns, validate changes with static and runtime evidence, and then tune to meet your performance requirements.