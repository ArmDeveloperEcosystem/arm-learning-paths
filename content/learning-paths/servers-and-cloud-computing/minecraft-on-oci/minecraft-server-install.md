---
title: Install the Minecraft server on an Arm-based virtual machine
description: Install the Java Runtime Environment, download the Minecraft server files, and launch the server application.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install the Java Runtime Environment

Before you install the Minecraft server, install necessary dependencies. For Minecraft 26 or earlier, you'll need to install Java 25.

After connecting to your VM instance over SSH, install Java 25:

```console
sudo dnf install java-25-openjdk.aarch64 -y
```

## Create a persistent terminal session for the server

The Minecraft server runs in the foreground of your terminal session. If you close your SSH
connection, the server process will stop. To keep the server running after you disconnect, use
`tmux` to create a persistent terminal session.

Install `tmux` on the VM instance:

```console
sudo dnf install tmux -y
```

Start a new `tmux` session named `minecraft`:

```console
tmux new -s minecraft
```

You're now inside a `tmux` session. Any commands you run here will continue running even after you
disconnect from SSH. You'll start the Minecraft server inside this session.

When you need to disconnect, press `Ctrl+B` then `D` to detach from the session. The server
continues running in the background.

To reattach to the session later (for example, after reconnecting to the instance via SSH), run:

```console
tmux attach -t minecraft
```

## Download and install the Minecraft server

For the latest version of the Minecraft server, see
[the Minecraft website](https://www.minecraft.net/en-us/download/server). 

Copy the `minecraft_server.x.x.x.jar` URL from that page. Then, run the following command on the instance to download `server.jar` from the Mojang website:

```bash
wget <paste URL to server.jar here>
```

You'll have a `server.jar` file on your OCI instance. To make it easier to keep track of different server versions, rename the `server.jar` file to something more meaningful as follows:

```bash
mv server.jar minecraft_server.26.2.jar
```

## Start the Minecraft server

To start the Minecraft server, run the command:

```bash
java -Xmx8G -Xms8G -jar minecraft_server.26.2.jar nogui
```

This runs the server without a graphical user interface, and allocates 8GB of memory to it.

The first time you do this, the start-up will fail and a file called `eula.txt` is created in the local folder. 

Before starting the server again, accept its terms of use. 

Open `eula.txt` and change `eula=false` to `eula=true`, or run:

```console
sed -i 's/eula=false/eula=true/' eula.txt
```

After accepting terms of use, you'll be able to run the server successfully with the same command as earlier.

The output shows that the process has completed successfully, and is similar to:

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

### What you've accomplished and what's next

You've now installed the open-source Java Runtime Environment on your instance, downloaded the Minecraft server files, accepted the End User License Agreement, and started the game server.

Next, you'll connect a Minecraft client to the server.