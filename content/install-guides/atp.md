---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Arm Total Performance

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- performance
- profiling
- analysis
- neoverse
- optimization
- perf
- top-down

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 30

### Link to official documentation
official_docs: https://arm-total-performance.tools.arm.com/

author: Pareena Verma

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: false             # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles

build:
  list: false                   # Exclude from .Pages collections and listings
  render: true                  # Still render the page (accessible via direct URL)
---

Arm Total Performance (ATP) is a desktop application that provides performance
analysis and profiling for Arm-based Linux systems. ATP connects to remote Arm
Linux targets via SSH and provides a graphical interface for capturing and
analyzing performance data using hardware performance counters and the top-down
methodology.

ATP provides capabilities for:

* Performance profiling using hardware performance monitoring counters
* Top-down methodology analysis for identifying performance bottlenecks
* System-wide and per-process profiling
* Statistical Profiling Extension (SPE) support on compatible systems
* Command-line interface (CLI) included with the GUI installation
* SSH-based remote target connections with optional jump node support

ATP is available for Windows, macOS, and Linux host machines, and connects to
Arm Linux target systems running Amazon Linux 2023, Ubuntu 20.04, or Ubuntu
24.04.

## What should I do before installing Arm Total Performance?

ATP requires different packages depending on your host platform:

* **Windows**: Windows 10 or later (Arm64 or x64 architecture)
* **macOS**: macOS on Arm64 (Apple Silicon)
* **Linux**: Debian-based distribution on Arm64 or x64 architecture

You also need access to an Arm Linux target system for profiling.

## How do I download and install Arm Total Performance?

ATP is distributed as platform-specific installer packages. The installation includes both the GUI and the CLI tool (`atperf`).

### How do I install ATP on Windows?

Download the Windows installer package for your architecture from the [Arm Total Performance download page](https://arm-total-performance.tools.arm.com/).

Alternatively, download using PowerShell:

{{< tabpane code=true >}}
  {{< tab header="Arm64" >}}
curl -o ArmTotalPerformance-arm64.exe https://artifacts.tools.arm.com/arm-total-performance/installers/latest/windows/arm64/ArmTotalPerformance-arm64.exe
  {{< /tab >}}
  {{< tab header="x64" >}}
curl -o ArmTotalPerformance-x64.exe https://artifacts.tools.arm.com/arm-total-performance/installers/latest/windows/x64/ArmTotalPerformance-x64.exe
  {{< /tab >}}
{{< /tabpane >}}

After downloading the `.exe` file, locate it in your Downloads folder and double-click it to start the installation wizard.

Review the License Agreement and select **I Agree**.

Choose whether to install ATP for all users or just yourself, then select **Next**.

If you choose **Anyone who uses this computer (all users)**, a User Access Control dialog opens. Enter an administrator username and password, then select **Yes**.

Choose the installation directory. You can accept the default or select **Browse** to choose a different location.

Select **Install**.

When the installation finishes, select **Finish** to close the wizard.

### How do I install ATP on Linux?

Download the Linux installer package for your architecture from the [Arm Total Performance download page](https://arm-total-performance.tools.arm.com/).

Alternatively, download using `wget`:

{{< tabpane code=true >}}
  {{< tab header="Arm64" >}}
wget -P $HOME https://artifacts.tools.arm.com/arm-total-performance/installers/latest/linux/arm64/ArmTotalPerformance-arm64.deb
  {{< /tab >}}
  {{< tab header="x64" >}}
wget -P $HOME https://artifacts.tools.arm.com/arm-total-performance/installers/latest/linux/x64/ArmTotalPerformance-x64.deb
  {{< /tab >}}
{{< /tabpane >}}

After downloading the `.deb` file, navigate to the directory where you downloaded it:

```bash
cd $HOME
```

Update the package list and install any missing dependencies:

```bash
sudo apt update
sudo apt-get install -f
```

Install the package:

```bash
sudo dpkg -i ArmTotalPerformance-arm64.deb
```

Navigate to the ATP installation directory:

```bash
cd "/opt/Arm Total Performance/assets/atperf/"
```

Verify the installation by checking the version:

```bash
./atperf version
```

The output displays the installed version number.

```output
Arm Total Performance CLI version: 0.39.0
Daemon process started; to stop call `atperf daemon stop`.
Arm Total Performance daemon version: 0.39.0
```

### How do I install ATP on macOS?

Download the macOS installer package from the [Arm Total Performance download page](https://arm-total-performance.tools.arm.com/).

Alternatively, download using `wget`:

```bash
wget https://artifacts.tools.arm.com/arm-total-performance/installers/latest/darwin/arm64/ArmTotalPerformance-arm64.pkg
```

After downloading the `.pkg` file, navigate to the directory where you downloaded it and double-click the file to start the installer.

Review the license agreement and select **Agree**.

Choose the installation destination. By default, ATP installs on your system drive.

Select **Install** and enter your macOS administrator password when prompted.

Wait while the installer copies the files.

When the installation finishes, select **Close** to exit the installer.

## How do I prepare my target for ATP connections?

Before connecting to an Arm Linux target, ensure SSH key-based authentication is configured and that passwordless sudo access is enabled. If you already manage your target system via SSH, you likely have most of this setup complete.

### Check your existing SSH key

Verify that you can connect to your target using SSH:

```bash
ssh user@target_host
```

If the connection works, you have SSH key authentication configured. Now check if your existing key has a passphrase. Try to display the public key:

```bash
ssh-keygen -y -f ~/.ssh/id_ed25519
```

If you're prompted for a passphrase, your key is protected with one. ATP doesn't support SSH keys with passphrases, so you need to create a separate key without a passphrase for ATP.

### Create a passphrase-free key for ATP (if needed)

If your existing SSH key has a passphrase, generate a new key specifically for ATP:

```bash
ssh-keygen -t ed25519 -f ~/.ssh/atp_key
```

Press **Enter** when prompted for a passphrase to leave it empty.

Copy the new public key to your target. If your existing SSH key is at a non-default location (for example, `~/cloud-keys/my-instance.pem`), specify it when copying:

```bash
ssh-copy-id -i ~/.ssh/atp_key.pub -o "IdentityFile=~/cloud-keys/my-instance.pem" user@target_host
```

If your existing key is in the default location (`~/.ssh/id_ed25519` or `~/.ssh/id_rsa`), use:

```bash
ssh-copy-id -i ~/.ssh/atp_key.pub user@target_host
```

You can now use `~/.ssh/atp_key` as the private key when configuring ATP's target connection.

### Enable passwordless sudo on the target

ATP needs to run commands with elevated privileges on the target system. Because ATP cannot enter sudo passwords interactively, configure passwordless sudo access.

On the target system, edit the sudoers file:

```bash
sudo visudo
```

Add the following line, replacing `<username>` with your actual username:

```bash
<username> ALL=(ALL) NOPASSWD:ALL
```

Save and exit the editor.

## How do I connect ATP to a target?

After installing ATP and preparing your target, you can connect using either the GUI or the CLI.

### Connect using the ATP GUI

The GUI is typically used on Windows and macOS hosts, though it's also available on Linux.

Open the ATP application.

On the home page, select **Connect a target** or select **Targets** in the activity bar to open the Targets view.

Select **Add Target**.

In the **Configure Target** form, provide the following details:

* **Host**: The hostname or IP address of the target machine
* **Name**: A descriptive name for the target
* **Port**: The SSH port number (default is 22)
* **User**: The username for SSH connection
* **SSH Private Key**: Choose **Automatically Detect Key** or **Select Key Manually**
  * For manual selection, enter the path to your private key (usually `~/.ssh/id_rsa` or `~/.ssh/id_ed25519`)
* **Host Key Verification**: Choose **Strict** (recommended) or **Ignore**
  * Strict mode verifies the server identity using your `~/.ssh/known_hosts` file

![ATP target configuration example #center](_images/atp-target-config.png)

Select **Add Target**.

The target appears in the targets list and is ready for profiling.

You can select the **Test Connection** button to verify your connection to the ATP Linux target is successful.

![ATP connection test #center](_images/atp-connection-test.png)

#### Configure jump nodes (optional)

If your target is behind a bastion host or requires intermediate servers for access, add jump nodes in the GUI:

In the **Jump Node** section, select **Add Jump Node**.

Provide the jump node details:

* **Host**: The hostname or IP address of the jump node
* **Port**: The SSH port (default is 22)
* **User**: The username for the jump node
* **SSH Private Key**: The key file path (if using manual selection)

Select **Add** to save the jump node.

You can add multiple jump nodes. The order matters—your connection uses them in sequence. Use drag and drop to reorder jump nodes.

### Connect using the ATP CLI

The CLI is useful for Linux hosts or when you prefer command-line workflows.

The `atperf` command-line tool is installed automatically with the GUI. On Linux, you can find it at:

```bash
/opt/Arm\ Total\ Performance/assets/atperf/atperf
```

For convenience, add it to your PATH or create an alias:

```bash
export PATH="/opt/Arm Total Performance/assets/atperf:$PATH"
```

Use the CLI help for command-line usage:

```bash
atperf --help
```

#### Profile the local machine

If your target is the same machine where you installed ATP (the host machine itself), ATP automatically provides a built-in `localhost` target. You don't need to configure authentication, SSH keys, or host verification for local profiling.

Verify the localhost target is available:

```bash
atperf target list
```

The output is similar to:

```output
name      default  host_key_policy  value
localhost yes      localhost
1 registered target found
```

Your local machine is now ready to use as a target. Specify `--target=localhost` when running ATP commands.

#### Add a remote target

To profile a workload on a remote machine, add it as a target using the standard syntax:

```bash
atperf target add <user>@<host>:<port>:<private_ssh_key_path>
```

Where:
* `user`: (Optional) SSH username. If not specified, uses your current system username
* `host`: (Required) Target hostname or IP address
* `port`: (Optional) SSH port. Default is 22
* `private_ssh_key_path`: (Optional) Path to your private SSH key

For example, to connect to a target at `192.168.1.10` using the `ubuntu` username:

```bash
atperf target add ubuntu@192.168.1.10
```

You can also use JSON format to specify the target:

```bash
atperf target add '{
  "host": "192.168.1.10",
  "port": 22,
  "username": "ubuntu",
  "privateKeyFilename": "~/.ssh/atp_key",
  "hostKeyPolicy": "accept-new"
}'
```

**Authentication options:**

Choose one of the following methods to authenticate with your target:

* **Use an existing SSH key in a non-default location:**
  
  If your private key is not in `~/.ssh/id_rsa` or `~/.ssh/id_ed25519`, specify its path in the target command:
  ```bash
  atperf target add user@host:22:/path/to/private_ssh_key
  ```

* **Automatically detect an existing SSH key:**
  
  ATP searches common locations (`~/.ssh/id_rsa`, `~/.ssh/id_ed25519`, etc.) for a usable key:
  ```bash
  atperf target add user@host --find-keys
  ```

* **Generate and configure a new SSH key pair using password authentication:**
  
  If your target supports password-based SSH login, ATP can generate a new key pair and configure it automatically:
  ```bash
  atperf target add user@host --password
  ```
  This option:
  - Generates an RSA 4096-bit key pair on your host (without a passphrase)
  - Authenticates to the target using the password you provide
  - Adds the public key to the target's `~/.ssh/authorized_keys` file
  - Records the target's host key in ATP's known hosts
  - Stores the private key securely for future ATP connections
  - Discards the password immediately after use (not stored)

**Host key verification:**

Specify host key verification with the `--host-key-policy` flag:

* `strict`: (Default) Fail if the host key is unknown or changed
* `ignore`: Disable host key verification
* `accept-new`: Accept unknown keys, but warn if they change later

```bash
atperf target add user@host --host-key-policy accept-new
```

**Naming and default targets:**

Give your target a friendly name using `--name`:

```bash
atperf target add ubuntu@192.168.1.10 --name my-target
```

Make a target the default for future commands with `--default`:

```bash
atperf target add ubuntu@192.168.1.10 --name my-target --default
```

After you run this command, `build-server` becomes the default target for future commands.

**Using jump nodes:**

If your target requires jump nodes (bastion hosts), use the `--jump` flag. Specify jump nodes in connection order:

```bash
atperf target add user@final-host --jump user@jumphost1 --jump admin@jumphost2
```

This connects through `jumphost1`, then `jumphost2`, then `final-host`.

**Verify and manage targets:**

Test the connection to a target:

```bash
atperf target test my-target
```

List all configured targets:

```bash
atperf target list
```

Remove a target:

```bash
atperf target remove my-target
```

## How do I uninstall Arm Total Performance?

To remove ATP from your system, use the appropriate method for your platform:

**Windows**: Open **Settings** > **Apps**, find **Arm Total Performance**, and select **Uninstall**.

**macOS**: Drag the Arm Total Performance application from **Applications** to the **Trash**.

**Linux**: Remove the package:

```bash
sudo apt remove arm-total-performance
```
