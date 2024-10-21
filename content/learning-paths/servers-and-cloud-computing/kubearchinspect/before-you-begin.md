---
title: Install KubeArchInspect
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

{{% notice Note %}}
KubeArchInspect is a command-line tool which requires a running Kubernetes cluster.

Make sure you can connect to your Kubernetes cluster using `kubectl`. 
{{% /notice %}}

## How do I install KubeArchInspect?

For Arm Linux, download the KubeArchInspect package from GitHub:

```console
wget https://github.com/ArmDeveloperEcosystem/kubearchinspect/releases/download/v0.2.0/kubearchinspect_Linux_arm64.tar.gz
```

Extract the files from the release package:

```console
tar xvfz kubearchinspect_Linux_arm64.tar.gz
```

The `kubearchinspect` binary is now in the current directory. 

If you are using a different platform, such as Windows or macOS, you can get other release packges from the [GitHub releases area](https://github.com/ArmDeveloperEcosystem/kubearchinspect/releases/).

You can run `kubearchinspect` from the current location or copy it to a directory in your search path such as `/usr/local/bin`.

## How do I verify KubeArchInspect is installed?

Confirm KubeArchInspect works correctly by running the `kubearchinspect` command: 

```console
./kubearchinspect images --help
```

If KubeArchInspect is working correctly, the usage message is displayed:

```output
Check which images in your cluster support arm64.

Usage:
  kubearchinspect images [flags]

Flags:
  -d, --debug   Enable debug mode
  -h, --help    help for images
```

You are now ready to use KubeArchInspect.