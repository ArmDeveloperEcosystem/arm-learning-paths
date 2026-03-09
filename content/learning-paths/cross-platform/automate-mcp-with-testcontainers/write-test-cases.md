---
title: Write integration tests for MCP servers
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understanding MCP communication

MCP servers communicate using JSON-RPC 2.0 over standard input/output (stdio transport). Each request is a JSON object followed by a newline, and the server responds with a JSON object on stdout.

The communication follows this pattern:

1. Client sends an `initialize` request with protocol version and capabilities.
2. Server responds with its capabilities and server info.
3. Client sends an `initialized` notification.
4. Client can now invoke tools using `tools/call` method.

## Create the constants file

Start by defining the test constants in `constants.py`. This file contains the MCP request payloads and expected responses:

```python
MCP_DOCKER_IMAGE = "arm-mcp:latest"

INIT_REQUEST = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "protocolVersion": "2024-11-05",
        "capabilities": {},
        "clientInfo": {"name": "pytest", "version": "0.1"},
    },
}

CHECK_IMAGE_REQUEST = {
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/call",
    "params": {
        "name": "check_image",
        "arguments": {
            "image": "ubuntu:24.04",
            "invocation_reason": (
                "Checking ARM architecture compatibility for ubuntu:24.04 "
                "container image as requested by the user"
            ),
        },
    },
}

EXPECTED_CHECK_IMAGE_RESPONSE = {
    "status": "success",
    "message": "Image ubuntu:24.04 supports all required architectures",
    "architectures": [
        "amd64", "unknown", "arm", "unknown", "arm64", "unknown",
        "ppc64le", "unknown", "riscv64", "unknown", "s390x", "unknown",
    ],
}
```

Add more test requests for other MCP tools:

```python
CHECK_NGINX_REQUEST = {
    "jsonrpc": "2.0",
    "id": 4,
    "method": "tools/call",
    "params": {
        "name": "knowledge_base_search",
        "arguments": {
            "query": "nginx performance tweaks",
        },
    },
}

EXPECTED_CHECK_NGINX_RESPONSE = [
    "https://learn.arm.com/learning-paths/servers-and-cloud-computing/nginx_tune/tune_static_file_server",
    "https://learn.arm.com/learning-paths/servers-and-cloud-computing/nginx_tune/test_optimizations",
]
```

## Create helper functions for MCP communication

The MCP server runs inside a Docker container that communicates over an attached socket. Create helper functions to encode and decode MCP messages:

```python
import json
import time

def _encode_mcp_message(payload: dict) -> bytes:
    """Encode an MCP message for stdio transport."""
    return (json.dumps(payload) + "\n").encode("utf-8")


def _read_docker_frame(sock, timeout: float) -> bytes:
    """Read a Docker multiplexed frame from the socket."""
    deadline = time.time() + timeout
    header = b""
    while len(header) < 8:
        if time.time() > deadline:
            raise TimeoutError("Timed out waiting for docker frame header.")
        chunk = sock.recv(8 - len(header))
        if not chunk:
            time.sleep(0.01)
            continue
        header += chunk

    # Docker frame format: 8-byte header
    # byte 0: stream type (0x01 = stdout, 0x02 = stderr)
    # bytes 1-3: Reserved (\x00\x00\x00)
    # bytes 4-7: Payload size (big-endian uint32)
    if header[1:4] != b"\x00\x00\x00":
        return header  # Raw/unframed output

    size = int.from_bytes(header[4:8], "big")
    payload = b""
    while len(payload) < size:
        if time.time() > deadline:
            raise TimeoutError("Timed out waiting for docker frame payload.")
        chunk = sock.recv(size - len(payload))
        if not chunk:
            time.sleep(0.01)
            continue
        payload += chunk
    return payload


def _read_mcp_message(sock, timeout: float = 10.0) -> dict:
    """Read and parse an MCP JSON-RPC message."""
    deadline = time.time() + timeout
    buffer = b""
    while True:
        if time.time() > deadline:
            raise TimeoutError("Timed out waiting for MCP response line.")
        frame = _read_docker_frame(sock, timeout)
        buffer += frame
        while b"\n" in buffer:
            line, buffer = buffer.split(b"\n", 1)
            if not line:
                continue
            try:
                return json.loads(line.decode("utf-8"))
            except json.JSONDecodeError:
                idx = line.find(b"{")
                if idx != -1:
                    try:
                        return json.loads(line[idx:].decode("utf-8"))
                    except json.JSONDecodeError:
                        continue
```

## Write the main test function

Create the main test function in `test_mcp.py` that uses testcontainers to manage the MCP server lifecycle:

```python
import os
from pathlib import Path
import pytest
from testcontainers.core.container import DockerContainer
from testcontainers.core.waiting_utils import wait_for_logs
import constants

def test_mcp_stdio_transport_responds():
    image = os.getenv("MCP_IMAGE", constants.MCP_DOCKER_IMAGE)
    repo_root = Path(__file__).resolve().parents[1]
    
    with (
        DockerContainer(image)
        .with_volume_mapping(str(repo_root), "/workspace")
        .with_kwargs(stdin_open=True, tty=False)
    ) as container:
        # Wait for MCP server to start
        wait_for_logs(container, "Starting MCP server", timeout=60)
        
        # Attach to container stdin/stdout
        socket_wrapper = container.get_wrapped_container().attach_socket(
            params={"stdin": 1, "stdout": 1, "stderr": 1, "stream": 1}
        )
        raw_socket = socket_wrapper._sock
        raw_socket.settimeout(10)

        # Initialize MCP session
        raw_socket.sendall(_encode_mcp_message(constants.INIT_REQUEST))
        response = _read_mcp_message(raw_socket, timeout=20)

        # Verify initialization
        assert response.get("id") == 1
        assert "result" in response
        assert "serverInfo" in response["result"]
        
        # Send initialized notification
        raw_socket.sendall(
            _encode_mcp_message({
                "jsonrpc": "2.0", 
                "method": "initialized", 
                "params": {}
            })
        )
```

## Add tool-specific tests

Extend the test function to verify individual MCP tools:

```python
        def _read_response(expected_id: int, timeout: float = 10.0) -> dict:
            """Helper to read a specific response by ID."""
            deadline = time.time() + timeout
            while time.time() < deadline:
                message = _read_mcp_message(raw_socket, timeout=timeout)
                if message.get("id") == expected_id:
                    return message
            raise TimeoutError(f"Timed out waiting for response id={expected_id}.")

        # Test check_image tool
        raw_socket.sendall(_encode_mcp_message(constants.CHECK_IMAGE_REQUEST))
        check_image_response = _read_response(2, timeout=60)
        assert check_image_response.get("result")["structuredContent"] == \
            constants.EXPECTED_CHECK_IMAGE_RESPONSE

        # Test knowledge_base_search tool
        raw_socket.sendall(_encode_mcp_message(constants.CHECK_NGINX_REQUEST))
        check_nginx_response = _read_response(4, timeout=60)
        urls = json.dumps(check_nginx_response["result"]["structuredContent"])
        assert any(
            expected in urls 
            for expected in constants.EXPECTED_CHECK_NGINX_RESPONSE
        )
```

## Run the tests

Execute the test suite using pytest:

```bash
python -m pytest -v mcp-local/tests/test_mcp.py
```

The output shows each test assertion:

```output
============================= test session starts ==============================
platform linux -- Python 3.11.0, pytest-8.0.0
collected 1 item

mcp-local/tests/test_mcp.py::test_mcp_stdio_transport_responds PASSED    [100%]

============================== 1 passed in 45.32s ==============================
```

For more verbose output that shows the test progress:

```bash
python -m pytest -s mcp-local/tests/test_mcp.py
```

The `-s` flag displays print statements, showing each tool test as it completes.

## How Testcontainers handle container lifecycle

The `with DockerContainer(image) as container` pattern:

1. Pulls the image if not present locally.
2. Creates and starts a new container.
3. Waits for the "Starting MCP server" log message.
4. Yields the container for your test code.
5. Automatically stops and removes the container when the test completes.

This ensures every test run starts with a clean environment.

## What you've accomplished and what's next

In this section:
- You learned how MCP servers communicate using JSON-RPC over stdio.
- You created helper functions to handle Docker socket communication.
- You wrote integration tests that verify MCP tool responses.
- You ran the test suite locally using pytest.

In the next section, you will configure GitHub Actions to run these tests automatically in your CI/CD pipeline.
