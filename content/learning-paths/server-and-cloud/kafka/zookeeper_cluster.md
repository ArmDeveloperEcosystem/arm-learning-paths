---
# User change
title: "Setup a 3 node Zookeeper Cluster"

weight: 3

layout: "learningpathall"


---

To setup a Kafka cluster, first we need to set up a Zookeeper cluster and configure it. Use the instructions below to setup a 3 node Zookeeper cluster.

## Setup 3 node Zookeeper Cluster:

### Node 1:

```console

mkdir Zookeeper_node1

cd Zookeeper_node1

wget https://dlcdn.apache.org/zookeeper/zookeeper-3.8.0/apache-zookeeper-3.8.0-bin.tar.gz

tar -xzf apache-zookeeper-3.8.0-bin.tar.gz

cd apache-zookeeper-3.8.0-bin

```
We need to create and setup **conf/zoo.cfg** file as shown below on each of the 3 nodes of the Zookeeper cluster. Below is the node 1 **conf/zoo.cfg** file.

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

### Node 2:

  Run the following on Zookeeper node 2.

```console

mkdir Zookeeper_node2

cd Zookeeper_node2

wget https://dlcdn.apache.org/zookeeper/zookeeper-3.8.0/apache-zookeeper-3.8.0-bin.tar.gz

tar -xzf apache-zookeeper-3.8.0-bin.tar.gz

cd apache-zookeeper-3.8.0-bin

```
Below is the node 2 **conf/zoo.cfg** file

```console

tickTime=2000

dataDir=/tmp/zookeeper

clientPort=2182

maxClientCnxns=60

initLimit=10

syncLimit=5

4lw.commands.whitelist=* 

server.1=zk_1_ip:2888:3888
server.2=0.0.0.0:2888:3888
server.3=zk_3_ip:2888:3888

```

### Node 3:

  Run the following on Zookeeper node 3.

```console

mkdir Zookeeper_node3

cd Zookeeper_node3

wget https://dlcdn.apache.org/zookeeper/zookeeper-3.8.0/apache-zookeeper-3.8.0-bin.tar.gz

tar -xzf apache-zookeeper-3.8.0-bin.tar.gz

cd apache-zookeeper-3.8.0-bin

```
Below is the node 3 **conf/zoo.cfg** file

```console

tickTime=2000

dataDir=/tmp/zookeeper

clientPort=2183

maxClientCnxns=60

initLimit=10

syncLimit=5

4lw.commands.whitelist=*
 
server.1=zk_1_ip:2888:3888
server.2=zk_2_ip:2888:3888
server.3=0.0.0.0:2888:3888

```

Create Zookeeper directories on all the three nodes as mentioned below:

Run the following on Zookeeper Node 1:

```console

mkdir  /tmp/zookeeper

echo 1 >> /tmp/zookeeper/myid

```
 
Run the following on  Zookeeper Node 2:

```console

mkdir  /tmp/zookeeper

echo 2 >> /tmp/zookeeper/myid 

```

Run the following on Zookeeper Node 3:

```console

mkdir  /tmp/zookeeper

echo 3 >> /tmp/zookeeper/myid 

```
### Start Zookeeper server on each node:

```console

bin/zkServer.sh start

```

### Verify the Zookeeper Cluster:
 
Run the command below using each of the Zookeeper nodes IP address to check the leader/follower mode of each node.

```console

echo stat | nc zk_1_ip 2181

```
![stat_with_ip (3)](https://user-images.githubusercontent.com/66300308/196909394-b83da0c7-973b-4d90-adc6-8b0451b199c9.png)


Start the Zookeeper CLI to connect to the cluster. This command can be executed on any of the 3 Zookeeper nodes.

```console

bin/zkCli.sh

```

To write a message into the Zookeeper cluster run the command as shown here

```console

create /FirstZnode "message you want to write in database"

```
![zookeeper1_message_written](https://user-images.githubusercontent.com/66300308/196949925-a53acf2b-1bc2-4ba0-afe8-e20e44127442.png)

You can read the previously written messages by running the command below from the Zookeeper CLI on any of the nodes.

```console

get /FirstZnode

```
![zookeeper3_output](https://user-images.githubusercontent.com/66300308/196901665-56c1e4d7-f760-42ed-8918-5f2c6908082c.png)

