---
title: Install and configure Golang on Azure Cobalt 100 Arm64

weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Golang on Azure Cobalt 100 

This section demonstrates how to install the Go programming language toolchain on Ubuntu Pro 24.04 LTS (Arm64), configure your development environment, and verify the setup for optimal performance on Azure Cobalt 100 virtual machines.

## Download the Official Go Distribution

Download the latest Arm64-optimized Go distribution directly from the official Go website. This ensures you get the best performance on Azure Cobalt 100 processors:

```console
wget https://go.dev/dl/go1.25.0.linux-arm64.tar.gz
```

{{% notice Note %}}
There are many enhancements added to Golang version 1.18, that have resulted in up to a 20% increase in performance for Golang workloads on Arm-based servers. For further information, see the AWS blog [Making your Go workloads up to 20% faster with Go 1.18 and AWS Graviton](https://aws.amazon.com/blogs/compute/making-your-go-workloads-up-to-20-faster-with-go-1-18-and-aws-graviton/).

The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) also recommends Golang version 1.18 as the minimum recommended on the Arm platforms.
{{% /notice %}}

## Extract the archive 

Unpack the downloaded archive into `/usr/local`, which is the conventional directory for installing system-wide software on Linux. This ensures the Go toolchain is available for all users and integrates cleanly with the system’s environment.

```console
sudo tar -C /usr/local -xzf ./go1.25.0.linux-arm64.tar.gz
```

## Add Go to your shell PATH

To make the Go toolchain accessible from any directory, add its binary location to your shell’s `PATH` environment variable. Updating your `.bashrc` file ensures this change persists across sessions:

```console
echo 'export PATH="$PATH:/usr/local/go/bin"' >> ~/.bashrc
```

## Reload shell configuration

Apply the environment changes to your current shell session without requiring a logout/login cycle:

```console
source ~/.bashrc
```

## Verify Go installation

Confirm that Go is properly installed and accessible:

```console
go version
```

Expected output for Azure Cobalt 100 Arm64:
```output
go version go1.25.0 linux/arm64
```

## Validate Go environment configuration


Use the following command to display Go’s environment variables and confirm that key paths (such as GOROOT and GOPATH) are correctly set:


```console
go env GOROOT GOPATH GOARCH GOOS
```

You should see output similar to: 

```output
AR='ar'
CC='gcc'
CGO_CFLAGS='-O2 -g'
CGO_CPPFLAGS=''
CGO_CXXFLAGS='-O2 -g'
CGO_ENABLED='1'
CGO_FFLAGS='-O2 -g'
CGO_LDFLAGS='-O2 -g'
CXX='g++'
GCCGO='gccgo'
GO111MODULE=''
GOARCH='arm64'
GOARM64='v8.0'
GOAUTH='netrc'
GOBIN=''
GOCACHE='/home/ubuntu/.cache/go-build'
GOCACHEPROG=''
GODEBUG=''
GOENV='/home/ubuntu/.config/go/env'
GOEXE=''
GOEXPERIMENT=''
GOFIPS140='off'
GOFLAGS=''
GOGCCFLAGS='-fPIC -pthread -Wl,--no-gc-sections -fmessage-length=0 -ffile-prefix-map=/tmp/go-build119388372=/tmp/go-build -gno-record-gcc-switches'
GOHOSTARCH='arm64'
GOHOSTOS='linux'
GOINSECURE=''
GOMOD='/dev/null'
GOMODCACHE='/home/ubuntu/go/pkg/mod'
GONOPROXY=''
GONOSUMDB=''
GOOS='linux'
GOPATH='/home/ubuntu/go'
GOPRIVATE=''
GOPROXY='https://proxy.golang.org,direct'
GOROOT='/usr/local/go'
GOSUMDB='sum.golang.org'
GOTELEMETRY='local'
GOTELEMETRYDIR='/home/ubuntu/.config/go/telemetry'
GOTMPDIR=''
GOTOOLCHAIN='auto'
GOTOOLDIR='/usr/local/go/pkg/tool/linux_arm64'
GOVCS=''
GOVERSION='go1.25.0'
GOWORK=''
PKG_CONFIG='pkg-config'
```
The Go installation on Ubuntu Pro 24.04 LTS (Arm64) VM is now complete and you are ready to proceed with Go application development, benchmarking, or performance tuning on Azure Cobalt 100 VMs.
