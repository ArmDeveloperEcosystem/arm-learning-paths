---
title: Understand pqm4 and post-quantum cryptography
weight: 2
layout: learningpathall
---

## What pqm4 is

[pqm4](https://github.com/mupq/pqm4) is a benchmarking and implementation framework for post-quantum cryptography (PQC) on Arm Cortex-M4 microcontrollers. pqm4 provides optimized implementations of NIST-standardized algorithms and standardized benchmarks for cycle counts, stack usage, and code size. It also provides a test harness for validating implementations against known test vectors.

pqm4 originated from the [PQCRYPTO](https://pqcrypto.eu.org) project and has become the standard platform for evaluating PQC on constrained embedded hardware.

## Why post-quantum cryptography matters for embedded systems

Classical public-key schemes such as RSA and elliptic curve cryptography will become insecure after sufficiently powerful quantum computers exist. Embedded devices are particularly exposed because they often remain deployed for 10 to 20 years, which is longer than the expected timeline for quantum threats to mature.

NIST has standardized the following core PQC primitives to replace classical schemes:

- ML-KEM (FIPS 203): a key encapsulation mechanism (KEM) for establishing shared secrets, replacing ECDH in protocols such as TLS
- ML-DSA (FIPS 204): a digital signature algorithm for authentication and integrity, replacing ECDSA

These algorithms demand more computation, memory, and code size than their classical counterparts, making evaluating them on real Cortex-M4 hardware non-trivial. In this Learning Path, you'll focus on KEM implementations.

## What pqm4 provides

pqm4 is designed around four practical goals that make it useful for embedded PQC evaluation:

- Automated functional testing and test vector validation against reference implementations
- Benchmarking of speed, stack usage, and code size on real hardware
- Profiling of underlying primitives such as SHA-2, SHA-3, and AES
- Integration of implementations from [PQClean](https://github.com/PQClean/PQClean) and new schemes

## Supported pqm4 schemes

pqm4 includes schemes that are:

- Standardized by NIST in FIPS 203, FIPS 204, or FIPS 205
- Selected for standardization by NIST
- Part of the 4th round of the NIST PQC standardization process
- Part of the first round of additional signatures of the NIST PQC standardization process
- Part of the second round of the KpqC competition, a Korean national PQC standardization effort running in parallel to NIST

## What you've learned and what's next

You've now learned what pqm4 is, why post-quantum cryptography matters for long-lived embedded devices, and how pqm4 helps evaluate PQC implementations on Arm Cortex-M4 microcontrollers. You also reviewed the main NIST-standardized algorithms and the types of schemes included in the pqm4 framework.

Next, you'll set up the development environment needed to build and run pqm4 on your Cortex-M4 board or in QEMU.
