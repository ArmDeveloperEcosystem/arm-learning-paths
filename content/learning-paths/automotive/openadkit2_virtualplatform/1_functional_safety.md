---
title: Functional Safety for automotive software development
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is Functional Safety?

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

Three of core objectives of Functional Safety are:
1. **Prevention**  
   - Reducing the likelihood of errors through rigorous software development processes and testing. In the electric vehicle, the battery systems monitor temperature to prevent overheating.
2. **Detection**  
   - Quickly identifying errors using built-in diagnostic mechanisms (e.g., Built-in Self-Test, BIST). 
3. **Mitigation**  
   - Controlling the impact of failures to ensure the overall safety of the system.

This approach is critical in applications such as **autonomous driving, flight control, and medical implants**, where failures can result in **severe consequences**.

### ISO 26262 Standard and Applications

[ISO 26262](https://www.iso.org/standard/68383.html) is a functional safety standard specifically for **automotive electronics and software systems**. It defines a comprehensive safety lifecycle, covering all phases from **requirement analysis, design, development, testing, to maintenance**.

Key Concepts of ISO 26262:
- **ASIL (Automotive Safety Integrity Level)**  
  - Evaluates the risk level of different system components (A, B, C, D, where **D represents the highest safety requirement**). 
  - For example: ASIL A can be Dashboard light failure (low risk) and ASIL D is Brake system failure (high risk).
  https://en.wikipedia.org/wiki/Automotive_Safety_Integrity_Level
- **HARA (Hazard Analysis and Risk Assessment)**  
  - Analyzes hazards and assesses risks to determine necessary safety measures.
- **Safety Mechanisms**  
  - Includes error detection, fault tolerance, and fail-safe modes to ensure safe operation.

List some of typical application scenarios:
- **Autonomous Driving Systems**: 
  - Ensures that even if sensors (e.g., LiDAR, radar, cameras) provide faulty data, the vehicle will not make dangerous decisions.
- **Powertrain Control**: 
  - Prevents braking system failures that could lead to loss of control.
- **Battery Management System (BMS)**: 
  - Prevents battery overheating or excessive discharge in electric vehicles.

For more details, you can check this video: [What is Functional Safety?](https://www.youtube.com/watch?v=R0CPzfYHdpQ)


### Safety Island

**Safety Island** is an independent safety subsystem separate from the main processor. It is responsible for monitoring and managing system safety. If the main processor fails or becomes inoperable, Safety Island can take over critical safety functions such as **deceleration, stopping, and fault handling** to prevent catastrophic system failures.

Key Functions of Safety Island
- **Monitoring System Health**  
   - Continuously monitors the operational status of the main processor (e.g., ADAS control unit, ECU) and detects potential errors or anomalies.
- **Fault Detection and Isolation**  
   - Independently evaluates and initiates emergency handling if the main processing unit encounters errors, overheating, computational failures, or unresponsiveness.
- **Providing Essential Safety Functions**  
   - Even if the main system crashes, Safety Island can still execute minimal safety operations, such as:
   - Autonomous Vehicles → Safe stopping (Fail-Safe Mode)
   - Industrial Equipment → Emergency power cutoff or speed reduction


### Integration of Safety Island and Functional Safety

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


### Impact of Functional Safety on Software Development Processes

Functional Safety impacts **both hardware and software development**, particularly in areas such as requirement changes, version management, and testing validation.  
For example, in ASIL-D level applications, every code modification requires a complete impact analysis and regression testing to ensure that new changes do not introduce additional risks.

List the Functional Safety Requirements in Software Development:
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

This learning path builds on the previous [learning path](https://learn.arm.com/learning-paths/automotive/openadkit1_container) and introduces how to incorporate Functional Safety design processes in the early stages of automotive software development.
By establishing an ASIL Partitioning software development environment and leveraging [**SOAFEE**](https://www.soafee.io/) technologies, developers can enhance software consistency and maintainability in Functional Safety applications.

