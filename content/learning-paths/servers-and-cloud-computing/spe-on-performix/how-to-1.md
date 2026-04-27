---
title: Get started
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is Arm Statistical Profiling Extension

Arm Statistical Profiling Extension (SPE) is a hardware-assisted profiling feature in the Arm A-profile architecture. It was introduced with Armv8.2-A and extended in later architecture revisions. Most modern Arm-based cloud systems support SPE.

Unlike traditional interrupt-driven sampling, SPE records rich metadata for sampled operations, including instruction context, memory address information, and latency-related attributes. This improves attribution accuracy and helps reduce drift (also called skid) when mapping instructions to sampled counts. For more background, see the [performance analysis white paper](https://developer.arm.com/documentation/109429/latest/).

For Arm Performix, this matters because SPE must be enabled to use the `Memory Access` recipe.

## Understand the platform layers that enable SPE

On Linux, SPE is available only when all required layers are aligned:

- **Architecture layer**: the CPU must implement SPE (common on Arm Neoverse systems and the Arm AGI CPU).
- **Firmware layer**: platform firmware must advertise the SPE PMU and its interrupt path through ACPI or Device Tree. This is usually already enabled, so this check is often skipped.
- **Kernel layer**: the running kernel must be built with Arm SPE PMU support through the `CONFIG_ARM_SPE_PMU` kernel build option.
- **Driver layer**: the `arm_spe_pmu` driver must initialize successfully (built-in or loaded as a module). This requires all the above layers to have Arm SPE support.

If any of these layers are missing, Linux cannot expose SPE to profiling tools. Additionally, cloud-based applications usually run on top of a hypervisor which typically disables SPE.

{{% notice Please Note %}}
 
Cloud providers often disable low-level profiling features on shared (multi-tenant) instances. To use Performix memory access profiling, run your application on an Arm-based **bare-metal instance** with full hardware access. These instances are typically named `metal` instances.

Be aware that this instance type typically has a higher cost.

{{% /notice %}}


## What is usually already present

On Neoverse-based systems, architecture support is already present, and firmware support is usually present.

This Learning Path helps you determine which case applies to your system and what action to take next. Because Linux distributions and kernel versions vary widely, this Learning Path provides practical guidance rather than an exhaustive set of steps.

## Check if Arm SPE is enabled

Open Performix from your local machine. If this is your first time using or installing Performix, see the [install guide](https://learn.arm.com/install-guides/performix/).

Connect to your instance, select the `Recipes` tab, and then select the `Memory Access` recipe. This automatically runs a precheck and prints the status at the bottom of the page. If you receive the **SPE is not configured** status shown below, you need to enable SPE before you can run the recipe.

![Screenshot of the Arm Performix Memory Access recipe showing a red status notification at the bottom of the page indicating that SPE has not been configured for the target system. This is the expected message when the arm_spe_pmu driver is missing or not loaded.#center](./memory-access-no-spe.png "Arm Performix Memory Access recipe reporting that SPE is not configured")

If you receive a different error message, SPE is likely **not** the cause of your issue. See the [Performix user guide](https://developer.arm.com/documentation/110163/latest).




