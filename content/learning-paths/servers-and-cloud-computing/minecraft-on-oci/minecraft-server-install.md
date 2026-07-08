---
title: Install the Minecraft server
description: Install the Java Runtime Environment, download the Minecraft server files, and launch the server application.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Installing the Minecraft server

### Installing the Java Runtime Environment

Before you install the Minecraft server, you need to install the required software. For the Minecraft 26 server or earlier, you will need Java 25.

Connect to your instance using SSH as described in the previous step. You can install Java 25 on Oracle Linux 9 with:

```console
sudo dnf install java-25-openjdk.aarch64 -y
```

### Keeping the server running after disconnecting

The Minecraft server runs in the foreground of your terminal session. If you close your SSH
connection, the server process will stop. To keep the server running after you disconnect, use
`tmux` to create a persistent terminal session.

While still connected to your instance via SSH, install `tmux` on Oracle Linux 9:

```console
sudo dnf install tmux -y
```

Start a new `tmux` session named "minecraft":

```console
tmux new -s minecraft
```

You are now inside a `tmux` session. Any commands you run here will continue running even after you
disconnect from SSH. You will start the Minecraft server inside this session in the next section.

When you need to disconnect, press `Ctrl+B` then `D` to detach from the session. The server
continues running in the background.

To reattach to the session later (for example, after reconnecting via SSH):

```console
tmux attach -t minecraft
```

### Downloading and installing the Minecraft server

You can find the link for the latest version of the Minecraft server
[on the Minecraft website](https://www.minecraft.net/en-us/download/server). 

On that page, right-click the `minecraft_server.x.x.x.jar` link and copy the URL. Then run the following command on your OCI instance to download it:

```console
wget <paste URL to server.jar here>
```

This will download `server.jar` from the Mojang website, and you will have a `server.jar` file on your OCI instance. To make it easier to keep track of different server versions, rename the `server.jar` file to a more meaningful name:

```console
mv server.jar minecraft_server.26.2.jar
```

To start the Minecraft server, run the command:

```console
java -Xmx8G -Xms8G -jar minecraft_server.26.2.jar nogui
```

This runs the server without a graphical user interface, and allocates 8GB of memory to it.

The first time you do this, the start-up will fail and a file called `eula.txt` is created in the local folder. 

Before you start the server, you first need to accept its terms of use. 

Open `eula.txt` and change `eula=false` to `eula=true`, or run:

```console
sed -i 's/eula=false/eula=true/' eula.txt
```

Running the server again after doing this will succeed, and you should see the following messages on the terminal, showing that the process has completed successfully (timestamps will be different at the start of the lines):

```output
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