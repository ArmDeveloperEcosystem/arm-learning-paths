---
# User change
title: "Run Docker images from Docker Hub and AWS Elastic Container Registry (ECR)"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Install Docker

[Install Docker](/install-guides/docker/) on any Arm machine you want to run the images created in the previous article. 

For Linux, confirm the architecture is Arm AArch64. 

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The output should be:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

## Pull and Run

If CodeBuild is complete, the images are ready to pull and run. Both images are identical and the output from the `uname` is the same and shows the image was built on Amazon Linux 2.

To get the image from Docker Hub:

```bash
docker pull <username>/c-hello-world
```

{{% notice Note %}}
Replace `<username>` with your Docker Hub user name.
{{% /notice %}}

To get the image from AWS ECR:
```bash
docker pull public.ecr.aws/<alias>/c-hello-world
```

{{% notice Note %}}
Replace `<alias>` with your AWS ECR alias (similar to `m6s3k6o5`)
{{% /notice %}}

To run the Docker Hub image:
```bash
docker run --rm <username>/c-hello-world
```

The output should be similar to:
```output
Hello, architecture from uname is Linux 39d131c8e64b 4.14.219-161.340.amzn2.aarch64 #1 SMP Thu Feb 4 05:54:27 UTC 2021 aarch64 Linux
64-bit userspace
```

To run the AWS ECR image:
```bash
docker run --rm public.ecr.aws/<alias>/c-hello-world
```

The output should be the same as above.

## Summary

CodeBuild makes it easy to automate Docker image creation on AWS Graviton processors. The images can be stored automatically in repositories such as Docker Hub and AWS ECR. The images can be run on any Arm machine with Docker installed, including Linux, macOS, and Windows on Arm.
 

