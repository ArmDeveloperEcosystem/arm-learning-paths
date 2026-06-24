---
title: Create an Amazon EKS cluster
description: Create and apply a Rafay cluster manifest to provision an Amazon EKS cluster with an AWS Graviton-based node group, then download kubeconfig and verify the nodes report arm64.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create the cluster manifest

The Rafay platform uses a declarative YAML manifest to define your EKS cluster. 

Create a file named `demo-eks-graviton.yaml` with the following content:

```yaml
apiVersion: infra.k8smgmt.io/v3
kind: Cluster
metadata:
  # The name of the cluster
  name: demo-eks-graviton
  # The name of the project the cluster will be created in
  project: defaultproject
spec:
  blueprintConfig:
    # The name of the blueprint the cluster will use
    name: minimal
    # The version of the blueprint the cluster will use
    version: latest
  # The name of the cloud credential that will be used to create the cluster 
  cloudCredentials: aws-cloud-credential
  config:
    # The EKS addons that will be applied to the cluster
    addons:
    - name: kube-proxy
      version: latest
    - name: vpc-cni
      version: latest
    - name: coredns
      version: latest
    managedNodeGroups:
      # The AWS AMI family type the nodes will use
    - amiFamily: AmazonLinux2023
      # The desired number of nodes that can run in the node group 
      desiredCapacity: 1
      iam:
        withAddonPolicies:
          # Enables the IAM policy for cluster autoscaler
          autoScaler: true
          # Allows for full ECR (Elastic Container Registry) access. This is useful for building, for example, a CI server that needs to push images to ECR
          imageBuilder: true
      # The Amazon EC2 instance type that will be used for the nodes
      instanceType: m7g.large
      # The maximum number of nodes that can run in the node group
      maxSize: 1
      # The minimum number of nodes that can run in the node group
      minSize: 1
      # The name of the node group that will be created in AWS
      name: graviton
    metadata:
      # The name of the cluster
      name: demo-eks-graviton
      # The AWS region the cluster will be created in
      region: us-east-1
      # The tags that will be applied to the AWS cluster resources
      tags:
        email: user@rafay.co
        env: qa
      # The Kubernetes version that will be installed on the cluster
      version: latest
    vpc:
      # AutoAllocateIPV6 requests an IPv6 CIDR block with /56 prefix for the VPC
      autoAllocateIPv6: false
      clusterEndpoints:
        # Enables private access to the Kubernetes API server endpoints
        privateAccess: true
        # Enables public access to the Kubernetes API server endpoints
        publicAccess: false
      # The CIDR that will be used  by the cluster VPC  
      cidr: 192.168.0.0/16
  type: aws-eks
```

Key fields to note:

- `cloudCredentials` — must exactly match the credential name you entered in the Rafay console
- `project` - must be the project you attached the credential to
- `instanceType: m7g.large` — a Graviton3-based instance with Arm Neoverse processors
- `publicAccess: false` — the Kubernetes API server has no public endpoint. You reach the cluster exclusively through RCTL, which routes traffic through the Rafay control plane.

## Apply the cluster manifest

Submit the manifest to Rafay using `rctl`:

```console
rctl apply -f demo-eks-graviton.yaml 
```

The output is similar to:

```output
[
  {
    "tasksetId": "ko9176k",
    "tasksetOperations": [
      {
        "operationName": "ClusterCreation",
        "resourceName": "demo-eks-graviton",
        "operationStatus": "PROVISION_TASK_STATUS_INPROGRESS"
      },
      {
        "operationName": "NodegroupCreation",
        "resourceName": "graviton",
        "operationStatus": "PROVISION_TASK_STATUS_PENDING"
      },
      {
        "operationName": "BlueprintSync",
        "resourceName": "demo-eks-graviton",
        "operationStatus": "PROVISION_TASK_STATUS_PENDING"
      }
    ],
    "tasksetStatus": "PROVISION_TASKSET_STATUS_INPROGRESS",
    "comments": "Configuration is being applied to the cluster"
  }
]
```

## Monitor cluster provisioning

Poll the cluster status until it reports `READY`: 

```console
rctl get cluster demo-eks-graviton 
```
Provisioning typically takes 15–20 minutes as Rafay creates the VPC, EKS control plane, and managed node group.

The output is similar to:

```output
+-------------------+-----------------------------+---------+-----------+-----------+---------------------------+---------------------+
| NAME              | CREATED AT                  | TYPE    | STATUS    | BLUEPRINT | PROVISION STATUS          | ENVIRONMENT CREATED |
+-------------------+-----------------------------+---------+-----------+-----------+---------------------------+---------------------+
| demo-eks-graviton | 2026-06-24T15:32:19.936269Z | aws-eks | NOT_READY | minimal   | INFRA_CREATION_INPROGRESS | false               |
+-------------------+-----------------------------+---------+-----------+-----------+---------------------------+---------------------+
```

While waiting, you can run the command again every few minutes. You'll see various status values before the status changes to `READY`. You can also check the AWS CloudFormation console to look for any stack errors.

## Download the kubeconfig

After the cluster is `READY`, download the kubeconfig file:

```console
rctl kubeconfig download --cluster demo-eks-graviton -f ~/.kube/demo-eks-graviton.kubeconfig
```

The output is similar to:

```output
kubeconfig downloaded to ~/.kube/demo-eks-graviton.kubeconfig
```

Export the path so that `kubectl` uses this cluster:

```console
export KUBECONFIG=~/.kube/demo-eks-graviton.kubeconfig
```

## Verify the nodes

Confirm that the cluster has a running node and that it reports the `arm64` architecture:

```console
kubectl get nodes -L kubernetes.io/arch
```

The output is similar to:

```output
NAME                            STATUS   ROLES    AGE   VERSION               ARCH
ip-192-168-13-74.ec2.internal   Ready    <none>   26m   v1.36.2-eks-93b80c6   arm64
```

The `arm64` value in the `ARCH` column confirms that the node is running on an AWS Graviton-based instance. Your EKS cluster is ready to accept workloads. 

## What you've accomplished and what's next

You've now defined and provisioned an Amazon EKS cluster with a Graviton-based node group using Rafay's declarative manifest format. You then applied the manifest with RCTL, waited for the cluster to reach a ready state, and downloaded the kubeconfig so you can interact with the cluster.

In the next section, you'll deploy NGINX to this cluster and verify it runs on the Graviton-based node.
