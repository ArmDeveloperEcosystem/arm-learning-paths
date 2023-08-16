---
title: "Tune Redis"
weight: 4
layout: "learningpathall"
---



##  Redis Deployment Tuning

Optimizing Redis application allows you to gain performance improvement without scaling your deployment up (bigger machines/nodes) or out (more machines/nodes). This gained performance can either be used, or traded for cost savings by reducing the amount of compute resources provisioned. The profile of requests made by clients will vary based on the use case. This means there is no one size fits all set of tuning parameters for Redis. Use the information below as general guidance on tuning Redis.

##  Redis File Configuration

In the [About Redis deployment configurations](https://learn.arm.com/learning-paths/servers-and-cloud-computing/redis/configurations/) section of the [Learn how to deploy Redis on Arm](https://learn.arm.com/learning-paths/servers-and-cloud-computing/redis/) learning path, a bare minimum file server configuration was discussed. In this section, a tuned file server configuration is discussed.

### Top Level redis.conf

A tuned top level configuration file [/etc/redis/redis.conf](https://raw.githubusercontent.com/redis/redis/7.0/redis.conf) is shown below. Only performance relevant parameters will be discussed.

```
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
  * Redis by defualt tries to store data on the disk which creates forks that can result in overall system slowdown. You can prevent this by commenting out the lines that begin with "save".
  * To entirely disable snapshotting, you can provide a single empty string argument.
* `stop-writes-on-bgsave-error`:
  *  If you have setup your proper monitoring of the Redis server and persistence, you may want to disable background saving so that Redis will continue to work as usual even if there are problems with disk, permissions, and so forth.
* `maxclients`:
  * If your system has a many connections, set the maxclients to a higher value (default is 10000). 
  * If your resources are limited but you're employing efficient horizontal sharding through a Redis cluster, consider reducing this value to prevent potential bottlenecks from arising.
* `maxmemory`:
  * In case maxmemory is not defined, Redis will continuously allocate memory based on its requirements, potentially consuming all available free memory over time. Therefore, it is generally recommended to configure this value to certain limits to prevent this from occurring. 
  * You can allocate 75-80% of your memory to Redis by changing maxmemory value in the configuration file. 
* `io-thread`:
  * Redis is mostly single threaded and usually threading reads doesn't help much. 
  * Redis documentation advises to use default value because if you need more threads, sharding redis or using pipeline > 1 is a better way to add parallelism.
  * Note that by default threading is disabled with the value of 4 which interpreted as setting io-threads to one.  