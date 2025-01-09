---
# User change
title: "Set up the Corstone-300 FVP"

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Corstone-300 FVP Setup for ExecuTorch

Navigate to the Arm examples directory in the ExecuTorch repository.
```bash
cd $HOME/executorch/examples/arm
./setup.sh --i-agree-to-the-contained-eula
```

```bash
export FVP_PATH=${pwd}/ethos-u-scratch/FVP-corstone300/models/Linux64_GCC-9.3
export PATH=$FVP_PATH:$PATH
```
Test that the setup was successful by running the `run.sh` script.

```bash
./run.sh
```

TODO connect this part to simple_nn.py part?

You will see a number of examples run on the FVP. This means you can proceed to the next section to test your environment setup.
