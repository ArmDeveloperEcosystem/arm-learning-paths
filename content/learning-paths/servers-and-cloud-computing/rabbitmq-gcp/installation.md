---
title: Install RabbitMQ
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install RabbitMQ on GCP SUSE Arm64 VM
This guide describes a **step-by-step installation of RabbitMQ** on a **Google Cloud Platform SUSE Linux Arm64 virtual machine**, using **RPM packages** for both **Erlang** and **RabbitMQ Server**.

RabbitMQ requires Erlang to be installed before setting up the server.


### Prerequisites

- GCP SUSE Linux Enterprise Server (Arm64)
- Root or sudo privileges
- Outbound internet access

### Refresh System Repositories
This step updates the system’s package list so the operating system knows about the latest software available from its repositories.

```console
sudo zypper refresh
```

### Install Required System Utilities
You can install the basic tools needed to download and manage packages.

```console
sudo zypper install -y curl wget gnupg tar socat logrotate
```

### Download Erlang RPM (Arm64)
RabbitMQ depends on Erlang. Download the Erlang RPM compatible with the Arm64 architecture.

```console
wget https://github.com/rabbitmq/erlang-rpm/releases/download/v26.2.5/erlang-26.2.5-1.el8.aarch64.rpm
sudo rpm -Uvh erlang-26.2.5-1.el8.aarch64.rpm
```

### Verify Erlang Installation
Confirm that Erlang is installed correctly.

```console
erl -eval 'io:format("~s~n", [erlang:system_info(system_version)]), halt().' -noshell
```

You should see an output similar to:

```output
Erlang/OTP 26 [erts-14.2.5] [source] [64-bit] [smp:4:4] [ds:4:4:10] [async-threads:1] [jit]
```

### Download RabbitMQ Server RPM
Download the RabbitMQ Server RPM package.

```console
wget https://github.com/rabbitmq/rabbitmq-server/releases/download/v4.2.0/rabbitmq-server-4.2.0-1.el8.noarch.rpm
sudo rpm -Uvh rabbitmq-server-4.2.0-1.el8.noarch.rpm
```

{{% notice Note %}}
RabbitMQ version 3.11.0 introduced significant performance enhancements for Arm-based architectures. This version requires Erlang 25.0 or later, which brings Just-In-Time (JIT) compilation and modern flame graph profiling tooling to both x86 and ARM64 CPUs. These features result in improved performance on ARM64 architectures.
You can view [this release note](https://github.com/rabbitmq/rabbitmq-server/blob/main/release-notes/3.11.0.md)

The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) recommends RabbitMQ version 3.11.0, the minimum recommended on the Arm platforms.
{{% /notice %}}

### Enable and Start RabbitMQ Service
Enable RabbitMQ to start automatically on boot and start the service immediately.

```console
sudo systemctl enable rabbitmq-server --now
```

### Verify RabbitMQ Service Status
Check the status of the RabbitMQ service.

```console
sudo systemctl status rabbitmq-server
```

The service should be in an active (running) state.

### Enable RabbitMQ Management Plugin
Enable the RabbitMQ management plugin to access the web-based dashboard.

```console
sudo rabbitmq-plugins enable rabbitmq_management
```

### Restart RabbitMQ
Restart RabbitMQ to apply plugin changes.

```console
sudo systemctl restart rabbitmq-server
```

### Verify RabbitMQ Version
Confirm the installed RabbitMQ version.

```console
sudo rabbitmqctl version
```

You should see an output similar to:

```output
4.2.0
```

### Access RabbitMQ Management UI
Create a new RabbitMQ user for remote access

- Create a new `admin` user

**Run these commands on the VM:**

```console
sudo rabbitmqctl add_user admin StrongPassword123
sudo rabbitmqctl set_user_tags admin administrator
sudo rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"
```

**Log in to Management UI**

Now, let’s test it from outside the VM. Open a web browser on your LOCAL machine (Chrome, Firefox, Edge, etc.) and enter the following URL and credentials in the address bar:

- **URL**: http://<VM_IP>:15672
- **Username**: admin
- **Password**: StrongPassword123

Replace `<VM_IP>` with the public IP of your GCP VM.

If everything is set up correctly, you will see a RabbitMQ login page in your browser. It looks like this:

![RabbitMQ page alt-text#center](images/rabbitmq.png "Figure 1: RabbitMQ Login page")

This confirms that your RabbitMQ management dashboard is operational.