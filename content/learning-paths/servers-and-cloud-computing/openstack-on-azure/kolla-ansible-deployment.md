---
title: Deploy OpenStack using Kolla-Ansible on an Azure Ubuntu Arm64 virtual machine
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you'll deploy OpenStack using Kolla-Ansible on the Azure Ubuntu 24.04 Arm64 virtual machine that you created in the previous section.

Kolla-Ansible deploys OpenStack services as Docker containers, making the deployment modular, reproducible, and easier to manage.

After completing this guide, your environment will run core OpenStack services such as Nova, Neutron, Keystone, and Glance. The environment will support Arm64 (`aarch64`) architecture, provide CLI and Horizon access, and allow launching virtual machines. 

{{% notice Warning %}}You can't run DevStack and Kolla-Ansible on the same VM at the same time. Use separate VMs for each approach. If you run both on the same host, port conflicts will cause deployment failures.{{% /notice %}} 

## Configure an external network interface

Configure an external network interface to ensure that OpenStack can use `eth1` as the external/provider network:

```console
sudo ip addr flush dev eth1
sudo ip link set eth1 up
```

## Install system dependencies

Install packages for Python builds and OpenStack dependencies:

```console
sudo apt update

sudo apt install -y \
python3-venv python3-dev python3-pip \
gcc libffi-dev libssl-dev \
libdbus-1-dev libglib2.0-dev pkg-config \
meson ninja-build curl
```

## Install Docker

Install Docker to run all OpenStack services as containers:

```console
sudo apt install -y docker.io

sudo systemctl enable docker
sudo systemctl start docker
```

Add user to Docker group:

```console
sudo usermod -aG docker $USER
```

Apply group permissions:

```console
newgrp docker
```
{{% notice Warning %}}
Without applying group permissions, Docker commands will fail with a permission error.
{{% /notice %}}

Verify Docker installation:

```console
docker run hello-world
```

## Create Python virtual environment

To isolate dependencies required for Kolla-Ansible, create a virtual environment:

```console
python3 -m venv ~/kolla-venv
source ~/kolla-venv/bin/activate
```

## Install Kolla-Ansible and dependencies

Install the following tools to deploy and manage OpenStack services:

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


## Configure Kolla

Copy the default configuration files and inventory into place:

```console
sudo mkdir -p /etc/kolla
sudo chown $USER:$USER /etc/kolla

cp -r ~/kolla-venv/share/kolla-ansible/etc_examples/kolla/* /etc/kolla
cp ~/kolla-venv/share/kolla-ansible/ansible/inventory/all-in-one .
```


## Edit globals.yml

Edit the configuration in `globals.yml`:

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

nova_compute_virt_type: "qemu"
```

The following are some of the key configuration choices:

- `kolla_base_distro: "debian"` — ensures Arm-compatible container images are available
- `openstack_tag_suffix: "-aarch64"` — ensures the correct image variant is selected
- `kolla_internal_vip_address: "127.0.0.1"` — avoids Azure networking issues on single-node deployments
- `enable_keepalived: "no"` — required for single-node deployments
- `nova_compute_virt_type: "qemu"` — ensures Nova uses QEMU (Quick Emulator) on Arm VMs where KVM (Kernel-based Virtual Machine) is unavailable


## Configure Nova

Arm-based Azure VMs do not support KVM virtualization. Update the configuration for Nova to account for this:

```console
sudo mkdir -p /etc/kolla/config

cat <<EOF | sudo tee /etc/kolla/config/nova.conf
[libvirt]
virt_type = qemu
cpu_mode = none
EOF
```

Setting `virt_type = qemu` and `cpu_mode = none` ensures Nova uses QEMU emulation, which works on Arm VMs where KVM is unavailable. Kolla deploys libvirt inside its own `nova_libvirt` container and manages the connection URI automatically.

## Generate passwords

Create all required passwords for OpenStack services:

```console
kolla-genpwd
```

## Deploy OpenStack

The deployment runs in five stages. Each stage must complete successfully before the next one starts.

| Stage | Command | What it does |
|-------|---------|-------------|
| Bootstrap | `bootstrap-servers` | Configures the host: Docker users, directories, and system settings |
| Prechecks | `prechecks` | Validates that the environment meets all requirements |
| Pull | `pull` | Downloads OpenStack container images from the registry |
| Deploy | `deploy` | Starts all OpenStack service containers |
| Post-deploy | `post-deploy` | Generates admin credentials and writes `admin-openrc.sh` |

Run each command and wait for it to complete before proceeding:

```console
kolla-ansible bootstrap-servers -i all-in-one
```

The output is similar to:

```output

PLAY RECAP ***************************************************************************************************************************
localhost                  : ok=41   changed=13   unreachable=0    failed=0    skipped=30   rescued=0    ignored=0
```

{{% notice Note %}}
Kolla-Ansible modifies Docker's systemd unit files during bootstrap. If Docker is already running, the service can fail with the following error:

```output
RUNNING HANDLER [openstack.kolla.docker : Restart docker]
fatal: [localhost]: FAILED! => {"changed": false, "msg": "Unable to start service docker: Job for docker.service failed because the control process exited with error code.\nSee \"systemctl status docker.service\" and \"journalctl -xeu docker.service\" for details.\n"}
```
Run these three commands to recover:

```console
sudo systemctl daemon-reload
sudo systemctl reset-failed docker.socket docker.service
sudo systemctl restart docker
```
`daemon-reload` picks up the updated unit files written by Kolla-Ansible.`reset-failed` clears the failed state that was blocking the restart.`restart docker` starts Docker cleanly.

After Docker is running, re-run the bootstrap step.
{{% /notice %}}


```console
kolla-ansible prechecks -i all-in-one 
```

The output is similar to:

```output
PLAY RECAP ***************************************************************************************************************************
localhost                  : ok=96   changed=0    unreachable=0    failed=0    skipped=142  rescued=0    ignored=0
```
 {{% notice Note %}}
Kolla-Ansible manages libvirt inside its own `nova_libvirt` container. If host `libvirtd` is running, prechecks will fail with:

```output
TASK [nova-cell : Checking that host libvirt is not running]
fatal: [localhost]: FAILED!
```

To fix this, stop and disable the host libvirt service before running prechecks:

```console
sudo systemctl stop libvirtd 2>/dev/null || true
sudo systemctl disable libvirtd 2>/dev/null || true
sudo rm -f /var/run/libvirt/libvirt-sock
```

Then re-run prechecks.
{{% /notice %}}

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
kolla-ansible deploy -i all-in-one
```

The output is similar to:

```output
PLAY [Apply role skyline] ************************************************************************************************************
skipping: no hosts matched

PLAY RECAP ***************************************************************************************************************************
localhost                  : ok=368  changed=34   unreachable=0    failed=0    skipped=267  rescued=0    ignored=0
```

The deploy step starts all OpenStack service containers. It takes the longest of the five stages — allow 20 to 30 minutes.

```console
kolla-ansible post-deploy -i all-in-one
```

## Install the OpenStack client and load credentials

The OpenStack CLI is not included in Kolla-Ansible. Install it inside the virtual environment, then load the admin credentials that `post-deploy` generated:

```console
source ~/kolla-venv/bin/activate
pip install python-openstackclient
source /etc/kolla/admin-openrc.sh
```

## Verify services

Confirm that all Nova compute services and Neutron network agents are running:

```console
openstack compute service list
```

The output is similar to:

```output
+--------------------------------------+----------------+--------------+----------+---------+-------+----------------------------+
| ID                                   | Binary         | Host         | Zone     | Status  | State | Updated At                 |
+--------------------------------------+----------------+--------------+----------+---------+-------+----------------------------+
| bcb60746-4219-44a7-b850-5f9b28ec12d7 | nova-scheduler | ansible-d8ps | internal | enabled | up    | 2026-04-14T07:38:13.000000 |
| 2054f4ad-2492-46e4-990a-4fdf7d40e20f | nova-conductor | ansible-d8ps | internal | enabled | up    | 2026-04-14T07:38:11.000000 |
| b0d28456-483b-4a9c-bcaf-5932364e32b6 | nova-compute   | ansible-d8ps | nova     | enabled | up    | 2026-04-14T07:38:16.000000 |
+--------------------------------------+----------------+--------------+----------+---------+-------+----------------------------+
```

```console
openstack network agent list
```

The output is similar to:

```output
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

All services should show `enabled` and state `up`. If any service shows `down`, check the container logs with `docker logs <container_name>`.

## What you've accomplished and what's next

In this section, you deployed OpenStack using Kolla-Ansible on an Azure Cobalt 100 Arm64 VM. The deployment ran all OpenStack services as Docker containers, including Nova, Neutron, Keystone, Glance, and Horizon. 

Your environment is now ready to launch and manage virtual machines. In the next section, you'll validate the OpenStack deployment and launch a test VM instance.

