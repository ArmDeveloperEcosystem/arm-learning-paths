---
title: Introduction to pqm4 and Post-Quantum Cryptography

weight: 2

layout: learningpathall
---

### Post-Quantum Cryptography

The [pqm4](https://github.com/mupq/pqm4) framework is a benchmarking and implementation suite for post-quantum cryptography (PQC) on Arm Cortex-M4 microcontrollers.  It originated from the [PQCRYPTO](https://pqcrypto.eu.org) project, funded by the European Commission, and has since evolved into a widely used platform for evaluating PQC in embedded environments.

As quantum computing advances, widely used cryptographic schemes such as RSA and elliptic curve cryptography are expected to become insecure. This presents a unique challenge for embedded systems, where devices often remain deployed for 10 to 20 years and must be designed with long-term security in mind.

Post-quantum cryptography is expected to play a critical role in securing a wide range of embedded applications, including secure firmware updates, device authentication, encrypted communication (e.g., IoT sensor-to-cloud), and integrity protection for edge AI models. These use cases require cryptographic mechanisms that remain secure over the lifetime of the device, even in the presence of future quantum adversaries.

To address this, new PQC algorithms have been standardized by NIST, including ML-KEM for key exchange and ML-DSA for digital signatures. However, these algorithms are significantly more demanding in terms of computation, memory, and code size compared to classical cryptography — making their deployment on constrained microcontrollers non-trivial.

The pqm4 framework provides a practical solution by enabling developers to evaluate PQC implementations under real embedded constraints. It offers standardized benchmarking for performance (cycle counts), memory usage (stack), and code size, along with optimized implementations tailored for the Cortex-M4 architecture. This allows developers to move beyond theoretical analysis and make informed decisions about deploying PQC in real-world embedded systems.


### Two Public-key Primitives

Two public-key primitives are particularly fundamental to modern cryptography: 
- key encapsulation mechanisms (KEMs) and 
- digital signature algorithms (DSAs). 

KEMs allow two parties to establish a shared secret over an insecure channel - the foundation for encrypted communications in protocols like TLS. Digital signatures provide authentication and integrity, ensuring that a message genuinely comes from its claimed sender and hasn't been tampered with. Together, these primitives underpin everything from secure web browsing to firmware updates on embedded devices.

Post-quantum cryptography replaces classical algorithms with new designs built on mathematical problems that remain hard even for quantum computers. Among the various primitives, KEMs and signatures are the most critical for most applications and have been the focus of NIST's standardization effort. KEMs have received particular urgency due to "harvest now, decrypt later" attacks - adversaries can record encrypted communications today and decrypt them once quantum computers become available.

This makes protecting data in transit an immediate priority, even though quantum computers may still be years away. Unlike classical public-key cryptography, which relies almost entirely on integer factorization and discrete logarithms, PQC draws on a variety of foundations: Lattices, hash functions, error-correcting codes, multivariate polynomials, and more. This diversity means that different PQC schemes come with very different performance characteristics and trade-offs.

In this learning path, we will focus on KEMs implementation on Cortex-M. 

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
