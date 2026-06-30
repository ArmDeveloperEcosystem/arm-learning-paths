---
title: Installing the Minecraft server
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Installing the Minecraft server

### Installing the Java Runtime Environment

Before we install the Minecraft server, we need to make sure that there are some prerequisites
installed. For the Minecraft 26 server or earlier, we will need Java 25.

Connect to your instance using SSH as described in the previous step. We can install Java 25 on
Oracle Linux with:
```
sudo dnf install java-25-openjdk
```
and on Ubuntu or similar distributions, with
```
sudo apt install openjdk-25-jre
```
Since the Minecraft server starts on the command line, you may also want to install the `screen` or
`tmux` utilities which allows commands to keep running after you disconnect from the server.
These commands are not strictly necessary, but you will need them to be running if you want to keep
the server running when you disconnect from your SSH session. 

Running the Minecraft server at start-up, or keeping it running when you are not connected, will
not be covered in this learning path.

### Downloading and installing the Minecraft server

You can find the link for the latest version of the Minecraft server
[on the Minecraft website](https://www.minecraft.net/en-us/download/server). Copy the link to
`server.jar` from this page, and run the following command on your OCI instance to download it:
```
wget <paste URL to server.jar here>
```

This will download server.jar from the Mojang website, and we will have a server.jar file on our OCI
instance. To make it easier to keep track of different server versions, rename the server.jar file
with a more meaningful name: `mv server.jar minecraft_server.26.2.jar`

To start the Minecraft server, run the command:
```
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

Your Minecraft server is now running - you can connect to it with the Minecraft client. Congratulations!


