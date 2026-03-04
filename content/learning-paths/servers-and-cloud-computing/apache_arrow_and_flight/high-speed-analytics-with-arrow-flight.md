---
title: Run high-speed analytics with Apache Arrow Flight on arm64
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run high-speed analytics with Apache Arrow Flight

In this section, you deploy Apache Arrow Flight, a high-performance RPC framework designed for analytics workloads. Arrow Flight enables zero-copy, memory-to-memory data transfer over gRPC, making it ideal for distributed analytics engines.

Arrow Flight enables **zero-copy, memory-to-memory data transfer over gRPC**, allowing analytical data to be shared between processes and systems without serialization overhead. This makes it ideal for distributed analytics engines, interactive query systems, and real-time data pipelines.

This section demonstrates how Arrow Flight works on arm64 (Axion) using a simple server-client setup on the same virtual machine.

## Architecture overview

```text
Arrow Table (In-Memory)
        |
        v
Arrow Flight Server (gRPC)
        |
        v
Arrow Flight Client
```

**What this architecture shows:**

- Data remains in Arrow’s in-memory columnar format
- gRPC is used as the transport layer
- No intermediate files or object storage are involved
- Data is transferred efficiently with minimal CPU overhead

## Start Arrow Flight server on the same virtual machine

In this step, you create an Arrow Flight server that exposes an in-memory Arrow table to clients over gRPC.

Create a file named `flight_server.py`.


```python
import pyarrow as pa
import pyarrow.flight as flight

class ArrowFlightServer(flight.FlightServerBase):
    def __init__(self, location):
        super().__init__(location)
        self.table = pa.table({
            "id": list(range(1000)),
            "value": [i * 10 for i in range(1000)]
        })

    def do_get(self, context, ticket):
        return flight.RecordBatchStream(self.table)

if __name__ == "__main__":
    server = ArrowFlightServer("grpc://0.0.0.0:8815")
    print("Arrow Flight server running on port 8815")
    server.serve()
```

### Run the server

```bash
source arrow-venv/bin/activate
python flight_server.py
```

This terminal will block — this indicates the server is running and listening for client connections.

The output is similar to:

```output
(arrow-venv) gcpuser@arrow-flight:~> python flight_server.py
Arrow Flight server running on port 8815
```

### Verify server is running

Open another terminal on the same VM and check that the gRPC port is listening.

```bash
ss -lntp | grep 8815
```

If you see a listening process, the server is up.

The output is similar to:

```output
ss -lntp | grep 8815
LISTEN 0      4096               *:8815             *:*    users:(("python",pid=4255,fd=7))
```

## Connect using an Arrow Flight client on the same virtual machine

Now you connect to the Arrow Flight server using a client and retrieve the in-memory dataset.

Create a file named `flight_client.py`.

```python
import pyarrow.flight as flight

client = flight.FlightClient("grpc://127.0.0.1:8815")

reader = client.do_get(flight.Ticket(b"dataset"))
table = reader.read_all()

print(table.schema)
print("Rows:", table.num_rows)
```

### Run it

```bash
source arrow-venv/bin/activate
python flight_client.py
```

The output is similar to:

```output
id: int64
value: int64
Rows: 1000
```

**What this demonstrates:**

- The client successfully connected over gRPC
- Data was transferred directly from server memory
- Arrow’s columnar format was preserved end-to-end

## What you've accomplished and what's next

In this section, you:

- Started an Arrow Flight server that streams an in-memory Arrow table over gRPC
- Connected a client to the Flight endpoint and read data without file serialization
- Validated end-to-end transfer using Arrow's columnar in-memory format

Next, review the Learning Path summary and continue with related Arm server analytics content in the next steps page.
