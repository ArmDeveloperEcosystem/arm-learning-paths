---
title: Run baseline Envoy testing on a Google Axion C4A Arm VM
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Validate Envoy installation with a baseline test

With Envoy installed successfully on your GCP C4A Arm virtual machine, you can now validate that Envoy is running as expected.

In this section, you will do the following:

- Create a minimal Envoy config
- Start Envoy with it with config
- Verify functionality using `curl`

The test confirms the following:

- Envoy listens on port **10000**
- Forwards requests to `httpbin.org`
- Returns a **200 OK** response

## Create a minimal configuration file

Using a text editor, create a file named `envoy_config.yaml` and add the following content as shown below. 

```yaml
static_resources:
  listeners:
  - name: listener_0
    address:
      socket_address:
        protocol: TCP
        address: 0.0.0.0
        port_value: 10000
    filter_chains:
    - filters:
      - name: envoy.filters.network.http_connection_manager
        typed_config:
          "@type": type.googleapis.com/envoy.extensions.filters.network.http_connection_manager.v3.HttpConnectionManager
          stat_prefix: ingress_http
          route_config:
            name: local_route
            virtual_hosts:
            - name: backend
              domains: ["*"]
              routes:
              - match:
                  prefix: "/"
                route:
                  cluster: service_httpbin
                  host_rewrite_literal: httpbin.org
          http_filters:
          - name: envoy.filters.http.router
            typed_config:
              "@type": type.googleapis.com/envoy.extensions.filters.http.router.v3.Router
  clusters:
  - name: service_httpbin
    connect_timeout: 0.5s
    type: LOGICAL_DNS
    dns_lookup_family: V4_ONLY
    lb_policy: ROUND_ROBIN
    load_assignment:
      cluster_name: service_httpbin
      endpoints:
      - lb_endpoints:
        - endpoint:
            address:
              socket_address:
                address: httpbin.org
                port_value: 80
```

## Explanatory notes on the configuration

This configures Envoy to listen on port **10000** and forward all traffic to `http://httpbin.org`. The `host_rewrite_literal` is required to prevent `404 Not Found` from the upstream server.

- **Listeners:** Envoy accepts incoming HTTP requests on port **10000** of your VM.
- **HTTP Connection Manager:** Processes incoming requests, and applies routing.
- **Routing:** All traffic is routed to the `service_httpbin` cluster, with the `Host` header rewritten to  `httpbin.org`.
- **Clusters:** The `service_httpbin` cluster defines the upstream as `httpbin.org:80`.

## Run and test Envoy

This is the final phase of functional validation, confirming that the proxy is operational.
Start the Envoy proxy using your configuration file:

```console
envoy -c envoy_config.yaml --base-id 1
```
The output should look similar to:

```output
[2025-08-21 11:53:51.597][67137][info][config] [source/server/configuration_impl.cc:138] loading 1 listener(s)
[2025-08-21 11:53:51.597][67137][info][config] [source/server/configuration_impl.cc:154] loading stats configuration
[2025-08-21 11:53:51.598][67137][warning][main] [source/server/server.cc:928] There is no configured limit to the number of allowed active downstream connections. Configure a limit in `envoy.resource_monitors.downstream_connections` resource monitor.
[2025-08-21 11:53:51.598][67137][info][main] [source/server/server.cc:969] starting main dispatch loop
[2025-08-21 11:53:51.599][67137][info][runtime] [source/common/runtime/runtime_impl.cc:614] RTDS has finished initialization
[2025-08-21 11:53:51.599][67137][info][upstream] [source/common/upstream/cluster_manager_impl.cc:240] cm init: all clusters initialized
[2025-08-21 11:53:51.599][67137][info][main] [source/server/server.cc:950] all clusters initialized. initializing init manager
[2025-08-21 11:53:51.599][67137][info][config] [source/common/listener_manager/listener_manager_impl.cc:930] all dependencies initialized. starting workers
```

Leave this terminal running. In a new terminal, send a test request to the Envoy listener using `curl`:

```console
curl -v http://localhost:10000/get
```
The `-v` flag provides verbose output, showing the full request and response headers. A successful test will show a **HTTP/1.1 200 OK** response with a JSON body from `httpbin.org`.

A successful test shows HTTP/1.1 200 OK with a JSON body from httpbin.org, for example:

```output
*   Trying 127.0.0.1:10000...
* Connected to 127.0.0.1 (127.0.0.1) port 10000 (#0)
> GET /get HTTP/1.1
> Host: 127.0.0.1:10000
> User-Agent: curl/7.76.1
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< date: Fri, 22 Aug 2025 11:20:35 GMT
< content-type: application/json
< content-length: 301
< server: envoy
< access-control-allow-origin: *
< access-control-allow-credentials: true
< x-envoy-upstream-service-time: 1042
<
{
  "args": {},
  "headers": {
    "Accept": "*/*",
    "Host": "httpbin.org",
    "User-Agent": "curl/7.76.1",
    "X-Amzn-Trace-Id": "Root=1-68a85282-10af9cfe0385774600509ddd",
    "X-Envoy-Expected-Rq-Timeout-Ms": "15000"
  },
  "origin": "34.63.220.63",
  "url": "http://httpbin.org/get"
}
* Connection #0 to host 127.0.0.1 left intact
```
## Summary of the curl output

- **Successful connection:** The `curl` command successfully connected to the Envoy proxy on `localhost:10000`.
- **Correct status code:** Envoy forwards the request and receives a successful `200 OK` response from the upstream.
- **Host header rewrite:** Envoy rewrites `Host` to `httpbin.org` as configured.
- **End-to-end Success:** The proxy is operational; requests are received, processed, and forwarded to the backend.

To stop Envoy in the first terminal, press **Ctrl+C**. This confirms the end-to-end flow with Envoy server is working correctly.
