---
title: Check C2PA Tool and prepare the sample image
description: Check C2PA Tool on your Arm device, download the sample JPEG, and confirm that it has no C2PA manifest before signing.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create a working directory

Use `bash` or `zsh` on Linux or macOS, or PowerShell on Windows. 

Open your terminal in the directory where you keep your projects, then create and enter a working directory:

```console
mkdir c2pa-demo
cd c2pa-demo
```

These commands create the `c2pa-demo` folder and make it the working directory of your terminal. If the
folder already exists, run only `cd c2pa-demo`. Run the remaining commands from this directory.
Keep all files from this Learning Path in the same folder. That way, the commands can use filenames
without full paths.

## Confirm C2PA Tool is available

Install the Coalition for Content Provenance and Authenticity (C2PA) Tool. For instructions, see the [C2PA Tool install guide](/install-guides/c2patool/).

Run the platform-independent version check:

```console
c2patool --version
```

The version number depends on the current stable release. All subsequent outputs in this Learning
Path were recorded using `c2patool` version `0.27.21`.

## Download the sample image

In a real-world workflow, the software that creates or modifies a digital asset adds Content
Credentials as part of that process. For example, when you take a photograph with a camera that
supports Content Credentials, the camera software signs the image. It adds Content Credentials
during capture.

To focus on signing and validation without setting up a camera, you can use a sample JPEG. For a sample JPEG, refer to the
[Content Authenticity Initiative `contentauth/c2patool` repository](https://github.com/contentauth/c2patool/blob/v0.27.20/sample/image.jpg), pinned to `v0.27.20`.

Assume that the sample represents a digitally captured photograph. The capture
details are available to the camera software when it adds Content Credentials.

From your `c2pa-demo` working directory, download the sample JPEG as `image.jpg` using `wget`:

```console
wget -O image.jpg https://raw.githubusercontent.com/contentauth/c2patool/v0.27.20/sample/image.jpg
```

The command saves the JPEG as `image.jpg`, replacing that file if it already exists. The URL points
to the raw image rather than the GitHub HTML page. The file is 61,720 bytes. Keep this unsigned
source file for the later steps.

The upstream sample is provided under the [MIT license, © Copyright 2020 Adobe](https://github.com/contentauth/c2patool/blob/v0.27.20/LICENSE-MIT).
Retain its copyright and permission notice if you redistribute the image.

## Confirm the starting state

Use C2PA Tool to confirm that the source image doesn't already contain a manifest:

```console
c2patool image.jpg --info
```

The expected output is:

```output
No C2PA Manifests. (file size = 61720)
```

The downloaded sample has no existing C2PA manifest, so you can use it as the unsigned source later.

## What you've accomplished and what's next

You've set up the C2PA Tool and downloaded a sample JPEG image from GitHub. You've also confirmed that the image has no existing C2PA manifest.

Next, you'll add Content Credentials to the sample image.
