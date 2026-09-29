---
title: Understand the sandbox architecture
description: Review how the runner creates a dedicated Firecracker microVM boundary for each generated-code execution.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What a microVM is

A microVM is a virtual machine (VM) designed to start quickly and run with a small device and memory footprint. Similar to a general-purpose VM, a microVM runs its own guest kernel. The VM monitor and kernel-based VM (KVM) use hardware virtualization to isolate that guest from the host.

MicroVMs remove devices and firmware that cloud workloads usually don't need. Instead of emulating a complete physical computer, a microVM commonly exposes only a virtual CPU, memory, storage, and network interface. The smaller device model reduces startup overhead and the amount of virtualization code exposed to the guest.

Firecracker is a VM monitor (VMM) built for microVM workloads. On Linux, Firecracker uses KVM to access the processor's hardware virtualization features. KVM runs guest CPU instructions, while Firecracker configures the virtual CPUs, memory, and minimal set of devices presented to the guest.

The isolation models differ in an important way:

| Environment | Kernel model | Typical use |
| --- | --- | --- |
| Container | Workloads share the host kernel | Package and deploy trusted applications efficiently |
| General-purpose VM | Each VM has a guest kernel and a broad virtual hardware model | Run complete operating systems and long-lived services |
| Firecracker microVM | Each microVM has a guest kernel and a minimal virtual hardware model | Run short-lived, isolated cloud workloads with low overhead |

A microVM doesn't make arbitrary code safe by itself. You still need the following:

- Host hardening
- Resource limits
- Network policy
- A clean guest image
- Lifecycle controls

The microVM provides the central kernel boundary around which you build those controls.

## Why you should isolate generated code

AI coding agents can create and run programs while they work on a task. Generated code can contain mistakes, consume excessive resources, modify unexpected files, or attempt network access. Running the code directly on the agent host gives it access to the host's kernel and any resources available to the agent process.

Each Firecracker microVM has its own guest kernel and root filesystem. This creates a stronger boundary than running generated code as another process on the host.

You can use an AI coding agent to run each generated program in a fresh microVM that acts as an ephemeral sandbox. To understand that execution flow, you'll build a small runner and run `hello-arm.sh`, a supplied Bash program that reports the guest's Arm architecture and system information.

You'll see how the runner starts the microVM, executes the program, collects results, and discards the guest filesystem. Future Learning Paths will cover connecting an AI coding agent to the sandbox. For this Learning Path, you don't need a model, an API key, or an AI framework.

The runner follows this lifecycle:

1. Copy a clean base root filesystem to a job-specific directory.
2. Create a private TAP network interface: a virtual Ethernet device that connects the host to the guest.
3. Start a Firecracker microVM with fixed CPU and memory allocations.
4. Copy one shell program into the guest and run it as the `ubuntu` user.
5. Save standard output, standard error, serial logs, and result metadata on the host.
6. Stop Firecracker and delete the writable guest disk and network interface.

The example runs one job at a time. The private `172.16.0.0/30` network provides two usable addresses: `172.16.0.1` for the host and `172.16.0.2` for the guest. An exclusive host lock prevents two runners using the same runtime directory from starting together.

## Understand the example boundary

The runner demonstrates the following controls:

| Resource | Control |
| --- | --- |
| Kernel | Each job runs with a dedicated guest kernel through KVM |
| CPU | Firecracker configures one virtual CPU by default |
| Memory | Firecracker configures 512 MiB by default |
| Time | GNU `timeout` limits the host-side SSH execution to 15 seconds |
| Filesystem | Each job receives a new writable copy of the base root filesystem |
| Network | IPv4 firewall rules drop forwarded guest traffic and new guest-initiated connections to host services |
| Results | Only output, metadata, and the Firecracker serial log remain on the host |

The running microVM doesn't receive host filesystem mounts or the host's SSH private key. The base root filesystem contains the public key that the runner uses to connect. The `ubuntu` guest user has passwordless `sudo`, so a job can become root inside its microVM. The guest account isn't an additional isolation boundary.


{{% notice Note %}}
Use the provided sample programs on a dedicated test host while exploring this educational sandbox. The runner starts Firecracker as host root without `jailer`. Before accepting untrusted generated code, add the production controls described in the final section.
{{% /notice %}}

## What you've learned and what's next

You've learned how microVMs combine a dedicated guest kernel with a minimal virtual hardware model. You've also reviewed the per-job lifecycle and boundaries enforced by the example.

Next, you'll confirm KVM access on your Arm Linux machine, install Firecracker, and prepare a reusable Arm guest image.
