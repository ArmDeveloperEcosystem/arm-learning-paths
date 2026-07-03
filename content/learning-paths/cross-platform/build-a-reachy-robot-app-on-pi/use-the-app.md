---
title: Use the Reachy Gladiator application
description: Open the dashboard on the Raspberry Pi, watch the live camera and robot state, and use thumbs-up or thumbs-down gestures to control Reachy Gladiator.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Open the application dashboard

If you're connected to the Raspberry Pi with VS Code Remote SSH, VS Code can forward the dashboard port to your laptop. Open the dashboard from your laptop browser:

```text
http://localhost:8042
```

If you aren't using Remote SSH port forwarding, use the Pi IP address directly.

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

## Control Reachy with thumbs-up and thumbs-down gestures

The app will count down from 10, and then Reachy will start performing moves. Reachy will perform the same move three times, and then await your thumbs-up or thumbs-down verdict. After you give a verdict, Reachy will perform the victory or defeat moves. Reachy will then randomly select another move, and the cycle repeats.

![Animated dashboard and simulation showing a thumbs-up gesture triggering Reachy's victory reaction. This confirms that the Pi app recognized the gesture and sent the matching robot command.#center](thumbs-up.gif "Thumbs up victory")

![Animated dashboard and simulation showing a thumbs-down gesture triggering Reachy's defeat reaction. This confirms that the Pi app can classify the opposite verdict and update Reachy's behavior.#center](thumbs-down.gif "Thumbs down defeat")

When you're finished with the Pi app, you can stop it with `Ctrl+C` in the terminal that you ran the application from.

## What you've accomplished and what's next

You've now opened the dashboard, watched the live camera and app state, given thumbs-up and thumbs-down verdicts, and seen how edge AI gesture recognition changes Reachy's next action. This is a simple application premise using vision to control expressive robot outputs. 

Next, you'll learn how the app works.
