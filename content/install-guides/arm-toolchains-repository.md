---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Arm Toolchains Repository

draft: true

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- Arm Toolchains
- Arm Toolchain for Linux
- Arm Performance Libraries
- Linux
- HPC

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

test_maintenance: false
test_images:
  - ubuntu:latest

### Link to official documentation
official_docs: https://developer.arm.com/tools-and-software
description: Configure the Arm Toolchains Repository package archive on supported Linux AArch64 distributions to enable installing Arm Toolchains products using the system package manager.
author: Gary Carroll

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

# Arm Toolchains Repository

The Arm Toolchains Linux repositories provide a native and convenient way to install selected Arm software products on supported Linux hosts using the host operating system package manager.

The repositories are published at [https://developer.arm.com/packages/arm-toolchains/](https://developer.arm.com/packages/arm-toolchains/).

They are used to distribute Linux packages for Arm Toolchains products, including:

- Arm Toolchain for Linux
- Arm Performance Libraries for supported compilers on Linux

Using the Arm Toolchains Linux repositories allows you to install, upgrade, and manage these products using standard Linux package-management tools such as `apt`, `dnf`, `yum`, and `zypper`.

Note: root permissions are required to install system packages.

{{% notice Repository signing key update July 2026 %}}
Arm has recently reviewed and strengthened the repository management and publication processes used for the Arm Toolchains Linux repositories.

As part of the continuing evolution of this release channel, Arm has revoked and replaced the signing key used for the Arm Toolchains Linux repositories.

If you previously configured the Arm Toolchains Linux repositories, install the `arm-toolchains-repository` package version `2-2` or later before installing or upgrading Arm Toolchain for Linux or Arm Performance Libraries.

Existing installed copies of Arm Toolchain for Linux and Arm Performance Libraries continue to work.
{{% /notice %}}

## Before you begin

You need a supported Linux host with `aarch64` architecture.

You also need the package manager for your Linux distribution:

- `apt` for Ubuntu LTS releases from 22.04
- `dnf` or `yum` for RHEL 8 or later and Amazon Linux 2023
- `zypper` for SLES 15 or 16

## What is the Arm Toolchains repository package?

Arm provides an `arm-toolchains-repository` package for each supported Linux distribution.

This package configures the Arm Toolchains Linux package repository on your host system.

The package installs:

- the Arm Toolchains repository definition for your Linux distribution
- the Arm Toolchains repository signing public key
- package manager configuration that associates the repository with the correct signing key

Install this repository package before you install Arm Toolchain for Linux or Arm Performance Libraries.

## Why the signing key matters

Linux package managers use signing keys to verify that repository metadata and packages come from the expected publisher.

For the Arm Toolchains Linux repositories, the signing key is part of the trust model for package installation and upgrades. If your package manager does not have the current Arm Toolchains repository signing key installed, it might refuse to refresh repository metadata or install packages from the repository.

The previous Arm Toolchains repository signing key was replaced in July 2026.

The previous key fingerprint was:

```output
EE37 7ACD D5AD 4AB6 BD79  9B8A B83D 741E 7A05 AF82
```

The current key fingerprint is:

```output
A406 5BCE 9386 DD1E 62FD  E03B 8144 CA16 11A0 BD71
```

You can display the fingerprint from a downloaded key file with:

```bash
gpg --show-keys --fingerprint arm-toolchains.gpg
```

The output should show the current fingerprint:

```output
A406 5BCE 9386 DD1E 62FD  E03B 8144 CA16 11A0 BD71
```

## Expected package manager errors

If your system still trusts only the previous Arm Toolchains repository signing key, package manager operations might fail when you refresh metadata, install packages, or upgrade packages.

Ubuntu hosts may experience errors running the `apt update` command, for example:

```output
Err:1 https://developer.arm.com/packages/arm-toolchains/ubuntu noble InRelease
  The following signatures couldn't be verified because the public key is not available: NO_PUBKEY <key-id>
W: An error occurred during the signature verification. The repository is not updated and the previous index files will be used. GPG error: <error>
W: Some index files failed to download. They have been ignored, or old ones used instead.
```

RPM based hosts may download the new signing key but refuse to use it:

```output
The GPG keys listed for the "Arm Toolchains" repository are already installed but they are not correct for this package.
Check that the correct key URLs are configured for this repository..
 GPG Keys are configured as: file:///etc/pki/rpm-gpg/RPM-GPG-KEY-arm-toolchains
Error: GPG check FAILED
```

These errors are expected on systems that have not yet installed the updated repository package or accepted the new signing key.

Install the `arm-toolchains-repository` package version `2-2` or later for your Linux distribution, then refresh package metadata to resolve such errors.

## Install the repository package

Install `arm-toolchains-repository` version `2-2` or later for your Linux distribution.

The examples below install the repository package directly from [https://developer.arm.com/packages/arm-toolchains/](https://developer.arm.com/packages/arm-toolchains/). This allows you to update the repository configuration even if your package manager cannot currently refresh the Arm Toolchains repository metadata.

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

## Verify the repository package version

After installing the repository package, verify that version `2-2` or later is installed.

{{< tabpane code=true >}}
  {{< tab header="Ubuntu" language="bash" >}}
dpkg -l arm-toolchains-repository
  {{< /tab >}}
  {{< tab header="RPM-based distributions" language="bash" >}}
rpm -q arm-toolchains-repository
  {{< /tab >}}
{{< /tabpane >}}

The installed version should be `2-2` or later.

## Install Arm Toolchain for Linux

After installing the repository package, follow the [Arm Toolchain for Linux installation instructions](https://developer.arm.com/documentation/110477/latest/Installation) for your distribution.

The repository package must be installed first because it configures the package manager repository and the signing key used to verify packages.

## Install Arm Performance Libraries

After installing the repository package, follow the [Arm Performance Libraries installation instructions](https://developer.arm.com/documentation/102620/latest/Installation) for your distribution.

The repository package must be installed first because it configures the package manager repository and the signing key used to verify packages.

## Manual recovery

The recommended method is to install `arm-toolchains-repository` version `2-2` or later.

Use manual recovery only if you cannot install the repository package directly.

### Ubuntu manual recovery

Remove previous Arm Toolchains repository key material if present:

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

Ensure the Arm Toolchains repository entry references the installed keyring using `signed-by`.

Example for Ubuntu 24.04:

```output
deb [signed-by=/usr/share/keyrings/arm-toolchains-archive-keyring.gpg] https://developer.arm.com/packages/arm-toolchains/ubuntu noble main
```

Example for Ubuntu 22.04:

```output
deb [signed-by=/usr/share/keyrings/arm-toolchains-archive-keyring.gpg] https://developer.arm.com/packages/arm-toolchains/ubuntu jammy main
```

Refresh package metadata:

```bash
sudo apt update
```

### RPM-based manual recovery

Remove the previous Arm Toolchains public key if present:

```bash
sudo rpm -e gpg-pubkey-7a05af82* 2>/dev/null || true
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

Refresh package metadata.

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

## Previous repository locations

The current Arm Toolchains Linux repositories at [https://developer.arm.com/packages/arm-toolchains/](https://developer.arm.com/packages/arm-toolchains/) replace the earlier repository structure that was based on repositories built using the SUSE Open Build Service.

Earlier repositories were published under the top-level package URL [https://developer.arm.com/packages/](https://developer.arm.com/packages/) and used repository prefixes such as:

```output
ACfL:<distro>
arm-toolchains:<distro>
```

These earlier repositories are deprecated but will continue to work until further notice.

Do not configure new systems to use the deprecated `ACfL:` or `arm-toolchains:` repository paths. Existing users should migrate to the current Arm Toolchains Linux repositories and install the current `arm-toolchains-repository` package.

The deprecated repositories will be removed in a future update.

## Summary

The Arm Toolchains Linux repositories provide a native package manager based installation channel for Arm Toolchain for Linux and Arm Performance Libraries on supported Linux hosts.

To use the repositories, install `arm-toolchains-repository` version `2-2` or later for your Linux distribution. This package configures the repository and installs the current repository signing key.

Use only the current Arm Toolchains Linux repositories at [https://developer.arm.com/packages/arm-toolchains/](https://developer.arm.com/packages/arm-toolchains/).

Do not use the deprecated top-level `ACfL:` or `arm-toolchains:` repository paths for new installations.
