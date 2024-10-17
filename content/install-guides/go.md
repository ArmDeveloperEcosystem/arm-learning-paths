---
additional_search_terms:
- linux
- cloud


layout: installtoolsall
minutes_to_complete: 10
author_primary: Jason Andrews
multi_install: false
multitool_install_part: false
official_docs: https://go.dev/doc/
test_images:
- ubuntu:latest
test_maintenance: true
title: Go
tool_install: true
weight: 1
---

[Go](https://go.dev/) is an open source programming language. 

## Before you begin

Go is available for a variety of operating systems and Linux distributions and has multiple ways to install it. 

This article provides a quick solution to install Go for Ubuntu on Arm.

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The output should be:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

## Download and install

The easiest way to install Go for Ubuntu on Arm is to download a release, extract it, and setup your `PATH` environment variable. 

Download a Go release:

```bash { target="ubuntu:latest" }
wget https://go.dev/dl/go1.23.1.linux-arm64.tar.gz
```

Extract the release to `/usr/local/go`:

```bash { target="ubuntu:latest" }
sudo tar -C /usr/local -xzf ./go1.23.1.linux-arm64.tar.gz
```

Add the path to `go` in your `.bashrc` file. 

```bash { target="ubuntu:latest" }
echo 'export PATH="$PATH:/usr/local/go/bin"' >> ~/.bashrc
source ~/.bashrc
```

Confirm `go` is installed by printing the version:

```bash { target="ubuntu:latest" env_source="~/.bashrc" } 
go version
```

The output should print the version:

```output
go version go1.23.1 linux/arm64
```

You are ready to use the Go programming language on your Arm machine running Ubuntu.
