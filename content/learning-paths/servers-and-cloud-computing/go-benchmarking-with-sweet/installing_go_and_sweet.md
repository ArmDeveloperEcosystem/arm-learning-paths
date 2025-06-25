---
title: Installing Go and Sweet
weight: 40

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you'll install Go, Sweet, and the Benchstat comparison tool on both VMs.

## Installation Script

Sweet is a Go benchmarking tool that provides a standardized way to run performance tests across different systems. Benchstat is a companion tool that analyzes and compares benchmark results, helping you understand performance differences between systems. Together, these tools will allow you to accurately measure and compare Go performance on Arm and x86 architectures.


{{% notice Note %}}
Subsequent steps in the learning path assume you are running this script (installing) from your home directory (`$HOME`), resulting in the creation of a `$HOME/benchmarks/sweet` final install path. If you install elsewhere, you need to adjust the path accordingly when prompted to run the benchmark logic later in the Learning Path.
{{% /notice %}}


Start by copying and pasting the script below on **both** of your GCP VMs. This script checks the architecture of your running VM, installs the required Go package on your VM. It then installs sweet, benchmarks, and the benchstat tools.

**You don't need to run it after pasting**, just paste it into your home directory and press enter to install all needed dependencies: 

```bash
#!/usr/bin/env bash

# Write the install script to filesystem using a HEREDOC
cat <<'EOF' > install_go_and_sweet.sh

sudo apt-get -y update
sudo apt-get -y install git build-essential

# Detect architecture - this allows the same script to work on both
# our Arm (c4a) and x86 (c4) VMs without modification
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
sweet get # to get assets

# Create a configuration file
    
cat <<CONFFILE > config.toml
[[config]]
  name = "arm-benchmarks"
  goroot = "/usr/local/go"

CONFFILE

EOF

# Make the script executable
chmod 755 install_go_and_sweet.sh

# Run the script
./install_go_and_sweet.sh

```

## Expected output from `sweet get`

When sweet get completes successfully, you’ll see output similar to:

```output
Sweet v0.3.0: Go Benchmarking Suite

Retrieves assets for benchmarks from GCS.

Usage: sweet get [flags]
  -cache string
        cache location for assets (default "/home/pareena_verma_arm_com/.cache/go-sweet")
  -clean
        delete all cached assets before installing new ones
  -copy string
        location to extract assets into, useful for development
  -version string
        the version to download assets for (default "v0.3.0")
```


## Verify Installation

To test that everything is installed correctly, set the environment variables shown below on each VM:

```bash
export GOPATH=$HOME/go
export GOBIN=$GOPATH/bin
export PATH=$PATH:$GOBIN:/usr/local/go/bin
```
Now run the `markdown` benchmark with `sweet` on both VMs as shown:

```bash
cd benchmarks/sweet
sweet get
sweet run -count 10 -run="markdown" config.toml # run one, 1X
```

You should see output similar to the following:

```bash
# Example output:
[sweet] Work directory: /tmp/gosweet3444550660
[sweet] Benchmarks: markdown (10 runs)
[sweet] Setting up benchmark: markdown
[sweet] Running benchmark markdown for arm-benchmarks: run 1
...
[sweet] Running benchmark markdown for arm-benchmarks: run 10
```
