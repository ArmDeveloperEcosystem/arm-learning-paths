---
title: Functional safety for automotive software development
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Functional Safety in the Software Development Lifecycle

Functional Safety impacts both hardware and software development, particularly in areas such as requirement changes, version management, and testing validation.  
For example, in ASIL-D level applications, every code modification requires a complete impact analysis and regression testing to ensure that new changes do not introduce additional risks.

### Functional Safety Requirements in Software Development

These practices ensure the software development process meets industry safety standards and can withstand system-level failures:
- Requirement Specification
   - Clearly defining safety-critical requirements and conducting risk assessments.
- Safety-Oriented Programming
   - Following MISRA C, CERT C/C++ standards and using static analysis tools to detect errors.
- Fault Handling Mechanisms
   - Implementing redundancy design and health monitoring to handle anomalies.
- Testing and Verification  
   - Using Hardware-in-the-Loop (HIL) testing to ensure software safety in real hardware environments.
- Version Management and Change Control  
   - Using Git, JIRA, Polarion to track changes for safety audits.

By establishing an ASIL Partitioning software development environment and leveraging SOAFEE technologies, you can enhance software consistency and maintainability in Functional Safety applications.

This Learning Path follows [Deploy Open AD Kit containerized autonomous driving simulation on Arm Neoverse](/learning-paths/automotive/openadkit1_container/) and introduces Functional Safety design practices from the earliest development stages.