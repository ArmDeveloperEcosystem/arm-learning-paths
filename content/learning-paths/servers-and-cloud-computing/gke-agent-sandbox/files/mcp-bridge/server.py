#!/usr/bin/env python3
"""Expose a fixed, launcher-owned GKE task workspace over stdio MCP."""

import argparse
from pathlib import Path

from mcp.server.fastmcp import FastMCP
from bridge import Bridge


def build_server(bridge):
    server = FastMCP("gke-sandbox", instructions="Use these tools for all task files and execution. "
                     "They operate in one claimed Arm gVisor Pod; paths are relative to its workspace.")

    @server.tool()
    def environment() -> dict:
        """Inspect the claim-bound GKE workspace, Arm architecture, UID, and Python version."""
        return bridge.invoke("environment")

    @server.tool()
    def execute_command(command: str, cwd: str = ".", timeout: int = 30) -> dict:
        """Run a shell command INSIDE the GKE Pod, never on the client. Timeout: 1–30 seconds.

        Return stdout, stderr, exit code, timeout and output truncation flags. Check them before
        reporting success. The shell starts in the remote task workspace, or a relative cwd.
        """
        return bridge.invoke("execute_command", command=command, cwd=cwd, timeout=timeout)

    @server.tool()
    def write_file(path: str, content: str) -> dict:
        """Write a UTF-8 task file in GKE (max 256 KiB); use a workspace-relative path."""
        return bridge.invoke("write_file", path=path, content=content)

    @server.tool()
    def read_file(path: str) -> dict:
        """Read a UTF-8 task file from GKE (max 256 KiB); use a workspace-relative path."""
        return bridge.invoke("read_file", path=path)

    @server.tool()
    def list_files(path: str = ".") -> dict:
        """List up to 200 entries in a remote task directory; use a workspace-relative path."""
        return bridge.invoke("list_files", path=path)

    return server


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", required=True, type=Path)
    args = parser.parse_args()
    build_server(Bridge(args.record)).run(transport="stdio")


if __name__ == "__main__":
    main()
