---
title: Installing Go and Sweet
weight: 40

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Section Overview

In this section, you'll install Go, Sweet, and the Benchstat comparison tool on both VMs.

## Installation Script

Sweet is a Go benchmarking tool that provides a standardized way to run performance tests across different systems. Benchstat is a companion tool that analyzes and compares benchmark results, helping you understand performance differences between systems. Together, these tools will allow us to accurately measure and compare Go performance on Arm and x86 architectures.


{{% notice Note %}}
Subsequent steps in the learning path assume you are running this script (installing) from your home directory (`~`), resulting in the creation of a `~/benchmarks/sweet` final install path. If you decide to install elsewhere, adjust the path accordingly when prompted to run the benchmark logic later in the learning path.
{{% /notice %}}


Copy and paste this script to **both** of your GCP VMs.  

**You don't need to run it after pasting**, just paste it into your home directory and press enter to install all needed dependencies: 

```bash
#!/usr/bin/env bash

# Write the script to filesystem using a HEREDOC
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
sweet get -force # to get assets

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



## Verify Installation

To test that everything is installed correctly, run the following command on each VM after the script completes:

```bash
# Run the benchmarks
export GOPATH=$HOME/go
export GOBIN=$GOPATH/bin
export PATH=$PATH:$GOBIN:/usr/local/go/bin
cd benchmarks/sweet
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