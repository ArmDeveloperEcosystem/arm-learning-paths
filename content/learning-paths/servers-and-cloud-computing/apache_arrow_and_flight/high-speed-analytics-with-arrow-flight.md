---
title: High-Speed Analytics with Apache Arrow Flight on Arm64
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## High-Speed Analytics with Apache Arrow Flight

In this section, you deploy Apache Arrow Flight, a high-performance RPC framework designed for analytics workloads. Arrow Flight enables zero-copy, memory-to-memory data transfer over gRPC, making it ideal for distributed analytics engines.

Arrow Flight enables **zero-copy, memory-to-memory data transfer over gRPC**, allowing analytical data to be shared between processes and systems without serialization overhead. This makes it ideal for distributed analytics engines, interactive query systems, and real-time data pipelines.

This section demonstrates how Arrow Flight works on Arm64 (Axion) using a simple **server–client setup on the same VM.**

## Architecture Overview

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

## Start Arrow Flight Server (Same Machine)
In this step, you create an Arrow Flight server that exposes an in-memory Arrow table to clients over gRPC.

Create a file named `flight_server.py`.


```pyhton
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

## Connect Using Arrow Flight Client (Same VM)
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

## What You Have Learned

Across this learning path, you have learned:

- How Apache Arrow works on Arm64 (Axion)
- How Parquet and ORC datasets are written and read from object storage
- How MinIO acts as S3-compatible storage for analytics
- How the Arrow Dataset API enables predicate pushdown and column pruning
- How Arrow Flight enables high-speed, memory-to-memory data transfer
- How all components work together on a single Arm64 VM
