---
# User change
title: "Getting Started with AWS"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
[Amazon Web Services (AWS)](https://aws.amazon.com/) is a public cloud computing platform. 

As with most cloud service providers, AWS offers a pay-as-you-use [pricing policy](https://aws.amazon.com/pricing/), including a number of [free](https://aws.amazon.com/free/) services.

This guide is to help you get started with [Amazon Elastic Compute Cloud (EC2)](https://aws.amazon.com/ec2/) compute services, using Arm-based [Graviton](https://aws.amazon.com/ec2/graviton/) processors. This is a general-purpose compute platform, essentially your own personal computer in the cloud.

Detailed instructions are available in the [Get started tutorial](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) from AWS.

## Create an account

Before you begin, create an account. For a personal account, click on [Create an AWS account](https://aws.amazon.com/), and follow the on-screen instructions to register. See the [Creating an AWS account documentation](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html) for full instructions.

If using an organization's account, you will likely need to consult with your internal administrator. See [this guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create.html) for additional information.

## Browse for an appropriate instance

AWS offers a wide range of instance types, covering all performance (and pricing) points. For an overview of the Graviton instance types, see the [Instance Type Explorer](https://aws.amazon.com/ec2/instance-explorer/), and select `AWS Graviton` from the list of `Processors`. As a general rule, instances with a `g` at the end of their name (for example `M6g`) are Graviton based.

Then, select an `instance size`, which will be one of many pre-defined configurations of processors and available memory. If you are unsure what your compute needs are, don't worry, you can easily experiment with different configurations.

## Create your EC2 instance {#create}

The easiest way to launch your instance is via the [AWS Console](https://console.aws.amazon.com).

Note the `region` you have logged into (for example `us-east-1`) is displayed in the upper right corner. You can select a different location from the pull-down menu if your default region does not offer Graviton servers.

![alt-text #center](https://user-images.githubusercontent.com/67620689/235883425-70e3e428-1f31-4603-9893-0c4034166615.png "Select an appropriate region")

Navigate to `EC2 Dashboard`, either by searching (`Alt+S`) for `EC2`, or via `Services` > `Compute` > `EC2`.

![alt-text #center](https://user-images.githubusercontent.com/67620689/235869564-b45b3d54-f08e-4719-b87e-6c697d26cf49.PNG "Navigate to EC2 Dashboard")

Use the `Launch instance` pull-down menu and select `Launch instance`.

![alt-text #center](https://user-images.githubusercontent.com/67620689/235869570-2a6e437f-e98f-4b1e-90b1-0abeb0c03b67.PNG "Launch an Amazon EC2 instance")

### Name your instance {#name}

Give your instance a meaningful, but arbitrary, name. This is particularly useful when creating multiple instances.

![alt-text #center](https://user-images.githubusercontent.com/87687468/192811901-40232129-2405-4a33-803c-1a9e40934b44.png "Specify a name for the instance")

### Select OS image

There are 1000s of [Amazon Machine Images (AMIs)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) available on the [AWS Marketplace](https://aws.amazon.com/marketplace), providing pre-configured setups.

For now, select `Ubuntu` images from the `Quick Start` list of available images, and version (e.g. `Ubuntu Server 22.04 LTS`) from the pull-down menu.

![alt-text #center](https://user-images.githubusercontent.com/87687468/192594550-95c51ac9-d1cd-4f0d-98f2-a1fce1a78b2d.png "Select a Ubuntu AMI")

In the `Architecture` pull-down menu, select `64-bit (Arm)` to ensure an Arm-based instance type is used.

![alt-text #center](https://user-images.githubusercontent.com/87687468/192595418-c96ad1e5-8a74-43f8-83c7-d5c19f14ff4a.png "Select '64-bit (Arm)' Architecture")

### Select instance type

Select an appropriate `instance type` for your compute needs from the pull-down menu. There is a `Compare instance types` table available if you wish to quickly compare features of different types.

![alt-text #center](https://user-images.githubusercontent.com/87687468/192596029-21b7dcc2-917c-41d0-bda2-3763584f7f00.png "Select an Instance type")

Scrolling down, there is an option to also `configure storage` if necessary.

![alt-text #center](https://user-images.githubusercontent.com/97123064/243395684-c6a3c52d-a9c1-4c35-a31b-8be13faa8246.png "Configure storage options")

### Set a Key Pair

To be able to access the instance, you must use a [key pair](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html).

If this is your first time logging in, you will need to select `Create new key pair`. If you have an existing key pair, select it from the pull-down menu.

![alt-text #center](https://user-images.githubusercontent.com/97123064/243401518-d90737eb-9a19-438d-9f9d-24f6400512b1.png "Select or create a key pair")

If creating a new key pair, name the key pair, then click `Create key pair`. This will initialize the key pair and save the private key to your local machine. Ensure that the private key is safe and accessible on your local machine. 

![alt-text #center](https://user-images.githubusercontent.com/87687468/189891219-ac02d5df-d247-4adb-8e3d-03c0212b9356.png "Create a new key pair")

### Network settings

It is strongly recommended that you create (or use an existing) [security group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html) to ensure that only users on your IP address can access your instance. Simple settings can be set here, such as selecting `My IP` from the `Allow SSH traffic from` pull-down menu. Other settings can be left as default.

![alt-text #center](https://user-images.githubusercontent.com/97123064/243441540-ec1e0f02-29bb-4f4e-b762-90703bd268e4.png "Configure a security group")

For advanced settings, it is recommended that you search `security groups` and create and configure such a group in this dialog. You can then select that group when creating the instance.

### Launch instance

When all options are set, click `Launch instance` to get started. 

![alt-text #center](https://user-images.githubusercontent.com/97123064/243456243-06c6f57d-457a-4b92-9705-8d6abf1870bf.png
 "Launch the instance")

Your compute instance will be created and be available after initialization. Click the `Instance ID` to observe the `Instance state` and other details about your instance.

![alt-text #center](https://user-images.githubusercontent.com/97123064/243434513-1762e92d-0fd6-41b9-8b7a-ff4ac87cf996.png "A successful instance launch message with Instance ID")

Once the `Instance state` reports that it is `Running`, you can connect to the instance. Click on the `Instance ID` to display the `Instance Summary` view which includes more details about your instance. You can also access this view from the list of `Instances` on the `EC2 dashboard`.

![alt-text #center](https://user-images.githubusercontent.com/97123064/243447184-b9e0854b-619d-4b48-80a4-5536a318cbf5.png "Instance ID is shown and Instance state is 'Running'")

## Connect to your instance

You can interact with your instance via the browser (EC2 Instance Connect) or via an SSH terminal application.

### EC2 Instance Connect

In the `Instance summary` view, click `Connect`, and select the `EC2 Instance Connect` tab. Click the `Connect` button to open a terminal in the browser.

![alt-text #center](https://user-images.githubusercontent.com/67620689/235869820-d1d697fc-934f-42e5-94ab-aa013a6d7588.PNG "Connect to the EC2 instance from the browser")

Once connected, you are now ready to use your instance.

### SSH client Connect

You can connect to the instance with your preferred SSH client. In the `Instance summary` view, click `Connect`, and select the `SSH client` tab to see the command used to launch the native SSH client.

![alt-text #center](https://user-images.githubusercontent.com/67620689/235870001-20716b2b-8d95-468b-bccb-b44bba7a2303.PNG "Connect to the EC2 instance with an SSH client")

For example if using `ubuntu` image:

```bash
ssh -i <private_key> ubuntu@<public_ip_address>
```
Terminal applications such as [PuTTY](https://www.putty.org/), [MobaXterm](https://mobaxterm.mobatek.net/) and similar can be used.

Different Linux distributions have different default usernames you can use to connect. 

[Default usernames](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connection-prereqs.html) for AMIs are listed in a table. Find your operating system and see the default username you should use to connect.

Once connected, you are now ready to use your instance.

## Explore your instance

### Run uname

Use the [uname](https://en.wikipedia.org/wiki/Uname) utility to verify that you are using an Arm-based server. For example:

```bash
uname -m
```
will identify the host machine as `aarch64`.

### Run hello world

Install the `gcc` compiler. If you are using `Ubuntu`, use the following commands. If not, refer to the [GNU compiler install guide](/install-guides/gcc):

```bash
sudo apt-get update
sudo apt install -y gcc
```

Using a text editor of your choice, create a file named `hello.c` with the contents below:

```C
#include <stdio.h>
int main(){
    printf("hello world\n");
    return 0;
}
```
Build and run the application:

```bash
gcc hello.c -o hello
./hello
```

The output is shown below:

```output
hello world
```
