---
# User change
title: "Configure Redis multi-node"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

### Multi-node configuration
A Redis multi-node cluster requires 3 primary and 3 replica nodes in a minimal configuration to work properly.  

You can use 6 different ports of the same host as shown in this command:
```console
redis-cli --cluster create HOST:port1 HOST:port2 HOST:port3 HOST:port4 HOST:port5 HOST:port6
```

Alternatively, create 6 different hosts with Redis server running on same port as shown:
```console
redis-cli --cluster create HOST1:port HOST2:port HOST3:port HOST4:port HOST5:port HOST6:port
```
Here, you are using the second approach, where you create 6 different hosts with Redis server running on **6379** port.

Shown here is the minimal template of **redis.conf** file:

```console
bind 0.0.0.0
protected-mode no
port 6379
cluster-enabled yes
cluster-config-file nodes.conf
cluster-node-timeout 5000
daemonize yes
appendonly yes
```

To connect to the remote Redis multi-node cluster, you need to use Redis Client (`redis-cli`) with:
- **-c** option to enable cluster mode
- **-h** option providing hostname
- **-p** option providing the port number.


## Create a Redis cluster

After the Redis installation has been completed on all servers, lift the cluster up with the help of the following command.

```console
redis-cli --cluster create {redis-deployment[0].public_ip}:6379 {redis-deployment[1].public_ip}:6379 {redis-deployment[2].public_ip}:6379 {redis-deployment[3].public_ip}:6379 {redis-deployment[4].public_ip}:6379 {redis-deployment[5].public_ip}:6379 --cluster-replicas 1
```
Replace `redis-deployment[n].public_ip` with their respective values.

The output should be similar to:

```output
>>> Performing hash slots allocation on 6 nodes...
Master[0] -> Slots 0 - 5460
Master[1] -> Slots 5461 - 10922
Master[2] -> Slots 10923 - 16383
Adding replica ec2-3-142-208-82.us-east-2.compute.amazonaws.com:6379 to ec2-18-117-150-63.us-east-2.compute.amazonaws.com:6379
Adding replica ec2-52-15-94-91.us-east-2.compute.amazonaws.com:6379 to ec2-18-191-103-96.us-east-2.compute.amazonaws.com:6379
Adding replica ec2-3-133-91-199.us-east-2.compute.amazonaws.com:6379 to ec2-18-220-255-133.us-east-2.compute.amazonaws.com:6379
M: e01e0295b9e1e4129f86c33880f8eb5873c77f05 ec2-18-117-150-63.us-east-2.compute.amazonaws.com:6379
   slots:[0-5460] (5461 slots) master
M: a871235e3fc81a8feee28527c3ae1435d4f9a7f0 ec2-18-191-103-96.us-east-2.compute.amazonaws.com:6379
   slots:[5461-10922] (5462 slots) master
M: d8965922e7ec90de5e8218c136f2b744be4cb258 ec2-18-220-255-133.us-east-2.compute.amazonaws.com:6379
   slots:[10923-16383] (5461 slots) master
S: 54214adb94bd90ca4ca69d9ca1cf4469594b7b48 ec2-3-133-91-199.us-east-2.compute.amazonaws.com:6379
   replicates d8965922e7ec90de5e8218c136f2b744be4cb258
S: 0e088022aabf1d8eaa65fef9b87dd46a9434caf6 ec2-3-142-208-82.us-east-2.compute.amazonaws.com:6379
   replicates e01e0295b9e1e4129f86c33880f8eb5873c77f05
S: cadd3b1b0c3975726fbf9859105df8ef60b837d2 ec2-52-15-94-91.us-east-2.compute.amazonaws.com:6379
   replicates a871235e3fc81a8feee28527c3ae1435d4f9a7f0
Can I set the above configuration? (type 'yes' to accept): yes
>>> Nodes configuration updated
>>> Assign a different config epoch to each node
>>> Sending CLUSTER MEET messages to join the cluster
Waiting for the cluster to join
...
>>> Performing Cluster Check (using node ec2-18-117-150-63.us-east-2.compute.amazonaws.com:6379)
M: e01e0295b9e1e4129f86c33880f8eb5873c77f05 ec2-18-117-150-63.us-east-2.compute.amazonaws.com:6379
   slots:[0-5460] (5461 slots) master
   1 additional replica(s)
M: a871235e3fc81a8feee28527c3ae1435d4f9a7f0 172.31.26.201:6379
   slots:[5461-10922] (5462 slots) master
   1 additional replica(s)
M: d8965922e7ec90de5e8218c136f2b744be4cb258 172.31.19.70:6379
   slots:[10923-16383] (5461 slots) master
   1 additional replica(s)
S: cadd3b1b0c3975726fbf9859105df8ef60b837d2 172.31.29.216:6379
   slots: (0 slots) slave
   replicates a871235e3fc81a8feee28527c3ae1435d4f9a7f0
S: 0e088022aabf1d8eaa65fef9b87dd46a9434caf6 172.31.26.125:6379
   slots: (0 slots) slave
   replicates e01e0295b9e1e4129f86c33880f8eb5873c77f05
S: 54214adb94bd90ca4ca69d9ca1cf4469594b7b48 172.31.22.1:6379
   slots: (0 slots) slave
   replicates d8965922e7ec90de5e8218c136f2b744be4cb258
[OK] All nodes agree about slots configuration.
>>> Check for open slots...
>>> Check slots coverage...
[OK] All 16384 slots covered.
```

## Status of the Redis Cluster

`cluster info` provides **info** style information about Redis Cluster vital parameters.
```console
redis-cli -c -h {redis-deployment[n].public_ip} -p 6379 cluster info
```
Replace `{redis-deployment[n].public_ip}` with the IP of any of the instances created.

The output should be similar to:

```output
cluster_state:ok
cluster_slots_assigned:16384
cluster_slots_ok:16384
cluster_slots_pfail:0
cluster_slots_fail:0
cluster_known_nodes:6
cluster_size:3
cluster_current_epoch:6
cluster_my_epoch:1
cluster_stats_messages_ping_sent:482
cluster_stats_messages_pong_sent:478
cluster_stats_messages_sent:960
cluster_stats_messages_ping_received:473
cluster_stats_messages_pong_received:482
cluster_stats_messages_meet_received:5
cluster_stats_messages_received:960
```

**cluster_state** is **ok** if the node is able to receive queries.

The `cluster nodes` command can be sent to any node in the cluster and provides the state of the cluster and the information for each node according to the local view the queried node has of the cluster.
```console
redis-cli -c -h {redis-deployment[n].public_ip} -p 6379 cluster nodes
```
The output should be similar to:

```output
a871235e3fc81a8feee28527c3ae1435d4f9a7f0 172.31.26.201:6379@16379 master - 0 1678791540000 2 connected 5461-10922
d8965922e7ec90de5e8218c136f2b744be4cb258 172.31.19.70:6379@16379 master - 0 1678791539596 3 connected 10923-16383
cadd3b1b0c3975726fbf9859105df8ef60b837d2 172.31.29.216:6379@16379 slave a871235e3fc81a8feee28527c3ae1435d4f9a7f0 0 1678791539000 6 connected
0e088022aabf1d8eaa65fef9b87dd46a9434caf6 172.31.26.125:6379@16379 slave e01e0295b9e1e4129f86c33880f8eb5873c77f05 0 1678791540800 5 connected
e01e0295b9e1e4129f86c33880f8eb5873c77f05 172.31.23.74:6379@16379 myself,master - 0 1678791539000 1 connected 0-5460
54214adb94bd90ca4ca69d9ca1cf4469594b7b48 172.31.22.1:6379@16379 slave d8965922e7ec90de5e8218c136f2b744be4cb258 0 1678791541300 4 connected
```

## Connecting to Redis cluster from local machine

Execute the steps below to connect to the remote Redis server from your local machine.
1. Install redis-tools to interact with redis-server.
```console
apt install redis-tools
```
2. Connect to redis-server through redis-cli.
```console
redis-cli -c -h <public-IP-address> -p 6379
```
The output will be:
```output
ubuntu@ip-172-31-38-39:~$ redis-cli -c -h ec2-18-117-150-63.us-east-2.compute.amazonaws.com -p 6379
ec2-18-117-150-63.us-east-2.compute.amazonaws.com:6379>
```
3. Try out commands in the redis-cli.              
The redis-cli will run in interactive mode. You can connect to any of the nodes, the command will get redirected to primary node.
```console
ec2-18-117-150-63.us-east-2.compute.amazonaws.com:6379> ping
PONG
ec2-18-117-150-63.us-east-2.compute.amazonaws.com:6379> set name test
-> Redirected to slot [5798] located at 172.31.26.201:6379
OK
172.31.26.201:6379> get name
"test"
172.31.26.201:6379> set ans sample
-> Redirected to slot [2698] located at 172.31.23.74:6379
OK
172.31.23.74:6379> get ans
"sample"
172.31.23.74:6379> get name
-> Redirected to slot [5798] located at 172.31.26.201:6379
"test"
172.31.26.201:6379>
```
You have successfully installed Redis in a multi-node configuration.

### Clean up resources

Run `terraform destroy` to delete all resources created.

```console
terraform destroy
```




