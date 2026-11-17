---
title: Understand the reusable CMSIS project
weight: 6
description: See how the solution, application project, board layer, and generated AI layer form the Corstone-300 runner.

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand the solution file

After understanding the CMSIS Packs needed by the project, explore how the project works. 

`cmsis-executorch-u55.csolution.yml` defines the complete Ethos-U55 build context.
The target definition in the solution file includes:

```yaml
target-types:
  - type: SSE-300-U55
    board: V2M-MPS3-SSE-300-FVP
    device: SSE-300-MPS3
    variables:
      - Board-Layer: $SolutionDir()$/board/Corstone-300/Board-U55.clayer.yml
      - AI-Layer: $SolutionDir()$/ai_layer/ai_layer.clayer.yml
```

`SSE-300-U55` is the readable target name of the project. The board and device
values identify records supplied by installed Packs. CMSIS-Toolbox uses those
identities to resolve startup files, memory information, and device conditions.

The `mlops:` node in the solution file is the single source for the NPU and Vela target
settings:

```yaml
mlops:
  npu:
    type: Ethos-U55
    macs: 128
  vela:
    system: Ethos_U55_High_End_Embedded
    memory: Shared_Sram
  model:
    clayer: $AI-Layer$
    name: TinyCNN
    input-shape: 1x16x16x3
    calibration-samples: 2
```

`cbuild setup` resolves this into the `*.cbuild-mlops.yml` file that's consumed by
`create_ai_layer.py`. The exporter therefore doesn't duplicate the
NPU configuration of the project.

## Follow the layers into the project

`cmsis-executorch.cproject.yml` owns the application and consumes two layers:

```yaml
groups:
  - group: App
    files:
      - file: ./src/app_main.cpp
      - file: ./src/arm_embedded_module.cpp
      - file: ./src/arm_embedded_module.hpp

layers:
  - layer: $Board-Layer$
    type: Board
  - layer: $AI-Layer$
    type: AI
```

Each part has one job:

- The Board layer supplies Cortex-M55 startup, the memory layout, and standard
  output. It also provides the Ethos-U55 driver and Corstone-300 initialization.
- The generated AI layer supplies the embedded model and its exact ExecuTorch
  and CMSIS-NN component selection.
- The App group initializes ExecuTorch, creates an input tensor, runs one
  inference, and prints the ten output values.

The Fixed Virtual Platform (FVP) configuration in `board/Corstone-300/fvp_config_u55.txt` describes the
simulated hardware. It's separate from the Board layer because one configures
the simulator, while the other builds software for the simulated target.

## See how the PTE enters the firmware

The AI-layer directory now contains the following related model files:

```text
ai_layer/model.pte
ai_layer/model_pte.c
ai_layer/model_pte.h
```

`model.pte` is the serialized ExecuTorch program. `model_pte.c` contains the
same bytes represented as a C array. This is why it appears to be a long list
of numbers. Embedding the bytes lets a bare-metal system load the program
without a filesystem.

`src/app_main.cpp` includes `model_pte.h`, wraps a deterministic
`1 x 16 x 16 x 3` input buffer as an ExecuTorch tensor, and calls the runtime.
The runtime follows the PTE execution plan. It invokes the Ethos-U backend for
the delegate and CPU kernels for the remaining operations.

The runner doesn't need model-specific edits because the adapted model preserves the original input shape and ten-value
output. A different model shape
or output contract would need corresponding changes in `app_main.cpp`.

## What you've learned and what's next

You've traced the ready-made project from target selection to the embedded
PTE. The repository removes board bring-up work while keeping
the CMSIS structure visible and reusable.

Next, you'll compile these parts, verify which Pack sources were used, and run
the image on the Corstone-300 FVP.
