---
title: Flash and run the project on the Alif Ensemble E8 DevKit
description: Build and flash the Alif E8 CMSIS firmware, then run MNIST inference on the Ethos-U85 NPU and view results with SEGGER RTT.
weight: 9
layout: learningpathall
---

## Build the project using the VS Code CMSIS extension

First, clear any cached build files present from previous runs:

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

CMSIS Toolbox caches aggressively and won’t pick up YAML configuration changes unless you clean first.

Next, to build the project in VS Code:

1. Select the **CMSIS** icon in the left sidebar.
2. Select the gear icon.
3. Set **Active Target** to **E8-HP**.
4. Set **Active Project** to **mnist_executorch**.
5. Select the **Build** hammer icon.

A successful build prints a memory report similar to:

```output
Memory region         Used Size  Region Size  %age Used
            ITCM:      149232 B       256 KB     56.93%
            DTCM:        256 KB       256 KB    100.00%
           SRAM0:       2576 KB         4 MB     62.89%
           SRAM1:          2 MB         4 MB     50.00%
            MRAM:      291008 B         2 MB     13.88%
```

## Flash the application

To flash the application, follow these steps:

1. Open the Command Palette (`Ctrl+Shift+P` on Windows and Linux or `Cmd+Shift+P` on macOS).
2. Select **Tasks: Run Task**.
3. Select **Program with Security Toolkit (select COM port)**.
4. Choose the DevKit's port when prompted.

Flashing takes about 30 seconds.

## Start the J-Link RTT server

Open a new terminal and start J-Link Commander:

{{< tabpane code=true >}}
  {{< tab header="macOS and Linux" language="bash" >}}
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

Open a second terminal and start the RTT client:

{{< tabpane code=true >}}
  {{< tab header="macOS and Linux" language="bash" >}}
JLinkRTTClient
  {{< /tab >}}

  {{< tab header="Windows (PowerShell)" language="powershell" >}}
& "C:\Program Files\SEGGER\JLink_V954\JLinkRTTClient.exe"
  {{< /tab >}}
{{< /tabpane >}}

The output is similar to:

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

## What you've accomplished

You have built and flashed a CMSIS-based firmware application that embeds an ExecuTorch `.pte` model, runs MNIST inference on the Ethos-U85 NPU, and reports the result through SEGGER RTT.

You can extend this project by trying different MNIST images, retraining the model, or replacing MNIST with a different model, such as one trained to classify handwritten letters instead of digits.
