---
title: Run the component and change its response
description: Start the wasmCloud development host, send HTTP requests to the running component, and modify the source to see changes take effect.
weight: 4
layout: learningpathall
---

## Start the application

This step uses two SSH terminals connected to the Arm server. `wash dev` runs
in the foreground and occupies the first terminal; you send requests from the
second.

In your first terminal, start the development host from the application
directory:

```bash
cd ~/wasmcloud-learning-path/hello-http
source "$HOME/.cargo/env"
wash dev
```

The output is similar to:

```output
INFO starting development session for project path="..."
INFO HTTP server listening addr=127.0.0.1:8000 protocol="HTTP"
INFO development session started, building and deploying component...
    Finished `release` profile [optimized] target(s) in 0.02s
INFO workload allowedHosts admits every host; set workload.allowedHosts in .wash/config.yaml to restrict outbound HTTP and socket connections
INFO listening for HTTP requests address=http://127.0.0.1:8000
```

Wait for the `listening for HTTP requests` line before continuing. Leave this terminal running.

## Send a request

Open a second SSH terminal connected to the same Graviton server. Send an HTTP
request to the loopback listener:

```bash
curl --noproxy '*' --fail --show-error -i http://127.0.0.1:8000/
printf '\n'
```

The output is similar to:

```output
HTTP/1.1 200 OK
transfer-encoding: chunked
date: Tue, 03 Nov 2026 18:31:16 GMT

hello from wasmCloud
```

Your request passed through the host's HTTP listener to the WebAssembly handler.
One application is loaded. That does not mean one guest instance must remain
alive for the entire server process: instance creation and reuse are runtime
policies, which you'll consider when interpreting performance.

## Change the application

Stop `wash dev` with Ctrl+C in the first terminal. In the application directory,
change the greeting in `src/lib.rs`:

```bash
cd ~/wasmcloud-learning-path/hello-http
sed -i 's/hello from wasmCloud/hello from Graviton/' src/lib.rs
wash dev
```

Wait for the listener message, then request it again from the second terminal:

```bash
curl --noproxy '*' --fail --show-error http://127.0.0.1:8000/
printf '\n'
```

The expected output is:

```output
hello from Graviton
```

This manual stop-and-restart cycle rebuilds and reloads the component.
`wash dev` in this version doesn't watch for file changes automatically.
Leave the modified application running for the performance exercise.

## Optional: view it from your computer

Run an SSH tunnel from your own computer, replacing the placeholders with your
key path and server address:

```bash
ssh -i /path/to/key.pem -N -L 8000:127.0.0.1:8000 ubuntu@SERVER_PUBLIC_IP
```

The command produces no output. It is forwarding traffic in the foreground.
Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your computer's browser. The tunnel forwards that
local port to the server's loopback listener. Close the tunnel with Ctrl+C when
finished.

## What you've accomplished

You have run a WebAssembly application on Graviton, verified its HTTP response,
and rebuilt it after changing its source. Next, measure the same running
application with a small set of HTTP tests.
