---
title: Connect to the Cobalt 100 VM and verify Arm64 architecture
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Connect to the Cobalt 100 VM via SSH

Use the public IP address from the previous step to connect to your Cobalt 100 VM:

```bash
ssh -i ~/.ssh/azure_cobalt_key azureuser@<public-ip-address>
```

Replace `<public-ip-address>` with the IP address you retrieved earlier.

If prompted about the host's authenticity, type `yes` to continue connecting. You'll see the Ubuntu welcome message and a command prompt.

## Verify the Arm64 architecture

Confirm you're running on Arm64 architecture:

```bash
uname -m
```

The output is `aarch64`, confirming you're on an Arm64 system.

Check the CPU information:

```bash
lscpu
```

The output shows details about the Cobalt 100 processor, including Architecture (aarch64), CPU count (four for Standard_D4ps_v6), and Vendor ID (ARM).

## Check system information

View detailed system information:

```bash
cat /proc/cpuinfo | head -10
```
The output is similar to:
```output
processor	: 0
BogoMIPS	: 2000.00
Features	: fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma lrcpc dcpop sha3 sm3 sm4 asimddp sha512 sve asimdfhm uscat ilrcpc flagm ssbs sb paca pacg dcpodp sve2 sveaes svebitperm svesha3 svesm4 flagm2 frint svei8mm svebf16 i8mm bf16
CPU implementer	: 0x41
CPU architecture: 8
CPU variant	: 0x0
CPU part	: 0xd49
CPU revision	: 0
```

This displays processor details, including key architectural features of the Cobalt 100 processor:

- **i8mm** (Int8 Matrix Multiplication): Hardware acceleration for 8-bit integer matrix operations, improving performance for machine learning inference workloads
- **bf16** (BFloat16): Support for 16-bit brain floating-point format, enabling efficient deep learning computations with reduced memory footprint
- **sve** and **sve2**: Scalable Vector Extension instructions for enhanced SIMD (Single Instruction, Multiple Data) performance
- **sha256**, **sha3**, **sha512**: Hardware-accelerated cryptographic operations for improved security workload performance

These features make Cobalt 100 well-suited for AI/ML workloads, data analytics, and compute-intensive applications on Arm64 architecture.

Verify the operating system:

```bash
lsb_release -a
```

The output confirms Ubuntu 24.04 LTS (Noble Numbat).

## Install and test software

Update the package lists and install a simple application to verify everything works:

```bash
sudo apt update
sudo apt install -y nginx
```

Check that nginx is running:

```bash
sudo systemctl status nginx
```

The output shows nginx is active and running:

```output
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset:>
     Active: active (running) since Tue 2026-01-27 22:31:28 UTC; 56s ago
       Docs: man:nginx(8)
    Process: 2559 ExecStartPre=/usr/sbin/nginx -t -q -g daemon on; master_proce>
    Process: 2560 ExecStart=/usr/sbin/nginx -g daemon on; master_process on; (c>
   Main PID: 2664 (nginx)
      Tasks: 5 (limit: 19090)
     Memory: 6.8M
        CPU: 26ms
     CGroup: /system.slice/nginx.service
             ├─2664 "nginx: master process /usr/sbin/nginx -g daemon on; master>
             ├─2666 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "">
             ├─2667 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "">
             ├─2668 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "">
             └─2669 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "">

Jan 27 22:31:28 cobaltdemo-vm systemd[1]: Starting A high performance web serve>
Jan 27 22:31:28 cobaltdemo-vm systemd[1]: Started A high performance web server>
```

Test that nginx is working:

```bash
curl http://localhost
```

The output displays the nginx default welcome page HTML, confirming the web server is running correctly:

```output
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

## Clean up resources (optional)

When you're done exploring, delete all resources to avoid ongoing charges:

```bash
az group delete --name cobalt-rg --yes --no-wait
```

This command deletes the resource group and all resources within it. The `--no-wait` flag returns immediately without waiting for the deletion to complete.

## What you've accomplished and what's next

You've deployed a Cobalt 100 VM using an Azure Resource Manager template, connected via SSH, verified the Arm64 architecture, and tested nginx on the running system.

Your template provides a reusable foundation for deploying Cobalt 100 VMs. You can customize it by changing the VM size, modifying the OS image, adding network security rules, including data disks, or deploying multiple VMs.

For production deployments, consider using parameters files for environment-specific configurations, Azure Key Vault for managing SSH keys, monitoring and diagnostics extensions, backup policies, and managed identities for Azure resource access.
