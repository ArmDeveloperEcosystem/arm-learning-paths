---
title: Set up the Azure Cobalt environment
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create and connect to an Arm64 Azure Cobalt virtual machine

To run QuantLib on Azure Cobalt, first create an Arm64 Ubuntu virtual machine in the Azure portal.

Use the following settings:

| Setting | Value |
|---|---|
| Virtual machine name | `quantlib-cobalt-vm` |
| Region | a Cobalt-supported region such as **West US 2** |
| Availability options | No infrastructure redundancy required |
| Security type | Standard |
| Image | Ubuntu Server 22.04 LTS |
| VM architecture | Arm64 |
| Size | Standard_D4ps_v5 |
| Authentication type | SSH public key |
| SSH public key name | `quantlib-cobalt-vm_key` |
| Username | `azureuser` |

For storage, a `64 GB` OS disk is sufficient for this workflow.

For networking, allow inbound SSH on port `22`. Restricting the source to **My IP** is recommended.

After creating the VM, download the generated private key in `.pem` format if Azure provides one during setup.

Before connecting, update the permissions on the private key from your local machine. SSH refuses to use keys that are readable by other users:

```bash
chmod 600 ~/Downloads/quantlib-cobalt-vm_key.pem
```

Connect to the VM using the key and the public IP address shown in the Azure portal:

```bash
ssh -i ~/Downloads/quantlib-cobalt-vm_key.pem azureuser@<VM_PUBLIC_IP>
```

Replace `<VM_PUBLIC_IP>` with the public IP address of your VM.


After logging in, verify the architecture before installing packages. The rest of this Learning Path assumes you are on an Arm64 system:

```bash
uname -m
```

The expected output is:

```bash
aarch64
```

If you do not see aarch64, check that you created the VM with Arm64 architecture and selected an Azure Cobalt-compatible instance type.

## Install dependencies and download QuantLib

Update the package index and install the required packages:

```bash
sudo apt update
sudo apt install -y build-essential cmake curl libboost-all-dev
```

These packages provide the compiler toolchain, build system support, download tools, and Boost libraries needed to build QuantLib.

Set the QuantLib version as an environment variable, then download the release archive. Keeping the version in `QL_VER` makes later commands easier to repeat or adapt for a newer release:

```bash
export QL_VER=1.41
cd ~
curl -L -o QuantLib-$QL_VER.tar.gz \
https://github.com/lballabio/QuantLib/releases/download/v$QL_VER/QuantLib-$QL_VER.tar.gz
```

Check that the file exists and has a non-zero size:

```bash
ls -lh QuantLib-$QL_VER.tar.gz
```

You should see output showing the file name and size, for example:

```bash
-rw-r--r-- 1 azureuser azureuser 41M QuantLib-1.41.tar.gz
```

If the file is missing or has size 0, re-run the curl command.

## Verify and extract the source archive

Use the `file` command to confirm that the archive is a gzip-compressed tar file:

```bash
file QuantLib-$QL_VER.tar.gz
```

Expected output is similar to:

```bash
QuantLib-1.41.tar.gz: gzip compressed data, max compression, from Unix, original size modulo 2^32 42721280
```

Once confirmed, extract it and move into the extracted directory:

```bash
tar -xzf QuantLib-$QL_VER.tar.gz
cd QuantLib-$QL_VER
```



List the contents to confirm that the source code is ready to configure and build:

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

{{% notice Optional Setup %}}
## Reconnect to Cobalt frequently

If you'll reconnect often, add a shortcut entry to your SSH config:

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

## Use tmux for remote builds

If your SSH session disconnects during the build, the compile job will be killed. To prevent this, install tmux and start a session before running `make`:

```bash
sudo apt update
sudo apt install -y tmux
tmux
```

Run the build commands from inside the tmux session. If your connection drops, reconnect to the VM and re-attach with:

```bash
tmux attach
```
{{% /notice %}}

With your environment set up, move on to the next section to build QuantLib.