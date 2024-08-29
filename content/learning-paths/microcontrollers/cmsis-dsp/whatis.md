---
# User change
title: What is CMSIS-DSP?

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
The [CMSIS-DSP](https://arm-software.github.io/CMSIS-DSP/latest/) software library is an open-source suite of common compute processing functions optimized for Arm Cortex-A and Cortex-M processors.

The source code is available in [this GitHub repository](https://github.com/ARM-software/CMSIS-DSP).

The library is easiest to use with Development tool IDEs such as `Keil MDK` and `Arm Development Studio`.

The library can be installed as a [CMSIS-Pack](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/index.html).

A number of example projects are also provided.


## Development Tools

[Arm Keil MDK](https://www.keil.arm.com/) will be used for this learning path. You can use `Keil Studio Visual Studio Code Extensions` or (legacy) `Keil μVision` IDE.

See the below install guides for set up instructions:

* [Keil Studio VS Code Extensions](/install-guides/keilstudio_vs/)
* [Keil μVision](/install-guides/mdk/)

Install the appropriate IDE you wish to use.

## Using the CMSIS-DSP library

To make any function from the `CMSIS-DSP` library available to your code, simply include the `arm_math.h` header file in any relevant source:
```C
#include "arm_math.h"
```
This file resides in the `Include` folder of the library installation.

The [Dot Product example](https://www.keil.com/pack/doc/CMSIS/DSP/html/group__DotproductExample.html) used makes use of two functions from the library:

  * `arm_mult_f32()`
  * `arm_add_f32()`

The appropriate implementation is selected at build time based on the processor.

For more information refer to the [CMSIS-DSP library documentation](https://arm-software.github.io/CMSIS-DSP/latest/index.html).
