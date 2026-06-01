---
title: Understand the app code
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand the code structure

The project separates perception, app logic, robot motion, and dashboard rendering.

The key files running on the Pi are:

```text
reachy_gladiator_lp/
├── main.py
├── camera.py
├── gesture.py
├── moves.py
├── assets/
│   └── gesture_recognizer.task
└── static/           # dashboard HTML, CSS, JavaScript, and media
```

## Follow the app lifecycle - main.py

`reachy_gladiator_lp/main.py` is the center of the application. It defines the `ReachyGladiatorLp` class, which inherits from `ReachyMiniApp`.

Two settings are important for the distributed simulation route:

```python
custom_app_url: str | None = "http://0.0.0.0:8042"
request_media_backend: str | None = "no_media"
```

`custom_app_url` tells the Reachy app framework where the dashboard is served.
`request_media_backend = "no_media"` tells the SDK not to request camera media
from the daemon, because the Pi uses its own USB webcam. For a physical Reachy
route, setting `REACHY_GLADIATOR_MEDIA_BACKEND=reachy` lets the SDK request the
daemon media backend.

The useful part to inspect is `run()`, because that is where the app receives a
connected `ReachyMini` object and starts the edge AI loop:

```python
def run(self, reachy_mini: ReachyMini, stop_event: threading.Event) -> None:
    rng = random.Random()
    move_queue: list[str] = []
    last_move: str | None = None
    detector: ThumbGestureDetector | None = None
    latest_frame: np.ndarray | None = None

    self._status = {
        "state": "starting",
        "round": 0,
        "active_move": None,
        "gesture": None,
        "confidence": 0.0,
        "camera_ready": False,
    }
```

This state drives both sides of the app: robot behavior and dashboard display.
The `run()` method keeps track of:

- `move_queue` stores the shuffled bag of moves.
- `last_move` prevents immediate repeats at a shuffle boundary.
- `detector` stores the MediaPipe gesture detector.
- `latest_frame` stores the newest webcam frame from the capture thread.
- `status` stores the data returned by the dashboard `/status` endpoint.

The `_update_status()` helper updates dashboard state safely:

```python
def _update_status(self, **values: Any) -> None:
    with self._state_lock:
        self._status.update(values)
```

The nested `capture_frames()` helper runs in the background. It reads frames from the selected camera source, saves the newest frame for gesture detection, and marks the dashboard camera as ready.

The actual loop is intentionally small:

```python
def capture_frames(frame_source: FrameSource) -> None:
    while not stop_event.is_set() and not capture_stop.is_set():
        frame = frame_source.get_frame()
        if frame is None:
            time.sleep(LOOP_SLEEP_S)
            continue

        self._update_frame(frame)
        self._update_status(camera_ready=True)
        time.sleep(LOOP_SLEEP_S)
```

`main.py` also registers FastAPI endpoints on `settings_app`:

- `/status` returns the latest round, state, move, gesture, confidence, and camera status.
- `/video` streams resized JPEG frames as an MJPEG feed for the browser dashboard.

Those routes are registered inside the app class:

```python
@self.settings_app.get("/status")
def get_status() -> dict[str, Any]:
    with self._state_lock:
        return dict(self._status)

@self.settings_app.get("/video")
def video() -> StreamingResponse:
    return StreamingResponse(
        self._video_stream(self._read_frame),
        media_type="multipart/x-mixed-replace; boundary=frame",
    )
```

The main loop has four phases:

1. Build the next move sequence with `_build_sequence()`.
2. Perform the selected move `MOVE_REPETITIONS` times.
3. Return to neutral and call `_await_verdict()`.
4. Run `victory()`, `defeat()`, or continue neutrally.

The verdict code requires two consecutive confident classifications before it accepts a gesture. This debounce step helps avoid reacting to a single noisy frame.

This is the core move-and-verdict flow:

```python
sequence = self._build_sequence(rng, move_queue, last_move)
for name in sequence:
    move_fn = gmoves.MOVE_CATALOGUE[name]
    for repeat_idx in range(1, MOVE_REPETITIONS + 1):
        self._update_status(active_move=name, current_repeat=repeat_idx)
        move_fn(reachy_mini)

gmoves.neutral(reachy_mini)
verdict, detector = self._await_verdict(
    reachy_mini,
    self._read_frame,
    detector,
    stop_event,
    self._update_status,
)
```

The app is still a normal Reachy Mini app. It receives a connected
`ReachyMini` object in `run()`. That object is the SDK boundary, so the rest of
the app does not need to know whether commands go to MuJoCo simulation or to a
physical robot.

## Capture camera frames - camera.py

`reachy_gladiator_lp/camera.py` selects the frame source. A frame source is
anything that can return the next camera image as a NumPy array.

For the default simulation-plus-Pi route, frames come from a USB webcam plugged
into the Raspberry Pi. The app uses OpenCV to open that webcam and read frames:

```python
self._capture = cv2.VideoCapture(camera_index)
```

`camera_index` is the local video-device number on the Pi. Index `0` usually
means the first camera OpenCV can open; index `1` means the next one. If
`REACHY_GLADIATOR_CAMERA_INDEX=1` worked in the camera check, use the same
value when running the app.

For the physical Reachy route, frames come from the Reachy daemon media
pipeline instead. In that case, `camera_index` is not used.

The `REACHY_GLADIATOR_CAMERA` environment variable chooses the route:

- `opencv` uses a local USB webcam through OpenCV.
- `reachy` uses camera frames from the Reachy daemon.

The source selection code is therefore small:

```python
requested = os.getenv("REACHY_GLADIATOR_CAMERA", "opencv").strip().lower()

if requested == "opencv":
    return OpenCVCameraFrameSource(_camera_index())

if requested == "reachy":
    return ReachyMediaFrameSource(reachy_mini)
```

After a frame is captured, the latest frame is copied into shared state. Both
the detector and dashboard stream read from that newest frame. This lets the
same app use either a Pi USB webcam or the physical Reachy camera without
changing the gesture-recognition code.

## Recognize thumbs with MediaPipe - gesture.py

`reachy_gladiator_lp/gesture.py` runs the MediaPipe Gesture Recognizer. This is
the edge AI part of the app: the Raspberry Pi classifies camera frames locally
and only sends robot commands over the network.

The recognizer loads this model bundle:

```text
reachy_gladiator_lp/assets/gesture_recognizer.task
```

The `.task` file is a MediaPipe Tasks model bundle. It includes the trained
gesture-recognition model and the metadata MediaPipe needs to run it through
the Tasks API.

Under the hood, MediaPipe Tasks commonly runs the model through TensorFlow Lite
for efficient on-device inference. On CPU builds, TensorFlow Lite can use the
XNNPACK delegate to speed up neural-network operations on Arm CPUs.

The detector runs in a worker process instead of the main app thread. This
keeps MediaPipe inference separate from the robot-control loop, dashboard
responses, and camera capture. The robot-control loop and dashboard server therefore remain responsive while MediaPipe is classifying a frame.

The app uses the CPU delegate:

```python
base_options = python.BaseOptions(
    model_asset_path=model_path,
    delegate=python.BaseOptions.Delegate.CPU,
)
```

The recognizer is configured for one hand in image mode:

```python
options = vision.GestureRecognizerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.IMAGE,
    num_hands=1,
    min_hand_detection_confidence=0.5,
    min_hand_presence_confidence=0.5,
    min_tracking_confidence=0.5,
)
```

Each OpenCV frame is converted from BGR to RGB before MediaPipe sees it. BGR
and RGB contain the same red, green, and blue color channels, but in a different
order. OpenCV returns webcam frames as blue-green-red, while MediaPipe expects
red-green-blue:

```python
rgb_frame = bgr_frame[:, :, ::-1].copy()
mp_image = mediapipe.Image(image_format=mediapipe.ImageFormat.SRGB, data=rgb_frame)
result = recognizer.recognize(mp_image)
```

The app then maps MediaPipe labels to its own labels:

```python
if raw_label == "Thumb_Up":
    label = "thumbs_up"
elif raw_label == "Thumb_Down":
    label = "thumbs_down"
else:
    label = None
```

The returned `GestureResult` also includes the thumb tip pixel position. The worker queues have `maxsize=1`, which keeps detection biased toward the newest camera frame.

The app also warms the detector in the background while Reachy is preparing.
This means the first verdict window does not have to pay all of the detector
startup cost:

```python
def warmup_detector() -> None:
    warmed_detector = ThumbGestureDetector()
    while not stop_event.is_set() and not capture_stop.is_set():
        frame = self._read_frame()
        if frame is not None:
            warmed_detector.detect(frame)
            break
        time.sleep(LOOP_SLEEP_S)
```

When the verdict window starts, the app reuses the warmed detector if it is
ready:

```python
if detector is None:
    detector_warmup_done.wait(timeout=GESTURE_WARMUP_WAIT_S)
    with detector_warmup_lock:
        detector = detector_warmup["detector"]
        detector_warmup["detector"] = None
```

The debounce logic accepts a verdict only after two matching confident frames:

```python
if (
    result.label in ("thumbs_up", "thumbs_down")
    and result.confidence >= VERDICT_MIN_CONFIDENCE
):
    if result.label == last_label:
        consecutive += 1
    else:
        last_label = result.label
        consecutive = 1
    if consecutive >= 2:
        return result.label, detector
```

## Send robot motion commands - moves.py

`reachy_gladiator_lp/moves.py` contains small robot motion primitives:
`Salute`, `Sword Swing`, `Shield Up`, `Battle Cry`, victory, defeat, and
neutral. Each move accepts a `ReachyMini` instance and sends one or more
`goto_target()` commands.

For example, the `salute()` move combines a head target with antenna targets:

```python
reachy_mini.goto_target(
    head=create_head_pose(pitch=-16, yaw=0, roll=0, degrees=True),
    antennas=np.deg2rad([58, 58]),
    duration=0.42,
    method="minjerk",
)
```

`create_head_pose(...)` builds the head target in degrees. The antenna values
are converted to radians with `np.deg2rad(...)`.

Some moves try to use body yaw:

```python
reachy_mini.goto_target(body_yaw=yaw_rad, duration=duration, method=method)
```

The helper `_safe_body_yaw()` catches SDK or hardware cases where body yaw is unavailable and falls back to a smaller head motion.

The move catalogue is deliberately simple:

```python
MOVE_CATALOGUE: dict[str, MoveFn] = {
    "Salute": salute,
    "Sword Swing": sword_swing,
    "Shield Up": shield_up,
    "Battle Cry": battle_cry,
}
```

Adding a move means writing a new function and registering it in
`MOVE_CATALOGUE`. That makes the app loop eligible to select and run the move.
To display it cleanly in the dashboard, also add a matching entry to
`MOVE_DESCRIPTIONS`.

The shuffled bag logic lives in `main.py`, not in the move functions:

```python
names = list(gmoves.MOVE_CATALOGUE.keys())
if not move_queue:
    move_queue.extend(rng.sample(names, len(names)))
    if last_move is not None and len(move_queue) > 1 and move_queue[0] == last_move:
        move_queue.append(move_queue.pop(0))

return [move_queue.pop(0)]
```

The victory and defeat reactions are also just move functions. The state machine decides when to call them:

```python
if verdict == "thumbs_up":
    gmoves.victory(reachy_mini)
elif verdict == "thumbs_down":
    gmoves.defeat(reachy_mini)
```

`main.py` decides what should happen, and `moves.py` describes how Reachy should move.

## Render the dashboard

Because `custom_app_url` is set, the Reachy app base class starts a FastAPI
server for this app. That server mounts `reachy_gladiator_lp/static/` at
`/static` and serves `static/index.html` at `/`. The files in `static/` are
therefore the dashboard you view in the browser:

- `index.html` defines the dashboard layout.
- `main.js` polls `/status` and updates the DOM.
- `style.css` controls the arena theme, verdict colors, and responsive layout.
- `reachy_gladiator.png` is the gladiator image shown in the dashboard.

The JavaScript does not control the robot. It only renders state produced by
the Python app.

The dashboard camera feed is an MJPEG stream from `/video`. Python resizes each frame and encodes it as JPEG:

```python
preview_frame = self._resize_preview_frame(frame)
ok, encoded = cv2.imencode(
    ".jpg",
    preview_frame,
    [cv2.IMWRITE_JPEG_QUALITY, DASHBOARD_PREVIEW_JPEG_QUALITY],
)
```

`static/index.html` displays that stream in an image element, while
`static/main.js` polls `/status` for the round state, gesture confidence, and
verdict highlighting. This split keeps video transport simple.

The command-line entry point wires the script environment into the Reachy SDK connection:

```python
if __name__ == "__main__":
    daemon_host = os.getenv("REACHY_GLADIATOR_DAEMON_HOST", "localhost")
    daemon_port = int(os.getenv("REACHY_GLADIATOR_DAEMON_PORT", "8000"))
    daemon_timeout = float(os.getenv("REACHY_GLADIATOR_DAEMON_TIMEOUT", "8.0"))
    os.environ.setdefault("REACHY_GLADIATOR_CAMERA", "opencv")
    os.environ.setdefault("REACHY_GLADIATOR_MEDIA_BACKEND", "no_media")
    app = ReachyGladiatorLp()
    app.wrapped_run(host=daemon_host, port=daemon_port, timeout=daemon_timeout)
```

Take some time to read through the files and understand the different parts before moving on to extend the project.

## What you learned

You inspected how the app captures camera frames, runs MediaPipe gesture recognition on the Pi, debounces thumbs-up and thumbs-down verdicts, sends Reachy SDK motion commands, and renders a browser dashboard. You are now ready to experiment with adapting this project, or building your own app.
