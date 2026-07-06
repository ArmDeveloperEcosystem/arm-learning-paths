---
# User change
title: "Overview of Arm CCA BootSync and Boot Sync Blocks protocol"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Design overview

Arm CCA BootSync is a boot-time synchronization mechanism for Arm CCA Realms. It lets Realm guest firmware obtain configuration and secret data before the guest operating system is running. This matters because early firmware does not have a network stack, but workflows such as UEFI Secure Boot and encrypted disk boot still need trusted inputs during that early boot window.

The reference implementation uses the *Boot Sync Blocks* (BSB) protocol described by the Realm Host Interface (RHI) specification. In this Learning Path, you use BootSync to provide two kinds of data to a Realm:

- Variable data, such as UEFI variables used to configure Secure Boot.
- Secret data, such as a disk unlock passphrase or other boot-time secret.

The data is not just copied into the Realm. BootSync first establishes a protected exchange between the Realm guest firmware and a *User Context* service controlled by the Realm initiator. The User Context service runs outside the Realm, but it represents the party that decides whether the Realm should receive the requested boot information.

## Component roles

The BootSync flow spans both the Normal World host and the Realm World guest:

- The *Realm guest firmware* starts BootSync early in boot and requests boot information.
- The *Realm Management Monitor* (RMM) exposes Realm services and creates attestation reports for the Realm.
- The *Virtual Machine Manager* (VMM), `lkvm-bootsync` in this Learning Path, forwards Realm Host Interface calls between the Realm and host user space.
- The *User Context* service receives BootSync requests, verifies attestation evidence, and returns encrypted boot information when the Realm is allowed to receive it.

The practical result is that the Realm firmware can get boot-time data without needing direct networking. The host can carry the request, but the release decision belongs to the User Context after the Realm has provided attestation evidence.

## BootSync protocol stages

The BSB protocol has three logical stages:

1. Key exchange establishes a secure session between the Realm guest firmware and the User Context service. The reference implementation uses ECDH over the P-384 curve, derives keys with HKDF-SHA512, and encrypts protocol data with AES-GCM.
2. Attestation lets the Realm guest firmware request an attestation report from the RMM. The binding key from the secure session is used as challenge data, so the User Context can bind the attestation evidence to this BootSync exchange.
3. Boot Information Blocks release the requested boot data after attestation succeeds. In this Learning Path, those blocks are represented by files whose names begin with the Realm Personalization Value (RPV), such as `ARMCCA01_VAR.dat` and `ARMCCA01_SEC.dat`.

The RPV is important because one User Context service can support multiple Realms. A Realm launched with `--realm-pv ARMCCA01` requests files that start with `ARMCCA01`. If the matching files are missing, BootSync can establish a session and complete attestation, but it cannot provide the requested boot information.

## What you will validate

The exercises intentionally show both failure and success cases:

- First, you launch a Realm without the variable data file. This demonstrates that the firmware can ask for BootSync data and that the User Context reports a missing `ARMCCA01_VAR.dat` file.
- Next, you add the variable data file. BootSync completes, UEFI Secure Boot is enabled, and the unsigned kernel is rejected.
- Then, you sign the Realm kernel. The Realm boots with UEFI Secure Boot enabled, and the Secure Boot UEFI variable reports `1`.
- Finally, you encrypt the Realm root file system and use BootSync secret data to provide the unlock passphrase during boot.

For more detail, see the [ArmCcaBootSync README](https://gitlab.arm.com/linux-arm/edk2-cca/-/blob/cca/4441_measured_boot_v1/ArmVirtPkg/ArmCcaBootSync/Readme.md), the [Realm Management Monitor specification](https://developer.arm.com/documentation/den0137/latest/), and the [Realm Host Interface specification](https://developer.arm.com/documentation/den0148/latest/).

In the next section, you will launch Realms and see how Arm CCA BootSync can inject UEFI variables and secret data during early boot.
