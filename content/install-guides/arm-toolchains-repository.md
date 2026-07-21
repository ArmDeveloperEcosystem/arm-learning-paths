---
title: Arm Toolchains repository

additional_search_terms:
- Arm Toolchains
- Arm Toolchain for Linux
- Arm Performance Libraries
- Linux
- HPC

minutes_to_complete: 15

test_maintenance: false
test_images:
  - ubuntu:latest

official_docs: https://developer.arm.com/tools-and-software
description: Configure the Arm Toolchains repository on supported Linux aarch64 distributions to install Arm Toolchain for Linux and Arm Performance Libraries using the system package manager.
author: Gary Carroll

weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

The [Arm Toolchains repository](https://developer.arm.com/packages/arm-toolchains/) provides a native and convenient way to install selected Arm software products on supported Linux hosts using the host operating system package manager.

The repository files are used to distribute Linux packages for Arm Toolchains, including:

- Arm Toolchain for Linux
- Arm Performance Libraries for supported compilers on Linux

Using the repository, you can install, upgrade, and manage these packages using standard Linux package-management tools such as `apt`, `dnf`, `yum`, and `zypper`.

To use the repository, you'll need to install the repository package. Arm provides an `arm-toolchains-repository` package for each supported Linux distribution. The package installs:

- the Arm Toolchains repository definition for your Linux distribution
- the Arm Toolchains repository signing public key
- package manager configuration that associates the repository with the correct signing key

{{% notice Note %}}
You need root or `sudo` permissions to install system packages.
{{% /notice %}}

## Before you begin

Confirm you are using an Arm Linux system by running:

```bash
uname -m
```

The output is similar to:

```output
aarch64
```

Use the native package manager for your distribution:

- `apt` for Ubuntu LTS releases from 22.04
- `dnf` or `yum` for RHEL 8 or later and Amazon Linux 2023
- `zypper` for SLES 15 or 16

## About the signing key

Linux package managers use cryptographic signing keys to verify that repository metadata and packages are authentic and come directly from Arm.

In July 2026, Arm reviewed and strengthened the repository management and publication processes used for the Arm Toolchains repository. As part of the continuing evolution of this release channel, Arm revoked and replaced the signing key.

If you're setting up a new system after July 2026, installing the `arm-toolchains-repository` package automatically configures the current repository signing key for you. You don't need to install the key manually or verify fingerprints.

However, if you're upgrading a system that configured the Arm Toolchains repository for Linux before July 2026, you need to update the repository configuration to use the new key. 
Otherwise, your package manager might refuse to refresh repository metadata or install packages.

Existing installed copies of Arm Toolchain for Linux and Arm Performance Libraries continue to work.

### Repository signing key fingerprints

For reference or manual verification, the fingerprints of the previous and current Arm Toolchains signing keys are as follows.

Previous fingerprint:

```output
EE37 7ACD D5AD 4AB6 BD79  9B8A B83D 741E 7A05 AF82
```

Current fingerprint:

```output
A406 5BCE 9386 DD1E 62FD  E03B 8144 CA16 11A0 BD71
```

### (Optional) Manually verify the signing key

If you want to manually verify the signing key, ensure the `gpg` utility (part of GnuPG) is installed on your system, then download the key file and display its fingerprint:

```bash
curl -O https://developer.arm.com/packages/arm-toolchains/arm-toolchains.gpg
gpg --show-keys --fingerprint arm-toolchains.gpg
```

The output should show the current fingerprint:

```output
A406 5BCE 9386 DD1E 62FD  E03B 8144 CA16 11A0 BD71
```

## Previous repository locations

The current Arm Toolchains repository at [https://developer.arm.com/packages/arm-toolchains/](https://developer.arm.com/packages/arm-toolchains/) replaces the earlier repository structure that was based on repositories built using the SUSE Open Build Service.

Earlier repositories were published under the top-level package URL [https://developer.arm.com/packages/](https://developer.arm.com/packages/) and used repository prefixes such as:

```output
ACfL:<distro>
arm-toolchains:<distro>
```

These earlier repositories are deprecated but will continue to work until further notice.

Don't configure new systems to use the deprecated `ACfL:` or `arm-toolchains:` repository paths. Migrate existing systems to the current Arm Toolchains Linux repositories and install the current `arm-toolchains-repository` package.

The deprecated repositories will be removed in a future update.

## Install the repository package directly

Use one of the following commands to install the repository package [directly](https://developer.arm.com/packages/arm-toolchains/). This allows you to update the repository configuration even if your package manager can't currently refresh the Arm Toolchains repository metadata.

{{< tabpane code=true >}}
  {{< tab header="Ubuntu 24.04" language="bash" >}}
curl -O https://developer.arm.com/packages/arm-toolchains/ubuntu/pool/arm-toolchains-repository_2-2~noble_all.deb
sudo dpkg -i arm-toolchains-repository_2-2~noble_all.deb
sudo apt update
  {{< /tab >}}
  {{< tab header="Ubuntu 22.04" language="bash" >}}
curl -O https://developer.arm.com/packages/arm-toolchains/ubuntu/pool/arm-toolchains-repository_2-2~jammy_all.deb
sudo dpkg -i arm-toolchains-repository_2-2~jammy_all.deb
sudo apt update
  {{< /tab >}}
  {{< tab header="RHEL 10" language="bash" >}}
sudo dnf install -y https://developer.arm.com/packages/arm-toolchains/rhel/el10/aarch64/arm-toolchains-repository-2-2.el10.noarch.rpm
sudo dnf clean all
sudo dnf makecache
  {{< /tab >}}
  {{< tab header="RHEL 9" language="bash" >}}
sudo dnf install -y https://developer.arm.com/packages/arm-toolchains/rhel/el9/aarch64/arm-toolchains-repository-2-2.el9.noarch.rpm
sudo dnf clean all
sudo dnf makecache
  {{< /tab >}}
  {{< tab header="RHEL 8" language="bash" >}}
sudo dnf install -y https://developer.arm.com/packages/arm-toolchains/rhel/el8/aarch64/arm-toolchains-repository-2-2.el8.noarch.rpm
sudo dnf clean all
sudo dnf makecache
  {{< /tab >}}
  {{< tab header="Amazon Linux 2023" language="bash" >}}
sudo dnf install -y https://developer.arm.com/packages/arm-toolchains/amazonlinux/al2023/aarch64/arm-toolchains-repository-2-2.al2023.noarch.rpm
sudo dnf clean all
sudo dnf makecache
  {{< /tab >}}
  {{< tab header="SLES 15" language="bash" >}}
sudo zypper install -y https://developer.arm.com/packages/arm-toolchains/sles/sles15/aarch64/arm-toolchains-repository-2-2.sles15.noarch.rpm
sudo zypper clean
sudo zypper refresh
  {{< /tab >}}
  {{< tab header="SLES 16" language="bash" >}}
sudo zypper install -y https://developer.arm.com/packages/arm-toolchains/sles/sles16/aarch64/arm-toolchains-repository-2-2.sles16.noarch.rpm
sudo zypper clean
sudo zypper refresh
  {{< /tab >}}
{{< /tabpane >}}


## Use manual recovery

The recommended method is to install `arm-toolchains-repository` version `2-2` or later directly.

Use manual recovery only if you cannot install the repository package directly.

### Ubuntu manual recovery

Remove previous Arm Linux Toolchains Repository key material if present:

```bash
sudo rm -f /usr/share/keyrings/arm-toolchains-archive-keyring.gpg
sudo rm -f /etc/apt/keyrings/arm-toolchains-archive-keyring.gpg
sudo rm -f /etc/apt/trusted.gpg.d/arm-toolchains.gpg
sudo rm -f /etc/apt/trusted.gpg.d/arm-toolchains.asc
```

Install the current Arm Toolchains repository signing key:

```bash
curl -O https://developer.arm.com/packages/arm-toolchains/arm-toolchains.gpg
sudo install -D -m 0644 arm-toolchains.gpg \
  /usr/share/keyrings/arm-toolchains-archive-keyring.gpg
```

Check the fingerprint:

```bash
gpg --show-keys --fingerprint /usr/share/keyrings/arm-toolchains-archive-keyring.gpg
```

The output should include:

```output
A406 5BCE 9386 DD1E 62FD  E03B 8144 CA16 11A0 BD71
```

Find any existing Arm Toolchains repository entries:

```bash
grep -Rns "developer.arm.com/packages/arm-toolchains/ubuntu" \
  /etc/apt/sources.list /etc/apt/sources.list.d 
```

If the command finds an existing entry, edit that entry so it references `/usr/share/keyrings/arm-toolchains-archive-keyring.gpg` using `signed-by`. Don't create a second entry for the same repository because `apt` might report conflicting `Signed-By` values.

If the command doesn't find an entry, create `/etc/apt/sources.list.d/arm-toolchains.list` using one of the following commands:

For Ubuntu 24.04, run:

```bash
echo "deb [signed-by=/usr/share/keyrings/arm-toolchains-archive-keyring.gpg] https://developer.arm.com/packages/arm-toolchains/ubuntu noble main" | \
  sudo tee /etc/apt/sources.list.d/arm-toolchains.list
```

For Ubuntu 22.04, run:

```bash
echo "deb [signed-by=/usr/share/keyrings/arm-toolchains-archive-keyring.gpg] https://developer.arm.com/packages/arm-toolchains/ubuntu jammy main" | \
  sudo tee /etc/apt/sources.list.d/arm-toolchains.list
```

After creating `arm-toolchains.list`, refresh package metadata:

```bash
sudo apt update
```

### RPM-based manual recovery

Remove the previous Arm Toolchains public key if present:

```bash
sudo rpm -e gpg-pubkey-7a05af82* || true
```

Install the current Arm Toolchains repository signing key:

```bash
curl -O https://developer.arm.com/packages/arm-toolchains/arm-toolchains.gpg
sudo rpm --import arm-toolchains.gpg
```

Check that the key is installed:

```bash
rpm -qa gpg-pubkey*
```

Refresh package metadata by running one of the following set of commands.

For RHEL, Amazon Linux, and compatible RPM-based distributions:

```bash
sudo dnf clean all
sudo dnf makecache
```

For SLES:

```bash
sudo zypper clean
sudo zypper refresh
```

## Verify the repository package version

After installing the repository package, verify the installation:

{{< tabpane code=true >}}
  {{< tab header="Ubuntu" language="bash" >}}
dpkg -l arm-toolchains-repository
  {{< /tab >}}
  {{< tab header="RPM-based distributions" language="bash" >}}
rpm -q arm-toolchains-repository
  {{< /tab >}}
{{< /tabpane >}}

The installed version should be `2-2` or later.

## Troubleshoot package manager errors

If your system still trusts only the previous Arm Toolchains Repository signing key, package manager operations might fail when you refresh metadata, install packages, or upgrade packages.

Ubuntu hosts might experience errors running the `apt update` command, for example:

```output
Err:1 https://developer.arm.com/packages/arm-toolchains/ubuntu noble InRelease
  The following signatures couldn't be verified because the public key is not available: NO_PUBKEY <key-id>
W: An error occurred during the signature verification. The repository is not updated and the previous index files will be used. GPG error: <error>
W: Some index files failed to download. They have been ignored, or old ones used instead.
```

RPM-based hosts might download the new signing key but refuse to use it:

```output
The GPG keys listed for the "Arm Toolchains" repository are already installed but they are not correct for this package.
Check that the correct key URLs are configured for this repository..
 GPG Keys are configured as: file:///etc/pki/rpm-gpg/RPM-GPG-KEY-arm-toolchains
Error: GPG check FAILED
```

To resolve these errors, install the updated repository package and accept the new signing key.

## Next steps

After installing the repository package, you're ready to install the Arm Toolchain for Linux and the Arm Performance Libraries.

For installation instructions, see the [Arm Toolchain for Linux installation instructions](https://developer.arm.com/documentation/110477/latest/Installation) and the [Arm Performance Libraries installation instructions](/install-guides/armpl/) for your distribution.



