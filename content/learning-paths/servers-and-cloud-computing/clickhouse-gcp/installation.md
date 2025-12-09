---
title: Install ClickHouse
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install ClickHouse on GCP VM
This guide covers installing, configuring, and validating ClickHouse on a GCP SUSE Linux Arm64 VM. It includes system preparation, installing ClickHouse with the official installer, verifying the setup, starting the server, and connecting via the client. The guide also configures ClickHouse as a systemd service to ensure reliable, automatic startup on Arm-based environments.

### Install required system packages and the ClickHouse repo
Refresh system repositories and install basic utilities needed to download and run ClickHouse.

```console
sudo zypper refresh
sudo zypper addrepo -r https://packages.clickhouse.com/rpm/clickhouse.repo -g
sudo zypper --gpg-auto-import-keys refresh clickhouse-stable
```

### Install ClickHouse via the ClickHouse repo
Download and install ClickHouse for SuSE systems:

```console
sudo zypper install -y clickhouse-server clickhouse-client
``` 

This installs:

- **ClickHouse Server** – Runs the core database engine and handles all data storage, queries, and processing.
- **ClickHouse Client** – Provides a command-line interface to connect to the server and run SQL queries.
- **ClickHouse Local** – Allows running SQL queries on local files without starting a server.
- **Default configuration files (/etc/clickhouse-server)** – Stores server settings such as ports, users, storage paths, and performance tuning options.

### Verify the installed version
Confirm that all ClickHouse components are installed correctly by checking their versions.

```console
clickhouse --version
clickhouse server --version
clickhouse client --version
clickhouse local --version
```

You should see an output similar to:
```output
ClickHouse local version 25.11.2.24 (official build).
ClickHouse server version 25.11.2.24 (official build).
ClickHouse client version 25.11.2.24 (official build).
```

### Create ClickHouse user and directories
Create a dedicated system user and required directories for data, logs, and runtime files.

```console
sudo useradd -r -s /sbin/nologin clickhouse || true
sudo mkdir -p /var/lib/clickhouse
sudo mkdir -p /var/log/clickhouse-server
sudo mkdir -p /var/run/clickhouse-client
```
Set proper ownership so ClickHouse can access these directories.

```console
sudo chown -R clickhouse:clickhouse \
  /var/lib/clickhouse \
  /var/log/clickhouse-server \
  /var/run/clickhouse-client
sudo chmod 755 /var/lib/clickhouse \
  /var/log/clickhouse-server \
  /var/run/clickhouse-client
```

### Start ClickHouse Server manually
You can just run the ClickHouse server in the foreground to confirm the configuration is valid.

```console
sudo -u clickhouse clickhouse server --config-file=/etc/clickhouse-server/config.xml
```
Keep this terminal open while testing.

### Connect using ClickHouse Client
Open a new SSH terminal and connect to the ClickHouse server.

```console
clickhouse client
```
Run a test query to confirm connectivity.

```sql
SELECT version();
```
You should see an output similar to:
```output
SELECT version()

Query id: ddd3ff38-c0c6-43c5-8ae1-d9d07af4c372

   ┌─version()───┐
1. │ 25.11.2.24 │
   └─────────────┘

1 row in set. Elapsed: 0.001 sec.
```

Please close the client SSH terminal and press "ctrl-c" in the server SSH terminal to halt the manual invocation of ClickHouse. FYI, the server may take a few seconds to close down when "ctrl-c" is received. 

{{% notice Note %}}
Recent benchmarks show that ClickHouse (v22.5.1.2079-stable) delivers up to 26% performance improvements on Arm-based platforms, such as AWS Graviton3, compared to other architectures, highlighting the efficiency of its vectorized execution engine on modern Arm CPUs.
You can view [this Blog](https://community.arm.com/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/improve-clickhouse-performance-up-to-26-by-using-aws-graviton3)

The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) recommends ClickHouse version v22.5.1.2079-stable, the minimum recommended on the Arm platforms.
{{% /notice %}}

### Create a systemd service
Set up ClickHouse as a system service so it starts automatically on boot.

```console
sudo tee /etc/systemd/system/clickhouse-server.service <<'EOF'
[Unit]
Description=ClickHouse Server
After=network.target

[Service]
Type=simple
User=clickhouse
Group=clickhouse
ExecStart=/usr/bin/clickhouse server --config=/etc/clickhouse-server/config.xml
Restart=always
RestartSec=10
LimitNOFILE=1048576

[Install]
WantedBy=multi-user.target
EOF
```
**Reload systemd and enable the service:**

```console
sudo systemctl enable clickhouse-server
sudo systemctl start clickhouse-server
sudo systemctl daemon-reload
```

{{% notice Note %}}
You may get the following error which can be safely ignored:

"ln: failed to create symbolic link '/etc/init.d/rc2.d/S50clickhouse-server': No such file or directory"
{{% /notice %}}

### Verify ClickHouse service
Ensure the ClickHouse server is running correctly as a background service.

```console
sudo systemctl status clickhouse-server
```

This confirms that the ClickHouse server is running correctly under systemd and ready to accept connections.

```output
● clickhouse-server.service - ClickHouse Server
     Loaded: loaded (/etc/systemd/system/clickhouse-server.service; enabled; vendor preset: disabled)
     Active: active (running) since Thu 2025-11-27 05:07:42 UTC; 18s ago
   Main PID: 4229 (ClickHouseWatch)
      Tasks: 814
        CPU: 2.629s
     CGroup: /system.slice/clickhouse-server.service
             ├─ 4229 clickhouse-watchdog server --config=/etc/clickhouse-server/config.xml
             └─ 4237 /usr/bin/clickhouse server --config=/etc/clickhouse-server/config.xml
```

### Final validation
Reconnect to ClickHouse and confirm it is operational.

```console
clickhouse client
```

```sql
SELECT version();
```

You should see an output similar to:
```output
SELECT version()

Query id: ddd3ff38-c0c6-43c5-8ae1-d9d07af4c372

   ┌─version()───┐
1. │ 25.12.1.168 │
   └─────────────┘

1 row in set. Elapsed: 0.001 sec.
```

ClickHouse is now successfully installed, configured, and running on SUSE Linux Arm64 with automatic startup enabled.
