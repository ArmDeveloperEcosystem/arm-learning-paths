---
# User change
title: "Run Docker images from Docker Hub and AWS Elastic Container Registry (ECR)"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Install Docker

[Install Docker](/install-tools/docker/) on any Arm machine you want to run the images created in the previous article. 

For Linux, confirm the architecture is Arm AArch64. 

```console
$ uname -m
aarch64
```

## Pull and Run

If CodeBuild is complete, the images are ready to pull and run. Both images are identical and the output from the uname is the same and shows the image was built on Amazon Linux 2.

To get the image from Docker Hub:

```console
docker pull jasonrandrews/c-hello-world
```

To get the image from AWS ECR:
```console
docker pull public.ecr.aws/z9p7l6s8/c-hello-world
```

To run the Docker Hub image:
```console
docker run --rm jasonrandrews/c-hello-world
```

The output should be similar to:
```console
Hello, architecture from uname is Linux 39d131c8e64b 4.14.219-161.340.amzn2.aarch64 #1 SMP Thu Feb 4 05:54:27 UTC 2021 aarch64 Linux
64-bit userspace
```

To run the AWS ECR image:
```console
docker run --rm public.ecr.aws/z9p7l6s8/c-hello-world
```

The output should be the same as above.

## Summary

CodeBuild makes it easy to automate Docker image creation on AWS Graviton processors. The images can be stored automatically in repositories such as Docker Hub and AWS ECR. The images can be run on any Arm machine with Docker installed, including Linux, macOS, and Windows on Arm.
 

