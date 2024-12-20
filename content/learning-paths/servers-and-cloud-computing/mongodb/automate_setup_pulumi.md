---
# User change
title: "Automate MongoDB Performance Benchmarking Infrastructure Setup with Pulumi"

weight: 8 # (intro is 1), 2 is first, 3 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

You can automate the MongoDB performance benchmarking setup, along with the YCSB framework and the required infrastructure in AWS using Pulumi.

[Pulumi](https://www.pulumi.com/) is a multi-language 'Infrastructure as Code' tool. Pulumi is [open source](https://github.com/pulumi/pulumi) and makes it easy to deploy cloud infrastructure.

## Before you begin

Install the python dependencies on your Ubuntu 22.04 machine:

```bash
sudo apt update
sudo apt install python-is-python3 -y
sudo apt install python3-pip -y
sudo apt install python3.10-venv
```

## Install Pulumi 

You can install Pulumi with this [install guide](/install-guides/pulumi/)

Check the version of Pulumi:

```bash
pulumi version
```

## Clone the Repository
The following github repo contains all the scripts required for this automation. Clone the repo on your local linux system:

```bash
git clone https://github.com/pbk8s/pulumi-ec2.git
```

## Build gatord
You would also need the gatord binary for performance analysis. [gator](https://github.com/ARM-software/gator) is a target agent (daemon), part of Arm Streamline, a set of performance analysis tools. Use the following commands to build it from source.

```bash
git clone https://github.com/ARM-software/gator.git
cd gator
sudo apt-get install ninja-build cmake gcc g++ g++-aarch64-linux-gnu zip pkg-config
./build-linux.sh
```
Once the build is successful, you should see an output like below

```output
Build complete. Please find gatord binaries at:
    /home/ubuntu/gator/build-native-gcc-rel/gatord
```

Copy the gatord binary to the Pulumi working directory

```bash
cp build-native-gcc-rel/gatord ~/pulumi-ec2/
```

## Install awscli and set environment variables
Use the [awscli](https://learn.arm.com/install-guides/aws-cli/) learning path to install the awscli. 

Set the following environment variables on your local computer to connect to your AWS account
```console
export AWS_ACCESS_KEY_ID=<access-key-id>
export AWS_SECRET_ACCESS_KEY=<secret-access-key>
export AWS_SESSION_TOKEN=<session-token>
```
Execute the following command to validate the credentials
```console
aws sts get-caller-identity
```

You should see an output as follows
```output
{
    "UserId": "XYXYXYXYXYXY:xyz@email.com",
    "Account": "123456789",
    "Arn": "arn:aws:sts::123456789:assumed-role/myrole/xyz@email.com"
}
```

## Setup configurations 

Navigate to 'pulumi-ec2' folder and set it as your working directory

```bash
cd ~/pulumi-ec2
```

Execute the following python script to install all dependencies

```bash
./python-setup.sh
```

Open the 'Pulumi.yaml' file in your preferred editor:

```bash
vi Pulumi.yaml
```

Edit the default AWS region to your preferred region:

```yaml
name: p1-py
runtime:
  name: python
  options:
    virtualenv: venv
description: Basic EC2 setup
template:
  config:
    aws:region:
      description: The AWS region to deploy into
      default: us-east-1
```

Edit the `__main__.py` file to change the availability zone of your network subnet

```python
subnet = aws.ec2.Subnet("p1-subnet",
    vpc_id=vpc.id,
    cidr_block="172.16.0.0/24",
    availability_zone="us-east-1a",
    map_public_ip_on_launch=True,
    tags={
        "Name": "p1-subnet",
    })
```

Note: The security groups created by this script are lot less restrictive, to simplify the deployment process and to remove additional complexities. Please modify the ingress/egress rules as per your organizations' policy.

```python
group = aws.ec2.SecurityGroup('p1-security-grouup',
    vpc_id=vpc.id,
    description='Enable HTTP and SSH access',
    ingress=[
        aws.ec2.SecurityGroupIngressArgs(
        protocol='tcp',
        from_port=80,
        to_port=80,
        cidr_blocks=['0.0.0.0/0'],),
        aws.ec2.SecurityGroupIngressArgs(
        protocol='tcp',
        from_port=22,
        to_port=22,
        cidr_blocks=['0.0.0.0/0'],),
    ],
    egress=[aws.ec2.SecurityGroupEgressArgs(
        from_port=0,
        to_port=0,
        protocol="-1",
        cidr_blocks=["0.0.0.0/0"],
        ipv6_cidr_blocks=["::/0"],
    )]
    )
```

## Pulumi commands 

Log in to your local machine, a shortcut to use ~/.pulumi to store project data.

```bash
pulumi login --local
```

Execute the following command to set the AWS region where you'd like to deploy the resources:

```bash
pulumi config set aws:region us-east-1
```
Enter the name of the new stack you'd like to create.

Now, deploy the Pulumi stack with the following command

```bash
pulumi up
```
Select the name of the stack from previous step and hit enter. You should see the following output.

```output
Previewing update (newstack2):
     Type                              Name                Plan       
 +   pulumi:pulumi:Stack               p1-py-newstack2     create     
 +   ├─ tls:index:PrivateKey           p1-key              create     
 +   │  └─ aws:ec2:KeyPair             p1-key              create     
 +   ├─ aws:ec2:Vpc                    p1-vpc              create     
 +   ├─ aws:ec2:Subnet                 p1-subnet           create     
 +   ├─ aws:ec2:InternetGateway        p1-igw              create     
 +   ├─ aws:ec2:SecurityGroup          p1-security-grouup  create     
 +   ├─ aws:ec2:RouteTable             p1-route-table      create     
 +   ├─ aws:ec2:Instance               p1-server           create     
 +   ├─ aws:ec2:RouteTableAssociation  p1-rta              create     
 +   ├─ command:remote:CopyFile        gatord-copy         create     
 +   ├─ command:remote:CopyFile        p1-copy-script      create     
 +   └─ command:remote:Command         p1-run-script       create     


Outputs:
    private_key_pem: output<string>
    public_dns     : output<string>
    public_ip      : output<string>

Resources:
    + 13 to create
```
You will be prompted to update the stack. Select 'yes' to create the stack. Once successfully completed, you can ssh to the instance using the 'public_ip' or 'public_dns' property. 

Execute the following script to get the private key to SSH to the new instance
```bash
./get-key.sh
```
For passphrase, you can just hit 'Enter' key. You should see the following message on the console
```console
You can SSH now: ssh -i p1-key.pem ubuntu@
```
This will generate a .pem file 'p1-key.pem' in your current working directory. Use this key to SSH to the instance created by Pulumi.
Verify that you can see all of the following components installed: mongodb, ycsb test suite, java etc.
