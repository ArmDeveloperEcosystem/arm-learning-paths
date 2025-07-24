---
title: Implement safety-critical isolation using safety island architecture
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## How safety islands support functional safety in software systems

In automotive systems, a non-safety ECU (Electronic Control Unit) typically runs non-critical tasks such as infotainment or navigation. 

A safety island, by contrast, is dedicated to executing safety-critical control logic (for example, braking and steering) with strong isolation, redundancy, and determinism.

The table below compares the characteristics of an ECU and a safety island in terms of their role in supporting functional safety.

| Feature               | ECU                | Safety island                        |
|------------------------|----------------------------|--------------------------------------|
| Purpose               | Comfort/non-safety logic | Safety-critical decision making      |
| OS/runtime            | Linux, Android             | RTOS, hypervisor, or bare-metal      |
| Isolation             | Soft partitioning          | Hardware-enforced isolation   |
| Functional safety requirement | None to moderate           | ISO 26262 ASIL-B to ASIL-D compliant |
| Fault handling        | Best-effort recovery       | Deterministic safe-state response    |

This comparison shows why safety-critical software depends on dedicated hardware domains to meet functional safety goals.

If the main processor fails or becomes inoperable, a safety island can take over critical safety functions such as deceleration, stopping, and fault handling to prevent catastrophic system failures.

{{% notice Tip %}}
Safety islands are often implemented as lockstep cores or separate MCUs that run on real-time operating systems (RTOS), offering guaranteed performance under fault conditions.
{{% /notice %}}

## Key capabilities of a safety island
- **System health monitoring** continuously monitors the operational status of the main processor (for example, the ADAS control unit) and detects potential errors or anomalies
- **Fault detection and isolation** independently detects failures and initiates emergency handling for overheating, execution faults, or unresponsiveness
- **Essential safety functions conitnue to operate**, even if the main system crashes. A safety island can execute fallback operations, such as:
   - Autonomous Vehicles → safe stopping (fail-safe mode)
   - Industrial Equipment → emergency power cutoff or speed reduction

## Why a safety island matters for functional safety

A safety island helps systems respond to high-risk scenarios and reduces the likelihood of catastrophic failures.

- **Acts as an independent redundant safety layer**  
   - Operates safety logic independently of the main processor

- **Supports ASIL-D safety level**  
   - Enables the system to meet the highest ISO 26262 requirements for critical operations

- **Provides independent fault detection and recovery mechanisms**  
  - *Fail-safe*: activates a minimal-risk mode, such as limiting vehicle speed or switching to manual control 
  - *Fail-operational*: allows high-integrity systems, such as those in aerospace or autonomous driving, to continue functioning under fault conditions

Safety islands play a key role in enabling ISO 26262 compliance by isolating safety-critical logic from general-purpose processing. They're a proven solution for improving system determinism, fault tolerance, and fallback behavior.