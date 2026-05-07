---
title: Alternative solutions
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Alternative solutions

### Step 3.0) Try another operating system or kernel

Many applications spend most execution time in user space, with relatively little time in kernel mode for tasks such as file handling. Even when an application spends meaningful time in kernel mode, switching to a newer or different kernel usually does not create a large performance change unless you are intentionally using a newer kernel feature.

Because of that, it is usually faster to try a different OS or kernel image before rebuilding your current kernel with SPE enabled. If you specifically need to rebuild your current kernel, continue to Step 3.1.

{{% notice Tip %}}
If you are unsure where your application is spending time, a basic command such as the one below can give you a high-level estimate of the ratio of user to kernel (also known as system) time.

```bash
/usr/bin/time -v <path to your application> 2>&1 | grep -e "User time" -e "System time"
```

In the [Mandelbrot example](/learning-paths/servers-and-cloud-computing/cpu_hotspot_performix/how-to-3/), about 0.3% of execution time is in kernel space.

```output
        User time (seconds): 47.52
        System time (seconds): 0.14
```
{{% /notice %}}

The quickest way to run the memory access recipe is often to test on a different operating system image. On cloud platforms, this is usually straightforward.

The information below is accurate at the time of writing, but SPE support can change over time. If you have access to the following cloud providers, use the recommended operating systems below.

{{< tabpane code=true >}}
{{< tab header="Amazon Web Services (AWS)" >}}
Amazon Linux 2023 AMI

Run on a metal instance (for example, `c<n>g.metal`, where `<n>` matches the required Graviton generation).
{{< /tab >}}
{{< tab header="Google Cloud Services (GCP)" >}}
The following images have been tested on Google Axion C4A metal instances and confirm SPE support.

**Ubuntu 24.04 LTS** and **Ubuntu 25.10** — both provide `arm_spe_pmu` as a loadable kernel module:

```
CONFIG_ARM_SPE_PMU=m
```

After loading the module, Sysreport confirms:

```
perf sampling:    SPE
```

**CentOS Stream 10 (Coughlan)** — also builds `arm_spe_pmu` as a loadable kernel module, and additionally includes Embedded Trace Macrocell (ETM) hardware trace support:

```
perf sampling:    SPE
perf HW trace:    ETM
```
{{< /tab >}}
{{< /tabpane >}}

### Step 3.1) Rebuild the kernel from source with Arm SPE

If your current system does not provide a kernel with Statistical Profiling Extension (SPE) enabled, you can rebuild the kernel with the required configuration. This approach is more involved than switching operating systems and should only be used if necessary.

#### Distribution-specific considerations

Most Linux distributions (for example Ubuntu or Debian) ship kernels with their own patches and configuration defaults. As a result, you should follow your distribution’s official kernel build guide rather than using a generic upstream process, for example the [Ubuntu](https://wiki.ubuntu.com/Kernel/BuildYourOwnKernel) and [Debian](https://wiki.debian.org/BuildingTutorial) guides. In some environments (e.g. cloud platforms), you may also need to build against a provider-specific kernel variant.


#### Enable Arm SPE in the kernel configuration

The key requirement is to ensure that the `CONFIG_ARM_SPE_PMU` option is enabled in the kernel `.config`.

If you already have a configured kernel tree, you can enable it directly using:

```bash
scripts/config --enable ARM_SPE_PMU
```

Note that `scripts/config` automatically strips the `CONFIG_` prefix from option names, so `ARM_SPE_PMU` is the correct argument even though the option is named `CONFIG_ARM_SPE_PMU` in the `.config` file. This modifies the `.config` file and sets:

```
CONFIG_ARM_SPE_PMU=y
```

After modifying the config, run:

```bash
make olddefconfig
```

This resolves any new dependencies introduced by enabling `CONFIG_ARM_SPE_PMU` and sets unset options to their defaults. It is non-interactive and will not prompt you for input.

### Use the interactive configuration menu

Alternatively, you can enable the option via the interactive terminal UI from the root of the kernel directory:

```bash
make menuconfig
```

- Press `/` to search.
- Enter `ARM_SPE_PMU`. The `menuconfig` search also strips the `CONFIG_` prefix, so entering `ARM_SPE_PMU` is correct.
- Select the option when it appears.
- Press:
  - `y` to build it into the kernel (`=y`)
  - `m` to build it as a module (`=m`)

In most cases, building it into the kernel (`y`) is preferred for profiling.

![Screenshot of the kernel menuconfig interface with ARM_SPE_PMU selected and enabled, confirming the Statistical Profiling Extension will be built into the kernel#center](./enabled_support.png "Kernel menuconfig with ARM_SPE_PMU enabled")

Once the kernel has been built, set your system to boot from the new kernel.

{{% notice Warning %}}
Before rebooting into a custom kernel, take the following precautions to avoid being locked out of your system:

- **Take a snapshot or backup** of your instance before rebooting. On cloud platforms, create a machine image or disk snapshot so you can restore quickly if the new kernel fails to boot.
- **Keep the original kernel as a fallback.** Most bootloaders (for example GRUB) retain previous kernel entries. Confirm the original kernel is still listed before you reboot.
- **Verify the bootloader configuration.** Check `/etc/default/grub` and confirm `GRUB_DEFAULT` points to your new kernel entry, then run `update-grub` to apply the change.
- **Test the new kernel without changing the default boot entry.** Use `grub-reboot` to boot into the new kernel exactly once, so the system automatically reverts to the previous kernel on the next reboot if something goes wrong:

```bash
sudo grub-reboot "Advanced options for Ubuntu>Ubuntu, with Linux <your-kernel-version>"
sudo reboot
```

Replace `<your-kernel-version>` with the version string of your newly built kernel. You can list available entries with `grep menuentry /boot/grub/grub.cfg`.
{{% /notice %}}

## Summary

Your Arm Linux target now has SPE enabled and is ready for memory access profiling with Arm Performix.

Across this Learning Path you:

- Checked whether Arm SPE was already active on your target using Sysreport and kernel-level configuration checks.
- Identified the correct remediation path for your environment, whether that meant loading the `arm_spe_pmu` kernel module, installing matching extra-modules packages, selecting a supported cloud image, or rebuilding the kernel with `CONFIG_ARM_SPE_PMU` enabled.
- Verified the final state using Sysreport, confirming that `perf sampling` reports `SPE` rather than `None`.

With SPE confirmed as active, you can now open Arm Performix on your host machine, connect to the target over SSH, and run the Memory Access recipe to begin profiling memory access patterns on your Arm Neoverse system.