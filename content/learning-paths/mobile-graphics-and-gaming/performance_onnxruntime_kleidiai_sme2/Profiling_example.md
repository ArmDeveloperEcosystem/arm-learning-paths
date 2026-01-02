---
title: Profiling – Use Resnet50v2 fp32 model as an example
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Profile an ONNX model – Use Resnet50v2 as an example 
The Resnet50v2 fp32 ONNX model can be downloaded from Hugging Face or Modescope.

The Android device that we used is a VIVO X300 phone with MTK D9500 processor, which has Arm C1-Ultra, C1-Premium and C1-Pro CPU cores with SME2 support on it. We chose a C1-Pro CPU core running at 2.0GHz to run the onnxruntime_perf_test benchmark application. You can use any other Android device with SME2 support.

To compare the performance of running Resnet50v2 on ORT with SME2 and without SME2 support, we built two versions of ORT, one with SME2 support (set *onnxruntime_USE_KLEIDIAI=ON* when building ORT), the other without SME2 support(*onnxruntime_USE_KLEIDIAI=OFF* when building ORT).

Run following command on the device,
```bash
taskset 1 ./onnxruntime_perf_test  -e cpu -r 5 -m times -s -Z  -x 1   ./resnet50v2.onnx  -p "resnet50v2.onnx_1xC1-Pro_profile
```

The *taskset 1* in the command sets the CPU affinity of *onnxruntime_perf_test* benchmark to CPU core 0, which is a C1-Pro CPU core. 
*-x 1* in the command sets the number of threads used to parallelize the execution within nodes as 1 (single thread).

Here is output from running onnxruntime_perf_test with ORT with SME2 support as below.
```text
Setting intra_op_num_threads to 1
Disabling intra-op thread spinning between runs
Session creation time cost: 0.217932 s
First inference time cost: 196 ms
Total inference time cost: 0.49481 s
Total inference requests: 5
Average inference time cost total: 98.961997 ms
Total inference run time: 0.494854 s
Number of inferences per second: 10.104
Avg CPU usage: 11 %
Peak working set size: 271122432 bytes
Avg CPU usage:11
Peak working set size:271122432
Runs:5
Min Latency: 0.0958204 s
Max Latency: 0.101519 s
P50 Latency: 0.0995086 s
P90 Latency: 0.101519 s
P95 Latency: 0.101519 s
P99 Latency: 0.101519 s
P999 Latency: 0.101519 s
``` 

Here is output from running onnxruntime_perf_test with ORT without SME2 support as below.
```text
Setting intra_op_num_threads to 1
Disabling intra-op thread spinning between runs
Session creation time cost: 0.227282 s
First inference time cost: 343 ms
Total inference time cost: 1.69691 s
Total inference requests: 5
Average inference time cost total: 339.381120 ms
Total inference run time: 1.69697 s
Number of inferences per second: 2.94642
Avg CPU usage: 11 %
Peak working set size: 241426432 bytes
Avg CPU usage:11
Peak working set size:241426432
Runs:5
Min Latency: 0.333323 s
Max Latency: 0.34682 s
P50 Latency: 0.336476 s
P90 Latency: 0.34682 s
P95 Latency: 0.34682 s
P99 Latency: 0.34682 s
P999 Latency: 0.34682 s
```
### Performance Indicators
| Metric   | Non-KleidiAI  | KleidiAI (with SME2)     | Speed Up                                |
|---------|----------------|----------------|-------------------------------------------------|
| Latency per inference (ms) | 339           | 99  | >3.4       |

We can use [prefetto tool](https://ui.perfetto.dev/), to view the two JSON profile files.

The figure below is a screenshot of the view of the Non-KleidiAI version of JSON profile file.  
The selected part(one model_run/SequentialExecutor) in the figure includes information of one inference execution.

![Figure showing profile file of Non-KleidiAI version alt-text#center](images/resnet50v2_no_sme_prefetto.png "prefetto view of Non-KleidiAI version of ORT")

The figure below is a screenshot of the view of the KleidiAI(with SME2) version of JSON profile file.  
The selected part (one model_run/SequentialExecutor) in the figure includes information of one inference execution.
![Figure showing profile file of KleidiAI with SME2 version alt-text#center](images/resnet50v2_sme_prefetto.png "prefetto view of KleidiAI with SME2 version of ORT")

We also convert the two JSON profile files to CSV sheets, then we combine the individual operator execution time of the Non-KleidiAI and KleidiAI(with SME2) version to a single chart. 
![Figure showing operator time of both versions of ORT alt-text#center](images/resnet50v2_with_sme_without_sme_2.png "Operator execution time comparison")

It shows that ORT with KleidiAI (with SME2) kernels uplifts the performance significantly, especially for convolution operators.

If we use Arm Streamline tools and PMU counters for further investigation, in the timeline view of Streamline, we can see SME2 floating point Outer Product and Accumulate (MOPA) instruction is used intensively during the inference.

![Figure showing SME2 instructions and cycles alt-text#center](images/resnet50v2_sme_onnx_streamline_1xgelas_annotation.png "SME2 instructions and cycles shown in Streamline")

Then we combine the function call view of ORT without KleidiAI and with KleidiAI(with SME2) from Streamline to a single figure,

![Figure showing function call percentage of both versions of ORT alt-text#center](images/function_call_compare.png "Function call percentage of both versions of ORT in Streamline ")

It shows that KleidiAI kernels provide a significant performance uplift for convolution operators compared to the default MLSA kernels (*MlasSgemmKernelAdd* and *MlasSgemmKernelZero*).

## Summary
By integrating KleidiAI (SME2) into ONNX Runtime, you unlock the massive parallel processing power of Arm SME2. This turns the Arm CPU from a "fallback" into a high-performance AI engine capable of running LLMs and complex vision models locally on devices.