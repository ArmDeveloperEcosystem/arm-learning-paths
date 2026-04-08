---
title: Introduction to pqm4 and Post-Quantum Cryptography

weight: 2

layout: learningpathall
---

The [pqm4](https://github.com/mupq/pqm4) library is a collection of post-quantum cryptographic algorithms designed for the ARM Cortex-M4 microcontrollers. It originated from the [PQCRYPTO](https://pqcrypto.eu.org) project, funded by the European Commission. The library includes implementations of post-quantum key-encapsulation mechanisms and signature schemes.

### Design Goals

The primary design goals of the pqm4 library are:

- Automated functional testing on widely available development boards.
- Automated generation of test vectors and comparison against reference implementations.
- Automated benchmarking for speed, stack usage, and code size.
- Automated profiling of cycles spent in symmetric primitives like SHA-2, SHA-3, and AES.
- Integration of clean implementations from [PQClean](https://github.com/PQClean/PQClean).
- Easy integration of new schemes and implementations into the framework.

### Scope of pqm4

The pqm4 library includes schemes that are:

- Standardized by NIST in FIPS203, FIPS204, or FIPS205.
- Selected for standardization by NIST.
- Part of the 4th round of the NIST PQC standardization process.
- Part of the first round of additional signatures of the NIST PQC standardization process.
- Part of the second round of the KpqC competition.
