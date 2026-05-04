---
title: Set up the Azure Cobalt environment
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create an Arm64 Azure Cobalt virtual machine

To run QuantLib on Azure Cobalt, first create an Arm64 Ubuntu virtual machine in the Azure portal.

Use the following settings:

- **Virtual machine name:** `quantlib-cobalt-vm`
- **Region:** a Cobalt-supported region such as **West US 2**
- **Availability options:** **No infrastructure redundancy required**
- **Security type:** **Standard**
- **Image:** **Ubuntu Server 22.04 LTS**
- **VM architecture:** **Arm64**
- **Size:** **Standard_D4ps_v5**
- **Authentication type:** **SSH public key**
- **Username:** `azureuser`

For storage, a `64 GB` OS disk is sufficient for this workflow.

For networking, allow inbound SSH on port `22`. Restricting the source to **My IP** is recommended.

After creating the VM, download the generated private key in `.pem` format if Azure provides one during setup.

## Connect to the virtual machine

On your local machine, update the permissions on the private key:

```bash
chmod 600 ~/Downloads/quantlib-cobalt-vm_key.pem
```

Then connect using SSH:

```bash
ssh -i ~/Downloads/quantlib-cobalt-vm_key.pem azureuser@<VM_PUBLIC_IP>
```

Replace <VM_PUBLIC_IP> with the public IP address of your VM.

If you’ll reconnect often, add a shortcut entry to your SSH config:

```bash
nano ~/.ssh/config
```

Add: 

```bash
Host quantlib-cobalt
    HostName <VM_PUBLIC_IP>
    User azureuser
    IdentityFile ~/Downloads/quantlib-cobalt-vm_key.pem
```

Then connect with:

```bash
ssh quantlib-cobalt
```

## Confirm that the system is Arm64

After logging in, verify the architecture:

```bash
uname -m
```

The expected output is:

```bash
aarch64
```

If you do not see aarch64, check that you created the VM with Arm64 architecture and selected an Azure Cobalt-compatible instance type.

## Install build dependencies

Update the package index and install required packages:

```bash
sudo apt update
sudo apt install -y build-essential cmake curl libboost-all-dev
```

These packages provide the compiler toolchain, build system support, download tools, and Boost libraries needed to build QuantLib.

## Optional: use tmux for remote builds

If you want the build to continue even if your SSH session disconnects, install tmux:

```bash
sudo apt update
sudo apt install -y tmux
tmux
```

## Download QuantLib

Set the version and download the release archive:

```bash
export QL_VER=1.41

cd ~
curl -L -o QuantLib-$QL_VER.tar.gz \
https://github.com/lballabio/QuantLib/releases/download/v$QL_VER/QuantLib-$QL_VER.tar.gz
```

Check that the file exists. Run:

```bash
ls -lh QuantLib-$QL_VER.tar.gz
```

You should see output showing the file name and size, for example:

```bash
-rw-r--r-- 1 azureuser azureuser 41M QuantLib-1.41.tar.gz
```

If the file is missing or has size 0, re-run the curl command.

## Verify the file type

Use the file command to confirm that the archive is a valid gzip-compressed tar file:
```bash
file QuantLib-$QL_VER.tar.gz
```

Expected output is simlar to:
```bash
QuantLib-1.41.tar.gz: gzip compressed data, max compression, from Unix, original size modulo 2^32 42721280
```

## (Optional) Test archive integrity

To check that the archive is not corrupted, run:
```bash
tar -tzf QuantLib-$QL_VER.tar.gz > /dev/null
```

If the command completes without errors, the archive is valid.

If you see errors such as:

```bash
gzip: stdin: unexpected end of file
tar: Unexpected EOF in archive
```

the download is incomplete or corrupted.l Delete the file and download it again.

## Extract the archive

Once the archive is verified, extract it:
```bash
tar -xzf QuantLib-$QL_VER.tar.gz
```

Then move into the extracted directory:
```bash
cd QuantLib-$QL_VER
```

## Confirm the extracted contents

List the contents:
```bash
ls
```

You should see files and directories such as:
```bash
configure
Makefile.am
ql/
test-suite/
```

This confirms that the source code has been unpacked correctly and is ready to configure and build.
