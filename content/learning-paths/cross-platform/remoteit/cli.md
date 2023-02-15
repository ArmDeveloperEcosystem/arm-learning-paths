---
layout: learningpathall
title: Automate connections with the CLI
weight: 5
---

## Install CLI 

You can use the remote.it CLI application to create peer to peer connections without the desktop software installation. This is useful when the initiator computer doesn’t have a desktop or automated scripting is needed. Visit the [download page](https://www.remote.it/download-list) and install a CLI binary for the initiator device you are using. If you installed the Desktop software the CLI binary is already included. 

The CLI downloads are single binary applications and ready to run. 

You can change the name of them and make sure they have execute permission on Linux. 

```console
wget https://downloads.remote.it/cli/v3.0.14/remoteit.aarch64-linux
mv remoteit.aarch64-linux remoteit
chmod +x remoteit
sudo cp remoteit /usr/local/bin
```

## Create a peer to peer connection using the CLI

A username and password can be used for the CLI but access keys are preferred. The username and password option will not work if you used Google to sign in. 

Create an [access keys](https://app.remote.it/#/account/accessKey) from your account.

Copy the access key and secret access key. Protect the secret access key. 

Manually create the file `~/.remoteit/credentials` with the 3 lines below. Enter your `access-key` and `secret-access-key`. 

```console
[default]
R3_ACCESS_KEY_ID=access-key
R3_SECRET_ACCESS_KEY=secret-access-key
```

You can also run the configure command enter the access key and secret access key and the credentials file will be created. 

Enter a profile name when prompted, such as `default`

```bash
remoteit configure
```


To connect to a target device you will need the connection ID. 

```console
sudo remoteit connection add --id <service id> --port <port> --p2p true
```

For example, a command to connect is shown here. Substitute the ID and port number for your target device. 

```console
sudo remoteit connection add --id 80:00:00:00:01:25:EF:4E --port 34000 --p2p true
```

More information to be added about using the CLI.


