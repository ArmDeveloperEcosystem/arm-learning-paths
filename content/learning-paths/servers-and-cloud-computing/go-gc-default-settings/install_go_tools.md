---
title: Install Go and Benchstat on an AWS Graviton-based Amazon EC2 instance
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Go on Arm Linux

After the instance starts running, install Go from the Linux `arm64` `go.dev` archive by following the steps in the [Go install guide](/install-guides/go/).


After installing, verify that Go is installed for Arm64 Linux:

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

Benchstat is a Go performance analysis tool that compares benchmark results and provides statistical analysis of performance differences between runs. 

You'll use Benchstat to determine whether observed changes in benchmark metrics are statistically significant rather than the result of normal measurement variability.

Install Benchstat:

```bash
go install golang.org/x/perf/cmd/benchstat@latest
```

The output is similar to:

```output
go: downloading golang.org/x/perf v0.0.0-20260512194132-3cf34090a3db
go: downloading github.com/aclements/go-moremath v0.0.0-20210112150236-f10218a38794
```

Finally, verify that Benchstat is installed:

```bash
benchstat -h
```

The output is similar to:

```output
Usage: benchstat [flags] inputs...

benchstat computes statistical summaries and A/B comparisons of Go
...
```
If you see this output, Benchstat is installed and ready to use. 

## What you've accomplished and what's next

You've now installed Go and Benchstat on an AWS Graviton-based Amazon EC2 instance. 

Next, you'll create a Go garbage collection benchmark.
