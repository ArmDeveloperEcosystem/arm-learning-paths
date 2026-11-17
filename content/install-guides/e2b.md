---
title: E2B

draft: true

description: Install a self-hosted E2B sandbox environment on Arm Linux with Docker Compose, KVM, and Firecracker microVMs.

minutes_to_complete: 25
official_docs: https://docs.e2b.dev/

author: Pareena Verma

test_images:
test_maintenance: false

weight: 1
tool_install: true
multi_install: false
multitool_install_part: false
layout: installtoolsall
---

E2B provides isolated Linux sandboxes for AI agents and generated code. A self-hosted E2B installation runs each sandbox in a Firecracker microVM and exposes the E2B API and SDK interfaces.

You'll install [E2B Embed](https://github.com/e2b-dev/runtime/tree/main/embed/compose), the official single-host deployment, on an Arm Linux system. E2B Embed uses Docker Compose to run the control plane, Firecracker orchestrator, dashboard, and supporting services on one host.

These instructions are for Ubuntu 24.04 LTS on `aarch64`. E2B requires KVM and Linux kernel 6.10 or later on Arm.

## Before you begin

Use a dedicated Arm Linux host with KVM, such as an Arm AGI CPU platform or an Arm-based bare-metal cloud instance. The installation loads kernel modules, reserves huge pages, creates host directories and network namespaces, and changes host networking and system settings.

You need:

- Ubuntu 24.04 LTS on `aarch64`
- Linux kernel 6.10 or later
- KVM and the TUN/TAP device
- A 4 KiB page-size kernel and cgroup v2
- Sudo access
- Docker Engine 27 or later and Docker Compose 2.24 or later
- 12 GiB of RAM and 20 GiB of free disk space, as recommended by E2B
- Internet access to Docker Hub, Google Artifact Registry, Google Cloud Storage and GitHub

The default configuration reserves 4 GiB of RAM as huge pages for sandboxes.

### Check the Arm Linux host

Print the architecture, kernel version, page size, and cgroup filesystem type:

```bash
uname -m
uname -r
getconf PAGESIZE
stat -fc %T /sys/fs/cgroup
```

Confirm that the output shows:

- `aarch64` for the architecture
- Kernel version 6.10 or later
- `4096` for the page size
- `cgroup2fs` for the cgroup filesystem

{{% notice 64 KiB page-size kernels %}}
The E2B Embed version used in this guide doesn't support 64 KiB-page kernels on Arm. E2B requires a 4 KiB-page kernel, and Firecracker currently supports only 4 KiB host and guest kernels on `aarch64`. Support for 64 KiB pages is tracked as a [Firecracker feature request](https://github.com/firecracker-microvm/firecracker/issues/6381), not as an experimental E2B feature. If `getconf PAGESIZE` returns `65536`, switch to a 4 KiB-page kernel before continuing. See the [E2B Embed host requirements](https://github.com/e2b-dev/runtime/tree/main/embed/compose#requirements) for more information.
{{% /notice %}}

If Ubuntu 24.04 is still using its original 6.8 kernel, install the current hardware enablement kernel:

```bash
sudo apt update
sudo apt install -y linux-generic-hwe-24.04
sudo reboot
```

After the system restarts, run `uname -r` again and confirm that the active kernel is version 6.10 or later.

### Check KVM and TUN/TAP

Confirm that the KVM and TUN/TAP devices exist:

```bash
ls -l /dev/kvm /dev/net/tun
```

Check that the current user can access KVM:

```bash
if [ -c /dev/kvm ] && [ -r /dev/kvm ] && [ -w /dev/kvm ]; then
    echo "KVM device is accessible"
else
    echo "STOP: resolve KVM availability or permissions before continuing"
fi
```

The expected output is:

```output
KVM device is accessible
```

If `/dev/kvm` belongs to the `kvm` group but your user doesn't have access, add the user to the group:

```bash
sudo usermod -aG kvm "$USER"
```

Activate the new group membership:

```bash
newgrp kvm
```

The command starts a new shell with `kvm` as the active group.

### Install the host packages

Install the packages required by E2B and its verification steps:

```bash
sudo apt update
sudo apt install -y ca-certificates curl e2fsprogs iproute2 iptables python3-venv rsync
```

### Install Docker

If Docker isn't already installed, follow the [Docker Engine install guide](/install-guides/docker/docker-engine/).

Add your user to the `docker` group so that the E2B commands don't require `sudo`:

```bash
sudo usermod -aG docker "$USER"
```

Activate the new group membership:

```bash
newgrp docker
```
Print the installed versions:

```bash
docker version --format 'Docker Engine {{.Server.Version}}'
docker compose version
```

The output is similar to:

```output
Docker Engine 29.8.0
Docker Compose version v5.5.1
```

Confirm that Docker Engine is version 27 or later and Docker Compose is version 2.24 or later.

## Install E2B Embed

Create a directory for the Compose deployment:

```bash
mkdir -p ~/e2b
cd ~/e2b
```

{{% notice Pinned E2B runtime revision %}}
These commands pin E2B runtime commit `780b991b5e4d814f5a7ef625a21033d75416e0f1` because `main` changes over time and release tag `2026.30` doesn't contain the Embed Compose files. This revision provides matching `compose.yaml` and `.env` files, pins E2B API v0.30.0, and was validated on an Arm AGI CPU. If you select another commit from the [E2B runtime repository](https://github.com/e2b-dev/runtime), download both files from that commit.
{{% /notice %}}

Download the Compose file and its matching environment file:

```bash
e2b_runtime_commit=780b991b5e4d814f5a7ef625a21033d75416e0f1
curl -fsSLo compose.yaml "https://raw.githubusercontent.com/e2b-dev/runtime/${e2b_runtime_commit}/embed/compose/compose.yaml"
curl -fsSLo .env "https://raw.githubusercontent.com/e2b-dev/runtime/${e2b_runtime_commit}/embed/compose/.env"
```

Validate the Compose configuration:

```bash
docker compose config --quiet
```

The command exits without output when the configuration is valid.

Start E2B and wait for the base sandbox template to become ready:

```bash
docker compose up -d --wait
```

The first run performs host checks, configures the host, downloads the Firecracker artifacts and container images, initializes the databases, and builds the `base` template. The download and build can take several minutes.

{{% notice Warning %}}
The E2B Compose file publishes multiple service ports on every host interface. Keep the host behind a firewall. Only expose ports 3000, 3001, and 3002 to trusted clients, if needed. In particular, don't expose the unauthenticated orchestrator API on port 5008.
{{% /notice %}}

## Verify the installation

Check the service state:

```bash
docker compose ps
```

In the output, confirm that the `ready` service has a status beginning with `Up`. E2B uses this service to indicate that the stack and the `base` template are usable. The other long-running services should also show `Up` and, when a health check is configured, `(healthy)`.

To include the one-time setup services in the output, run:

```bash
docker compose ps -a
```

Setup services such as `preflight`, `host-setup`, `fetch-artifacts`, the database migrators, `seed`, and `base-template` should show `Exited (0)`. A nonzero exit code or a long-running service that isn't `Up` indicates a failed installation.

Run the packaged smoke test:

```bash
docker compose --profile test run --rm smoke
```

The test creates a sandbox through the E2B SDK, runs a command in the Firecracker microVM, reaches a test service through the client proxy, and deletes the sandbox. Docker prints container status updates before the test result. The final line is similar to:

```output
smoke: ok sandbox=i7hkvuw9l8pybg2bfreo8 port 8080 reached through http://127.0.0.1:3002
```

The sandbox ID differs on each run. Confirm that the final line begins with `smoke: ok`, reports that port 8080 was reached through `http://127.0.0.1:3002`.

### Run Python in an E2B sandbox

Load the local E2B API endpoints and generated team API key into the current shell:

```bash
eval "$(docker compose exec ready cat /run/e2b/sdk.env)"
```

The API key is a secret. Don't print or store the command output in logs.

Create a Python virtual environment and install the SDK version tested by the pinned E2B deployment:

```bash
python3 -m venv .venv
.venv/bin/pip install e2b==2.46.0
```

Run a Python program that creates a sandbox, prints its architecture, performs a calculation, and deletes the sandbox:

```bash
.venv/bin/python - <<'PY'
from e2b import Sandbox

sandbox = Sandbox.create("base")
try:
    result = sandbox.commands.run(
        "uname -m && python3 -c 'print(6 * 7)'"
    )
    print(result.stdout, end="")
finally:
    sandbox.kill()
PY
```

The expected output is:

```output
aarch64
42
```

This confirms that the E2B API created an Arm64 Firecracker sandbox and ran commands inside it.

## Troubleshoot E2B

If `docker compose up` fails, identify the failing service:

```bash
docker compose ps -a
```

Read the logs for the setup services:

```bash
docker compose logs preflight host-setup fetch-artifacts base-template
```

Look for a line beginning with `FIX:`, correct the reported problem, and run `docker compose up -d --wait` again. The setup steps are idempotent and skip work that already succeeded.

If sandbox creation fails on Arm with `Failed to UFFD object`, the running kernel lacks the userfaultfd write-protect support E2B needs. Install the Ubuntu 24.04 hardware enablement kernel, reboot, and confirm that `uname -r` reports kernel 6.10 or later.

If the stack reports insufficient huge pages, check the current allocation:

```bash
grep -E 'HugePages_Total|HugePages_Free|Hugepagesize' /proc/meminfo
```

The default `HUGEPAGES=2048` reserves 2048 pages of 2 MiB each, or 4 GiB. On a host with less memory, lower `HUGEPAGES` in `.env` and run `docker compose up -d --wait` again. A 512 MiB `base` sandbox needs 256 of the 2 MiB huge pages.

If the smoke test fails, inspect the main runtime logs:

```bash
docker compose logs api orchestrator client-proxy
```

After a host reboot, return to `~/e2b` and run `docker compose up -d --wait` to restore the host networking state required by E2B.

## Next steps

You can now use the E2B SDKs to run AI agent code in self-hosted Firecracker microVMs on Arm Linux.

For configuration, upgrades, security considerations, and sandbox limits, see the [E2B Embed Docker Compose documentation](https://github.com/e2b-dev/runtime/tree/main/embed/compose).
