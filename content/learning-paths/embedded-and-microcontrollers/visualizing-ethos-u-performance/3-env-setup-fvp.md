---
# User change
title: "Set up the Corstone-320 FVP on Linux"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

In this section, you will run scripts to set up the Corstone-320 reference package.

The Corstone-320 Fixed Virtual Platform (FVP) is a pre-silicon software development environment for Arm-based microcontrollers. It provides a virtual representation of hardware, allowing developers to test and optimize software before actual hardware is available. Designed for AI and machine learning workloads, it includes support for Arm's Ethos-U NPU and Cortex-M processors, making it ideal for embedded AI applications. The FVP accelerates development by enabling early software validation and performance tuning in a flexible, simulation-based environment.

The Corstone reference system is provided free of charge, although you will have to accept the license in the next step. For more information on Corstone-320, check out the [official documentation](https://developer.arm.com/documentation/109761/0000?lang=en).

## Corstone-320 FVP Setup for ExecuTorch

{{% notice macOS %}}

Setting up FVPs on MacOS requires some extra steps, outlined in GitHub repo [FVPs-on-Mac](https://github.com/Arm-Examples/FVPs-on-Mac/). macOS users must do this first, before setting up the Corstone-320 FVP.

{{% /notice %}}

Navigate to the Arm examples directory in the ExecuTorch repository. Run the following command.

```bash
cd $HOME/executorch/examples/arm
./setup.sh --i-agree-to-the-contained-eula
```

After the script has finished running, it prints a command to run to finalize the installation. This step adds the FVP executables to your system path.

```bash
source $HOME/executorch/examples/arm/ethos-u-scratch/setup_path.sh
```

Test that the setup was successful by running the `run.sh` script for Ethos-U85, which is the target device for Corstone-320:

{{% notice macOS %}}

**Start Docker:** on macOS, FVPs run inside a Docker container.

{{% /notice %}}

```bash
 ./examples/arm/run.sh --target=ethos-u85-256
```

You will see a number of examples run on the FVP.

This confirms the installation, so you can now proceed to the Learning Path [Build a Simple PyTorch Model](/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/4-build-model/).
