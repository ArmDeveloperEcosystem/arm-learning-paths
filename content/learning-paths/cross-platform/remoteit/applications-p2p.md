---
layout: learningpathall
title: Install applications and create peer to peer connections
weight: 4
---

## Install remote.it applications

Remote.it provides four types of packages for [download](https://www.remote.it/download-list).

| Application type | Operating Systems | Devices supported |
| ----------- | ----------- |----------- |
| Desktop | Windows, macOS, and Linux | initiator and target |
| Mobile | Andoid, iOS | initiator and target |
| Device package | Linux | target only |
| CLI | Linux | initiator and target |

Any software package marked as initiator can connect to other target devices. The target software packages can receive connections from other devices. Packages marked as both initiator and target can do both functions. 

## Persistent connections

The remote.it web dashboard creates proxy connections between the initiator and target devices. Proxy connections are the easiest to setup because additional software is installed on the target device only. The initiator device connects to the target device without any additional software installed. It uses only standard software such as SSH. All traffic is routed through a remote.it server.

Peer to peer connections provide an alternative to proxy connections. Peer to peer connections are direct between initiator and target. 

The advantages are:
- Consistency in URL and port values (proxy connection information changes on reconnect)
- No timeouts when connections are idle (proxy connections timeout when idle and need to be reconnected)
- Higher performance by eliminating the proxy server

Peer to peer connections are created by installing a software package with initiator support on the initiator device.

Install a desktop application on your initiator device and create a peer to peer connection.

## Localhost connections

Peer to peer connections to the target computer appear as a local port on the initiator computer.

Start the SSH service from the Desktop application on the initiator computer. 

SSH is now available using `localhost` from the initiator computer with the assigned port. The port will not change, even if there are no connections for some time. 

Copy the port from the desktop application and connect to the target computer using SSH. Instead of the proxy server, use `localhost` and the port number.

For example:

```console
ssh ubuntu@localhost -p 33004 
```

You should now be connected to the target device. 

Peer to peer provides easy access using `localhost` and the best performance. Peer to peer connections require software to be installed on the initiator device. 

The next section explains how to use the remote.it CLI to create peer to peer connections and automate tasks using scripts. 

