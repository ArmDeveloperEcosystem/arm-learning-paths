---
title: "Create an EKS cluster"
weight: 2
layout: learningpathall
---

## Before you begin

You will need a computer with the following tools installed: [EKS CLI](/install-guides/eksctl/), [AWS CLI](/install-guides/aws-cli), and [Kubernetes CLI](/install-guides/kubectl). 

Install each of these tools and confirm you can run the `aws`, `ekscli`, and `kubectl` commands. 

Any computer (desktop, laptop computer or virtual machine) which has the required tools installed can be used for this Learning Path.

You will also need an [AWS account](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=default&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start) for this Learning Path. Create an account if you don't already have one.

Make sure to configure your access key ID and secret access key, which are used to sign programmatic requests you make to AWS. Refer to [AWS Credentials](/install-guides/aws_access_keys/) for a quick summary of how to run `aws configure`.

With the required tools installed and your AWS account configured for CLI access, you are now ready to begin.

## Create an Elastic Kubernetes Service (EKS) cluster 

You can create an EKS cluster with the EKS command line tool `eksctl`. 

Navigate to an empty directory and use a text editor to save the information below in a file named `eks-cluster.yaml`.

```yaml
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig
metadata:
  name: demo-eks
  region: us-east-1

managedNodeGroups:
  - name: node-group-1
    instanceType: t4g.large
    desiredCapacity: 2
    minSize: 1
    maxSize: 3
    iam:
      withAddonPolicies:
        autoScaler: true
        externalDNS: true
        ebs: true
```

The new EKS cluster uses the t4g.large instance type which includes AWS Graviton processors. You can change the `region` and the `instanceType` if you want to work in a different region or use a different instance type.

Run the command below to create the cluster:

```console
eksctl create cluster -f eks-cluster.yaml
```

It will take about 15 minutes to create the cluster. The example output is shown below:

```output
2024-04-08 18:56:57 [ℹ]  eksctl version 0.175.0
2024-04-08 18:56:57 [ℹ]  using region us-east-1
2024-04-08 18:56:58 [ℹ]  skipping us-east-1e from selection because it doesn't support the following instance type(s): t4g.large
2024-04-08 18:56:58 [ℹ]  setting availability zones to [us-east-1a us-east-1c]
2024-04-08 18:56:58 [ℹ]  subnets for us-east-1a - public:192.168.0.0/19 private:192.168.64.0/19
2024-04-08 18:56:58 [ℹ]  subnets for us-east-1c - public:192.168.32.0/19 private:192.168.96.0/19
2024-04-08 18:56:58 [ℹ]  nodegroup "node-group-1" will use "" [AmazonLinux2/1.29]
2024-04-08 18:56:58 [ℹ]  using Kubernetes version 1.29
2024-04-08 18:56:58 [ℹ]  creating EKS cluster "demo-eks" in "us-east-1" region with managed nodes
2024-04-08 18:56:58 [ℹ]  1 nodegroup (node-group-1) was included (based on the include/exclude rules)
2024-04-08 18:56:58 [ℹ]  will create a CloudFormation stack for cluster itself and 0 nodegroup stack(s)
2024-04-08 18:56:58 [ℹ]  will create a CloudFormation stack for cluster itself and 1 managed nodegroup stack(s)
2024-04-08 18:56:58 [ℹ]  if you encounter any issues, check CloudFormation console or try 'eksctl utils describe-stacks --region=us-east-1 --cluster=demo-eks'
2024-04-08 18:56:58 [ℹ]  Kubernetes API endpoint access will use default of {publicAccess=true, privateAccess=false} for cluster "demo-eks" in "us-east-1"
2024-04-08 18:56:58 [ℹ]  CloudWatch logging will not be enabled for cluster "demo-eks" in "us-east-1"
2024-04-08 18:56:58 [ℹ]  you can enable it with 'eksctl utils update-cluster-logging --enable-types={SPECIFY-YOUR-LOG-TYPES-HERE (e.g. all)} --region=us-east-1 --cluster=demo-eks'
2024-04-08 18:56:58 [ℹ]  
2 sequential tasks: { create cluster control plane "demo-eks", 
    2 sequential sub-tasks: { 
        wait for control plane to become ready,
        create managed nodegroup "node-group-1",
    } 
}
2024-04-08 18:56:58 [ℹ]  building cluster stack "eksctl-demo-eks-cluster"
2024-04-08 18:56:59 [ℹ]  deploying stack "eksctl-demo-eks-cluster"
2024-04-08 18:57:29 [ℹ]  waiting for CloudFormation stack "eksctl-demo-eks-cluster"
2024-04-08 18:57:59 [ℹ]  waiting for CloudFormation stack "eksctl-demo-eks-cluster"
2024-04-08 19:00:00 [ℹ]  waiting for CloudFormation stack "eksctl-demo-eks-cluster"
2024-04-08 19:02:00 [ℹ]  waiting for CloudFormation stack "eksctl-demo-eks-cluster"
2024-04-08 19:04:01 [ℹ]  waiting for CloudFormation stack "eksctl-demo-eks-cluster"
2024-04-08 19:06:02 [ℹ]  waiting for CloudFormation stack "eksctl-demo-eks-cluster"
2024-04-08 19:09:06 [ℹ]  building managed nodegroup stack "eksctl-demo-eks-nodegroup-node-group-1"
2024-04-08 19:09:07 [ℹ]  deploying stack "eksctl-demo-eks-nodegroup-node-group-1"
2024-04-08 19:09:07 [ℹ]  waiting for CloudFormation stack "eksctl-demo-eks-nodegroup-node-group-1"
2024-04-08 19:10:19 [ℹ]  waiting for CloudFormation stack "eksctl-demo-eks-nodegroup-node-group-1"
2024-04-08 19:13:20 [ℹ]  waiting for CloudFormation stack "eksctl-demo-eks-nodegroup-node-group-1"
2024-04-08 19:13:21 [✔]  saved kubeconfig as "/home/ubuntu/.kube/config"
2024-04-08 19:13:21 [ℹ]  no tasks
2024-04-08 19:13:21 [✔]  all EKS cluster resources for "demo-eks" have been created
2024-04-08 19:13:22 [ℹ]  nodegroup "node-group-1" has 2 node(s)
2024-04-08 19:13:22 [ℹ]  node "ip-192-168-12-242.ec2.internal" is ready
2024-04-08 19:13:22 [ℹ]  node "ip-192-168-42-64.ec2.internal" is ready
2024-04-08 19:13:22 [ℹ]  waiting for at least 1 node(s) to become ready in "node-group-1"
2024-04-08 19:13:22 [ℹ]  nodegroup "node-group-1" has 2 node(s)
2024-04-08 19:13:22 [ℹ]  node "ip-192-168-12-242.ec2.internal" is ready
2024-04-08 19:13:22 [ℹ]  node "ip-192-168-42-64.ec2.internal" is ready
2024-04-08 19:13:23 [ℹ]  kubectl command should work with "/home/ubuntu/.kube/config", try 'kubectl get nodes'
2024-04-08 19:13:23 [✔]  EKS cluster "demo-eks" in "us-east-1" region is ready
```

When the command completes the cluster is ready. You can display the nodes with `kubectl`:

```console
kubectl get nodes
```

The output will be similar to:

```output
NAME                             STATUS   ROLES    AGE     VERSION
ip-192-168-12-242.ec2.internal   Ready    <none>   4m21s   v1.29.0-eks-5e0fdde
ip-192-168-42-64.ec2.internal    Ready    <none>   4m2s    v1.29.0-eks-5e0fdde
```

You are now ready to deploy WordPress.


