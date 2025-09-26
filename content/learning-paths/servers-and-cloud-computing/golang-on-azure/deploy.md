---
title: Install Golang
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Install Golang on Ubuntu Pro 24.04 LTS (Arm64)
This section guides you through installing the latest Go toolchain on Ubuntu Pro 24.04 LTS (Arm64), configuring the environment, and verifying the setup for benchmarking workloads on Azure Cobalt 100 VMs.

1. Download the Golang archive

Use the following command to download the latest Go release for Linux Arm64 directly from the official Go distribution site:

```console
wget https://go.dev/dl/go1.25.0.linux-arm64.tar.gz
```
{{% notice Note %}}
There are many enhancements added to Golang version 1.18, that have resulted in up to a 20% increase in performance for Golang workloads on Arm-based servers. Please see [this blog](https://aws.amazon.com/blogs/compute/making-your-go-workloads-up-to-20-faster-with-go-1-18-and-aws-graviton/) for the details.

The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) also recommends Golang version 1.18 as the minimum recommended on the Arm platforms.
{{% /notice %}}

2. Extract the archive 

Unpack the downloaded archive into `/usr/local`, which is the conventional directory for installing system-wide software on Linux. This ensures the Go toolchain is available for all users and integrates cleanly with the system’s environment.

```console
sudo tar -C /usr/local -xzf ./go1.25.0.linux-arm64.tar.gz
```

3. Add Go to your system PATH

To make the Go toolchain accessible from any directory, add its binary location to your shell’s PATH environment variable. Updating your `.bashrc` file ensures this change persists across sessions:

```console
echo 'export PATH="$PATH:/usr/local/go/bin"' >> ~/.bashrc
```

4. Apply the PATH changes immediately

After updating .bashrc, reload it so your current shell session picks up the new environment variables without requiring you to log out and back in:

```console
source ~/.bashrc
```

5. Verify Go installation

Check if Go is installed correctly and confirm the version:

```console
go version
```

You should see output similar to: 

```output
go version go1.25.0 linux/arm64
```
6. Check Go environment settings

Use the following command to display Go’s environment variables and confirm that key paths (such as GOROOT and GOPATH) are correctly set:

```console
go env
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
At this point, the Go installation on Ubuntu Pro 24.04 LTS (Arm64) VM is complete. You are now ready to proceed with Go application development, benchmarking, or performance tuning on Azure Cobalt 100 VMs.
