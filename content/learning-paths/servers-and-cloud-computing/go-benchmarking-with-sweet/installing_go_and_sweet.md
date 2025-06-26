---
title: Install Go, Sweet, and Benchstat
weight: 40

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you'll install Go, Sweet, and Benchstat on both virtual machines.

Sweet is a Go benchmarking tool that provides a standardized way to run performance tests across systems. Benchstat is a companion tool that compares benchmark results to highlight meaningful performance differences. Together, these tools help you evaluate Go performance on both Arm and x86 architectures.

{{% notice Note %}}
Subsequent steps in the learning path assume you are running this script (installing) from your home directory (`$HOME`), resulting in the creation of a `$HOME/benchmarks/sweet` final install path. If you install to a different directory, update the paths in later steps to match your custom location.
{{% /notice %}}

## Installation script

Start by copying and pasting the script below on both of your GCP VMs. This script automatically detects your system architecture, installs the appropriate Go version, and sets up Sweet, Benchstat, and the Go benchmark suite.

Paste the full block into your terminal. This creates and runs an installer script directly from your home directory:

```bash
#!/usr/bin/env bash

# Write the install script to filesystem using a HEREDOC
cat <<'EOF' > install_go_and_sweet.sh

sudo apt-get -y update
sudo apt-get -y install git build-essential

# Detect architecture - this allows the same script to work on both
# Arm (c4a) and x86 (c4) VMs without modification
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

## Expected output from sweet get

When `sweet get` completes successfully, you’ll see output similar to:

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


## Verify installation

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
