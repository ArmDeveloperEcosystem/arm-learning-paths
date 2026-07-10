---
title: Configure the Arm Performix MCP server in Codex

weight: 3

layout: learningpathall
---
There are 3 ways to configure the MCP server:

- Through VS Code's GUI
- Through the Codex CLI
- By editing the Codex configuration file: `~/.codex/config.toml`.

## Configure the MCP server through VS Code

Use the following procedure in Visual Studio Code:

1. Open Visual Studio Code and open the Codex sidebar.
2. Open Codex settings.
3. In the Codex Settings tab, select MCP servers.
4. Click + Add server.
5. In the Name field, enter a name such as arm-performix.
6. In the Command to launch field, enter the path to the Arm Performix `apx` executable.
    Default paths include:

    ```
    /Applications/Arm Performix.app/Contents/assets/apx/apx

    /opt/Arm Performix/assets/apx/apx
    ```

    On Windows, the default installation directory depends on whether Arm Performix was installed for one user or all users:

    ```
    C:\Users\<username>\AppData\Local\Programs\Arm Performix 

    C:\Program Files\Arm Performix
    ```

7. In the Arguments field, add:

    ```
    mcp
    start
    ```

8. Click **Save** and restart the Codex extension.

## Configure the MCP server using Codex CLI

Alternatively, you can use Codex's CLI to add an MCP server. Replace `<path-to-apx>` with the path to the `apx` executable on your system. If the path contains spaces, put the path in double quotation marks.

```
codex mcp add arm-performix -- "<path-to-apx>" mcp start
```

For example, on macOS:

```
codex mcp add arm-performix -- "/Applications/Arm Performix.app/Contents/assets/apx/apx" mcp start
```

## Configure the MCP server in the Codex configuration file

You can also configure the MCP server by editing the Codex configuration file directly.

1. Open this file in a text editor: `~/.codex/config.toml`

2. Add a server entry:

    ```
    [mcp_servers.arm-performix]

    command = "/Applications/Arm Performix.app/Contents/assets/apx/apx"

    args = ["mcp", "start"]
    ```

3. Replace the command value with the path to the apx executable on your system.
4. Save the file and restart the Codex extension.

## Check that the MCP server is connected

Before generating insights, ask Codex to confirm that it can see Arm Performix data:

```
List the available Arm Performix recipes and profiling runs. If no code hotspots runs are available, tell me that the MCP server is connected but there are no supported runs to analyze.
```

If the assistant lists Arm Performix recipes or runs, the MCP server is connected.

To narrow the result, include a workload name, recipe, or time period:

```
Show me a list of Arm Performix runs for which AI insights are available.
```

Review the returned runs and identify the run you want to analyze. Note the run name or run ID.

If no supported Code Hotspots runs are available, you can create one from VS Code by asking the assistant to use the Arm Performix MCP server.
