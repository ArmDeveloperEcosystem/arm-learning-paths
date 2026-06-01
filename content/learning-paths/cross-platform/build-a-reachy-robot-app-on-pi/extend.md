---
title: (Optional) Extend the project
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Try focused changes

You now have a working physical AI pattern: sensor input at the edge, local
inference, robot commands, and a dashboard for visibility. A good next step is
to make small changes where the effect is easy to observe:

- Change `VERDICT_MIN_CONFIDENCE` in `main.py` to make thumbs detection
  stricter or more forgiving.
- Change `MOVE_REPETITIONS` in `main.py` so each move plays more or fewer
  times.
- Add a fifth move in `moves.py` and register it in `MOVE_CATALOGUE`.
- Try a different webcam with `REACHY_GLADIATOR_CAMERA_INDEX=1`.

These changes are deliberately small. They help you learn which part of the
system owns each behavior before you make larger changes to perception, robot
motion, or packaging.

## Change the classifier

Try adding new gesture controls. Start in `gesture.py`, where the app maps MediaPipe labels such as `Thumb_Up` and `Thumb_Down` to app labels. Then add matching robot behavior in `moves.py` and branch on the new label in `main.py`.

Some game-themed ideas:

- Map `Closed_Fist` to `challenge`, and make Reachy repeat the current move
- Map `Pointing_Up` to `reroll`, and make Reachy reject the current move and
  choose another one.
- Map the number of fingers shown to choose a specific move.

## Add audio output

The gladiator theme is a good fit for sound. Try adding audio cues such as:

- a crowd cheer during victory,
- a dramatic sound during defeat,
- a short drum hit before each move,
- a spoken move name before Reachy performs it.

Keep audio output separate from `moves.py` at first. For example, create an
`audio.py` helper and call it from `main.py` when the state changes. This keeps
robot motion and sound effects easy to change independently.

## Replace thumbs with audio input

The vision-based verdict is one edge AI input modality. You can replace
or complement it with audio. Many webcams include microphones, or you can use a USB microphone.

- say "yes" for victory and "no" for defeat,
- clap once for victory and twice for defeat,

A lightweight keyword-spotting model can map spoken commands to the same game states currently triggered by MediaPipe gestures.

## Try the packaged app on a physical Reachy

If you have a physical Reachy Mini, the quickest way to try the finished
experience is to install the packaged [Reachy Gladiator app](https://huggingface.co/spaces/cossinsmatthew/reachy_gladiator) through the [Reachy Mini Control app](https://github.com/pollen-robotics/reachy-mini-desktop-app).

Install Reachy Mini Control on a supported machine, connect it to your Reachy, and search for the Reachy Gladiator app.

{{% notice Warning %}}
If using a physical Reachy Mini, use caution and ensure the robot is used in an area with appropriate space. The robot has moving parts and could be a health & safety risk. You are responsible for your safety and the safety of others around you when using physical robotic devices.
{{% /notice %}}

## Adapt this source project for physical Reachy

The main learning path uses the Raspberry Pi USB webcam for perception and a
remote MuJoCo daemon for robot motion. A physical Reachy route changes two
things:

- camera frames come from the Reachy daemon instead of the Pi USB webcam,
- the Pi app connects to the physical Reachy daemon instead of the simulation
  daemon.

The source project exposes these switches as environment variables, so you do
not need to edit the Python source:

```bash
REACHY_GLADIATOR_MEDIA_BACKEND=reachy \
REACHY_GLADIATOR_CAMERA=reachy \
REACHY_GLADIATOR_DAEMON_PORT=8000 \
./scripts/run_pi_app.sh localhost
```

Use `localhost` only when the physical daemon runs on the same Pi as the app.
If the daemon runs on another machine, replace `localhost` with that machine's
IP address and set `REACHY_GLADIATOR_DAEMON_PORT` to the daemon port.

These variables map to the code in two places:

- `REACHY_GLADIATOR_MEDIA_BACKEND=reachy` lets `ReachyMiniApp` request daemon
  camera media.
- `REACHY_GLADIATOR_CAMERA=reachy` tells `camera.py` to use
  `ReachyMediaFrameSource` instead of `OpenCVCameraFrameSource`.

## Build your own Reachy Mini app

A Reachy Mini app is a Python package with a class that inherits from `ReachyMiniApp`, implements `run()`, and exposes an entry point in `pyproject.toml`.

To build a fresh app:

1. Start with one `ReachyMiniApp` class.
2. Add one safe motion such as `neutral()`.
3. Add one input source such as a camera gesture, audio command, button, or web
   endpoint.
4. Add a dashboard only after the core loop works.
5. Test in simulation before physical hardware.
6. Package the app when it is stable enough for repeated use.

The Reachy Mini tooling can scaffold and validate a shareable app:

```bash
reachy-mini-app-assistant create my_app ~/reachy_projects
reachy-mini-app-assistant check ~/reachy_projects/my_app
```

The [Reachy Mini app publishing guide](https://huggingface.co/blog/pollen-robotics/make-and-publish-your-reachy-mini-apps)
explains the packaging and publishing workflow in more detail.

Use the Reachy Mini SDK documentation and examples to understand available
motion, media, and daemon APIs. If you use an AI coding agent, give it the
Pollen Robotics `AGENTS.md` instructions, provided by the [Reachy Mini project](https://github.com/pollen-robotics/reachy_mini) so it follows the expected app structure.

## What you learned

You explored options for extending from simulation to a physical Reachy, as well as ideas for changing the project to include audio, new vision gestures, or different behaviors.
