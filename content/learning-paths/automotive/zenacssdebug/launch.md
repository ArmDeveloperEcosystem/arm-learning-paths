---
# User change
title: "Launch the FVP"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Start the FVP from the build environment

You can launch the FVP within the build environment with the software stack loaded:

```command
kas shell -c "../layers/meta-arm/scripts/runfvp -t tmux --verbose"
```

See the [Arm Zena CSS User Guide](https://arm-auto-solutions.docs.arm.com/en/v2.0/rd-aspen/user_guide/reproduce.html#run-the-fvp) for further information.

While you can continue to use this method during debugging, it does not enable the Iris debug server in the model, so the system cannot be debugged from Arm Development Studio. Additional command-line options are required.

You will use the following options (see `FVP_RD_Aspen --help` for the full list). Options are case-sensitive.

| Option                  | Alias | Notes                                                 |
|-------------------------|:-----:|-------------------------------------------------------|
| `--iris-server`         | `-I`  | Start the Iris debug server                           |
| `--iris-port <port>`    |       | Set the Iris port (default `7100`)                    |
| `--run`                 | `-R`  | Run the simulation when the debug server starts       |
| `--iris-allow-remote`   | `-A`  | Allow remote connections (only if required)           |

## Enable the Iris debug server for Arm Development Studio

Append `--` to pass model options through `runfvp`.

Start the model with the debug server and hold at reset:
```command
kas shell -c "../layers/meta-arm/scripts/runfvp -t tmux --verbose -- --iris-server --iris-port 7100"
```

Start the model with the debug server and begin execution so that boot can progress:
```command
kas shell -c "../layers/meta-arm/scripts/runfvp -t tmux --verbose -- --iris-server --iris-port 7100 --run"
```

If required, allow remote debug connections using option aliases:
```command
kas shell -c "../layers/meta-arm/scripts/runfvp -t tmux --verbose -- -I -A --iris-port 7100"
```

{{% notice Note %}}
Even when using the default, specify the Iris port explicitly so it matches your debugger connection settings. If you enable remote connections, ensure your firewall allows inbound access to the chosen port.
{{% /notice %}}
