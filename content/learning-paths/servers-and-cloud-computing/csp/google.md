---
# User change
title: "Getting Started with Google Cloud Platform"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
[Google Cloud](https://cloud.google.com/) is a public cloud computing platform. 

As with most cloud service providers, Google Cloud offers a pay-as-you-use [pricing policy](https://cloud.google.com/pricing), including a number of [free](https://cloud.google.com/free/docs/free-cloud-features) services.

This section is to help you get started with [Google Cloud Compute Engine](https://cloud.google.com/compute) compute services, using Arm-based [Tau T2A](https://cloud.google.com/tau-vm) Virtual Machines. This is a general purpose compute platform, essentially your own personal computer in the cloud.

Detailed instructions are available in the Google Cloud [documentation](https://cloud.google.com/compute/docs/instances). 

## Create an account

Before you begin, create an account. For a personal account, click on [Get started for free](https://cloud.google.com/), and follow the on-screen instructions to register. You can use an existing Google account if you have one.

If using an organization's account, you will likely need to consult with your internal administrator. See [this guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create.html) for additional information.

## Browse for an appropriate instance

Google Cloud offers a wide range of instance types, covering all performance (and pricing) points. For an overview of the Tau T2A instance types, see the [General-purpose machine family](https://cloud.google.com/compute/docs/general-purpose-machines#t2a_machines) overview, and select `AWS Graviton` from the list of `Processors`. 

Also note in which [region](https://cloud.google.com/compute/docs/regions-zones#available) these servers are available.

## Create your Compute Engine instance

The easiest way to launch your instance is via the [Google Cloud Console](https://console.cloud.google.com). Activities can be separated by `Project`. By default, when you first login, you will be in `My First Project`. If you wish to rename this, navigate to `IAM & Admin` > `Settings`, and rename. You can also create new project(s) from the pull down menu, or [directly](https://console.cloud.google.com/projectcreate).

Select `Compute Engine` from the `Quick access` section, if shown. Else navigate to `Compute Engine` > `VM instances`. If it is your first time, you will be prompted to enable `Compute Engine API`. Go to the [VM instances](https://console.cloud.google.com/compute/instances) area of the console.

Click the `CREATE INSTANCE` button.

![image](https://user-images.githubusercontent.com/67620689/202090364-2946214c-2347-4538-b2b0-3a36f45caee0.PNG)

### Name your instance

Give your instance a meaningful, but arbitrary, name. This is particularly useful when creating multiple instances. You can optionally add [labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels) as additional identifiers.

![image](https://user-images.githubusercontent.com/67620689/202098830-532b5dc8-f6b5-4cff-931c-ec41edd08516.PNG)

### Select Region and Zone for your instance.

Select an appropriate `region` and `zone` that supports Arm-based servers. Check the latest information about [available regions and zones](https://cloud.google.com/compute/docs/regions-zones#available).

![image](https://user-images.githubusercontent.com/67620689/202097168-6208b6ae-3627-47b3-a397-7783769e6727.PNG)

### Machine configuration

Select `T2A` from the `Series` pull down menu. Then select an appropriate `Machine type` configuration for your needs.

![image](https://user-images.githubusercontent.com/67620689/203740482-d820ced1-5eeb-4c07-99a3-18a7a7511966.PNG)

### Boot disk configuration

Click the `CHANGE` button if you wish to change the virtual disk size, or the operating system or version, for example to `Ubuntu 20.04 LTS`. Be sure to select Arm compatible image.

![image](https://user-images.githubusercontent.com/67620689/204448755-f1259724-a386-4dc3-9b88-8ece7057d4de.PNG)

## Security and SSH key pair

By default, you can access your instance via the browser. If you wish to use an SSH terminal, you must [create](https://cloud.google.com/compute/docs/connect/create-ssh-keys) and [add](https://cloud.google.com/compute/docs/connect/add-ssh-keys)  an appropriate SSH key pair.

![image](https://user-images.githubusercontent.com/67620689/225616099-8fc7791a-24b3-4195-b957-154eaca43080.PNG)

### Other options

Other options, such as `Confidential VM service`, can optionally be enabled. For now, leave as default (disabled). See the Google Cloud documentation for an explanation of these configurations.

When satisfied, click `CREATE`. After a few moments the instance will be available, and listed in your [console](https://console.cloud.google.com/compute/instances).

![image](https://user-images.githubusercontent.com/67620689/202098038-7bfb0b6c-af18-4d5c-92a8-ca90a57bc25b.PNG)

## Connect to your instance

Once running, the IP address will be displayed, and you are able to connect to the instance.

Select `Open in browser window` to open an SSH shell directly.

If an SSH key pair was set, connect to the instance with your preferred SSH client. For example if using `ubuntu` image:

```console
ssh -i <private_key> ubuntu@<public_ip_address>
```
Terminal applications such as [PuTTY](https://www.putty.org/), [MobaXterm](https://mobaxterm.mobatek.net/) and similar can be used.

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

