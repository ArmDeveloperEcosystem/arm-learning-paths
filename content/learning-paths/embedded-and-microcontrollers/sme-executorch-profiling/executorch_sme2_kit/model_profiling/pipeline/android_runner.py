from __future__ import annotations

import re
import shlex
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

from .config import ExperimentConfig
from .runner_base import BaseRunner
from .util import ensure_path


@dataclass
class AndroidRunnerSettings:
    device_path: str = "/data/local/tmp/executorch"
    auto_push_runner: bool = True
    adb_binary: str = "adb"
    remote_device: Optional[str] = None  # e.g., "10.1.16.56:5555" for remote ADB connection


class AndroidRunner(BaseRunner):
    default_output_dir_name = "android"

    def __init__(self, settings: Optional[AndroidRunnerSettings] = None):
        super().__init__()
        self.settings = settings or AndroidRunnerSettings()
        # Connect to remote device if specified
        if self.settings.remote_device:
            self._connect_remote_device()

    def run_experiment(
        self,
        *,
        model: Path,
        output_root: Path,
        experiment: ExperimentConfig,
        threads: int,
        python: Path,
        verbose: bool = False,
    ) -> Dict[str, Path]:
        _ = python  # Python executable reserved for parity with other runners
        out_dir = self.resolve_output_dir(model, output_root)
        ensure_path(out_dir)
        prefix = f"{model.stem}_{experiment.name}_t{threads}"

        artifacts = self._build_artifact_paths(out_dir, prefix, experiment.mode)
        if experiment.mode == "xnntrace":
            log_path = artifacts["xnntrace_log"]
            etdump_name = None
        else:
            log_path = artifacts["latency_log"]
            etdump_name = artifacts["etdump"].name

        # push artifacts
        device_model = self._push_file(model)
        device_runner = None
        if experiment.runner_path:
            # Resolve runner path relative to executorch directory
            runner_path = self.resolve_runner_path(experiment.runner_path)
            device_runner = self._push_runner(runner_path, experiment.name)

        if experiment.mode == "timing":
            result = self._run_timing(
                device_runner=device_runner,
                device_model=device_model,
                threads=threads,
                runs=experiment.runs,
                warmup=experiment.warmup,
                log_path=log_path,
                etdump_name=etdump_name,
                extra_args=experiment.extra_args,
                cpu_affinity=experiment.cpu_affinity,
            )
        elif experiment.mode == "xnntrace":
            result = self._run_xnntrace(
                device_runner=device_runner,
                device_model=device_model,
                threads=threads,
                log_path=log_path,
                extra_args=experiment.extra_args,
                cpu_affinity=experiment.cpu_affinity,
            )
        else:
            raise ValueError(f"Unsupported experiment mode: {experiment.mode}")

        if etdump_name:
            etdump_path = artifacts.get("etdump")
            if etdump_path:
                artifacts["etdump"] = etdump_path if etdump_path.exists() else result.get("etdump")
        return artifacts

    def derive_artifact_paths(
        self,
        *,
        model: Path,
        output_root: Path,
        experiment: ExperimentConfig,
        threads: int,
    ) -> Dict[str, Path]:
        out_dir = self.resolve_output_dir(model, output_root)
        prefix = f"{model.stem}_{experiment.name}_t{threads}"
        return self._build_artifact_paths(out_dir, prefix, experiment.mode)

    # Internal helpers -------------------------------------------------
    def _connect_remote_device(self) -> None:
        """Connect to a remote Android device via ADB."""
        remote = self.settings.remote_device
        print(f"🔌 Connecting to remote device: {remote}", file=sys.stderr)
        
        # Check if device is already connected
        try:
            devices_result = subprocess.run(
                [self.settings.adb_binary, "devices"],
                check=True,
                text=True,
                capture_output=True,
            )
            if remote in devices_result.stdout and "device" in devices_result.stdout:
                print(f"✅ Device {remote} is already connected", file=sys.stderr)
                return
        except subprocess.CalledProcessError:
            pass  # Continue to connection attempt
        
        try:
            # Connect to the remote device
            result = subprocess.run(
                [self.settings.adb_binary, "connect", remote],
                check=True,
                text=True,
                capture_output=True,
            )
            output = result.stdout.strip()
            print(f"✅ {output}", file=sys.stderr)
            
            # Check if connection was successful
            if "connected" in output.lower() or "already connected" in output.lower():
                print(f"✅ Successfully connected to {remote}", file=sys.stderr)
            elif "unauthorized" in output.lower():
                print(
                    f"⚠️  WARNING: Device {remote} requires authorization. "
                    f"Please accept the authorization dialog on the device and try again.",
                    file=sys.stderr,
                )
                # Don't raise - let the user authorize and retry
            else:
                print(f"⚠️  WARNING: Connection status unclear: {output}", file=sys.stderr)
        except subprocess.CalledProcessError as e:
            error_msg = e.stderr.decode() if isinstance(e.stderr, bytes) else str(e.stderr)
            print(
                f"⚠️  WARNING: Failed to connect to remote device {remote}: {error_msg}",
                file=sys.stderr,
            )
            print(
                f"💡 Tip: Make sure the device is on the same network and ADB debugging is enabled.",
                file=sys.stderr,
            )
            # Don't raise - allow the pipeline to continue (might work if already connected)

    def _adb(self, args: List[str], *, capture: bool = False) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [self.settings.adb_binary, *args],
            check=True,
            text=True,
            capture_output=capture,
        )

    def _push_file(self, path: Path) -> str:
        dest = f"{self.settings.device_path}/{path.name}"
        self._adb(["push", str(path), dest])
        return path.name

    def _push_runner(self, runner_path: Path, experiment_name: str) -> str:
        # Generate unique runner name to avoid overwriting different runners
        # Format: executor_runner_{experiment_name}
        unique_name = f"executor_runner_{experiment_name}"
        dest = f"{self.settings.device_path}/{unique_name}"
        if self.settings.auto_push_runner:
            self._adb(["push", str(runner_path), dest])
            self._adb(["shell", f"chmod 755 {dest}"])
        return unique_name

    def _build_shell_command(self, binary: str, args: List[str], env: Optional[Dict[str, str]] = None, cpu_affinity: Optional[str] = None) -> str:
        exports = [f"export {k}={shlex.quote(v)}" for k, v in (env or {}).items()]
        run = "./" + binary
        cmd_parts = [f"cd {shlex.quote(self.settings.device_path)}", *exports]
        
        # Wrap with taskset if CPU affinity is specified
        if cpu_affinity:
            cmd_parts.append(f"taskset {cpu_affinity} {run} {' '.join(shlex.quote(a) for a in args)}")
        else:
            cmd_parts.append(f"{run} {' '.join(shlex.quote(a) for a in args)}")
        
        command = " && ".join(cmd_parts)
        return command

    def _run_timing(
        self,
        *,
        device_runner: Optional[str],
        device_model: str,
        threads: int,
        runs: int,
        warmup: int,
        log_path: Path,
        etdump_name: Optional[str],
        extra_args: List[str],
        cpu_affinity: Optional[str] = None,
    ) -> Dict[str, Path]:
        runner = device_runner or "executor_runner"
        if warmup > 0:
            warmup_cmd = [
                "--model_path",
                device_model,
                "--num_executions",
                str(warmup),
                "--cpu_threads",
                str(threads),
            ]
            try:
                self._adb(
                    [
                        "shell",
                        self._build_shell_command(runner, warmup_cmd, env={"LD_LIBRARY_PATH": self.settings.device_path}, cpu_affinity=cpu_affinity),
                    ]
                )
            except subprocess.CalledProcessError as e:
                # Warmup failed (e.g., segmentation fault), continue anyway
                # This allows us to still attempt timing runs even if warmup crashes
                print(
                    f"⚠️  WARNING: Warmup failed with exit code {e.returncode} (likely segmentation fault). "
                    f"Continuing with timing runs, but results may be invalid.",
                    file=sys.stderr,
                )

        exec_args = [
            "--model_path",
            device_model,
            "--num_executions",
            str(runs),
            "--cpu_threads",
            str(threads),
        ]
        if etdump_name:
            exec_args.extend(["--etdump_path", etdump_name])
        exec_args.extend(extra_args)

        env = {"LD_LIBRARY_PATH": self.settings.device_path, "XNN_LOG_LEVEL": "0"}
        shell_cmd = self._build_shell_command(runner, exec_args, env=env, cpu_affinity=cpu_affinity)
        start = time.perf_counter()
        runner_crashed = False
        stdout_text = ""
        try:
            proc = self._adb(["shell", shell_cmd], capture=True)
            elapsed = time.perf_counter() - start
            stdout_text = proc.stdout
            log_path.write_text(stdout_text)
        except subprocess.CalledProcessError as e:
            # Runner may have crashed (e.g., segmentation fault), but still try to get ETDump if it exists
            runner_crashed = True
            elapsed = time.perf_counter() - start
            if hasattr(e, 'stdout') and e.stdout:
                stdout_text = e.stdout
                log_path.write_text(e.stdout)
            else:
                log_path.write_text(f"Runner crashed with exit code {e.returncode}\n")
            print(
                f"⚠️  WARNING: Runner crashed with exit code {e.returncode} (likely segmentation fault). "
                f"ETDump timing data may still be valid, but model outputs are invalid.",
                file=sys.stderr,
            )
        
        # Check for NaN outputs in the log
        if stdout_text:
            nan_pattern = re.compile(r'\b-nan\b|\bnan\b', re.IGNORECASE)
            if nan_pattern.search(stdout_text):
                print(
                    f"⚠️  WARNING: Model produced NaN (Not a Number) outputs. "
                    f"This indicates invalid model execution (e.g., unnormalized inputs). "
                    f"ETDump timing data may still be valid, but model outputs are invalid.",
                    file=sys.stderr,
                )
        
        result = {"wall_time": elapsed}
        if etdump_name:
            local_etdump = log_path.parent / etdump_name
            # Try to pull ETDump even if runner crashed (it might have been created before crash)
            try:
                self._adb(["pull", f"{self.settings.device_path}/{etdump_name}", str(local_etdump)])
                if local_etdump.exists():
                    result["etdump"] = local_etdump
                    if runner_crashed:
                        print(
                            f"ℹ️  INFO: ETDump was successfully generated despite runner crash. "
                            f"Timing data should be valid.",
                            file=sys.stderr,
                        )
            except subprocess.CalledProcessError:
                # ETDump doesn't exist or couldn't be pulled
                if runner_crashed:
                    print(
                        f"❌ ERROR: Runner crashed and no ETDump was generated. "
                        f"No timing data available.",
                        file=sys.stderr,
                    )
        return result

    def _run_xnntrace(
        self,
        *,
        device_runner: Optional[str],
        device_model: str,
        threads: int,
        log_path: Path,
        extra_args: List[str],
        cpu_affinity: Optional[str] = None,
    ) -> Dict[str, Path]:
        runner = device_runner or "executor_runner"
        exec_args = [
            "--model_path",
            device_model,
            "--num_executions",
            "1",
            "--cpu_threads",
            str(threads),
        ]
        # Android xnntrace mode doesn't need --verbose-runner (uses device_runner directly)
        # extra_args are passed through as-is for any additional flags
        exec_args.extend(extra_args)
        env = {"LD_LIBRARY_PATH": self.settings.device_path, "XNN_LOG_LEVEL": "5"}
        shell_cmd = self._build_shell_command(runner, exec_args, env=env, cpu_affinity=cpu_affinity)
        
        # On Android, XNNPACK logs go to logcat, not stdout/stderr
        # We need to capture both stdout and logcat
        stdout_text = ""
        logcat_text = ""
        
        # Clear logcat buffer and start capturing in background
        logcat_tag = "XNNPACK"
        try:
            # Clear logcat buffer for our tag (ignore errors)
            try:
                self._adb(["logcat", "-c"])
            except subprocess.CalledProcessError:
                pass  # Ignore errors when clearing logcat
            
            # Run the command and capture stdout
            try:
                proc = self._adb(["shell", shell_cmd], capture=True)
                stdout_text = proc.stdout
            except subprocess.CalledProcessError as e:
                # Runner may have crashed, but still capture any output
                print(
                    f"⚠️  WARNING: XNNTrace runner crashed with exit code {e.returncode}. "
                    f"XNNPACK trace may be incomplete.",
                    file=sys.stderr,
                )
                if hasattr(e, 'stdout') and e.stdout:
                    stdout_text = e.stdout
                else:
                    stdout_text = f"Runner crashed with exit code {e.returncode}\n"
            
            # Capture logcat output for XNNPACK
            # Wait a bit for logs to flush, then capture
            time.sleep(0.5)  # Give time for logs to flush
            
            try:
                logcat_proc = self._adb(
                    ["logcat", "-d", "-s", logcat_tag], 
                    capture=True
                )
                logcat_text = logcat_proc.stdout if hasattr(logcat_proc, 'stdout') else ""
            except subprocess.CalledProcessError:
                # If logcat capture fails, continue without it
                logcat_text = ""
            except Exception:
                # If logcat capture fails, continue without it
                logcat_text = ""
            
        except Exception as e:
            print(
                f"⚠️  WARNING: Error during XNNTrace execution: {e}",
                file=sys.stderr,
            )
            stdout_text = f"Error: {e}\n"
        
        # Combine stdout and logcat into the log file
        combined_log = ""
        if logcat_text:
            combined_log += f"=== XNNPACK Logcat Output ===\n{logcat_text}\n\n"
        if stdout_text:
            combined_log += f"=== Runner stdout ===\n{stdout_text}\n"
        
        log_path.write_text(combined_log)
        
        # Check for NaN outputs in the log
        if stdout_text:
            nan_pattern = re.compile(r'\b-nan\b|\bnan\b', re.IGNORECASE)
            if nan_pattern.search(stdout_text):
                print(
                    f"⚠️  WARNING: Model produced NaN outputs during XNNTrace. "
                    f"This indicates invalid model execution.",
                    file=sys.stderr,
                )
        return {}
