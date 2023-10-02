---
# User change
title: "Automate infrastructure setup for MongoDB performance benchmarking with Pulumi"

weight: 4 # (intro is 1), 2 is first, 3 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Setup environment variables

Export the following environment variables on your local compute to connect to AWS account
```console
export AWS_ACCESS_KEY_ID=<access-key-id>
export AWS_SECRET_ACCESS_KEY=<secret-access-key>
export AWS_SESSION_TOKEN=<session-token>
```

## Install awscli on Ubuntu 22.04
```console
sudo apt install awscli -y
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
Execute the following script to set the private key parameters
```bash
./get-key.sh
```

## Install python on Ubuntu 22.04
```bash
sudo apt install python-is-python3 -y
sudo apt install python3-pip -y
sudo apt install python3.10-venv
```

## Install gator on Ubuntu 22.04
[gator](https://github.com/ARM-software/gator) is a target agent (daemon), part of Arm Streamline, a set of performance analysis tools. Use the following commands to build it from source.

```bash
git clone https://github.com/ARM-software/gator.git
pushd gator
./build-linux.sh
popd
```

## Install Pulumi on Ubuntu 22.04
[Pulumi](https://www.pulumi.com/) is a multi-language infrastructure as code tool. Pulumi is [open source](https://github.com/pulumi/pulumi) and makes it easy to deploy cloud infrastructure.

You can install Pulumi with the following command:

```bash
curl -fsSL https://get.pulumi.com | sh
```
Run the following command to add Pulumi to local environment
```bash
source $HOME/.bashrc
```
Check the version of Pulumi with the following:

```bash
pulumi version
v3.78.0
```
To learn more about Pulumi, check out the [install guide](https://learn.arm.com/install-guides/pulumi/).

## Setup configurations 

Clone the following github repo on your local computer

```bash
git clone https://github.com/pbk8s/pulumi-ec2.git
```

Execute the following python script to install all dependencies

```bash
./python-setup.sh
```

Navigate to 'pulumi-ec2' folder and open the 'Pulumi.yaml' file

```bash
cd pulumi-ec2
vi Pulumi.yaml
```

Edit the default aws region to your region of choice

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

Edit the __main__.py file to change the availabilty zone of your network subnet

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

Note: The security groups created by this script are lot less restrictive, to simplify the deployment process and to remove addtional complexities. Please modify the ingress/egress rules as per your organizations' policy.

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

Before executing the Pulumi commands, copy the gatord binary generated earlier to the Pulumi working directory

```bash
cp <gator-build-path>/gator/build-native-gcc-rel/gatord <path-to-pulumi-working-directory>/pulumi-ec2/
```

## Pulumi commands 

Execute the following command to set the AWS region where you'd like to deploy the resources:

```bash
pulumi config set aws:region us-east-1
```
Enter the name of the new stack you'd like to create.

Now, deploy the Pulumi stack with the following command

```console
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
Select yes to create the stack. Once successfully completed, you can ssh to the instance using the 'public_ip' or 'public_dns' property. Verify that you can see all of the following components installed: mongodb, ycsb test suite etc.

Run a few tests from previous pages to verify all of the components installed properly.