---
# User change
title: "Set up the Grove Vision AI Module V2"

weight: 6 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
## Before you begin 

This section requires the Grove Vision AI Module. Due to its constrained environment, we will focus on lightweight, optimized, tools and models.

### Compilers 

The examples can be built with Arm Compiler for Embedded or Arm GNU Toolchain.

Use the install guides to install each compiler on your host machine:
- [Arm Compiler for Embedded](/install-guides/armclang/).
- [Arm GNU Toolchain](/install-guides/gcc/arm-gnu/).

## Board Setup 

![Hardware Overview #center](Overview.png)

Hardware overview: [Image credits](https://wiki.seeedstudio.com/grove_vision_ai_v2/). 

1. Download and extract the latest Edge Impulse firmware
Grove Vision V2 [Edge impulse Firmware](https://cdn.edgeimpulse.com/firmware/seeed-grove-vision-ai-module-v2.zip). 

2. Connect the Grove Vision AI Module V2 to your computer using the USB-C cable. 

![Board connection](Connect.png)

{{% notice Note %}}
Ensure the board is properly connected and recognized by your computer.
{{% /notice %}}

3. In the extracted Edge Impulse firmware, locate and run the `flash_linux.sh` script to flash your device. 

   ```console
   ./flash_linux.sh
   ```
You have now set up the board successfully. In the next section, you will learn how to use the functionality in the ExecuTorch repository for TinyML, using a hardware emulator.

{{% notice Note %}}
In the next Learning Path in this series, you will incorporate the board into the workflow, running workloads on real hardware.
{{% /notice %}}

Continue to the next page to build a simple PyTorch model.
