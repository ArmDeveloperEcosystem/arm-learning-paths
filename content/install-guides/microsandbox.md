---
title: Microsandbox

description: Install Microsandbox on Arm Linux with KVM and run a Python verification workload inside a libkrun microVM.

minutes_to_complete: 15
official_docs: https://docs.microsandbox.dev/

author: Pareena Verma

test_images:
test_maintenance: false

weight: 1
tool_install: true
multi_install: false
multitool_install_part: false
layout: installtoolsall
draft: true
---

Microsandbox is an open-source, local-first microVM runtime for untrusted workloads, including AI agents, user code, plugins, package installs, CI jobs, development environments, scrapers, and automation. It runs workloads in lightweight virtual machines (microVMs) using libkrun. On Arm Linux, it uses Kernel-based Virtual Machine (KVM) support to run a separate guest kernel for each sandbox.

Microsandbox runs on Linux, macOS, and Windows. The following steps install the `msb` command-line runtime on Ubuntu 24.04 LTS on `aarch64`, the tested Linux distribution for this guide. You then run Python inside a sandbox to verify the installation.

Microsandbox also supports macOS on Apple Silicon, where you can use the same installation script. For macOS installation and platform-specific setup checks, see the [Microsandbox quickstart](https://docs.microsandbox.dev/getting-started/quickstart).

The Microsandbox release bundle supplies the runtime and `libkrunfw` guest firmware library. You don't need Docker, Python on the host, or a separate system installation of libkrun.

## Before you begin

You need an Arm Linux system running Ubuntu 24.04 LTS, with sudo access and internet access to GitHub and Docker Hub. Allow disk space for the downloaded image and its extracted filesystem. You also need enough available memory for a 512 MiB guest alongside the host operating system.

These steps were tested on an Arm AGI CPU host. Your host must expose KVM to run the sandbox. If Ubuntu runs inside a virtual machine (VM), the outer hypervisor must expose nested virtualization.

Check your host:

```bash
uname -m
uname -r
cat /etc/os-release
```

Confirm that the architecture is `aarch64` and the operating system is Ubuntu 24.04 LTS.

### Check KVM access

Check that your current user can read and write the KVM device:

```bash
ls -l /dev/kvm
if [ -c /dev/kvm ] && [ -r /dev/kvm ] && [ -w /dev/kvm ]; then
    echo "KVM device is accessible"
else
    echo "STOP: resolve KVM availability or permissions before continuing"
fi
```

The expected output includes:

```output
KVM device is accessible
```

If the device exists and belongs to the `kvm` group but your user lacks access, add your user to that group:

```bash
sudo usermod -aG kvm "$USER"
```

Log out and back in to activate the kvm group for your session. 

## Install Microsandbox

Install the download and extraction tools:

```bash
sudo apt update
sudo apt install -y ca-certificates curl tar gzip coreutils
```

{{% notice Note %}}
The installer downloads the latest release. These steps were tested with Microsandbox v0.7.8. To find available versions, see the [Microsandbox releases page](https://github.com/superradcompany/microsandbox/releases).
{{% /notice %}}

Run the official installer from your user account, without `sudo`. By default, it installs the runtime and firmware in `~/.microsandbox` and creates command links in `~/.local/bin`. The `~` directory is your current user's home; for root, it resolves to `/root`.

```bash
curl -fsSL https://install.microsandbox.dev | sh
```

The output is similar to this excerpt. Home directory paths are shown as `~`; the installer prints their full paths:

```output
  Microsandbox Installer

info Detected platform: linux-aarch64
info Latest version: v0.7.8
info Downloading microsandbox...
...
info Verifying checksum...
done Checksum verified
info Extracting...
done Installed msb to ~/.microsandbox/bin/msb
done Linked microsandbox -> msb in ~/.microsandbox/bin/
done Installed libkrunfw to ~/.microsandbox/lib/
done Linked ~/.local/bin/msb -> ~/.microsandbox/bin/msb
done Linked ~/.local/bin/microsandbox -> ~/.microsandbox/bin/microsandbox
```

Wait for the installer to report that installation is complete. If `~/.local/bin` isn't on your PATH, the installer prints instructions for adding it.

Make the installed commands available in your current Bash session:

```bash
export PATH="$HOME/.local/bin:$PATH"
hash -r
```

Add the same `export PATH` line to `~/.bashrc` to make the commands available in future Bash sessions. Run the remaining commands with the same account you used to install Microsandbox.

Confirm the installed version:

```bash
msb --version
```

The output from the tested release is:

```output
msb 0.7.8
```

Your version can be newer because the installer selects the latest release.

## Verify the installation

Create a sandbox and run a Python command to verify that Microsandbox works as expected.

### Create a sandbox

Create a named microVM with one virtual CPU and 512 MiB of memory:

```bash
msb create --name arm-install-check --cpus 1 --memory 512M python:3.12-slim
```

The first run downloads the Arm64 image from Docker Hub. The `python:3.12-slim` tag can change as new Python releases become available. Wait for sandbox creation to finish successfully before continuing.

### Run a command in a sandbox

Execute Python through the sandbox runtime:

```bash
msb exec arm-install-check -- python3 -c 'import platform; print(platform.machine()); print("Python calculation:", 6 * 7)'
```

The expected output is:

```output
aarch64
Python calculation: 42
```

### Inspect the sandbox

Check the sandbox status and resource allocation:

```bash
msb inspect arm-install-check
```

The output is similar to:

```output
Name:           arm-install-check
Status:         running
Created:        2026-10-19 15:03:42
Updated:        2026-10-19 15:03:42
Image:          python:3.12-slim
Root Disk:      4096 MiB (managed, ext4)

Resources
  CPUs:         1
  Max CPUs:     1
  CPU Placement:inherit
  Memory:       512 MiB
  Max Memory:   512 MiB
  THP:          madvise
Security:       default
Deployment Profile:single-tenant
Shell:          /bin/sh

Environment
  PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
  LANG=C.UTF-8
  GPG_KEY=7169605F62C751356D054A26A821E680E5FA6305
  PYTHON_VERSION=3.12.15
  PYTHON_SHA256=c2c4321961fab0fb999d66e0cecf521c2ab3994c7992873ea99e306c1094fd5a
```

Confirm that the sandbox is `running` with one CPU and 512 MiB of memory. Timestamps vary between runs. Image environment values can change when the image tag is updated.

### List sandboxes

List the sandboxes:

```bash
msb ls
```

The output is similar to:

```output
NAME                 IMAGE               STATUS     CREATED
arm-install-check    python:3.12-slim    running    2026-10-19 15:03:42
```

Confirm that `arm-install-check` appears with the image `python:3.12-slim` and status `running`. Together with the Python output, this confirms that Microsandbox created the sandbox and executed the verification workload successfully.

### Check filesystem isolation

The sandbox has its own filesystem. Host files are accessible only through mounts you explicitly provide, as described in the [Microsandbox isolation overview](https://microsandbox.dev/features/isolation). The sandbox created in this guide has no host-directory mounts.

In your host terminal, create a temporary file and confirm that you can read it. Keep the same terminal open for the remaining checks and cleanup:

```bash
msb_host_file=$(mktemp /tmp/msb-host-check.XXXXXX)
printf 'This file belongs to the host.\n' > "$msb_host_file"
cat "$msb_host_file"
```

The expected output is:

```output
This file belongs to the host.
```

Try to read the same absolute path inside the sandbox:

```bash
msb exec arm-install-check -- python3 -c '
import pathlib
import sys

try:
    pathlib.Path(sys.argv[1]).read_text()
except FileNotFoundError:
    print("Host file is not visible in the sandbox.")
else:
    sys.exit("Unexpected result: the host file path is readable in the sandbox.")
' "$msb_host_file"
```

The expected output is:

```output
Host file is not visible in the sandbox.
```

This checks that the host file isn't exposed at the same path in the sandbox. The result is a missing file, rather than a filesystem permission denial.

Confirm that the sandbox can still write to its own `/tmp` directory:

```bash
msb exec arm-install-check -- python3 -c 'from pathlib import Path; p = Path("/tmp/msb-guest-check.txt"); p.write_text("Sandbox write succeeded."); print(p.read_text())'
```

The expected output is:

```output
Sandbox write succeeded.
```

Remove the temporary host file:

```bash
rm -- "${msb_host_file:?}"
```

Deleting the sandbox in the next step removes its test file.

## Delete the test sandbox

Stop and remove the verification sandbox:

```bash
msb stop arm-install-check
msb rm arm-install-check
msb ls
```

The output is similar to:

```output
   ✓ Stopped      arm-install-check
   ✓ Removed      arm-install-check
No sandboxes found.
```

If you have other sandboxes, `msb ls` lists those instead.

Confirm that `arm-install-check` no longer appears. This removes the sandbox; downloaded images remain cached for reuse.

Optionally remove the verification image if no other sandbox needs it:

```bash
msb image rm python:3.12-slim
```

The installed runtime and firmware remain available for future use.

## Next steps

You can now use Microsandbox to run Python workloads in microVMs on Arm Linux.

See the [Microsandbox CLI documentation](https://docs.microsandbox.dev/cli/overview) for sandbox lifecycle commands and the [Microsandbox SDK documentation](https://docs.microsandbox.dev/sdk/overview) for programmatic execution.
