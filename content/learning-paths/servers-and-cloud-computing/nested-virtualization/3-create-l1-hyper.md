---
title: Creating a Hypervisor virtual machine
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Creating a Hypervisor virtual machine on the host

At this point, you have already used command line tools to create, boot, and connect to a guest virtual machine running on your Arm64 host. By the end of this step, you will have another virtual machine running on our host which can serve as a hypervisor for nested virtual machines. To complete this step, you will connect to it over SSH, and verify that it is capable of running a virtual machine.

This process is essentially the same as the previous step up to the point that we get a VM running.

1. Set similar convenience environment variables to the previous step. Our L1 hypervisor will need a bigger disk than the L1 guest, since it will contain an identical 40GB L2 guest image inside it: 

   ``` 
    # If these environment variables are already set, there is no need to re-set them
    export VMDIR="/var/lib/libvirt/images”
    export IMG="${HOME}/Fedora-Cloud-Base-Generic-42-1.1.aarch64.qcow2"

    # Use a different QCOW2 filename for the hypervisor VM
    export DISK_L1_HYPER="${VMDIR}/fedora-l1-hyper.qcow2"

    # Prepare the L1 hypervisor image
    sudo cp "$IMG" "$DISK_L1_HYPER"
    sudo qemu-img resize "$DISK_L1_HYPER" 80G
   ```
2. Create a seed ISO image for the guest hypervisor for cloud-init. We will use the same SSH key pair that we generated or used in the previous step - the main change here is the hostname of the guest. 

   ```
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

3. Start the L1 hypervisor VM. 

   ```
    sudo virt-install \
      --name fedora-l1-hyper \
      --memory 8192 \
      --vcpus 8 \
      --arch aarch64 \
      --machine virt \
      --disk path=${DISK_L1_HYPER},format=qcow2,bus=virtio \
      --disk path=/path/to/seed_hyper.iso,device=cdrom,readonly=on \
      --network network=default,model=virtio \
      --os-variant fedora42 \
      --import \
      --noautoconsole
   ```

4. After the VM has started and has obtained an IP address, we need to shut it down to make some changes to the XML that defined the VM. This step passes a kernel parameter to the VM to enable passthrough of virtualization capability which is what turns our guest into a hypervisor.
   ```
    # Check that VM is fully initialized first
    sudo virsh net-dhcp-leases default 

    # Once this command shows that the VM has an IP address, proceed
    sudo virsh shutdown fedora-l1-hyper 
    sudo virsh list –-all # Verify that VM status is “shut off” 
   ```

5. Next we edit the XML configuration describing the VM and make two changes. First, we import the XML schema for the qemu namespace which allows us to specify additional parameters to the qemu command that actually instantiates the VM. Second, we define a <qemu:commandline> block that enables virtualization functionality in the guest. 

   ```
    sudo virsh edit fedora-l1-hyper 

    # In the XML file defining the virtual machine, change the opening <domain> tag to: 
    <domain type=’kvm’ xmlns:qemu='http://libvirt.org/schemas/domain/qemu/1.0' >

    # At the end of the file, just before the </domain> tag, add the following:
    <qemu:commandline>
      <qemu:arg value='-machine'/>
      <qemu:arg value='virt,virtualization=on'/>
    </qemu:commandline>

    # Save the XML file, and verify that it passes validation against the libvirt schema
   ```

6. At this point, we should be able to boot our L1 hypervisor VM and verify that virtualization is supported:

   ```
    sudo virsh start fedora-l1-hyper
    # After a few seconds...
    sudo virsh net-dhcp-leases default
    ssh –i /path/to/private_key fedora@{ip address}

    #Inside the fedora-l1-hyper VM, verify that virtualization functionality has been passed through
    sudo dmesg | grep -i "el2\|vhe\|kvm"
    # Expected: "CPU: All CPU(s) started at EL2"
    # Expected: "kvm [1]: VHE mode initialized successfully"
    ls -la /dev/kvm
    # /dev/kvm should exist inside the VM
   ```

If you see the line “CPU: All CPU(s) started at EL2”, congratulations! You now have a virtual machine that can function as a hypervisor. We will now install virtualization tooling and instantiate our first L2 guest VM.
 

