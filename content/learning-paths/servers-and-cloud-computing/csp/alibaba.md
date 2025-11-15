---
# User change
title: "Getting Started with Alibaba Cloud Services"

weight: 6 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
[Alibaba Cloud](https://www.alibabacloud.com/) is a public cloud computing platform. 

As with most cloud service providers, Alibaba Cloud offers a pay-as-you-use [pricing policy](https://www.alibabacloud.com/pricing), including a number of [free](https://www.alibabacloud.com/free) services.

This guide is to help you get started with their [Elastic Compute Service (ECS)](https://www.alibabacloud.com/product/ecs), using [Arm-based](https://www.alibabacloud.com/product/ecs/g8m) processors. This is a general-purpose compute platform, essentially your own personal computer in the cloud.

Detailed instructions are available in the Alibaba Cloud [documentation](https://www.alibabacloud.com/help/en/elastic-compute-service), as well as their [ECS Learning Path](https://www.alibabacloud.com/getting-started/learningpath/ecs).

## Create an account

Before you begin, create an account. For a personal account, click on [Free Trial](https://www.alibabacloud.com/), and follow the on-screen instructions to register. You can select an individual or business account.

If using an organization's existing account, you will likely need to consult with your internal administrator.

## Browse for an appropriate instance type

Alibaba Cloud offers a wide range of [instance families](https://www.alibabacloud.com/help/en/elastic-compute-service/latest/instance-family), covering all performance (and pricing) points. Select an appropriate Arm-based type for your needs. You may also wish to note in which [region](https://ecs-buy.aliyun.com/instanceTypes/#/instanceTypeByRegion) the instance family is available.


You then select an `instance size`, which will be one of a number of pre-defined configurations of a number of processors and available memory. If you are unsure what your compute needs are, don't worry, you can easily experiment with different configurations.

## Create your ECS instance

The easiest way to launch your instance is via the [ECS Console](https://ecs.console.aliyun.com/).

Navigate to `Elastic Compute Service` by search or the menu.

![alibaba #center](images/588897d0-6c77-ee64-c7aa-235cbf460426.webp "Navigate to the ECS Dashboard")

Use the `Create ECS Instance` button to get started. Select `Custom Launch` configuration.

![alibaba #center](images/bf7f23d0-2afb-6a84-60aa-78dc1c27be39.webp "Create Instance")

![alibaba #center](images/2bd139ad-a28b-8e82-8dae-c0d7e54a4ebc.webp "Custom Launch")

### Select a Billing Method

`Subscription`, `Pay-as-you-go`, or `Preemptible Instance` options are available. If you are experimenting initially, select `Preemptible Instance` for the lowest cost. You will be prompted for pricing options later.

![alibaba #center](images/99554b4b-5f15-2dce-4de4-c59e26a3a90e.webp "Select a Billing Method")

### Select Instance Type

Using the `Type-based Selection` tab, set `Architecture` as `ARM`, and `Category` as `General Purpose`, to see the available instance types. If you already know the desired instance type, you can enter this in the filter.

![alibaba #center](images/6ccdd195-7020-b944-4eed-846edf808b2a.webp "Select Instance Type")

### Select OS image

There are many images available on the [Alibaba Cloud Marketplace](https://marketplace.alibabacloud.com/), providing pre-installed or pre-configured setups.

For now, select `Ubuntu` version (e.g. `20.04 64-bit for ARM`) from the pull-down menu.

![alibaba #center](images/c0329674-b751-5aa5-09b8-f2786a338d8e.webp "Select OS Image")

### Other settings

Other settings, such as storage size are selectable. For now, use the default selection. Click `Next` to move to `Networking`. Proceed with the default selection for `Networking`. Click `Next` to move to `System Configurations`.

![alibaba #center](images/08b7ccdd-003f-b23d-de99-471aa11eb285.webp "Configure Storage Options")

![alibaba #center](images/ee8331cb-caec-a3a1-5ded-f7eb56f3e558.webp "Configure Network Options")

### Set a Key Pair and other security settings

To be able to access the instance (see later), you must use a [key pair](https://www.alibabacloud.com/help/en/elastic-compute-service/latest/key-pairs). If this is your first time logging in, use the `Create Key Pair` dialog to create your key. The `public-key` will be downloaded to your local machine. When created, select from the pull-down.

![alibaba #center](images/bf231337-39ba-5d61-6bbb-4c9d2c3f8d6c.webp "Select or create a key pair")

Select `Logon Credentials` and set `Logon Username` to `ecs-user` and an appropriate  `password` if desired.

![alibaba #center](images/8be6f704-0b04-1a19-e156-9f4b5e2f6d10.webp "Set Username and Password for logon")

Other settings such as `Instance Name` and `Description` are free-form for appropriate personal input. Other settings can be left as default.

![alibaba #center](images/fd90820b-5ac5-6fae-831c-1505028e4393.webp "Advanced Settings(Optional)")

In the `Preview` stage, click `Create Instance`. After a few moments, the instance will be available for use.

![alibaba #center](images/e8e336c4-87e7-a8ae-d798-f5d755211270.png "The last step of instance creation")


## Connect to your instance

There are a number of different [Connection methods](https://www.alibabacloud.com/help/en/elastic-compute-service/latest/connection-methods) supported.

Connecting by [SSH Key Pair](https://www.alibabacloud.com/help/en/elastic-compute-service/latest/connect-to-a-linux-instance-by-using-an-ssh-key-pair) is likely the most convenient.

For example, to ssh into your virtual machine instance:

```console
ssh -i <private_key> ecs-user@<public_ip_address>
```

{{% notice Note %}}
Replace `<private_key>` with the private key on your local machine and `<public_ip_address>` with the public IP of the target VM.
{{% /notice %}}

Terminal applications such as [PuTTY](https://www.putty.org/), [MobaXterm](https://mobaxterm.mobatek.net/) and similar can be used to connect via `ssh`.

## Explore your instance

### Run uname

Use the [uname](https://en.wikipedia.org/wiki/Uname) utility to verify that you are using an Arm-based server. For example:

```console
uname -m
```
will identify the host machine as `aarch64`.

### Run hello world

Install the `gcc` compiler. If you are using `Ubuntu`, use the following commands. If not, refer to the [GNU compiler install guide](/install-guides/gcc):

```console
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

```console
gcc hello.c -o hello
./hello
```
