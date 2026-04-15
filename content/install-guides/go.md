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
ecosystem_dashboard: https://developer.arm.com/ecosystem-dashboard/linux?package=golang
test_images:
- ubuntu:latest
test_maintenance: true
title: Go
tool_install: true
weight: 1
---

[Go](https://go.dev/) is an open source programming language. It is available for a variety of operating systems and Linux distributions. 

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

The easiest way to install Go for Ubuntu on Arm is to download a release, extract it, and set up your `PATH` environment variable. To do so, follow these steps:

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

The output should print the version and is similar to:

```output
go version go1.24.5 linux/arm64
```

You are now ready to use the Go programming language on your Arm machine running Ubuntu.
