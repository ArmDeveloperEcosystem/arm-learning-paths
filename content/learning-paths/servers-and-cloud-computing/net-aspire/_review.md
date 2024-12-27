---
review:
    - questions:
        question: >
            Which command do you use to install the Aspire workload on an Arm-powered VM?
        answers:
            - sudo apt install aspire.
            - dotnet workload install aspire.
            - dotnet install aspire --arm64.
        correct_answer: 2
        explanation: >
            The correct command to install the Aspire workload is `dotnet workload install aspire`, as it uses the .NET CLI to manage workloads.

    - questions:
        question: >
            When creating an AWS EC2 instance, which step ensures secure remote access to the VM?
        answers:
            - Creating a new key pair in the "Key pair (login)" section.
            - Selecting the appropriate security group for the instance.
            - Allowing HTTP and HTTPS traffic in the network settings.
        correct_answer: 1
        explanation: >
            Creating a new key pair in the "Key pair (login)" section generates a private key file that is essential for secure SSH access to the EC2 instance.

    - questions:
        question: >
            In Google Cloud Platform, which series should you select to use an Arm64 processor for your VM?
        answers:
            - T2A (Ampere Altra Arm).
            - E2 (General Purpose).
            - N2D (Compute Optimized).
        correct_answer: 1
        explanation: >
            The T2A series (Ampere Altra Arm) is designed specifically for Arm64 processors and provides cost-effective, high-performance computing in the Google Cloud Platform.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
