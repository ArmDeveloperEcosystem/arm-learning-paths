---
# User change
title: "Run an end-to-end Attestation with Arm CCA"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Run the Key Broker Server

The concept of a KBS is a common one in confidential computing, and there are multiple open-source implementations, including the [Trustee](https://github.com/confidential-containers/trustee) from the [CNCF Confidential Containers](https://confidentialcontainers.org/) project. The KBS in this learning path is part of the [Veraison](https://github.com/veraison) project. It has been created specifically for educational purposes and not designed for production use. Its aim is to be small and simple to understand.

First, pull the docker container image with the pre-built KBS and then run the container:

```bash
docker pull armswdev/cca-learning-path:cca-key-broker-v1
docker run --rm -it armswdev/cca-learning-path:cca-key-broker-v1
```

Now within your running docker container, get a list of network interfaces:

```bash
ip -c a
```

The output should look like:

```output
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
20: eth0@if21: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether 02:42:ac:11:00:02 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 172.17.0.2/16 brd 172.17.255.255 scope global eth0
       valid_lft forever preferred_lft forever
```
Start the key broker server on the `eth0` network interface:

```bash
./keybroker-server -v --addr 172.17.0.2
```

The output should look like:

```output
INFO starting 16 workers
INFO Actix runtime found; starting in Actix runtime
INFO starting service: "actix-web-service-172.17.0.2:8088", workers: 16, listening on: 172.17.0.2:8088
```

With the key broker server running in one terminal, open up a new terminal in which you will run the key broker client.

## Run the Key Broker Client

In a new terminal, pull the docker container image which contains the FVP and pre-built software binaries to run the key broker client in a realm.

```bash
docker pull armswdev/cca-learning-path:cca-simulation-v1
```

Now run this docker container:
```bash
docker run --rm -it armswdev/cca-learning-path:cca-simulation-v1
```

Within you running container, launch the `run-cca-fvp.sh` script to run the Arm CCA pre-built binaries on the FVP:

```bash
./run-cca-fvp.sh
```
The run-cca-fvp.sh script uses the screen command to connect to the different UARTs in the FVP.

You should see the host Linux kernel boot on your terminal. You will be prompted to log in to the host. Enter root as the username:

```output
[    4.169458] Run /sbin/init as init process
[    4.273748] EXT4-fs (vda): re-mounted 64d1bcff-5d03-412c-83c6-48ec4253590e r/w. Quota mode: none.
Starting syslogd: OK
Starting klogd: OK
Running sysctl: OK
Starting network: [    5.254843] smc91x 1a000000.ethernet eth0: link up, 10Mbps, half-duplex, lpa 0x0000
udhcpc: started, v1.36.1
udhcpc: broadcasting discover
udhcpc: broadcasting select for 172.20.51.1, server 172.20.51.254
udhcpc: lease of 172.20.51.1 obtained from 172.20.51.254, lease time 86400
deleting routers
adding dns 172.20.51.254
OK

Welcome to the CCA host
host login: root
(host) #
```
Use kvmtool to launch guest Linux in a Realm:
```bash
cd /cca
./lkvm run --realm --disable-sve --irqchip=gicv3-its --firmware KVMTOOL_EFI.fd -c 1 -m 512 --no-pvtime --force-pci --disk guest-disk.img --measurement-algo=sha256 --restricted_mem 
```
You should see the realm boot. After boot up, you will be prompted to log in at the guest Linux prompt. Use root again as the username:

```output
Starting syslogd: OK
Starting klogd: OK
Running sysctl: OK
Starting network: udhcpc: started, v1.36.1
udhcpc: broadcasting discover
udhcpc: broadcasting select for 192.168.33.15, server 192.168.33.1
udhcpc: lease of 192.168.33.15 obtained from 192.168.33.1, lease time 14400
deleting routers
adding dns 172.20.51.254
OK

Welcome to the CCA realm
realm login: root
(realm) #
```

Now run the key broker client application in the realm. Use the endpoint address that the key broker server is listening on in the other terminal:
```bash
cd /cca 
./keybroker-app -v --endpoint http://172.17.0.2:8088 skywalker 
```
In the command above `skywalker` is the key name that is requested from the key broker server. After some time, you should see the following output:
```
INFO Requesting key named 'skywalker' from the keybroker server with URL http://172.17.0.2:8088/keys/v1/key/skywalker
INFO Challenge (64 bytes) = [0f, ea, c4, e2, 24, 4e, fa, dc, 1d, ea, ea, 3d, 60, eb, a6, 8f, f1, ed, 1a, 07, 35, cb, 5b, 1b, cf, 5b, 21, a4, bc, 14, 65, c2, 21, 3f, bf, 33, a0, b0, 7c, 78, 3a, a6, 32, c6, 34, be, ff, 45, 98, f4, 17, b1, 24, 71, 4f, 9c, 75, 58, 37, 3a, 28, ea, 97, 33]
INFO Submitting evidence to URL http://172.17.0.2:8088/keys/v1/evidence/3974368321
INFO Attestation failure :-( ! AttestationFailure: No attestation result was obtained. No known-good reference values.
```
You can see from the key broker client application output that the `skywalker` key is requested from the key broker server, which did send a challenge. The key broker client application uses the challenge to submit its evidence back to the key broker server, but it gets an attestation failure. This is because the server does not have any known good reference values.

Now look at the key broker server output on the terminal where the server is running. It will look like:

```output
INFO Known-good RIM values are missing. If you trust the client that submitted
evidence for challenge 1302147796, you should restart the keybroker-server with the following
command-line option to populate it with known-good RIM values:
--reference-values <(echo '{ "reference-values": [ "tiA66VOokO071FfsCHr7es02vUbtVH5FpLLqTzT7jps=" ] }')
INFO Evidence submitted for challenge 1302147796: no attestation result was obtained. No known-good reference values.
```
From the server output you will notice that it did create the challenge for the key broker application, but it complains that it has no known good reference values. It does however provide a way to provision the key broker server with known good values if the client is trusted. 
In a production environment, the known good reference value would be generated using a deployment specific process, but for demonstration purposes and simplification, you will use the value proposed by the key broker server.

Now go ahead and terminate the running instance of the key broker server(ctrl+C) and restart it with the known good reference value. Notice here that you need to copy the `--reference-values` argument directly from the previous error message reported by the key broker. When running this next command, ensure that you are using exactly that value, for example::

```bash
./keybroker-server -v --addr 172.17.0.2 --reference-values <(echo '{ "reference-values": [ "tiA66VOokO071FfsCHr7es02vUbtVH5FpLLqTzT7jps=" ] }')
```

On the terminal with the running realm, re-run the key broker client application with the exact same command line parameters as before:

```bash
./keybroker-app -v --endpoint http://172.17.0.2:8088 skywalker
```

You should now get a successful attestion as shown:

```output
INFO Requesting key named 'skywalker' from the keybroker server with URL http://172.17.0.2:8088/keys/v1/key/skywalker
INFO Challenge (64 bytes) = [05, 9e, ef, af, 59, e5, 2d, 0f, db, d8, 24, 40, 1e, 0d, 09, c9, d4, 3c, 9e, 99, c5, 64, cf, e6, b9, 20, 29, be, d7, ec, ea, 9a, a3, 91, dc, 16, e6, b7, 0f, 39, 0f, 06, b6, cc, b6, 9f, 0e, 3a, da, 26, 57, 5c, ed, 7f, 11, 1f, 2b, 3c, 9e, aa, 8c, d6, bc, b8]
INFO Submitting evidence to URL http://172.17.0.2:8088/keys/v1/evidence/2828132982
INFO Attestation success :-) ! The key returned from the keybroker is 'May the force be with you.'
```

You have successfully run an end-to-end attestation flow with Arm CCA.




