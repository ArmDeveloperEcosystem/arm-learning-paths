---
# User change
title: "Getting Started with Oracle OCI"

weight: 6 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
[Oracle Cloud Infrastructure (OCI)](https://oracle.com/cloud/) is a public cloud computing platform. 

As with most cloud service providers, OCI offers a pay-as-you-use [pricing policy](https://www.oracle.com/cloud/pricing/), including a number of [free](https://www.oracle.com/cloud/free/) services.

This guide is to help you get started with [compute services](https://www.oracle.com/cloud/compute/), using Arm-based [Ampere](https://www.oracle.com/cloud/compute/arm/) processors. This is a general-purpose compute platform, essentially your own personal computer in the cloud.

Detailed instructions are available in the Oracle [documentation](https://docs.oracle.com/en-us/iaas/Content/Compute/References/arm.htm#create-instances).

## Create an account

Before you start, creating an account. For a personal account, click on [Sign in to Oracle Cloud](https://www.oracle.com/cloud), and follow the on-screen instructions to log in or register as a new user. You will get immediate access to [OCI Cloud Free Tier](https://www.oracle.com/cloud/free) services.

If using an organization's account, you will likely need to consult with your internal administrator.

Once logged in, you will be presented with the [Oracle Cloud console](https://docs.oracle.com/en-us/iaas/Content/GSG/Concepts/console.htm). 

## Create compartment

If this is your first time logging in, it is recommended to create a `compartment` to store your compute instances. Search for `Compartments` or navigate to `Identity & Security` > `Compartments` from the menu.

![oci1 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/45129984-ae50-4794-893c-9b03bb90a3cb "Navigate to the `Compartments` page")

Use the `Create Compartment` button to start configuring your compartment.

![oci2 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/64f08ccf-3c04-426b-ba01-5d8c8d5f6aed "Click on 'Create Compartment'")

Create a compartment with a meaningful name (and optional description), for example `Ampere_A1_instances`. When finished, click `Create Compartment`. Full details on using compartments are described in the Oracle [documentation](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/managingcompartments.htm).

![oci3 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/55153d88-b8d6-4ec2-a208-e459ee8149f9 "Create a name and description for the compartment")

## Create your compute instance

Search for `Instances` or navigate the menu to `Compute` > `Instances`.

![alt-text #center](https://user-images.githubusercontent.com/97123064/244126707-4c184318-fc42-4906-955b-e9d0796eb269.png "Navigate to the 'Instances' page")

Use the `Create Instance` button to get to the `Create compute instance` dialog.

![alt-text #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/e8e21133-8174-491c-b640-89cda8025031 "Click on 'Create instance'")

### Name your instance

Give your instance a meaningful, but arbitrary, name. This is particularly useful when creating multiple instances. Select the `compartment` you created above to be the location for this instance.

![oci6 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/26beff38-fcbd-4f94-ac7f-f2c90968aef1 "Specify a name for the instance and select your compartment")

### Placement

These settings are generally left as default. See the Oracle [documentation](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm) for a full description.

![oci7 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/c45308b8-44ef-477f-b857-4aa3c4feddcf "Choose availability domain placement")

### Select instance image and shape

Click the `Edit` button to configure which OS image and instance shape you will use.

![oci8 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/43f14faf-b4ba-4a99-82b3-c3940a426854 "Click 'Edit' to change the image and shape")

Click `Change image` to select the operating system image. 

![oci9 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/3e8fb9ee-f047-4705-9d1b-90d1056b177f "Click `Change image'")

Several images are available from the [marketplace](https://cloudmarketplace.oracle.com/marketplace), but for now, select a standard image, such as `Canonical Ubuntu 22.04` from the list of `Platform images`. Click `Select image` to confirm.

![oci10 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/99891969-0f17-4b6f-9c9b-0f14bdc11d1d "Choose a standard image")

Click `Change shape`, to select the instance type and processor series.

![oci11 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/97ebbd4d-1ba6-49bc-b941-ba7a872479c2 "Click `Change shape'")

Select the `Ampere` Arm-based processor shape series. Select the `Shape name` (for example `VM.Standard.A1.Flex`), and use slider to select the number of processors you wish to use. At the time of writing, the free tier allows up to 4 Ampere processors (across all instances) to be used. Click `Select shape` to confirm.

![oci12 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/1e3ce661-ce85-4fc5-a67e-0fbecf6297c6 "Choose an Ampere Arm-based processor shape")

### Networking

These settings can likely be left as default. Ensure that a public IP address is assigned so that you can access the instance.

![oci13 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/f51df044-8bb5-4a90-b480-1b39b04be39f "Configure network settings if necessary")

### Add SSH keys

To be able to access the instance, you must use a [key pair](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingkeypairs.htm). Use the dialog to generate a new key pair and download the private key to your local machine, or you can upload an existing public key if you have one.

Note that if you do not generate a key and have access to the private key, you will not be able to connect to the instance.

![oci14 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/37a03ac4-d6f5-4e32-9523-02dd6542a5df "Create or upload a key pair")

### Boot volume and other advanced options

These can likely be left as default. See the Oracle [documentation](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/bootvolumes.htm) for settings information if necessary.

![oci15 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/74658e9c-4538-4d17-8941-9c14c48434c3 "Configure boot volume and advanced options if necessary")

### Launch instance

When all options are set, click `Create` to get started. 

![oci16 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/4d7f2204-45ad-4864-83b6-954af6c47828 "Create the VM instance")

Your compute instance will be created and be available after initialization, when status is shown as `RUNNING`. Note the `Public IP address` and `Username` of your instance as you will need these to connect to your instance.

![oci17 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/56a4c3d4-90bb-4ac2-9fca-1b5113928295 "Confirm the instance is running and note instance details")

## Connect to your instance

You can connect to the instance with your preferred SSH client. For example, if using `ubuntu` image:

```console
ssh -i <private_key> ubuntu@<public_ip_address>
```

{{% notice Note %}}
Replace `<private_key>` with the private key on your local machine and `<public_ip_address>` with the public IP of the target VM.
{{% /notice %}}

Terminal applications such as [PuTTY](https://www.putty.org/), [MobaXterm](https://mobaxterm.mobatek.net/) and similar can be used.

Detailed instructions are given in the Oracle [documentation](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/accessinginstance.htm).

Once connected, you are now ready to use your instance.

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

The output is shown below:

```output
hello world
```
