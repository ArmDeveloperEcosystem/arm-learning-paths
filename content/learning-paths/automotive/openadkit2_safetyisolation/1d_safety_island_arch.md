---
title: Implement safety-critical isolation with Safety Island architecture
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Isolate safety-critical logic using a Safety Island

In automotive systems, a general ECU (Electronic Control Unit) typically runs non-critical tasks such as infotainment or navigation. 

A Safety Island, by contrast, is dedicated to executing safety-critical control logic (for example, braking and steering) with strong isolation, redundancy, and determinism.

The table below compares the characteristics of a general ECU and a Safety Island in terms of their role in supporting functional safety.

| Feature               | General ECU                | Safety Island                        |
|------------------------|----------------------------|--------------------------------------|
| Purpose               | Comfort/non-safety logic | Safety-critical decision making      |
| OS/runtime            | Linux, Android             | RTOS, hypervisor, or bare-metal      |
| Isolation             | Soft partitioning          | Hardware-enforced isolation   |
| Functional safety req | None to moderate           | ISO 26262 ASIL-B to ASIL-D compliant |
| Fault handling        | Best-effort recovery       | Deterministic safe-state response    |

{{% notice Tip %}}
Safety Islands are often implemented as lockstep cores or separate MCUs that run on real-time operating systems (RTOS), offering guaranteed performance under fault conditions.
{{% /notice %}}

This contrast highlights why safety-focused software needs a dedicated hardware domain with certified execution behavior.

If the main processor fails or becomes inoperable, Safety Island can take over critical safety functions such as deceleration, stopping, and fault handling to prevent catastrophic system failures.

## Key capabilities of Safety Island
- **System health monitoring**  
   - Continuously monitors the operational status of the main processor (for example, the ADAS control unit) and detects potential errors or anomalies.
- **Fault detection and isolation**
   -   Independently detects failures and initiates emergency handling for overheating, execution faults, or unresponsiveness.
- **Provides essential safety functions**, even if the main system crashes, the Safety Island still executes minimal safety operations, such as:
   - Autonomous Vehicles → safe stopping (fail-safe mode)
   - Industrial Equipment → emergency power cutoff or speed reduction

## Why Safety Island matters for functional safety

Safety Island helps systems respond to high-risk scenarios and reduces the likelihood of catastrophic failures.

- **Acts as an independent redundant safety layer**  
   - Operates safety logic independently of the main processor

- **Supports ASIL-D safety level**  
   - Enables the system to meet the highest ISO 26262 requirements for critical operations

- **Provides independent fault detection and recovery mechanisms**  
  - *Fail-safe*: activates a minimal-risk mode, such as limiting vehicle speed or switching to manual control 
  - *Fail-operational*: allows high-integrity systems, such as those in aerospace or autonomous driving, to continue functioning under fault conditions
