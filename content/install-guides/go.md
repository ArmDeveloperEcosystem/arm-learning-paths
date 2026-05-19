---
additional_search_terms:
- linux
- cloud
layout: installtoolsall
minutes_to_complete: 10
author: Jason Andrews
multi_install: false
multitool_install_part: false
official_docs: https://go.dev/doc/
description: Install the Go programming language on Arm Linux (aarch64) and verify the installation by printing the installed version.
ecosystem_dashboard: https://developer.arm.com/ecosystem-dashboard/linux?package=golang
test_images:
- ubuntu:latest
test_maintenance: true
title: Go
tool_install: true
weight: 1
---

[Go](https://go.dev/) is an open source programming language that's available for a variety of operating systems and Linux distributions. 

There are multiple ways to install Go. In this guide, you'll learn how to install Go for Ubuntu on Arm.

## Before you begin

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The output is similar to:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

## Download and install Go

The easiest way to install Go for Ubuntu on Arm is to download a release, extract it, and set up your `PATH` environment variable. To download and install Go, follow these steps:

{{% notice Note %}}
The following commands use Go version 1.24.5. The same commands work with other versions. Replace the file used in these steps with the file for your version of choice. To find the latest version of Go, see [All releases](https://go.dev/dl/).
{{% /notice %}}

1. Download a Go release:

```bash { target="ubuntu:latest" }
wget https://go.dev/dl/go1.24.5.linux-arm64.tar.gz
```

2. Extract the release to `/usr/local/go`:

```bash { target="ubuntu:latest" }
sudo tar -C /usr/local -xzf ./go1.24.5.linux-arm64.tar.gz
```

3. Add the path to `go` in your `.bashrc` file:

```bash { target="ubuntu:latest" }
echo 'export PATH="$PATH:/usr/local/go/bin"' >> ~/.bashrc
source ~/.bashrc
```

## Verify Go installation

Confirm `go` is installed by printing the version:

```bash { target="ubuntu:latest" env_source="~/.bashrc" } 
go version
```

The output is similar to:

```output
go version go1.24.5 linux/arm64
```

## Next steps

You are now ready to use the Go programming language on your Arm machine running Ubuntu. You can explore Learning Paths for working with Go on Arm, such as [Deploy Golang on Azure Cobalt 100 on Arm](/learning-paths/servers-and-cloud-computing/golang-on-azure/) and [Benchmark Go performance with Sweet and Benchstat](/learning-paths/servers-and-cloud-computing/go-benchmarking-with-sweet/).
