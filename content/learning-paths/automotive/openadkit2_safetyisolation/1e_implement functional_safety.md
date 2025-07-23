---
title: Functional safety for automotive software development
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## The software development lifecycle

Functional Safety affects both hardware and software development, particularly in areas such as requirement changes, version control, and test validation. For example, in ASIL-D level applications, every code change must go through a full impact analysis and regression testing to ensure it doesn't introduce new risks.

## Software development practices for functional safety

These practices ensure that software meets industry standards and can withstand system-level failures:
- **Define requirements clearly**  
  - Specify safety-critical requirements and conduct formal risk assessments.

- **Follow safety-oriented programming standards**  
  - Use MISRA C or CERT C/C++ and static analysis tools to detect unsafe behavior.

- **Implement fault-handling mechanisms**  
  - Use redundancy, health monitoring, and fail-safe logic to manage faults gracefully.

- **Test and verify rigorously**  
  - Use Hardware-in-the-Loop (HIL) testing to validate behavior under realistic conditions.

- **Track changes with version control and audits**  
  - Use tools like Git, JIRA, or Polarion to manage revisions and maintain traceability for audits.

Building an ASIL-partitioned development environment and adopting SOAFEE technologies can help improve software maintainability and ensure consistent compliance with functional safety standards.

{{% notice Note %}}
This Learning Path builds on [Deploy Open AD Kit containerized autonomous driving simulation on Arm Neoverse](/learning-paths/automotive/openadkit1_container/). It introduces functional safety practices from the earliest stages of software development.
{{% /notice %}}
