---
title: CCA Attestation
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Confidential computing is about protecting data in use. This protection comes from the creation of a security boundary around the computation being performed. This security boundary creates what is normally called a Trusted Execution Environment (TEE). The data and code that executes within the TEE is protected from the outside world. Different technologies exist for creating this secure boundary. In the case of Arm CCA, the secure boundary is provided by the Realm Management Extensions (RME), which are part of the Arm Architecture v9 for A-profile CPUs.

A secure boundary is necessary for confidential computing, but it is not sufficient. There must also be a way to establish trust with the target compute environment that the boundary is protecting (the TEE). Trusting the environment implicitly does not meet the strict definition of confidential computing. Instead, trust needs to be built by a process that is both explicit and transparent. This process is known as attestation. The role of attestation is described in the figure below.

![Attestation role](./attestation-role.png)

All confidential computing architectures provide attestation as a means of building trust. The exact details of attestation vary from one type of platform to another. This learning path will help you to understand the common concepts, while also guiding you through a practical exercise that focuses on how attestation is performed with CCA.

At the heart of the CCA attestation process is a small, self-contained packet of data known as a CCA attestation token. CCA attestation tokens are produced by realms. They contain evidence about the booted state of the realm. They also contain evidence about the state of the CCA host platform on which the realm is running, including details about the hardware and firmware. You will learn more about this evidence later in the learning path.

CCA attestation tokens have two very important properties. The first is that they are cryptographically signed using a private key that is strongly protected by the platform where the realm is running. The second is that they can be evaluated remotely using an attestation verification service. The verification service acts as a trust authority. It can verify the token’s cryptographic signature, which ensures that the evidence is authentic. It can also compare the evidence against the expectations of a trustworthy platform. These two properties combine to allow a user of the realm to decide whether the realm will provide an adequate trusted environment for confidential computing.

In the rest of this learning path, you will download a file that contains an example of a CCA attestation token. You will then use command-line tools to inspect the contents of the token, and you will see how to use an attestation verifier service to verify and evaluate the token.

