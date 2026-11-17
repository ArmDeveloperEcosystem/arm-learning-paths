---
title: ExifTool
description: Install ExifTool on macOS, Linux on Arm, or Windows on Arm to read and write media metadata from the command line.
minutes_to_complete: 10
official_docs: https://exiftool.org/install.html
author: Kostiantyn Perehuda

test_maintenance: false

### FIXED, DO NOT MODIFY
weight: 1
tool_install: true
multi_install: false
multitool_install_part: false
layout: installtoolsall
---

[ExifTool](https://exiftool.org/) reads and writes metadata in image, audio, and video files.
You can install ExifTool on macOS on Apple silicon, 64-bit Arm Linux, or Windows 11 on Arm.
On Windows on Arm, you'll use the Windows x64 executable under emulation.

Package-manager commands install the version available from your package source. For current releases, see the
[ExifTool download page](https://exiftool.org/).

## Install on macOS

Install [Homebrew](https://brew.sh/) if it isn't already available, then install ExifTool:

```console
brew install exiftool
```

## Install on Arm Linux

On Ubuntu and Debian, install the `libimage-exiftool-perl` package:

```console
sudo apt update
sudo apt install libimage-exiftool-perl
```

On Fedora, install the [perl-Image-ExifTool package](https://packages.fedoraproject.org/pkgs/perl-Image-ExifTool/perl-Image-ExifTool/):

```console
sudo dnf install perl-Image-ExifTool
```

Both packages provide the `exiftool` command and its Perl dependencies.

## Install on Windows 11 on Arm

The Windows x64 executable runs through
[x64 application emulation on Windows 11 on Arm](https://learn.microsoft.com/en-us/windows/arm/apps-on-arm-x86-emulation).

Follow the [official Windows installation instructions](https://exiftool.org/install.html#Windows):

1. Download the **64-bit Windows Executable** ZIP from the [ExifTool download page](https://exiftool.org/).
2. Extract the archive and open the extracted folder containing `exiftool(-k).exe`.
3. In File Explorer, select **View > Show > File name extensions**, then rename `exiftool(-k).exe` to `exiftool.exe`.
4. Move `exiftool.exe` and its accompanying `exiftool_files` folder into a permanent folder, such as `C:\Users\<username>\Tools\ExifTool`. Keep them together.
5. Search the **Start** menu for **Edit environment variables for your account** and open it. 
6. Under **User variables**, select **Path**, then select **Edit > New**. 
7. Add the full path to the folder directly containing `exiftool.exe`, such as `C:\Users\<username>\Tools\ExifTool`. Replace `<username>` with the name of your Windows user folder. 
8. Select **OK** to save and close the dialogs.
9. Open a new PowerShell window so that it picks up the change.

## Verify the installation

Print the installed version:

```console
exiftool -ver
```

The output is similar to:

```output
13.55
```

Your version can differ. List the available metadata tags to confirm that ExifTool runs:

```console
exiftool -list
```

The output begins with `Available tags:` followed by tag names.

## Troubleshoot installation issues

If your shell can't find `exiftool`, open a new terminal. Confirm that the directory containing
`exiftool` is in your `PATH`. On Windows, also check that the executable is named `exiftool.exe` and that `exiftool_files` is still beside it.

If Ubuntu can't locate the package, check that the `universe` repository is enabled for your Ubuntu
release. After checking, run `sudo apt update` again.

## Next steps

You can now use ExifTool to read and write media metadata on Arm.

For a Learning Path that involves using ExifTool, see [Create and verify C2PA Content Credentials on Arm](/learning-paths/embedded-and-microcontrollers/c2pa-on-arm/).
