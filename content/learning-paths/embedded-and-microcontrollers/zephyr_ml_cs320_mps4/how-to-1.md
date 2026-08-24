---
title: Set up the Zephyr and ExecuTorch development environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Platform and Software Setup

The Arm Corstone SSE-320 FPGA image for MPS4 (FI101) is an FPGA implementation that runs on the MPS4 board. The image includes an Arm Cortex-M85 processor, an Arm Ethos-U85 NPU, and a range of peripheral components. It provides a practical hardware platform for developing and evaluating machine learning applications.

Download the latest Corstone-320 FPGA image and review the platform documentation:

- [Arm Corstone SSE-320 with Cortex-M85 and Ethos-U85: Example FPGA (FI101)](https://developer.arm.com/downloads/view/FI101)
- [SSE-320 FPGA Image for MPS4 Application Note](https://developer.arm.com/documentation/109762/0100/?lang=en)
- [Arm MPS4 FPGA Prototyping Board Technical Reference Manual](https://developer.arm.com/documentation/102577/latest/)
- [Arm Corstone SSE-320 Example Subsystem Software Programmers Guide](https://developer.arm.com/documentation/109759/latest/)


This section describes the software and development environment that you need to deploy a Zephyr-based machine learning application on this platform.

### Zephyr workspace and board target set up

Follow the [Port Zephyr RTOS and run applications on the Arm Corstone-320 MPS4 platform ](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_cs320_mps4/how-to-1/) to set up the Zephyr workspace for the Arm Corstone-320 MPS4 platform. The Zephyr version used is V4.3.0.

### ExecuTorch integration in the Zephyr tree

ExecuTorch is integrated into the Zephyr workspace as an external module located in `modules/lib/executorch`. The module provides the ExecuTorch runtime, the Arm backend, the Ethos-U delegate, build scripts, and sample applications. You can build the sample applications using the Zephyr build system.

To add ExecuTorch as a Zephyr module, create `executorch.yaml` in `zephyr/submanifests` with the following content:

```yaml
manifest:
  projects:
    - name: executorch
      url: https://github.com/pytorch/executorch
      revision: main
      path: modules/lib/executorch
```

Run the following commands to fetch the ExecuTorch repository and its submodules. The commands place the ExecuTorch source tree in `modules/lib/executorch`.

```bash
west update
cd modules/lib/executorch
git submodule sync
git submodule update --init --recursive
./install_executorch.sh
```


### Set up the Arm/Ethos-U toolchain
ExecuTorch includes a setup script that downloads the Arm GNU Toolchain, the TOSA Serialization Library, the Ethos-U Vela graph compiler, and other utilities.
 
Run the following commands to download, install, and configure these tools on your system.

```bash
./examples/arm/setup.sh --i-agree-to-the-contained-eula
source examples/arm/arm-scratch/setup_path.sh
```

## Pre-process the PyTorch Model for NPU delegation 
The ExecuTorch [Ahead-of-Time (AOT)](https://github.com/pytorch/executorch/blob/main/examples/arm/aot_arm_compiler.py) pipeline takes a PyTorch Model (a torch.nn.Module) and produces a .pte binary file. The ExecuTorch runtime uses this file for inference.

The following example shows a simple PyTorch model, `add.py`, that performs a single addition.

```python
import torch

b = 2

class myModelAdd(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return x + x + b


ModelUnderTest = myModelAdd()
ModelInputs = (torch.ones(5),)
```
Run the following commands from the `modules/lib/executorch` directory to quantize the model and export it through the Ahead-of-Time (AOT) flow using the Ethos-U backend.

```bash
source ~/zephyrproject/.venv/bin/activate
python3 -m executorch.backends.arm.scripts.aot_arm_compiler \
  --model_name=examples/arm/example_modules/add.py \
  -t ethos-u85-1024 \
  --delegate \
  --quantize \
  --memory_mode=Sram_Only \
  -o add_u85_1024_sram_only.pte
```
**Key parameters:**

| Parameter | Value | Notes |
|-----------|-------|-------|
| `--model_name` | path to `.py` model file | Use absolute or workspace-relative path |
| `-t` / `--target` | `ethos-u85-1024` | Must match `CONFIG_ETHOS_U85_1024=y` in Kconfig |
| `--delegate` | (flag) | Enables Ethos-U NPU delegation via ArmBackend |
| `--quantize` | (flag) | Applies INT8 symmetric quantisation |
| `--memory_mode` | `Shared_Sram` or `Sram_Only` | Vela memory layout; must match the runtime build |
| `--system_config` | `Ethos_U85_SYS_DRAM_Mid` | Optional; selects Vela system config from `vela.ini` |
| `-o` | output filename | Saved in the project root by default |

The `add_u85_1024_sram_only.pte` file contains the model graph, quantized weights, and a Vela-compiled command stream. The Ethos-U85 executes the command stream directly.

Verify the model file was created:

```bash
ls -la add_u85_1024_sram_only.pte
```



You now have a quantized `.pte` model file ready for deployment. In the next section, you will port the `hello-executorch` sample application to the Corstone-320 MPS4 platform and run inference on the Ethos-U85 NPU.
