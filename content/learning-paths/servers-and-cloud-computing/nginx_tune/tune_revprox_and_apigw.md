---
title: Tune an NGINX reverse proxy or API gateway for performance on Arm 
description: Tune NGINX reverse proxy and API gateway directives for Arm-based platforms so upstream keepalive, rewrites, and caching decisions match your workload.
weight: 5
layout: "learningpathall"
---

## NGINX reverse proxy and API gateway configuration

You'll now review a tuned configuration based on the configuration in the [set up a reverse proxy and API gateway](/learning-paths/servers-and-cloud-computing/nginx/reverse_proxy_and_api_gateway/) section of the [Learn how to deploy NGINX](/learning-paths/servers-and-cloud-computing/nginx/) Learning Path. 

Use this example configuration as a starting point, then size each directive for your workload and validate the result with repeatable measurements.

### Top-level nginx.conf

Use the same top-level configuration from [Tune a static file server](/learning-paths/servers-and-cloud-computing/nginx_tune/tune_static_file_server/).

### Tuned reverse proxy and API gateway configuration

The following is a tuned configuration (`/etc/nginx/conf.d/loadbalancer.conf`):

```nginx
# Upstreams for https
upstream ssl_file_server_com {
  server <fileserver_1_ip_or_dns>:443;
  server <fileserver_2_ip_or_dns>:443;
  keepalive 1024;
}

# HTTPS reverse proxy and API gateway
server {
  listen 443 ssl reuseport backlog=65535;
  root /usr/share/nginx/html;
  index index.html index.htm;
  server_name $hostname;

  ssl_certificate /etc/nginx/ssl/ecdsa.crt;
  ssl_certificate_key /etc/nginx/ssl/ecdsa.key;
  ssl_ciphers ECDHE-ECDSA-AES256-GCM-SHA384;

  # API gateway path
  location ~ ^/api_old/.*$ {
    limit_except GET {
      deny all;
    }
    rewrite ^/api_old/(.*)$ /api_new/$1 last;
  }
  location /api_new {
    internal;
    proxy_pass https://ssl_file_server_com;
    proxy_http_version 1.1;
    proxy_set_header Connection "";
  }

  # Reverse proxy path
  location / {
    limit_except GET {
      deny all;
    }
    proxy_pass https://ssl_file_server_com;
    proxy_http_version 1.1;
    proxy_set_header Connection "";
  }
}
```

The following are performance-relevant directives that weren't described in the [static file server section](/learning-paths/servers-and-cloud-computing/nginx_tune/tune_static_file_server/):

- [`keepalive`](https://nginx.org/en/docs/http/ngx_http_upstream_module.html#keepalive): Controls the cache of idle connections to upstream servers. For NGINX 1.29.7 and later, upstream keepalive is enabled by default with a small cache. Set `keepalive` explicitly when you want to tune the upstream idle connection cache for your workload.

  For older NGINX versions, enable upstream keepalive with the `keepalive` directive. Also set [`proxy_http_version`](https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_http_version) to `1.1` and clear the `Connection` header with [`proxy_set_header`](https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_set_header).
  
  The value `1024` is a cache size for idle upstream connections per worker, not a total upstream connection limit. Keep this value small enough that upstream servers can still accept new connections.
- [`rewrite`](https://nginx.org/en/docs/http/ngx_http_rewrite_module.html#rewrite): Rewrites the old API path to the internal API path. Regular expression-heavy configurations can make PCRE performance more important, as discussed in [Kernel, compiler, and libraries](/learning-paths/servers-and-cloud-computing/nginx_tune/kernel_comp_lib/).
- [`proxy_pass`](https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_pass): Forwards matching requests to the upstream server group. Use the same upstream block for related locations when you want them to share the same upstream connection pool.
- [`internal`](https://nginx.org/en/docs/http/ngx_http_core_module.html#internal) and [`limit_except`](https://nginx.org/en/docs/http/ngx_http_core_module.html#limit_except): Included for request handling and access control, not as primary performance settings.
- [`proxy_cache_path`](https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_cache_path): Not in the example configuration, but it's worth considering when responses can be cached by the reverse proxy or API gateway.
  
  When you use this directive, review [`proxy_cache_lock`](https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_cache_lock) and [`proxy_cache_valid`](https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_cache_valid).
  
  For more information, see the NGINX Admin Guide section on [content caching](https://docs.nginx.com/nginx/admin-guide/content-cache/content-caching/).
- NGINX variables: The example uses `$hostname` in `server_name`. For the full list of built-in variables, see the NGINX [variable index](https://nginx.org/en/docs/varindex.html).

## What you've learned and what's next

You've now reviewed reverse proxy and API gateway directives that affect upstream connection reuse, request rewriting, access control, and caching decisions.

Next, you'll test NGINX optimizations with a repeatable `wrk` workload.

