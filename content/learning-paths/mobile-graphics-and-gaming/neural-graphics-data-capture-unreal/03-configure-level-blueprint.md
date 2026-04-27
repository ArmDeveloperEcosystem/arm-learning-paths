---
title: Configure Level Blueprint capture controls
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Open the Level Blueprint

In your level:

- Open the **Blueprints** drop-down.
- Select **Open Level Blueprint**.

![Screenshot of the Unreal Engine toolbar showing the Blueprints menu expanded with Open Level Blueprint option highlighted. Select this option to open the blueprint editor.#center](./images/open-level-blueprint-menu.png "Open Level Blueprint menu")

## Fast path: download and paste the ready-made blueprint snippet

On Windows, use PowerShell to download the prepared Level Blueprint snippet from this Learning Path repository:

```powershell
wget "https://raw.githubusercontent.com/ArmDeveloperEcosystem/arm-learning-paths/main/content/learning-paths/mobile-graphics-and-gaming/neural-graphics-data-capture-unreal/assets/level_blueprint.txt" -OutFile ".\level_blueprint.txt"
```

Then in Unreal Editor:

- Open `level_blueprint.txt` in a text editor and copy all text.
- Select empty space in the Level Blueprint Event Graph.
- Paste to create the full node graph.
- Select **Compile** and **Save**.

{{% notice %}}
If you use Git Bash with GNU `wget`, use `wget -O level_blueprint.txt "https://raw.githubusercontent.com/ArmDeveloperEcosystem/arm-learning-paths/main/content/learning-paths/mobile-graphics-and-gaming/neural-graphics-data-capture-unreal/assets/level_blueprint.txt"` instead.
{{% /notice %}}

## Blueprint capture flow configuration

The snippet wires the following capture flow:

- Gets the **Neural Graphics Data Capture Subsystem**.
- Builds `NGDCCaptureSettings` from:
  - `NGDCRenderingSettings`
  - `NGDCExportSettings`
- Calls **Begin Capture** on key `C`.
- Calls **End Capture** on key `V`.

It also sets these export defaults to match this tutorial:

- `Dataset Dir`: `NeuralGraphicsDataset`
- `Capture Name`: `0000`

![Close-up screenshot of the Level Blueprint showing the capture settings nodes and the Neural Graphics Data Capture Subsystem being wired to Begin Capture and End Capture nodes. This shows how the settings are configured.#center](./images/blueprint-capture-subsystem-closeup.webp "Capture settings and subsystem wiring")

The full event graph should look similar to this:

![Screenshot of the complete Level Blueprint event graph showing keyboard input C connected to Begin Capture and keyboard input V connected to End Capture, with all necessary settings nodes connected. This is the expected final blueprint configuration.#center](./images/level-blueprint-full-graph.webp "Complete blueprint graph")

Continue to run the level in Standalone mode and test capture.
