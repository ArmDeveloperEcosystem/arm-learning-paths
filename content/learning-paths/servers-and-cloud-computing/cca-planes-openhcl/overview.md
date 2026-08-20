---
# User change
title: "Understand CCA planes"

weight: 2

# Do not modify these elements
layout: "learningpathall"
---

## Understand CCA planes

Arm Confidential Compute Architecture (CCA) protects confidential workloads by running them in Realms. Planes extend this model by dividing a Realm into multiple isolated execution environments.

Plane 0 is the initial Realm execution environment. Plane N is an auxiliary plane that plane 0 software can enter by using the Realm Service Interface (RSI). In this Learning Path, plane 0 runs a Linux kernel with support for the OpenHCL prototype. Plane 0 then starts a small VMM process, `tmk_vmm`, which enters plane 1 and runs the `simple_tmk` test microkernel.

The prototype stack has the following components:

- An Arm FVP with Realm Management Extension (RME), Permission Indirection, and Permission Overlay support enabled.
- Trusted Firmware-A (TF-A) and the Realm Management Monitor (RMM) built with CCA v1.1 experimental features enabled.
- Host Linux and `kvmtool` with support for creating a Realm that has an auxiliary plane.
- Plane 0 Linux with CCA guest support, 9P filesystem support, and OpenHCL driver support.
- `tmk_vmm` and `simple_tmk`, built from OpenVMM/OpenHCL sources.

Plane 0 prepares memory and processor state for the auxiliary plane. When `tmk_vmm` runs, it uses the CCA backend to call into the plane support exposed by plane 0 Linux. The RMM handles the transition from plane 0 to plane 1, and returns control to plane 0 on a plane exit.

## What you've learned

You have seen the role of each component in the prototype flow. Next, set up the host machine and build the software stack.

