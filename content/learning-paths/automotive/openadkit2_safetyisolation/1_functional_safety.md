---
title: Functional Safety for automotive software development
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why Functional Safety Matters in Automotive Software

[Functional Safety](https://en.wikipedia.org/wiki/Functional_safety) refers to a system's ability to detect potential faults and respond appropriately to ensure that the system remains in a safe state, preventing harm to individuals or damage to equipment. 

This is particularly important in **automotive, autonomous driving, medical devices, industrial control, robotics and aerospace** applications, where system failures can lead to severe consequences.

In software development, Functional Safety focuses on minimizing risks through **software design, testing, and validation** to ensure that critical systems operate in a predictable, reliable, and verifiable manner. This means developers must consider:
- **Error detection mechanisms**
- **Exception handling**
- **Redundancy design**
- **Development processes compliant with safety standards**

### Definition and Importance of Functional Safety

The core of Functional Safety lies in **risk management**, which aims to reduce the impact of system failures.

In autonomous vehicles, Functional Safety ensures that if sensor data is incorrect, the system can enter a **safe state**, preventing incorrect driving decisions.

The three core objectives of Functional Safety are:
1. **Prevention**  
   - Reducing the likelihood of errors through rigorous software development processes and testing. In the electric vehicle, the battery systems monitor temperature to prevent overheating.
2. **Detection**  
   - Quickly identifying errors using built-in diagnostic mechanisms (e.g., Built-in Self-Test, BIST). 
3. **Mitigation**  
   - Controlling the impact of failures to ensure the overall safety of the system.

This approach is critical in applications such as **autonomous driving, flight control, and medical implants**, where failures can result in **severe consequences**.

### ISO 26262: Automotive Functional Safety Standard

[ISO 26262](https://www.iso.org/standard/68383.html) is a functional safety standard specifically for **automotive electronics and software systems**. It defines a comprehensive [V-model](https://en.wikipedia.org/wiki/V-model) aligned safety lifecycle, covering all phases from **requirement analysis, design, development, testing, to maintenance**.

Key Concepts of ISO 26262:
- **ASIL (Automotive Safety Integrity Level)**  
  - Evaluates the risk level of different system components (A, B, C, D, where **D represents the highest safety requirement**). 
  - For example: ASIL A can be Dashboard light failure (low risk) and ASIL D is Brake system failure (high risk).
  https://en.wikipedia.org/wiki/Automotive_Safety_Integrity_Level
- **HARA (Hazard Analysis and Risk Assessment)**  
  - Analyzes hazards and assesses risks to determine necessary safety measures.
- **Safety Mechanisms** 
  - Includes real-time error detection, system-level fault tolerance, and defined fail-safe or fail-operational fallback states. 

Typical Application Scenarios:
- **Autonomous Driving Systems**: 
  - Ensures that even if sensors (e.g., LiDAR, radar, cameras) provide faulty data, the vehicle will not make dangerous decisions.
- **Powertrain Control**: 
  - Prevents braking system failures that could lead to loss of control.
- **Battery Management System (BMS)**: 
  - Prevents battery overheating or excessive discharge in electric vehicles.

For more details, you can check this video: [What is Functional Safety?](https://www.youtube.com/watch?v=R0CPzfYHdpQ)


### Common Use Cases of Functional Safety in Automotive
- **Autonomous Driving**:
  - Ensures the vehicle can operate safely or enter a fail-safe state when sensors like LiDAR, radar, or cameras malfunction.
  - Functional Safety enables real-time fault detection and fallback logic to prevent unsafe driving decisions.

- **Powertrain Control**: 
  - Monitors throttle and brake signals to prevent unintended acceleration or braking loss. 
  - Includes redundancy, plausibility checks, and emergency overrides to maintain control under failure conditions.

- **Battery Management Systems (BMS)**: 
  - Protects EV batteries from overheating, overcharging, or deep discharge. 
  - Safety functions include temperature monitoring, voltage balancing, and relay cut-off mechanisms to prevent thermal runaway.

These use cases highlight the need for a dedicated architectural layer that can enforce Functional Safety principles with real-time guarantees.
A widely adopted approach in modern automotive platforms is the Safety Island—an isolated compute domain designed to execute critical control logic independently of the main system.

### Safety Island: Enabling Functional Safety in Autonomous Systems

In automotive systems, a **General ECU (Electronic Control Unit)** typically runs non-critical tasks such as infotainment or navigation, whereas a **Safety Island** is dedicated to executing safety-critical control logic (e.g., braking, steering) with strong isolation, redundancy, and determinism.

The table below compares the characteristics of a General ECU and a Safety Island in terms of their role in supporting Functional Safety.

| Feature               | General ECU                | Safety Island                        |
|------------------------|----------------------------|--------------------------------------|
| Purpose               | Comfort / non-safety logic | Safety-critical decision making      |
| OS/Runtime            | Linux, Android             | RTOS, Hypervisor, or bare-metal      |
| Isolation             | Soft partitioning          | Hard isolation (hardware-enforced)   |
| Functional Safety Req | None to moderate           | ISO 26262 ASIL-B to ASIL-D compliant |
| Fault Handling        | Best-effort recovery       | Deterministic safe-state response    |

This contrast highlights why safety-focused software needs a dedicated hardware domain with certified execution behavior.

**Safety Island** is an independent safety subsystem separate from the main processor. It is responsible for monitoring and managing system safety. If the main processor fails or becomes inoperable, Safety Island can take over critical safety functions such as **deceleration, stopping, and fault handling** to prevent catastrophic system failures.

Key Capabilities of Safety Island
- **System Health Monitoring**  
   - Continuously monitors the operational status of the main processor (e.g., ADAS control unit, ECU) and detects potential errors or anomalies.
- **Fault Detection and Isolation**  
   - Independently evaluates and initiates emergency handling if the main processing unit encounters errors, overheating, computational failures, or unresponsiveness.
- **Providing Essential Safety Functions**  
   - Even if the main system crashes, Safety Island can still execute minimal safety operations, such as:
   - Autonomous Vehicles → Safe stopping (Fail-Safe Mode)
   - Industrial Equipment → Emergency power cutoff or speed reduction


### Why Safety Island Matters for Functional Safety

Safety Island plays a critical role in Functional Safety by ensuring that the system can handle high-risk scenarios and minimize catastrophic failures.

How Safety Island Enhances Functional Safety
1. **Acts as an Independent Redundant Safety Layer**  
   - Even if the main system fails, it can still operate independently.
2. **Supports ASIL-D Safety Level**  
   - Monitors ECU health status and executes emergency safety strategies (e.g., emergency braking).
3. **Provides Independent Fault Detection and Recovery Mechanisms**  
   - **Fail-Safe**: Activates a **safe mode**, such as limiting vehicle speed or switching to manual control.
   - **Fail-Operational**: Ensures that high-safety applications (e.g., aerospace systems) can continue operating under certain conditions.

For more insights on **Arm's Functional Safety solutions**, you can refer to: [Arm Functional Safety Compute Blog](https://community.arm.com/arm-community-blogs/b/automotive-blog/posts/functional-safety-compute)


### Functional Safety in the Software Development Lifecycle

Functional Safety impacts **both hardware and software development**, particularly in areas such as requirement changes, version management, and testing validation.  
For example, in ASIL-D level applications, every code modification requires a complete impact analysis and regression testing to ensure that new changes do not introduce additional risks.

### Functional Safety Requirements in Software Development
These practices ensure the software development process meets industry safety standards and can withstand system-level failures:
- **Requirement Specification**  
   - Clearly defining **safety-critical requirements** and conducting risk assessments.
- **Safety-Oriented Programming**  
   - Following **MISRA C, CERT C/C++ standards** and using static analysis tools to detect errors.
- **Fault Handling Mechanisms**  
   - Implementing **redundancy design and health monitoring** to handle anomalies.
- **Testing and Verification**  
   - Using **Hardware-in-the-Loop (HIL)** testing to ensure software safety in real hardware environments.
- **Version Management and Change Control**  
   - Using **Git, JIRA, Polarion** to track changes for safety audits.

This learning path builds upon the previous containerized [learning path](https://learn.arm.com/learning-paths/automotive/openadkit1_container) guide and introduces Functional Safety design practices from the earliest development stages.

By establishing an ASIL Partitioning software development environment and leveraging [**SOAFEE**](https://www.soafee.io/) technologies, developers can enhance software consistency and maintainability in Functional Safety applications.
