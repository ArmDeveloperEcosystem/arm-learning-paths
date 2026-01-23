---
title: "Setup Build Instance"

weight: 3

layout: "learningpathall"
---

## Provision the build host

CPU-optimized instances compile kernels quickly, so in our example, an AWS Graviton `m6g.12xlarge` instance is used. It will be referred to as the *build* machine throughout the rest of the guide.

{{% notice Note %}}
The following steps involve launching an EC2 instance.  You can perform all EC2 instance creation steps via the AWS Management Console instead or AWS CLI.  For step-by-step instructions to bring up an EC2 instance via the console, consult the [Compute Service Provider learning path](/learning-paths/servers-and-cloud-computing/csp/) for detailed instructions.  A tutorial from AWS is also available via [Get started with Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html).
{{% /notice %}}

Create build host with the following specifications:

1. **Name** — *fastpath-build*
2. **Operating system** — *Ubuntu*
3. **AMI** — *Ubuntu 24.04 LTS (Arm)*
4. **Architecture** — *64-bit Arm*
5. **Instance type** — `m6g.12xlarge`
6. **Key pair** — *Select or create a key for SSH*
7. **Security group** — *allow SSH inbound from your IP and cluster peers*
8. **Storage** — *200 GB gp3*

There are many different ways to create this instance, and a few different methods are demonstrated below.  Choose the method which suits you best.  

{{< tabpane >}}
  {{< tab header="AWS Console" img_src="/learning-paths/servers-and-cloud-computing/fastpath/images/ec2_setup.png">}}
  {{< /tab >}}

  {{< tab header="AWS CLI" language="shell">}}
# Replace the placeholders with values from your account/environment
aws ec2 run-instances \
  --image-id resolve:ssm:/aws/service/canonical/ubuntu/server/24.04/stable/current/arm64/hvm/ebs-gp3/ami-id \
  --instance-type m6g.12xlarge \
  --key-name <KEY_PAIR_NAME> \
  --subnet-id <SUBNET_ID> \
  --security-group-ids <SECURITY_GROUP_ID> \
  --associate-public-ip-address \
  --block-device-mappings '[{"DeviceName":"/dev/sda1","Ebs":{"VolumeSize":200,"VolumeType":"gp3","DeleteOnTermination":true}}]' \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=fastpath-build},{Key=fastpath:role,Value=build}]'
  {{< /tab >}}

  {{< tab header="CloudFormation" language="yaml" >}}

cat <<'EOF' > build-host.yaml

# README FIRST!
#
# 1. Click the copy icon to save this file to your clipboard.
# 2. Paste it into your terminal, it will be saved as `build-host.yaml`
# 3. Go to the CloudFormation console at https://us-east-1.console.aws.amazon.com/cloudformation/home
# 4. Click "Create stack -> With new resources (standard)"
# 5. Choose "Upload a template file" in the CloudFormation console.
# 6. Name the stack "fastpath-build", enter remaining required values, then click "Submit" to create the stack.


AWSTemplateFormatVersion: '2010-09-09'
Description: >-
  Fastpath Learning Path - Build host for kernel compilation (Ubuntu 24.04 LTS on Graviton m6g.12xlarge).

Parameters:
  LatestUbuntuAmiId:
    Type: 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    Default: /aws/service/canonical/ubuntu/server/24.04/stable/current/arm64/hvm/ebs-gp3/ami-id
    Description: SSM parameter for the latest Ubuntu 24.04 LTS (Arm) AMI.
  InstanceType:
    Type: String
    Default: m6g.12xlarge
    AllowedValues:
      - m6g.12xlarge
      - m6g.8xlarge
      - m6g.4xlarge
    Description: Instance size for the build host.
  KeyPairName:
    Type: AWS::EC2::KeyPair::KeyName
    Description: Existing EC2 key pair to enable SSH access.
  VpcId:
    Type: AWS::EC2::VPC::Id
    Description: VPC where the build host will run.
  SubnetId:
    Type: AWS::EC2::Subnet::Id
    Description: Subnet (preferably public) for the build host.
  SSHAllowedCidr:
    Type: String
    Default: 0.0.0.0/0
    Description: CIDR block allowed to SSH into the build host.
  BuildSecurityGroupId:
    Type: String
    Default: ''
    Description: Security group ID of the Fastpath host to allow peer-to-peer SSH.
  RootVolumeSizeGiB:
    Type: Number
    Default: 200
    MinValue: 100
    MaxValue: 1024
    Description: Size (GiB) of the gp3 root volume.

Conditions:
  HasFastpathPeer: !Not [ !Equals [ !Ref BuildSecurityGroupId, '' ] ]

Resources:
  BuildSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Enable SSH access for Fastpath build host
      VpcId: !Ref VpcId
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 22
          ToPort: 22
          CidrIp: !Ref SSHAllowedCidr
      SecurityGroupEgress:
        - IpProtocol: -1
          CidrIp: 0.0.0.0/0
      Tags:
        - Key: Name
          Value: fastpath-build-sg

  BuildHost:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: !Ref LatestUbuntuAmiId
      InstanceType: !Ref InstanceType
      KeyName: !Ref KeyPairName
      SubnetId: !Ref SubnetId
      SecurityGroupIds:
        - !Ref BuildSecurityGroup
      BlockDeviceMappings:
        - DeviceName: /dev/sda1
          Ebs:
            VolumeSize: !Ref RootVolumeSizeGiB
            VolumeType: gp3
            Encrypted: true
            DeleteOnTermination: true
      Tags:
        - Key: Name
          Value: fastpath-build
        - Key: fastpath:role
          Value: build

Outputs:
  InstanceId:
    Description: ID of the build host EC2 instance.
    Value: !Ref BuildHost
  PublicIp:
    Description: Public IPv4 address (if assigned) to reference as BUILD_PUBLIC_IP.
    Value: !GetAtt BuildHost.PublicIp
  PrivateIp:
    Description: Private IPv4 address to reference as BUILD_PRIVATE_IP.
    Value: !GetAtt BuildHost.PrivateIp
  SecurityGroupId:
    Description: Security group attached to the build host.
    Value: !Ref BuildSecurityGroup
EOF

  {{< /tab >}}
{{< /tabpane >}}

When the instance reports a `running` state, note the public and private IP addresses as BUILD_PUBLIC_IP and BUILD_PRIVATE_IP.  You'll need these values later.

## Clone the Kernel Build repository on the build machine

The Kernel Build repository contains build scripts and configuration files needed to easily compile kernels. To clone the repository:

1. SSH into the `m6g.12xlarge` host using the configured key pair.

    ```output
    ssh -i ~/.ssh/gcohen1.pem ubuntu@34.216.87.65

    $ ssh -i ~/.ssh/gcohen1.pem ubuntu@54.174.185.226

    Warning: Permanently added '54.174.185.226' (ED25519) to the list of known hosts.
    Welcome to Ubuntu 24.04.3 LTS (GNU/Linux 6.14.0-1018-aws aarch64)

    System information as of Thu Jan  8 18:12:07 UTC 2026

      System load:  0.35               Users logged in:        0
      Memory usage: 0%                 IPv4 address for ens66: 172.31.110.110

    Last login: Thu Jan  8 18:12:14 2026 from 217.140.103.82
    ubuntu@ip-172-31-110-110:~$
    ```

2. Open the [Install and Clone section](https://localhost:1313/install-guides/kernel-build/#install-and-clone) of the install guide from your workstation.

3. Run each command from that section on the build machine.  It should be similar to the following (always refer to the above link for the latest command line):


```output
$ sudo apt update
$ sudo apt install -y git python3 python3-pip python3-venv build-essential bc rsync dwarves flex bison libssl-dev libelf-dev btop yq
$ cd
$ git clone https://github.com/geremyCohen/arm_kernel_install_guide.git ~/arm_kernel_install_guide
$ cd ~/arm_kernel_install_guide
$ chmod +x scripts/*.sh

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.
Hit:1 http://us-east-1.ec2.ports.ubuntu.com/ubuntu-ports noble InRelease
Get:2 http://us-east-1.ec2.ports.ubuntu.com/ubuntu-ports noble-updates InRelease [126 kB]
Get:3 http://us-east-1.ec2.ports.ubuntu.com/ubuntu-ports noble-backports InRelease [126 kB]
Get:4 http://ports.ubuntu.com/ubuntu-ports noble-security InRelease [126 kB]
...
0 upgraded, 104 newly installed, 0 to remove and 43 not upgraded.
Setting up build-essential (12.10ubuntu1) ...
Setting up libssl-dev:arm64 (3.0.13-0ubuntu3.6) ...
Setting up python3-pip (24.0+dfsg-1ubuntu1.3) ...
Cloning into 'arm_kernel_install_guide'...
```

## Building with the Kernel Build utility script

With the repository cloned, you can now produce kernels with *fastpath* support.

Normally, to manually build, you'd have to:

  - Update the host and install proper versions of every kernel build dependency
  - Find and utilize the current stock kernel config 
  - Clone the upstream kernel tree to fetch the desired versions and clean the tree between builds
  - For each kernel version, copy the base config into the workspace, and append all *fastpath*-specific options
  - Run tuxmake for each kernel with the proper options
  - Repeat the entire process for the second tag, ensuring the builds don’t collide
  - Verify both kernel directories contain the required files
  
But do not fear... Using ```scripts/kernel_build_and_install.sh``` bundles all those steps together in a single easy-to-use command.

### Which kernels should you build and test against with Fastpath?
The answer to this question depends on what you are trying to accomplish.  

If you are running through the *fastpath* tutorial for the first time and getting used to how it works, its fine to use the arbitrary kernel versions given in *fastpath* Example 2, which are v6.18.1 and v6.19-rc1.

Once you are familiar with the process and you wish to explore and test further, choose any specific kernel versions, based on your use case.  

## Compile and build Fastpath-enabled kernels 6.18.1 and 6.19-rc1

To run the script with *fastpath* options:

1. On the build machine, ```cd``` into the `arm_kernel_install_guide` folder you just cloned. 

```command
cd ~/arm_kernel_install_guide
```

```output
ubuntu@ip-172-31-110-110:~/arm_kernel_install_guide$
```

2. Open the [Custom tags with *fastpath* enabled](http://localhost:1313/install-guides/kernel-build/#2-custom-tags-with-fastpath-enabled) section from the install guide, and follow the instructions to run the build script. It should be similar to the following (always refer to the above link for the latest command line):

```output
$ ./scripts/kernel_build_and_install.sh --tags v6.18.1,v6.19-rc1 --fastpath true

[2026-01-08 18:13:14] Updating apt metadata
Kernel build settings:
  Repo:                git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git
  Branch:              linux-rolling-stable
  Tags:                v6.18.1,v6.19-rc1
  Config file:         /boot/config-6.14.0-1018-aws
  Kernel dir base:     /home/ubuntu/kernels/linux
  Output base:         /home/ubuntu/kernels
  Fastpath configs:    true
  64K page size:       false
  Kernel install:      false
...
I: build output in /home/ubuntu/kernels/6.18.1-ubuntu
[2026-01-08 18:32:03] [v6.18.1-1] Build artifacts are located in /home/ubuntu/kernels/6.18.1-ubuntu+
I: build output in /home/ubuntu/kernels/6.19.0-rc1-ubuntu
[2026-01-08 18:32:06] [v6.19-rc1-2] Build artifacts are located in /home/ubuntu/kernels/6.19.0-rc1-ubuntu+
```

The script will now build two kernel images.  This process may take some time -- on a `m6g.12xlarge` instance, expect approximately 30 minutes for both kernel builds to complete.

4. Monitor the console output for the `BUILD COMPLETE` message. 

Once finished, you will be ready to move on to the next step, where you prepare the *fastpath* host.
