---
title: Set up environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

This learning path assumes you have a Arm Development Studio installed and an appropriate license set up. See the [install guide](//install-guides/armds) for instructions. Screenshots shown are from the 2023.0 version.

The learning path also assumes you have set up the Neoverse Reference Design software stack and associated FVP. See this [learning path](//learning-paths/servers-and-cloud-computing/refinfra-quick-start/) for instructions. The Neoverse N2 (`RD-N2`) stack is used.

## Modify the run script

Modify the provided script at:

```bash
rdinfra/model-scripts/rdinfra/platforms/rdn2/run_model.sh
```
Remove `–R` parameter from `PARAMS=` section. This option was used in the original script to allow the FVP to continue to execute and not wait for the debug connection.

![modify parameters alt-text#center](images/modify_params.png "Figure 1. Modify run_model.sh")

{{% notice Debug server %}}
The `-S` option is used to start a `CADI` debug server. Changing this to `-I` would start an `Iris` debug server instead.
{{% /notice %}}

Run the script to launch the model.
```bash
./run_model.sh
```

{{% notice FVP Accuracy %}}
FVPS do not completely model the `IMP DEF` behavior that RTL does.

FVPs also do not model cycles/performance nor `AXI/ACE/AHB/CHI` bus level transactions.
{{% /notice %}}
