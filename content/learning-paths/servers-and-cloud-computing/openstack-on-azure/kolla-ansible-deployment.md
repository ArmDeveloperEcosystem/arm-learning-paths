---
title: Deploy OpenStack using Kolla-Ansible on Azure Ubuntu Arm64 VM
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Deploy OpenStack on Azure Cobalt 100 VM using Kolla-Ansible

{{% notice Note %}}Use the virtual machine prepared for Kolla-Ansible deployment (with dual NICs and a data disk). This setup is required for proper networking and storage configuration.{{% /notice %}}

This guide walks you through deploying OpenStack using Kolla-Ansible on an Azure Ubuntu 24.04 Arm64 virtual machine.

Kolla-Ansible deploys OpenStack services as Docker containers, making the deployment modular, reproducible, and easier to manage.

After completing this guide, your environment will:

* Run core OpenStack services (Nova, Neutron, Keystone, Glance)
* Support Arm64 (`aarch64`) architecture
* Provide CLI and Horizon access
* Allow launching virtual machines


## Prerequisites

* Ubuntu 24.04 Arm64 VM (Azure)
* Minimum 4 vCPU, 8 GB RAM (16 GB recommended)
* Disk: 100 GB+
* Two network interfaces:

  * `eth0` → management (with IP)
  * `eth1` → external (no IP)

## Configure external interface

```console
sudo ip addr flush dev eth1
sudo ip link set eth1 up
```

This ensures that OpenStack can use `eth1` as the external/provider network.


## Install system dependencies

```console
sudo apt update

sudo apt install -y \
python3-venv python3-dev python3-pip \
gcc libffi-dev libssl-dev \
libdbus-1-dev libglib2.0-dev pkg-config \
meson ninja-build curl
```

These packages are required for Python builds and OpenStack dependencies.

## install Docker

Docker is used to run all OpenStack services as containers.

```console
sudo apt install -y docker.io

sudo systemctl enable docker
sudo systemctl start docker
```

**Add user to Docker group:**

```console
sudo usermod -aG docker $USER
```

**Apply group permissions (IMPORTANT):**

```console
newgrp docker
```

**Verify Docker installation:**

```console
docker run hello-world
```

This step is critical. Without applying group permissions, Docker commands will fail with a permission error.

## Create Python virtual environment

```console
python3 -m venv ~/kolla-venv
source ~/kolla-venv/bin/activate
```

A virtual environment isolates dependencies required for Kolla-Ansible.

## Install Kolla-Ansible and dependencies

```console
pip install -U pip

pip install \
'ansible-core>=2.15,<2.17' \
kolla-ansible \
docker \
dbus-python
ansible-galaxy collection install openstack.kolla
kolla-ansible install-deps
```

These tools are required to deploy and manage OpenStack services.

## Configure Kolla

```console
sudo mkdir -p /etc/kolla
sudo chown $USER:$USER /etc/kolla

cp -r ~/kolla-venv/share/kolla-ansible/etc_examples/kolla/* /etc/kolla
cp ~/kolla-venv/share/kolla-ansible/ansible/inventory/all-in-one .
```


## Edit globals.yml

```console
vi /etc/kolla/globals.yml
```

```yaml
kolla_base_distro: "debian"
openstack_tag_suffix: "-aarch64"

network_interface: "eth0"
neutron_external_interface: "eth1"

kolla_internal_vip_address: "127.0.0.1"

enable_keepalived: "no"
```

### Why this configuration?

- **Debian base** → Arm images are available
- **aarch64 suffix** → ensures correct image selection
- **VIP = VM IP** → avoids Azure networking issues
- **HA disabled**→ required for single-node deployments


## Configure Nova (Arm fix)


```console
sudo mkdir -p /etc/kolla/config

cat <<EOF | sudo tee /etc/kolla/config/nova.conf
[libvirt]
virt_type = qemu
cpu_mode = none
EOF
```

### Why this is required

Arm-based Azure VMs do not support KVM virtualization. Using QEMU ensures that instances can be launched successfully.

## Generate passwords

```console
kolla-genpwd
```

This creates all required passwords for OpenStack services.

## Deploy OpenStack

Run the following commands in order:

```console
kolla-ansible bootstrap-servers -i all-in-one
```

The output is similar to:

```output

PLAY RECAP ***************************************************************************************************************************
localhost                  : ok=41   changed=13   unreachable=0    failed=0    skipped=30   rescued=0    ignored=0
```

```console
kolla-ansible prechecks -i all-in-one 
```

The output is similar to:

```output
PLAY RECAP ***************************************************************************************************************************
localhost                  : ok=96   changed=0    unreachable=0    failed=0    skipped=142  rescued=0    ignored=0
```

```console
kolla-ansible pull -i all-in-one
```

The output is similar to:

```output
PLAY [Apply role skyline] ************************************************************************************************************
skipping: no hosts matched

PLAY RECAP ***************************************************************************************************************************
localhost                  : ok=33   changed=14   unreachable=0    failed=0    skipped=52   rescued=0    ignored=0
```
```console
kolla-ansible deploy -i all-in-one deploy
````

The output is similar to:

```output
PLAY [Apply role skyline] ************************************************************************************************************
skipping: no hosts matched

PLAY RECAP ***************************************************************************************************************************
localhost                  : ok=368  changed=34   unreachable=0    failed=0    skipped=267  rescued=0    ignored=0
```

#### What happens during deployment?

- **Bootstrap** → prepares system (Docker, users, configs)
- **Prechecks** → validates environment
- **Pull** → downloads OpenStack container images
- **Deploy** → starts all services
- **Post-deploy** → generates access credentials

```console
kolla-ansible -i all-in-one post-deploy
```

## Load environment

```console
source /etc/kolla/admin-openrc.sh
```

This enables OpenStack CLI commands.

## Verify services

```console
openstack compute service list
openstack network agent list
```

All services should be UP.

The output is similar to:

```output
openstack network agent list
+--------------------------------------+----------------+--------------+----------+---------+-------+----------------------------+
| ID                                   | Binary         | Host         | Zone     | Status  | State | Updated At                 |
+--------------------------------------+----------------+--------------+----------+---------+-------+----------------------------+
| bcb60746-4219-44a7-b850-5f9b28ec12d7 | nova-scheduler | ansible-d8ps | internal | enabled | up    | 2026-04-14T07:38:13.000000 |
| 2054f4ad-2492-46e4-990a-4fdf7d40e20f | nova-conductor | ansible-d8ps | internal | enabled | up    | 2026-04-14T07:38:11.000000 |
| b0d28456-483b-4a9c-bcaf-5932364e32b6 | nova-compute   | ansible-d8ps | nova     | enabled | up    | 2026-04-14T07:38:16.000000 |
+--------------------------------------+----------------+--------------+----------+---------+-------+----------------------------+
+------------------------+--------------------+--------------+-------------------+-------+-------+--------------------------+
| ID                     | Agent Type         | Host         | Availability Zone | Alive | State | Binary                   |
+------------------------+--------------------+--------------+-------------------+-------+-------+--------------------------+
| 0ac15427-97e0-4690-    | Metadata agent     | ansible-d8ps | None              | :-)   | UP    | neutron-metadata-agent   |
| be2b-ac3b236a331f      |                    |              |                   |       |       |                          |
| 41dc2dee-106e-4a99-    | DHCP agent         | ansible-d8ps | nova              | :-)   | UP    | neutron-dhcp-agent       |
| 8e7b-94b8fac38fe1      |                    |              |                   |       |       |                          |
| f36a8827-ee1f-4387-    | L3 agent           | ansible-d8ps | nova              | :-)   | UP    | neutron-l3-agent         |
| 9c11-bdbb0c10dee4      |                    |              |                   |       |       |                          |
| fb0f81ce-06e1-4ded-    | Open vSwitch agent | ansible-d8ps | None              | :-)   | UP    | neutron-openvswitch-     |
| b736-1bd329a3a59e      |                    |              |                   |       |       | agent                    |
+------------------------+--------------------+--------------+-------------------+-------+-------+--------------------------+
```

## What you've learned

You successfully deployed OpenStack using Kolla-Ansible on an Arm-based Azure VM.

You also resolved key challenges, including:

- Docker permission issues
- Arm virtualization limitations (QEMU)
- Image compatibility (aarch64)
- Azure networking constraints (VIP handling)
- Single-node deployment limitations (HA disabled)

You now have a fully functional OpenStack environment capable of launching and managing virtual machines.
