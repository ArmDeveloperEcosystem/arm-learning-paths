---
title: Flash and run on hardware
weight: 9
layout: learningpathall
---

## Overview

This section covers programming the Alif Ensemble E8 DevKit using VS Code CMSIS Extensions, viewing debug output via SEGGER RTT, and verifying successful deployment.

## Build the project using VS Code CMSIS Extension

Firstly, clear any cached build files present from previous runs (eg: Blinky project). CMSIS Toolbox caches aggressively and won’t pick up YAML configuration changes unless you clean first:

{{< tabpane code=true >}}
  {{< tab header="macOS / Linux" language="bash" >}}
cd ~/mnist_alif/alif_vscode-template
rm -rf tmp/ out/
  {{< /tab >}}

  {{< tab header="Windows (PowerShell)" language="powershell" >}}
cd "$HOME\mnist_alif\alif_vscode-template"
Remove-Item -Recurse -Force .\tmp, .\out -ErrorAction SilentlyContinue
  {{< /tab >}}
{{< /tabpane >}}

Next, follow these steps to build:
- Select the **CMSIS** icon in the left sidebar.
- Select the gear icon.
- Set **Active Target** to **E8-HP**.
- Set **Active Project** to **mnist_executorch**.
- Select the **Build** hammer icon.

A successful build prints a memory report similar to:

```output
Memory region         Used Size  Region Size  %age Used
            ITCM:      149232 B       256 KB     56.93%
            DTCM:        256 KB       256 KB    100.00%
           SRAM0:       2576 KB         4 MB     62.89%
           SRAM1:          2 MB         4 MB     50.00%
            MRAM:      291008 B         2 MB     13.88%
```

## Flash the pplication

Press F1, select **Tasks: Run Task**. then select **Program with Security Toolkit (select COM port)**. Choose the DevKit's port when prompted.
Flashing takes about 30 seconds.

## Start the J-Link RTT server

Open a new terminal and start J-Link Commander.

{{< tabpane code=true >}}
  {{< tab header="macOS / Linux" language="bash" >}}
JLinkExe -device AE822FA0E5597LS0_M55_HE -if SWD -speed 4000
  {{< /tab >}}

  {{< tab header="Windows (PowerShell)" language="powershell" >}}
& "C:\Program Files\SEGGER\JLink_V954\JLink.exe" -device AE822FA0E5597LS0_M55_HP -if SWD -speed 4000
  {{< /tab >}}
{{< /tabpane >}}

At the `J-Link>` prompt, run:

```text
connect
r
g
```

Leave this terminal open. It acts as the RTT server.

## Start the RTT client

Open another terminal and start the RTT client.

{{< tabpane code=true >}}
  {{< tab header="macOS / Linux" language="bash" >}}
JLinkRTTClient
  {{< /tab >}}

  {{< tab header="Windows (PowerShell)" language="powershell" >}}
& "C:\Program Files\SEGGER\JLink_V954\JLinkRTTClient.exe"
  {{< /tab >}}
{{< /tabpane >}}

You should see output similar to:

```output
ExecuTorch MNIST NPU Demo
Alif Ensemble E8 - Cortex-M55 HP

Initializing SRAM0 power...
SRAM0 enabled successfully

Loading model ...
Running inference...
Inference completed!
Predicted digit: ...
```

The predicted digit depends on the image you converted in the previous section.