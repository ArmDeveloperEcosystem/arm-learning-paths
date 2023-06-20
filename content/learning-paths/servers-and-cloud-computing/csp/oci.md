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

![alt-text #center](https://user-images.githubusercontent.com/97123064/244114923-3c25e3c2-34b5-4d3b-8779-c96a899ef079.png "Navigate to the `Compartments` page")

Use the `Create Compartment` button to start configuring your compartment.

![alt-text #center](https://user-images.githubusercontent.com/97123064/244119606-a04407f5-71ec-4560-8535-8e92148ad405.png "Click on 'Create Compartment'")

Create a compartment with a meaningful name (and optional description), for example `Ampere_A1_instances`. When finished, click `Create Compartment`. Full details on using compartments are described in the Oracle [documentation](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/managingcompartments.htm).

![alt-text #center](https://user-images.githubusercontent.com/97123064/244123626-52cc723d-ddd6-478d-88aa-7161c1d5f1c4.png "Create a name and description for the compartment")

## Create your compute instance

Search for `Instances` or navigate the menu to `Compute` > `Instances`.

![alt-text #center](https://user-images.githubusercontent.com/97123064/244126707-4c184318-fc42-4906-955b-e9d0796eb269.png "Navigate to the 'Instances' page")

Use the `Create Instance` button to get to the `Create compute instance` dialog.

![alt-text #center](https://user-images.githubusercontent.com/97123064/244178554-1b9e12bd-032f-42b2-b351-48df22db7dec.png "Click on 'Create instance'")

### Name your instance

Give your instance a meaningful, but arbitrary, name. This is particularly useful when creating multiple instances. Select the `compartment` you created above to be the location for this instance.

![alt-text #center](https://user-images.githubusercontent.com/97123064/244482401-5a4ea63b-68c7-4e41-a19e-846fadcb15a9.png "Specify a name for the instance and select your compartment")

### Placement

These settings are generally left as default. See the Oracle [documentation](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm) for a full description.

![alt-text #center](https://user-images.githubusercontent.com/97123064/244480624-0cb7112f-3b14-48e1-a68c-dd995fb5bc45.png "Choose availability domain placement")

### Select instance image and shape

Click the `Edit` button to configure which OS image and instance shape you will use.

![alt-text #center](https://user-images.githubusercontent.com/97123064/244479595-178b251b-9357-4aa0-96bc-1f7802798da0.png "Click 'Edit' to change the image and shape")

Click `Change image` to select the operating system image. 

![alt-text #center](https://user-images.githubusercontent.com/97123064/244734737-478d4f93-02da-434a-946b-200d08c7c415.png "Click `Change image'")

Several images are available from the [marketplace](https://cloudmarketplace.oracle.com/marketplace), but for now, select a standard image, such as `Canonical Ubuntu 22.04` from the list of `Platform images`. Click `Select image` to confirm.

![alt-text #center](https://user-images.githubusercontent.com/97123064/244742845-8f3b5bb8-f59b-407f-a77a-fb17ffe0cf43.png "Choose a standard image")

Click `Change shape`, to select the instance type and processor series.

![alt-text #center](https://user-images.githubusercontent.com/97123064/244734750-4477f282-02b4-428b-8c7b-448be8ec31ff.png "Click `Change shape'")

Select the `Ampere` Arm-based processor shape series. Select the `Shape name` (for example `VM.Standard.A1.Flex`), and use slider to select the number of processors you wish to use. At the time of writing, the free tier allows up to 4 Ampere processors (across all instances) to be used. Click `Select shape` to confirm.

![alt-text #center](https://user-images.githubusercontent.com/97123064/244744932-bed21937-bfd7-4643-b2d8-5e0582873103.png "Choose an Ampere Arm-based processor shape")

### Networking

These settings can likely be left as default. Ensure that a public IP address is assigned so that you can access the instance.

![alt-text #center](https://user-images.githubusercontent.com/97123064/244747189-b3f40d99-ffe0-4768-a348-6fa8b3e92d74.png "Configure network settings if necessary")

### Add SSH keys

To be able to access the instance, you must use a [key pair](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingkeypairs.htm). Use the dialog to generate a new key pair and download the private key to your local machine, or you can upload an existing public key if you have one.

Note that if you do not generate a key and have access to the private key, you will not be able to connect to the instance.

![alt-text #center](https://user-images.githubusercontent.com/97123064/244751504-5c258c49-f53d-4afc-9fbd-e87e086ed15c.png "Create or upload a key pair")

### Boot volume and other advanced options

These can likely be left as default. See the Oracle [documentation](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/bootvolumes.htm) for settings information if necessary.

![alt-text #center](https://user-images.githubusercontent.com/97123064/244750495-cbfceecd-ede0-4b9c-a896-921823f514f3.png "Configure boot volume and advanced options if necessary")

### Launch instance

When all options are set, click `Create` to get started. 

![alt-text #center](https://user-images.githubusercontent.com/97123064/244753930-375d8b53-9f1f-4fe4-95ba-aac6d554c05a.png "Create the VM instance")

Your compute instance will be created and be available after initialization, when status is shown as `RUNNING`. Note the `Public IP address` and `Username` of your instance as you will need these to connect to your instance.

![alt-text #center](https://user-images.githubusercontent.com/97123064/244758586-8d9c0515-d8bb-4434-8bd2-83362d4e4ac6.png "Confirm the instance is running and note instance details")

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
