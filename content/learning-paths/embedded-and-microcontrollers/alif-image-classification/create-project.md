---
title: Create the image classification firmware project
weight: 4

layout: "learningpathall"
---

## What you'll build in this section

In this section, you duplicate the existing Blinky example to create a new CMSIS project called `mv2_runner`, configured to include ExecuTorch libraries, the compiled model, and SEGGER RTT for debug output.

## Duplicate the Blinky project

Start by copying the working Blinky project as a template:

```bash
cd ~/alif/alif_vscode-template
cp -R blinky/ mv2_runner
```

Rename the project file inside the new directory:

```bash
mv mv2_runner/blinky.cproject.yml mv2_runner/mv2_runner.cproject.yml
```

Replace all internal references from `blinky` to `mv2_runner`:

```bash
perl -pi -e 's/\bblinky\b/mv2_runner/g' $(grep -RIl "blinky" mv2_runner)
```

## Rename main.c to main.cpp

ExecuTorch is a C++ library, so the source file needs a `.cpp` extension:

```bash
mv mv2_runner/main.c mv2_runner/main.cpp
```

## Copy model assets

Create an assets directory and copy the model header into the project:

```bash
mkdir -p mv2_runner/assets
cp ~/alif/models/mv2_ethosu85_256_pte.h mv2_runner/assets/
```

## Create the SEGGER RTT configuration

RTT (Real-Time Transfer) works through the J-Link debug probe, reading and writing a memory buffer through the debug interface. It's faster than UART and doesn't require extra wiring. Create the configuration file `mv2_runner/SEGGER_RTT_Conf.h`:

```c
#ifndef SEGGER_RTT_CONF_H
#define SEGGER_RTT_CONF_H

#define SEGGER_RTT_MAX_NUM_UP_BUFFERS     (1)
#define SEGGER_RTT_MAX_NUM_DOWN_BUFFERS   (1)

#define SEGGER_RTT_BUFFER_SIZE_UP         (1024)
#define SEGGER_RTT_BUFFER_SIZE_DOWN       (16)

#define SEGGER_RTT_MODE_DEFAULT           SEGGER_RTT_MODE_NO_BLOCK_SKIP

#define SEGGER_RTT_PRINTF_BUFFER_SIZE     (256)

#endif
```

## Install additional CMSIS packs

The project depends on two CMSIS packs that aren't installed by default. Install them from the terminal:

```bash
cpackget add ARM::CMSIS-Compiler@2.1.0
cpackget add Keil::MDK-Middleware@8.2.0
```

## Update the solution file

Open `alif.csolution.yml` and make the following changes.

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
            - project-context: mv2_runner.debug
```

For all other target types (E7-HE, E7-HP, E1C-HE, E8-HE), add a `target-set` pointing to `blinky.debug` instead.

Add `mv2_runner` to the projects list:

```yaml
  projects:
    - project: blinky/blinky.cproject.yml
    - project: hello/hello.cproject.yml
    - project: hello_rtt/hello_rtt.cproject.yml
    - project: mv2_runner/mv2_runner.cproject.yml
```

## Configure the project file

Replace the contents of `mv2_runner/mv2_runner.cproject.yml` with the following configuration:

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/Open-CMSIS-Pack/devtools/tools/projmgr/2.6.0/tools/projmgr/schemas/cproject.schema.json
project:
  groups:
    - group: App
      files:
        - file: main.cpp
        - file: SEGGER_RTT_Conf.h
        - file: assets/input_image.h
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
    - ETHOSU85

  add-path:
    - .
    - ../libs/SEGGER_RTT_V796h/RTT
    - ../third_party/executorch/et_bundle/include
    - ../third_party/executorch/et_bundle/include/executorch/runtime/core/portable_type/c10

  misc:
    - for-compiler: GCC
      Link:
        - -L/absolute/path/to/alif/third_party/executorch/lib
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
You must update the `-L` path to match the absolute path to your `third_party/executorch/lib` directory. For example: `-L/Users/username/alif/third_party/executorch/lib`.
{{% /notice %}}

There are several important details in this configuration:

- **`--whole-archive`** is required for `libexecutorch`, `libexecutorch_core`, `libexecutorch_delegate_ethos_u`, and `libcortex_m_ops_lib`. These libraries contain static registration constructors (for operator registration and PAL symbols) that the linker would otherwise discard as unused.
- **Don't add** `portable_ops_lib` or `quantized_ops_lib` to `--whole-archive`. They are large and will overflow the microcontroller's ITCM/MRAM.
- **`--start-group`/`--end-group`** resolves circular dependencies among the remaining libraries.
- **`C10_USING_CUSTOM_GENERATED_MACROS`** tells ExecuTorch to skip looking for a `cmake_macros.h` header that doesn't exist in the bare-metal build.
- The **c10 include path** provides the tensor type definitions that ExecuTorch's headers depend on.

The project structure is ready. The next sections cover the application code, memory configuration, and image preparation before you build and flash.
