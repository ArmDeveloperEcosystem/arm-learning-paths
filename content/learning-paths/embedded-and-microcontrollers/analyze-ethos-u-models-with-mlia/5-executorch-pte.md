---
title: Analyze ExecuTorch artifacts with Corstone

description: Run MLIA Corstone checks on packaged ExecuTorch PTE artifacts and compare whole-model NPU performance counters for Ethos-U55 and Ethos-U85.

weight: 6

### FIXED, DO NOT MODIFY
layout: "learningpathall"
---

## Understand the ExecuTorch path

You previously used LiteRT and Tensor Operator Set Architecture (TOSA) artifacts with Vela. You can also use Arm ML Inference Advisor (MLIA) if you're working with an ExecuTorch flow.

A `.pte` file is a portable ExecuTorch executable: the packaged artifact that ExecuTorch can load and run.

You'll compare two packaged `.pte` artifacts with Corstone backends.

## Compare prebuilt .pte artifacts

The model artifacts repository includes prebuilt Ethos-U `.pte` files:

```output
pte/toy_conditional_select_int8_ethos_u55_256.pte
pte/toy_conditional_select_int8_ethos_u85_256.pte
```

These are synthetic learning artifacts rather than benchmark models. The artifacts use a small convolution plus a conditional selection pattern to make target-dependent delegation easier to see. A model can be packaged for different Ethos-U targets and show different delegation and runtime-counter behavior.

For supported `.pte` workloads, MLIA performance analysis uses a Corstone backend. In this context, Corstone refers to an Arm reference subsystem platform, and the backend uses a Fixed Virtual Platform (FVP). 

An FVP is a software model of a hardware platform. You can use an FVP to run a packaged artifact in a target-like environment and collect performance counters without needing a physical board on your desk.

For `.pte` artifacts, MLIA currently supports performance analysis only. The artifact has already been packaged for an ExecuTorch deployment path, so Corstone is used to run the packaged program on an FVP and collect NPU performance counters for the whole model run. 

Corstone doesn't provide per-layer estimates or operator breakdowns. Perform a Vela-backed analysis similar to earlier when you need layer-level performance estimates or compatibility checks.

Run the Ethos-U55 artifact with the Corstone-300 backend:

```bash
mlia check pte/toy_conditional_select_int8_ethos_u55_256.pte \
  --target-profile ethos-u55-256 \
  --performance \
  --backend corstone-300
```

Running the check installs any required Corstone backends that weren't previously installed.

{{% notice Note %}}
Corstone backend installation requires accepting a license. You will be prompted in the terminal to agree.
{{% /notice %}}

Run the Ethos-U85 artifact with the Corstone-320 backend:

```bash
mlia check pte/toy_conditional_select_int8_ethos_u85_256.pte \
  --target-profile ethos-u85-256 \
  --performance \
  --backend corstone-320
```

The reports should show Corstone running each `.pte` artifact and collecting NPU performance counters for the whole model run. Read the Corstone report as runtime counter evidence:

| Field | What it tells you |
| --- | --- |
| `NPU active cycles` | Cycles where the NPU was doing work. |
| `NPU idle cycles` | Cycles where the NPU was present but not active. A very small value means this run kept the NPU busy once work was issued. |
| `NPU total cycles` | Active plus idle cycles for the NPU portion of the run. |
| `NPU AXI0 RD/WR data beat` | Memory traffic on the AXI0 port, configured as SRAM for this target profile. |
| `NPU AXI1 RD/WR data beat` | Memory traffic on the AXI1 port, configured as DRAM for this target profile. |

Use the reports to compare the NPU counters for each packaged artifact:

| Artifact | Target profile | Backend | NPU total cycles |
| --- | --- | --- | --- |
| `toy_conditional_select_int8_ethos_u55_256.pte` | `ethos-u55-256` | `corstone-300` | `273,088` |
| `toy_conditional_select_int8_ethos_u85_256.pte` | `ethos-u85-256` | `corstone-320` | `19,056` |

The comparison uses `ethos-u55-256` and `ethos-u85-256`, so both target profiles use 256 MACs per cycle. However, Ethos-U85 is a newer and higher performance NPU than Ethos-U55. The target information in the reports also shows other platform differences, such as accelerator clock and memory configuration.

The Ethos-U55 report shows `271,725` NPU active cycles and `1,363` NPU idle cycles. The Ethos-U85 report shows `18,183` NPU active cycles and `873` NPU idle cycles, for `19,056` total NPU cycles. This difference reflects the combined effect of improvements in Ethos-U85 over Ethos-U55.

Use the Corstone counters to compare packaged artifacts under the same target profile and backend. If part of the graph runs outside the NPU delegate, the CPU-side cost isn't fully represented by the NPU cycle table.

## Use Model Explorer for graph structure

You've used MLIA with LiteRT, TOSA, and ExecuTorch `.pte` artifacts. MLIA answers target-aware questions about compatibility, estimated performance, runtime counters, and advice. To see how these artifacts can be visualized as graphs in Model Explorer, continue with the [Explore model artifacts with Model Explorer](/learning-paths/cross-platform/explore-model-artifacts-with-model-explorer/) Learning Path, which uses many of the same files from the model artifacts repository.

Model Explorer can open some formats directly, while other formats use adapters. Use Model Explorer alongside MLIA when you want to connect target advice with the graph structure that produced it.

In the earlier example, not only is Ethos-U85 expected to perform better due to its platform differences, there's also a difference in the way the model delegates to Ethos-U85 vs Ethos-U55.

The model pattern is:

```output
convolution / activation
conditional select
convolution / activation / convolution
```

On Ethos-U55, the conditional select part isn't kept inside the Ethos-U delegate path. The partitioning therefore is as follows:

```output
EthosUBackend region
aten::gt / aten::where outside delegate
EthosUBackend region
```

On Ethos-U85, the model pattern is handled more cleanly by this backend flow, so the packaged artifact has one `EthosUBackend` region. This will provide further performance benefit, as there's reduced fragmentation between CPU and NPU. To visualize the delegation of models to different backends, use the Model Explorer tool with Arm adapters.

{{% notice Note %}}
An ExecuTorch `.pte` file can contain work outside an accelerator delegate, but there's no guarantee that every non-delegated operator can run on the CPU runtime you deploy. CPU execution depends on the kernel libraries linked into that runtime and the operators, dtypes, layouts, and shapes that they support. 

Cortex-M bare-metal runtimes are usually built with a smaller, more selective kernel set than Cortex-A runtimes, because Cortex-M systems have tighter memory and storage constraints. In both cases, CPU fallback support depends on which kernels are included in the runtime build.
{{% /notice %}}

## What you've accomplished 

You've learned how `.tflite`, `.tosa`, and `.pte` fit into MLIA workflows. You've also seen why PTE is useful for ExecuTorch artifact analysis, where TOSA can fit as an intermediate handoff, and why Model Explorer remains useful for graph structure.

You can extend this CLI workflow to evaluate other models for whether they're suitable for a target. If you want to call MLIA from automation or another tool, see [(Optional) Use the MLIA Python API](/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/6-python-api/).
