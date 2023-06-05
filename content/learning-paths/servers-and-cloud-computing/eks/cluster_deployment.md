---
title: "Deploy an EKS cluster"
weight: 2
layout: learningpathall
---

## Before you begin

You should have the prerequisite tools installed before starting the Learning Path.

Any computer which has the required tools installed can be used for this section. The computer can be your desktop or laptop computer or a virtual machine with the required tools.

You will need an [AWS account](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=default&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start) to complete this Learning Path. Create an account if you don't have one.

## EKS cluster deployment configuration
To deploy the Elastic Kubernetes Service(EKS) cluster start by creating the terraform configuration on your running Arm machine.

The Terraform configuration for this Elastic Kubernetes Service (EKS) deployment is contained in 7 files: `eks_cluster.tf`, `variables.tf`, `vpc.tf`, `security-groups.tf`, `main.tf`, `terraform.tf`, `output.tf`.

Using an editor of your choice, create and copy the content of the 7 files as shown below.

File 1: `providers.tf` sets versions for the providers used by the configuration. Add the following code in this file:
```console
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
    }

    random = {
      source  = "hashicorp/random"
    }

    tls = {
      source  = "hashicorp/tls"
    }

    cloudinit = {
      source  = "hashicorp/cloudinit"
    }

    kubernetes = {
      source  = "hashicorp/kubernetes"
    }
  }
}
```

File 2: `variables.tf` contains a region variable that controls where to create the EKS cluster. Add the following code in this file:
```console
variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-east-2"
}
```

File 3: `vpc.tf` provisions a VPC, subnets, and availability zones using the [AWS VPC Module](https://registry.terraform.io/modules/terraform-aws-modules/vpc/aws/2.32.0). Add the following code in this file:
```console
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "3.14.2"

  name = "demo-vpc"

  cidr = "10.0.0.0/16"
  azs  = slice(data.aws_availability_zones.available.names, 0, 3)

  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.4.0/24", "10.0.5.0/24", "10.0.6.0/24"]

  enable_nat_gateway   = true
  single_nat_gateway   = true
  enable_dns_hostnames = true

  public_subnet_tags = {
    "kubernetes.io/cluster/${local.cluster_name}" = "shared"
    "kubernetes.io/role/elb"                      = 1
  }

  private_subnet_tags = {
    "kubernetes.io/cluster/${local.cluster_name}" = "shared"
    "kubernetes.io/role/internal-elb"             = 1
  }
}
```

File 4: `security-groups.tf` provisions the security groups, the EKS cluster will use.
```console
resource "aws_security_group" "node_group_one" {
  name_prefix = "node_group_one"
  vpc_id      = module.vpc.vpc_id

  ingress = [
    {
      description      = "All traffic"
      from_port        = 0    # All ports
      to_port          = 0    # All Ports
      protocol         = "-1" # All traffic
      cidr_blocks      = ["0.0.0.0/0"]
      ipv6_cidr_blocks = null
      prefix_list_ids  = null
      security_groups  = null
      self             = null
    }
  ]

  egress = [
    {
      from_port        = 0
      to_port          = 0
      protocol         = "-1"
      cidr_blocks      = ["0.0.0.0/0"]
      ipv6_cidr_blocks = ["::/0"]
      description      = "Outbound rule"
      prefix_list_ids  = null
      security_groups  = null
      self             = null
    }
  ]
}

resource "aws_security_group" "node_group_two" {
  name_prefix = "node_group_two"
  vpc_id      = module.vpc.vpc_id

  ingress = [
    {
      description      = "All traffic"
      from_port        = 0    # All ports
      to_port          = 0    # All Ports
      protocol         = "-1" # All traffic
      cidr_blocks      = ["0.0.0.0/0"]
      ipv6_cidr_blocks = null
      prefix_list_ids  = null
      security_groups  = null
      self             = null
    }
  ]

  egress = [
    {
      from_port        = 0
      to_port          = 0
      protocol         = "-1"
      cidr_blocks      = ["0.0.0.0/0"]
      ipv6_cidr_blocks = ["::/0"]
      description      = "Outbound rule"
      prefix_list_ids  = null
      security_groups  = null
      self             = null
    }
  ]
}
```

File 5: `eks-cluster.tf` uses the [AWS EKS Module](https://registry.terraform.io/modules/terraform-aws-modules/eks/aws/11.0.0) to provision an EKS Cluster and other required resources, including Auto Scaling Groups, Security Groups, IAM Roles, and IAM Policies. Below parameter will create three nodes across two node groups.
```console
module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "18.26.6"

  cluster_name    = local.cluster_name
  cluster_version = "1.22"

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.public_subnets

  eks_managed_node_group_defaults = {
    ami_type = "AL2_ARM_64"
    attach_cluster_primary_security_group = true
    # Disabling and using externally provided security groups
    create_security_group = false
  }

  eks_managed_node_groups = {
    one = {
      name = "node-group-1"
      instance_types = ["t4g.large"]
      min_size     = 1
      max_size     = 3
      desired_size = 2
      pre_bootstrap_user_data = <<-EOT
      echo 'foo bar'
      EOT
      vpc_security_group_ids = [
        aws_security_group.node_group_one.id
      ]
    }

    two = {
      name = "node-group-2"
      instance_types = ["t4g.large"]
      min_size     = 1
      max_size     = 2
      desired_size = 1
      pre_bootstrap_user_data = <<-EOT
      echo 'foo bar'
      EOT
      vpc_security_group_ids = [
        aws_security_group.node_group_two.id
      ]
    }
  }
}
```

File 6: `outputs.tf` defines the output values for this configuration.
```console
output "cluster_id" {
  description = "EKS cluster ID"
  value       = module.eks.cluster_id
}

output "cluster_endpoint" {
  description = "Endpoint for EKS control plane"
  value       = module.eks.cluster_endpoint
}

output "cluster_security_group_id" {
  description = "Security group ids attached to the cluster control plane"
  value       = module.eks.cluster_security_group_id
}

output "region" {
  description = "AWS region"
  value       = var.region
}

output "cluster_name" {
  description = "Kubernetes Cluster Name"
  value       = local.cluster_name
}
```

File 7 : Add below code in `main.tf`
```console
provider "kubernetes" {
  host                   = module.eks.cluster_endpoint
  cluster_ca_certificate = base64decode(module.eks.cluster_certificate_authority_data)
}

provider "aws" {
  region = var.region
}

data "aws_availability_zones" "available" {}

locals {
  cluster_name = "demo-eks-${random_string.suffix.result}"
}

resource "random_string" "suffix" {
  length  = 8
  special = false
}
```

## Terraform commands
### Initialize Terraform
Run `terraform init` to initialize the Terraform deployment. This command downloads the AWS modules required to manage your AWS resources. Run this command in the directory which contains the 7 configuration files you created.
```console
terraform init
```
The output from running this command should look like what is shown here:


```output
Initializing modules...

Initializing the backend...

Initializing provider plugins...
- Reusing previous version of hashicorp/aws from the dependency lock file
- Reusing previous version of hashicorp/random from the dependency lock file
- Reusing previous version of hashicorp/tls from the dependency lock file
- Reusing previous version of hashicorp/cloudinit from the dependency lock file
- Reusing previous version of hashicorp/kubernetes from the dependency lock file
- Using previously-installed hashicorp/aws v4.15.1
- Using previously-installed hashicorp/random v3.1.3
- Using previously-installed hashicorp/tls v3.4.0
- Using previously-installed hashicorp/cloudinit v2.2.0
- Using previously-installed hashicorp/kubernetes v2.12.1

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

### Create Terraform execution plan
Creating a terraform execution plan will check for your AWS account credentials. Either set the [AWS environment variables or add a profile to your AWS credentials file](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html) on your running Arm machine.
Now, run `terraform plan` to create an execution plan.
```console
terraform plan
```
A long output of resources to be created will be printed.

### Apply Terraform execution plan

Run `terraform apply` to apply the execution plan to your cloud infrastructure. Below command creates all required infrastructure.
```
  terraform apply
```
The output from running this command is shown below:

```output
Apply complete! Resources: 56 added, 0 changed, 0 destroyed.

Outputs:

cluster_endpoint = "https://8AD4D643BDAA50CA99B369951048E106.gr7.us-east-2.eks.amazonaws.com"
cluster_id = "demo-eks-HjmS0zFi"
cluster_name = "demo-eks-HjmS0zFi"
cluster_security_group_id = "sg-0b571848495e3542b"
region = "us-east-2"
```

### Configure kubectl

Now run the command shown with the terraform output region and cluster_name to match what was previously output
```console
aws eks --region $(terraform output region) update-kubeconfig --name $(terraform output cluster_name)
```

Run the following command to see the status of the nodes. They should be in the ready state.
```console
kubectl get nodes
```

```output
NAME                                       STATUS   ROLES    AGE   VERSION
ip-10-0-4-111.us-east-2.compute.internal   Ready    <none>   19m   v1.22.17-eks-0a21954
ip-10-0-4-204.us-east-2.compute.internal   Ready    <none>   19m   v1.22.17-eks-0a21954
ip-10-0-6-209.us-east-2.compute.internal   Ready    <none>   19m   v1.22.17-eks-0a21954
```

Run the following command to see the current pods running on the cluster.
```console
kubectl get pods -A
```

```output
NAMESPACE     NAME                       READY   STATUS    RESTARTS   AGE
kube-system   aws-node-2ckzl             1/1     Running   0          6m28s
kube-system   aws-node-8bqrx             1/1     Running   0          6m18s
kube-system   aws-node-hnd5x             1/1     Running   0          6m17s
kube-system   coredns-5db97b446d-4c4wn   1/1     Running   0          10m
kube-system   coredns-5db97b446d-hg6p6   1/1     Running   0          10m
kube-system   kube-proxy-drt6g           1/1     Running   0          6m28s
kube-system   kube-proxy-mjtws           1/1     Running   0          6m18s
kube-system   kube-proxy-v252s           1/1     Running   0          6m18s
```

Make sure that all of these services are in a running state as shown above.
