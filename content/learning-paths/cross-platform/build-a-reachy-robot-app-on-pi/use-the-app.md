---
title: Look at the dashboard and use the Reachy Gladiator application
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Open the dashboard

If you're connected to the Raspberry Pi with VS Code Remote SSH, VS Code can forward the dashboard port to your laptop. Open the dashboard from your laptop browser:

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

This method works even when the Pi is headless. The browser needs network access only
to the Pi and port `8042`.

## Use Reachy Gladiator

The app will count down from 10, and then Reachy will start performing moves. Reachy will perform the same move three times, and then await your thumbs-up or thumbs-down verdict. After you give a verdict, Reachy will perform the victory or defeat moves. Reachy will then randomly select another move, and the cycle repeats.

![Thumbs Up Victory#center](thumbs-up.gif "Thumbs Up Victory")

![Thumbs Down Defeat#center](thumbs-down.gif "Thumbs Down Defeat")

When you're finished with the Pi app, you can stop it with `Ctrl+C` in the terminal that you ran the application from.

## What you've learned and what's next

You've now opened the dashboard, watched the live camera and app state, given thumbs-up and thumbs-down verdicts, and seen how edge AI gesture recognition changes Reachy's next action. This is a simple application premise using vision to control expressive robot outputs. 

Next, you'll learn how the app works and how you can take this further or make your own.
