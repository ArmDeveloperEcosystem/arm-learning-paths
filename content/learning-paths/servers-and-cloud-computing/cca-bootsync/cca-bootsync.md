---
# User change
title: Understand Arm CCA BootSync and the Boot Injection Protocol

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## What Arm CCA BootSync is

Arm Confidential Compute Architecture (CCA) BootSync is a boot-time synchronization mechanism for Arm CCA Realms. The mechanism lets Realm guest firmware obtain configuration and secret data before the guest operating system is running. This matters because early firmware doesn't have a network stack, but workflows such as UEFI Secure Boot and encrypted disk boot still need trusted inputs during that early boot window.

The reference implementation uses the *Boot Injection protocol*. The Boot Injection appendix of the [Realm Host Interface (RHI) specification](https://developer.arm.com/documentation/den0148/latest/) refers to the protocol as the BIB protocol. 

You'll use BootSync to provide two kinds of data to a Realm:

- Variable data, such as UEFI variables used to configure Secure Boot.
- Secret data, such as a disk unlock passphrase or other boot-time secret.

Before data is copied into the Realm, BootSync establishes a protected exchange between the Realm guest firmware and a *User Context* service controlled by the Realm initiator. The User Context service runs outside the Realm, but it decides whether the Realm should receive the requested boot information.

## Components of the BootSync flow

The BootSync flow spans both the Normal World host and the Realm World guest:

- The *Realm guest firmware* starts BootSync early in boot and requests boot information.
- The *Realm Management Monitor* (RMM) exposes Realm services and creates attestation reports for the Realm.
- The *Virtual Machine Manager* (VMM), in this case `lkvm-bootsync`, forwards Realm Host Interface calls between the Realm and host user space.
- The *User Context* service receives BootSync requests, verifies attestation evidence, and returns encrypted boot information when the Realm is allowed to receive it.

The practical result is that the Realm firmware can get boot-time data without needing direct networking. The host can carry the request, but the release decision belongs to the User Context after the Realm has provided attestation evidence.

## Stages of the Boot Injection protocol

The Boot Injection protocol has three logical stages:

1. Key exchange establishes a secure session between the Realm guest firmware and the User Context service. The reference implementation uses ECDH over the P-384 curve, derives keys with HKDF-SHA512, and encrypts protocol data with AES-GCM.
2. Attestation lets the Realm guest firmware request an attestation report from the RMM. The binding key from the secure session is used as challenge data, so the User Context can bind the attestation evidence to this BootSync exchange.
3. Boot Information Blocks carry the requested boot data after attestation succeeds.

## What you will validate

You'll validate both failure and success cases:

- First, you'll launch a Realm without injecting any boot data to see that the firmware can run successful attestation and ask for BootSync data.
- Next, you'll add the variable data file. BootSync completes, UEFI Secure Boot is enabled, and the unsigned kernel is rejected.
- Then, you'll sign the Realm kernel. The Realm boots with UEFI Secure Boot enabled, and the Secure Boot UEFI variable reports `1`.
- Finally, you'll encrypt the Realm root file system and use BootSync secret data to provide the unlock passphrase during boot.

## What you've learned and what's next

You’ve learned how Arm CCA BootSync uses key exchange, attestation, and Boot Information Blocks to provide trusted data during Realm boot.

Next, you'll launch Realms and see how Arm CCA BootSync can inject UEFI variables and secret data during early boot.
