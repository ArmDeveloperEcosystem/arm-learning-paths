---
# User change
title: "Run the examples on Corstone-300 FVP"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
## Run an example

To run an example on the Corstone-300 FVP target, launch the FVP executable with `-a` to specify the software application.

To run the key word spotting example `ethos-u-kws.axf` compiled with `gcc` use:

- on your computer with the FVP installed

```console
FVP_Corstone_SSE-300_Ethos-U55 -a cmake-build-mps3-sse-300-ethos-u55-128-gnu/bin/ethos-u-kws.axf
```

- on Arm Virtual Hardware

```console
VHT_Corstone_SSE-300_Ethos-U55 -a cmake-build-mps3-sse-300-ethos-u55-128-gnu/bin/ethos-u-kws.axf
```
When the example is running, a telnet instance will open allowing you to interact with the example.

{{% notice Note %}}
It may take some time to initialize the terminal, please be patient. 

If you see warnings regarding loading the image, these can likely be ignored.
{{% /notice %}}


Use the menu to control the application. For the key word spotting application enter 1 to classify the next audio clip.

![terminal #center](term.png)

The results of the classification will appear in the visualization window of the FVP. 

The display shows a 98% chance of the audio clips sound was down.

![visualization #center](vis.png)

End the simulation by pressing Control-C in the terminal where to started the FVP.

You now have the ML Evaluation Kit examples running. Experiment with the different examples provided.

## Addedum: Setting model parameters

You can specify additional parameters to configure certain aspects of the simulated Corstone-300.

### List parameters

List the available parameters by running the FVP executable with the `--list-params` option, for example:

```console
FVP_Corstone_SSE-300_Ethos-U55 --list-params > parameters.txt
```

{{% notice Note %}}
If you are running with Arm Virtual Hardware substitute `VHT_Corstone_SSE-300_Ethos-U55` as the executable name.
{{% /notice %}}

Open the file `parameters.txt` to see all of the possible parameters and the default values. 

### Set parameters

Individual parameters can be set with the `-C` command option. 

For example, to put the Ethos-U component into fast execution mode:

```console
FVP_Corstone_SSE-300_Ethos-U55 -a cmake-build-mps3-sse-300-ethos-u55-128-gnu/bin/ethos-u-kws.axf -C ethosu.extra_args="--fast"
```
{{% notice Note %}}
Do not use fast execution mode whilst benchmarking performance.
{{% /notice %}}

To set multiple parameters it may be easier to list them in a text file (without `-C`) and use `-f` to specify the file.

For example, use a text editor to create a file named `options.txt` with the contents:

```console
mps3_board.visualisation.disable-visualisation=1
ethosu.extra_args="--fast"
```

Run the FVP with the `-f` option and the `options.txt` file:

```console
FVP_Corstone_SSE-300_Ethos-U55 -a cmake-build-mps3-sse-300-ethos-u55-128-gnu/bin/ethos-u-kws.axf -f options.txt
```

Full instructions are provided in the evaluation kit [documentation](https://review.mlplatform.org/plugins/gitiles/ml/ethos-u/ml-embedded-evaluation-kit/+/HEAD/docs/quick_start.md).
