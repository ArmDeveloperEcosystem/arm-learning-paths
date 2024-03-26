---
title: Create a Debug Connection
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create a Debug Connection
{{% notice %}}
In this example, we will be working with the RD-N2 platform.
{{% /notice %}}

1. Modify the rdinfra/model-scripts/rdinfra/platforms/rdn2/run_model.sh.
1. Remove –R parameter from PARAMS= section. That makes FVP stop while cores are in reset and wait for the debug connection.

![modify parameters alt-text#center](images/modify_params.png "Figure 1. Modify run_model.sh")

{{% notice %}}
FVPS do not completely model the IMP DEF behavior that RTL does. FVPs also do not model cycles/performance or AXI/ACE/AHB/CHI bus level transactions.
{{% /notice %}}

