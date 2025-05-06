---
title: Use TF-A extra build options to build cpu_ops into images
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### 1. Why build cpu_ops into images

If you build the software without any modification, you might get the following error message after running the software stack:

```
ASSERT: File lib/cpus/aarch64/cpu_helpers.S Line 00035
```

The previous error message is issued because the TF-A does not build the cpu_ops into the images:

```
31   /* Get the matching cpu_ops pointer */

32   bl   get_cpu_ops_ptr

33 #if ENABLE_ASSERTIONS

34   cmp  x0, #0

35   ASM_ASSERT(ne)

36 #endif
```


The cpu_ops are defined in the source file as follows:

```
lib/cpus/aarch64/cortex_a510.S
lib/cpus/aarch64/cortex_a53.S
lib/cpus/aarch64/cortex_a55.S
lib/cpus/aarch64/cortex_a57.S
lib/cpus/aarch64/cortex_a65.S
lib/cpus/aarch64/cortex_a65ae.S
lib/cpus/aarch64/cortex_a710.S
lib/cpus/aarch64/cortex_a715.S
lib/cpus/aarch64/cortex_a72.S
lib/cpus/aarch64/cortex_a73.S
```

Check the Makefile (plat/arm/board/fvp/platform.mk) of the FVP platform. You can find the following code:  

```
ifeq (${HW_ASSISTED_COHERENCY}, 0)
# Cores used without DSU
	FVP_CPU_LIBS	+=	lib/cpus/aarch64/cortex_a35.S			\
				lib/cpus/aarch64/cortex_a53.S			\
				lib/cpus/aarch64/cortex_a57.S			\
				lib/cpus/aarch64/cortex_a72.S			\
				lib/cpus/aarch64/cortex_a73.S
else
# Cores used with DSU only
	ifeq (${CTX_INCLUDE_AARCH32_REGS}, 0)
	# AArch64-only cores
		FVP_CPU_LIBS	+=	lib/cpus/aarch64/cortex_a76.S		\
					lib/cpus/aarch64/cortex_a76ae.S		\
					lib/cpus/aarch64/cortex_a77.S		\
					lib/cpus/aarch64/cortex_a78.S		\
					lib/cpus/aarch64/neoverse_n_common.S	\
					lib/cpus/aarch64/neoverse_n1.S		\
					lib/cpus/aarch64/neoverse_n2.S		\
					lib/cpus/aarch64/neoverse_e1.S		\
					lib/cpus/aarch64/neoverse_v1.S		\
					lib/cpus/aarch64/neoverse_v2.S	\
					lib/cpus/aarch64/cortex_a78_ae.S	\
					lib/cpus/aarch64/cortex_a510.S		\
					lib/cpus/aarch64/cortex_a710.S		\
					lib/cpus/aarch64/cortex_a715.S		\
					lib/cpus/aarch64/cortex_x3.S 		\
					lib/cpus/aarch64/cortex_a65.S		\
					lib/cpus/aarch64/cortex_a65ae.S		\
					lib/cpus/aarch64/cortex_a78c.S		\
					lib/cpus/aarch64/cortex_hayes.S		\
					lib/cpus/aarch64/cortex_hunter.S	\
					lib/cpus/aarch64/cortex_x2.S		\
					lib/cpus/aarch64/neoverse_poseidon.S
	endif
	# AArch64/AArch32 cores
	FVP_CPU_LIBS	+=	lib/cpus/aarch64/cortex_a55.S		\
				lib/cpus/aarch64/cortex_a75.S
endif
```

HW_ASSISTED_COHERENCY = 0 and CTX_INCLUDE_AARCH32_REGS =1 are default build options.

### 2. Required build options

Building the cpu_ops into the TF-A image requires different build options, depending on the CPU type. For example, different platforms require different build options when building the TF-A:

* For the A55 CPU FVP, add the HW_ASSISTED_COHERENCY=1 and USE_COHERENT_MEM=0 build options.
* For the A78 CPU FVP, add the HW_ASSISTED_COHERENCY=1, USE_COHERENT_MEM=0, and CTX_INCLUDE_AARCH32_REGS=0 build options.
* For the A53 CPU FVP, you do not need extra build options.

Note: The build option USE_COHERENT_MEM cannot be enabled with HW_ASSISTED_COHERENCY=1.


### 3. Steps to build cpu_ops into the TF-A image

Perform the following steps to build cpu_ops into the TF-A image:

3.1  Modify the following build script to add build options. The [Arm reference software stack](https://gitlab.arm.com/arm-reference-solutions/arm-reference-solutions-docs/-/blob/master/docs/aemfvp-a/user-guide.rst) uses the [build-scripts](https://gitlab.arm.com/arm-reference-solutions/build-scripts) to build the TF-A.

```
build-scripts/ configs/aemfvp-a/aemfvp-a
```

3.2 Add TF-A build options, depending on the CPU type. For example:

* For A55 CPU FVP, add the following line:

```
ARM_TF_BUILD_FLAGS="$ARM_TF_BUILD_FLAGS HW_ASSISTED_COHERENCY=1 USE_COHERENT_MEM=0 "
```

* For A78 CPU FVP, add the following line:

```
ARM_TF_BUILD_FLAGS="$ARM_TF_BUILD_FLAGS HW_ASSISTED_COHERENCY=1 USE_COHERENT_MEM=0 CTX_INCLUDE_AARCH32_REGS=0"
```

3.3  Rebuild the TF-A by using the following commands:

```
./build-scripts/build-arm-tf.sh -p aemfvp-a -f busybox clean

./build-scripts/build-arm-tf.sh -p aemfvp-a -f busybox build
```

3.4 Package the built TF-A into the BusyBox disk image by using the following command:

```
./build-scripts/aemfvp-a/build-test-busybox.sh -p aemfvp-a package
```

