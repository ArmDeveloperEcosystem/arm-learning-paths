---
title: Run capture and verify outputs
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run in Standalone Game mode

Use **Standalone Game** for capture:

1. Open the play mode menu next to the **Play** button.
2. Select **Standalone Game**.

![Unreal Play mode menu with Standalone Game selected#center](./images/play-standalone-mode.png "Figure 7: Select Standalone Game before capturing.")

{{% notice %}}
If you use **New Editor Window (PIE)**, captured frame dimensions can differ from expected output sizes.
{{% /notice %}}

## Start and stop capture

1. Press **Play**.
2. Press `C` to begin capture.
3. Move through the level to capture frames.
4. Press `V` to stop capture.

![Standalone game window while capture is running#center](./images/standalone-capture-running.png "Figure 8: Capture running in Standalone mode.")

After stopping, you should see a completion notification in the bottom right corner. 

## Locate the dataset

Captured output is written under:

```
<YourProject>/Saved/NeuralGraphicsDataset/
```

With the defaults from this tutorial, look for:

```
<YourProject>/Saved/NeuralGraphicsDataset/0000
```

Proceed to the next section to tune settings and troubleshoot common issues.
