---
title: Installing Go and Sweet
weight: 40

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Installing dependencies
```bash
#!/usr/bin/env bash
set -euo pipefail

sudo apt-get -y update
sudo apt-get -y install git build-essential


# Detect architecture
ARCH=$(uname -m)
case "$ARCH" in
  arm64|aarch64)
    GO_PKG="go1.24.2.linux-arm64.tar.gz"
    ;;
  x86_64|amd64)
    GO_PKG="go1.24.2.linux-amd64.tar.gz"
    ;;
  *)
    echo "Unsupported architecture: $ARCH"
    exit 1
    ;;
esac

# Download and install architecture-specific Go environments

URL="https://go.dev/dl/${GO_PKG}"
echo "Downloading $URL..."
wget -q --show-progress "$URL"

echo "Extracting $GO_PKG to /usr/local..."
sudo tar -C /usr/local -xzf "$GO_PKG"


echo "Go 1.24.2 installed successfully for $ARCH."

export GOPATH=$HOME/go
export GOBIN=$GOPATH/bin
export PATH=$PATH:$GOBIN:/usr/local/go/bin

# Install Sweet, benchmarks, and benchstat tools
go install golang.org/x/benchmarks/sweet/cmd/sweet@latest
go install golang.org/x/perf/cmd/benchstat@latest

git clone https://github.com/golang/benchmarks
cd benchmarks/sweet
sweet get -force # to get assets

# Create a configuration file

cat <<EOF > config.toml
[[config]]
  name = "go-time-config"
  goroot = "/usr/local/go"

EOF

# Run the benchmarks
sweet run -count 10 -run="etcd" config.toml # run one, 1X

```

Before we can run the benchmarks, we need to install the required packages and runtimes:
1. Install apt packages
2. Install Go
3. Set up the Go environment
4. Install the Sweet CLI
5. clone Benchmarks
6. Create a configuration file
7. Run the benchmarks
8. Compare the results
9. 

# Go Benchmarking Learning Path: Automated Setup with Bash

In this learning path, you’ll walk through a Bash script that automates the installation of Go 1.24.2, the Sweet multi-node benchmark runner, and the Benchstat comparison tool. Each section corresponds to a phase in the script, from detecting architecture to running your first benchmark run.

---

## Step 1: Detect Architecture

The script begins by determining your machine’s CPU architecture:

```bash
ARCH=$(uname -m)
case "$ARCH" in
  arm64|aarch64)  GO_PKG="go1.24.2.linux-arm64.tar.gz"  ;;
  x86_64|amd64)   GO_PKG="go1.24.2.linux-amd64.tar.gz" ;;
  *) echo "Unsupported architecture: $ARCH"; exit 1 ;;
esac
```

## Download and set arch-specific Go and environment

```bash
URL="https://go.dev/dl/${GO_PKG}"
wget -q --show-progress "$URL"
sudo tar -C /usr/local -xzf "$GO_PKG"

export GOPATH=$HOME/go
export GOBIN=$GOPATH/bin
export PATH=$PATH:$GOBIN:/usr/local/go/bin
```

## Install Sweet, Benchmarks, and Benchstat Tools

With Go in place, install the performance tools:

```bash
go install golang.org/x/benchmarks/sweet/cmd/sweet@latest
go install golang.org/x/perf/cmd/benchstat@latest

git clone https://github.com/golang/benchmarks
cd benchmarks/sweet
sweet get -force
```

## Create a Configuration File

Sweet requires a TOML config to know what and where to run. Create a minimal config file:

```bash
cat <<EOF > config.toml
[[config]]
  name = "go-time-config"
  goroot = "/usr/local/go"
EOF
```




# All at once

```bash
#!/usr/bin/env bash
set -euo pipefail

sudo apt-get -y update
sudo apt-get -y install git build-essential

# Detect architecture
ARCH=$(uname -m)
case "$ARCH" in
  arm64|aarch64)
    GO_PKG="go1.24.2.linux-arm64.tar.gz"
    ;;
  x86_64|amd64)
    GO_PKG="go1.24.2.linux-amd64.tar.gz"
    ;;
  *)
    echo "Unsupported architecture: $ARCH"
    exit 1
    ;;
esac

# Download and install architecture-specific Go environments

URL="https://go.dev/dl/${GO_PKG}"
echo "Downloading $URL..."
wget -q --show-progress "$URL"

echo "Extracting $GO_PKG to /usr/local..."
sudo tar -C /usr/local -xzf "$GO_PKG"

echo "Go 1.24.2 installed successfully for $ARCH."

export GOPATH=$HOME/go
export GOBIN=$GOPATH/bin
export PATH=$PATH:$GOBIN:/usr/local/go/bin

# Install Sweet, benchmarks, and benchstat tools
go install golang.org/x/benchmarks/sweet/cmd/sweet@latest
go install golang.org/x/perf/cmd/benchstat@latest

git clone https://github.com/golang/benchmarks
cd benchmarks/sweet
sweet get -force # to get assets

# Create a configuration file

cat <<EOF > config.toml
[[config]]
  name = "go-time-config"
  goroot = "/usr/local/go"

EOF

# Run the benchmarks
sweet run -count 10 -run="etcd" config.toml # run one, 1X

```