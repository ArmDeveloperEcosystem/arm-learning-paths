---
# User change
title: "Set up the Corstone-320 FVP"

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Corstone-320 FVP Setup for ExecuTorch

Navigate to the Arm examples directory in the ExecuTorch repository.

```bash
cd $HOME/executorch/examples/arm
./setup.sh --i-agree-to-the-contained-eula
```

After the script has finished running, it prints a command to run to finalize the installation. This will add the FVP executable's to your path.

```bash
source $HOME/executorch/examples/arm/ethos-u-scratch/setup_path.sh
```

Test that the setup was successful by running the `run.sh` script for Ethos-U85, which is the target device for Corstone-320.

```bash
 ./examples/arm/run.sh --target=ethos-u85-256
```

You will see a number of examples run on the FVP. This means you can proceed to the next section [Build a Simple PyTorch Model](/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/build-model-8/) to test your environment setup.