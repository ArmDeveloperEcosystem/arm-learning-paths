---
# User change
title: "Launch FVP"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Launch FVP

You can now launch the FVP within the virtual environment with the software stack loaded:

```command
kas shell -c "../layers/meta-arm/scripts/runfvp -t tmux --verbose"
```
Refer to the [documentation](https://arm-auto-solutions.docs.arm.com/en/v2.0/rd-aspen/user_guide/reproduce.html#run-the-fvp) for more details.
While you can continue to use this method to launch the FVP whilst debugging, this command does not enable the Iris debug server inside the model, and so will not be debuggable.

Additional command options are necessary.

You will use the following. See output of `FVP_RD_Aspen --help` for full list and explanation. Options are case-sensitive.

| Option                | Alias    | Notes                                         |
|---------------------- |--------- |---------------------------------------------- |
| `--iris-server`       | `-I`     | Start Iris Debug Server                       |
| `--iris-port`         |          | Specify a port number (default = `7100`)      |
| `--run`               | `-R`     | Run simulation when debug server started      |
| `--iris-allow-remote` | `-A`     | Allow remote connections (if different hosts) |

### Launch FVP with additional options

To launch the FVP with additional options, modify the above command by adding `--` and then the options.

For example, to launch the model with the debug server and hold at the initial reset condition:

```command
kas shell -c "../layers/meta-arm/scripts/runfvp -t tmux --verbose -- --iris-server --iris-port 7100"
```

To launch the model and start running (so that it can start to boot up):

```command
kas shell -c "../layers/meta-arm/scripts/runfvp -t tmux --verbose -- --iris-server --iris-port 7100 --run"
```

To launch the model so that remote hosts can access it (not recommended if not needed), using options aliases:

```command
kas shell -c "../layers/meta-arm/scripts/runfvp -t tmux --verbose -- -I -A --iris-port 7100"
```

{{% notice Note %}}
It is recommended to specify the port number used even if it is the default as that must match the debug connection setting (see later).
{{% /notice %}}
