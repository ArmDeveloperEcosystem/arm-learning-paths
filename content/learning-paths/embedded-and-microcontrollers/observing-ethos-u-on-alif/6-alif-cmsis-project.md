---
title: Create Alif E8 CMSIS project
weight: 7
layout: learningpathall
---

## Overview

In this section, you duplicate the existing Blinky example to create a new CMSIS project called mnist_executorch, configured to include ExecuTorch libraries, the compiled model, and SEGGER RTT for debug output.

## Duplicate the Blinky project

Start by copying the working Blinky project as a template, and renaming the project file inside the new directory:

{{< tabpane code=true >}}
  {{< tab header="macOS / Linux" language="bash" >}}
cd ~/mnist_alif/alif_vscode-template
cp -R blinky/ mnist_executorch
mv mnist_executorch/blinky.cproject.yml mnist_executorch/mnist_executorch.cproject.yml
  {{< /tab >}}

  {{< tab header="Windows (PowerShell)" language="powershell" >}}
cd ~\mnist_alif\alif_vscode-template
Copy-Item .\blinky .\mnist_executorch -Recurse
Rename-Item .\mnist_executorch\blinky.cproject.yml mnist_executorch.cproject.yml
  {{< /tab >}}
{{< /tabpane >}}

Next, replace all internal references from `blinky` to `mnist_executorch`:
{{< tabpane code=true >}}
  {{< tab header="macOS / Linux" language="bash" >}}
perl -pi -e 's/\bblinky\b/mnist_executorch/g' $(grep -RIl "blinky" mnist_executorch)
  {{< /tab >}}

  {{< tab header="Windows (PowerShell)" language="powershell" >}}
Get-ChildItem .\mnist_executorch -Recurse -File | Where-Object { Select-String -Path $_.FullName -Pattern '\bblinky\b' -Quiet } | ForEach-Object { $text = Get-Content $_.FullName -Raw; $text = $text -replace '\bblinky\b', 'mnist_executorch'; Set-Content $_.FullName $text -NoNewline }
  {{< /tab >}}
{{< /tabpane >}}

## Rename main.c to main.cpp

ExecuTorch is a C++ library, so the source file needs a `.cpp` extension:
{{< tabpane code=true >}}
  {{< tab header="macOS / Linux" language="bash" >}}
mv mnist_executorch/main.c mnist_executorch/main.cpp
  {{< /tab >}}
  {{< tab header="Windows (PowerShell)" language="powershell" >}}
Rename-Item .\mnist_executorch\main.c main.cpp
  {{< /tab >}}
{{< /tabpane >}}

## Copy model assets

Create an assets directory and copy the model header into the project:
{{< tabpane code=true >}}
  {{< tab header="macOS / Linux" language="bash" >}}
mkdir -p mnist_executorch/assets
cp ~/mnist_alif/executorch-alif/output/mnist_model_data.h mnist_executorch/assets/
  {{< /tab >}}

  {{< tab header="Windows (PowerShell)" language="powershell" >}}
New-Item -ItemType Directory -Force -Path .\mnist_executorch\assets
Copy-Item ~\mnist_alif\executorch-alif\output\mnist_model_data.h .\mnist_executorch\assets\
  {{< /tab >}}
{{< /tabpane >}}

## Create the SEGGER RTT configuration

RTT (Real-Time Transfer) works through the J-Link debug probe, reading and writing a memory buffer through the debug interface. It's faster than UART and doesn't require extra wiring. Within `mnist_executorch/`, create the configuration file `SEGGER_RTT_Conf.h`:

```c
#ifndef SEGGER_RTT_CONF_H
#define SEGGER_RTT_CONF_H
#define SEGGER_RTT_MAX_NUM_UP_BUFFERS     (1)
#define SEGGER_RTT_MAX_NUM_DOWN_BUFFERS   (1)
#define SEGGER_RTT_BUFFER_SIZE_UP         (4096)
#define SEGGER_RTT_BUFFER_SIZE_DOWN       (16)
#define SEGGER_RTT_MODE_DEFAULT           SEGGER_RTT_MODE_NO_BLOCK_SKIP
#define SEGGER_RTT_PRINTF_BUFFER_SIZE     (256)
#endif
```

## Update the solution file

The `alif.csolution.yml` file describes the whole CMSIS workspace: available projects, targets, devices, packs, and flash settings.

Open it and make the following changes.

Update the `created-for` field to match your CMSIS Toolbox version:

```yaml
  created-for: CMSIS-Toolbox@2.12.0
```

Add the required packs under the `packs:` section:

```yaml
  packs:
    - pack: AlifSemiconductor::Ensemble@2.0.4
    - pack: ARM::CMSIS@6.0.0
    - pack: ARM::CMSIS-Compiler@2.1.0
    - pack: Keil::MDK-Middleware@8.2.0
    - pack: ARM::ethos-u-core-driver
```

Add a `target-set` block to the `E8-HP` target type so the Security Toolkit knows which binary to flash. Find the `type: E8-HP` section and add:

```yaml
    - type: E8-HP
      device: Alif Semiconductor::AE822FA0E5597LS0:M55_HP
      board: Alif Semiconductor::DevKit-E8
      define:
        - "CORE_M55_HP"
      target-set:
        - set:
          images:
            - project-context: mnist_executorch.debug
```

For all other target types (E7-HE, E7-HP, E1C-HE, E8-HE), add a `target-set` pointing to `blinky.debug` instead.

Add `mnist_executorch` to the projects list. It's at the bottom of the file:

```yaml
  projects:
    - project: blinky/blinky.cproject.yml
    - project: hello/hello.cproject.yml
    - project: hello_rtt/hello_rtt.cproject.yml
    - project: mnist_executorch/mnist_executorch.cproject.yml
```

## Configure the project file

The `mnist_executorch/mnist_executorch.cproject.yml` file describes our MNIST application: its source files, components, include paths, and build options.
Locate this file and replace the contents with the following configuration:

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/Open-CMSIS-Pack/devtools/tools/projmgr/2.6.0/tools/projmgr/schemas/cproject.schema.json
project:
  groups:
    - group: App
      files:
        - file: main.cpp
        - file: executorch_runner.cpp
        - file: executorch_runner.h
        - file: SEGGER_RTT_Conf.h
        - file: assets/mnist_model_data.h

    - group: SEGGER_RTT
      files:
        - file: ../libs/SEGGER_RTT_V796h/RTT/SEGGER_RTT.c
        - file: ../libs/SEGGER_RTT_V796h/RTT/SEGGER_RTT_printf.c
        - file: ../libs/SEGGER_RTT_V796h/Syscalls/SEGGER_RTT_Syscalls_GCC.c

  output:
    base-name: $Project$
    type:
      - elf
      - bin

  layers:
    - layer: ../device/ensemble/alif-ensemble.clayer.yml

  packs:
    - pack: AlifSemiconductor::Ensemble
    - pack: ARM::ethos-u-core-driver

  components:
    - component: ARM::Machine Learning:NPU Support:Ethos-U Driver&Generic U85

  define:
    - C10_USING_CUSTOM_GENERATED_MACROS
    - ETHOSU
    - ETHOSU85

  add-path:
    - .
    - assets
    - ../libs/SEGGER_RTT_V796h/RTT
    - ../third_party/executorch/et_bundle/include
    - ../third_party/executorch/et_bundle/include/executorch/runtime/core/portable_type/c10

  misc:
    - for-compiler: GCC
      C-CPP:
        - -std=c++17
        - -fno-rtti
        - -fno-exceptions
        - -DETHOSU_ARCH=u85
        - -DETHOSU_MACS=256
        - -DETHOSU_MODEL=1
      Link:
        - -L/absolute/path/to/third_party/executorch/et_bundle/lib
        - -Wl,--whole-archive
        - -lexecutorch
        - -lexecutorch_core
        - -lexecutorch_delegate_ethos_u
        - -lcortex_m_ops_lib
        - -Wl,--no-whole-archive
        - -Wl,--start-group
        - -lextension_runner_util
        - -lcortex_m_kernels
        - -lportable_ops_lib
        - -lportable_kernels
        - -lquantized_ops_lib
        - -lquantized_kernels
        - -lkernels_util_all_deps
        - -lcmsis-nn
        - -lflatccrt
        - -Wl,--end-group
```

{{% notice Warning %}}
Update the `-L` path to match the absolute path to your `third_party/executorch/et_bundle/lib` directory. For example: `-L/Users/username/mnist_alif/alif_vscode-template/third_party/executorch/et_bundle/lib`.
{{% /notice %}}

There are several important details in this configuration:

- **`--whole-archive`** is required for `libexecutorch`, `libexecutorch_core`, `libexecutorch_delegate_ethos_u`, and `libcortex_m_ops_lib`. These libraries contain static registration constructors (for operator registration and PAL symbols) that the linker would otherwise discard as unused.
- **Don't add** `portable_ops_lib` or `quantized_ops_lib` to `--whole-archive`. They are large and will overflow the microcontroller's ITCM/MRAM.
- **`--start-group`/`--end-group`** resolves circular dependencies among the remaining libraries.
- **`C10_USING_CUSTOM_GENERATED_MACROS`** tells ExecuTorch to skip looking for a `cmake_macros.h` header that doesn't exist in the bare-metal build.
- The **c10 include path** provides the tensor type definitions that ExecuTorch's headers depend on.

## Add the source files

The application code is split across three source files:

- `main.cpp` is the firmware entry point. It initializes the board, loads the embedded model from `mnist_model_data.h`, passes the MNIST input image to the runner, and prints the predicted digit and output scores.
- `executorch_runner.h` declares the small C-style interface used by `main.cpp` to initialize ExecuTorch and run inference.
- `executorch_runner.cpp` implements the ExecuTorch integration. It initializes the Ethos-U NPU driver, loads the `.pte` program, prepares input and output tensors, allocates runtime buffers, and executes the model.

Run these commands to download the source files and place them in `mnist_executorch/`:

```bash
cd ~/mnist_alif/alif_vscode-template/mnist_executorch
curl -o main.cpp https://raw.githubusercontent.com/arm-education/alif-ethos-u85-npu-mnist/refs/heads/main/mnist_executorch/main.cpp
curl -o executorch_runner.cpp  https://raw.githubusercontent.com/arm-education/alif-ethos-u85-npu-mnist/refs/heads/main/mnist_executorch/executorch_runner.cpp
curl -o executorch_runner.h https://raw.githubusercontent.com/arm-education/alif-ethos-u85-npu-mnist/refs/heads/main/mnist_executorch/executorch_runner.h
```
After downloading the files, open them in VS Code and briefly review how `main.cpp` calls into `executorch_runner.cpp` to initialize ExecuTorch, pass in the MNIST input tensor, and read back the model output.

## Update the linker script

Open:

```text
device/ensemble/RTE/Device/AE822FA0E5597LS0_M55_HP/linker_gnu_mram.ld.src
```

On Cortex-M systems, the **DTCM (Data Tightly Coupled Memory)** is a small, fast RAM region connected closely to the CPU. By default, the linker script sends most `.bss` data to DTCM. 

ExecuTorch uses large memory pools, so this data must be routed to SRAM0 and SRAM1 instead. Without this change, the linker reports that `.bss` does not fit in DTCM.

Make the following changes.

### Add SRAM1 to the zero-initialization table

Find this block in `.zero.table`:

```ld
#if __HAS_BULK_SRAM
    LONG (ADDR(.bss.at_sram0))
    LONG (SIZEOF(.bss.at_sram0)/4)
#endif
```

Replace it with:

```ld
#if __HAS_BULK_SRAM
    LONG (ADDR(.bss.at_sram0))
    LONG (SIZEOF(.bss.at_sram0)/4)
    LONG (ADDR(.bss.at_sram1))
    LONG (SIZEOF(.bss.at_sram1)/4)
#endif
```

This tells the startup code to clear both SRAM0 and SRAM1 `.bss` sections before `main()` runs.

### Add GOT sections to `.data.at_dtcm`

Find this part of `.data.at_dtcm`:

```ld
    KEEP(*(.jcr*))
    . = ALIGN(8);
```

Replace it with:

```ld
    KEEP(*(.jcr*))
    *(.got)
    *(.got.plt)
    . = ALIGN(8);
```

The ExecuTorch C++ libraries can use a Global Offset Table (GOT). These entries must be copied into RAM at startup.

### Route ExecuTorch buffers to SRAM0 and SRAM1

Find this existing block:

```ld
#if __HAS_BULK_SRAM
  .bss.at_sram0 (NOLOAD) : ALIGN(8)
  {
    *(.bss.lcd_crop_and_interpolate_buf)
    *(.bss.lcd_frame_buf)
    *(.bss.camera_frame_buf)
    *(.bss.camera_frame_bayer_to_rgb_buf)
  } > SRAM0
#endif
```

Replace it with:

```ld
#if __HAS_BULK_SRAM
  .bss.at_sram0 (NOLOAD) : ALIGN(8)
  {
    *(.bss.lcd_crop_and_interpolate_buf)
    *(.bss.lcd_frame_buf)
    *(.bss.camera_frame_buf)
    *(.bss.camera_frame_bayer_to_rgb_buf)
    *(.bss.at_sram0)
    *(.bss.at_sram0.*)
  } > SRAM0
  .bss.at_sram1 (NOLOAD) : ALIGN(8)
  {
    *(.bss.at_sram1)
    *(.bss.at_sram1.*)
  } > SRAM1
#endif
```

This must appear before the generic `.bss` section. Otherwise, sections such as `.bss.at_sram0` and `.bss.at_sram1` are caught by `*(.bss.*)` and placed in DTCM.

The project structure is ready. The next sections cover image preparation before you build and flash.

## What you've learned and what's next

You've created the mnist_executorch firmware project, configured CMSIS packs, and set up the linker to include ExecuTorch libraries with the correct archive flags.

You've also added the application code that loads the model and runs inference on the Ethos-U85 NPU.