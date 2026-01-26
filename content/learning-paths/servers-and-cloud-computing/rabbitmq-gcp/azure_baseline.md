---
title: Validate RabbitMQ on Azure
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run a baseline test with RabbitMQ
This section shows you how to validate a working RabbitMQ 4.2.0 installation with Erlang OTP 26 on an Azure Ubuntu Arm64 VM.  

All steps use the command line and are suitable for baseline verification.

## Verify RabbitMQ service status

```console
sudo systemctl status rabbitmq
```

### Verify Erlang Version
RabbitMQ depends on Erlang. This step ensures the broker is using Erlang OTP 26.

```console
erl -eval 'io:format("~s~n", [erlang:system_info(system_version)]), halt().' -noshell
```

### Verify RabbitMQ Version
Confirm the installed RabbitMQ version.

```console
rabbitmqctl version
```

### Verify Enabled Plugins
List all enabled plugins and confirm that the management plugins are active.

```console
rabbitmq-plugins list -e
```

```output
Listing plugins with pattern ".*" ...
 Configured: E = explicitly enabled; e = implicitly enabled
 | Status: * = running on rabbit@lpprojectubuntuarm64
 |/
[E*] rabbitmq_management       4.2.0
[e*] rabbitmq_management_agent 4.2.0
[e*] rabbitmq_web_dispatch     4.2.0
````

This confirms that:

- The management UI is enabled
- Required supporting plugins are running

### Check RabbitMQ Node Health
Retrieve detailed runtime and resource information for the RabbitMQ node.

```console
rabbitmqctl status
```
This confirms that:

- Node is running
- No alarms are reported
- Erlang version matches OTP 26

### Ensure RabbitMQ Configuration Directory Permissions
RabbitMQ requires write access to its configuration directory for plugin management.

```console
sudo mkdir -p /opt/rabbitmq/etc/rabbitmq
sudo chown -R azureuser:azureuser /opt/rabbitmq/etc/rabbitmq
```

### Create a Baseline Test Virtual Host
Create an isolated virtual host for baseline testing.

```console
rabbitmqctl add_vhost test_vhost
rabbitmqctl set_permissions -p test_vhost guest ".*" ".*" ".*"
```

This ensures:

- Tests do not interfere with default workloads
- Full permissions are available for validation

### Download RabbitMQ Admin CLI
Download the `rabbitmqadmin` CLI tool from the management endpoint.

```console
wget http://localhost:15672/cli/rabbitmqadmin -O ~/rabbitmqadmin
chmod +x ~/rabbitmqadmin
```

This CLI is used to perform queue and message operations.

### Declare a Test Queue
Create a non-durable test queue in the test virtual host.

```console
~/rabbitmqadmin -V test_vhost declare queue name=test durable=false
```

### Publish a Test Message
Publish a sample message to the test queue using the default exchange.

```console
~/rabbitmqadmin -V test_vhost publish \
  exchange=amq.default \
  routing_key=test \
  payload="Hello RabbitMQ"
```

This validates:

- Message routing
- Exchange-to-queue binding behavior

### Consume The Test Message
Retrieve and remove the message from the queue.

```console
~/rabbitmqadmin -V test_vhost get queue=test count=1
```

You should see an output similar to:

```output
+-------------+----------+---------------+----------------+---------------+------------------+------------+-------------+
| routing_key | exchange | message_count |    payload     | payload_bytes | payload_encoding | properties | redelivered |
+-------------+----------+---------------+----------------+---------------+------------------+------------+-------------+
| test        |          | 0             | Hello RabbitMQ | 14            | string           |            | False       |
+-------------+----------+---------------+----------------+---------------+------------------+------------+-------------+
```

- Message payload: Hello RabbitMQ
- Queue becomes empty after consumption

This baseline validates a healthy RabbitMQ 4.2.0 deployment running on Erlang/OTP 26 on an Azure Ubuntu Arm64 VM. Core components, plugins, and node health were verified, followed by successful message publish and consume operations.
