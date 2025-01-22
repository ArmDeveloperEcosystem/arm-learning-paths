---
title: "Build options for multi-architecture container images"

weight: 2

layout: "learningpathall"
---

## How can I build multi-architecture container images?

Building multi-architecture container images for complex projects is challenging.

There are two common ways to build multi-architecture images, and both are explained in [Learn how to use Docker](/learning-paths/cross-platform/docker/).

### Use instruction emulation

The first method uses instruction emulation. You can learn about this method in [Build multi-architecture images with Docker buildx](/learning-paths/cross-platform/docker/buildx/). The drawback of emulation is slow performance, especially for complex builds which involve tasks such as compiling large C++ applications. 

### Use a manifest and multiple computers

The second method uses multiple computers, one for each architecture, and joins the images to create a multi-architecture image using Docker manifest. You can learn about this method in [Use Docker manifest to create multi-architecture images](/learning-paths/cross-platform/docker/manifest/). The drawback of the manifest method is its complexity as it requires multiple systems.

### Arm-hosted runners

Arm-hosted runners from GitHub provide a way to create multi-architecture images with higher performance and lower complexity compared to the two methods described above. 

When you use Arm-hosted runners, you don't need to worry about self-hosting (managing servers) or instruction emulation (slow performance).
