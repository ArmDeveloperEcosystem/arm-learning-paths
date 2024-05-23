---
additional_search_terms:
- kubernetes
- EKS
- AWS
- infrastructure
author_primary: Jason Andrews
layout: installtoolsall
minutes_to_complete: 5
multi_install: false
multitool_install_part: false
official_docs: https://docs.aws.amazon.com/eks/latest/userguide/eksctl.html
test_images:
- ubuntu:latest
test_link: null
test_maintenance: true
test_status:
- passed
title: AWS EKS CLI (eksctl)
tool_install: true
weight: 1
---

The Amazon EKS CLI, `eksctl`, is a command line tool to create and manage Kubernetes clusters in Amazon Kubernetes Service (EKS). It simplifies cluster creation and saves time compared to using the AWS console. For additional information refer to the [EKS CLI official documentation](https://eksctl.io/).

The EKS CLI is available for a variety of operating systems and Linux distributions and there are multiple ways to install it. It runs on both Arm Linux distributions and Windows on Arm.

## What should I do before installing eksctl on Arm Linux and Windows on Arm?

This install guide provides a quick solution to install `eksctl` on Arm Linux and Windows on Arm. 

1. Confirm you have an Arm machine

For Linux, confirm you are using an Arm machine by running:

```bash { target="ubuntu:latest" }
uname -m
```

The output should be:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

For Windows, confirm the Arm architecture by typing "Settings" in the Windows search box. 

When the settings appear, click System on the left side and then About at the bottom.

In the Device specifications section look for "ARM-based processor" in the System type area. 

2. Install `kubectl`

Install the Kubernetes command-line tool, `kubectl`, using the [Kubectl install guide](/install-guides/kubectl/).

## How do I download and install eksctl on Arm Linux?

1. Download the `eksctl` package using `curl`: 

```bash { target="ubuntu:latest" }
curl -sLO "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_Linux_arm64.tar.gz"
```

2. Install `eksctl` with: 

```bash { target="ubuntu:latest" }
tar -xzf eksctl_Linux_arm64.tar.gz -C /tmp && rm eksctl_Linux_arm64.tar.gz
sudo mv /tmp/eksctl /usr/local/bin
```

3. Confirm `eksctl` is installed:

```bash { target="ubuntu:latest" }
eksctl version
```

The output will be similar to:

```output
0.160.0
```

## How do I download and install eksctl on Windows?

1. Use a browser to download the [EKS CLI latest release](https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_Windows_arm64.zip).

2. Unzip the downloaded file.

3. Confirm `eksctl.exe` is installed:

```console
eksctl.exe version
```

The output will be similar to:

```output
0.160.0
```

## How do I configure the AWS CLI?

`eksctl` relies on the AWS CLI being installed and configured. Use the [AWS CLI install guide](/install-guides/aws-cli/) to install the AWS CLI. The CLI provides the `aws` command.

You will also need to configure the AWS CLI using the `aws configure` or the `aws configure sso` command. There are multiple ways to configure the CLI, including environment variables, command-line options, and credentials files. Refer to the [Configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) for more details. 

## How do I use eksctl to create a simple EKS cluster?

With your AWS account configured, run `eksctl` to create a cluster with 2 nodes with AWS Graviton processors: 

```console
eksctl create cluster  \
--name cluster-1  \
--region us-east-1 \
--node-type t4g.small \
--nodes 2 \
--nodegroup-name node-group-1 
```

Use the AWS console to look at the resources associated with the cluster and monitor progress of cluster creation. 

When the cluster is created, use `kubectl` to get the status of the nodes in the cluster. 

```console
kubectl get nodes -o wide
```

The output is similar to:

```output
NAME                             STATUS   ROLES    AGE     VERSION                INTERNAL-IP      EXTERNAL-IP      OS-IMAGE         KERNEL-VERSION                   CONTAINER-RUNTIME
ip-192-168-38-144.ec2.internal   Ready    <none>   2m31s   v1.25.13-eks-43840fb   192.168.38.144   35.153.206.210   Amazon Linux 2   5.10.192-183.736.amzn2.aarch64   containerd://1.6.19
ip-192-168-4-142.ec2.internal    Ready    <none>   2m31s   v1.25.13-eks-43840fb   192.168.4.142    54.175.254.219   Amazon Linux 2   5.10.192-183.736.amzn2.aarch64   containerd://1.6.19
```

## How do I use eksctl to delete the cluster?

To delete the resources associated with the cluster, run:

```console
eksctl delete cluster --region=us-east-1 --name=cluster-1
```

You can now use `eksctl` to create, manage, and delete more complex infrastructures.
