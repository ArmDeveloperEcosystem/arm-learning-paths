---
title: Build and run the mixed application
weight: 7
description: Compile the selected Pack sources, verify their provenance, and run the application on the Corstone-300 Ethos-U55 FVP.

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build the application

Make sure the `vcpkg` tools are active in your current terminal, then build the
U55 target from the repository root:

```console
cbuild cmsis-executorch-u55.csolution.yml --active SSE-300-U55
```

CMSIS-Toolbox combines the App, Board, and AI layers, resolves their selected
components, and invokes Arm Compiler for Embedded. The final output includes:

```output
Build summary: 1 succeeded, 0 failed
```

The generated images are written under:

```text
out/cmsis-executorch/SSE-300-U55/Debug/
```

The `.axf` file contains the linked executable and debug information. The
`.hex` file contains the image loaded into the FVP.

## Verify the compiled source paths

A successful build proves that an image was produced, but it doesn't by itself
show which implementation supplied each operation. Run the verification helper
against the compilation database:

{{< tabpane code=true >}}
  {{< tab header="Linux" language="bash">}}
python verify_pack_sources.py \
  out/cmsis-executorch/SSE-300-U55/Debug/compile_commands.json
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell">}}
python .\verify_pack_sources.py `
  .\out\cmsis-executorch\SSE-300-U55\Debug\compile_commands.json
  {{< /tab >}}
{{< /tabpane >}}

The expected output is: 

```output
PASS: ExecuTorch runtime was compiled from its declared CMSIS Pack
PASS: ExecuTorch Cortex-M convolution wrapper was compiled from its declared CMSIS Pack
PASS: CMSIS-NN convolution kernel was compiled from its declared CMSIS Pack
PASS: Ethos-U backend was compiled from its declared CMSIS Pack
PASS: ExecuTorch portable topk kernel was compiled from its declared CMSIS Pack
```

These checks distinguish the two layers of the optimized fallback. The
ExecuTorch Pack provides the `quantized_conv2d` wrapper, while the CMSIS-NN
Pack provides the convolution implementation that wrapper calls.

Together with `cmsis-executorch-u55.cbuild-pack.yml`, the compilation database
shows both the resolved Pack versions and the source files actually compiled.

## Run the image on the FVP

Start the Corstone-300 model and load the generated HEX image:

```console
FVP_Corstone_SSE-300_Ethos-U55 -f board/Corstone-300/fvp_config_u55.txt -a out/cmsis-executorch/SSE-300-U55/Debug/cmsis-executorch.hex --simlimit 60
```

The relevant output is:

```output
Ethos-U version info:
        Arch:       v1.1.0
        MACs/cc:    128
        Cmd stream: v0
ExecuTorch Ethos-U55-128 application: 7608 byte model
Output: 10 element(s): 0.0532 -0.0239 0.0541 0.1064 0.0706 0.0395 0.0881 0.1340 0.0807 0.0064
Test_result: PASS
```

{{% notice Note %}}
On Windows, the FVP can print warnings that `python3.dll` is unavailable and
that the VIO or VSI bridges are disabled. This headless example doesn't use
those bridges. If the run reaches `Test_result: PASS`, inference completed
successfully.
{{% /notice %}}



The FVP result proves functional execution, not physical-device latency or
power. Measure the complete graph on your target hardware before drawing
performance conclusions because delegation boundaries and tensor conversions
also have a cost.

## What you've accomplished

You have built and run one ExecuTorch program across three execution paths:

- The supported convolution runs in an Ethos-U55 delegate.
- The unsupported stride-four convolution runs on Cortex-M55 through the
  ExecuTorch wrapper and optimized CMSIS-NN kernel.
- `topk` runs through the portable ExecuTorch CPU kernel.

You also verified the implementation rather than inferring it from a successful
run. The exported graph shows ownership, the compilation database shows the
compiled Pack sources, and the FVP confirms that the combined firmware runs.

This build uses U55 to make one unsupported convolution predictable. The same
Pack workflow applies to another Ethos-U target when its delegated graph leaves
operations for Cortex-M execution.

To adapt the project, replace `model/model.py`, provide representative
calibration inputs, preserve or update the runner's tensor interface, and
regenerate the AI layer before rebuilding.
