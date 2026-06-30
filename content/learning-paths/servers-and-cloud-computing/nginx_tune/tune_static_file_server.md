---
title: Tune a static file server
weight: 4
layout: "learningpathall"
---

## NGINX file server configuration

In the [set up a static file server](/learning-paths/servers-and-cloud-computing/nginx/basic_static_file_server/) section of the [Learn how to deploy NGINX](/learning-paths/servers-and-cloud-computing/nginx/) Learning Path, you configured a minimal file server. 

You'll now review a tuned file server configuration. Use this example configuration as a starting point, then size each directive for your workload and validate the result with repeatable measurements.

### Top-level nginx.conf

The following is a tuned top-level configuration file (`/etc/nginx/nginx.conf`): 

```nginx
user www-data;
worker_processes auto;
worker_rlimit_nofile 1000000;
pid /run/nginx.pid;

events {
  worker_connections 512;
}

http {
  ##
  # Basic Settings
  ##
  sendfile on;
  tcp_nopush on;
  keepalive_timeout 75;
  keepalive_requests 1000000000;

  include /etc/nginx/mime.types;
  default_type application/octet-stream;

  ##
  # Logging Settings
  ##
  access_log off;
  error_log /var/log/nginx/error.log;

  ##
  # Virtual Host Configs
  ##
  include /etc/nginx/conf.d/*.conf;
}
```

The full NGINX [directive index](https://nginx.org/en/docs/dirindex.html) and [variable index](https://nginx.org/en/docs/varindex.html) are useful references when you tune configuration files. 

The following are performance-relevant directives:

- [`worker_processes`](https://nginx.org/en/docs/ngx_core_module.html#worker_processes):
  - Selects how many worker processes NGINX starts.
  - `auto` starts one worker process per available CPU, which is a good starting point for most deployments.
- [`worker_rlimit_nofile`](https://nginx.org/en/docs/ngx_core_module.html#worker_rlimit_nofile):
  - Selects the maximum number of files that can be opened by NGINX worker processes.
  - If your deployment needs to sustain a large number of open connections, this should be set relatively high.
  - If this value is too low, connections can fail or be rejected. That said, `1000000` is likely excessive for many deployments.
  - This directive changes the open-file limit for NGINX worker processes, so you can raise the worker limit without relying on a separate `ulimit` setting in the service startup environment.
- [`worker_connections`](https://nginx.org/en/docs/ngx_core_module.html#worker_connections):
  - Selects the number of simultaneous worker connections that can be opened by a worker process.
  - The default is `512`, so this directive can be removed from the example configuration. It's shown here because deployments that need to sustain a large number of connections might also need a higher `worker_connections` value.
- [`sendfile`](https://nginx.org/en/docs/http/ngx_http_core_module.html#sendfile):
  - Allows NGINX to copy data from one file descriptor to another without copying the data into a user-space buffer first, which can improve static file serving performance.
- [`tcp_nopush`](https://nginx.org/en/docs/http/ngx_http_core_module.html#tcp_nopush):
  - Delays packet sending so NGINX can send response headers and file data together when `sendfile` is enabled, which can improve static file serving efficiency.
- [`keepalive_timeout`](https://nginx.org/en/docs/http/ngx_http_core_module.html#keepalive_timeout):
  - The default is `75s`, so this directive can be removed from the example configuration.
  - Increase this value only when your deployment needs to hold idle keepalive connections open for longer.
- [`keepalive_requests`](https://nginx.org/en/docs/http/ngx_http_core_module.html#keepalive_requests):
  - Sets the number of requests that can be served through a single connection before it's closed by NGINX.
  - The default is `1000`, which can be too small for some use cases. If individual clients make many requests over a single connection, increasing this value can reduce connection reestablishment overhead.
  - Avoid setting this higher than needed. NGINX closes keepalive connections periodically to free per-connection memory, so very high values can increase memory use.
- [`access_log`](https://nginx.org/en/docs/http/ngx_http_log_module.html#access_log):
  * Access logging can add significant write overhead in high-request-rate workloads. If you need access logs, consider buffering them instead of turning logging off.
- [`error_log`](https://nginx.org/en/docs/ngx_core_module.html#error_log):
  * Error logging usually has little performance impact unless NGINX is writing frequent messages. If errors reported, fix them.

### File server configuration

The following is a tuned file server configuration file (`/etc/nginx/conf.d/fileserver.conf`): 

```nginx
# HTTPS file server
server {
  listen 443 ssl reuseport backlog=65535;
  root /usr/share/nginx/html;
  index index.html index.htm;
  server_name $hostname;

  open_file_cache max=1000;

  ssl_certificate /etc/nginx/ssl/ecdsa.crt;
  ssl_certificate_key /etc/nginx/ssl/ecdsa.key;
  ssl_ciphers ECDHE-ECDSA-AES256-GCM-SHA384;

  location / {
    limit_except GET {
      deny all;
    }
    try_files $uri $uri/ =404;
  }
}
```

The following are performance-relevant directives:

- [`listen`](https://nginx.org/en/docs/http/ngx_http_core_module.html#listen):
  - Selects the port and protocol of the file server.
  - `reuseport` allows NGINX to distribute incoming connections across worker processes.
  - `backlog` sets the maximum length of the pending connection queue. Align it with `net.core.somaxconn`, and keep it at least `512`.
- [`open_file_cache`](https://nginx.org/en/docs/http/ngx_http_core_module.html#open_file_cache):
  - Configures a cache that stores information about open file descriptors.
  - It can improve performance when NGINX serves a repeated set of files.
- [`ssl_ciphers`](https://nginx.org/en/docs/http/ngx_http_ssl_module.html#ssl_ciphers):
  - The cipher suite used for HTTPS can greatly impact performance. It's important to understand both the security and performance implications of the chosen cipher suite.
  - The TLS library used by NGINX and how it was built can also affect cipher performance. For more information, see the [Kernel, compiler, and libraries](/learning-paths/servers-and-cloud-computing/nginx_tune/kernel_comp_lib/) section of this Learning Path.
- [`server_name`](https://nginx.org/en/docs/http/ngx_http_core_module.html#server_name) and [`try_files`](https://nginx.org/en/docs/http/ngx_http_core_module.html#try_files):
  - The example uses NGINX variables such as `$hostname` and `$uri`. For a full list of build-in variables, see the NGINX [variable index](https://nginx.org/en/docs/varindex.html).

## What you've learned and what's next

You've now seen example top-level and file server configurations and learned about performance-relevant directives that you can optimize to tune NGINX performance. 

Next, you'll learn about tuning a reverse proxy and API gateway configuration.
