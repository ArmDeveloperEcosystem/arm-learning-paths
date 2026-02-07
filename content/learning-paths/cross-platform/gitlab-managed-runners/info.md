---
title: GitLab runners overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is a GitLab runner?

A GitLab Runner is an agent that executes CI/CD jobs defined in your pipeline configuration. GitLab offers two types:

- **GitLab-hosted runners**: Managed by GitLab, no setup required
- **Self-managed runners**: You install and manage on your own infrastructure

When you register a runner, you choose an executor that determines the job environment (Docker, Shell, Kubernetes, etc.).

### Arm64 runner support

GitLab-hosted runners support both x86-64 and arm64 architectures. For developers targeting Arm platforms (servers, edge devices, or embedded systems), using Arm64 runners provides:

- Native compilation for Arm architecture without cross-compilation
- Consistent build environment matching deployment targets
- Access to Arm-specific instructions and optimizations
- Faster builds when targeting Arm64 platforms

{{% notice Note %}}
GitLab-hosted runner specifications are subject to change. See the [GitLab documentation](https://docs.gitlab.com/ci/runners/hosted_runners/) for current details.
{{% /notice %}}

## GitLab-hosted runners

### Execution environment

Each job runs in a newly provisioned virtual machine dedicated to that job. The VM is deleted immediately after job completion.

- Untagged jobs default to the small Linux x86-64 runner
- Jobs time out after three hours
- The VM has sudo access without password
- Storage is shared between OS, container image, and repository clone

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

1. GitLab provisions a new VM for your job
2. The job executes in this dedicated environment
3. GitLab sends deletion command to Google Compute API immediately after completion
4. The [Google Compute Engine hypervisor](https://cloud.google.com/blog/products/gcp/7-ways-we-harden-our-kvm-hypervisor-at-google-cloud-security-in-plaintext) securely deletes the VM and data
