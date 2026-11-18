---
title: NVIDIA OpenShell

description: Install NVIDIA OpenShell on Arm Linux to run AI agents in policy-governed sandboxes with kernel-level isolation.

minutes_to_complete: 15
official_docs: https://docs.nvidia.com/openshell/latest/

additional_search_terms:
- openshell
- nvidia
- nemoclaw
- sandbox
- agent
- landlock
- microvm

author: Jason Andrews

test_images:
test_maintenance: false

weight: 1
tool_install: true
multi_install: false
multitool_install_part: false
layout: installtoolsall
---

NVIDIA OpenShell is an open-source, secure runtime for autonomous AI agents. It protects your host machine and enterprise systems by running agents inside sandboxes. The sandboxes provide kernel-level isolation, granular filesystem jails, and network policy enforcement.

On Arm Linux, OpenShell uses the Linux kernel Landlock Linux Security Module (LSM) and seccomp for process containment. For stronger isolation, OpenShell also supports a microVM mode that adds a hardware virtual machine (VM) boundary using kernel-based VM (KVM) and `libkrun`.

OpenShell runs on multiple platforms. The following steps are for Ubuntu and Debian on `aarch64`. You can use the same steps for other Debian-based distributions on Arm Linux. 

OpenShell is also supported on macOS, where you can install it using Homebrew and run the gateway as a Homebrew service. For macOS-specific steps, see the [NVIDIA OpenShell documentation](https://docs.nvidia.com/openshell/about/installation).

## Before you begin

You need an Arm Linux system running Ubuntu 22.04 or later on `aarch64`, with sudo access.

Choose a sandbox backend and complete its prerequisites before installing OpenShell:

- The container backend is the default. It uses Landlock, seccomp, and supervisor-level network policy. It works on Arm Linux servers that meet the kernel and runtime requirements, including cloud instances and VMs without KVM. You can use Docker or Podman as the runtime.
- The microVM backend runs each sandbox in its own lightweight VM using `libkrun` and KVM. It adds a hardware VM boundary on top of the Landlock and seccomp controls, acting as a second layer of isolation. It requires host access to KVM.

Use the microVM backend if you need a hardware VM boundary in addition to the sandbox controls.

### Container backend prerequisites

For the container backend, confirm that your Arm Linux host meets the Landlock and runtime prerequisites.

#### Landlock requirement

Containers share the host kernel, so your host needs Landlock enabled. Landlock limits which files an agent can access. OpenShell needs Landlock ABI 3 or newer, introduced in Linux 6.2.

Check your running host kernel version:

```bash
uname -r
```

Use Linux 6.2 or later with Landlock enabled, or a distribution kernel with the required facilities backported.

Check the active LSMs on the host:

```bash
sudo cat /sys/kernel/security/lsm
```

The output is similar to:

```output
lockdown,capability,landlock,yama,apparmor,ima,evm
```

Confirm that `landlock` appears in the comma-separated output. This confirms that Landlock is active, but not its ABI version.

The host kernel also needs seccomp user-notification and support for reading workload process memory. OpenShell checks the required facilities when starting a sandbox and refuses to start the workload if they are unavailable. For the full set of requirements and startup checks, see the [OpenShell kernel requirements](https://docs.nvidia.com/openshell/about/support-matrix#kernel-requirements).

#### Install a sandbox runtime

If you don't already have Docker Engine, install it:

{{% notice Note %}}
Alternatively, you can use the Podman driver to run container sandboxes. For setup and configuration details, see the [OpenShell Podman driver documentation](https://docs.nvidia.com/openshell/how-it-works/sandboxes/runtimes#podman-driver).
{{% /notice %}}

```bash
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
```

Add your user to the docker group:

```bash
sudo usermod -aG docker $USER
```

Log out and back in to activate the Docker group for your session. 

On cloud instances such as Amazon EC2, the systemd user session can persist across SSH reconnects. Reboot instead:

```bash
sudo reboot
```

When the instance is back up, check that the group is active:

```bash
groups
```

Confirm that `docker` appears in the output.

### microVM backend prerequisites

Confirm that your Arm host supports KVM acceleration and that the gateway user has access to `/dev/kvm`. Your host kernel doesn't need Landlock for the microVM backend.

The guest kernel inside the microVM needs Landlock enabled with ABI 3 or newer, seccomp user-notification, and support for reading workload process memory. OpenShell checks for these requirements inside the guest when starting a sandbox. For more information, see the [OpenShell kernel requirements](https://docs.nvidia.com/openshell/about/support-matrix#kernel-requirements).

Install `cpu-checker` on Ubuntu:

```bash
sudo apt install cpu-checker -y
```

Check if KVM is available:

```bash
sudo kvm-ok
```

If KVM is available, the output is similar to:

```output
INFO: /dev/kvm exists
KVM acceleration can be used
```

## Install OpenShell

After completing the prerequisites for your backend, run the official installation script. On Ubuntu or Debian, it installs a Debian package, starts the gateway as a systemd user service, and registers it with the CLI.

{{% notice Note %}}
The command installs the latest stable release. To install a specific version, set the `OPENSHELL_VERSION` environment variable to a release tag before running the script. To find available releases, see the [OpenShell releases page](https://github.com/NVIDIA/OpenShell/releases).
{{% /notice %}}

Run the installation script:

```bash
curl -LsSf https://raw.githubusercontent.com/NVIDIA/OpenShell/main/install.sh | sh
```

Confirm that the CLI can connect to the gateway:

```bash
openshell status
```

The output is similar to:

```output
Server Status

  Gateway: openshell
  Server: https://127.0.0.1:17670
  Status: Connected
  Authentication: Authenticated (mTLS transport)
  Version: 0.1.3
```

## (Optional) Configure the microVM backend 

To use the microVM backend, switch to it after installing OpenShell. If you're using the container backend, skip this section.

Create the configuration directory if needed:

```bash
mkdir -p ~/.config/openshell
```

Open `~/.config/openshell/gateway.toml` in a text editor. If the file exists, change or add `compute_driver = "vm"` under its existing `[openshell.gateway]` table, preserving all other settings. Don't add a duplicate table or key.

If the file doesn't exist, create it with the following contents:

```toml
[openshell]
version = 2

[openshell.gateway]
compute_driver = "vm"
```

Validate the configuration before restarting the gateway:

```bash
openshell-gateway config preflight --path ~/.config/openshell/gateway.toml
```

If preflight reports an error, correct it before continuing. Restart the gateway to apply the change:

```bash
systemctl --user restart openshell-gateway
```

Confirm that the gateway is still connected:

```bash
openshell status
```

The output is similar to:

```output
Server Status

  Gateway: openshell
  Server: https://127.0.0.1:17670
  Status: Connected
  Authentication: Authenticated (mTLS transport)
  Version: 0.1.3
```

To return to the Docker driver, change `compute_driver` to `"docker"` under the existing `[openshell.gateway]` table. Preserve the rest of the file, then validate it and restart the gateway:

```bash
openshell-gateway config preflight --path ~/.config/openshell/gateway.toml
```

After preflight succeeds, run:

```bash
systemctl --user restart openshell-gateway
```

## Verify the installation

Create a sandbox to verify that OpenShell works as expected. You can then check the filesystem and network boundaries of the sandbox.

### Create a sandbox

Create a test sandbox using the default workload image (`nvcr.io/nvidia/base/ubuntu:24.04`):

```bash
openshell sandbox create --name verify-test --detach
```
The output is similar to:

```output
Created sandbox: verify-test

  [0.0s] Requesting compute...
  [0.0s] Sandbox allocated
  [0.6s] Pulling image nvcr.io/nvidia/base/ubuntu:24.04
  [3.3s] Image pulled
  [3.6s] Starting sandbox Container created
```
To use a different image when creating the sandbox, pass it with `--from`:

```bash
openshell sandbox create --name verify-test --from ubuntu:26.04 --detach
```
### Check the sandbox kernel

Check the kernel version and architecture inside it:

```bash
openshell sandbox exec -n verify-test -- uname -rm
```

With the Docker driver, the sandbox shares the host kernel, so you'll see the host kernel information. The output is similar to:

```output
7.1.5-76070105-generic aarch64
```

With the microVM backend, the sandbox runs a guest kernel provided by `libkrun`, so you'll see a different kernel version from the host.

The output is similar to:

```output
6.12.76 aarch64
```

Both examples report `aarch64`. Kernel versions vary by host and OpenShell release. A different guest kernel version is consistent with a separate VM kernel, but `uname` alone doesn't verify KVM use or the selected runtime.

### List sandboxes

List all running sandboxes:

```bash
openshell sandbox list
```

The output is similar to:

```output
NAME        CREATED              PHASE
verify-test 2026-10-08 19:48:42  Ready
```

### Run a command in a sandbox

Run a command inside a running sandbox with `sandbox exec`:

```bash
openshell sandbox exec -n verify-test -- uname -m
```

The output is:

```output
aarch64
```

The `aarch64` output confirms the sandbox kernel's architecture.

### Connect to a sandbox

Open an interactive shell session inside a sandbox:

```bash
openshell sandbox connect verify-test
```

To exit the session, press **Ctrl + C**.

### Test sandbox boundaries

OpenShell applies a restrictive default policy when all of the following are true:

- No global policy is active
- The sandbox has no saved policy
- Its image contains no policy

Creating a sandbox without `--policy` doesn't guarantee that the restrictive default applies. The following examples assume that the default is active and that no providers add network access. For policy selection and runtime additions, see [Default Policy and Baseline Paths](https://docs.nvidia.com/openshell/how-it-works/policies/default-policy) in the NVIDIA OpenShell documentation.

#### Filesystem isolation

The restrictive default grants read-only access to the following paths:

- `/bin`
- `/usr`
- `/lib`
- `/proc`
- `/dev/urandom`
- `/etc`
- `/var/log`

It grants read-write access to the sandbox working directory, `/tmp`, and `/dev/null`. These paths belong to the sandbox filesystem. Host files aren't exposed by default. Explicitly configured mounts can change that boundary.

Inspect the base and effective policies of the sandbox before testing the boundary:

```bash
openshell policy get verify-test --base
openshell policy get verify-test --full
```

Confirm that the filesystem access matches the restrictive default and that the effective policy has no network rules. These views omit some runtime-only filesystem grants, such as sandbox CA certificates. If another policy is active, the following results can differ.

Try to list the sandbox's `/root/.ssh` directory:

```bash
openshell sandbox exec -n verify-test -- ls /root/.ssh
```

The output shows that access is denied:

```output
ls: cannot access '/root/.ssh': Permission denied
```

Try to list the sandbox's `/home` directory. This tests sandbox path access, rather than inspecting the host's home directory:

```bash
openshell sandbox exec -n verify-test -- ls /home
```

The output is similar to:

```output
ls: cannot open directory '/home': Permission denied
```

Writes outside allowed paths are also blocked:

```bash
openshell sandbox exec -n verify-test -- touch /etc/evil
```

The output is similar to:

```output
touch: cannot touch '/etc/evil': Permission denied
```

The `/tmp` directory is writable so that agents have a scratch space:

```bash
openshell sandbox exec -n verify-test -- touch /tmp/ok && echo "write succeeded"
```

The output is:

```output
write succeeded
```

#### Network isolation

The restrictive default defines no network rules, so outbound connections are denied. Image policies, global policies, and attached providers can change the effective network access.

With no network rules in the effective policy, test a direct outbound connection:

```bash
openshell sandbox exec -n verify-test -- bash -c 'echo > /dev/tcp/93.184.216.34/80'
```

The output is similar to:

```output
bash: connect: Permission denied
bash: line 1: /dev/tcp/93.184.216.34/80: Permission denied
```

To grant an agent access to specific network destinations, create a declarative YAML policy and pass it at sandbox creation with `--policy`. For more information, see [Sandbox Policies](https://docs.nvidia.com/openshell/how-it-works/policies/overview) in the NVIDIA OpenShell documentation.

OpenShell enforces isolation through multiple layers:

- Landlock LSM adds kernel-enforced filesystem restrictions to the sandboxed processes.
- Network policy mediates each outbound TCP connection at the supervisor level.
- Credential providers mean that the agent process never receives real API key values.

Landlock provides another containment layer, but it relies on the enforcing kernel. It can't guarantee protection against an exploit that compromises that kernel.

## Delete the test sandbox

After verification, delete the test sandbox:

```bash
openshell sandbox delete verify-test
```

The output is similar to:

```output
✓ Sandbox verify-test deletion accepted; cleanup is pending
```

## Next steps

You can now use NVIDIA OpenShell to run AI agents and untrusted code in policy-governed environments.
