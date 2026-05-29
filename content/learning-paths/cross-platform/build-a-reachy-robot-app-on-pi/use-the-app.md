---
title: Look at the dashboard and use the application
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Open the dashboard

If you are connected to the Raspberry Pi with VS Code Remote SSH, VS Code can forward the dashboard port to your laptop. Open the dashboard from your laptop browser:

```text
http://localhost:8042
```

If you are not using Remote SSH port forwarding, use the Pi IP address directly.

Find the Raspberry Pi IP address:

```bash
hostname -I
```

Then open the dashboard from any browser on the same network:

```text
http://<pi-ip-address>:8042
```

This works even when the Pi is headless. The browser only needs network access
to the Pi and port `8042`.

The app will countdown from 10, and then Reachy will start performing moves. Reachy will perform the same move three times, and then await your verdict. After a verdict is given, Reachy will perform the **Victory** or **Defeat** moves. Reachy will then randomly select another move the cycle will repeat.

![Thumbs Up Victory#center](thumbs-up.gif "Thumbs Up Victory")

![Thumbs Down Defeat#center](thumbs-down.gif "Thumbs Down Defeat")

When you are finished, you can stop the Pi app with `Ctrl+C` in the terminal you ran the application from.

## What you learned and what is next

You opened the dashboard, watched the live camera and app state, gave thumbs-up and thumbs-down verdicts, and saw how edge AI gesture recognition changes Reachy's next action. This is a simple application premise using vision to control expressive robot outputs. Next you will understand how the app works and how you could take this further or make your own.
