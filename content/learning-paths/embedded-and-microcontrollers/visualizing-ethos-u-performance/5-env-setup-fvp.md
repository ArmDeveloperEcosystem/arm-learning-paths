---
# User change
title: "Set up the Corstone-320 Fixed Virtual Platform"

weight: 5 

# Do not modify these elements
layout: "learningpathall"
---

## Get started with the Corstone-320 FVP

In this section, you’ll install and configure the Corstone-320 FVP to simulate an Arm-based embedded system. This lets you run ExecuTorch-compiled models in a virtual environment without any hardware required.

## Install the Corstone-320 FVP

Before you begin, make sure you’ve completed the steps in the previous section to install ExecuTorch.

{{< notice Note >}}
If you're using macOS, you need to perform additional setup to support FVP execution.  

See the <a href="https://github.com/Arm-Examples/FVPs-on-Mac/" target="_blank">FVPs-on-Mac GitHub repo</a> for instructions before continuing.
{{< /notice >}}

Run the setup script provided in the ExecuTorch examples directory:

```bash
cd $HOME/executorch/examples/arm
./setup.sh --i-agree-to-the-contained-eula
```

The `--i-agree-to-the-contained-eula` flag is required to run the script. It indicates your acceptance of Arm’s licensing terms for using the FVP.

This installs the FVP and extracts all necessary components. It also prints a command to configure your shell environment.

## Add the FVP to your system PATH

Run the following command to update your environment:

```bash
source $HOME/executorch/examples/arm/ethos-u-scratch/setup_path.sh
```

This ensures the FVP binaries are available in your terminal session.

## Verify your setup

Run a quick test to check that the FVP is working:


```bash
./examples/arm/run.sh --target=ethos-u85-256
```

This executes a built-in example on the Ethos-U85 configuration of the Corstone-320 platform.

{{% notice macOS %}}

On macOS, make sure Docker is running. FVPs execute inside a Docker container on macOS systems.

{{% /notice %}}

If you see example output from the platform, the setup is complete.

## Next steps
You’re now ready to deploy and run your own TinyML model using ExecuTorch on the Corstone-320 FVP.










