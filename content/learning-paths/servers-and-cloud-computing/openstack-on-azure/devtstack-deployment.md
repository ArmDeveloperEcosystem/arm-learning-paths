---
title: Deploy OpenStack on Azure Arm using DevStack (Cobalt 100)
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Deploy OpenStack on Arm using DevStack (Azure Cobalt 100)

{{% notice Note %}}Use the VM with a single network interface (DevStack setup). You do not need to add an extra NIC or data disk for these steps.{{% /notice %}}

This guide walks you through deploying OpenStack using DevStack on an Arm-based Azure virtual machine (Azure Cobalt 100).

DevStack is a lightweight OpenStack deployment tool designed for development and testing.
It installs core OpenStack services such as Nova, Keystone, Glance, and Horizon on a single node.

After completing this guide, your environment will:

* Run OpenStack services locally
* Provide access to the Horizon
* Support Arm64 (`aarch64`) architecture
* Be accessible via browser and CLI

## Objective

In this guide, you will:

* Deploy OpenStack on Arm using DevStack
* Fix Arm-specific compatibility issues (etcd, libvirt)
* Access Horizon dashboard via public IP
* Validate services using OpenStack CLI

## Environment

| Component | Value                |
| --------- | -------------------- |
| Platform  | Azure Cobalt (Arm64) |
| OS        | Ubuntu 24.04         |
| VM Size   | D4ps_v6              |
| RAM       | ≥ 8 GB               |
| Disk      | ≥ 80 GB              |


## Clean previous setup

Before starting, remove any previous DevStack or etcd installation.

```console
sudo rm -rf ~/devstack
sudo rm -rf /opt/stack
sudo rm -rf /var/lib/etcd
sudo rm -f /etc/systemd/system/etcd.service
```

This ensures:

* No leftover configuration conflicts
* Clean environment for deployment
* Avoids service startup failures

## System preparation

Update packages and install required tools.

```console
sudo apt update && sudo apt upgrade -y

sudo apt install -y \
git curl vim net-tools python3-pip
```

These tools are required for:

* Cloning DevStack repository (`git`)
* Downloading dependencies (`curl`)
* Editing configuration (`vim`)
* Network debugging (`net-tools`)

## Configure hostname

```console
sudo hostnamectl set-hostname devstack-Arm
exec bash
```

Setting a consistent hostname ensures:

* Proper service registration
* Correct identification in OpenStack services

## Install etcd (Arm fix)

DevStack uses etcd internally, but on Ubuntu 24.04 Arm:

 * Built-in etcd service is unstable ❌

So we install a stable Arm-compatible version manually.

```console
cd /tmp
wget https://github.com/etcd-io/etcd/releases/download/v3.5.13/etcd-v3.5.13-linux-Arm64.tar.gz
tar -xvf etcd-v3.5.13-linux-Arm64.tar.gz
cd etcd-v3.5.13-linux-Arm64
sudo cp etcd etcdctl /usr/local/bin/
```

## Configure etcd service

```console
sudo vi /etc/systemd/system/etcd.service
```

```ini
[Unit]
Description=etcd
After=network.target

[Service]
User=azureuser
ExecStart=/usr/local/bin/etcd \
  --data-dir=/var/lib/etcd
Restart=always

[Install]
WantedBy=multi-user.target
```

This configuration ensures:

* etcd starts automatically on boot
* Data is stored persistently
* Service is managed via systemd

## Start etcd

```console
sudo mkdir -p /var/lib/etcd
sudo chown -R $USER:$USER /var/lib/etcd

sudo systemctl daemon-reload
sudo systemctl enable etcd
sudo systemctl start etcd
```
Verify:

```console
sudo systemctl status etcd
```

The output is similar to:

```output
Active: active (running)
```

This confirms etcd is running correctly.


## Install DevStack

```console
cd ~
git clone https://opendev.org/openstack/devstack
cd devstack
```

This downloads the DevStack scripts required to install OpenStack.

## Configure DevStack

```console
vi local.conf
```

### Arm-optimized configuration

```ini
[[local|localrc]]
ADMIN_PASSWORD=admin
DATABASE_PASSWORD=admin
RABBIT_PASSWORD=admin
SERVICE_PASSWORD=admin

HOST_IP=<Private_IP>
SERVICE_HOST=<Private_IP>

enable_service horizon

disable_service neutron
disable_service q-agt
disable_service q-dhcp
disable_service q-l3
disable_service q-meta
disable_service q-svc
disable_service ovn-controller
disable_service ovs-vswitchd
disable_service ovsdb-server

disable_service etcd3

KEYSTONE_USE_MOD_WSGI=False
ENABLE_HTTPD_MOD_WSGI_SERVICES=False

LIBVIRT_TYPE=qemu

disable_service tempest
```

### Why these changes?

* **Disable Neutron** → avoids Arm networking issues
* **Disable etcd3** → uses our stable external etcd
* **LIBVIRT_TYPE=qemu** → avoids KVM issues on Arm
* **Enable Horizon** → provides web UI

## Get private IP

```console
hostname -I
```

Replace `<Private_IP>` in `local.conf`.

## Deploy OpenStack

```console
./stack.sh | tee stack.log
```

This script:

* Installs all OpenStack services
* Configures database and messaging
* Starts services

**Deployment time: ~15–25 minutes**

## Access Horizon dashboard

Open in browser:

```text
http://<PUBLIC_IP>/dashboard
```

Example:

```text
http://4.186.31.18/dashboard
```

![OpenStack Horizon login page alt-txt#center](images/openstack-horizon-dashboard.png "OpenStack Horizon Login Screen")

## Login credentials

```text
Username: admin
Password: admin
```

## Azure network fix (critical)

Ensure port 80 is open:

```text
Azure Portal → VM → Networking → Inbound Rules
```

| Port | Protocol | Action |
| ---- | -------- | ------ |
| 80   | TCP      | Allow  |


## Verify via CLI

```console
source openrc admin admin

openstack service list
openstack compute service list
```

## Expected output

Services should include:

```text
Keystone → OK
Nova → OK
Glance → OK
Placement → OK
Cinder → OK
```

Compute:

```text
  import eventlet
+----------------------------------+-------------+----------------+
| ID                               | Name        | Type           |
+----------------------------------+-------------+----------------+
| 0a0554a3a6bf45e8937fa389ab559be3 | glance      | image          |
| 448f4e62b7344cac969c9ec18af4048d | nova        | compute        |
| 5cf7336818784a4383c0a543303ab4d7 | keystone    | identity       |
| 6ebdc6a1d7814f138f59ac5719bb4394 | cinder      | block-storage  |
| b86d2058e0604db6bcc9b12f3d2b16b4 | nova_legacy | compute_legacy |
| fd998beaffe64e2191795082470d03c0 | placement   | placement      |
+----------------------------------+-------------+----------------+

  import eventlet
+--------------------------------------+----------------+--------------+----------+---------+-------+----------------------------+
| ID                                   | Binary         | Host         | Zone     | Status  | State | Updated At                 |
+--------------------------------------+----------------+--------------+----------+---------+-------+----------------------------+
| 46946541-a6c1-4b8c-92e3-5d037bb2d577 | nova-scheduler | devstack-Arm | internal | enabled | up    | 2026-04-14T08:14:42.000000 |
| e1aa2f20-3f39-4d12-9702-4b144a739f56 | nova-conductor | devstack-Arm | internal | enabled | up    | 2026-04-14T08:14:46.000000 |
| caeab24b-a938-420b-9ae0-e335ed8acfea | nova-conductor | devstack-Arm | internal | enabled | up    | 2026-04-14T08:15:56.000000 |
| b612363d-b7ad-4c9e-93b8-afd20fb9b863 | nova-compute   | devstack-Arm | nova     | enabled | up    | 2026-04-14T08:15:05.000000 |
+--------------------------------------+----------------+--------------+----------+---------+-------+----------------------------+

```


## What you've learned

You successfully deployed OpenStack using DevStack on an Arm-based Azure VM.

You resolved Arm-specific issues, including:

* etcd compatibility
* networking limitations
* libvirt virtualization (QEMU)

You validated the deployment using CLI and accessed the Horizon UI.

