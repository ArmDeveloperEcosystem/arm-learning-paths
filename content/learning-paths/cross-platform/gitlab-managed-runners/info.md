---
title: Build and use GitLab-hosted Arm runners for CI/CD
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is a GitLab runner?

A GitLab Runner is an agent that executes CI/CD jobs defined in your pipeline configuration. GitLab offers two types of runners:

- **GitLab-hosted runners**: GitLab manages these runners, so you don't need to set up or maintain infrastructure.
- **Self-managed runners**: you install and maintain these runners on your own infrastructure.

For Arm development, GitLab-hosted runners offer a managed way to build and test applications targeting Arm platforms without maintaining your own infrastructure. You'll choose between the Docker executor (for containerized builds) or the Shell executor (for direct access to the Arm64 runner environment).

When you register a runner, you specify an executor that determines the job environment. For Arm development workflows, Docker and Shell executors are the most common choices, letting you build container images or compile applications directly on native Arm64 hardware.

## Arm64 runner support

GitLab-hosted runners support both x86-64 and arm64 architectures. For developers targeting Arm platforms (servers, edge devices, or embedded systems), using Arm64 runners provides:

- Native compilation for Arm architecture without cross-compilation
- Consistent build environment matching deployment targets
- Access to Arm-specific instructions and optimizations
- Faster builds when targeting Arm64 platforms

{{% notice Note %}}
GitLab-hosted runner specifications are subject to change. See the [GitLab documentation](https://docs.gitlab.com/ci/runners/hosted_runners/) for further information.
{{% /notice %}}

## GitLab-hosted runners

### Execution environment

Each job runs in a newly provisioned virtual machine dedicated to that job. The VM is deleted immediately after job completion.

GitLab-hosted runners provide the following execution environment:

- Jobs run with sudo access (no password required)
- Jobs time out after three hours
- Storage is shared between the operating system, container images, and your repository clone
- Untagged jobs default to the small Linux x86-64 runner (specify `saas-linux-small-arm64` or another Arm64 tag to use Arm runners)


### Network isolation

- Outbound communication to the public internet is allowed
- Inbound communication from the public internet is blocked
- Communication between VMs is not permitted
- Only the runner manager can communicate with ephemeral VMs

### Available Arm64 runners

GitLab provides three tiers of Linux Arm64 runners:

- `saas-linux-small-arm64` (free tier)
- `saas-linux-medium-arm64` (paid tier)
- `saas-linux-large-arm64` (paid tier)

For complete specifications, see [GitLab-hosted runners](https://docs.gitlab.com/ci/runners/hosted_runners/linux/).

### VM lifecycle

Each job executes in complete isolation:

- GitLab provisions a new VM for your job
- The job executes in this dedicated environment
- GitLab sends deletion command to Google Compute API immediately after completion
- The [Google Compute Engine hypervisor](https://cloud.google.com/blog/products/gcp/7-ways-we-harden-our-kvm-hypervisor-at-google-cloud-security-in-plaintext) securely deletes the VM and data
