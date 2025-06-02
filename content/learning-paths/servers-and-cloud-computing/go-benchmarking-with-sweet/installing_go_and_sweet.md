---
title: Installing Go and Sweet
weight: 40

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Installing Go and Sweet
Now that you have your GCP VMs set up, it’s time to install Go, Sweet, and the Benchstat comparison tool on **both** VMs.

Copy and paste this script to **both** of your GCP VMs to automatically install all the needed Go and benchmarking dependencies: 

```bash
cat <<'EOF' > install_go_and_sweet.sh

#!/usr/bin/env bash

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
    
cat <<CONFFILE > config.toml
[[config]]
  name = "arm-benchmarks"
  goroot = "/usr/local/go"

CONFFILE

EOF

chmod 755 install_go_and_sweet.sh
./install_go_and_sweet.sh

```

To test that everything is installed correctly, run the following command on each VM post-script execution:



```bash
# Run the benchmarks
export GOPATH=$HOME/go
export GOBIN=$GOPATH/bin
export PATH=$PATH:$GOBIN:/usr/local/go/bin
cd benchmarks/sweet
sweet run -count 10 -run="markdown" config.toml # run one, 1X
```

You should see output similar to the following:

```output
[sweet] Work directory: /tmp/gosweet3444550660
[sweet] Benchmarks: markdown (10 runs)
[sweet] Setting up benchmark: markdown
[sweet] Running benchmark markdown for arm-benchmarks: run 1
...
[sweet] Running benchmark markdown for arm-benchmarks: run 10
```
