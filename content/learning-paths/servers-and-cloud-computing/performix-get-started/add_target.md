---
title: Set up Arm Performix

weight: 2

layout: learningpathall
---

Arm Performix is a performance analysis toolkit that uses guided recipes to turn hardware performance counter data into actionable insights on Arm-based systems. Unlike command-line tools such as Perf, Performix attributes metrics directly to functions, applies Arm's standardized performance methodologies, and presents results with context and suggested next steps. You don't need to be a performance expert to get useful results.

Performix runs on your local machine (Windows, macOS, or Linux) and connects over SSH to a remote Arm Linux server, referred to as the *target*, where it collects performance data.

## Before you begin

Follow the [Arm Performix install guide](/install-guides/performix/) to download and install Performix on your local machine. The toolkit is available for Windows, macOS, and Linux on Arm64 or x64 architecture.

## Prepare the target

Complete these steps on your Arm Linux server before connecting with Performix.

### Configure SSH key-based authentication

Performix connects to your target over SSH. If you don't already have an SSH key pair, generate one on your local machine:

```bash
ssh-keygen -t ed25519
```

Press Enter to accept the defaults. Then copy the public key to your Arm server:

```bash
ssh-copy-id username@your-server
```

Replace `username` with your user on the server and `your-server` with the hostname or IP address.

Verify you can connect without a password prompt:

```bash
ssh username@your-server
```

For more details, see the [SSH install guide](/install-guides/ssh/).

### Enable passwordless sudo

Performix installs profiling tools on the target and requires root privileges. Configure passwordless sudo for your user to avoid interactive prompts during analysis.

On the target, create a sudoers drop-in file for your user, replacing `username` with your actual username:

```bash
echo "username ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/username
sudo chmod 440 /etc/sudoers.d/username
```

Verify it works by running:

```bash
sudo whoami
```

The expected output is:

```output
root
```

## Add a new target in Arm Performix

When you launch Arm Performix, the Welcome screen appears. From here you can connect to a target and run your first analysis.

![Arm Performix Welcome screen showing the Connect a Target button and activity bar#center](images/welcome.png "Performix Welcome screen")

1. Select **Connect a Target** or select **Targets** in the activity bar to open the Targets view.
1. Select **Add Target**.
1. Fill in the **Configure Target** form with the following details:

   - **Host:** the hostname or IP address of the target machine
   - **Name:** a descriptive name for the target
   - **Port:** the SSH port number (default is 22)
   - **User:** the username for SSH connection, which must be a valid user on the target machine
   - **Authentication method:** your private SSH key, stored locally (usually `~/.ssh/id_rsa` or `~/.ssh/id_ed25519`)

   For authentication, you can select **Automatically Detect Key** to let Performix find your private key, **Select Key Manually** to provide the path to a specific key, or **Username and password** to be prompted for a password on connection.

1. If you need to route your connection through intermediate hosts, select **Add Jump Node** to add one or more jump nodes. Specify them in the order your connection should use them.
1. Select **Test Connection** to verify your target is reachable. If any required tools are missing, Performix installs them for you.
1. Select **Add Target**. The target appears in the list and is ready for profiling.

![Configure Target form with Host, Name, Port, User, and Authentication fields filled in#center](images/add_target.png "Adding a target in Performix")

You should see your target listed in the Targets view with a connected status, confirming Performix can reach your server.

With your target connected, you can now build an example application to profile.
