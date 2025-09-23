---
# User change
title: "Launch FVP"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Launch the FVP

You can launch the FVP within the build environment with the software stack loaded:

```command
kas shell -c "../layers/meta-arm/scripts/runfvp -t tmux --verbose"
```

See the [documentation](https://arm-auto-solutions.docs.arm.com/en/v2.0/rd-aspen/user_guide/reproduce.html#run-the-fvp) for details.

While you can continue to use this method during debugging, it does not enable the Iris debug server in the model, so the system cannot be debugged from Arm Development Studio. Additional command-line options are required.

You will use the following options (see `FVP_RD_Aspen --help` for the full list). **Options are case-sensitive.**

| Option                  | Alias | Notes                                                 |
|-------------------------|:-----:|-------------------------------------------------------|
| `--iris-server`         | `-I`  | Start the Iris debug server                           |
| `--iris-port <port>`    |       | Set the Iris port (default `7100`)                    |
| `--run`                 | `-R`  | Run the simulation when the debug server starts       |
| `--iris-allow-remote`   | `-A`  | Allow remote connections (only if required)           |

## Launch the FVP with additional options

Append `--` to pass model options through `runfvp`.

**Start the model with the debug server and hold at reset:**
```command
kas shell -c "../layers/meta-arm/scripts/runfvp -t tmux --verbose -- --iris-server --iris-port 7100"
```

Start the model with the debug server and begin execution (so boot can progress):
```command
kas shell -c "../layers/meta-arm/scripts/runfvp -t tmux --verbose -- --iris-server --iris-port 7100 --run"
```

Allow remote debug connections (only if needed), using option aliases:
```command
kas shell -c "../layers/meta-arm/scripts/runfvp -t tmux --verbose -- -I -A --iris-port 7100"
```

{{% notice Note %}}
Specify the Iris port explicitly (even when using the default) so it matches your debugger connection settings. If you enable remote connections, ensure your firewall allows inbound access to the chosen port.
{{% /notice %}}
