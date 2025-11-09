---
# User change
title: "Configure the model"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Set up a debug configuration for the Zena CSS FVP

Now you'll walk through setting up an Arm Development Studio debug configuration for the Zena CSS FVP using the Iris interface. This is a fast, reliable path to a working configuration.

As of Arm Development Studio 2025.0, there is no out-of-the-box configuration for the Zena CSS FVP. Creating one, however, is straightforward.

For full guidance, see the Arm Development Studio [Getting Started Guide](https://developer.arm.com/documentation/101469/latest/Migrating-from-DS-5-to-Arm-Development-Studio/Connect-to-new-or-custom-models). A concise, task-focused version is below.

## Launch the FVP (with Iris)

Launch the FVP with the Iris server enabled:

```bash
kas shell -c "../layers/meta-arm/scripts/runfvp -t tmux --verbose -- --iris-server --iris-port 7100"
```
If connecting to the FVP remotely, you can use this command:

```bash
kas shell -c "../layers/meta-arm/scripts/runfvp -t tmux --verbose -- --iris-server --iris-port 7100 -A"
```

{{% notice Note %}}
This example modeled below uses a local connection for the remaining steps.
{{% /notice %}}

## Create a configuration database in Arm Development Studio

Debug configurations are stored in a configuration database. Create a local database to store your model configuration:

- In Arm Development Studio, go to **File > New > Other**.
- Select **Configuration Database > Configuration Database**.
- Click **Next**, enter a **Name**, then click **Finish**.

## Create a model configuration for Zena CSS FVP (Iris)

- Open the same wizard (**File > New > Other**), then choose **Configuration Database > Model Configuration**.
- Click **Next**, select the **Configuration Database** you created, then click **Next**.
- For **Model Interface**, choose **Iris**, then click **Next**.
- Choose **Browse for model running on local host**. Select your FVP and click **Finish**. The debugger detects and interrogates the FVP.  
- If connecting remotely, choose **Connect to model running on either local or remote host** and provide the host and port.

{{% notice Tip %}}
The name of the FVP may be displayed as `RD_ASD` or other.

If unsure, use the port number to identify the correct FVP.
{{% /notice %}}

Arm Development Studio generates a `model.mdf` file that enumerates all CPUs in the FVP.

Optionally, update **Manufacturer Name** (for example, `Arm`) and **Platform Name** (for example, `Zena_CSS_FVP`).

**Save** and **Import** the model into the configuration database.

{{% notice Tip %}}
If the FVP is not detected, verify the Iris server is running on the expected port (`7100` by default) and that your firewall allows local connections.

For remote connections, confirm the host is reachable and the port is open.
{{% /notice %}}

A `model.mdf` file will be created that identifies all CPUs within the FVP.

The debugger is now aware of the FVP and you are ready to debug.
