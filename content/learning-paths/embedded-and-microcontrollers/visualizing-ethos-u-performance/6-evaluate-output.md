---
# User change
title: "Evaluate Ethos-U Performance"

weight: 7 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Observe Ahead-of-Time Compilation
- The below output snippet from [run.sh](https://github.com/pytorch/executorch/blob/main/examples/arm/run.sh) is how you can confirm ahead-of-time compilation
- Specifically you want to see that the original PyTorch model was converted to an ExecuTorch `.pte` file
- For the MobileNet V2 example, the compiled ExecuTorch file will be output as `mv2_arm_delegate_ethos-u85-128.pte`

{{% notice Note %}}

In the below sample outputs, the `executorch` directory path is indicated as `/path/to/executorch`. Your actual path will depend on where you cloned your local copy of the [executorch repo](https://github.com/pytorch/executorch/tree/main).

{{% /notice %}}

**Ahead-of-Time Compiler Start:**
```bash { output_lines = "1-4" }
--------------------------------------------------------------------------------
Running e2e flow for model 'mv2' with flags '--delegate --quantize --delegate --quantize --intermediates mv2_u85/ --debug --evaluate'
--------------------------------------------------------------------------------
CALL python3 -m examples.arm.aot_arm_compiler --model_name=mv2 --target=ethos-u85-128 --delegate --quantize --delegate --quantize --intermediates mv2_u85/ --debug --evaluate --intermediate=/path/to/executorch/mv2_u85 --output=/path/to/executorch/mv2_u85/mv2_arm_delegate_ethos-u85-128.pte --system_config=Ethos_U85_SYS_DRAM_Mid --memory_mode=Sram_Only
```

**.pte File Build Completion:**
```bash { output_lines = "1-3" }
PTE file saved as /path/to/executorch/mv2_u85/mv2_arm_delegate_ethos-u85-128.pte
pte_data_size:  3809584 /path/to/executorch/mv2_u85/mv2_arm_delegate_ethos-u85-128.pte
pte_file: /path/to/executorch/mv2_u85/mv2_arm_delegate_ethos-u85-128.pte
```

**Ethos-U Delegate Build Start:**
```bash{ output_lines = "1-5" }
+ backends/arm/scripts/build_executor_runner.sh --et_build_root=/path/to/executorch/arm_test --pte=/path/to/executorch/mv2_u85/mv2_arm_delegate_ethos-u85-128.pte --build_type=Release --target=ethos-u85-128 --system_config=Ethos_U85_SYS_DRAM_Mid --memory_mode=Sram_Only --extra_build_flags= --ethosu_tools_dir=/path/to/executorch/examples/arm/ethos-u-scratch
--------------------------------------------------------------------------------
Build Arm Baremetal executor_runner for ethos-u85-128 with /path/to/executorch/mv2_u85/mv2_arm_delegate_ethos-u85-128.pte using Ethos_U85_SYS_DRAM_Mid Sram_Only  to '/path/to/executorch/mv2_u85/mv2_arm_delegate_ethos-u85-128/cmake-out'
--------------------------------------------------------------------------------
```

**Ethos-U Delegate Build Completion:**
```bash { output_lines = "1" }
[100%] Built target arm_executor_runner
```

## Observe Test Batch Performance
By default, `run.sh` (and the underlying ethos_u_runner) uses:
- A constant input tensor, usually filled with zeros, ones, or random-ish synthetic data
- Input shape matches MobileNet V2: typically `[1, 3, 224, 224]` (batch size 1, 3 RGB channels, 224×224 image)
- Input tensor size: `1 × 3 × 224 × 224 × 1 byte = 150528 bytes ≈ 147 KB`
  ```bash { output_lines = "1" }
  Input   SRAM bandwidth = 15.49 MB/batch
  ```
- `Batch Inference time` gives you a single performance metric for the Ethos-U85 (versus other [Ethos-U NPUs](https://developer.arm.com/Processors#q=Ethos-U&aq=%40navigationhierarchiescategories%3D%3D%22Processor%20products%22%20AND%20%40navigationhierarchiescontenttype%3D%3D%22Product%20Information%22&numberOfResults=48))
   ```bash { output_lines = "1" }
   Batch Inference time                 4.94 ms,  202.34 inferences/s (batch size 1)
   ```

**Test Batch Performance:**
```bash { output_lines = "1-34" }
Network summary for out
Accelerator configuration               Ethos_U85_128
System configuration             Ethos_U85_SYS_DRAM_Mid
Memory mode                                 Sram_Only
Accelerator clock                                1000 MHz
Design peak SRAM bandwidth                      29.80 GB/s

Total SRAM used                               5178.77 KiB

CPU operators = 0 (0.0%)
NPU operators = 64 (100.0%)

Average SRAM bandwidth                           7.21 GB/s
Input   SRAM bandwidth                          15.49 MB/batch
Weight  SRAM bandwidth                          11.87 MB/batch
Output  SRAM bandwidth                           6.66 MB/batch
Total   SRAM bandwidth                          35.65 MB/batch
Total   SRAM bandwidth            per input     35.65 MB/inference (batch size 1)

Neural network macs                         300836992 MACs/batch

Info: The numbers below are internal compiler estimates.
For performance numbers the compiled network should be run on an FVP Model or FPGA.

Network Tops/s                                   0.12 Tops/s

NPU cycles                                    4832315 cycles/batch
SRAM Access cycles                            1168037 cycles/batch
DRAM Access cycles                                  0 cycles/batch
On-chip Flash Access cycles                         0 cycles/batch
Off-chip Flash Access cycles                        0 cycles/batch
Total cycles                                  4942076 cycles/batch

Batch Inference time                 4.94 ms,  202.34 inferences/s (batch size 1)
```

## Observe Operator Delegation
This output indicates which operators go to processors:
- **Ethos-U85 NPU:** `occurrences_in_delegated_graphs`
- **Cortex-M85 CPU:** `occurrences_in_non_delegated_graph`

```bash { output_lines = "1-34" }
Total delegated subgraphs: 1
Number of delegated nodes: 419
Number of non-delegated nodes: 3

Delegation table:
╒════╤════════════════════════════════════════════════════╤═══════════════════════════════════╤═══════════════════════════════════════╕
│    │ op_type                                            │   occurrences_in_delegated_graphs │   occurrences_in_non_delegated_graphs │
╞════╪════════════════════════════════════════════════════╪═══════════════════════════════════╪═══════════════════════════════════════╡
│  0 │ aten_add_tensor                                    │                                10 │                                     0 │
├────┼────────────────────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│  1 │ aten_clone_default                                 │                                 1 │                                     0 │
├────┼────────────────────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│  2 │ aten_convolution_default                           │                                52 │                                     0 │
├────┼────────────────────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│  3 │ aten_hardtanh_default                              │                                35 │                                     0 │
├────┼────────────────────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│  4 │ aten_linear_default                                │                                 1 │                                     0 │
├────┼────────────────────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│  5 │ aten_mean_dim                                      │                                 1 │                                     0 │
├────┼────────────────────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│  6 │ aten_view_copy_default                             │                                 1 │                                     0 │
├────┼────────────────────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│  7 │ cortex_m_dequantize_per_tensor_default             │                                 0 │                                     1 │
├────┼────────────────────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│  8 │ cortex_m_quantize_per_tensor_default               │                                 0 │                                     1 │
├────┼────────────────────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│  9 │ getitem                                            │                                 0 │                                     1 │
├────┼────────────────────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│ 10 │ quantized_decomposed_dequantize_per_tensor_default │                               217 │                                     0 │
├────┼────────────────────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│ 11 │ quantized_decomposed_quantize_per_tensor_default   │                               101 │                                     0 │
├────┼────────────────────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│ 12 │ Total                                              │                               419 │                                     3 │
╘════╧════════════════════════════════════════════════════╧═══════════════════════════════════╧═══════════════════════════════════════╛
```

## Observe the Ethos-U Performance Monitoring Unit
This output shows Ethos-U performance, from the Performance Monitoring Unit (PMU)
```bash { output_lines = "1-7" }
I [executorch:arm_perf_monitor.cpp:180] Ethos-U PMU report:
I [executorch:arm_perf_monitor.cpp:181] ethosu_pmu_cycle_cntr : 4738932
I [executorch:arm_perf_monitor.cpp:184] ethosu_pmu_cntr0 : 1447178
I [executorch:arm_perf_monitor.cpp:184] ethosu_pmu_cntr1 : 420661
I [executorch:arm_perf_monitor.cpp:184] ethosu_pmu_cntr2 : 0
I [executorch:arm_perf_monitor.cpp:184] ethosu_pmu_cntr3 : 0
I [executorch:arm_perf_monitor.cpp:184] ethosu_pmu_cntr4 : 130
```

**Table of Ethos-U PMU Counters:**
|PMU Counter|Default Event Tracked|Description|Interpretation|
|-----------|---------------------|-----------|--------------|
|ethosu_pmu_cycle_cntr|Total NPU cycles|Counts the number of core clock cycles where the Ethos-U NPU was executing work.|High value = long runtime; use to compute throughput.|
|ethosu_pmu_cntr0|SRAM read data beats received(ETHOSU_PMU_SRAM_RD_DATA_BEAT_RECEIVED)|How many data beats (e.g., 64-bit words) the NPU read from local SRAM.|Indicates input + weight loading efficiency.|
|ethosu_pmu_cntr1|SRAM write data beats written(ETHOSU_PMU_SRAM_WR_DATA_BEAT_WRITTEN)|Number of data beats the NPU wrote back to SRAM (e.g., outputs or intermediate results).|Reflects output bandwidth usage.|
|ethosu_pmu_cntr2|External DRAM read beats(ETHOSU_PMU_EXT_RD_DATA_BEAT_RECEIVED)|Number of data beats read from off-chip memory (e.g., DRAM). Often 0 if Sram_Only is used.|If non-zero, may indicate cache misses or large model size.|
|ethosu_pmu_cntr3|External DRAM write beats(ETHOSU_PMU_EXT_WR_DATA_BEAT_WRITTEN)|Number of write data beats to external memory.|Helps detect offloading or insufficient SRAM.|
|ethosu_pmu_cntr4|Idle cycles(ETHOSU_PMU_NPU_IDLE)|Number of cycles where the NPU had no work scheduled (i.e., idle).|High idle count = possible pipeline stalls or bad scheduling.|
