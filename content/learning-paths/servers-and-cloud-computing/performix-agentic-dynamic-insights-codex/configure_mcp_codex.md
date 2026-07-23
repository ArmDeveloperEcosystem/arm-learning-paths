---
title: Configure the Arm Performix MCP server in Codex

weight: 3

description: Add the local Arm Performix MCP server to Codex and verify that the extension can access Performix tools and profiling runs.

layout: learningpathall
---
## Choose a configuration method

Codex CLI and the Codex extension share MCP configuration on the same host. Choose one of these methods:

- Use the Codex extension settings.
- Run `codex mcp add` in a terminal.
- Edit `~/.codex/config.toml`.

You only need to complete one method. The MCP server is a local standard input/output (STDIO) process started by the `apx` executable.

{{% notice Note %}}
Configure the server on the host where Codex runs. In a local VS Code session, this is your development computer. In a remote development session, confirm which host runs the Codex extension and which Arm Performix data directory it uses.
{{% /notice %}}

## Configure the server in the Codex extension

To add the server in Visual Studio Code:

1. Open the Codex sidebar and select the gear icon.
2. Select **MCP servers**, then select **Add server**.
3. Enter `arm-performix` for the server name.
4. Select **STDIO** as the transport.
5. Enter the full path to the Arm Performix `apx` executable in the command field.

    On macOS:

    ```text
    /Applications/Arm Performix.app/Contents/assets/apx/apx
    ```

    On Linux:

    ```text
    /opt/Arm Performix/assets/apx/apx
    ```

    On Windows with an all-users installation:

    ```text
    C:\Program Files\Arm Performix\assets\apx\apx.exe
    ```

    On Windows with a single-user installation:

    ```text
    C:\Users\<username>\AppData\Local\Programs\Arm Performix\assets\apx\apx.exe
    ```

6. Add one argument:

    ```text
    mcp
    start
    ```

7. Select **Save**, then select **Restart extension**.

## Configure the MCP server with Codex CLI

If the `codex` command is available in your terminal, add the same STDIO server from the command line. Replace `<path-to-apx>` with the full executable path for your host:

```bash
codex mcp add arm-performix -- "<path-to-apx>" mcp start
```

For example, on macOS:

```bash
codex mcp add arm-performix -- "/Applications/Arm Performix.app/Contents/assets/apx/apx" mcp start
```

Restart the Codex extension after the command completes.

## Configure the server in `config.toml`

For direct configuration, open `~/.codex/config.toml` and add:

```toml
[mcp_servers.arm-performix]
command = "/Applications/Arm Performix.app/Contents/assets/apx/apx"
args = ["mcp", "start"]
```

Replace `command` with the full path to `apx` on your host. Save the file and restart the Codex extension.

On Windows, use a TOML literal string so backslashes in the path aren't treated as escape characters:

```toml
[mcp_servers.arm-performix]
command = 'C:\Program Files\Arm Performix\assets\apx\apx.exe'
args = ["mcp", "start"]
```

## Check that the MCP server is connected

If the `codex` command is available, confirm that Codex loaded the configuration:

```bash
codex mcp list
```

Find `arm-performix` in the server list and check that its command and `mcp` argument are correct. If you don't use Codex CLI, open **MCP servers** from the Codex gear menu to review the same status.

Configuration alone doesn't prove that the tools can read Performix data. In a new Codex chat, enter:

```text
Use the Arm Performix MCP server to list the available recipes and profiling runs. For each run, include its run ID, recipe, target, workload, and creation time when those fields are available.
```

If Codex returns Performix recipes or runs, the end-to-end connection works. An empty run list isn't a connection failure if recipes or targets are returned.

Next, ask Codex to identify runs that support the insight workflow:

```text
List the Arm Performix Code Hotspots runs that can be used to generate an AI Insight. Include the run ID and enough workload and target details for me to choose the correct run.
```

Record the run ID you want to analyze. A run name can be changed and might not be unique, so use the run ID in later prompts.

You have now configured and tested the MCP connection. If no supported run is available, create a Code Hotspots run in the next section.
