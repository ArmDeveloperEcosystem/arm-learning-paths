---
title: libjpeg-turbo
description: Install libjpeg-turbo on macOS, Linux on Arm, or Windows on Arm to encode, decode, and transform JPEG images.
minutes_to_complete: 10
official_docs: https://libjpeg-turbo.org/Documentation/Documentation
author: Kostiantyn Perehuda

draft: true

test_maintenance: false

### FIXED, DO NOT MODIFY
weight: 1
tool_install: true
multi_install: false
multitool_install_part: false
layout: installtoolsall
---

## Overview

[libjpeg-turbo](https://www.libjpeg-turbo.org/) provides JPEG encoding and decoding libraries and
command-line tools. The tools include `cjpeg` for encoding, `djpeg` for decoding, and `jpegtran`
for transforming JPEG images.

You can install the tools on macOS on Apple silicon, 64-bit Arm Linux, or Windows on Arm.
Package-manager commands on macOS and Linux install the version available from your package source.

## Install on macOS

Install [Homebrew](https://brew.sh/) if it isn't already available, then install the
[jpeg-turbo package](https://formulae.brew.sh/formula/jpeg-turbo):

```console
brew install jpeg-turbo
```

## Install on Arm Linux

On Ubuntu and Debian, install the `libjpeg-turbo-progs` package:

```console
sudo apt update
sudo apt install libjpeg-turbo-progs
```

On Fedora, install the [libjpeg-turbo-utils package](https://packages.fedoraproject.org/pkgs/libjpeg-turbo/libjpeg-turbo-utils/):

```console
sudo dnf install libjpeg-turbo-utils
```

Both packages provide `jpegtran` and the other command-line tools. Installing only the JPEG
runtime library doesn't provide these tools.

## Install on Windows on Arm

{{% notice Note %}}
The following steps use libjpeg-turbo version 3.1.4.1. You can use another version that provides
a native ARM64 installer. Replace the installer with the file for your chosen version.
To find the latest version, see [libjpeg-turbo releases](https://github.com/libjpeg-turbo/libjpeg-turbo/releases).
{{% /notice %}}

1. Download `libjpeg-turbo-3.1.4.1-vc-arm64.exe` from the
   [libjpeg-turbo 3.1.4.1 release](https://github.com/libjpeg-turbo/libjpeg-turbo/releases/tag/3.1.4.1).
2. Run the installer and note the installation directory.
3. Add the installation's `bin` directory, containing `jpegtran.exe`, to your user's `Path`
   environment variable.
4. Open a new PowerShell window so it picks up the change.

## Verify the installation

Print the installed version:

```console
jpegtran -version
```

The output is similar to:

```output
libjpeg-turbo version 3.1.4.1 (build 20260327)
```

Your version and build can differ. A successful version check confirms that your terminal can
find and run `jpegtran`.

## Troubleshooting

If your shell can't find `jpegtran`, open a new terminal and confirm that the directory containing the
executable is in your `PATH`. On Windows, check for `jpegtran.exe` in the installation's `bin`
directory. On Linux, check that you installed the command-line tools package for your distribution.

If Ubuntu cannot locate the package, check that the `universe` repository is enabled for your
release, then run `sudo apt update` again.
