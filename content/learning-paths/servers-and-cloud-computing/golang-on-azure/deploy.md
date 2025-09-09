---
title: Install Golang
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Install Golang on Ubuntu Pro 24.04 LTS (Arm64)
This section covers installing the latest Golang version on **Ubuntu Pro 24.04 LTS Arm64**, configuring the environment, and verifying the setup.

1. Download the Golang archive

This command downloads the official Golang package for Linux Arm64 from the Golang website.

```console
wget https://go.dev/dl/go1.25.0.linux-arm64.tar.gz
```
{{% notice Note %}}
There are many enhancements added to Golang version 1.18, that has resulted in up to a 20% increase in performance for Golang workloads on Arm-based servers. Please see [this reference content](https://aws.amazon.com/blogs/compute/making-your-go-workloads-up-to-20-faster-with-go-1-18-and-aws-graviton/) for the details.

The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) also recommends Golang version 1.18 as the minimum recommended on the Arm platforms.
{{% /notice %}}

2. Extract the archive into `/usr/local`

This unpacks the Golang files into the system directory /usr/local, which is a standard place for system-wide software.

```console
sudo tar -C /usr/local -xzf ./go1.25.0.linux-arm64.tar.gz
```

3. Add Golang to your system PATH

This updates your .bashrc file so your shell can recognize the Golang command from anywhere.

```console
echo 'export PATH="$PATH:/usr/local/go/bin"' >> ~/.bashrc
```

4. Apply the PATH changes immediately

This reloads your .bashrc so you don’t need to log out and log back in for the changes to take effect.

```console
source ~/.bashrc
```

5. Verify Golang installation

This checks if Golang is installed correctly and shows the installed version.

```console
go version
```

You should see an output similar to: 

```output
go version go1.25.0 linux/arm64
```
6. Check Golang environment settings

This displays Golang’s environment variables (like GOROOT and GOPATH) to ensure they point to the correct installation.

```console
go env
```

You should see an output similar to: 

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
Golang installation on Ubuntu Pro 24.04 LTS Arm64 is complete. You can now proceed with Golang development or baseline testing.
