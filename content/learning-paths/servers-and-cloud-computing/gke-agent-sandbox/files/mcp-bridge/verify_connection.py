#!/usr/bin/env python3
"""Initialize a real stdio MCP client and verify read-only access to the GKE claim."""

import argparse
import asyncio
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def verify(record_path):
    record = json.loads(record_path.read_text())
    parameters = StdioServerParameters(command=sys.executable,
                                      args=[str(Path(__file__).with_name("server.py")), "--record", str(record_path)],
                                      env=dict(os.environ))
    async with stdio_client(parameters) as (read, write):
        async with ClientSession(read, write, read_timeout_seconds=timedelta(seconds=180)) as session:
            initialized = await session.initialize()
            tools = await session.list_tools()
            names = sorted(tool.name for tool in tools.tools)
            expected = ["environment", "execute_command", "list_files", "read_file", "write_file"]
            if names != expected:
                raise RuntimeError(f"Unexpected MCP tool inventory: {names}")
            result = await session.call_tool("environment", {})
            if result.isError:
                raise RuntimeError(str(result.content))
            data = result.structuredContent
            if not data:
                data = json.loads(next(block.text for block in result.content if block.type == "text"))
            if (data["architecture"] not in {"aarch64", "arm64"} or data["uid"] != 1000
                    or data["binding"] != record["binding"] or data["workspace"] != record["workspace"]):
                raise RuntimeError(f"Unexpected GKE environment: {data}")
            evidence = {"utc": datetime.now(timezone.utc).isoformat(),
                        "initialization": initialized.model_dump(mode="json"),
                        "tools": names, "environment": data, "status": "passed"}
            (record_path.parent / "mcp-connection.json").write_text(json.dumps(evidence, indent=2) + "\n")
            print(f"MCP connected: {', '.join(names)}")
            print(f"GKE: {data['architecture']} UID {data['uid']}; Pod {data['binding']['pod']}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", required=True, type=Path)
    args = parser.parse_args()
    asyncio.run(verify(args.record.resolve()))


if __name__ == "__main__":
    main()
