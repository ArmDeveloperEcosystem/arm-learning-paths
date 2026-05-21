---
title: Setup Pi and run Edge AI app
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare the Raspberry Pi

The Raspberry Pi should be installed with Raspberry Pi OS Trixie, and be accessible over SSH.

Connect to your Raspberry Pi over SSH using [VSCode Remote - SSH](https://code.visualstudio.com/docs/remote/ssh), or via terminal e.g.,

```bash
ssh <user>@<pi-ip-address>
```

On your Pi, create a workspace and move into it:

```bash
mkdir -p ~/reachy_projects
cd ~/reachy_projects
```

Install and enable Git LFS before cloning the app. The MediaPipe gesture model
is stored as a Git LFS asset, so a normal clone without LFS can leave a tiny
pointer file instead of the real model:

```bash
sudo apt update
sudo apt install git-lfs
git lfs install
```

Clone the `reachy_gladiator_lp` project into this directory:

```bash
git clone https://github.com/matt-cossins/reachy_gladiator_lp.git
cd reachy_gladiator_lp
git lfs pull
```

Check that the gesture model was downloaded:

```bash
ls -lh reachy_gladiator_lp/assets/gesture_recognizer.task
```

The file should be about 8 MB. If it is only 132 bytes, run `git lfs pull`
again before continuing.

## Install the Pi runtime

Run the Pi setup script:

```bash
./scripts/setup_pi.sh
```

The script installs the system packages, Python version, Python packages, and app entry point used by this Learning Path.

Raspberry Pi OS Trixie can use Python 3.13 as the default `python3`, but the tested Pi environment for this app uses Python 3.12. The setup script installs Python 3.12.3 with `pyenv` so you do not need to modify the system Python.

The script also handles the Pi-specific package versions:

- `mediapipe==0.10.18`, because newer MediaPipe wheels are not available for the tested Pi environment.
- `numpy==2.4.4`, which is required by the Reachy Mini SDK and has been tested with the gesture worker.
- `reachy-mini==1.7.3`, installed without dependency resolution so pip does not reject the MediaPipe and NumPy combination.
- `git-lfs`, so the MediaPipe gesture model is downloaded as the real binary asset rather than an LFS pointer file.
- `v4l-utils`, so you can inspect connected camera devices with `v4l2-ctl`.

When setup finishes, activate the virtual environment:

```bash
source .venv/bin/activate
```

The setup script runs an import smoke test. It also runs `pip check`; a MediaPipe NumPy metadata warning is expected for this Pi setup.

Test the MediaPipe gesture worker from a real Python file:

```bash
cat > /tmp/test_gesture_worker.py <<'PY'
import numpy as np
from reachy_gladiator_lp.gesture import ThumbGestureDetector

def main():
    print("creating detector")
    detector = ThumbGestureDetector()
    frame = np.zeros((480, 640, 3), dtype=np.uint8)
    result = detector.detect(frame)
    print(result)
    detector.close()
    print("gesture detector OK")

if __name__ == "__main__":
    main()
PY
python /tmp/test_gesture_worker.py
```

The output should show that the detector starts and returns a neutral result for the blank test frame:

```output
creating detector
GestureResult(label=None, x_px=320, y_px=240, confidence=0.0)
gesture detector OK
```

MediaPipe may also print TensorFlow Lite or CPU delegate warnings before the result. The important line is `gesture detector OK`.

## Check the USB webcam

Plug the USB webcam into the Raspberry Pi and list video devices:

```bash
ls /dev/video*
```

Run the included camera check:

```bash
./scripts/check_pi_camera.sh
```

The output is similar to:

```output
Video devices:
/dev/video0
Camera index 0 OK: 1280x720
```

If camera index `0` does not work, try index `1`:

```bash
REACHY_GLADIATOR_CAMERA_INDEX=1 ./scripts/check_pi_camera.sh
```

If a different camera index works, use the same value when you run the app. For example, if camera index `1` works:

```bash
REACHY_GLADIATOR_CAMERA_INDEX=1 \
REACHY_GLADIATOR_DAEMON_PORT=18000 \
./scripts/run_pi_app.sh <simulation-host-ip>
```

## Run the distributed app

Keep the simulation terminal running on your simulation host.

On the Raspberry Pi, run the app with the simulation host IP address and the simulation port. This learning path uses port `18000`:

```bash
REACHY_GLADIATOR_DAEMON_PORT=18000 ./scripts/run_pi_app.sh <simulation-host-ip>
```

If you started the simulation on a different port, pass that same value in `REACHY_GLADIATOR_DAEMON_PORT`.

## What is the script doing?

The script sets the app configuration:

```text
REACHY_GLADIATOR_DAEMON_HOST=<simulation-host-ip>
REACHY_GLADIATOR_DAEMON_PORT=18000
REACHY_GLADIATOR_DASHBOARD_HOST=0.0.0.0
REACHY_GLADIATOR_DASHBOARD_PORT=8042
REACHY_GLADIATOR_MEDIA_BACKEND=no_media
REACHY_GLADIATOR_CAMERA=opencv
REACHY_GLADIATOR_CAMERA_INDEX=0
```

The app then runs:

```bash
python -m reachy_gladiator_lp.main
```

`REACHY_GLADIATOR_MEDIA_BACKEND=no_media` tells the Reachy SDK not to request
camera media from the daemon. This is the right default for the learning path
because the Pi owns the USB webcam. `REACHY_GLADIATOR_CAMERA=opencv` tells the
gesture recognizer to read frames from that local webcam.

## What you learned and what is next

You installed the Pi runtime with the project setup script, validated the MediaPipe gesture worker, checked the USB webcam, and started the edge AI app so it can run the application, perform inference on incoming frames, and send Reachy commands to the simulation host. Now you get to try out the app!
