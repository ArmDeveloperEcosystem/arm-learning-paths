---
title: "Containerize an example application"
weight: 2

layout: "learningpathall"
---

[AWS Copilot CLI](https://aws.github.io/copilot-cli/) is an open source command line interface for running containers on AWS App Runner, Amazon Elastic Container Service (ECS), and AWS Fargate. 

You can use Copilot to run containers on Fargate serverless compute with Graviton2 processors and benefit from improved price performance. 

Graviton2 is not the default for Copilot, but read on to find out how to set the architecture to Arm.

# Before you begin

This guide is applicable to both Linux and macOS users.

Before starting, ensure you have Docker and Copilot installed on your computer.

For Docker installation, refer to the [Docker install guide](/install-guides/docker/).

For Copilot installation, refer to the [AWS Copilot CLI install guide](/install-guides/aws-copilot).

You will also need an AWS account, which you can create at https://aws.amazon.com. (Click on **Create an AWS Account** in the top right corner. Follow the instructions to register. See the [Creating an AWS account documentation](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html) for full instructions.)

Make sure to configure your access key ID and secret access key, which are used to sign programmatic requests that you make to AWS. Refer to [AWS Credentials](/install-guides/aws_access_keys/) for a quick summary of how to run `aws configure`. The install guide also covers how to install the AWS CLI. Make a note of the AWS region you set with `aws configure` so you can see the resources created by Copilot in the AWS console.


# Create an example application

To try Copilot on Graviton2 processors, you can use the Go application provided below.

Use a text editor to create the three files below.

Create a file named `hello.go` with the contents:

```go
// Copyright 2022 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package main

import (
	"fmt"
	"log"
	"net/http"
	"runtime"
)

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello from CPU PLATFORM:%s/%s",
		runtime.GOOS, runtime.GOARCH)
}

func main() {
	http.HandleFunc("/", handler)
	log.Fatal(http.ListenAndServe(":8080", nil))
}
```

Next, create a file named `go.mod` with the following two lines:

```go
module example.com/arm
go 1.21
```

Create a third file named `Dockerfile` with the contents:

```dockerfile
#
# Build: 1st stage
#
FROM golang:1.21-alpine as builder
ARG TARCH
WORKDIR /app
COPY go.mod .
COPY hello.go .
RUN go build -o /hello && \
    apk add --update --no-cache file && \
    file /hello

#
# Release: 2nd stage
#
FROM alpine
WORKDIR /
COPY --from=builder /hello /hello
RUN apk add --update --no-cache file
CMD [ "/hello" ]
```

The application listens on port 8080 and prints the architecture of the machine.

