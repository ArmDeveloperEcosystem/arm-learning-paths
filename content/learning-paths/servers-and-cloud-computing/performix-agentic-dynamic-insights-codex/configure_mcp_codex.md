---
title: Configure the Arm Performix MCP server in Codex

weight: 3

description: Add the local Arm Performix MCP server to Codex and verify that the extension can access Performix tools and profiling runs.

layout: learningpathall
---
## Choose a configuration method

Codex CLI and the Codex extension share MCP configuration on the same host. Choose one of the following methods:

- Use the Codex extension settings.
- Run `codex mcp add` in a terminal.
- Edit `~/.codex/config.toml`.

You need to complete only one method. The MCP server is a local standard input and output (STDIO) process started by the `apx` executable.

{{% notice Note %}}
Configure the server on the host where Codex runs. In a local Visual Studio Code (VS Code) session, this is your development computer. In a remote development session, confirm which host runs the Codex extension and which Arm Performix data directory it uses.
{{% /notice %}}

## Configure the server in the Codex extension

To add the server in VS Code:

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

## Configure the server in the Codex config file

For direct configuration, open `~/.codex/config.toml` and add the following:

```toml
[mcp_servers.arm-performix]
command = "/Applications/Arm Performix.app/Contents/assets/apx/apx"
args = ["mcp", "start"]
```

Replace `command` with the full path to `apx` on your host. Save the file and restart the Codex extension.

{{% notice Note %}}
On Windows, use a TOML literal string so backslashes in the path aren't treated as escape characters:

```toml
[mcp_servers.arm-performix]
command = 'C:\Program Files\Arm Performix\assets\apx\apx.exe'
args = ["mcp", "start"]
```
{{% /notice %}}

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

## Troubleshoot the MCP connection

Use the following checks to troubleshoot issues with MCP connection: 

### The Arm Performix MCP server isn't listed

Check whether Codex loaded the server configuration:

```bash
codex mcp list
```

Find `arm-performix` in the output. Then confirm:

- The command is the full path to the `apx` executable, including `apx.exe` on Windows.
- The arguments are `mcp` and `start`.
- The server is enabled.
- You restarted the extension after changing the configuration.
- You edited the configuration for the same user account and Codex host that runs the extension.

### The MCP server fails to start

Run the executable's built-in help from a terminal to separate an `apx` problem from a Codex configuration problem. Replace `<path-to-apx>` with the configured path:

```bash
"<path-to-apx>" mcp --help
```

If the help text doesn't appear, check the executable path, file permissions, and installed Arm Performix version. If it does appear, reopen **MCP servers** in the Codex extension and check the server status.

In a remote development session, make sure `apx` is installed on the Codex host and that this installation uses the expected Performix configuration and run data.

### Codex doesn't use Arm Performix

Name the server and task explicitly:

```text
Use the Arm Performix MCP server to list the available Arm Performix runs.
```

For a specific run:

```text
Use Arm Performix to generate an AI Insight for run ID "<run-id>".
```

If you have several MCP servers, an ambiguous prompt such as `give me insights` might not select Arm Performix.

### Code Hotspots runs are missing

Check:

- You created at least one completed Code Hotspots run.
- The MCP server runs as the same user who created or imported the run.
- The GUI, CLI, and MCP server use the same Arm Performix data location.
- The selected run contains enough samples and profile data for analysis.
- A remote Visual Studio Code environment isn't using a different home directory or Performix configuration.

Compare the MCP result with the CLI:

```bash
apx run list
```

If the CLI also returns no run, create or import a run. If the CLI returns the run but Codex doesn't, recheck which host, user, and configuration start the MCP server.

## What you've accomplished and what's next

You've now configured and tested the MCP connection.

Next, you'll create a Code Hotspots run if no supported run is available. If you have an available supported run, skip to [Generate Arm Performix AI insights for a Code Hotspots run](/learning-paths/servers-and-cloud-computing/performix-agentic-dynamic-insights-codex/generate_ai_insights/).
