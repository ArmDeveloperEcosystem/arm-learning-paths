---
title: gVisor (runsc)

description: Install gVisor on Ubuntu 24.04 for Arm and verify that Docker runs containers with the runsc application kernel runtime.

minutes_to_complete: 15

official_docs: https://gvisor.dev/docs/

additional_search_terms:
- gvisor
- runsc
- containers
- docker
- containment
- sandbox

author: Jason Andrews

test_images:
- ubuntu:latest
test_maintenance: true

weight: 1
tool_install: true
multi_install: false
multitool_install_part: false
layout: installtoolsall
---

gVisor provides an application kernel that implements Linux system calls in user space. The gVisor `runsc` runtime lets you run containers with an additional isolation boundary between the application and the host kernel.

gVisor delivers a middle ground between lightweight containers and hardware-virtualized microVMs. Standard containers share the host kernel directly, while microVMs run full guest kernels inside hypervisors. gVisor instead intercepts application system calls and reimplements them inside a memory-safe user-space application kernel. This sandbox architecture limits direct host kernel exposure without the resource footprint or startup latency of a microVM, making it well-suited for running untrusted workloads safely.

You'll install `runsc` on an Arm Linux host and verify it with Docker Engine. 

By default, gVisor uses its systrap platform to intercept system calls in user space using Linux signals and shared memory. gVisor therefore doesn't need hardware virtualization or `/dev/kvm` access.

## Before you begin

Ensure that you have the following:

- Ubuntu 22.04 and later running on an Arm Linux system 
- [Docker Engine](/install-guides/docker/docker-engine/) installed
- Sudo access to install packages and restart Docker

Confirm that you're using an Arm machine:

```bash
uname -m
```

For an Arm Linux system, the output is:

```output
aarch64
```

## Install gVisor runsc

Install the APT repository prerequisites:

```bash
sudo apt update
sudo apt install ca-certificates curl gnupg -y
```

Import the gVisor repository signing key:

```bash
curl -fsSL https://gvisor.dev/archive.key -o gvisor-archive.key
sudo gpg --dearmor --yes -o /usr/share/keyrings/gvisor-archive-keyring.gpg gvisor-archive.key
```

Add the repository and install the package:

{{% notice Note %}}
The commands use the gVisor release version `20261005.0`. To select another release, check the [gVisor releases](https://github.com/google/gvisor/releases) and [versioned APT repository instructions](https://gvisor.dev/docs/user_guide/install/#specific-release), then update the repository date and package version.
{{% /notice %}}

```bash
echo "deb [arch=arm64 signed-by=/usr/share/keyrings/gvisor-archive-keyring.gpg] https://storage.googleapis.com/gvisor/releases 20261005 main" | sudo tee /etc/apt/sources.list.d/gvisor.list
sudo apt update
sudo apt install -y runsc=20261005.0
```

The package includes the runtime and its accompanying binaries. 

## Configure Docker

When you install `runsc`, Docker is automatically configured.

Restart Docker to load the runtime configuration:

```bash
sudo systemctl restart docker
```

## Verify the installation

Print the runtime version:

```bash
runsc --version
```

The first line identifies the installed runtime release. 

For version `20261005.0`, the expected output is:

```output
runsc version release-20261005.0
```

If you installed another release, check that its version appears instead.

Confirm that Docker registered the `runsc` runtime:

```bash
sudo docker info --format '{{if .Runtimes.runsc}}runsc runtime is registered{{else}}runsc runtime is NOT registered{{end}}'
```

The expected output is:

```output
runsc runtime is registered
```

Print the host kernel release and architecture:

```bash
uname -rm
```

The output shows your host's Linux kernel release and `aarch64`. The kernel release varies by host.

Run the same check inside a container using `runsc`:

```bash
sudo docker run --runtime=runsc --rm ubuntu:24.04 uname -rm
```

After any image download messages, the expected output for the gVisor release with its default configuration is:

```output
4.19.0-gvisor aarch64
```

The container sees the kernel release advertised by gVisor instead of the host kernel's release. `4.19.0-gvisor` is a Linux compatibility identifier and doesn't mean that gVisor runs a Linux 4.19 guest kernel. Use `runsc --version` to identify the installed gVisor release. The version string alone doesn't verify isolation.

### Compare kernel logs

Run `dmesg` using Docker's standard `runc` runtime:

```console
sudo docker run --runtime=runc --rm ubuntu:24.04 dmesg
```

With normal Docker security settings, the expected output is:

```output
dmesg: read kernel buffer failed: Operation not permitted
```

Repeat the check with `runsc` and list the first 10 log lines using the [upstream runtime verification command](https://gvisor.dev/docs/user_guide/quick_start/docker/#verify-the-runtime):

```bash
sudo docker run --runtime=runsc --rm ubuntu:24.04 sh -c 'dmesg | head -n 10'
```

The output starts with messages similar to:

```output
[    0.000000] Starting gVisor...
[    0.317761] Letting the watchdogs out...
[    0.616103] Generating random numbers by fair dice roll...
[    0.617251] Creating bureaucratic processes...
[    0.768548] Gathering forks...
[    1.138589] Granting licence to kill(2)...
[    1.203738] Committing treasure map to memory...
[    1.414817] DeFUSEing fork bombs...
[    1.791267] Daemonizing children...
[    2.095388] Consulting tar man page...
```

The message text and timestamps vary between runs.

gVisor handles the kernel-log request and generates sandbox messages instead of exposing the host's kernel logs. The banner is a quick check that Docker selected gVisor for the test container. 

## Troubleshoot issues with gVisor

If Docker reports an unknown runtime, or if you install Docker after `runsc`, run `sudo runsc install`. Then, restart Docker and inspect the runtimes again. The [Docker quick start](https://gvisor.dev/docs/user_guide/quick_start/docker/) describes the configuration entry.

If Docker fails to restart, inspect `sudo journalctl -u docker -n 50 --no-pager` for configuration errors. Preserve other settings in `/etc/docker/daemon.json` when correcting the runtime entry.

If the test container works but your application fails, check the [gVisor application compatibility guidance](https://gvisor.dev/docs/user_guide/compatibility/linux/arm64). An unsupported system call might require an application change or a different runtime.

## Next steps

You can now run your own containers with gVisor by including `--runtime=runsc` in your `docker run` commands. 

For guidance on choosing workloads and tuning your configuration, see the [gVisor production guide](https://gvisor.dev/docs/user_guide/production/).
