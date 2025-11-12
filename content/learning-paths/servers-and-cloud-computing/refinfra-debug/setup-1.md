---
title: Set up your development environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

To debug the Neoverse N2 reference firmware, you need Arm Development Studio installed, and an appropriate license. See the [Arm Development Studio Install Guide](/install-guides/armds) for instructions. Screenshots are from Arm Development Studio 2023.0.

You also need the Neoverse RD-N2 Reference Design Software Stack set up, and an associated FVP (Fixed Virtual Platform). You should be familiar with [Get started with the Neoverse Reference Design Software Stack](/learning-paths/servers-and-cloud-computing/refinfra-quick-start/) before you start debugging.

## SCP/LCP/RSE debug

If you want to debug SCP/LCP/RSE, you need to modify the run script:

```console
rdinfra/model-scripts/rdinfra/platforms/rdn2/run_model.sh
```

To prepare for debugging, remove the `–R` parameter from the `PARAMS=` section. 

When `-R` is used, the FVP continues execution and does not wait for the debug connection.

![modify parameters alt-text#center](images/modify_params.webp "Figure 1. Modify run_model.sh")

{{% notice Debug server %}}
To start a `CADI` debug server, use the `-S` option. For an `Iris` debug server, change this to `-I` instead.
{{% /notice %}}

Run the script to launch the model:

```bash
./run_model.sh
```

## AP debug

To debug the AP, you do not want to remove the `-R` flag. 

If you remove the `-R` flag, RSE CPU waits and the APs will be powered off. You will have to kick-off the run, then it starts booting from RSE to AP cores. 

This will be explained further in BL1, BL31, and BL33 chapters.

{{% notice FVP Accuracy %}}
FVPs do not model the `IMP DEF` behavior with the same level of detail included in the RTL design. 

FVPs do not model cycles, performance, or `AXI/ACE/AHB/CHI` level transactions.
{{% /notice %}}
