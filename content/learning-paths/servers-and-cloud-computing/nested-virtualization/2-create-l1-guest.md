---
title: Prepare and start an L1 guest virtual machine
description: Create an L1 guest VM from a Fedora cloud image and connect to it over SSH for comparison with a nested VM.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why create a guest VM

Before creating a nested virtual machine (VM), create an L1 guest VM running on the host. The guest VM gives you an unnested VM to compare the performance overhead of virtualization against the additional overhead of nested virtualization. You can use the VM to compare the extra work that's required to create an L1 hypervisor VM.

To create a guest VM, download a cloud image. Make some configuration changes to the base image using `cloud-config`. Then, install and start the VM using `virt-install`. After the VM starts, connect to it to confirm that it started correctly.

## Download an Arm64 cloud image

Download an Arm64 cloud image to use for the VMs:

```bash
curl -LO https://dl.fedoraproject.org/pub/fedora/linux/releases/44/Cloud/aarch64/images/Fedora-Cloud-Base-Generic-44-1.7.aarch64.qcow2
```
To be consistent with the host, Fedora 44 is used in this example. Any recent Linux distribution works.

## Copy and resize the disk image

Make a copy of the base disk image and resize it to give the VM more disk space. For convenience, also set some environment variables:

```bash
export VMDIR="/var/lib/libvirt/images"
export IMG="${HOME}/Fedora-Cloud-Base-Generic-44-1.7.aarch64.qcow2"
export DISK_L1_GUEST="${VMDIR}/fedora-l1-guest.qcow2"

# Prepare the L1 guest image
sudo cp "$IMG" "$DISK_L1_GUEST"
sudo qemu-img resize "$DISK_L1_GUEST" 40G
```

## Create a cloud-init seed ISO

Create a seed ISO image for `cloud-init`. `cloud-init` runs automatically the first time you instantiate the VM, and it can perform some initialization actions for you. `cloud-init` looks for special files called `meta-data` and `user-data` for configuration information. 

You'll create a default unprivileged user (fedora) and ensure that the user has permission to run commands as root using `sudo` without a password. You'll include your public SSH key in the `authorized_keys` of that user so that you can SSH into the VM from the host.

If you don't already have an SSH key-pair to use for the guest VMs, generate a key-pair on the host:

```bash
ssh-keygen -t ed25519 -f ~/.ssh/guest_key -N ""
```

This creates a private key at `~/.ssh/guest_key` and a public key at `~/.ssh/guest_key.pub`. In the `user-data` file, replace `<your-public-key>` with the contents of `~/.ssh/guest_key.pub`. You'll use the matching private key, `~/.ssh/guest_key`, to connect to the VM later.

Create the `user-data` and `meta-data` files, then generate the seed ISO image that you'll attach to the VM. Copy the ISO to the same directory as the `qcow2` VM image that you created earlier:

```bash
 cat > /tmp/user-data <<EOF 
 #cloud-config 
 users: 
  - name: fedora 
    sudo: ALL=(ALL) NOPASSWD:ALL 
    shell: /bin/bash 
    ssh_authorized_keys: 
      - <your-public-key> 
 chpasswd: 
   expire: False 
 ssh_pwauth: False 
 EOF 

 cat > /tmp/meta-data <<EOF 
 instance-id: my-guest 
 local-hostname: my-guest 
 EOF 

 SEEDTMP=$(mktemp -d) 
 cp /tmp/user-data "$SEEDTMP/user-data" 
 cp /tmp/meta-data "$SEEDTMP/meta-data" 
 genisoimage -output ${HOME}/seed_guest.iso \ 
      -volid cidata -joliet -rock -input-charset utf-8 \ 
      "$SEEDTMP/user-data" "$SEEDTMP/meta-data" 
 sudo cp ${HOME}/seed_guest.iso ${VMDIR} 
 rm -rf "$SEEDTMP" 
```

## Start the L1 guest VM

Start the L1 guest VM using `virt-install`:

```bash
 sudo virt-install \
   --name fedora-l1-guest \
   --memory 8192 \
   --vcpus 8 \
   --arch aarch64 \
   --machine virt \
   --disk path=${DISK_L1_GUEST},format=qcow2,bus=virtio \
   --disk path=${VMDIR}/seed_guest.iso,device=cdrom,readonly=on \
   --network network=default,model=virtio \
   --os-variant fedora43 \
   --import \
   --noautoconsole 
```
The `virt-install` command includes parameters for the following:

- The VM image
- The ISO CD image that you created for `cloud-config`
- A `name` to identify the image with `virsh` and `virt-manager`
- The number of virtual CPUs and amount of memory allocated to the VM

 The `os-variant` argument passes hints about which operating system runs. At the time of writing, `fedora44` isn't yet an accepted `os-variant` value. `fedora43`, the most recent value that the `osinfo` database recognizes, is used in the command as an example.

## Connect to the guest VM over SSH

After the VM starts, find its IP address with `virsh net-dhcp-leases`:

```bash
sudo virsh net-dhcp-leases default
```

The output is similar to:

```output
 Expiry Time           MAC address         Protocol   IP address           Hostname   Client ID or DUID
--------------------------------------------------------------------------------------------------------
 2026-10-06 17:11:32   52:54:00:ca:0a:64   ipv4       192.168.122.171/24   -          -
```

Use the IP address from the output to connect with the private key that you created earlier:

```bash
ssh -i ~/.ssh/guest_key fedora@192.168.122.171
```

{{% notice Note %}}
The DHCP lease can appear before the VM finishes its first boot. If SSH reports `Connection refused`, wait a minute for `cloud-init` to finish and the SSH service to start, then try again.
{{% /notice %}}

## What you've accomplished and what's next

You've now created an L1 guest VM and connected to it over SSH. After you've verified that you can connect to the L1 guest VM, exit the shell to return to the host environment.

Next, you'll instantiate a hypervisor VM. 

