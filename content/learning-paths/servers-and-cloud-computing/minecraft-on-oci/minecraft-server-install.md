---
title: Install the Minecraft server
description: Install the Java Runtime Environment, download the Minecraft server files, and launch the server application.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Installing the Minecraft server

### Installing the Java Runtime Environment

Before you install the Minecraft server, you need to make sure that there are some prerequisites
installed. For the Minecraft 26 server or earlier, you will need Java 25.

Connect to your instance using SSH as described in the previous step. You can install Java 25 on
Oracle Linux with:

```console
sudo dnf install java-25-openjdk -y
```

and on Ubuntu or similar distributions, with

```console
sudo apt install openjdk-25-jre -y
```

Since the Minecraft server starts on the command line, you might also want to install the `screen` or
`tmux` utilities which allows commands to keep running after you disconnect from the server.
These commands are not strictly necessary, but you will need them to be running if you want to keep
the server running when you disconnect from your SSH session. 

Running the Minecraft server at start-up, or keeping it running when you are not connected, will
not be covered in this learning path.

### Downloading and installing the Minecraft server

You can find the link for the latest version of the Minecraft server
[on the Minecraft website](https://www.minecraft.net/en-us/download/server). Copy the link to
`server.jar` from this page, and run the following command on your OCI instance to download it:

```console
wget <paste URL to server.jar here>
```

This will download `server.jar` from the Mojang website, and you will have a `server.jar` file on your OCI
instance. To make it easier to keep track of different server versions, rename the `server.jar` file
with a more meaningful name: 

```console
mv server.jar minecraft_server.26.2.jar
```

To start the Minecraft server, run the command:

```console
java -Xmx8G -Xms8G -jar minecraft_server.26.2.jar nogui
```

This runs the server withough a graphical user interface, and allocates 8GB of memory to it. If you
allocated less than this amount of memory to your instance, set this number to 3/4 of the memory that
you allocated to the instance - the other operating system services need some memory too.

The first time you do this, the start-up will fail expectedly - a file called `eula.txt` is created
in the local folder, and before you start the server, you first need to accept its terms of use. Open
this file and follow the instructions to accept the terms and conditions. Running the server again
after doing this will succeed, and you should see the following messages on the terminal, showing
that the process has completed successfully (timestamps will be different at the start of the lines):

```
[00:40:50] [Server thread/INFO]: Starting minecraft server version 26.2
[00:40:50] [Server thread/INFO]: Loading properties
[00:40:50] [Server thread/INFO]: Default game type: SURVIVAL
[00:40:50] [Server thread/INFO]: Generating keypair
[00:40:51] [Server thread/INFO]: Starting Minecraft server on *:25565
[00:40:51] [Server thread/INFO]: Preparing level "world"
[00:40:51] [Server thread/INFO]: Selecting global world spawn...
[00:41:04] [Server thread/INFO]: Loading 0 persistent chunks...
[00:41:04] [Server thread/INFO]: Preparing spawn area: 100%
[00:41:04] [Server thread/INFO]: Time elapsed: 13099 ms
[00:41:04] [Server thread/INFO]: Done (13.448s)! For help, type "help"
[00:41:04] [Server thread/INFO]: Saving chunks for level 'ServerLevel[world]'/minecraft:overworld
[00:41:04] [Server thread/INFO]: Saving chunks for level 'ServerLevel[world]'/minecraft:the_nether
[00:41:04] [Server thread/INFO]: Saving chunks for level 'ServerLevel[world]'/minecraft:the_end
[00:41:04] [Server thread/INFO]: ThreadedAnvilChunkStorage (world): All chunks are saved
[00:41:04] [Server thread/INFO]: ThreadedAnvilChunkStorage (DIM-1): All chunks are saved
[00:41:04] [Server thread/INFO]: ThreadedAnvilChunkStorage (DIM1): All chunks are saved
[00:41:04] [Server thread/INFO]: ThreadedAnvilChunkStorage: All dimensions are saved
```

### What you've accomplished

You installed the open-source Java Runtime Environment on your instance, downloaded the Minecraft server files, accepted the End User License Agreement, and started the game server.

### Next step

With the server successfully running in the cloud, you will now open the necessary network ports to allow the Minecraft client to connect to your instance.


