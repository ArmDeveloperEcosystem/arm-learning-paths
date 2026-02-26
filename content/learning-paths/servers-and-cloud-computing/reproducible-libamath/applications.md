---
title: Applications of Reproducibility
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Applications of Reproducibility


Reproducibility is not required for every application, but it is critical in several important domains. Here are some examples.

### Auto-vectorisation

Modern compilers automatically vectorise scalar loops when possible. This means that, depending on the compiler decisions, the same source code may be executed as a scalar loop, as a Neon vectorized loop or as a SVE vectorised loop.

Additionally, vectorised loops often include scalar tail handling for leftover elements that do not fill an entire vector.

Reproducibility across math routines garantees that:

* Vectorized loops (Neon or SVE) match regardless of which one is used

* The result of loops over scalar routines matches the results of vectorised loops (Neon or SVE)

* Changing vector width or enabling/disabling auto-vectorisation does not change the final output


### Distributed Computing

In distributed or parallel workloads, computations are often decomposed across multiple machines or execution units.

* Different nodes may execute scalar, Neon, or SVE code paths

* The decomposition of work can change between runs

* Without reproducible math routines, small numerical differences can accumulate and lead to divergent final results

### Embedded and real-time systems

In real-time environments, determinism is essential.

* Bitwise-identical results simplify validation

* Reproducibility ensures consistent behavior across software updates and hardware variants

* Debugging and fault analysis become significantly easier

### Gaming and simulation
Many games and simulations rely on deterministic numerical behavior.

* Reproducibility enables lockstep simulations across threads or devices

* It helps prevent desynchronization in multiplayer or replay systems

* Deterministic math simplifies testing and debugging of complex numerical code
