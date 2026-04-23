---
title: Prepare Azure Arm64 VM for Kolla-Ansible (Network and Storage Setup)
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare VM for Kolla-Ansible Deployment

Before deploying OpenStack using Kolla-Ansible, the Azure virtual machine must be prepared with proper networking and storage.

In this section, you will:

* Add a second network interface (NIC)
* Attach a data disk
* Prepare the VM for OpenStack networking and storage

## Why this setup is required

OpenStack requires multiple network layers:

* **Management network (`eth0`)** → internal communication  
* **External network (`eth1`)** → VM traffic (provider network)  
* **Dedicated storage disk** → for Cinder and container storage  

Without this setup, VM networking and storage services will fail.

# Step 1: Add a second NIC in Azure

## Stop the VM

Go to:

* Azure Portal → Virtual Machines  
* Select your VM  
* Click **Stop**

![Azure VM stop button highlighted alt-txt#center](images/kolla-ansible-nic1.png "Stopping the VM before attaching NIC")

Stopping the VM is required because Azure does not allow NIC attachment while the VM is running.

## Attach a new NIC

* Go to **Networking → Network settings**
* Click **Attach network interface**
* Select **Create new NIC**

![Create NIC configuration screen alt-txt#center](images/kolla-ansible-nic2.png "Creating new NIC for OpenStack external network")

## Configure NIC

* Keep the NIC in the same Virtual Network  
* Select the same subnet  
* Do **NOT** assign a public IP  
* Click **Create**

![Attach network interface option alt-txt#center](images/kolla-ansible-nic3.png "Attach network interface in Azure")


## Start the VM

* Go back to the VM overview  
* Click **Start**

# Step 2: Attach a data disk in Azure

## Add disk

* Go to Azure Portal → Virtual Machine  
* Select **Disks**  
* Click **Create and attach a new disk**

## Configure disk

* Disk name: `openstack-disk`  
* Size: **32 GB** (recommended minimum)  
* Type: **Standard SSD**  
* Click **Apply**

![Attach data disk in Azure alt-txt#center](images/kolla-ansible-data-disk.png "Adding data disk for OpenStack storage")

## Why this disk is important

This disk will be used for:

* Cinder (block storage)
* Docker volumes
* OpenStack service data

Using a separate disk ensures better performance and avoids filling the OS disk.

## What you've accomplished

You successfully prepared the Azure Arm64 virtual machine for Kolla-Ansible by:

* Adding and configuring a second network interface  
* Attaching a dedicated storage disk  
* Preparing networking for the OpenStack provider network  
* Ensuring the system is ready for containerized OpenStack deployment  

## What's next

In the next section, you will:

* Install Kolla-Ansible  
* Deploy OpenStack services  
* Validate the deployment  
