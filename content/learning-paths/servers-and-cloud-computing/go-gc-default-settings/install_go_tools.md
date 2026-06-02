---
title: Install Go and benchmark tools
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Go on Arm Linux

Install Go on the AWS Graviton instance. The commands below use the Linux Arm64 archive from `go.dev`.

{{% notice Note %}}
The following commands use Go 1.26.3. The same commands work with other Go versions. Replace the archive name and checksum with the values for your version of choice. To find the latest version, see the [Go downloads page](https://go.dev/dl/).
{{% /notice %}}

Download the Go archive and verify the checksum:

```console
cd $HOME
curl -LO https://go.dev/dl/go1.26.3.linux-arm64.tar.gz
echo "9d89a3ea57d141c2b22d70083f2c8459ba3890f2d9e818e7e933b75614936565  go1.26.3.linux-arm64.tar.gz" | sha256sum -c -
```

Install Go under `/usr/local`:

```console
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf go1.26.3.linux-arm64.tar.gz
```

Add Go to your shell path:

```console
export PATH=/usr/local/go/bin:$HOME/go/bin:$PATH
```

To make the path update persistent, add it to your shell profile:

```console
echo 'export PATH=/usr/local/go/bin:$HOME/go/bin:$PATH' >> $HOME/.profile
```

Verify that Go is installed for Arm64 Linux:

```console
go version
go env GOOS GOARCH
```

The output should show `linux` and `arm64`:

```output
linux
arm64
```

## Install Benchstat

Install Benchstat to summarize repeated Go benchmark runs:

```console
go install golang.org/x/perf/cmd/benchstat@latest
```

Verify that Benchstat is available:

```console
benchstat -h
```

You now have Go and Benchstat installed on the AWS Graviton instance.
