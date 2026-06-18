---
title: Install Go and Benchstat on an AWS Graviton-based Amazon EC2 instance
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Go on Arm Linux

After the instance starts running, install Go. You'll use the following commands to install Go from the Linux Arm64 `go.dev` archive.

{{% notice Note %}}
The following commands use Go 1.26.3. The same commands work with other Go versions. Replace the archive name and checksum with the values for your version of choice. To find the latest version, see the [Go downloads page](https://go.dev/dl/).
{{% /notice %}}


Download the Go archive and verify the checksum:

```bash
cd $HOME
curl -LO https://go.dev/dl/go1.26.3.linux-arm64.tar.gz
echo "9d89a3ea57d141c2b22d70083f2c8459ba3890f2d9e818e7e933b75614936565  go1.26.3.linux-arm64.tar.gz" | sha256sum -c -
```

Install Go under `/usr/local`:

```bash
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf go1.26.3.linux-arm64.tar.gz
```

Add Go to your shell path:

```bash
export PATH=/usr/local/go/bin:$HOME/go/bin:$PATH
```

To make the path update persistent, add it to your shell profile:

```bash
echo 'export PATH=/usr/local/go/bin:$HOME/go/bin:$PATH' >> $HOME/.profile
```

Verify that Go is installed for Arm64 Linux:

```bash
go version
go env GOOS GOARCH
```

The output is similar to:

```output
go version go1.26.3 linux/arm64
linux
arm64
```

## Install Benchstat

`benchstat` is a Go performance analysis tool that compares benchmark results and provides statistical analysis of performance differences between runs. You'll use `benchstat` to determine whether observed changes in benchmark metrics are statistically significant rather than the result of normal measurement variability.

Install `benchstat`:

```bash
go install golang.org/x/perf/cmd/benchstat@latest
```

The output is similar to:

```output
go: downloading golang.org/x/perf v0.0.0-20260512194132-3cf34090a3db
go: downloading github.com/aclements/go-moremath v0.0.0-20210112150236-f10218a38794
```

Finally, verify that `benchstat` is installed:

```bash
benchstat -h
```

The output is similar to:

```output
Usage: benchstat [flags] inputs...

benchstat computes statistical summaries and A/B comparisons of Go
...
```
If you see this output, `benchstat` is installed and ready to use. 


## What you've accomplished and what's next

You've now installed Go and `benchstat` installed on an AWS Graviton-based Amazon EC2 instance. 

Next, you'll create a Go garbage collection benchmark.
