---
title: Create a Code Hotspots run

weight: 4

description: Create a representative Arm Performix Code Hotspots run through Codex or the Performix CLI and record its run ID.

layout: learningpathall
---
## Prepare a representative workload

You can skip this section if you already selected a supported Code Hotspots run.

For a new run, choose a workload that represents the behavior you want to optimize. Specify the executable with an absolute path because Performix doesn't support relative workload paths. Build it with debug symbols when possible so Performix can attribute samples to functions and source lines. Aim for at least 20 seconds of representative activity; a very short run might not collect enough samples for useful analysis.

Before profiling, make sure you know:

- The Performix target name.
- The executable path and arguments on the target.
- The workload's working directory and required environment variables.
- Whether running the workload has side effects.

## Create a run with Codex

First, ask Codex to list the configured targets:

```text
Use the Arm Performix MCP server to list the configured targets. Include each target's name and connection status when available.
```

Choose the correct target, then ask Codex to run Code Hotspots. Keep collection and analysis as separate requests so you can confirm the target and workload before remote execution:

```text
Use Arm Performix to run the Code Hotspots recipe on target "<target-name>" with workload "<command>". Before starting, repeat the target and workload and ask me to confirm them. When the run completes, return its run ID and collection status.
```

Replace:

- `<target-name>` with the Performix target name returned by Codex.
- `<command>` with the command that starts your workload on the target.

For example:

```text
Use Arm Performix to run the Code Hotspots recipe on target "graviton-dev" with workload "/opt/myapp/bin/my_app --input /data/input.dat". Before starting, repeat the target and workload and ask me to confirm them. When the run completes, return its run ID and collection status.
```

After you confirm, Codex uses the MCP server to start the recipe. Review any permission request before allowing the assistant to run a command on the target.

## Create a run with the Performix CLI

If you prefer to control collection from a terminal, first check that the recipe dependencies and workload are ready:

```bash
apx recipe ready code_hotspots \
    --target my-target \
    --workload "/opt/myapp/bin/my_app --input /data/input.dat"
```

If Performix reports missing or outdated target tools, deploy them as part of the run:

```bash
apx recipe run code_hotspots \
    --target my-target \
    --workload "/opt/myapp/bin/my_app --input /data/input.dat" \
    --timeout 30 
```

The `--timeout 30` option limits profiling to 30 seconds; it doesn't make a short workload run longer. Use a duration that captures representative behavior. Add `--working-dir`, `--env`, or `--source` when your workload needs a specific working directory, environment variables, or host-based source mapping. For an already-running process, replace `--workload` with `--pid <process-id>`.

When collection finishes, list the saved runs:

```bash
apx run list
```

Confirm that the new run completed successfully and record its run ID. You now have the stable identifier Codex needs to analyze the intended profile.
