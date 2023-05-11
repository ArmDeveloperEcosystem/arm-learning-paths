---
# User change
title: "Getting Started with Oracle OCI"

weight: 6 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
[Oracle Cloud Infrastructure (OCI)](https://oracle.com/cloud/) is a public cloud computing platform. 

As with most cloud service providers, OCI offers a pay-as-you-use [pricing policy](https://www.oracle.com/cloud/pricing/), including a number of [free](https://www.oracle.com/cloud/free/) services.

This guide is to help you get started with [compute services](https://www.oracle.com/cloud/compute/), using Arm-based [Ampere](https://www.oracle.com/cloud/compute/arm/) processors. This is a general purpose compute platform, essentially your own personal computer in the cloud.

Detailed instructions are available in the Oracle [documentation](https://docs.oracle.com/en-us/iaas/Content/Compute/References/arm.htm#create-instances).

## Create an account

Before you start, creating an account. For a personal account, click on [Sign in to Oracle Cloud](https://www.oracle.com/cloud), and follow the on-screen instructions to log in, else register as a new user. You will get immediate access to [OCI Cloud Free Tier](https://www.oracle.com/cloud/free) services.

If using an organization's account, you will likely need to consult with your internal administrator.

Once logged in, you will be presented with the [Oracle Cloud console](https://docs.oracle.com/en-us/iaas/Content/GSG/Concepts/console.htm). 

## Create compartment

If this is your first time logging in, it is recommended to create a `compartment` to store your compute instances. Search for `Compartments`, else navigate the menu to `Identity` > `Compartments`.

Use the `Create Compartment` button to get to the `Create Compartment` dialog. Create a compartment with a meaningful name (and optional description), for example `Ampere_A1_instances`.

Full details on using compartments is described in the Oracle [documentation](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/managingcompartments.htm).

## Create your compute instance

Search for `Instances`, else navigate the menu to `Compute` > `Instances`.

Use the `Create Instance` button to get to the `Create compute instance` dialog.

### Name your instance

Give your instance a meaningful, but arbitrary, name. This is particularly useful when creating multiple instances. Select the above `compartment` in which to create the instance.

### Placement

These settings are generally left as default. See the Oracle [documentation](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm) for a full description.

### Select instance image and shape

Click the `Edit` button to configure which OS image and instance shape you will use.

Click `Change image` to select the operating system image. A number of images are available from the [marketplace](https://cloudmarketplace.oracle.com/marketplace), but for now, select a standard image, such as `Canonical Ubuntu 22.04` from the list of `Platform images`. Click `Select image` to confirm.

Click `Change shape`, and select the `Ampere` Arm-based processor series.

Select the `Shape name` (for example `VM.Standard.A1.Flex`), and use slider to select the number of processors you wish to use. At the time of writing, the free tier allows up to 4 Ampere processors (across all instances) to be used. Click `Select shape` to confirm.


### Networking

These settings can likely be left as default. Ensure that a public IP address is assigned so that you can access the instance.

### Add SSH keys

To be able to access the instance, you must use a [key pair](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingkeypairs.htm). Use the dialog to generate a new key pair, else you can upload an existing public key. Note that if you do not generate a key, you will not be able to connect to the instance.

### Boot volume and other advanced options

These can likely be left as default. See the Oracle documentation for settings information if necessary.

### Launch instance

When all options are set, click `Create` to get started. Your compute instance will be created and be available after initialization, when status is shown as `RUNNING`. Note the `Public IP address` and `Username` of your instance.

## Connect to your instance

You can connect to the instance with your preferred SSH client. For example if using `ubuntu` image:

```console
ssh -i <private_key> ubuntu@<public_ip_address>
```
Terminal applications such as [PuTTY](https://www.putty.org/), [MobaXterm](https://mobaxterm.mobatek.net/) and similar can be used.

Detailed instructions are given in the Oracle [documentation](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/accessinginstance.htm).

## Explore your instance

### Run uname

Use the [uname](https://en.wikipedia.org/wiki/Uname) utility to verify that you are using an Arm-based server. For example:
```console
uname -m
```
will identify the host machine as `aarch64`.

### Run hello world

Install the `gcc` compiler. Assuming you are using `Ubuntu`, use the following commands. If not, refer to the [GNU compiler install guide](/install-guides/gcc):

```console
sudo apt-get update
sudo apt install -y gcc
```

Using a text editor of your choice, create a file `hello.c` with the contents below:

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

