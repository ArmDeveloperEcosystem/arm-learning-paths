---
title: Build, flash, and verify inference
weight: 8

layout: "learningpathall"
---

## Clean previous build artifacts

If you've built other projects (like Blinky), delete the cached build files. CMSIS Toolbox caches aggressively and won't pick up YAML configuration changes unless you clean first:

```bash
cd ~/alif/alif_vscode-template
rm -rf tmp/ out/
```

You can also clean from VS Code: press **F1** and select **CMSIS: Clean all out and tmp directories**.

## Build the project

### Option 1: Build from VS Code

1. Select the **CMSIS** icon in the left sidebar.
2. Select the gear icon and set **Active Target** to **E8-HP** and **Active Project** to **mv2_runner**.
3. Select the **Build** (hammer) icon.

### Option 2: Build from the command line

If you prefer to build from the terminal, set the required environment variables first. The exact paths depend on where the Arm Tools Environment Manager installed the tools:

```bash
export PATH="~/.vcpkg/artifacts/2139c4c6/tools.open.cmsis.pack.cmsis.toolbox/2.12.0/bin:~/.vcpkg/artifacts/2139c4c6/compilers.arm.arm.none.eabi.gcc/13.3.1/bin:~/.vcpkg/artifacts/2139c4c6/tools.kitware.cmake/3.31.5/bin:~/.vcpkg/artifacts/2139c4c6/tools.ninja.build.ninja/1.13.2:$PATH"
export CMSIS_COMPILER_ROOT="~/.vcpkg/artifacts/2139c4c6/tools.open.cmsis.pack.cmsis.toolbox/2.12.0/etc"
export GCC_TOOLCHAIN_13_3_1="~/.vcpkg/artifacts/2139c4c6/compilers.arm.arm.none.eabi.gcc/13.3.1/bin"

cbuild alif.csolution.yml --context mv2_runner.debug+E8-HP
```

{{% notice Note %}}
The `GCC_TOOLCHAIN_13_3_1` variable must include the `/bin` suffix. Without it, the build system can't find the compiler executables.
{{% /notice %}}

Check the output binary size:

```bash
ls -lh out/mv2_runner/E8-HP/debug/mv2_runner.bin
```

The binary should be approximately 4 MB.

## Flash to the board

In VS Code, press **F1**, select **Tasks: Run Task**, then select **Program with Security Toolkit (select COM port)**. Choose the DevKit's port when prompted.

The flashing process takes about 30 seconds. The Security Toolkit reads the `M55_HP_cfg.json` configuration and writes the binary to the correct MRAM address.

## View output with SEGGER RTT Viewer

1. Open **SEGGER J-Link RTT Viewer** on your development machine.
2. Set **Connection** to **USB**.
3. Filter by manufacturer: **AlifSemiconductor**.
4. For **Device**, start typing `AE822F` and select **AE822FA0E5597LS0_M55_HP** (Core: Cortex-M55).
5. Select **OK** to connect.

The expected output is:

```output
mv2_runner booted
Ethos-U85 NPU initialized (polling mode)
Model bytes: 3835552
Image bytes: 150528
ExecuTorch runtime initialized
Program loaded successfully
Method 'forward': 1 inputs, 1 outputs, 1 planned buffers
  Planned buffer[0]: 752640 bytes
Loading method 'forward'...
[I] data:0x800432b0
Method loaded, 1 inputs, 1 outputs
Converted input to float32
Input tensor set (1x3x224x224 float32)
Running inference...
[sem_take #1] count=1
[sem_take #2] count=0
Inference complete!
Output tensor: 1000 elements
Top-1 class: 283
Detected: cat! (ImageNet class 283)
```

If you see `Detected: cat!` with a class in the 280-285 range, the inference ran successfully on the Ethos-U85 NPU.

## Understanding the output

Each line tells you something about what's happening:

- **"Ethos-U85 NPU initialized (polling mode)"**: The NPU driver connected to the correct peripheral (NPU_HG). "Polling mode" means NPU completion is detected by polling the status register rather than using an interrupt.
- **"Model bytes: 3835552"**: The embedded `.pte` model is 3.7 MB.
- **"Method 'forward': 1 inputs, 1 outputs, 1 planned buffers"**: The model has a single input tensor and single output tensor. ExecuTorch pre-plans one intermediate buffer.
- **"sem_take #1 count=1"** and **"sem_take #2 count=0"**: The NPU semaphore was signaled. Two semaphore takes means the NPU processed the entire model as a single command stream.
- **"Top-1 class: 283"**: ImageNet class 283 is "Persian cat". The 1000-element output vector was scanned for the highest score.

## Troubleshooting

If you don't see the expected output, check these common issues:

- **RTT Viewer shows nothing**: The code starts running as soon as it's flashed. If you connect RTT Viewer too late, you might miss the output. Press the board's reset button after connecting RTT Viewer.
- **"ethosu_init failed"**: The NPU base address is wrong. Verify the code uses `NPU_HG_BASE` (0x49042000), not `NPU_HP_BASE`.
- **BusFault at a low address**: The GOT sections are missing from the linker script. Verify that `*(.got)` and `*(.got.plt)` are in the `.data.at_dtcm` section.
- **"Missing operator: cortex_m::quantize_per_tensor.out"**: `libcortex_m_ops_lib` isn't in the `--whole-archive` block. Check `mv2_runner.cproject.yml`.
- **"Memory allocation failed: 1505280B requested"**: The temp allocator pool is too small. The Ethos-U85 scratch buffer needs approximately 1.44 MB. Verify `TEMP_ALLOC_POOL_SIZE` is at least `1536 * 1024`.
- **MRAM overflow linker error**: Verify `APP_MRAM_HP_SIZE` is set to `0x00580000` in `app_mem_regions.h`.
- **"Vela bin ptr not aligned to 16 bytes"**: The model array in the header needs `__attribute__((aligned(16)))`.

This completes the setup and deployment of MobileNetV2 image classification on the Ethos-U85 NPU using ExecuTorch. The model went from PyTorch, through the Vela compiler, into a `.pte` flatbuffer embedded in firmware, and produced a correct classification result on real hardware.

## What you've learned

You've successfully deployed a complete machine learning inference pipeline on the Alif Ensemble E8 DevKit. You compiled a MobileNetV2 model for the Ethos-U85 NPU, configured the firmware memory layout, integrated ExecuTorch libraries, and verified that the model correctly classifies ImageNet categories using real-time inference on the Arm Cortex-M55 microcontroller.
