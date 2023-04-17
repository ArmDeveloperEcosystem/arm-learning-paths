---
# User change
title: "Deploy Azure Arm based virtual machines using the console"
draft: true

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##  Use the GUI to deploy Azure Arm based virtual machines

Azure currently offers various Arm based VMs including the Dpsv5, Dpdsv5, Dplsv5, Dpldsv5, Epsv5, and Epdsv5. More information about Azure virtual machines can be found [here](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/series/).

Create an Azure account at https://portal.azure.com with a [Pay-As-You-Go](https://signup.azure.com/signup?offer=MS-AZR-0003P) subscription to use dpsv5 Arm virtual machines.

![image](https://user-images.githubusercontent.com/42368140/196611560-6fdbab30-c9dc-4b2b-8041-e855161cb6c3.PNG)

First, log in to your Azure account and go to the dashboard. To create a linux Arm VM, select **Virtual machines** and click on **Create**.

![image #center](https://user-images.githubusercontent.com/42368140/196386746-84d3bd42-c676-4ca9-b0d2-89f11e475ad8.png)

## Resource Group

A resource group is a container that holds related resources for an Azure solution.

Click on **Create new** under the Resource group label.

![image #center](https://user-images.githubusercontent.com/42368140/196379160-1e6a9f51-b6f7-48d6-83f2-b843109b0a9b.png)

## Instance details

* **Virtual Machine Name:** Name the VM (Eg: Myvm1)
* **Region:** Choose region (Eg: (US) East US)
* **Security type:** Level of security (Eg: Standard)
* **Image:** Select image to launch VM (Eg: Ubuntu Server 20.04 LTS - Gen2)
* **VM architecture:** Choose architecture (Eg: Arm64)
* **Size:** Choose CPU as per your requirement (Eg: Standard_D2ps_v5 - 2 vcpus, 8GiB memory)

![image #center](https://user-images.githubusercontent.com/42368140/196609858-fcb05ae5-6352-476b-9db0-de1b133bbe21.PNG)

## Request Quota

While choosing size like **D2psv5 vCPUs**, we get validation error that **2vCPUs are needed for this configuration but only 0 vCPUs are available**. We need to select **Request quota** and submit request to increase the limit.

**Note:** Please skip this section, if you don't have above error of not enough vCPUs available.

![image #center](https://user-images.githubusercontent.com/42368140/196379402-704c594a-89eb-4a67-949a-1f703492365a.PNG)

## SSH Public Key

Use a public key to securely connect to our VM. We can choose from an existing public key, or create a new one. It is generally preferred that instead of using the same public key for all servers, we should create a new one for certain groups of servers. To do that, we can choose **Generate new key pair** and enter name of the key(Eg: Myvm1_key).

![image #center](https://user-images.githubusercontent.com/42368140/196379560-695da753-ec49-4489-9370-c8040afe2d5d.PNG)

## Disks

After providing instance details, click on **Next: Disks**. We can modify the details required or proceed with default disk configuration as below.

![image #center](https://user-images.githubusercontent.com/42368140/196379817-dfcc3427-2be1-40fd-8600-e1571a5c52c6.PNG)

## Networking

After entering disk details, click on **Next: Networking** and enter below details:
* **Virtual Network:** Enter virtual network name
* **Public IP:** Default will be None. If required you can create static Public IP
* **NIC network security group:** Default will be "Basic".
* **Public inbound ports:** Choose required inbound ports

![image #center](https://user-images.githubusercontent.com/42368140/196611792-824bf8ec-ce3d-433d-997b-2bbd79d801d9.PNG)

## Management

Configure Management options for your VM.

![image #center](https://user-images.githubusercontent.com/42368140/196380030-8cf86c83-f33b-4b5f-8f1b-d8a4030bd5bf.PNG)

## Monitoring

Configure Monitoring options for your VM.

![image #center](https://user-images.githubusercontent.com/42368140/196380118-ce67b091-41b8-41a2-9d70-d6d6abb52b58.PNG)

## Advanced configuration

Add additional configuration, agents, scripts or applications via virtual machine extensions or cloud-init.

![image #center](https://user-images.githubusercontent.com/42368140/196380191-97789b03-24d5-4ae7-852f-c2a76eb4490d.PNG)
 
## Tags

Tags are name/value pairs that enable you to categorize resources.
 
![image #center](https://user-images.githubusercontent.com/42368140/196635499-2621cc37-28d4-4598-a62d-84f3115e3878.PNG)

## Create VM

Once all details are updated, click on **Review + create** to validate the entered details.

![image #center](https://user-images.githubusercontent.com/42368140/196384876-260cec4b-d6d1-4c07-8c38-46a82366e72e.png)

## Save Key pair
Once VM details are validated, save the key pair and create the resource.

![image #center](https://user-images.githubusercontent.com/42368140/196384978-f32b6d88-7556-466f-b43a-4de69a33720d.PNG)

## Deployment Details

Check all the resources created and deployed.
 
![image #center](https://user-images.githubusercontent.com/42368140/196380494-627009c2-4cb1-4a88-a49e-502bb63945ba.PNG)


## Connect to azure VM

We can login into created VM using SSH. To do that, we require access to the key pair (Pem file) which we have downloaded. By default, pem file permission is set to `rw-r--r--`. This is not allowed for SSH Pem files. We have to change the permission for this Pem file to 400, so that only the current user can read this Pem file.

```console
chmod 400 Myvm1_key.pem
```

To get the publicIP and user details, we need to Go to resource **Myvm1(VM)** and **GO TO >> connect**

![image #center](https://user-images.githubusercontent.com/42368140/196381065-1e810dd3-091b-4672-8f94-738b427115cd.PNG)

Run following command in the same directory where pem file is available to connect to VM through SSH:

```console
ssh -i "Myvm1_key.pem" azureuser@<Public IP>
```

![image #center](https://user-images.githubusercontent.com/42368140/196381209-dd44ab32-621d-4008-bf9e-87a18ab7fae0.PNG)
