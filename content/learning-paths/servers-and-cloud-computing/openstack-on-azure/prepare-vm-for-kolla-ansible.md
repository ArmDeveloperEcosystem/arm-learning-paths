---
title: Prepare Azure Arm64 VM for Kolla-Ansible (Network and Storage Setup)
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare a second VM for Kolla-Ansible

You've completed the DevStack deployment on VM 1. The Kolla-Ansible deployment runs on a **separate** Azure VM with a more complex configuration: it needs two network interfaces and a dedicated data disk.

Create a new VM using the same base process as VM 1 (Ubuntu Pro 24.04 LTS, D4ps_v6, SSH key auth), then follow the steps below to add the required networking and storage.

| | VM 1 — DevStack (done) | VM 2 — Kolla-Ansible (this section) |
|-|------------------------|--------------------------------------|
| NICs | 1 (`eth0`) | 2 (`eth0` + `eth1`) |
| Data disk | None | 32 GB |
| RAM | 8 GB | 16 GB recommended |
| Purpose | Dev/test deployment | Containerized production deployment |

Once the new VM is running, complete the following steps before starting the Kolla-Ansible deployment.

# Step 1: Add a second NIC in Azure

Kolla-Ansible requires two network interfaces:

* `eth0` — management network, carries API traffic between OpenStack services
* `eth1` — external/provider network, carries traffic to and from virtual machine instances

Azure does not allow NIC attachment to a running VM. Stop the VM first.

## Stop the VM

Navigate to **Virtual Machines**, select your VM, and click **Stop**.

![Azure Portal showing the VM Stop button highlighted in the top action bar, used to shut down the VM before attaching a NIC#center](images/kolla-ansible-nic1.png "Stop the VM before attaching a network interface")

## Attach a new NIC

* Go to **Networking → Network settings**
* Click **Attach network interface**
* Select **Create new NIC**

![Azure Portal Create NIC configuration screen showing subnet selection and name field for the new network interface#center](images/kolla-ansible-nic2.png "Create a new NIC for the OpenStack external network")

## Configure NIC

* Keep the NIC in the same Virtual Network  
* Select the same subnet 
* Enter a Name 
* Do **NOT** assign a public IP  
* Click **Create**

![Azure Portal Networking settings showing the Attach network interface option selected in the Network settings panel#center](images/kolla-ansible-nic3.png "Attach network interface in Azure Networking settings")


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

![Azure Portal Disks settings showing the newly attached 32 GB Standard SSD listed under data disks#center](images/kolla-ansible-data-disk.png "32 GB data disk attached for OpenStack storage")

## Why this disk is required

Kolla-Ansible uses a dedicated disk for:

* **Cinder** — provides block storage volumes to OpenStack instances
* **Docker volumes** — stores container data for all OpenStack services

Using a separate disk keeps OpenStack data off the OS disk and avoids filling it during deployment.

## What you've accomplished

You've prepared a second Azure Arm64 VM for Kolla-Ansible with:

* A second NIC (`eth1`) for OpenStack's provider network
* A dedicated 32 GB data disk for Cinder and Docker volumes

In the next section, you'll install Kolla-Ansible and deploy OpenStack as containers on this VM.
