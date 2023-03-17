---
# User change
title: "Deploy AWS Graviton EC2 instances using the AWS Console"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##  Use the AWS Console to deploy EC2 instances with Graviton processors

AWS Graviton processors are Arm based processors designed specifically for AWS. More information can be found [here](https://aws.amazon.com/pm/ec2-graviton/).

## Deploy Graviton based EC2 instances using the AWS Console

Log in to your AWS account and open the EC2 Dashboard. To launch an instance, select Launch instance.

![image](https://user-images.githubusercontent.com/87687468/189866780-e67c8a99-e5f2-445f-938c-a672cd926c4a.png)
   
## Name and Tags

Enter a name for the instance.

Tags are optional.
    
![image](https://user-images.githubusercontent.com/87687468/192811901-40232129-2405-4a33-803c-1a9e40934b44.png)

## Choose an Amazon Machine Image (AMI)

Select an Ubuntu AMI and change the architecture to Arm.
   
![image](https://user-images.githubusercontent.com/87687468/192594550-95c51ac9-d1cd-4f0d-98f2-a1fce1a78b2d.png)

Also select "64-bit (Arm)" from Architecture drop down
   
![image](https://user-images.githubusercontent.com/87687468/192595418-c96ad1e5-8a74-43f8-83c7-d5c19f14ff4a.png)

## Choose an Instance Type

For instance type, we select an Arm based t4g.nano instance as shown below. More information on Arm based Graviton instance types can be found on the [AWS Graviton page](https://aws.amazon.com/ec2/graviton/).
   
![image](https://user-images.githubusercontent.com/87687468/192596029-21b7dcc2-917c-41d0-bda2-3763584f7f00.png)
 
## SSH Key pair

Use a key pair to securely connect to our instance. Choose an existing key pair, or create a new one. It is generally preferred that instead of using the same key pair for all instances, you should create a new one for different groups of instances.
   
![image](https://user-images.githubusercontent.com/87687468/189890580-0b647d1e-baad-4597-95ad-7fcad81e9324.png)

To create a new Key pair Go to > **Create a new pair** and then name it (e.g. demoserver). Select the key type and format and press **Create key pair**

![image](https://user-images.githubusercontent.com/87687468/189891219-ac02d5df-d247-4adb-8e3d-03c0212b9356.png)

Download the newly created Key Pair. Once it is downloaded, select it from the drop down list.
   
![image](https://user-images.githubusercontent.com/87687468/189892157-580783ad-f387-4f6e-83f6-793661078bbc.png)

## Network setting

Use the default VPC and Subnet.

## Configure Security Group

Choose an existing security group or create a new security group. Below shows how to create a new security group that allows SSH access to the instance.
   
![image](https://user-images.githubusercontent.com/87687468/189876379-1d9118c8-a9a6-4e6d-892a-e37443d37546.png)
   
## Configure Storage

By default, EC2 instances create 8 GiB of storage. Increase this for scenarios that require more storage. For example, select  25 GiB of storage. Selecting a volume type of General Purpose SSD (gp2) is a good starting point. Explore different storage options after you better understand the nature of the workload.
   
![image](https://user-images.githubusercontent.com/87687468/189878035-87d9721f-c58e-4ce7-800b-093d4d3e59ce.png)
   
Set Delete On Termination to yes. This will ensure that the volume is deleted and will not incur charges on you account once the instance is terminated.
   
## Review and Launch

Check the details in the summary box and press launch.

![image](https://user-images.githubusercontent.com/87687468/189878839-3ef022f7-2be7-458a-b0ce-20cf5ee0bcaa.png)

## SSH into the launched instance

Login to the created instance using SSH. 

To do that, use the key pair (pem file) which was downloaded. By default, pem file permission is set to `rw-r--r--`. This is not allowed for SSH pem files. Change the permission for the pem file to 400, so that only the current user can read this Pem file.

```
$ chmod 400 demoserver.pem
```
   
Now, only the owner of the Pem file can read it. In fact, these are permissions that a pem file expects. Select the Instance by checking the box of the instance you want to connect to and GO TO » connect.
   
![image](https://user-images.githubusercontent.com/87687468/192154311-55889d4e-6dd2-4bc3-81a9-95cca7356e0a.png)
   
In the SSH Client, you will see instructions that explain how to SSH into the instance.
   
![image](https://user-images.githubusercontent.com/87687468/190095052-41851f3d-61db-486f-9c00-2f504587bdcc.png)
   
In a terminal, navigate to the same directory where the pem file is located. 

Use following command to ssh to the instance:
   
```
ssh -i "demoserver.pem" ubuntu@<Public IP/DNS address>
```

