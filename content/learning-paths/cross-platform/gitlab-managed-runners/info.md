---
title: "Important Information"
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is a GitLab runner?
A GitLab Runner works with GitLab CI/CD to run jobs in a pipeline. It acts as an agent and executes the jobs you define in your GitLab CI/CD configuration. Some key points to note about GitLab Runner:

1. GitLab offers multiple types of runners - You can use GitLab-hosted runners, self-managed runners, or a combination of both. GitLab manages GitLab-hosted runners, while you install and manage self-managed runners on your own infrastructure.

2. Each runner is configured as an Executor - When you register a runner, you choose an executor, which determines the environment in which the job runs. Executors can be Docker, Shell, Kubernetes, etc.

3. Multi-architecture support: GitLab runners support multiple architectures including - **`x86/amd64`** and **`arm64`**.


{{% notice Note %}}
All The information provided in the next section are from GitLab official Pages and it's provided here for convenience and can be changed by Gitlab at anytime. Please refer to the [Gitlab Documentation](https://docs.gitlab.com/ci/runners/hosted_runners/) for more details and for the latest updates.
{{% /notice %}}

## GitLab-Hosted Runners Facts

1. Each of your jobs runs in a newly provisioned VM, which is dedicated to the specific job.

2. The storage is shared by the operating system, the container image with pre-installed software, and a copy of your cloned repository. This means that the available free disk space for your jobs to use is reduced.

3. Untagged jobs run on the **`small`** Linux x86-64 runner.

4. Jobs handled by hosted runners on GitLab.com time out after 3 hours, regardless of the timeout configured in a project.

5. The virtual machine where your job runs has **`sudo`** access with no password.

6. Firewall rules only allow outbound communication from the ephemeral VM to the public internet.

7. Inbound communication from the public internet to the ephemeral VM is not allowed.

8. Firewall rules do not permit communication between VMs.

9. The only internal communication allowed to the ephemeral VMs is from the runner manager.

10. Ephemeral runner VMs serve a single job and are deleted right after the job execution.

11. In addition to isolating runners on the network, each ephemeral runner VM only serves a single job and is deleted straight after the job execution. In the following example, three jobs are executed in a project’s pipeline. Each of these jobs runs in a dedicated ephemeral VM.

12. GitLab sends the command to remove the ephemeral runner VM to the Google Compute API immediately after the CI job completes. The [Google Compute Engine hypervisor](https://cloud.google.com/blog/products/gcp/7-ways-we-harden-our-kvm-hypervisor-at-google-cloud-security-in-plaintext) takes over the task of securely deleting the virtual machine and associated data.

13. The hosted runners share a distributed cache stored in a Google Cloud Storage (GCS) bucket. Cache contents not updated in the last 14 days are automatically removed, based on the [object lifecycle management policy](https://cloud.google.com/storage/docs/lifecycle). The maximum size of an uploaded cache artifact can be 5 GB after the cache becomes a compressed archive.