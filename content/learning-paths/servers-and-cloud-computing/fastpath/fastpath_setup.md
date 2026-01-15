---
title: "Setup Fastpath Instance"

weight: 6

layout: "learningpathall"
---
With newly compiled kernels ready and waiting on the build instance, it's time to set up the *fastpath* host. 

The *fastpath* host will manage testing against the system under test (SUT) and coordinate benchmarking runs.

## Provision the Fastpath host

{{% notice Note %}}
The following steps involve launching an EC2 instance.  You can perform all EC2 instance creation steps via the AWS Management Console instead or AWS CLI.  For step-by-step instructions to bring up an EC2 instance via the console, consult the [Compute Service Provider learning path](/learning-paths/servers-and-cloud-computing/csp/) for detailed instructions.  A tutorial from AWS is also available via [Get started with Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html).
{{% /notice %}}

Create build host with the following specifications:

1. **Name** — *fastpath-host*
2. **Operating system** — *Ubuntu*
3. **AMI** — *Ubuntu 24.04 LTS (Arm)*
4. **Architecture** — *64-bit Arm*
5. **Instance type** — `c8g.24xlarge`
6. **Key pair** — *Select or create a key for SSH*
7. **Security group** — *allow SSH inbound from your IP and cluster peers*
8. **Storage** — *200 GB gp3*

{{< tabpane >}}
  {{< tab header="AWS Console" img_src="/learning-paths/servers-and-cloud-computing/fastpath/images/ec2_setup.png">}}
  {{< /tab >}}

  {{< tab header="AWS CLI" language="shell">}}
# Replace the placeholders with values from your account/environment
aws ec2 run-instances \
  --image-id resolve:ssm:/aws/service/canonical/ubuntu/server/24.04/stable/current/arm64/hvm/ebs-gp3/ami-id \
  --instance-type c8g.4xlarge \
  --key-name <KEY_PAIR_NAME> \
  --subnet-id <SUBNET_ID> \
  --security-group-ids <SECURITY_GROUP_ID> \
  --associate-public-ip-address \
  --block-device-mappings '[{"DeviceName":"/dev/sda1","Ebs":{"VolumeSize":200,"VolumeType":"gp3","DeleteOnTermination":true}}]' \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=fastpath-host},{Key=fastpath:role,Value=controller}]'
  {{< /tab >}}

  {{< tab header="CloudFormation" language="yaml">}}

cat <<'EOF' > fastpath-host.yaml

# README FIRST!
#
# 1. Click the copy icon to save this file to your clipboard.
# 2. Paste it into your terminal, it will be saved as `fastpath-host.yaml`
# 3. Go to the CloudFormation console at https://us-east-1.console.aws.amazon.com/cloudformation/home
# 4. Click "Create stack -> With new resources (standard)"
# 5. Choose "Upload a template file" in the CloudFormation console.
# 6. Name the stack "fastpath-host", enter remaining required values, then click "Submit" to create the stack.

AWSTemplateFormatVersion: '2010-09-09'
Description: >-
  Fastpath Learning Path - Fastpath host (controller) instance for benchmarking orchestration.

Parameters:
  LatestUbuntuAmiId:
    Type: 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    Default: /aws/service/canonical/ubuntu/server/24.04/stable/current/arm64/hvm/ebs-gp3/ami-id
    Description: SSM parameter for the latest Ubuntu 24.04 LTS (Arm) AMI.
  InstanceType:
    Type: String
    Default: c8g.4xlarge
    AllowedValues:
      - c8g.4xlarge
      - c8g.8xlarge
      - c8g.12xlarge
    Description: Instance size for the Fastpath host.
  KeyPairName:
    Type: AWS::EC2::KeyPair::KeyName
    Description: Existing EC2 key pair to enable SSH access.
  VpcId:
    Type: AWS::EC2::VPC::Id
    Description: VPC where the Fastpath host will run.
  SubnetId:
    Type: AWS::EC2::Subnet::Id
    Description: Subnet (public or private with outbound access) for the Fastpath host.
  SSHAllowedCidr:
    Type: String
    Default: 0.0.0.0/0
    Description: CIDR block allowed to SSH into the Fastpath host.
  FastpathSecurityGroupId:
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
  HasFastpathPeer: !Not [ !Equals [ !Ref FastpathSecurityGroupId, '' ] ]

Resources:
  FastpathSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Enable SSH access for the Fastpath host
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
          Value: fastpath-host-sg

  FastpathHost:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: !Ref LatestUbuntuAmiId
      InstanceType: !Ref InstanceType
      KeyName: !Ref KeyPairName
      SubnetId: !Ref SubnetId
      SecurityGroupIds:
        - !Ref FastpathSecurityGroup
      BlockDeviceMappings:
        - DeviceName: /dev/sda1
          Ebs:
            VolumeSize: !Ref RootVolumeSizeGiB
            VolumeType: gp3
            Encrypted: true
            DeleteOnTermination: true
      Tags:
        - Key: Name
          Value: fastpath-host
        - Key: fastpath:role
          Value: controller

Outputs:
  InstanceId:
    Description: ID of the Fastpath host EC2 instance.
    Value: !Ref FastpathHost
  PublicIp:
    Description: Public IPv4 address for the Fastpath host (if applicable).
    Value: !GetAtt FastpathHost.PublicIp
  PrivateIp:
    Description: Private IPv4 address for intra-cluster communication.
    Value: !GetAtt FastpathHost.PrivateIp
  SecurityGroupId:
    Description: Security group attached to the Fastpath host.
    Value: !Ref FastpathSecurityGroup
EOF

  {{< /tab >}}
{{< /tabpane >}}

When the instance reports a `running` state, note the public and private IP addresses as FASTPATH_PUBLIC_IP and FASTPATH_PRIVATE_IP.  You'll need these values later.

## Install Fastpath Dependencies

Repeat the dependency installation process so the *fastpath* host has the same toolchain and helper scripts as the build machine.

1. SSH into the `c8g.4xlarge` *fastpath* host using the configured key pair.

2. Open the [Install and Clone section](https://localhost:1313/install-guides/kernel-build/#install-and-clone) of the install guide from your workstation.

3. Run each command from that section on the *fastpath* machine.  It should be similar to the following (always refer to the above link for the latest command line):

    ```output
    $ sudo apt update && sudo apt install -y git python3 python3-pip python3-venv build-essential bc rsync dwarves flex bison libssl-dev libelf-dev btop yq

    WARNING: apt does not have a stable CLI interface. Use with caution in scripts.
    Hit:1 http://us-east-1.ec2.ports.ubuntu.com/ubuntu-ports noble InRelease
    Get:2 http://us-east-1.ec2.ports.ubuntu.com/ubuntu-ports noble-updates InRelease [126 kB]
    ...
    0 upgraded, 104 newly installed, 0 to remove and 43 not upgraded.
    Setting up build-essential (12.10ubuntu1) ...
    Setting up libssl-dev:arm64 (3.0.13-0ubuntu3.6) ...
    Setting up python3-pip (24.0+dfsg-1ubuntu1.3) ...

    $ cd
    $ git clone https://github.com/geremyCohen/arm_kernel_install_guide.git ~/arm_kernel_install_guide
    $ cd ~/arm_kernel_install_guide && chmod +x scripts/*.sh

    Cloning into 'arm_kernel_install_guide'...
    ```

## Copy kernels between build and Fastpath instances

When we begin testing, the *fastpath* instance will push the compiled kernels to the SUT for testing.  But as of now, the kernels are still on the build instance. This next step copies the kernels from the build instance to the new *fastpath* instance.

1. Locate the value you recorded earlier for BUILD_PRIVATE_IP.

2. On the *fastpath* instance, ```cd``` into the `arm_kernel_install_guide` folder you just cloned. 

3. Run the `pull_kernel_artifacts.sh` script, substituting BUILD_PRIVATE_IP with the private IP of the build instance:

    ```command
    cd ~/arm_kernel_install_guide
    ./scripts/pull_kernel_artifacts.sh --host 172.31.110.110 
    ```

    ```output
    [2026-01-08 18:35:14] Pulling kernel artifacts:
    [2026-01-08 18:35:14]   Host        : 172.31.110.110
    [2026-01-08 18:35:14]   SSH user    : ubuntu
    [2026-01-08 18:35:14]   Remote dir  : /home/ubuntu/kernels
    [2026-01-08 18:35:14]   Local dir   : /home/ubuntu/kernels
    [2026-01-08 18:35:14]   Versions    : auto-detected
    [2026-01-08 18:35:15] Copying 6.18.1-ubuntu+/Image.gz
    [2026-01-08 18:35:16] Copying 6.18.1-ubuntu+/modules.tar.xz
    [2026-01-08 18:35:18] Copying optional 6.18.1-ubuntu+/config.stock
    [2026-01-08 18:35:18] Copying 6.19.0-rc1-ubuntu+/Image.gz
    [2026-01-08 18:35:19] Copying 6.19.0-rc1-ubuntu+/modules.tar.xz
    [2026-01-08 18:35:21] Copying optional 6.19.0-rc1-ubuntu+/config.stock
    [2026-01-08 18:35:21] Artifact pull complete.
    ```


When the script completes, the *fastpath* host is ready with the kernels it needs for testing.

## Power down the build machine

After copying the artifacts from the build machine, stop (or terminate it) to avoid incurring additional costs.  If you wish to keep it around for future kernel builds, stopping it is sufficient.


{{% notice Note %}}
If you do decide to keep the machine around as a kernel copy host, you can modify it to a smaller instance type such as `c8g.4xlarge` to save on costs when its running.  The larger 24xlarge instance is only needed during kernel compilation.
{{% /notice %}}

## Configure the Fastpath host

With kernels copied over, the final step is to install and configure the *fastpath* software onto the *fastpath* host.  From the same folder, run the host configuration script targeting localhost:

1. Stay on the *fastpath* host and ensure you are in the cloned repository.  If needed, you can easily navigate there again:

    ```command
    cd ~/arm_kernel_install_guide
    ```

2. Run the *fastpath* host setup script, targeting localhost (the current machine):

    ```command
    ./scripts/configure_fastpath_host.sh --host localhost
    ```

    ```output
    [2026-01-08 18:35:27] Configuring fastpath host localhost (non-interactive mode)
    [2026-01-08 18:35:27] Installing prerequisites
    ...
    [2026-01-08 18:36:10] Fastpath host setup complete.
    ```

Note that the script creates a Python virtual environment at `~/venv` and installs the *fastpath* CLI alongside its dependencies:

```command
source ~/venv/bin/activate
which python
```

```output
/home/ubuntu/venv/bin/python
```

{{% notice Note %}}
Whenever you log back into the machine, make sure to activate the virtual environment (the above command line) before running any *fastpath* commands.
{{% /notice %}}

With the *fastpath* host configured, you're now ready to provision the system under test (SUT) and verify connectivity between them.
