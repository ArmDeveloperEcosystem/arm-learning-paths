---
title: Prepare firmware artifacts
weight: 6
layout: learningpathall
---

## Overview

This section prepares the generated model and the ExecuTorch libraries needed for the project. 

## Prerequisites
The firmware project needs two artifacts:

- `mnist_ethos_u85.pte`: the ExecuTorch model compiled for Ethos-U85
- `et_bundle.tar.gz`: ExecuTorch headers and static libraries for the bare-metal Cortex-M build

If you completed the optional export section, these files are already in `~/mnist_alif/executorch-alif/output/`

<!-- This is if we provide it as a package instead of separate files -->

If you skipped the optional export section, create the output directory and download the provided artifacts:

{{< tabpane code=true >}}
  {{< tab header="macOS / Linux" language="bash" >}}
mkdir -p ~/mnist_alif/executorch-alif/output
cd ~/mnist_alif/executorch-alif/output
curl -L -o et_bundle.tar.gz https://raw.githubusercontent.com/arm-education/alif-ethos-u85-npu-mnist/main/et_bundle.tar.gz
curl -L -o mnist_ethos_u85.pte https://raw.githubusercontent.com/arm-education/alif-ethos-u85-npu-mnist/main/mnist_ethos_u85.pte
  {{< /tab >}}

  {{< tab header="Windows (PowerShell)" language="powershell" >}}
New-Item -ItemType Directory -Force -Path "$HOME\mnist_alif\executorch-alif\output"
cd "$HOME\mnist_alif\executorch-alif\output"
curl.exe -L -o et_bundle.tar.gz https://raw.githubusercontent.com/arm-education/alif-ethos-u85-npu-mnist/main/et_bundle.tar.gz
curl.exe -L -o mnist_ethos_u85.pte https://raw.githubusercontent.com/arm-education/alif-ethos-u85-npu-mnist/main/mnist_ethos_u85.pte
  {{< /tab >}}
{{< /tabpane >}}

Verify all artifacts are present:

{{< tabpane code=true >}}
  {{< tab header="macOS / Linux" language="bash" >}}
ls -lh ~/mnist_alif/executorch-alif/output/mnist_ethos_u85.pte
ls -lh ~/mnist_alif/executorch-alif/output/et_bundle.tar.gz
  {{< /tab >}}

  {{< tab header="Windows (PowerShell)" language="powershell" >}}
Get-Item ~\mnist_alif\executorch-alif\output\mnist_ethos_u85.pte
Get-Item ~\mnist_alif\executorch-alif\output\et_bundle.tar.gz
  {{< /tab >}}
{{< /tabpane >}}

## Convert the model to a C header

The firmware embeds the `.pte` model as a byte array in flash memory. Use `xxd` to generate a C header:

{{< tabpane code=true >}}
  {{< tab header="macOS / Linux" language="bash" >}}
cd ~/mnist_alif/executorch-alif/output
xxd -i mnist_ethos_u85.pte > mnist_model_data.h
  {{< /tab >}}

{{< tab header="Windows (PowerShell)" language="powershell" >}}
cd ~\mnist_alif\executorch-alif\output
& "$env:ProgramFiles\Git\usr\bin\xxd.exe" -i mnist_ethos_u85.pte | Set-Content -Encoding ascii mnist_model_data.h
{{< /tab >}}
{{< /tabpane >}}

Open the generated header (`mnist_model_data.h`) and change the first array declaration to this:

```c
#include <stdint.h>
const uint8_t __attribute__((aligned(16))) mnist_ethos_u85_pte[] = {
```

{{% notice Important %}}
The `aligned(16)` attribute is required because the Ethos-U85 needs the Vela command stream data aligned to 16 bytes. Without it, the NPU driver will report an alignment error at runtime.
{{% /notice %}}

## Extract the Executorch bundle

Extract the ExecuTorch headers (from `et_bundle.tar.gz`) into the VS Code template project:

{{< tabpane code=true >}}
  {{< tab header="macOS / Linux" language="bash" >}}
cd ~/mnist_alif/alif_vscode-template
mkdir -p third_party/executorch
tar -C third_party/executorch -xzf ~/mnist_alif/executorch-alif/output/et_bundle.tar.gz
  {{< /tab >}}

  {{< tab header="Windows (PowerShell)" language="powershell" >}}
cd ~\mnist_alif\alif_vscode-template
New-Item -ItemType Directory -Force -Path .\third_party\executorch
tar -C .\third_party\executorch -xzf "$HOME\mnist_alif\executorch-alif\output\et_bundle.tar.gz"
  {{< /tab >}}
{{< /tabpane >}}

Verify the headers are in place:
```bash
ls third_party/executorch/et_bundle/include/executorch/
```
You should see `runtime/` and other directories.

You are now ready to integrate the model into the VS Code project.

## Summary
In this section, you prepared the following firmware inputs:

- `mnist_model_data.h` contains the embedded ExecuTorch model
- `third_party/executorch/et_bundle/include` contains ExecuTorch headers
- `third_party/executorch/et_bundle/lib` contains the static libraries used by the firmware build

The next section creates the MNIST firmware project by duplicating the Blinky example and replacing relevant files to fit our application.