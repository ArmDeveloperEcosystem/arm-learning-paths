---
title: Benchmark the LiteRT model
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Use the benchmark tool

First, you should check if your Android phone supports SME2. You can check it by the following command.

``` bash
cat /proc/cpuinfo

...
processor	: 7
BogoMIPS	: 2000.00
Features	: fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma lrcpc dcpop sha3 sm3 sm4 asimddp sha512 sve asimdfhm dit uscat ilrcpc flagm ssbs sb dcpodp sve2 sveaes svepmull svebitperm svesha3 svesm4 flagm2 frint svei8mm svebf16 i8mm bf16 dgh bti mte ecv afp mte3 sme smei8i32 smef16f32 smeb16f32 smef32f32 wfxt rprfm sme2 smei16i32 smebi32i32 hbc lrcpc3
```

As you can see from the `Features`, the CPU 7 supports the SME2.

Then, you can run the `benchmark_model` tool on the CPU that supports the SME2. One of the example is as follows. 

This example uses the `taskset` command to configure the benchmark workload to run on cores 7. It specifies to utilize 1 thread by the option `--num_threads=1`, and running the inferences at least 1000 times by the option `--num_runs=1000`. The CPU is selected. Also, it passes the option `--use_profiler=true` to produce a operator level profiling during inference.

``` bash
taskset 80 ./benchmark_model --graph=./fc_fp32.tflite --num_runs=1000 --num_threads=1 --use_cpu=true --use_profiler=true

...
INFO: [litert/runtime/accelerators/auto_registration.cc:148] CPU accelerator registered.
INFO: [litert/runtime/compiled_model.cc:415] Flatbuffer model initialized directly from incoming litert model.
INFO: Initialized TensorFlow Lite runtime.
INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
VERBOSE: Replacing 1 out of 1 node(s) with delegate (TfLiteXNNPackDelegate) node, yielding 1 partitions for subgraph 0.
INFO: The input model file size (MB): 3.27774
INFO: Initialized session in 4.478ms.
INFO: Running benchmark for at least 1 iterations and at least 0.5 seconds but terminate if exceeding 150 seconds.
INFO: count=1055 first=1033 curr=473 min=443 max=1033 avg=465.319 std=18 p5=459 median=463 p95=478

INFO: Running benchmark for at least 1000 iterations and at least 1 seconds but terminate if exceeding 150 seconds.
INFO: count=2112 first=463 curr=459 min=442 max=979 avg=464.545 std=13 p5=460 median=462 p95=478

INFO: [./litert/tools/benchmark_litert_model.h:81] 
========== BENCHMARK RESULTS ==========
INFO: [./litert/tools/benchmark_litert_model.h:82] Model initialization: 4.48 ms
INFO: [./litert/tools/benchmark_litert_model.h:84] Warmup (first):       1.03 ms
INFO: [./litert/tools/benchmark_litert_model.h:86] Warmup (avg):         0.47 ms (1055 runs)
INFO: [./litert/tools/benchmark_litert_model.h:88] Inference (avg):      0.46 ms (2112 runs)
INFO: [./litert/tools/benchmark_litert_model.h:92] Inference (min):      0.44 ms
INFO: [./litert/tools/benchmark_litert_model.h:94] Inference (max):      0.98 ms
INFO: [./litert/tools/benchmark_litert_model.h:96] Inference (std):      0.01
INFO: [./litert/tools/benchmark_litert_model.h:103] Throughput:           525.55 MB/s
INFO: [./litert/tools/benchmark_litert_model.h:112] 
Memory Usage:
INFO: [./litert/tools/benchmark_litert_model.h:114] Init footprint:       8.94 MB
INFO: [./litert/tools/benchmark_litert_model.h:116] Overall footprint:    11.51 MB
INFO: [./litert/tools/benchmark_litert_model.h:123] Peak memory usage not available. (peak_mem_mb <= 0)
INFO: [./litert/tools/benchmark_litert_model.h:126] ======================================

INFO: [./litert/tools/benchmark_litert_model.h:179] 
============================== Run Order ==============================
	                             [node type]	  [first]	 [avg ms]	     [%]	  [cdf%]	  [mem KB]	[times called]	[Name]
	        LiteRT::Run[buffer registration]	    0.020	    0.014	  3.309%	  3.309%	     0.000	        1	LiteRT::Run[buffer registration]/0
	                         AllocateTensors	    0.291	    0.291	  0.022%	  3.331%	   452.000	        0	AllocateTensors/0
	                     Static Reshape (NC)	    0.085	    0.003	  0.739%	  4.070%	     0.000	        1	Delegate/Static Reshape (NC):0
	         Fully Connected (NC, PF32) GEMM	    0.538	    0.382	 92.948%	 97.018%	     0.000	        1	Delegate/Fully Connected (NC, PF32) GEMM:1
	                LiteRT::Run[Buffer sync]	    0.013	    0.012	  2.982%	100.000%	     0.000	        1	LiteRT::Run[Buffer sync]/0

============================== Top by Computation Time ==============================
	                             [node type]	  [first]	 [avg ms]	     [%]	  [cdf%]	  [mem KB]	[times called]	[Name]
	         Fully Connected (NC, PF32) GEMM	    0.538	    0.382	 92.948%	 92.948%	     0.000	        1	Delegate/Fully Connected (NC, PF32) GEMM:1
	                         AllocateTensors	    0.291	    0.291	  0.022%	 92.970%	   452.000	        0	AllocateTensors/0
	        LiteRT::Run[buffer registration]	    0.020	    0.014	  3.309%	 96.279%	     0.000	        1	LiteRT::Run[buffer registration]/0
	                LiteRT::Run[Buffer sync]	    0.013	    0.012	  2.982%	 99.261%	     0.000	        1	LiteRT::Run[Buffer sync]/0
	                     Static Reshape (NC)	    0.085	    0.003	  0.739%	100.000%	     0.000	        1	Delegate/Static Reshape (NC):0

Number of nodes executed: 5
============================== Summary by node type ==============================
	                             [Node type]	  [count]	  [avg ms]	    [avg %]	    [cdf %]	  [mem KB]	[times called]
	         Fully Connected (NC, PF32) GEMM	        1	     0.382	    93.171%	    93.171%	     0.000	        1
	        LiteRT::Run[buffer registration]	        1	     0.013	     3.171%	    96.341%	     0.000	        1
	                LiteRT::Run[Buffer sync]	        1	     0.012	     2.927%	    99.268%	     0.000	        1
	                     Static Reshape (NC)	        1	     0.003	     0.732%	   100.000%	     0.000	        1
	                         AllocateTensors	        1	     0.000	     0.000%	   100.000%	   452.000	        0

Timings (microseconds): count=3166 first=947 curr=406 min=390 max=947 avg=411.071 std=14
Memory (bytes): count=0
5 nodes observed
```

As you can see from the results above, the results include the time spent on model initialization, warm-up, and inference, as well as memory usage. Since the profiler was enabled, the output also reports the execution time of each operator.

Because the model contains only a single fully connected layer, the node type `Fully Connected (NC, PF32) GEMM` shows the average execution time is 0.382 ms, accounting for 93.171% of the total inference time.

{{% notice Note %}}
To verify the KleidiAI SME2 micro-kernels are invoked for the Fully Connected operator during the model inference, you can use the `simpleperf record -g -- <workload>` to capture the calling graph. For the benchmark_model, you should also build it with the option `-c dbg`.
{{% /notice %}}

## Measure the performance impact of KleidiAI SME2 micro-kernels

To compare the performance of the KleidiAI SME2 implementation with the original XNNPACK implementation, you can run the `benchmark_model` tool without KleidiAI enabled and then benchmark again using the same parameters.

One example is as follows.

``` bash
taskset 80 ./benchmark_model --graph=./fc_fp32.tflite --num_runs=1000 --num_threads=1 --use_cpu=true --use_profiler=true

...
INFO: [litert/runtime/accelerators/auto_registration.cc:148] CPU accelerator registered.
INFO: [litert/runtime/compiled_model.cc:415] Flatbuffer model initialized directly from incoming litert model.
INFO: Initialized TensorFlow Lite runtime.
INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
VERBOSE: Replacing 1 out of 1 node(s) with delegate (TfLiteXNNPackDelegate) node, yielding 1 partitions for subgraph 0.
INFO: The input model file size (MB): 3.27774
INFO: Initialized session in 4.488ms.
INFO: Running benchmark for at least 1 iterations and at least 0.5 seconds but terminate if exceeding 150 seconds.
INFO: count=358 first=1927 curr=1370 min=1363 max=1927 avg=1386.31 std=38 p5=1366 median=1377 p95=1428

INFO: Running benchmark for at least 1000 iterations and at least 1 seconds but terminate if exceeding 150 seconds.
INFO: count=1000 first=1407 curr=1370 min=1362 max=1452 avg=1379.64 std=14 p5=1365 median=1373 p95=1409

INFO: [./litert/tools/benchmark_litert_model.h:81] 
========== BENCHMARK RESULTS ==========
INFO: [./litert/tools/benchmark_litert_model.h:82] Model initialization: 4.49 ms
INFO: [./litert/tools/benchmark_litert_model.h:84] Warmup (first):       1.93 ms
INFO: [./litert/tools/benchmark_litert_model.h:86] Warmup (avg):         1.39 ms (358 runs)
INFO: [./litert/tools/benchmark_litert_model.h:88] Inference (avg):      1.38 ms (1000 runs)
INFO: [./litert/tools/benchmark_litert_model.h:92] Inference (min):      1.36 ms
INFO: [./litert/tools/benchmark_litert_model.h:94] Inference (max):      1.45 ms
INFO: [./litert/tools/benchmark_litert_model.h:96] Inference (std):      0.01
INFO: [./litert/tools/benchmark_litert_model.h:103] Throughput:           176.96 MB/s
INFO: [./litert/tools/benchmark_litert_model.h:112] 
Memory Usage:
INFO: [./litert/tools/benchmark_litert_model.h:114] Init footprint:       9.07 MB
INFO: [./litert/tools/benchmark_litert_model.h:116] Overall footprint:    11.25 MB
INFO: [./litert/tools/benchmark_litert_model.h:123] Peak memory usage not available. (peak_mem_mb <= 0)
INFO: [./litert/tools/benchmark_litert_model.h:126] ======================================

INFO: [./litert/tools/benchmark_litert_model.h:179] 
============================== Run Order ==============================
	                             [node type]	  [first]	 [avg ms]	     [%]	  [cdf%]	  [mem KB]	[times called]	[Name]
	        LiteRT::Run[buffer registration]	    0.026	    0.018	  1.392%	  1.392%	     0.000	        1	LiteRT::Run[buffer registration]/0
	                         AllocateTensors	    0.195	    0.195	  0.011%	  1.403%	    56.000	        0	AllocateTensors/0
	                     Static Reshape (NC)	    0.004	    0.004	  0.307%	  1.710%	     0.000	        1	Delegate/Static Reshape (NC):0
	          Fully Connected (NC, F32) GEMM	    1.564	    1.269	 97.059%	 98.769%	     0.000	        1	Delegate/Fully Connected (NC, F32) GEMM:1
	                LiteRT::Run[Buffer sync]	    0.018	    0.016	  1.231%	100.000%	     0.000	        1	LiteRT::Run[Buffer sync]/0

============================== Top by Computation Time ==============================
	                             [node type]	  [first]	 [avg ms]	     [%]	  [cdf%]	  [mem KB]	[times called]	[Name]
	          Fully Connected (NC, F32) GEMM	    1.564	    1.269	 97.059%	 97.059%	     0.000	        1	Delegate/Fully Connected (NC, F32) GEMM:1
	                         AllocateTensors	    0.195	    0.195	  0.011%	 97.070%	    56.000	        0	AllocateTensors/0
	        LiteRT::Run[buffer registration]	    0.026	    0.018	  1.392%	 98.462%	     0.000	        1	LiteRT::Run[buffer registration]/0
	                LiteRT::Run[Buffer sync]	    0.018	    0.016	  1.231%	 99.693%	     0.000	        1	LiteRT::Run[Buffer sync]/0
	                     Static Reshape (NC)	    0.004	    0.004	  0.307%	100.000%	     0.000	        1	Delegate/Static Reshape (NC):0

Number of nodes executed: 5
============================== Summary by node type ==============================
	                             [Node type]	  [count]	  [avg ms]	    [avg %]	    [cdf %]	  [mem KB]	[times called]
	          Fully Connected (NC, F32) GEMM	        1	     1.268	    97.090%	    97.090%	     0.000	        1
	        LiteRT::Run[buffer registration]	        1	     0.018	     1.378%	    98.469%	     0.000	        1
	                LiteRT::Run[Buffer sync]	        1	     0.016	     1.225%	    99.694%	     0.000	        1
	                     Static Reshape (NC)	        1	     0.004	     0.306%	   100.000%	     0.000	        1
	                         AllocateTensors	        1	     0.000	     0.000%	   100.000%	    56.000	        0

Timings (microseconds): count=1357 first=1807 curr=1295 min=1291 max=1807 avg=1307.19 std=21
Memory (bytes): count=0
5 nodes observed
```

As you can see from the results, for the same model, the XNNPACK node type name is different. For the non-KleidiAI implementation, the node type is `Fully Connected (NC, F32) GEMM`, whereas for the KleidiAI implementation, it is `Fully Connected (NC, PF32) GEMM`.

For other operators supported by KleidiAI, the per-operator profiling node types differ between the implementations with and without KleidiAI enabled in XNNPACK as follows:

| Operator                               | Node Type (KleidiAI Enabled)                          | Node Type (KleidiAI Disabled)                          |
|----------------------------------------|-------------------------------------------------------|--------------------------------------------------------|
| Fully Connected / Conv2D (Pointwise)   | Fully Connected (NC, PF32)                            | Fully Connected (NC, F32)                              |
| Fully Connected                        | Dynamic Fully Connected (NC, PF32)                    | Dynamic Fully Connected (NC, F32)                      |
| Fully Connected / Conv2D (Pointwise)   | Fully Connected (NC, PF16)                            | Fully Connected (NC, F16)                              |
| Fully Connected                        | Dynamic Fully Connected (NC, PF16)                    | Dynamic Fully Connected (NC, F16)                      |
| Fully Connected                        | Fully Connected (NC, QP8, F32, QC4W)                  | Fully Connected (NC, QD8, F32, QC4W)                   |
| Fully Connected / Conv2D (Pointwise)   | Fully Connected (NC, QP8, F32, QC8W)                  | Fully Connected (NC, QD8, F32, QC8W)                   |
| Fully Connected / Conv2D (Pointwise)   | Fully Connected (NC, PQS8, QC8W)                      | Fully Connected (NC, QS8, QC8W)                        |
| Batch Matrix Multiply                  | Batch Matrix Multiply (NC, PF32)                      | Batch Matrix Multiply (NC, F32)                        |
| Batch Matrix Multiply                  | Batch Matrix Multiply (NC, PF16)                      | Batch Matrix Multiply (NC, F16)                        |
| Batch Matrix Multiply                  | Batch Matrix Multiply (NC, QP8, F32, QC8W)            | Batch Matrix Multiply (NC, QD8, F32, QC8W)             |
| Conv2D                                 | Convolution (NHWC, PQS8, QS8, QC8W)                   | Convolution (NHWC, QC8)                                |
| TransposeConv                          | Deconvolution (NHWC, PQS8, QS8, QC8W)                 | Deconvolution (NC, QS8, QC8W)                          |

As you can see from the list, the letter “P” indicates that the node type corresponds to a KleidiAI implementation.

For example, in `Convolution (NHWC, PQS8, QS8, QC8W)`, this represents a Conv2D operator computation by KleidiAI micro-kernel, where the tensor is in NHWC layout.

* The input is packed INT8 quantized,
* The weights are per-channel INT8 quantized,
* The output is INT8 quantized.