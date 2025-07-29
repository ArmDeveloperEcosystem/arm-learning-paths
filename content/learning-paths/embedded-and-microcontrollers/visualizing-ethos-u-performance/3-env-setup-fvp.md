---
# User change
title: "Set up the Corstone-320 FVP on Linux"

weight: 4 

# Do not modify these elements
layout: "learningpathall"
---
## What is Corstone-320?

To simulate embedded AI workloads on Arm hardware, you’ll use the Corstone-320 Fixed Virtual Platform (FVP). This pre-silicon software development environment for Arm-based microcontrollers provides a virtual representation of hardware, allowing developers to test and optimize software before actual hardware is available. Designed for AI and machine learning workloads, it includes support for Arm's Ethos-U NPU and Cortex-M processors, making it ideal for embedded AI applications. The FVP accelerates development by enabling early software validation and performance tuning in a flexible, simulation-based environment.

The Corstone-320 reference system is free to use, but you'll need to accept the license agreement during installation.  
For more information, see the [official Corstone-320 documentation](https://developer.arm.com/documentation/109761/0000?lang=en).

## Set up the Corstone-320 FVP for ExecuTorch

Before you begin, make sure you’ve completed the steps in the previous section to install ExecuTorch.

{{< notice note >}}
On macOS, you'll need to perform additional setup to support FVP execution.  
See the [FVPs-on-Mac GitHub repo](https://github.com/Arm-Examples/FVPs-on-Mac/) for instructions before continuing.
{{< /notice >}}







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

This confirms the installation, so you can now proceed to the next section.






