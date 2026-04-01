---
title: Get started
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare your environment

For this learning path, you will use an Arm Linux system (aarch64), such as an AWS Graviton instance running Amazon Linux 2023; it has been tested on an AWS Graviton 3 `c7g.metal` instance with 64 Neoverse V1 cores.

Install the following packages, replacing `dnf` with the package manager for your Linux distribution.

```bash
sudo dnf update -y
sudo dnf install -y git cmake g++ environment-modules python3 python3-pip
```

Next, [install Arm Performix](https://learn.arm.com/install-guides/performix/) on the remote Arm Linux target (`c7g.metal` instance) and the graphical user interface on your local machine. There's no need to use the command-line interface (CLI).

Install the prebuilt Arm Performance Libraries on your Arm Linux system using the [install guide](https://learn.arm.com/install-guides/armpl/). Follow the instructions and load the module file. A module file configures your environment by setting paths and variables so the correct software and libraries are available. To verify the module loaded successfully, run:

```bash
module list
```

You should see the output below. You'll need to load the environment module with the `module load <arm-performance-lib>` command if it isn't already loaded.

```output
Currently Loaded Modulefiles:
 1) arm-performance-libraries
```

{{% notice Please Note %}}
When you open a new terminal, you will need to reload the modulefile. To simplify this, you can add the modulefile path to your `~/.bashrc` so modules can be loaded directly with the `module load <arm-performance-lib>` command
```bash
echo "export MODULEPATH=$MODULEPATH:/opt/arm/modulefiles" >> ~/.bashrc
```
{{% /notice %}}

Clone and build the example project:

```bash
git clone https://github.com/arm-education/Data-Processing-Example.git
cd Data-Processing-Example
```

In the next section, you examine what the data-processing example does and run the visualization helper.
