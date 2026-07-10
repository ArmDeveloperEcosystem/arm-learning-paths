---
title: Create a Code Hotspots run

weight: 4

layout: learningpathall
---
If no supported Code Hotspots runs are available, you can create one from VS Code by asking the assistant to use the Arm Performix MCP server.

First, ask the assistant to list the configured targets:

```
List the available Arm Performix targets
```

Choose the target that should run your workload, then ask the assistant to run Code Hotspots and generate insights from the result:

```
Run the Code Hotspots recipe on the target named "<target name>" with this workload: "<command>". 
When the run completes, generate AI insights for that run. Suggest where I should start investigating next. 
```

Replace:

- `<target name>` with the Performix target name returned by the assistant.

- `<command>` with the command that starts your workload on the target. 

For example: 

```
Run the Code Hotspots recipe on the target named "graviton-dev" with this workload: "/opt/myapp/bin/my_app --input /data/input.dat". 
```

The assistant uses the Arm Performix MCP server to prepare the target, run the Code Hotspots recipe.

If you prefer to run the profile manually, use the Performix CLI:

```
apx recipe ready code_hotspots --target my-target --workload "/opt/myapp/bin/my_app --input /data/input.dat" 
 
apx recipe run code_hotspots --target my-target --workload "/opt/myapp/bin/my_app --input /data/input.dat" --timeout 30
```

Use `--timeout` for unattended profiling so the run ends automatically. If you are profiling an already-running process, use `--pid` instead of `--workload`.
