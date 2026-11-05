---
title: Understand and build the HTTP application
description: Inspect the WebAssembly HTTP handler source, understand its WIT interface, and build the component artifact with wash.
weight: 3
layout: learningpathall
---

## Get the application source

Download and extract the sample application archive, then move into the project directory:

```bash
cd ~/wasmcloud-learning-path
curl -fLO https://learn.arm.com/learning-paths/servers-and-cloud-computing/wasmcloud/_examples/hello-http.tar.gz
tar -xzf hello-http.tar.gz
cd hello-http
```

The archive includes source, rather than a precompiled application. You'll
build the component on your Graviton server.

## Understand the handler

Open `src/lib.rs`:

```bash
cat src/lib.rs
```

The handler implementation is:

```rust
impl Guest for Component {
    fn handle(_request: IncomingRequest, response_out: ResponseOutparam) {
        let response = OutgoingResponse::new(Fields::new());
        response.set_status_code(200).unwrap();
        let body = response.body().unwrap();
        ResponseOutparam::set(response_out, Ok(response));

        let stream = body.write().unwrap();
        stream.blocking_write_and_flush(b"hello from wasmCloud").unwrap();
        drop(stream);
        OutgoingBody::finish(body, None).unwrap();
    }
}
```

The function receives a request, creates an HTTP response with status 200, and
writes a fixed greeting to its body. It ignores the request contents. There is
no database, external network call, or substantial computation in the handler.

The surrounding `wit_bindgen::generate!` and `export!(Component)` statements
generate the bindings and export the implementation. WIT, the WebAssembly
Interface Types language, describes the interfaces between components and hosts.

Read the interface declaration:

```bash
cat wit/world.wit
```

The expected output is:

```output
package wasmcloud:http-handler-p2;

world http-handler-p2 {
    export wasi:http/incoming-handler@0.2.2;
}
```

This declares an incoming HTTP handler export. The component implements the
handler; it does not open the server's TCP listening port itself.

## Build the WebAssembly component

Inspect the `wash` configuration:

```bash
cat .wash/config.yaml
```

The expected output is:

```yaml
build:
  command: cargo build --target wasm32-wasip2 --release
  component_path: target/wasm32-wasip2/release/http_handler_p2.wasm
dev:
  address: "127.0.0.1:8000"
```

The build command selects the WebAssembly target and release profile. The
component path tells `wash` where to find the result. The development listener
uses loopback, so you do not need to open an HTTP port in the EC2 security group.

Build the application:

```bash
source "$HOME/.cargo/env"
rustup target add wasm32-wasip2
wash build
ls -lh target/wasm32-wasip2/release/http_handler_p2.wasm
```

The output is similar to:

```output
-rw-rw-r-- 2 ubuntu ubuntu 95K Nov  4 15:26 target/wasm32-wasip2/release/http_handler_p2.wasm
```

wash resolves the local WIT dependencies and runs the configured Cargo build.
The result is `http_handler_p2.wasm`. The first build also creates `Cargo.lock`;
retain it if you rebuild the application later.

Your `wash` executable is native Arm64 code. The application you just built is
a WebAssembly component, executed by the host. These are separate artifacts.

## What you've accomplished

You have read the handler, identified its HTTP interface, and built its `.wasm`
artifact. Next, load that artifact into the development host and send a request.
