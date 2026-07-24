---
title: Troubleshooting

weight: 7

description: Diagnose Arm Performix MCP startup, Codex tool selection, run discovery, remote authentication, and low-quality insight problems.

layout: learningpathall
---
## Diagnose the MCP workflow

Use these checks to isolate configuration, process startup, data discovery, and profile-quality problems.

## The Codex extension does not show the Arm Performix MCP server

Check whether Codex loaded the server configuration:

```bash
codex mcp list
```

Find `arm-performix` in the output. Then confirm:

- The command is the full path to the `apx` executable, including `apx.exe` on Windows.
- The only argument is `mcp`.
- The server is enabled.
- You restarted the extension after changing the configuration.
- You edited the configuration for the same user account and Codex host that runs the extension.

## The MCP server fails to start

Run the executable's built-in help from a terminal to separate an `apx` problem from a Codex configuration problem. Replace `<path-to-apx>` with the configured path:

```bash
"<path-to-apx>" mcp --help
```

If the help text doesn't appear, check the executable path, file permissions, and installed Arm Performix version. If it does appear, reopen **MCP servers** in the Codex extension and check the server status.

In a remote development session, make sure `apx` is installed on the Codex host and that this installation uses the expected Performix configuration and run data.

## Codex does not use Arm Performix

Name the server and task explicitly:

```text
Use the Arm Performix MCP server to list the available Arm Performix runs.
```

For a specific run:

```text
Use Arm Performix to generate an AI Insight for run ID "<run-id>".
```

If you have several MCP servers, an ambiguous prompt such as `give me insights` might not select Arm Performix.

## No supported runs are found

Check:

- You created at least one completed Code Hotspots run.
- The MCP server runs as the same user who created or imported the run.
- The GUI, CLI, and MCP server use the same Arm Performix data location.
- The selected run contains enough samples and profile data for analysis.
- A remote VS Code environment isn't using a different home directory or Performix configuration.

Compare the MCP result with the CLI:

```bash
apx run list
```

If the CLI also returns no run, create or import a run. If the CLI returns the run but Codex doesn't, recheck which host, user, and configuration start the MCP server.

## Remote target authentication fails

Check:

- SSH key-based authentication works without an interactive password prompt.
- The private key doesn't require an interactive passphrase.
- Passwordless `sudo` is configured for the target user.
- Strict host-key checking succeeds.
- `~/.ssh/known_hosts` contains the target key and each jump-node key.

Use the Arm Performix target test to check the configured connection independently of Codex:

```bash
apx target test --target <target-name>
```

## The insight is too generic

Ask for one finding and its evidence:

```text
Focus on the highest-impact finding in run ID "<run-id>". Cite the measured evidence, distinguish hypotheses from observations, and identify the next Performix view or recipe to inspect.
```

For a known hotspot:

```text
For function "<function-name>" in run ID "<run-id>", summarize what Code Hotspots proves, what it doesn't prove, and which additional evidence is needed to identify the root cause.
```

If the response remains generic, confirm that the run has enough samples, symbols, source mapping, and disassembly. Code Hotspots locates sampled CPU time; use a more specific Performix recipe when you need evidence about microarchitecture, instruction mix, or memory access.
