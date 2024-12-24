---
title: Deploy to AWS EC2
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Objective
In this section, you will learn how to deploy the .NET Aspire application on to an AWS EC2 (Elastic Compute Cloud) Virtual Machine powered by Arm-based processors, such as AWS Graviton. This involves leveraging the cost and performance benefits of Arm architecture while demonstrating the seamless deployment of cloud-native applications on modern infrastructure.

### Set up your AWS EC2 Instance
Follow these steps to deploy an app on to an Arm-powered EC2 instance:
1. Log in to the [AWS Management Console](http://console.aws.amazon.com).
2. Navigate to the EC2 Service. 

   As shown in Figure 5, in the search box, type "EC2". 
   
   Then, click on **EC2** in the search results:

![Figure 5 alt-text#center](figures/05.png "Figure 5: Search for EC2 Service in the AWS Management Console.")

3. In the EC2 Dashboard, click **Launch Instance** and fill out the following details:
* Name: type "arm-server".
* AMI: select **Arm-compatible Amazon Machine Image, Ubuntu 22.04 LTS for Arm64**.
* Architecture: select **64-bit (Arm)**.
* Instance Type: select **t4g.small**.

The configuration should look like the configuration fields shown in Figure 6:

![Figure 6 alt-text#center](figures/06.png "Figure 6: Configuration.")

4. Scroll down to **Key pair** (login), and click **Create new key pair**. 
  This displays the "Create key pair" window. 
  Now configure the following fields:
* Key pair name: **arm-key-pair**.
* Key pair type: **RSA**.
* Private key format: **.pem**.
* Click the **Create key pair** button, and download the key pair to your computer.

![fig7](figures/07.png)

5. Scroll down to "Network Settings", where:
* VPC: use default
* Subnet: select no preference
* Auto-assign public IP: Enable
* Firewall: Check Create security group
* Security group name: arm-security-group
* Description: arm-security-group
* Inbound security groups 

![fig8](figures/08.png)

6. Configure "Inbound Security Group Rules". Specifically, click "Add Rule" and set the following details:
* Type: Custom TCP
* Protocol: TCP
* Port Range: 7133.
* Source: Select Anywhere (0.0.0.0/0) for public access or restrict access to your specific IP for better security.
* Repeat this step for all three ports the application is using. Here I have 7133, 7511, 17222. These must match the values we had, when we run the app locally.

The configuration should look as follows:

![fig9](figures/09.png)

7. Launch an instance by clicking "Launch instance" button. You should see the green box with the Success label. This box also contains a link to the EC2 instance. Click it. It will take you to the instance dashboard, which looks like the one below:

![fig10](figures/10.png)

### Deploy the application
Once the EC2 instance is ready, you can connect to it and deploy the application. Follow these steps to connect:
1. Locate the instance public IP (e.g. 98.83.137.101 in this case).
2. Use an SSH client to connect:
* Open the terminal
* Set appropriate permissions for the key pair file (remember to use your IP address)
```console
chmod 400 arm-key-pair.pem                     
ssh -i arm-key-pair.pem ubuntu@98.83.137.101 
```

![fig11](figures/11.png)

You can now install required components, pull the application code from git, and launch the app:
In the EC2 terminal run: 
```console
sudo apt update && sudo apt upgrade -y
```

This will update the package list and upgrade the installed packages.

Install .NET SDK using the following commands:
```console
wget https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
sudo apt update
sudo apt install -y dotnet-sdk-8.0
```

Verify the installation:
```console
dotnet --version
```
Install the Aspire workload using the dotnet CLI
```console
dotnet workload install aspire
```
Clone the repository which contains the application you created in the previous section:
```console
git clone https://github.com/dawidborycki/NetAspire.Arm.git
cd NetAspire.Arm/
```
Trust the development certificate:
```console
dotnet dev-certs https --trust
```
 Build and run the project:
```console
dotnet restore
dotnet run --project NetAspire.Arm.AppHost
```

The application will run the same way as locally. You should see the following:

![fig12](figures/12.png)

Finally, open the application in the web browser, using the EC2's public IP:

![fig13](figures/13.png)

### Summary 
You have successfully deployed the Aspire app on to an Arm-powered AWS EC2 instance. This demonstrates the compatibility of .NET applications with Arm architecture and AWS Graviton instances, offering high performance and cost-efficiency.

