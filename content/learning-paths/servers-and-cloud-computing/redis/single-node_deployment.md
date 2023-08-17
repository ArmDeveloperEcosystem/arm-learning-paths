---
# User change
title: "Configure Redis single-node"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
##  Redis deployment configurations

Getting Redis up and running with the default out of box configuration file is straightforward and easy. Once you have it working, we recommend to follow the [Learn how to Tune Redis](/learning-paths/servers-and-cloud-computing/redis_tune/) learning path to improve Redis performance.

### Single node configuration
By default Redis runs on localhost (`127.0.0.1`) on port **6379**. As a result, port **6379** becomes unavailable for binding with the public IP of the remote server. You need to set the bind configuration option in the **redis.conf** file to `0.0.0.0`.

For a single-node Redis server, set the following configuration options as shown in the **redis.conf** file:
```console
bind 0.0.0.0
port 6379
protected-mode yes
cluster-enabled no
daemonize yes
appendonly no
```

To connect to the remote Redis server, you need to use Redis Client (`redis-cli`) with:
- **-h** option providing hostname
- **-p** option providing the port number  

### Connect to the Redis server from local machine

Execute the steps below to connect to the remote Redis server from your local machine.

1. Install redis-tools to interact with redis-server:
```console
sudo apt install redis-tools
```
2. Connect to the redis-server through `redis-cli`:
```console
redis-cli -h <public-IP-address> -p 6379
```
The output from this command will be similar to:
```output
ubuntu@ip-172-31-38-39:~$ redis-cli -h 172.31.30.40 -p 6379
172.31.30.40:6379> 
```
3. Authorize Redis with the password you set in the `playbook.yaml` file using `AUTH`.
An example of authorizing Redis is shown below:
```output
172.31.30.40:6379> ping
(error) NOAUTH Authentication required.
172.31.30.40:6379> AUTH 123456789
OK
172.31.30.40:6379> ping
PONG
```
4. Try out commands in the redis-cli.
Shown here is the output from running some commands:

```output
172.31.30.40:6379> set name test
OK
172.31.30.40:6379> get name
"test"
172.31.30.40:6379>
```
You have successfully installed Redis in a single-node configuration.



