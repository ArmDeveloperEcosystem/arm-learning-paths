---
title: Check C2PA Tool and prepare the sample image
description: Check C2PA Tool on your Arm device, download the sample JPEG, and confirm that it has no C2PA manifest before signing.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create a working directory

Create a folder named `c2pa-demo` wherever you keep your projects, using your file manager or terminal.
Open a terminal in that folder and run the remaining commands there. Keep all files from this
Learning Path in the same folder so the commands can use their filenames without full paths.

## Confirm C2PA Tool is available

Run the platform-independent version check:

```console
c2patool --version
```

The version number depends on the current stable release. All subsequent outputs in this Learning
Path were recorded using the following version:

```output
c2patool 0.27.21
```

If the command is unavailable, follow the [C2PA Tool install guide](/install-guides/c2patool/).

## Download the sample image

In a real-world workflow, the software that creates or modifies a digital asset adds Content
Credentials as part of that process. For example, when you take a photograph with a camera that
supports Content Credentials, the camera software signs the image and adds Content Credentials
during capture.

To focus on signing and validation without setting up a camera, use the
[sample JPEG from the Content Authenticity Initiative's `contentauth/c2patool` repository, pinned to `v0.27.20`](https://github.com/contentauth/c2patool/blob/v0.27.20/sample/image.jpg).
For this exercise, assume the sample represents a digitally captured photograph whose capture
details are available to the camera software when it adds Content Credentials.

Download the original JPEG from that GitHub page and save it as `image.jpg` in your `c2pa-demo`
working directory. If your browser displays the raw image, use **Save image as**. The file is
61,720 bytes. Keep this unsigned source file for the later steps.

The upstream sample is provided under the [MIT license, © Copyright 2020 Adobe](https://github.com/contentauth/c2patool/blob/v0.27.20/LICENSE-MIT).
Retain its copyright and permission notice if you redistribute the image.

## Confirm the starting state

Use C2PA Tool to confirm that the source image does not already contain a manifest:

```console
c2patool image.jpg --info
```

The expected output includes:

```output
No C2PA Manifests. (file size = 61720)
```

The downloaded sample has no existing C2PA manifest, so you can use it as the unsigned source for the
next step.

Next, you will add Content Credentials to the image.
