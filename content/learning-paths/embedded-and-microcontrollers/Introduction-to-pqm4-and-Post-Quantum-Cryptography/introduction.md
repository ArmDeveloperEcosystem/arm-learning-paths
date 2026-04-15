---
title: Introduction to pqm4 and Post-Quantum Cryptography

weight: 2

layout: learningpathall
---

The [pqm4](https://github.com/mupq/pqm4) library is a collection of post-quantum cryptographic algorithms designed for the ARM Cortex-M4 microcontrollers. It originated from the [PQCRYPTO](https://pqcrypto.eu.org) project, funded by the European Commission. The library includes implementations of post-quantum key-encapsulation mechanisms and signature schemes.

### Benefits of pqm4 for ARM Developers

- Efficient evaluation of post-quantum cryptographic algorithms on ARM Cortex-M4 microcontrollers.
- Accurate measurement of performance, memory usage, and execution cycles on real embedded hardware.
- Standardized framework for testing, benchmarking, and comparing multiple cryptographic implementations.
- Simplified integration and experimentation with new cryptographic schemes and optimizations for ARM platforms.

### Design Goals

The primary design goals of the pqm4 library are:

- Automated functional testing and test vector generation with validation against reference implementations.
- Comprehensive benchmarking, including speed, stack usage, and code size analysis.
- Profiling of cryptographic primitives such as SHA-2, SHA-3, and AES.
- Easy integration of clean and optimized implementations (e.g., from [PQClean](https://github.com/PQClean/PQClean)) and new schemes.

### Scope of pqm4

The pqm4 library includes schemes that are:

- Standardized by NIST in FIPS203, FIPS204, or FIPS205.
- Selected for standardization by NIST.
- Part of the 4th round of the NIST PQC standardization process.
- Part of the first round of additional signatures of the NIST PQC standardization process.
- Part of the second round of the KpqC competition.
