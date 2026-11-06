---
title: Run the component and change its response
description: Start the wasmCloud development host, send HTTP requests to the running component, and modify the source to see changes take effect.
weight: 4
layout: learningpathall
---

## Start the application

Now that you've built the application, you can start it.

You'll use two SSH terminals connected to the Arm server. You'll run `wash dev`
in the foreground in the first terminal. You'll send requests from the
second terminal.

In the first terminal, start the development host from the application
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

## Send an HTTP request and receive a response

In the second terminal, send an HTTP
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

Your request passed through the host HTTP listener to the WebAssembly handler.
One application is loaded. This doesn't mean that one guest instance needs to remain
alive for the entire server process. Instance creation and reuse are runtime
policies that you'll consider when interpreting performance.

## Change the application and receive an updated response

Stop `wash dev` with **Ctrl+C** in the first terminal. 

Then, in the application directory, change the greeting in `src/lib.rs`:

```bash
cd ~/wasmcloud-learning-path/hello-http
sed -i 's/hello from wasmCloud/hello from Graviton/' src/lib.rs
wash dev
```

Wait for the listener message, then send an HTTP request again from the second terminal:

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

## (Optional) View the response from your computer

Run an SSH tunnel from your own computer, replacing the placeholders with your
key path and server address:

```bash
ssh -i /path/to/key.pem -N -L 8000:127.0.0.1:8000 ubuntu@SERVER_PUBLIC_IP
```

The command produces no output. It's forwarding traffic in the foreground.

Open the [local HTTP endpoint](http://127.0.0.1:8000/) in a browser on your computer. The tunnel forwards that
local port to the server loopback listener. Close the tunnel with **Ctrl+C** when
finished.

## What you've accomplished and what's next

You've run a WebAssembly application on Graviton and verified its HTTP response. Then, you rebuilt the application after changing its source and received an updated response. 

Next, you'll measure the same running application with a small set of HTTP tests.
