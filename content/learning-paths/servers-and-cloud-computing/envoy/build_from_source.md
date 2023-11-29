---
title: "Run Envoy as a service"
weight: 3
layout: "learningpathall"
---

### Run Envoy as a service

You will need to either create a config file or use a sample config to run Envoy as a service. 

Using a file editor of your choice,  copy the contents below into a sample config file `configs/config-http.yaml`:
```console
static_resources:
  listeners:
  - address:
      socket_address:
        address: 0.0.0.0
        port_value: 80
    filter_chains:
    - filters:
      - name: envoy.filters.network.http_connection_manager
        typed_config:
          '@type': type.googleapis.com/envoy.extensions.filters.network.http_connection_manager.v3.HttpConnectionManager
          codec_type: AUTO
          stat_prefix: ingress_http
          route_config:
            name: test
            virtual_hosts:
            - name: direct_response_service
              domains:
              - "*"
              routes:
              - match:
                  prefix: "/"
                direct_response:
                  status: 200
                  body:
                    inline_string: "[arm] hello world\n"
          http_filters:
          - name: envoy.filters.http.cors
            typed_config:
              '@type': type.googleapis.com/envoy.extensions.filters.http.cors.v3.Cors
          - name: envoy.filters.http.rbac
            typed_config:
              '@type': type.googleapis.com/envoy.extensions.filters.http.rbac.v3.RBAC
          - name: envoy.filters.http.local_ratelimit
            typed_config:
              '@type': type.googleapis.com/envoy.extensions.filters.http.local_ratelimit.v3.LocalRateLimit
              stat_prefix: http_local_rate_limiter
          - name: envoy.filters.http.fault
            typed_config:
              '@type': type.googleapis.com/envoy.extensions.filters.http.fault.v3.HTTPFault
          - name: envoy.filters.http.router
            typed_config:
              '@type': type.googleapis.com/envoy.extensions.filters.http.router.v3.Router
```

To run Envoy service, execute the following command:

```console
sudo bazel-bin/source/exe/envoy-static.stripped -c configs/config-http.yaml --concurrency 16 &

Where:
-c <string>,  --config-path <string>
        Path to configuration file
--concurrency <uint32_t>
        # of worker threads to run
```
Now run curl on localhost:

```console
curl localhost
```

The output from this command will look similar to:

```output
[arm] hello world
```

This demonstrates that Envoy is now successfully running.

