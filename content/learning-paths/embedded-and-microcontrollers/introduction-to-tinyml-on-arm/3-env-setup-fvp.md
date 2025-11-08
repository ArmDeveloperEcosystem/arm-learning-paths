---
# User change
title: "Set up the Corstone-320 FVP"

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Overview

In this section, you run scripts to set up the Corstone-320 reference package.

The Corstone-320 Fixed Virtual Platform (FVP) is a pre-silicon software development environment for Arm-based microcontrollers. It provides a virtual representation of hardware so you can test and optimize software before boards are available. Designed for AI and machine learning workloads, it includes support for Arm Ethos-U NPUs and Cortex-M processors, which makes it well-suited to embedded AI applications. The FVP accelerates development by enabling early software validation and performance tuning in a flexible, simulation-based environment.

The Corstone reference system is provided free of charge, although you will have to accept the license in the next step. For more information on Corstone-320, check out the [official documentation](https://developer.arm.com/documentation/109761/0000?lang=en).

## Set up Corstone-320 FVP for ExecuTorch

Run the FVP setup script in the ExecuTorch repository:

```bash
cd $HOME/executorch
./examples/arm/setup.sh --i-agree-to-the-contained-eula
```

When the script completes, it prints a command to finalize the installation by adding the FVP executables to your `PATH`:

```bash
source $HOME/executorch/examples/arm/ethos-u-scratch/setup_path.sh
```

Then configure git informations, you can stay anonymous or fill in your email and name:

```bash
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

Test that the setup was successful by running the `run.sh` script for Ethos-U85, which is the target device for Corstone-320:

```bash
 ./examples/arm/run.sh --target=ethos-u85-256
```

You will see a number of examples run on the FVP.

This confirms the installation, so you can now proceed to the Learning Path [Build a Simple PyTorch Model](/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/4-build-model/).
