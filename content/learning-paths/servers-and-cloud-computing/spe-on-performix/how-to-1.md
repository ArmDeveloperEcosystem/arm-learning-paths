---
title: Understand Arm Statistical Profiling Extension (Arm SPE)
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is Arm Statistical Profiling Extension?

Arm Statistical Profiling Extension (SPE) is a hardware-assisted profiling feature in the Arm A-profile architecture. It was introduced with Armv8.2-A and extended in later architecture revisions. Most modern Arm-based cloud systems support SPE.

Unlike traditional interrupt-driven sampling, SPE records rich metadata for sampled operations, including instruction context, memory address information, and latency-related attributes. This improves attribution accuracy and helps reduce drift (also called skid) when mapping instructions to sampled counts. For more information, see the [performance analysis white paper](https://developer.arm.com/documentation/109429/latest/).

For Arm Performix, this matters because SPE must be enabled to use the `Memory Access` recipe.

## Understand the platform layers that enable Arm SPE

On Linux, SPE is available only when all required layers are aligned:

- **Architecture layer**: the CPU must implement SPE (common on Arm Neoverse systems and the Arm AGI CPU).
- **Firmware layer**: platform firmware must advertise the SPE PMU and its interrupt path through ACPI or Device Tree. This is usually already enabled, so this check is often skipped.
- **Kernel layer**: the running kernel must be built with Arm SPE PMU support through the `CONFIG_ARM_SPE_PMU` kernel build option.
- **Driver layer**: the `arm_spe_pmu` driver must initialize successfully, either built-in or loaded as a module. This requires all the other layers to have Arm SPE support.

If any of these layers are missing, Linux can't expose SPE to profiling tools. Additionally, cloud-based applications usually run on top of a hypervisor that typically disables SPE.

{{% notice Note %}}

Cloud providers often disable low-level profiling features on shared (multi-tenant) instances. To use Performix memory access profiling, run your application on an Arm-based bare-metal instance with full hardware access. These instances are typically named `metal` instances and typically cost more than virtualized instances.

{{%/ notice %}}

On Neoverse-based systems, architecture support is already present, and firmware support is usually present.

In this Learning Path, you'll follow a diagnostic flow with remediation paths based on what you find. Because Linux distributions and kernel versions vary widely, this Learning Path provides practical guidance rather than an exhaustive set of steps.

## Check whether Arm SPE is enabled

Open Performix from your local machine. If this is your first time using Performix, see the [Performix install guide](/install-guides/performix/).

Connect to your instance, select the `Recipes` tab, and then select the `Memory Access` recipe. Performix automatically runs a precheck and prints the status at the end of the page. If you receive the **SPE is not configured** status shown in the following screenshot, you need to enable SPE before you can run the recipe.

![Screenshot of the Arm Performix Memory Access recipe showing a red status notification at the bottom of the page indicating that SPE has not been configured for the target system. This is the expected message when the arm_spe_pmu driver is missing or not loaded.#center](./memory-access-no-spe.png "Arm Performix Memory Access recipe reporting that SPE is not configured")

If you receive a different error message, SPE might not be the cause of your issue. For more information, see the [Performix user guide](https://developer.arm.com/documentation/110163/latest).

## What you've learned and what's next

You now know what Arm SPE is and what platform layers need to be present to support SPE. You also checked whether Arm SPE is enabled on your instance. 

Next, you'll check whether the OS kernel of the instance is built with Arm SPE or includes modules that can be loaded. You'll learn about different remediation steps based on your environment.