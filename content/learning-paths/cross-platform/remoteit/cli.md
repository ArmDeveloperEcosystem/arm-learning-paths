---
layout: learningpathall
title: Remote.It CLI
weight: 4
---

## Install CLI

You can use the Remote.It CLI application to create connections without the Desktop software installation. This is useful when the initiator computer doesn’t have a desktop or automated scripting is needed. Visit the [download page](https://link.remote.it/download/cli) and install a CLI binary for the initiator device you are using. If you installed the Desktop software the CLI binary is already included.

The CLI downloads are single binary applications and ready to run.

You can change the name of them and make sure they have execute permission on Linux. Full instructions for other operating systems can be found on the download page.

Example
please use the most current url from the [download page](https://link.remote.it/download/cli):

```console
wget https://downloads.remote.it/cli/v3.0.14/remoteit.aarch64-linux
mv remoteit.aarch64-linux remoteit
chmod +x remoteit
sudo cp remoteit /usr/local/bin
```

## Create a connection using the CLI

A username and password can be used for the CLI but access keys are preferred. The username and password option will not work if you used Google to sign in or add 2FA authentication to your account.

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

This requires the service ID and local port. Verify there are not other connections on the local port before generating. The service ID of the target can be found on the service page of the targe device in the Remote.It Web Portal or via API.
Optional arguments are --p2p boolean (default true) and --failover boolean (default true). --failover will attempt p2p connection first and then failover to proxy. If --failover is false, then only p2p connections will be attempted.

```console
sudo remoteit connection add --id <service id> --port <port> --p2p true
```

For example, a command to connect is shown here. Substitute the ID for your target device's service. The port will need to be a port that is not in use on this device itself or used by another connection. For example if this device has SSH running on port 22, you cannot use 22 for the connection. It is recommended to use ports in the range of 33000-35000 which are typically not in use.

```console
sudo remoteit connection add --id 80:00:00:00:01:25:EF:4E --port 34000 --p2p true
```

You can view the connection information by running the status command

```console
sudo remoteit status
```

## Additional CLI Usage

The CLI provides commands such as to register this device as a target for connections.

You can get help within the CLI by using the help command. You can also append the --help flag to any CLI commands to get more details on flags.

```console
sudo remoteit --help
```

Example help command for adding a connection

```console
sudo remoteit connection add --help
```

See also [Documentation for CLI](https://link.remote.it/docs/cli-usage)
