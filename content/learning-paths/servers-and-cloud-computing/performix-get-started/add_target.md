---
title: Add a new target

weight: 4

layout: learningpathall
---
## Prepare the target

Follow these steps to prepare your Arm-based server for performance analysis:

1. Ensure SSH key-based authentication is configured for your target machine.
1. Enable passwordless sudo access.

Follow the [installation guide](https://learn.arm.com/install-guides/performix) for detailed instructions.

## Add a new target in Arm Performix

When you launch Arm Performix, the first thing you'll see is the Welcome screen. From here you can quickly connect to a target system and run your first analysis.

![Arm Performix Welcome Screen #center](images/welcome.png "Arm Performix Welcome Screen")

1. Choose **Connect a Target** or select Targets in the activity bar to open the Targets view.
1. Select **Add Target**.
1. In the **Configure Target** form, provide the following details:
    1. **Host** the hostname or IP address of the target machine
    1. **Name** a descriptive name for the target
    1. **Port** the SSH port number (default is 22)
    1. **User** the username for SSH connection. This username must be a valid user on the target machine.
    1. **Authentication method** your private SSH key, stored locally (usually ~/.ssh/id_rsa or ~/.ssh/id_ed25519).
        1. Choose **Automatically Detect Key** to let Performix find your private key
        1. Choose **Select Key Manually** to provide the path to your private key (useful if you have more than one key stored).
        1. Choose **Username and password** to be prompted for a password on connection.
1. If you need to securely route your connection through intermediate hosts before reaching your target machine, click **Add Jump Node** to add one or more jump nodes. The order in which you specify jump nodes is important. Specify them in the order in which your connection should use them.
1. Select **Test Connection** to check if your target is reachable. If any required tools are missing, Performix will install them for you.
1. Select **Add Target**. The target appears in the list and is ready for profiling.

![Adding a target in Arm Performix #center](images/add_target.png "Adding a target in Arm Performix")
