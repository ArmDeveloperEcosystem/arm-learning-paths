#!/usr/bin/env python3

import argparse
import re
import shutil
import subprocess
from pathlib import Path


LIBPNG_REPOSITORY = "https://github.com/pnggroup/libpng.git"
LIBPNG_COMMIT = "a37d4836519517bdce6cb9d956092321eca3e73b"
TARGET_MACROS = {
    "ENABLE_MAGMA_FIXES": False,
    "MAGMA_ENABLE_CANARIES": False,
    "MAGMA_ENABLE_FIXES": False,
}

IFDEF = re.compile(r"^\s*#\s*(ifdef|ifndef)\s+(\w+)\s*$")
IF = re.compile(r"^\s*#\s*if\s+defined\s*\(\s*(\w+)\s*\)\s*$")
ELSE = re.compile(r"^\s*#\s*else\b")
ELIF = re.compile(r"^\s*#\s*elif\b")
ENDIF = re.compile(r"^\s*#\s*endif\b")
ANY_IF = re.compile(r"^\s*#\s*(if|ifdef|ifndef)\b")


def run(*command: str, cwd: Path | None = None, input_text: str | None = None) -> None:
    subprocess.run(
        command,
        cwd=cwd,
        input=input_text,
        text=True,
        check=True,
    )


def sanitize_file(path: Path) -> None:
    lines = path.read_text(errors="surrogateescape").splitlines(keepends=True)
    output: list[str] = []
    stack: list[dict[str, object]] = []
    emitting = True

    for line_number, line in enumerate(lines, start=1):
        match = IFDEF.match(line)
        if match and match.group(2) in TARGET_MACROS:
            directive, macro = match.groups()
            condition = TARGET_MACROS[macro]
            if directive == "ifndef":
                condition = not condition
            stack.append(
                {
                    "targeted": True,
                    "parent_emitting": emitting,
                    "condition": condition,
                    "else_seen": False,
                }
            )
            emitting = emitting and condition
            continue

        match = IF.match(line)
        if match and match.group(1) in TARGET_MACROS:
            condition = TARGET_MACROS[match.group(1)]
            stack.append(
                {
                    "targeted": True,
                    "parent_emitting": emitting,
                    "condition": condition,
                    "else_seen": False,
                }
            )
            emitting = emitting and condition
            continue

        if ANY_IF.match(line):
            stack.append({"targeted": False})
            if emitting:
                output.append(line)
            continue

        if ELSE.match(line):
            if not stack:
                raise RuntimeError(f"unmatched #else in {path}:{line_number}")
            frame = stack[-1]
            if frame["targeted"]:
                if frame["else_seen"]:
                    raise RuntimeError(f"duplicate #else in {path}:{line_number}")
                frame["else_seen"] = True
                emitting = bool(frame["parent_emitting"]) and not bool(
                    frame["condition"]
                )
            elif emitting:
                output.append(line)
            continue

        if ELIF.match(line):
            if stack and stack[-1]["targeted"]:
                raise RuntimeError(
                    f"targeted #elif is unsupported in {path}:{line_number}"
                )
            if emitting:
                output.append(line)
            continue

        if ENDIF.match(line):
            if not stack:
                raise RuntimeError(f"unmatched #endif in {path}:{line_number}")
            frame = stack.pop()
            if frame["targeted"]:
                emitting = bool(frame["parent_emitting"])
            elif emitting:
                output.append(line)
            continue

        if emitting:
            output.append(line)

    if stack:
        raise RuntimeError(f"unterminated conditional in {path}")

    path.write_text("".join(output), errors="surrogateescape")


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prepare the sanitized Magma libpng target for Metis review."
    )
    parser.add_argument(
        "--magma-dir",
        type=Path,
        required=True,
        help="Path to a cloned HexHive/magma repository.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
        help="Destination for the prepared libpng source tree.",
    )
    return parser.parse_args()


def main() -> None:
    arguments = parse_arguments()
    magma_dir = arguments.magma_dir.resolve()
    output_dir = arguments.output_dir.resolve()
    patch_dir = magma_dir / "targets" / "libpng" / "patches" / "bugs"

    if not patch_dir.is_dir():
        raise SystemExit(f"Magma libpng patches not found: {patch_dir}")
    if output_dir.exists():
        raise SystemExit(f"Output directory already exists: {output_dir}")

    run("git", "clone", LIBPNG_REPOSITORY, str(output_dir))
    run("git", "checkout", LIBPNG_COMMIT, cwd=output_dir)

    patch_files = sorted(patch_dir.glob("*.patch"))
    for patch_file in patch_files:
        patch_text = patch_file.read_text().replace(
            "%MAGMA_BUG%", patch_file.stem
        )
        run("patch", "-p1", cwd=output_dir, input_text=patch_text)

    for path in output_dir.rglob("*"):
        if path.is_file() and path.suffix.lower() in {
            ".c",
            ".cc",
            ".cpp",
            ".cxx",
            ".h",
            ".hpp",
        }:
            sanitize_file(path)

    for pattern in ("*.orig", "*.rej"):
        for path in output_dir.rglob(pattern):
            path.unlink()

    (output_dir / ".metis.md").write_text(
        "# Project security context\n\n"
        "This library parses PNG files supplied by untrusted users. Treat image "
        "dimensions, chunk lengths, offsets, and compressed data as "
        "attacker-controlled. Review memory safety, integer arithmetic, parser "
        "state, resource exhaustion, and cleanup on error paths.\n"
    )
    (output_dir / ".metisignore").write_text(
        ".git/\ncontrib/\ndocs/\nexamples/\nscripts/\ntests/\n"
    )

    print(f"Prepared libpng commit {LIBPNG_COMMIT}")
    print(f"Applied {len(patch_files)} Magma vulnerability-introducing patches")
    print(f"Output: {output_dir}")


if __name__ == "__main__":
    main()
