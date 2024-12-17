---
# User change
title: "Overview of the Software Architecture"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Overview 
In this learning path you will learn how attestation can control the release of confidential data into a confidential Linux realm for processing.

The role of attestation is to assess whether the target compute environment (the Linux realm, in this case) offers a provable level of confidential isolation. This assessment needs to occur before the realm can be trusted to receive confidential data or algorithms. This use of attestation to judge the trustworthiness of a compute environment, before allowing it to do any processing, is a common pattern in confidential computing. Here, you will learn about this pattern using a minimal set of software components.

## Understanding the key software components 
In this learning path, you will make use of a key broker service, or KBS. The role of the KBS is to be a repository for encryption keys or other confidential data resources. A KBS will release such secrets for processing in a confidential computing environment, but only when that environment has proved itself trustworthy through attestation.

The workload that runs inside the realm is a client of the KBS. It calls the KBS to request a secret. The KBS will not return the secret immediately. Instead, it will issue an attestation challenge back to the client. The client must respond with evidence in the form of a [CCA attestation token](/learning-paths/servers-and-cloud-computing/cca-container/cca-container/#obtain-a-cca-attestation-token-from-the-virtual-guest-in-a-realm).

When the KBS receives an attestation token from the realm, it needs to call a verification service that will check the token's cryptographic signature and verify that it denotes a confidential computing platform. As you saw in the [Introduction to CCA Attestation with Veraison learning path](/learning-paths/servers-and-cloud-computing/cca-veraison), Linaro provides such an attestation verifier for use with pre-silicon CCA platforms. This verifier is built from the open-source [Veraison project](https://github.com/veraison). The KBS calls this verifier to obtain an attestation result. The KBS can then use this result to decide whether to release the secrets into the realm for processing.

For additional security, the KBS does not release any secrets in clear text, even after a successful verification of the attestation token. Instead, the realm provides an additional public encryption key to the KBS. This is known as a wrapping key. The KBS will use this public key to encrypt(wrap) the secrets. The client workload inside the realm is then able to use its own private key to unwrap the secrets and use them.

In this learning path example, you will see the secret that is exchanged between the KBS and the realm is a small string value, which the realm will decrypt and echo to its console window once all the attestation steps have succeeded.

For convenience, both the KBS and the client software are packaged in docker containers, which you can execute on any suitable development machine (aarch64 or x86_64). Since the client software runs in a realm, it makes use of the Fixed Virtual Platform (FVP) and the reference software stack for Arm CCA. If you have not yet familiarised yourself with running applications in realms using FVP and the reference software stack, please refer to the [Run an application in a Realm using the Arm Confidential Computing Architecture (CCA)](/learning-paths/servers-and-cloud-computing/cca-container) learning path.

The attestation verification service is hosted by Linaro, so it will not be necessary for you to build or deploy this service yourself.

Shown in this figure below is the software architecture you will construct to run the attestation example in this learning path.

![cca-essentials](cca-essentials.png)

You can now proceed to the next section to run the end-to-end attestation example with the software components and architecture as described.
