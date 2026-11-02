#!/usr/bin/env python3
"""Capture one NX dispatch and restore the Android GPU debug configuration."""

import argparse
import json
from pathlib import Path
import shlex
import shutil
import signal
import subprocess
import sys
import tarfile
import time


PACKAGE = "com.arm.ai_ml_sdk_scenario_runner"
KEYS = ("enable_gpu_debug_layers", "gpu_debug_app", "gpu_debug_layer_app", "gpu_debug_layers")
PROPERTY = "debug.vulkan.khronos_profiles.settings_path"


class Device:
    def __init__(self, serial):
        self.serial = serial

    def adb(self, *args, stdout=subprocess.PIPE):
        return subprocess.run(
            ["adb", "-s", self.serial, *args], check=True,
            stdout=stdout, stderr=subprocess.PIPE, timeout=30,
        ).stdout

    def shell(self, *args):
        return self.adb("shell", shlex.join(args)).decode().rstrip("\r\n")

    def settings(self):
        values = {key: self.shell("settings", "get", "global", key) for key in KEYS}
        values[PROPERTY] = self.shell("getprop", PROPERTY)
        return values


def save_json(path, data):
    path.write_text(json.dumps(data, indent=2) + "\n")


def restore(device, run_dir, before):
    """Attempt every restoration step, even if an earlier step fails."""
    errors = []
    commands = [("am", "force-stop", PACKAGE)]
    for key in KEYS:
        if before[key] == "null":
            commands.append(("settings", "delete", "global", key))
        else:
            commands.append(("settings", "put", "global", key, before[key]))
    commands.append(("setprop", PROPERTY, before[PROPERTY]))
    for command in commands:
        try:
            device.shell(*command)
        except (subprocess.SubprocessError, OSError) as error:
            errors.append(str(error))
    try:
        after = device.settings()
        save_json(run_dir / "settings-after.json", after)
        if after != before:
            errors.append("The device settings differ from their saved values.")
    except (subprocess.SubprocessError, OSError) as error:
        errors.append(str(error))
    if errors:
        recovery = shlex.join([sys.executable, str(Path(__file__).resolve()), "--restore", str(run_dir)])
        raise RuntimeError(
            "Device restoration needs attention. Reconnect the same device and run:\n"
            + recovery + "\n" + "\n".join(errors)
        )
    print("Device settings restored and verified.", flush=True)


def capture(workspace, layer, timeout):
    (workspace / "last-capture.txt").unlink(missing_ok=True)
    for path in (workspace / "workload/model.vgf", workspace / "workload/scenario.json", layer):
        if not path.is_file() or path.stat().st_size == 0:
            raise RuntimeError(f"Required file is missing or empty: {path}")
    scenario = json.loads((workspace / "workload/scenario.json").read_text())
    if "TEMPLATE_PATH" in json.dumps(scenario):
        raise RuntimeError("Remove tensor-file placeholders from scenario.json before capture.")
    serial = subprocess.check_output(["adb", "get-serialno"], text=True, timeout=30).strip()
    device = Device(serial)
    device.shell("run-as", PACKAGE, "id")
    run_name = "nx-" + str(time.time_ns())
    capture_name = "capture-" + run_name
    staging = "/data/local/tmp/" + run_name
    run_dir = workspace / "runs" / run_name
    run_dir.mkdir(parents=True)
    before = device.settings()
    save_json(run_dir / "settings-before.json", before)
    save_json(run_dir / "device.json", {
        "serial": serial,
        "model": device.shell("getprop", "ro.product.model"),
        "android_version": device.shell("getprop", "ro.build.version.release"),
    })
    print(f"Run directory: {run_dir}", flush=True)
    changed = False
    log_process = None
    try:
        device.adb("push", str(workspace / "workload"), staging)
        device.shell("chmod", "-R", "a+rX", staging)
        device.shell("run-as", PACKAGE, "mkdir", "-p", "files/" + run_name)
        device.shell("run-as", PACKAGE, "cp", "-r", staging + "/.", "files/" + run_name + "/")
        device.adb("push", str(layer), staging + "/libVkLayerNeuralStatistics.so")
        device.shell("chmod", "a+r", staging + "/libVkLayerNeuralStatistics.so")
        device.shell("run-as", PACKAGE, "cp", staging + "/libVkLayerNeuralStatistics.so", ".")
        settings = run_dir / "vk_layer_settings.txt"
        settings.write_text(
            f"lgl_neural_statistics.capture_folder = /data/data/{PACKAGE}/files/{capture_name}\n"
            "lgl_neural_statistics.statistics_mode = 1\n"
            "lgl_neural_statistics.dispatch_filter = 0\n"
        )
        settings_path = staging + "/vk_layer_settings.txt"
        device.adb("push", str(settings), settings_path)
        device.shell("chmod", "a+r", settings_path)
        changed = True
        device.shell("setprop", PROPERTY, settings_path)
        for key, value in zip(KEYS, ("1", PACKAGE, PACKAGE, "VK_LAYER_LGL_neural_statistics")):
            device.shell("settings", "put", "global", key, value)
        device.shell("am", "force-stop", PACKAGE)
        stamp = device.shell("date", "+%m-%d %H:%M:%S.000")
        log_path = run_dir / "logcat.txt"
        with log_path.open("wb") as log:
            log_process = subprocess.Popen(
                ["adb", "-s", serial, "logcat", "-v", "time", "-T", stamp, "-s",
                 "ScenarioService", "ScenarioRunner", "VkLayerNeuralStatistics", "vulkan", "AndroidRuntime"],
                stdout=log, stderr=subprocess.STDOUT,
            )
            device_dir = f"/data/data/{PACKAGE}/files/{run_name}"
            args = f"--scenario,{device_dir}/scenario.json,--output,{device_dir},--repeat,1,--log-level,debug"
            device.shell("am", "start-foreground-service", "-n", PACKAGE + "/.Main", "--esa", "args", args)
            deadline = time.monotonic() + timeout
            while time.monotonic() < deadline:
                text = log_path.read_text(errors="replace")
                if "runScenarioRunner failed" in text or "FATAL EXCEPTION" in text:
                    raise RuntimeError(f"Scenario Runner failed; inspect {log_path}")
                current = text.partition("arg=" + device_dir + "/scenario.json")[2]
                if "native exit code=" in current:
                    if "native exit code=0" not in current:
                        raise RuntimeError(f"Scenario Runner returned an error; inspect {log_path}")
                    break
                if log_process.poll() is not None:
                    raise RuntimeError(f"ADB logging stopped; inspect {log_path}")
                time.sleep(0.25)
            else:
                raise RuntimeError(f"Runner timed out after {timeout:g} seconds; inspect {log_path}")
        with (run_dir / "capture.tar").open("wb") as archive:
            device.adb("exec-out", "run-as", PACKAGE, "tar", "-C", "files", "-cf", "-", capture_name, stdout=archive)
        captures = workspace / "captures"
        captures.mkdir(exist_ok=True)
        with tarfile.open(run_dir / "capture.tar") as archive:
            archive.extractall(captures, filter="data")
        capture_root = captures / capture_name
        metadata = json.loads((capture_root / "capture.json").read_text())
        if metadata.get("status") != "complete" or metadata.get("capture", {}).get("statistics_mode") != 1:
            raise RuntimeError(f"Capture is incomplete or not mode 1; inspect {capture_root / 'capture.json'}")
        if not list(capture_root.rglob("statistics_mode1.bin")):
            raise RuntimeError(f"Capture has no mode-1 statistics: {capture_root}")
        if metadata.get("warnings"):
            raise RuntimeError(f"Review capture warnings before analysis: {metadata['warnings']}")
    finally:
        # Restore settings even if logging cleanup fails or capture is interrupted.
        try:
            if log_process is not None:
                log_process.terminate()
                log_process.wait(timeout=10)
        finally:
            if changed:
                restore(device, run_dir, before)
    (workspace / "last-capture.txt").write_text(str(capture_root) + "\n")
    print(f"Complete mode-1 capture: {capture_root}", flush=True)


def interrupted(signum, frame):
    raise KeyboardInterrupt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path, help="NX workspace containing workload/")
    parser.add_argument("--layer", type=Path, help="Android Arm64 libVkLayerNeuralStatistics.so")
    parser.add_argument("--timeout", type=float, default=120, help="Runner wait in seconds (default: 120)")
    parser.add_argument("--restore", type=Path, metavar="RUN_DIR", help="Retry restoring a saved run's device settings")
    args = parser.parse_args()
    if not shutil.which("adb"):
        parser.error("adb must be on PATH")
    signal.signal(signal.SIGTERM, interrupted)
    try:
        if args.restore:
            run_dir = args.restore.resolve()
            serial = json.loads((run_dir / "device.json").read_text())["serial"]
            before = json.loads((run_dir / "settings-before.json").read_text())
            restore(Device(serial), run_dir, before)
        else:
            if not args.workspace or not args.layer or args.timeout <= 0:
                parser.error("capture requires --workspace, --layer, and a positive --timeout")
            capture(args.workspace.resolve(), args.layer.resolve(), args.timeout)
    except KeyboardInterrupt:
        print("Capture interrupted. Check the restoration result above before using the device.", file=sys.stderr)
        return 130
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError, tarfile.TarError) as error:
        print(f"Error: {error}", file=sys.stderr)
        if isinstance(error, subprocess.CalledProcessError) and error.stderr:
            print(error.stderr.decode(errors="replace"), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
