---
title: Creating a hypervisor virtual machine
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create a hypervisor virtual machine on the host

At this point, you have used command line tools to create, boot, and connect to a guest virtual machine running on your Arm64 host. By the end of this step, you have another virtual machine running on the host that can serve as a hypervisor for nested virtual machines. To complete this step, you connect to it over SSH and verify that it is capable of running a virtual machine.

This process is essentially the same as the previous step up to the point where you get a VM running.

## Set environment variables

Set similar convenience environment variables to the previous step. The L1 hypervisor needs a bigger disk than the L1 guest, because it contains an identical 40GB L2 guest image inside it:

```bash
# If these environment variables are already set, there is no need to re-set them
export VMDIR="/var/lib/libvirt/images"
export IMG="${HOME}/Fedora-Cloud-Base-Generic-44-1.7.aarch64.qcow2"

# Use a different QCOW2 filename for the hypervisor VM
export DISK_L1_HYPER="${VMDIR}/fedora-l1-hyper.qcow2"

# Prepare the L1 hypervisor image
sudo cp "$IMG" "$DISK_L1_HYPER"
sudo qemu-img resize "$DISK_L1_HYPER" 80G
```

## Create a cloud-init seed ISO

Create a seed ISO image for the guest hypervisor for cloud-init. Use the same SSH key pair that you generated or used in the previous step - the main change here is the hostname of the guest.

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
 instance-id: my-hyper 
 local-hostname: my-hyper 
 EOF 

 SEEDTMP=$(mktemp -d) 
 cp /tmp/user-data "$SEEDTMP/user-data" 
 cp /tmp/meta-data "$SEEDTMP/meta-data" 
 genisoimage -output ${HOME}/seed_hyper.iso \
      -volid cidata -joliet -rock -input-charset utf-8 \
      "$SEEDTMP/user-data" "$SEEDTMP/meta-data"
 sudo cp ${HOME}/seed_hyper.iso ${VMDIR} 
 rm -rf "$SEEDTMP" 
```

## Start the L1 hypervisor VM

Start the L1 hypervisor VM:

```bash
 sudo virt-install \
   --name fedora-l1-hyper \
   --memory 8192 \
   --vcpus 16 \
   --arch aarch64 \
   --machine virt \
   --disk path=${DISK_L1_HYPER},format=qcow2,bus=virtio \
   --disk path=${VMDIR}/seed_hyper.iso,device=cdrom,readonly=on \
   --network network=default,model=virtio \
   --os-variant fedora43 \
   --import \
   --noautoconsole
```

## Shut down the VM to edit its configuration

After the VM starts and obtains an IP address, shut it down to make some changes to the XML that defines the VM. These changes pass a kernel parameter to the VM that enables passthrough of virtualization capability, which is what turns the guest into a hypervisor.

```bash
 # Check that the VM is fully initialized first
 sudo virsh net-dhcp-leases default 

 # After this command shows that the VM has an IP address, proceed
 sudo virsh shutdown fedora-l1-hyper 
 sudo virsh list --all # Verify that VM status is "shut off" 
```

## Enable virtualization in the VM configuration

Edit the XML configuration that describes the VM and make two changes. First, import the XML schema for the qemu namespace, which lets you pass additional parameters to the qemu command that instantiates the VM. Second, add a `<qemu:commandline>` block that enables virtualization functionality in the guest.

Open the VM configuration in an editor:

```bash
sudo virsh edit fedora-l1-hyper
```

Change the opening `<domain>` tag to import the qemu namespace schema:

```xml
<domain type='kvm' xmlns:qemu='http://libvirt.org/schemas/domain/qemu/1.0'>
```

Then, just before the closing `</domain>` tag, add the following block:

```xml
<qemu:commandline>
  <qemu:arg value='-machine'/>
  <qemu:arg value='virt,virtualization=on'/>
</qemu:commandline>
```

Save the file. `virsh` validates the XML against the libvirt schema when you save.

## Boot the hypervisor VM and verify virtualization support

Boot the L1 hypervisor VM and verify that virtualization is supported:

```bash
 sudo virsh start fedora-l1-hyper
 # After a few seconds...
 sudo virsh net-dhcp-leases default
 ssh -i ~/.ssh/guest_key fedora@{ip address}
```

Inside the `fedora-l1-hyper` VM, verify that virtualization functionality has been passed through:

```bash
sudo dmesg | grep -i "el2\|vhe\|kvm"
```

The output is similar to:

```output
CPU: All CPU(s) started at EL2
kvm [1]: VHE mode initialized successfully
```

Confirm that `/dev/kvm` exists inside the VM:

```bash
ls -la /dev/kvm
```

If you see the line `CPU: All CPU(s) started at EL2`, you now have a virtual machine that can function as a hypervisor. Next, you install virtualization tooling and instantiate your first L2 guest VM.

