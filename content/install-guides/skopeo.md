---
title: Skopeo
author_primary: Jason Andrews
minutes_to_complete: 10
official_docs: https://github.com/containers/skopeo

additional_search_terms:
- containers
- images
- registry

layout: installtoolsall
multi_install: false
multitool_install_part: false
test_images:
- ubuntu:latest
test_maintenance: false
tool_install: true
weight: 1
---

Skopeo is a command-line utility that performs various operations on container images and image repositories. It does not require a daemon to be running on your computer. 

This article explains how to install Skopeo for Ubuntu on Arm.

Skopeo is available for Windows, macOS, and Linux and supports the Arm architecture. See [Installing Skopeo](https://github.com/containers/skopeo/blob/main/install.md) for further information about other operating systems and architectures.

## What should I consider before installing Skopeo on Arm?

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The output should be:
```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

## How do I download and Install Skopeo for Ubuntu on Arm?

The easiest way to install Skopeo is to use the package manager:

```bash
sudo apt update
sudo apt install -y skopeo
```

Confirm the installation by checking the version:

```bash
skopeo --version
```

To see the help message use this command:

```bash
skopeo --help
```

The output that you will see should be:

```output
Various operations with container images and container image registries

Usage:
  skopeo [flags]
  skopeo [command]

Available Commands:
  copy                                          Copy an IMAGE-NAME from one location to another.
  delete                                        Delete image IMAGE-NAME.
  generate-sigstore-key                         Generate a sigstore public/private key pair.
  help                                          Help about any command.
  inspect                                       Inspect image IMAGE-NAME.
  list-tags                                     List tags in the transport/repository specified by the SOURCE-IMAGE.
  login                                         Log in to a container registry.
  logout                                        Log out of a container registry.
  manifest-digest                               Compute a manifest digest of a file.
  standalone-sign                               Create a signature using local files.
  standalone-verify                             Verify a signature using local files.
  sync                                          Synchronize one or more images from one location to another.

Flags:
      --command-timeout duration   Timeout for the command execution.
      --debug                      Enable debug output.
  -h, --help                       Help for skopeo.
      --insecure-policy            Run the tool without any policy check.
      --override-arch ARCH         Use ARCH instead of the architecture of the machine for choosing images.
      --override-os OS             Use OS instead of the running OS for choosing images.
      --override-variant VARIANT   Use VARIANT instead of the running architecture variant for choosing images.
      --policy string              Path to a trust policy file.
      --registries.d DIR           Use registry configuration files in DIR (for example, for container signature storage).
      --tmpdir string              Directory used to store temporary files.
  -v, --version                    Version for Skopeo.

Use "skopeo [command] --help" for more information about a command.
```

## How do I get started with Skopeo?

You can use the commands listed below to get you started with Skopeo.

### How can I check if a container image supports Arm?

To find out if an image is multi-architecture, including Arm, you can inspect the image's manifest.

For example, to check if the dev container available for creating Arm Learning Paths supports the Arm architecture, run:

```bash
skopeo inspect --raw docker://docker.io/armswdev/learn-dev-container:latest | jq '.manifests[] | select(.platform.architecture == "arm64")'
```

The output is similar to:

```output
{
  "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
  "size": 1574,
  "digest": "sha256:b7abfdc06d4cb06dfbb644f0d7c50202f99f83298da7903ea6463de23b55fb10",
  "platform": {
    "architecture": "arm64",
    "os": "linux"
  }
}
```

If the command returns a result for an image, the image supports the `arm64` architecture.

### How can I check if a container image supports multiple architectures?

To find out if an image supports both `arm64` and `amd64` architectures, you can inspect the image's manifest for both architectures.

For example, to check if the same dev container supports both architectures run:

```bash
skopeo inspect --raw docker://docker.io/armswdev/learn-dev-container:latest | jq '.manifests[] | select(.platform.architecture == "arm64" or .platform.architecture == "amd64")'
```

The output confirms that both `arm64` and `amd64` are supported architectures as shown below:

```output
{
  "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
  "size": 1574,
  "digest": "sha256:15fe2dc0925c6e5da27048edcd034660f51216ad700cb7cf12cb7779c16e9bce",
  "platform": {
    "architecture": "amd64",
    "os": "linux"
  }
}
{
  "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
  "size": 1574,
  "digest": "sha256:b7abfdc06d4cb06dfbb644f0d7c50202f99f83298da7903ea6463de23b55fb10",
  "platform": {
    "architecture": "arm64",
    "os": "linux"
  }
}
```

## What are some other uses for Skopeo?

Copy an image from a registry to a local directory. This command is similar to `docker pull` and copies the image from the remote registry to your local directory.

```bash
skopeo copy docker://docker.io/armswdev/uname:latest dir:./uname
```

The output is:

```output
Getting image source signatures
Copying blob cd741b12a7ea done   |
Copying config d11135df72 done   |
Writing manifest to image destination
```

Inspect an image in a remote registry:

```bash
skopeo inspect docker://docker.io/armswdev/uname:latest
```

The output is:

```output
{
    "Name": "docker.io/armswdev/uname",
    "Digest": "sha256:4f1fe1e1e1ad179bb2cec6b3c8b458d6ead02bd7459798a357791353b867462d",
    "RepoTags": [
        "latest"
    ],
    "Created": "2023-03-08T04:32:41.063980445Z",
    "DockerVersion": "",
    "Labels": {
        "org.opencontainers.image.ref.name": "ubuntu",
        "org.opencontainers.image.version": "22.04"
    },
    "Architecture": "arm64",
    "Os": "linux",
    "Layers": [
        "sha256:cd741b12a7eaa64357041c2d3f4590c898313a7f8f65cd1577594e6ee03a8c38"
    ],
    "LayersData": [
        {
            "MIMEType": "application/vnd.oci.image.layer.v1.tar+gzip",
            "Digest": "sha256:cd741b12a7eaa64357041c2d3f4590c898313a7f8f65cd1577594e6ee03a8c38",
            "Size": 27347481,
            "Annotations": null
        }
    ],
    "Env": [
        "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
    ]
}
```

List tags in a remote registry for the Ubuntu image with many tags:

```bash
skopeo list-tags docker://docker.io/library/ubuntu
```

The partial output is:

```output
{
    "Repository": "docker.io/library/ubuntu",
    "Tags": [
        "10.04",
        "12.04",
        "12.04.5",
        "12.10",
        "13.04",
        "13.10",
        "14.04",
        "14.04.1",
        "14.04.2",
        "14.04.3",
        "14.04.4",
        "14.04.5",
        "14.10",
        "15.04",
        "15.10",
        "16.04",
        "16.10",
        "17.04",
        "17.10",
        "18.04",
        "18.10",
        "19.04",
        "19.10",
        "20.04",
        "20.10",
        "21.04",
        "21.10",
        "22.04",
        "22.10",
        "23.04",
        "23.10",
        "24.04",
        "24.10",
        "25.04",
< many more tag with Ubuntu release names omitted>
```

You are ready to use Skopeo for your projects.
