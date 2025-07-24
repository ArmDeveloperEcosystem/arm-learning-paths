---
title: Functional safety for automotive software development
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## The software development lifecycle

Functional safety affects both hardware and software development, particularly in areas such as requirement changes, version control, and test validation. For example, in ASIL-D level applications, every code change must go through a full impact analysis and regression testing to ensure it doesn't introduce new risks.

## Software development practices for functional safety

These practices ensure that software meets industry standards and can withstand system-level failures:
- **Defining requirements clearly**  
  - Specifying safety-critical requirements and conduct formal risk assessments.

- **Following safety-oriented programming standards**  
  - Using MISRA C or CERT C/C++ and static analysis tools to detect unsafe behavior.

- **Implementing fault-handling mechanisms**  
  - Using redundancy, health monitoring, and fail-safe logic to manage faults gracefully.

- **Testing and verifying rigorously**  
  - Using Hardware-in-the-Loop (HIL) testing to validate behavior under realistic conditions.

- **Tracking changes with version control and audits**  
  - Using tools like Git, JIRA, or Polarion to manage revisions and maintain traceability for audits.

- **Building an ASIL-partitioned development environment and adopting SOAFEE technologies** to help improve software maintainability and ensure consistent compliance with functional safety standards.

{{% notice Note %}}
This Learning Path builds on [Deploy Open AD Kit containerized autonomous driving simulation on Arm Neoverse](/learning-paths/automotive/openadkit1_container/). It introduces functional safety practices from the earliest stages of software development.
{{% /notice %}}
