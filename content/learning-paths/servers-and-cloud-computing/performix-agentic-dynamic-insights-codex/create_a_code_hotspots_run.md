---
title: Create an Arm Performix Code Hotspots run

weight: 4

description: Create a representative Arm Performix Code Hotspots run through Codex or the Performix CLI and record its run ID.

layout: learningpathall
---
## Prepare a representative workload

If you already have a supported Code Hotspots run, skip to [Generate Arm Performix AI insights for a Code Hotspots run](/learning-paths/servers-and-cloud-computing/performix-agentic-dynamic-insights-codex/generate_ai_insights/).

For a new run, choose a workload that represents the behavior you want to optimize. Specify the executable with an absolute path because Performix doesn't support relative workload paths. Build it with debug symbols when possible so Performix can attribute samples to functions and source lines. Aim for at least 20 seconds of representative activity; a very short run might not collect enough samples for useful analysis.

Before profiling, make sure you know:

- the Performix target name
- the executable path and arguments on the target
- the workload's working directory and required environment variables
- whether running the workload has side effects

## Create a run with Codex

First, ask Codex to list the configured targets:

```text
Use the Arm Performix MCP server to list the configured targets. Include each target's name and connection status when available.
```

Choose the correct target, then ask Codex to run Code Hotspots. Keep collection and analysis as separate requests so you can confirm the target and workload before remote execution:

```text
Use Arm Performix to run the Code Hotspots recipe on target "<target-name>" with workload "<command>". Before starting, repeat the target and workload and ask me to confirm them. When the run completes, return its run ID and collection status.
```

Replace the following placeholders:

- `<target-name>` with the Performix target name returned by Codex
- `<command>` with the command that starts your workload on the target

For example:

```text
Use Arm Performix to run the Code Hotspots recipe on target "graviton-dev" with workload "/opt/myapp/bin/my_app --input /data/input.dat". Before starting, repeat the target and workload and ask me to confirm them. When the run completes, return its run ID and collection status.
```

After you confirm the target, Codex uses the MCP server to start the recipe. Review any permission request before allowing the assistant to run a command on the target.

## Create a run with the Arm Performix CLI

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

The `--timeout 30` option limits profiling to 30 seconds and doesn't make a short workload run longer. Use a duration that captures representative behavior.

Add `--working-dir`, `--env`, or `--source` when your workload needs a specific working directory, environment variables, or host-based source mapping. For an already-running process, replace `--workload` with `--pid <process-id>`.

When collection finishes, list the saved runs:

```bash
apx run list
```

Confirm that the new run completed successfully and record its run ID.

## Troubleshoot remote target authentication

If remote target authentication fails, check that:

- SSH key-based authentication works without an interactive password prompt.
- The private key doesn't require an interactive passphrase.
- Passwordless `sudo` is configured for the target user.
- Strict host-key checking succeeds.
- `~/.ssh/known_hosts` contains the target key and each jump-node key.

Use the Arm Performix target test to check the configured connection independently of Codex:

```bash
apx target test --target <target-name>
```

## What you've accomplished and what's next

You now have the stable identifier Codex needs to analyze the intended profile.

Next, you'll generate AI insights from a Code Hotspots run.
