---
title: Install and enable the plugin
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin

This plugin currently supports **Unreal Engine 5.5**.

Use a **C++ Unreal project** so the plugin module can compile through Visual Studio.

## Clone the repository

The plugin lives in a GitHub repository. Start by cloning it:

```
git clone https://github.com/arm/neural-graphics-data-capture-for-unreal
```

## Add plugin files to your project

- Open your Unreal project folder in File Explorer.
- Create a `Plugins` folder at the root of the project if it doesn't already exist.
- Copy the `NeuralGraphicsDataCapture` plugin folder from the `Source` directory into your new `Plugins/` directory. 

![Screenshot of Windows File Explorer showing the project root directory with a Plugins folder containing the NeuralGraphicsDataCapture folder. This confirms the plugin is in the correct location.#center](./images/project-plugins-folder.png "Project root with Plugins directory")

## Reopen project and build module

- Reopen the `.uproject` file.
- If prompted about missing modules, select **Yes** to rebuild.

![Dialog box showing that the NeuralGraphicsDataCapture module is missing and asking whether to rebuild it. Select Yes to continue.#center](./images/missing-modules-rebuild-prompt.png "Missing module rebuild prompt")

- Build the project in Visual Studio.

{{% notice %}}If Unreal doesn't detect the plugin after copying files, regenerate project files and rebuild from Visual Studio.{{% /notice %}}

## Verify plugin is enabled

In Unreal Editor:

- Go to **Edit > Plugins**.
- Search for `data cap`.
- Confirm **Neural Graphics Data Capture Plugin for Unreal Engine** is enabled.

![Screenshot of the Unreal Engine Plugins window with the search results showing Neural Graphics Data Capture Plugin for Unreal Engine with the enabled checkbox selected. This confirms the plugin is active.#center](./images/plugin-enabled-in-editor.png "Plugin enabled in Unreal Editor")

Next, add the capture graph to your Level Blueprint.