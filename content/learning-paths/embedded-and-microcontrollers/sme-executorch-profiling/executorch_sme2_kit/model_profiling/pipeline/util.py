from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from typing import Iterable, Sequence


def ensure_path(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def run_subprocess(
    cmd: Sequence[str],
    cwd: Path | None = None,
    check: bool = True,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        list(cmd),
        cwd=str(cwd) if cwd else None,
        check=check,
        text=True,
    )


def find_python_executable() -> Path:
    for candidate in ("python", "python3"):
        path = shutil.which(candidate)
        if path:
            return Path(path)
    raise RuntimeError("No Python interpreter found in PATH.")
