---
title: Troubleshooting

weight: 7

layout: learningpathall
---
Here are some solutions to common problems you may face when using this workflow.

## The Codex extension does not show the Arm Performix MCP server

Use Codex's `mcp list` subcommand to check if Codex has picked up the MCP server and what settings are present:

```
codex mcp list
Name                Command                 Args
arm-performix     /Applications/Arm Performix.app/Contents/assets/apx/apx      mcp start
```

If this is correct, check:

1. the `apx` command path is correct,
2. the arguments are `mcp` and `start`,
3. the server name is configured in Codex settings or `~/.codex/config.toml`,
4. you restarted the Codex extension after saving the configuration,
5. you are editing the Codex configuration for the same user account that runs VS Code.

## The MCP server fails to start

Common causes include:

1. incorrect Arm Performix executable path,
2. missing execute permission,
3. incompatible Arm Performix version,
4. missing license or environment setup,
5. server started on the wrong machine when using remote development,
6. SSH target configuration that does not satisfy Arm Performix requirements.

## The Assistant does not use Arm Performix

Try a more explicit prompt:

```
Use the Arm Performix MCP server to list the available Arm Performix runs. 
```

Or:

```
Use Arm Performix to generate AI Insights for the run named "<run ID>". 
```

If you have many MCP servers installed, ambiguous prompts such as give me insights might cause the assistant to choose a different tool.

## No supported runs are found

Check:

1. you have created at least one supported Code Hotspots run,
2. the MCP server is running as the same user who created the run,
3. the run exists in the same Arm Performix data location used by the GUI and CLI,
4. the run has enough profile data, symbols, source, or disassembly to support useful analysis,
5. you are not connected to a remote VS Code environment that has a different home directory or Arm Performix configuration.

## Remote target authentication fails

Check:

1. SSH key-based authentication is configured,
2. passwordless sudo is configured if your recipe or target setup requires it,
3. strict host-key checking can succeed,
4. your known_hosts file contains the target SSH host key,
5. your known_hosts file contains each jump-node host key, if jump nodes are used.

## The insight is too generic

Try narrowing the request:

```
Focus on the highest-impact finding in run "<run ID>" and explain the evidence. 
```

Or:

```
Explain whether <function-name> appears to be limited by scalar code, memory traffic, locking, allocation, or call overhead. Use evidence from the Performix run. 
```

The more specific the question, the easier it is for the assistant to use high-signal profile evidence.
