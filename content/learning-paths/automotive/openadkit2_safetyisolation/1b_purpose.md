---
title: Understand functional safety risks
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Manage risk with functional safety principles

At its core, functional safety is about managing risk and reducing the impact of system failures.

In autonomous vehicles, for example, functional safety ensures that if sensors produce unreliable or conflicting input, the vehicle can fall back to a known-safe state and maintain control.

The three core objectives of functional safety are:

- **Prevention** reduces the likelihood of errors through rigorous software development processes and testing. For example, electric vehicles monitor battery temperature to prevent overheating.
- **Detection** quickly identifies errors using built-in diagnostic mechanisms, such as self-test routines.
- **Mitigation** controls the impact of failures to ensure the system stays safe, even when something goes wrong.

In practice, these principles might be implemented through:

- Redundant sensor fusion code paths
- Timeout mechanisms for control loops
- Watchdog timers that reset components on fault detection
- Safe-state logic embedded in actuator control routines

Together, prevention, detection, and mitigation form the foundation for building safer, more reliable software systems.

In the next step, you’ll explore how functional safety principles are formalized through safety standards like ISO 26262 and applied to real-world systems.









