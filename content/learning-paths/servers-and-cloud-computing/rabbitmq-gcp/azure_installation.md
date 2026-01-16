---
title: Install RabbitMQ on Azure Cobalt 100
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install RabbitMQ on Azure Cobalt 100
This guide describes the end-to-end installation of RabbitMQ 4.2.0 on an Azure Cobalt 100 (Arm-based) Ubuntu Pro 24.04 virtual machine. It covers system preparation, Erlang installation, RabbitMQ setup, service configuration, and validation with the management plugin enabled.

### Update system and install build dependencies
This step ensures the operating system is up to date and installs all required packages needed to build Erlang and run RabbitMQ reliably.

```console
sudo apt update
sudo apt install -y build-essential libssl-dev libncurses-dev libtinfo-dev \
                    libgl1-mesa-dev libglu1-mesa-dev libpng-dev libssh-dev \
                    unixodbc-dev wget tar xz-utils git
```

### Build and install Erlang OTP 26
RabbitMQ 4.2.0 requires Erlang OTP 26. This section builds Erlang from source to ensure full compatibility on Arm64.

```console
# Clone Erlang source
git clone https://github.com/erlang/otp.git
cd otp

# Checkout OTP 26 branch
git checkout OTP-26

# Clean previous builds
make clean

# Configure build with SSL/crypto support
./configure --prefix=/usr/local/erlang-26 \
            --enable-smp-support \
            --enable-threads \
            --enable-kernel-poll \
            --with-ssl

# Build and install
make -j$(nproc)
sudo make install
```
### Make Erlang PATH persistent (IMPORTANT)
This step ensures the Erlang binaries are permanently available in the system PATH across sessions and reboots.

```console
echo 'export ERLANG_HOME=/usr/local/erlang-26' | sudo tee /etc/profile.d/erlang.sh
echo 'export PATH=$ERLANG_HOME/bin:$PATH' | sudo tee -a /etc/profile.d/erlang.sh
```

### Download and install RabbitMQ

Download the official RabbitMQ 4.2.0 generic Unix distribution and install it under `/opt/rabbitmq`.

```console
cd ~
wget https://github.com/rabbitmq/rabbitmq-server/releases/download/v4.2.0/rabbitmq-server-generic-unix-4.2.0.tar.xz
sudo mkdir -p /opt/rabbitmq
sudo tar -xvf rabbitmq-server-generic-unix-4.2.0.tar.xz -C /opt/rabbitmq --strip-components=1

# Create directories for logs and database
sudo mkdir -p /var/lib/rabbitmq /var/log/rabbitmq
sudo chown -R $USER:$USER /var/lib/rabbitmq /var/log/rabbitmq
```

## Update PATH environment variable

Make RabbitMQ CLI tools available in the current shell. Add this to `~/.bashrc` or `~/.profile` for persistence across sessions.

```console
export PATH=/usr/local/erlang-26/bin:/opt/rabbitmq/sbin:$PATH
```

Add this line to `~/.bashrc` or `~/.profile` for persistence.

## Configure RabbitMQ systemd service

Configure RabbitMQ to run as a managed systemd service, enabling automatic startup and controlled lifecycle management.

Create `/etc/systemd/system/rabbitmq.service`:

```ini
[Unit]
Description=RabbitMQ broker
After=network.target

[Service]
Type=simple
User=azureuser
Group=azureuser

Environment=HOME=/home/azureuser
Environment=RABBITMQ_HOME=/opt/rabbitmq
Environment=RABBITMQ_MNESIA_BASE=/var/lib/rabbitmq
Environment=RABBITMQ_LOG_BASE=/var/log/rabbitmq
Environment=PATH=/usr/local/erlang-26/bin:/opt/rabbitmq/sbin:/usr/bin

ExecStart=/opt/rabbitmq/sbin/rabbitmq-server
ExecStop=/opt/rabbitmq/sbin/rabbitmqctl shutdown

Restart=on-failure
RestartSec=10
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
```

Reload systemd and start RabbitMQ:

```console
sudo systemctl daemon-reload
sudo systemctl enable rabbitmq
sudo systemctl start rabbitmq
sudo systemctl status rabbitmq
```

### Enable RabbitMQ management plugin
This step enables the RabbitMQ management plugin, which provides a web-based UI and HTTP API for monitoring and administration.

```console
# Ensure config directory exists
sudo mkdir -p /opt/rabbitmq/etc/rabbitmq
sudo chown -R $USER:$USER /opt/rabbitmq/etc/rabbitmq

# Enable management plugin
rabbitmq-plugins enable rabbitmq_management
```

### Verify installation
This section validates that both Erlang and RabbitMQ are installed correctly and running with the expected versions.

**Erlang version:**

```console
erl -eval 'io:format("~s~n", [erlang:system_info(system_version)]), halt().' -noshell
```

You should see an output similar to:
```output
Erlang/OTP 26 [erts-14.2.5.12] [source] [64-bit] [smp:4:4] [ds:4:4:10] [async-threads:1] [jit]
```

**Verify RabbitMQ version:**

```console
rabbitmqctl version
```

You should see an output similar to:
```output
4.2.0
```
RabbitMQ 4.2.0 is successfully installed on an Azure Cobalt 100 Ubuntu Pro 24.04 Arm64 VM with systemd management, persistent storage, logging, and the management plugin enabled.
