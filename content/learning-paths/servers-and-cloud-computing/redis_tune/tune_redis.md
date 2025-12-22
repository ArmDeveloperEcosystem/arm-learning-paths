---
title: "Tune Redis"
weight: 3
layout: "learningpathall"
---

##  Redis Deployment Tuning

Optimizing Redis allows you to gain performance improvement without scaling your deployment up (bigger machines/nodes) or out (more machines/nodes). This gained performance can either be used, or traded for cost savings by reducing the amount of compute resources provisioned. The profile of requests made by clients will vary based on the use case. This means there is no one size fits all set of tuning parameters for Redis. Use the information below as general guidance on tuning Redis.

##  Redis File Configuration

In the [Configure Redis single-node](/learning-paths/servers-and-cloud-computing/redis/single-node_deployment/) section of the [Learn how to deploy Redis on Arm](/learning-paths/servers-and-cloud-computing/redis/) learning path, a bare minimum file server configuration was discussed. In this section, a tuned file server configuration is discussed.

### Top Level redis.conf

A tuned top level configuration file [/etc/redis/redis.conf](https://raw.githubusercontent.com/redis/redis/7.0/redis.conf) is shown below. Only performance relevant parameters are discussed.

```console
################################ SNAPSHOTTING  #################################

save ""

stop-writes-on-bgsave-error no

################################### CLIENTS ####################################

maxclients 10000 

############################## MEMORY MANAGEMENT ################################

maxmemory <bytes>
 

################################ THREADED I/O #################################

io-threads 1
```

* `save`:
  * Redis by default tries to store data on the disk which creates forks that can result in overall system slowdown. You can prevent this by commenting out the lines that begin with "save".
  * To entirely disable snapshotting, you can provide a single empty string argument.
* `stop-writes-on-bgsave-error`:
  *  If you have setup your proper monitoring of the Redis server and persistence, you may want to disable background saving so that Redis will continue to work as usual even if there are problems with disk, permissions, and so forth.
* `maxclients`:
  * If your system has a many connections, set the maxclients to a higher value (default is 10000). 
  * If your resources are limited but you are employing efficient horizontal sharding through a Redis cluster, consider reducing this value to prevent potential bottlenecks from arising.
* `maxmemory`:
  * If maxmemory is not defined, Redis will continuously allocate memory based on its requirements, potentially consuming all available free memory over time. Therefore, it is generally recommended to configure this value to certain limits to prevent this from occurring. 
  * You can allocate 75-80% of your memory to Redis by changing maxmemory value in the configuration file. 
* `io-thread`:
  * Redis is mostly single threaded and usually threading reads does not help much. 
  * Redis documentation advises to use default value because if you need more threads, sharding redis or using pipeline > 1 is a better way to add parallelism.
  * The commented io-threads value in the configuration file is 4, which means Redis will use the default value for io-threads which is 1.  

  #### Client side pipelining

Pipelining is a feature primarily implemented on the client side. When a client uses the Redis client library like [memtier](https://github.com/RedisLabs/memtier_benchmark) does then the client can choose to use pipelining, which is a more effective approach for achieving parallelism. You should use a pipeline ranging from 1 (default) to approximately 20 as a large pipeline value (> 20) will increase latency. You will need to experiment and decide what pipeline value makes the most sense for your use case.



