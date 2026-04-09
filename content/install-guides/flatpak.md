---
title: "Flatpak"
minutes_to_complete: 10
official_docs: "https://flatpak.org"
author: "Jason Andrews"
description: "Install Flatpak on Arm Linux, add the Flathub remote, and verify the setup by running a native aarch64 application."
weight: 1
draft: true
tool_install: true
layout: installtoolsall
multi_install: false
multitool_install_part: false
---

Flatpak is a framework for distributing Linux applications. It provides distribution-agnostic packaging and a sandboxed runtime, so the same application bundle runs on Ubuntu, Fedora, Arch, and openSUSE without repackaging. [Flathub](https://flathub.org/) is the primary community-maintained repository of Flatpak applications, many of which publish native Arm builds.

## How does Flatpak sandboxing work?

Each Flatpak application runs inside an isolated environment built on three Linux kernel features: namespaces, seccomp, and cgroups. Namespaces give the application its own view of the filesystem, network, and process tree. Seccomp filters restrict the system calls the application can make. Together, these mechanisms prevent an application from reading files outside its sandbox or interfering with other processes on the host.

The sandbox is implemented by [bubblewrap](https://github.com/containers/bubblewrap), a low-level sandboxing tool that Flatpak calls at launch time. Applications declare the permissions they need, such as access to the home directory, the network, or audio devices, in a manifest. You can inspect and override these permissions using `flatpak override`.

## How are Flatpak applications packaged?

A Flatpak application is distributed as an OSTree commit, a content-addressed filesystem tree stored in a local repository. When you install an application, Flatpak fetches only the changed objects from the remote, similar to how Git fetches commits. This makes updates efficient even for large applications.

Applications either bundle their own libraries directly or declare runtime dependencies, such as `org.freedesktop.Platform` or `org.gnome.Platform`. The runtime provides a consistent base set of libraries, such as libc and GTK, that multiple applications can share on disk, reducing total storage. The application and its runtime are kept separate from the host system libraries, which means you don't need to resolve conflicts.

For Arm developers, the key advantage is that Flatpak applications can publish separate builds for `x86_64` and `aarch64` under the same application ID. Flatpak selects the correct architecture automatically at install time.

## How does Flatpak compare to Linux package managers?

Linux package managers like `apt`, `dnf`, and `pacman` are tightly coupled to the distribution release cycle. An application packaged for Ubuntu 24.04 may lag the upstream version, and some applications aren't packaged for every Linux distribution. Flatpak addresses this by letting upstream developers publish and maintain their own builds directly on Flathub. This allows you to get the current release of an application on any supported Linux distribution.

Because a Flatpak application bundles its own libraries or pins a specific runtime version, installing or updating it can't conflict with host system libraries or break other packages. A distro upgrade won't silently change the libraries an application links against. This also means you can run two different applications that require incompatible versions of the same library side by side without issues.

The instructions below cover installing Flatpak on Arm Linux (aarch64), adding the Flathub remote, and verifying the installation by installing VSCodium.

## Before you begin

Confirm your system is running a 64-bit Arm Linux distribution:

```bash
uname -m
```

The output should be:

```output
aarch64
```

## How do I install Flatpak?

### Ubuntu or Debian

Update your package lists and install Flatpak:

```bash
sudo apt update
sudo apt install -y flatpak
```

### Fedora

Install Flatpak using DNF:

```bash
sudo dnf install -y flatpak
```

### Arch or Manjaro

Sync the package database and install Flatpak:

```bash
sudo pacman -S --noconfirm flatpak
```

### openSUSE

Refresh the repository metadata and install Flatpak:

```bash
sudo zypper refresh
sudo zypper install -y flatpak
```

After installing, log out and back in to ensure desktop integration works correctly.

## Verify Flatpak is installed

Confirm Flatpak is available and check the version:

```bash
flatpak --version
```

The output will look similar to:

```output
Flatpak 1.16.1
```

## How do I add the Flathub remote?

Add the Flathub repository as a remote source:

```bash
sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

Confirm the remote was added:

```bash
flatpak remotes
```

The output should include a line for `flathub`:

```output
Name    Options
flathub system
```

## How do I install the VSCodium Flatpak?

[VSCodium](https://vscodium.com/) is the telemetry-free build of VS Code, available on Flathub with a native Arm build, making it a useful application to test. 

Install it with the `--assumeyes` flag, which automatically answers yes to any prompts during installation:

```bash
flatpak install --assumeyes flathub com.vscodium.codium
```

Confirm the installation and check the architecture:

```bash
flatpak info com.vscodium.codium
```

The output includes the runtime architecture:

```output
VSCodium - Telemetry-less code editing

          ID: com.vscodium.codium
         Ref: app/com.vscodium.codium/aarch64/stable
        Arch: aarch64
      Branch: stable
     Version: 1.112.01907
     License: MIT
      Origin: flathub
  Collection: org.flathub.Stable
Installation: system
   Installed: 500.4 MB
     Runtime: org.freedesktop.Sdk/aarch64/25.08
         Sdk: org.freedesktop.Sdk/aarch64/25.08

      Commit: 941b853cf7e254f628e79549ff39b2940faeb11a0c022485507ee83af7d1ffb9
      Parent: 8bf491c5bb50857418982dea2cf3a78ca127e888f8055332cf11650ab7472b99
     Subject: fix: :fire: Remove urls to fix all the appstream validationwarnings (92763b676197)
        Date: 2026-03-30 05:03:53 +0000
```

The `Arch: aarch64` line confirms a native Arm build is installed.

To start VSCodium on the project in your current directory, run:

```bash
flatpak run com.vscodium.codium . &
```

You can also create an alias to make it easier:

```bash
alias codium='flatpak run com.vscodium.codium'
```

Now, run using the alias:

```bash
codium . &
```

## What are some other useful Flatpak commands? 

If an installation becomes corrupted or incomplete, run `flatpak repair` to check your local Flatpak installation and fix any inconsistencies:

```bash
flatpak repair
```

To update all installed Flatpak applications and runtimes to their latest versions, run:

```bash
flatpak update
```

To inspect the sandbox permissions granted to an application, run:

```bash
flatpak info --show-permissions com.vscodium.codium
```

To open an interactive shell inside an application's sandbox, which is useful for debugging permission or runtime issues, run:

```bash
flatpak run --command=bash com.vscodium.codium
```

Note that not all applications include `bash` in their sandbox, so this command may not work for every Flatpak. Your shell prompt may not look any different, but you are in the sandbox. To confirm run:

```bash 
ls /app
cat /etc/os-release
```

The output is similar to:

```output
bin  lib  manifest-base-1.json  manifest.json  share  tools
NAME="Freedesktop SDK"
VERSION="25.08 (Flatpak runtime)"
VERSION_ID=25.08
ID=org.freedesktop.platform
PRETTY_NAME="Freedesktop SDK 25.08 (Flatpak runtime)"
BUG_REPORT_URL=https://gitlab.com/freedesktop-sdk/freedesktop-sdk/issues
```

The `/app` directory contains the application runtime files, and the `os-release` file shows the Flatpak runtime rather than the host OS. 

## How can I find Arm-native applications on Flathub?

Flatpak makes it straightforward to discover which applications support aarch64. Visit the [Flathub app browser](https://flathub.org/apps) and filter by architecture to find applications with native Arm builds. You can also search from the command line after adding the Flathub remote:

```bash
flatpak remote-ls --app --arch=aarch64 flathub
```

This lists every application on Flathub that publishes a native aarch64 build. Use `grep` to narrow results by name or category.

## Uninstall

To remove VSCodium, run:

```bash
flatpak uninstall --assumeyes com.vscodium.codium
```

To remove the Flathub remote, run:

```bash
sudo flatpak remote-delete flathub
```
