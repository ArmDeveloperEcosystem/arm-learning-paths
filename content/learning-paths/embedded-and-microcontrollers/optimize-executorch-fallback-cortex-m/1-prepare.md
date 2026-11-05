---
title: Understand and prepare the environment
weight: 2
description: Set up the reusable CMSIS-Executorch project and its pinned Python and Arm tool environments.

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## ExecuTorch for Cortex-M and Ethos-U

ExecuTorch is PyTorch’s runtime for deploying machine learning models on edge devices, including embedded systems. It converts trained models into programs that can run within the limited memory and compute resources of a microcontroller.

Many microcontrollers use Arm Cortex-M CPUs, and others integrate both Cortex-M CPUs, and Arm Ethos-U NPUs.

For combined Cortex-M and Ethos-U systems, ExecuTorch lets one model use both processors: supported operations are dispatched to the Ethos-U NPU, while remaining operations run on the Cortex-M CPU.

This Learning Path will demonstrate how developers can better optimize ExecuTorch deployment, either when running models directly on a Cortex-M CPU, or in a scenario where unsupported operators fallback from an Ethos-U to the Cortex-M CPU.

## Ethos-U vs CMSIS-NN vs Portable Kernels

You will use the ExecuTorch ahead-of-time export flow to divide one model across
three execution paths:

- A stride-one convolution that Ethos-U55 accepts.
- A stride-four convolution that Ethos-U55 rejects but CMSIS-NN supports.
- A `topk` operation that remains an ExecuTorch portable FP32 operation.

This is illustrated in the following diagram:

![Diagram of the simulated Corstone-300 FVP target showing the Cortex-M CPU running the ExecuTorch runtime and dispatching a stride-one convolution to Ethos-U55, while CMSIS-NN executes the stride-four convolution and a portable kernel executes topk on Cortex-M#center](images/cortex-m-execution-picture.svg "ExecuTorch execution paths")

The three execution paths have different roles:

| Technology | Role in this Learning Path | Expected performance |
| --- | --- | --- |
| [Ethos-U55](https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u55) | Runs supported graph regions on the NPU. (eg: Stride-1 convolution) | Expected to provide the best performance and energy efficiency for supported neural-network operations. |
| [CMSIS-NN](https://arm-software.github.io/CMSIS-NN/latest/index.html) | Supplies optimized Cortex-M kernels for quantized CPU operations that are unsupported by the NPU. (eg: Stride-4 convolution) | Preferred CPU fallback when a matching CMSIS-NN-backed operator is available. |
| ExecuTorch portable kernels | Supply general CPU implementations for operations without an accelerated backend implementation. (eg: `topk` operation) | Compatibility fallback rather than the preferred performance path. |

Fallback here is planned during export. It isn't recovery from an NPU failure
at runtime. The exporter determines which regions the target Ethos-U delegate
supports, then assigns known remaining patterns to the Cortex-M backend.

{{% notice Why this example uses Ethos-U55 %}}
Ethos-U55 is used because its unsupported stride-four convolution creates a
predictable fallback region. Ethos-U85 supports more operator configurations,
so it will typically have less CPU fallback than Ethos-U55. The same workflow still
applies when a model contains operations that remain outside the U85 delegate.
{{% /notice %}}

In this Learning Path, you will clone a [CMSIS-Executorch example](https://github.com/Arm-Examples/cmsis-executorch) that already contains the needed board support,
runner, memory configuration, and Fixed Virtual Platform (FVP) settings. You
will then inspect and modify it to observe Cortex-M fallback using optimized CMSIS-NN microkernels.

## Clone the example project

Begin by cloning the CMSIS-Executorch project used by this Learning Path:

```console
git clone https://github.com/Arm-Examples/CMSIS-Executorch.git
cd CMSIS-Executorch
git checkout 4002b63dcc3e27eb7444946a0dbf69b9a74d6fc9
```

The explicit checkout pins the project to a revision that has been tested and validated.

## Set up the project in VS Code

Install [Visual Studio Code](https://code.visualstudio.com/), the
[Keil Studio Pack](https://marketplace.visualstudio.com/items?itemName=Arm.keil-studio-pack),
and the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python).
Install Python 3.10–3.13 on your host; Python 3.14 is not supported by the
pinned export dependencies. On Windows, enable
[long-path support](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation).

1. Open the cloned `CMSIS-Executorch` folder in VS Code.
2. Allow Arm Environment Manager to install the tools declared in
   `vcpkg-configuration.json` and wait for installation to finish.
3. In the **CMSIS** view, select **... > Open Solution in Workspace**
   and choose `cmsis-executorch-u55.csolution.yml`.
4. Select **Terminal > Run Task > Create Python environment (pip)**. Wait for the
   task to create `.venv` and install the pinned dependencies.
5. Open a new VS Code terminal in the project folder so it receives the Arm tool
   environment. Run all subsequent commands in this terminal.

Activate the Python environment in each new terminal:

{{< tabpane code=true >}}
  {{< tab header="Linux and macOS" language="bash">}}
source .venv/bin/activate
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell">}}
.\.venv\Scripts\Activate.ps1
  {{< /tab >}}
{{< /tabpane >}}

### Additional macOS setup

Install and start [Docker Desktop](https://docs.docker.com/desktop/setup/install/mac-install/).
The FVP runs inside a Linux container because there is no native macOS FVP.
Keep the project under your home directory so the wrapper can mount it into
Docker. Confirm Docker is running and select the Ethos-U55 model in each new terminal:

```bash
docker info
export FVP_MODEL=FVP_Corstone_SSE-300_Ethos-U55
```

The final chapter uses the repository's `.vscode/fvp.sh` wrapper to run the
application on macOS. Its first run builds the container image.

## Verify the environment

The Python package and CMSIS Pack versions must match because the embedded
runtime loads the program produced by the exporter. Check the host tools, Arm
build tools, and Python packages:

{{< tabpane code=true >}}
  {{< tab header="Linux and macOS" language="bash">}}
python --version
cbuild --version
armclang --version
python -c "from importlib.metadata import version; print('ExecuTorch', version('executorch')); print('PyTorch', version('torch'))"
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell">}}
python --version
cbuild --version
armclang --version
python -c "from importlib.metadata import version; print('ExecuTorch', version('executorch')); print('PyTorch', version('torch'))"
  {{< /tab >}}
{{< /tabpane >}}

Confirm that Python is between 3.10 and 3.13,
`cbuild` reports 2.15.0, Arm Compiler for Embedded reports 6.24, and the final
two lines are:

```output
ExecuTorch 1.5.1
PyTorch 2.14.0
```

## Download the Learning Path assets

Download the fallback model, focused integration patch, and two inspection
helpers into the repository root:

{{< tabpane code=true >}}
  {{< tab header="Linux and macOS" language="bash">}}
LP_ASSETS=https://raw.githubusercontent.com/ArmDeveloperEcosystem/arm-learning-paths/main/content/learning-paths/embedded-and-microcontrollers/optimize-executorch-fallback-cortex-m/files

curl -fLO "$LP_ASSETS/mixed_backend_cnn.py"
curl -fLO "$LP_ASSETS/enable_cortex_m_fallback.patch"
curl -fLO "$LP_ASSETS/export_cortex_m_fallback.py"
curl -fLO "$LP_ASSETS/verify_pack_sources.py"
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell">}}
$lpAssets = "https://raw.githubusercontent.com/ArmDeveloperEcosystem/arm-learning-paths/main/content/learning-paths/embedded-and-microcontrollers/optimize-executorch-fallback-cortex-m/files"

curl.exe -fLO "$lpAssets/mixed_backend_cnn.py"
curl.exe -fLO "$lpAssets/enable_cortex_m_fallback.patch"
curl.exe -fLO "$lpAssets/export_cortex_m_fallback.py"
curl.exe -fLO "$lpAssets/verify_pack_sources.py"
  {{< /tab >}}
{{< /tabpane >}}

## Use a simple convolution example

The CMSIS-Executorch repository starts with a TinyCNN model that can be delegated completely to
Ethos-U. You will change this model to one that will demonstrate fallback by retaining its input and output
interface, but adjusting the operations happening inside it.

Replace the original model with the one you have downloaded:

{{< tabpane code=true >}}
  {{< tab header="Linux and macOS" language="bash">}}
cp mixed_backend_cnn.py model/model.py
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell">}}
Copy-Item .\mixed_backend_cnn.py .\model\model.py
  {{< /tab >}}
{{< /tabpane >}}

The model still accepts one `16 x 16` RGB image in NHWC order and returns ten
values. Keeping that interface means the supplied bare-metal runner needs no
changes.

The important part of `model/model.py` now looks like this:

```python
self.conv1 = nn.Conv2d(
    channels, 4, kernel_size=3, stride=1, padding=1, bias=False
)
self.conv2 = nn.Conv2d(
    4, num_classes, kernel_size=3, stride=4, padding=1, bias=False
)

values = torch.relu(self.conv1(values))
values = self.conv2(values)
values = torch.flatten(values, start_dim=2)
values, _ = torch.topk(values, k=1, dim=-1)
```

The *stride* controls how far a convolution filter moves between positions. A
stride of one visits adjacent positions. A stride of four moves four positions
at a time and produces a smaller output. For this Ethos-U55 target and tensor shape,
the first convolution can be delegated to the NPU, while the stride-four convolution
remains outside the delegate. `topk` selects the largest spatial response for
each of the ten output channels.

## What you've accomplished and what's next

You now have a pinned Corstone-300 Ethos-U55 project, its matching Python packages, its versioned Arm tools, and a model that will only partially run on an Ethos-U55. Next, you will understand how to optimize supported operators with CMSIS-NN on Cortex-M CPUs in a CPU-only example.
