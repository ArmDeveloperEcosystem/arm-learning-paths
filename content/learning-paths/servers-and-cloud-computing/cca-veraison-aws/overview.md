---
title: "Overview: Deploying Veraison in AWS"
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview
[Veraison](https://github.com/veraison) is a community open-source project that is part of the [Confidential Computing Consortium (CCC)](https://confidentialcomputing.io). Veraison provides the components that are needed to build attestation verification services for confidential computing or other use cases. Veraison acts as the Verifier role in the [RATS architecture (RFC9334)](https://datatracker.ietf.org/doc/rfc9334/), which is a common model for attestation-based systems. Veraison makes use of community standardisation efforts to ensure a high degree of interoperability.

Attestation is essential for confidential computing, and Veraison can be used as the verifier service for Arm's Confidential Compute Architecture (CCA). If you have not already familiarised yourself with CCA attestation and Veraison, it is recommended that you first follow the learning paths [Get Started with CCA Attestation and Veraison](https://learn.arm.com/learning-paths/servers-and-cloud-computing/cca-veraison/) and [Run an end-to-end Attestation Flow with Arm CCA](https://learn.arm.com/learning-paths/servers-and-cloud-computing/cca-essentials/).

The two learning paths linked above make use of a Veraison verification service that is published and maintained by [Linaro](https://www.linaro.org).

In this learning path, you will create and publish your own Veraison verification service in the AWS cloud. After you complete the learning path, you will be able to go back through the steps of the previous two learning paths, and use your own AWS-hosted Veraison service instead of the one hosted by Linaro.

AWS is not the only way to deploy Veraison, but we will adopt it here as an example of using public cloud infrastructure. You can read about other types of deployment [in the Veraison project README](https://github.com/veraison/services?tab=readme-ov-file#services).
