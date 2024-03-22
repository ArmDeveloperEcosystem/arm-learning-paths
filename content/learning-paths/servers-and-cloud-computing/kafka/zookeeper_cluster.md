---
# User change
title: "Setup a 3 node Zookeeper Cluster"

weight: 3

layout: "learningpathall"


---

To setup a Kafka cluster, first you need to set up a Zookeeper cluster and configure it. Use the instructions below to setup a 3 node Zookeeper cluster.

## Setup 3 node Zookeeper Cluster:

In this section, you will setup 3 Arm machines as a Zookeeper cluster. Each of the machines is referred to as a node.

### Node 1:

Run the commands shown to download and install Zookeeper on node 1:

```console
mkdir Zookeeper_node1
cd Zookeeper_node1
wget https://dlcdn.apache.org/zookeeper/zookeeper-3.9.2/apache-zookeeper-3.9.2-bin.tar.gz
tar -xzf apache-zookeeper-3.9.2-bin.tar.gz
cd apache-zookeeper-3.9.2-bin
```
Use a file editor of you choice and create a file named `conf/zoo.cfg` with the content shown below:
Replace `zk_2_ip` and `zk_3_ip` with the IP addresses of the node 2 and node 3 respectively.

```console
tickTime=2000 

dataDir=/tmp/zookeeper 

clientPort=2181 

maxClientCnxns=60 

initLimit=10 

syncLimit=5

4lw.commands.whitelist=* 

server.1=0.0.0.0:2888:3888
server.2=zk_2_ip:2888:3888
server.3=zk_3_ip:2888:3888
```
Create the zookeeper ID for this node:

```console
mkdir  /tmp/zookeeper
echo 1 >> /tmp/zookeeper/myid
```

Start Zookeeper server on node 1:

```console
bin/zkServer.sh start
```
The output from this command will look like:

```output
/usr/bin/java
ZooKeeper JMX enabled by default
Using config: /home/ubuntu/apache-zookeeper-3.8.0-bin/bin/../conf/zoo.cfg
Starting zookeeper ... STARTED
```

### Node 2:

Run the following commands to download and install Zookeeper node 2:

```console
mkdir Zookeeper_node2
cd Zookeeper_node2
wget https://dlcdn.apache.org/zookeeper/zookeeper-3.9.2/apache-zookeeper-3.9.2-bin.tar.gz
tar -xzf apache-zookeeper-3.9.2-bin.tar.gz
cd apache-zookeeper-3.9.2-bin
```
Use a file editor of you choice and create a file named `conf/zoo.cfg` with the content shown below:
Replace `zk_1_ip` and `zk_3_ip` with the IP addresses of the node 1 and node 3 respectively.

```console
tickTime=2000

dataDir=/tmp/zookeeper

clientPort=2181

maxClientCnxns=60

initLimit=10

syncLimit=5

4lw.commands.whitelist=* 

server.1=zk_1_ip:2888:3888
server.2=0.0.0.0:2888:3888
server.3=zk_3_ip:2888:3888
```
Create the Zookeeper ID for this node:

```console
mkdir  /tmp/zookeeper
echo 2 >> /tmp/zookeeper/myid
```
Start Zookeeper server on node 2:

```console
bin/zkServer.sh start
```
The output from this command will look like:

```output
/usr/bin/java
ZooKeeper JMX enabled by default
Using config: /home/ubuntu/apache-zookeeper-3.8.0-bin/bin/../conf/zoo.cfg
Starting zookeeper ... STARTED
```

### Node 3:

Run the following commands to download and install Zookeeper node 3:

```console
mkdir Zookeeper_node3
cd Zookeeper_node3
wget https://dlcdn.apache.org/zookeeper/zookeeper-3.9.2/apache-zookeeper-3.9.2-bin.tar.gz
tar -xzf apache-zookeeper-3.9.2-bin.tar.gz
cd apache-zookeeper-3.9.2-bin
```
Use a file editor of you choice and create a file named `conf/zoo.cfg` with the content shown below:
Replace `zk_1_ip` and `zk_2_ip` with the IP addresses of the node 1 and node 2 respectively.

```console
tickTime=2000

dataDir=/tmp/zookeeper

clientPort=2181

maxClientCnxns=60

initLimit=10

syncLimit=5

4lw.commands.whitelist=*
 
server.1=zk_1_ip:2888:3888
server.2=zk_2_ip:2888:3888
server.3=0.0.0.0:2888:3888
```
Create the Zookeeper ID for this node:

```console
mkdir  /tmp/zookeeper
echo 3 >> /tmp/zookeeper/myid
```

Start Zookeeper server on node 3:

```console
bin/zkServer.sh start
```

The output from this command will look like:

```output
/usr/bin/java
ZooKeeper JMX enabled by default
Using config: /home/ubuntu/apache-zookeeper-3.8.0-bin/bin/../conf/zoo.cfg
Starting zookeeper ... STARTED
```

### Verify the Zookeeper Cluster:

The Zookeeper server is now running on all 3 nodes.
 
Run the command below using each of the Zookeeper nodes IP address to check the leader/follower mode:

Replace `zk_1_ip` with the IP address of each of the Zookeeper nodes.

```console
echo stat | nc zk_1_ip 2181
```

The example output from this command is shown:

```output
Latency min/avg/max: 0/0.0/0
Received: 2
Sent: 1
Connections: 1
Outstanding: 0
Zxid: 0x100000000
Mode: leader
Node count: 5
Proposal sizes last/min/max: -1/-1/-1
```

Start the Zookeeper CLI to connect to the cluster. This command can be executed on any of the 3 Zookeeper nodes:

```console
bin/zkCli.sh
```

Write a message into the Zookeeper cluster:

```console
create /FirstZnode "message written to database"
```

Output for this command:

```output
[zk: localhost:2181(CONNECTED) 0] create /FirstZnode “message written to database”
Created /FirstZnode
```

You can read the previously written messages by running the command below from the Zookeeper CLI on any of the nodes:

```console
get /FirstZnode
```

Output for this command:

```output
[zk: localhost:2181(CONNECTED) 1] get /FirstZnode
message written to database
```

