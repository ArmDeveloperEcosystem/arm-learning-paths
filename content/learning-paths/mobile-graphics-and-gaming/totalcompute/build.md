---
# User change
title: "Build and run the Total Compute software stack"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
The [Arm Total Compute](https://developer.arm.com/Tools%20and%20Software/Total%20Compute) reference software stack is a fully integrated open-source stack, from firmware up to Android. he stack includes open-source code available from the relevant upstream projects: SCP firmware, Trusted firmware, Linux kernel, Android, and Arm NN.

## Download and install the FVP

The Total Compute reference stack is built to run on the Total Compute Fixed Virtual Platform (FVP), a complete virtual system implementation.

At time of writing, only the `TC0` FVP is publicly available from the [Arm Ecosystem FVPs](https://developer.arm.com/downloads/-/arm-ecosystem-fvps) page.

For access to later Total Compute FVPs, contact the Arm support team by [opening a support case](https://developer.arm.com/All%20Support%20Services). Access may be restricted depending on your organization.

You can download directly from the above Ecosystem FVP page, else with a command such as:
```console
wget https://developer.arm.com/-/media/Arm%20Developer%20Community/Downloads/OSS/FVP/TotalCompute/Total%20Compute%20Update%202022/FVP_TC0_11.17_18.tgz
```
To install to default location, agreeing to the EULA, use:
```console
tar -xf FVP_TC0_11.17_18.tgz
./FVP_TC0.sh --i-agree-to-the-contained-eula --no-interactive
```
## Build the software stack

The reference software can be built as a minimal BSP, or a full Android stack.

Complete build instructions are given in the documentation, see the section `Syncing and building the source code`:
- [TC0](https://gitlab.arm.com/arm-reference-solutions/arm-reference-solutions-docs/-/blob/master/docs/totalcompute/tc0/user-guide.rst)
- [TC1](https://gitlab.arm.com/arm-reference-solutions/arm-reference-solutions-docs/-/blob/master/docs/totalcompute/tc1/user-guide.rst)
- [TC2](https://gitlab.arm.com/arm-reference-solutions/arm-reference-solutions-docs/-/blob/master/docs/totalcompute/tc2/user-guide.rst)

Note that builds take a considerable time to complete.

## Run software on FVP

A `run_model.sh` script is provided to configure the FVP and load the appropriate binaries. See the `Running the software on FVP` section of the documentation.
- [TC0](https://gitlab.arm.com/arm-reference-solutions/arm-reference-solutions-docs/-/blob/master/docs/totalcompute/tc0/user-guide.rst)
- [TC1](https://gitlab.arm.com/arm-reference-solutions/arm-reference-solutions-docs/-/blob/master/docs/totalcompute/tc1/user-guide.rst)
- [TC2](https://gitlab.arm.com/arm-reference-solutions/arm-reference-solutions-docs/-/blob/master/docs/totalcompute/tc2/user-guide.rst)

