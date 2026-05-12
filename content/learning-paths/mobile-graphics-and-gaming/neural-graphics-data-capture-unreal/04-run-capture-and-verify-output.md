---
title: Run capture and verify outputs
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run in Standalone Game mode

Use **Standalone Game** for capture:

- Open the play mode menu next to the **Play** button.
- Select **Standalone Game**.

![Screenshot of the Unreal Engine Play mode dropdown menu with Standalone Game option highlighted. Select this option instead of Play in Editor to ensure correct frame dimensions.#center](./images/play-standalone-mode.png "Standalone Game mode selection")

{{% notice %}}
If you use **New Editor Window (PIE)**, captured frame dimensions can differ from expected output sizes.
{{% /notice %}}

## Start and stop capture

- Press **Play**.
- Press `C` to begin capture.
- Move through the level to capture frames.
- Press `V` to stop capture.

![Screenshot of the Standalone Game window during active capture showing the game viewport with the character visible. This shows what you'll see while frames are being captured.#center](./images/standalone-capture-running.webp "Capture running in Standalone mode")

After stopping, you should see a completion notification in the bottom right corner. 

## Locate the dataset

Captured output is written under:

```
<YourProject>/Saved/NeuralGraphicsDataset/
```

With the defaults from this tutorial, see:

```
<YourProject>/Saved/NeuralGraphicsDataset/0000
```

Proceed to the next section to tune settings and troubleshoot common issues.
