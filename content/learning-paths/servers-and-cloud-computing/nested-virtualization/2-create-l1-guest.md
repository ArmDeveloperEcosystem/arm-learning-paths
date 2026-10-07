---
title: Preparing and starting an L1 guest virtual machine
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare and start an L1 guest VM

Before you create a nested VM, you create an L1 guest VM running on the host. This gives you an unnested VM to compare the performance overhead of virtualization against the additional overhead of nested virtualization, and lets you compare the extra work required to create an L1 hypervisor VM in the next step.

To create a VM, you first download a cloud image, make some configuration changes to the base image using cloud-config, and install and start the VM using `virt-install`. After the VM starts, you connect to it to confirm that it started correctly.

## Download an Arm64 cloud image

Download an Arm64 cloud image to use for the VMs. To be consistent with the host, this example uses Fedora 44, but any recent Linux distribution works:

```bash
curl -LO https://dl.fedoraproject.org/pub/fedora/linux/releases/44/Cloud/aarch64/images/Fedora-Cloud-Base-Generic-44-1.7.aarch64.qcow2
```

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

Create a seed ISO image for `cloud-init`. `cloud-init` runs automatically the first time you instantiate the virtual machine, and can perform some initialization actions for you. `cloud-init` looks for special files called `meta-data` and `user-data` for configuration information. In this case, you create a default unprivileged user (fedora), ensure that the user has permission to run commands as root using `sudo` without a password, and include your public SSH key in the `authorized_keys` of that user so that you can SSH into the virtual machine from the host.

If you do not already have an SSH key-pair to use for the guest VMs, generate one on the host now:

```bash
ssh-keygen -t ed25519 -f ~/.ssh/guest_key -N ""
```

This creates a private key at `~/.ssh/guest_key` and a public key at `~/.ssh/guest_key.pub`. In the `user-data` below, replace `<your-public-key>` with the contents of `~/.ssh/guest_key.pub`. You use the matching private key, `~/.ssh/guest_key`, to connect to the VM later.

After creating these files, you generate a special CD disk image (format ISO) that is attached to the VM when you instantiate it. After you have the ISO image, copy it to the same directory as the qcow2 VM image you created in the previous step.

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

Start the L1 guest VM using `virt-install`. The `virt-install` command includes parameters for the VM image, the ISO CD image you created for `cloud-config`, a `name` parameter to identify the image with `virsh` and `virt-manager`, and parameters for the number of virtual CPUs and amount of memory allocated to the VM. The `os-variant` argument passes hints about which operating system runs. At the time of writing, `fedora44` is not yet an accepted `os-variant` value, so this example uses `fedora43`, the most recent value the `osinfo` database recognizes.

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

Use the IP address from the output to connect with the private key you created earlier:

```bash
ssh -i ~/.ssh/guest_key fedora@192.168.122.171
```

{{% notice Note %}}
The DHCP lease can appear before the VM finishes its first boot. If SSH reports `Connection refused`, wait a minute for `cloud-init` to finish and the SSH service to start, then try again.
{{% /notice %}}

At this point, you should be connected to the L1 guest VM over SSH.

In the next step, you instantiate a hypervisor VM, which requires some additional configuration steps. After you have verified that you can connect to the L1 guest VM, you can exit the shell to return to the host environment.

