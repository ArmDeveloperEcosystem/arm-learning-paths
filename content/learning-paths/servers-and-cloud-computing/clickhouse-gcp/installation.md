---
title: Install ClickHouse
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install ClickHouse on GCP VM

This section shows you how to install and validate ClickHouse on your Google Cloud SUSE Linux Arm64 virtual machine. You’ll install ClickHouse using the official repository, verify the installation, start the server, connect using the client, and configure ClickHouse to run as a systemd service for reliable startup.

{{% notice Note %}}On some SUSE configurations, the ClickHouse system user and runtime directories might not be created automatically. The following steps ensure ClickHouse has the required paths and permissions.{{% /notice %}}

### Install required system packages and add the ClickHouse repository

Refresh system repositories and add the ClickHouse repository:

```console
sudo zypper refresh
sudo zypper addrepo -r https://packages.clickhouse.com/rpm/clickhouse.repo -g
sudo zypper --gpg-auto-import-keys refresh clickhouse-stable
```

### Install ClickHouse

Install ClickHouse server and client:

```console
sudo zypper install -y clickhouse-server clickhouse-client
``` 

This installs the following components:

- ClickHouse Server: runs the core database engine and handles data storage, queries, and processing.
- ClickHouse Client: provides a command-line interface to connect to the server and run SQL queries.
- ClickHouse Local: allows running SQL queries on local files without starting a server.
- Default configuration files (`/etc/clickhouse-server`): stores server settings such as ports, users, storage paths, and performance tuning options.

### Verify the installed version

Verify that ClickHouse is installed:

```console
clickhouse --version
clickhouse server --version
clickhouse client --version
clickhouse local --version
```

The output is similar to:
```output
ClickHouse local version 25.11.2.24 (official build).
ClickHouse server version 25.11.2.24 (official build).
ClickHouse client version 25.11.2.24 (official build).
```

### Create ClickHouse user and directories

Create a dedicated system user and required directories for data, logs, and runtime files:

```console
sudo useradd -r -s /sbin/nologin clickhouse || true
sudo mkdir -p /var/lib/clickhouse
sudo mkdir -p /var/log/clickhouse-server
sudo mkdir -p /var/run/clickhouse-client
```

Set proper ownership:

```console
sudo chown -R clickhouse:clickhouse \
  /var/lib/clickhouse \
  /var/log/clickhouse-server \
  /var/run/clickhouse-client
sudo chmod 755 /var/lib/clickhouse \
  /var/log/clickhouse-server \
  /var/run/clickhouse-client
```

### Start ClickHouse server manually

Run the ClickHouse server in the foreground to confirm the configuration is valid:

```console
sudo -u clickhouse clickhouse server --config-file=/etc/clickhouse-server/config.xml
```

Keep this terminal open while testing.

### Connect using ClickHouse client

Open a new SSH terminal and connect to the ClickHouse server:

```console
clickhouse client
```

Run a test query to confirm connectivity:

```sql
SELECT version();
```

The output is similar to:
```output
SELECT version()

Query id: ddd3ff38-c0c6-43c5-8ae1-d9d07af4c372

   ┌─version()───┐
1. │ 25.11.2.24 │
   └─────────────┘

1 row in set. Elapsed: 0.001 sec.
```

Close the client SSH terminal and press `Ctrl+C` in the server SSH terminal to stop the manual invocation of ClickHouse. The server may take a few seconds to shut down.

### Create a systemd service

Set up ClickHouse as a system service so it starts automatically on boot:

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

Reload systemd and enable the service:
```console
sudo systemctl daemon-reload
sudo systemctl enable clickhouse-server
sudo systemctl start clickhouse-server
```

{{% notice Note %}}
You might see the following error, which can be safely ignored:

`ln: failed to create symbolic link '/etc/init.d/rc2.d/S50clickhouse-server': No such file or directory`
{{% /notice %}}

## Verify ClickHouse service

Verify the ClickHouse server is running as a background service:

```console
sudo systemctl status clickhouse-server
```

The output is similar to:

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

Reconnect to ClickHouse and confirm it's operational:

```console
clickhouse client
```

```sql
SELECT version();
```

The output is similar to:
```output
SELECT version()

Query id: ddd3ff38-c0c6-43c5-8ae1-d9d07af4c372

   ┌─version()───┐
1. │ 25.12.1.168 │
   └─────────────┘

1 row in set. Elapsed: 0.001 sec.
```

ClickHouse is now installed, configured, and running on SUSE Linux Arm64 with automatic startup enabled.
