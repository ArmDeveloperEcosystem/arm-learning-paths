---
title: "VirtIO for device attach"
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you will learn how VirtIO works in the context of Arm CCA Realms and how it enables efficient data exchange between a Realm and the untrusted external world.

A Realm must eventually use physical devices to interact with the external world. The simplest way to do this is by using VirtIO, which provides a fast, paravirtualized interface. This is considered the first level of device attach, where access is mediated by the hypervisor using paravirtualized drivers.

More advanced device attach features can be enabled by hardware security features such as PCIe-TDISP (TEE Device Interface Security Protocol) and PCIe-IDE (Integrity
and Data Encryption). In those cases, the host OS assigns a physical device to a Realm, and the Realm can then measure the device and include those measurements in its attestation base.

## What is VirtIO?

VirtIO is a standardized, paravirtualized interface for virtual devices in virtualized environments. It allows guest operating systems to use optimized drivers to communicate with host-provided devices, avoiding the overhead of fully emulating physical hardware.

Paravirtualized means that the guest OS is aware it’s running in a virtualized environment. It allows guest operating systems to use optimized drivers to communicate with host-provided virtual hardware. Emulating physical hardware devices (like NICs or disks) for VMs is slow and inefficient. VirtIO allows VMs to bypass full device emulation and use streamlined drivers.

VirtIO is most commonly used with KVM/QEMU virtualization. Example drivers include:

- `virtio-net`: paravirtualized networking
- `virtio-blk`: block storage
- `virtio-fs`: file sharing between host and guest
- `virtio-balloon`: dynamic memory management
- `virtio-rng`: random number source
- `virtio-console`: simple console interface

## How does VirtIO work in VMs?

1. The host hypervisor (for example, QEMU/KVM) exposes VirtIO backend devices.
2. The guest OS loads VirtIO frontend drivers such as `virtio_net`or `virtio_blk` that communicate using the VirtIO protocol.
3. I/O uses shared memory `virtqueues`, which avoids full device emulation.
4. Devices are exposed over the PCI or MMIO bus to the guest.

For example, instead of emulating an Intel e1000 NIC, the host exposes a `virtio-net` interface. The guest OS uses the `virtio-net` driver to exchange packets through shared buffers.

## Key takeaways

- VirtIO provides fast I/O through paravirtualization, not hardware emulation.
- Shared queues reduce overhead and context switching.
- It is the simplest and most common first step for device attach in Realms.

## Next steps

In the next section, you'll learn how bounce buffers make VirtIO safe for Realms. 
