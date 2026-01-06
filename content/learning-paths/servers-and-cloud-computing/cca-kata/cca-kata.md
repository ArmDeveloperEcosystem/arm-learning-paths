---
# User change
title: "Overview of Confidential Containers and Arm CCA Attestation with Trustee"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---


## Confidential Containers

["Confidential Containers"](https://github.com/confidential-containers/confidential-containers) is an open-source community
project focused on enabling cloud native confidential computing by leveraging Trusted Execution Environments (TEEs) to protect container workloads and the data they process.

## Design overview

Confidential computing systems are typically defined by what runs inside the Trusted Execution Environment (TEE) and what remains outside of it.
In the Confidential Containers architecture, the TEE contains:
  * The workload pod
  * Helper processes and daemons required to support the workload pod.
Everything else outside of the TEE, including the hypervisor, other pods, and the control plane, is considered untrusted. This trust boundary is fundamental to how Confidential Containers protect workload confidentiality.

### Kata Containers

Confidential Containers and [Kata Containers](https://github.com/kata-containers/kata-containers) are closely related, although the distinction between them is not always immediately clear. Kata Containers is an established open-source project that runs Kubernetes pods inside lightweight virtual machines. These VMs can, in turn, be executed within a TEE. In this Learning Path, the guest virtual machine is run inside an Arm CCA Realm, which you will later verify by inspecting kernel messages inside the guest.

This VM-based isolation model aligns well with the pod-centric design of Confidential Containers. However, while Kata Containers provide strong isolation, additional functionality is required to preserve confidentiality when the host environment is untrusted. These extensions are provided by the Confidential Containers project.

### Image Pulling

In a standard Kata Containers deployment, container images are pulled on the worker node using a CRI runtime such as containerd. The images are then exposed to the guest VM via filesystem passthrough. This approach is not suitable for confidential workloads because container images are visible to the untrusted host. Confidential Containers address this limitation by pulling and unpacking container images inside the guest VM.
To enable this, additional components such as **image-rs** are included in the guest root filesystem. These components go beyond traditional Kata deployments and are maintained in the Confidential Containers ["guest components"](https://github.com/confidential-containers/guest-components) repository.

On the host side, a **nydus snapshotter** intercepts the image pull process and redirects control to **image-rs** running inside the guest.
The diagram below illustrates the interaction between **containerd**, the **nydus snapshotter**, and **image-rs**.
![Image pulling alt-text#center](image_pulling.png "Image pulling")

### Attestation

Confidential Containers also include components that enable attestation, which is a core requirement for confidential computing.
Many guest operations depend on attestation. For example, before an encrypted container image can be unpacked, the guest must prove its identity and integrity in order to retrieve the decryption key.
Inside the guest the Confidential Data Hub (CDH) and Attestation Agent (AA) manage attestation flows and secret handling.
Like image pulling components, these services extend beyond traditional Kata deployments and are part of the Confidential Containers ["guest components"](https://github.com/confidential-containers/guest-components) repository.

The CDH and AA communicate with an external trusted service using the Key Broker Service (KBS) protocol.
Confidential Containers provide [Trustee](https://github.com/confidential-containers/trustee) as an attestation service and key management engine that:
   * Verifies the guest Trusted Computing Base (TCB)
   * Evaluates attestation evidence
   * Releases secrets only when policy requirements are met

The diagram below shows a simplified view of the attestation flow.
![Attestation alt-text#center](attestation.png "Attestation")

In this Learning Path, attestation is used to obtain the encryption key required to decrypt a container image.
Learn more about how Trustee services are used to evaluate the trustworthiness of a CCA Realm and how attestation policy gates secrets release in the
["Run an end-to-end Attestation with Arm CCA and Trustee"](/learning-paths/servers-and-cloud-computing/cca-trustee) Learning Path.

### Full Architecture Overview

By combining, Kata Containers, Guest-side image pulling and attestation and secret management, you arrive at the complete Confidential Containers architecture shown below:

![Confidential Containers alt-text#center](confidential_containers.png "Confidential Containers")


For convenience, both the Confidential Containers software stack and Trustee services are packaged as Docker containers. These can be run on any suitable AArch64 or x86_64 development host.
Because the confidential workload itself runs inside an Arm CCA Realm, this Learning Path uses the Arm Fixed Virtual Platform (FVP) along with the Arm CCA reference software stack to provide the required environment.

Proceed to the next section to run a confidential container using the components and architecture described here.
