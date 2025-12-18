---
title: "Overview"
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Deploying Veraison on AWS
[Veraison](https://github.com/veraison) is a community open-source project that is part of the [Confidential Computing Consortium (CCC)](https://confidentialcomputing.io). Veraison provides components for building attestation verification services for confidential computing and other use cases. 

Veraison acts as the Verifier role in the [RATS architecture (RFC9334)](https://datatracker.ietf.org/doc/rfc9334/), which is a common model for attestation-based systems. Veraison makes use of community standardization efforts to ensure a high degree of interoperability.

Attestation is essential for confidential computing, and Veraison acts as a verifier for Arm's Confidential Compute Architecture (CCA). 

{{% notice Learning Tip %}}
If you're new to CCA attestation and Veraison, you will benefit from first completing the Learning Paths [Get Started with CCA Attestation and Veraison](/learning-paths/servers-and-cloud-computing/cca-veraison/) and [Run an end-to-end Attestation Flow with Arm CCA](/learning-paths/servers-and-cloud-computing/cca-essentials/). These two Learning Paths above use a Veraison verification service hosted by [Linaro](https://www.linaro.org).
{{% /notice %}}

In this Learning Path, you'll create and deploy your own Veraison verification service on AWS. After completing this Learning Path, you'll be able to revisit the two Learning Paths mentioned above, using your own AWS-hosted Veraison service instead of the one hosted by Linaro.

{{% notice Note%}}
AWS isn't the only deployment option for Veraison, but you'll use it here as an example of deploying on public cloud infrastructure. For other deployment methods, see the [Veraison project README](https://github.com/veraison/services?tab=readme-ov-file#services).
{{% /notice %}}