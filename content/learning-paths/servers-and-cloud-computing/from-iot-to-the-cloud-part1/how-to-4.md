---
title: Installing application dependencies and running the application
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Objective
In this step, you will install in the virtual machine the following tools:
• .NET 7 SDK – to build and run the application,
• git – to clone application sources.

Then, you will use git to clone applicaiton sources. Finally, you will build and launch the application.

### Dependencies
To install .NET SDK:
1.	In the terminal of the virtual machine type:
```console 
wget https://dot.net/v1/dotnet-install.sh
```
This will download the installation script.

2.	Make the script executable:
```console
chmod +x dotnet-install.sh 
```
3.	Run the script (it will install .NET SDK 7 under the folder .dotnet): 
```console
./dotnet-install.sh --channel 7.0
```
4.	Let's add .dotnet folder to the PATH by typing:
```console
export PATH="/home/arm/.dotnet/:$PATH"
```
5.	To ensure that installation was successful, type: 
```console 
dotnet --list-sdsk
```

Note that, in this tutorial, we installed .NET 7 because the application we will deploy was built using .NET 7. If you need to install another .NET version, modify the channel parameter of the installation script.

To install git use the terminal of the virtual machine, where you type 
```console
sudo apt-get install -y git-all
```

Wait for the installation to be completed. It will take a longer while.

### Clone and run the application
You will now clone the application by typing:
```console
git clone https://github.com/dawidborycki/People.WebApp.git
```
The application sources will be cloned to People.WebApp folder. So, we change the working directory:
```conolse 
cd People.WebApp/
```
Then, we run the application such that it will listen on port 8080:
```console
dotnet run --urls "http://0.0.0.0:8080"
```
After completing this you will see the following output:

![Application#left](figures/14.png "Figure 14. Cloning and running the application")

The application is ready and listening for the requests on port 8080. However, the network traffic is blocked on all ports except 22. You will need to configure the Network Security Group to enable the traffic. 

### Configure Network Security Group 
To pass through the traffic on port 8080 for the Virtual Machine of name vm-arm64 you proceed as follows:
1.	In the search box of Azure Portal, type **vm-arm64**, and select this resource.
2.	In the vm-arm64 screen, click the Networking tab on the left (it's under Settings). You will see the following screen:
![Application#left](figures/15.png "Figure 15. Networking tab of the virtual machine")

In the Networking tab of the Virtual Machine, click the **Add inbound port rule** button (it's on the right). This will open a new popup window **Add inbound security rule**:
![Application#left](figures/16.png "Figure 16. Adding inbound port rule")

Ensure the rule is configured as follows:
1.	Source: **Any**
2.	Source port ranges: *****
3.	Destination: **Any**
4.	Service: **Custom**
5.	Destination port ranges: **8080**
6.	Protocol: **Any**
7.	Action: **Allow**
8.	Priority: **310**
9.	Name: **AllowAnyCustom8080Inbound**

Then, click **Add** and wait for the security rule to be applied.

Once this is done, open your web browser, and type the public IP address of your VM followed by 8080 port: **52.149.156.228:8080**. You'll see the application up and running:
![Application#left](figures/17.png "Figure 17. An application deployed to Azure virtual machine")