---
title: Validate OpenStack Deployment and Launch VM on Azure Cobalt 100 vm
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Validate OpenStack Deployment and Launch a Virtual Machine

After deploying OpenStack using Kolla-Ansible, it is important to verify that all services are functioning correctly and that the environment can successfully launch virtual machines.

In this guide, you will:

* Validate OpenStack services
* Fix common Arm + Azure networking issues
* Upload an Arm-compatible image
* Create network and compute resources
* Launch and verify a virtual machine


## Install OpenStack CLI (if not installed)

```console
pip install python-openstackclient
```

This tool allows you to interact with OpenStack services via the command line.

## Load admin credentials

```console
source /etc/kolla/admin-openrc.sh
```

This sets environment variables required to authenticate with OpenStack.

## Verify services

```console
openstack compute service list
openstack network agent list
```

**Expected result:**

All services should show:

- Status → enabled
- State → up

If any service is down, the deployment is incomplete or misconfigured.

## Open vSwitch bridges

In Arm + Azure environments, OVS bridges may not come up automatically.

This causes:

* VM stuck in `ERROR`
* No networking
* No IP assignment

Run the following commands:

```console
sudo ip link set br-int up
sudo ip link set br-ex up
sudo ip link set br-tun up
```

Verify OVS configuration:

```console
sudo ovs-vsctl show
```

**Expected output:**

You should see:

- br-int → integration bridge
- br-ex → external bridge
- br-tun → tunnel bridge

All bridges must exist and be active.

## Upload image

Download a Debian Arm64 cloud image:

```console
wget https://cloud.debian.org/images/cloud/bookworm/latest/debian-12-genericcloud-Arm64.qcow2
```

Upload it to OpenStack:

```console
openstack image create "test-image" \
  --file debian-12-genericcloud-Arm64.qcow2 \
  --disk-format qcow2 \
  --container-format bare \
  --public
```

## Verify image upload

```console
openstack image list
```

The output is similar to:

```output
+--------------------------------------+------------+--------+
| ID                                   | Name       | Status |
+--------------------------------------+------------+--------+
| 4537107d-4c52-4537-a3d2-bd5c5a13de5b | test-image | active |
+--------------------------------------+------------+--------+
```

The image must be in an active state before launching VMs.

## Create network

```console
openstack network create test-net

openstack subnet create test-subnet \
  --network test-net \
  --subnet-range 192.168.0.0/24
```

### Why this is required

OpenStack networking (Neutron) requires:

- Network → logical network
- Subnet → IP range for instances

## Verify network

```console
openstack network list
```

The output is similar to:

```output
+--------------------------------------+----------+--------------------------------------+
| ID                                   | Name     | Subnets                              |
+--------------------------------------+----------+--------------------------------------+
| 1d8b3cc8-a2d3-476c-86d7-4b9533dbefb2 | test-net | a31916fa-783b-4b25-8acb-8694007b9198 |
+--------------------------------------+----------+--------------------------------------+
```

## Verify subnet

```console
openstack subnet list
```

The output is similar to:

```output
+--------------------------------------+-------------+--------------------------------------+----------------+
| ID                                   | Name        | Network                              | Subnet         |
+--------------------------------------+-------------+--------------------------------------+----------------+
| a31916fa-783b-4b25-8acb-8694007b9198 | test-subnet | 1d8b3cc8-a2d3-476c-86d7-4b9533dbefb2 | 192.168.0.0/24 |
+--------------------------------------+-------------+--------------------------------------+----------------+
```

Both should show your created resources.

## Create flavor

```console
openstack flavor create m1.tiny --ram 512 --disk 5 --vcpus 1
```

### Why is flavor required

A flavor defines:

- CPU
- RAM
- Disk

for the virtual machine.

## Verify flavor

```console
openstack flavor list
```

The output is similar to:

```output
+--------------------------------------+---------+-----+------+-----------+-------+-----------+
| ID                                   | Name    | RAM | Disk | Ephemeral | VCPUs | Is Public |
+--------------------------------------+---------+-----+------+-----------+-------+-----------+
| 20ea160b-bff7-4c2a-be1e-588a44dc699a | m1.tiny | 512 |    5 |         0 |     1 | True      |
+--------------------------------------+---------+-----+------+-----------+-------+-----------+
```

## Launch VM

```console
openstack server create \
  --flavor m1.tiny \
  --image test-image \
  --network test-net \
  test-vm
```


## Verify VM status

```console
watch -n 2 openstack server list
```

The output is similar to:

```output
+--------------------------------------+---------+--------+------------------------+------------+---------+
| ID                                   | Name    | Status | Networks               | Image      | Flavor  |
+--------------------------------------+---------+--------+------------------------+------------+---------+
| 4f42729c-0635-40e2-9432-ac056e40f781 | test-vm | ACTIVE | test-net=192.168.0.150 | test-image | m1.tiny |
+--------------------------------------+---------+--------+------------------------+------------+---------+
```

If the VM stays in ERROR, check:

- OVS bridges
- compute service status
- image compatibility

## Access Horizon dashboard

Open browser:

```text
http://<VM_PUBLIC_IP>
```

Get password:

```console
cat /etc/kolla/passwords.yml | grep keystone_admin_password
```

Login:

* Username: admin
* Domain: Default

The following image shows a successfully launched instance in the OpenStack Horizon UI.

![OpenStack Horizon dashboard showing running instance test-vm alt-txt#center](images/openstack-ui.png "OpenStack Horizon Instances view with ACTIVE VM")


## What you've learned

You successfully validated your OpenStack deployment and confirmed that all services are operational.

You also:

- Created vSwitch networking specific to Arm + Azure
- Uploaded an Arm-compatible image
- Created network and compute resources
- Launched and verified a virtual machine

Your OpenStack environment is now fully functional and ready for use.
