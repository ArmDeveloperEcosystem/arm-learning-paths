---
title: "Tune a static file server"
weight: 4
layout: "learningpathall"
---

##  Tuning a static file server

The profile of requests made by clients will vary based on the use case. This means there is no one size fits all set of tuning parameters for Nginx. Use the information below as general guidance on tuning Nginx.

##  Nginx File Server Configuration

In the [Setup a static file server](/learning-paths/servers-and-cloud-computing/nginx/basic_static_file_server) section of the [Learn how to deploy Nginx](/learning-paths/servers-and-cloud-computing/nginx/) learning path, a bare minimum file server configuration was discussed. In this section, a tuned file server configuration is discussed.

### Top Level nginx.conf

A tuned top level configuration file (`/etc/nginx/nginx.conf`) is shown below. Only performance relevant directives will be discussed.

```
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

* [`worker_rlimit_nofile`](https://nginx.org/en/docs/ngx_core_module.html#worker_rlimit_nofile):
  * This directive selects the maximum number of files that can be opened by Nginx worker processes.
  * If your deployment needs to sustain a large number of open connections, this should be set relatively high.
  * If this value is too low, you will get failed/rejected connections. That said, 1000000 is probably excessively large for production.
  * Using this directive means you do not have to use the `ulimit` command to set the system wide open file limit.
* [`worker_connections`](https://nginx.org/en/docs/ngx_core_module.html#worker_connections):
  * This directive selects the number of simultaneous worker connections that can be opened by a worker process.
  * The default is 512 which means this directive can be removed from the configuration above. However, it is shown here to emphasize that if your deployment needs to sustain a large number of connections, this value needs to be increased (along with `worker_rlimit_nofile`).
* [`sendfile`](https://nginx.org/en/docs/http/ngx_http_core_module.html#sendfile):
  * This directive allows Nginx to directly copy data from one file descriptor to another without copying the data into a buffer first. The elimination of this copy can boost performance.
  * This is a common optimization that you will see in almost all Nginx configurations.
* [`tcp_nopush`](https://nginx.org/en/docs/http/ngx_http_core_module.html#tcp_nopush):
  * This directive allows Nginx to send HTTP response headers along with file data in the same packet.
  * This is a common optimization and is suggested to be enabled when `sendfile` is enabled.
* [`keepalive_timeout`](https://nginx.org/en/docs/http/ngx_http_core_module.html#keepalive_timeout):
  * The default is 75s which means this directive can be removed from the configuration shown above. However, it is shown here to emphasize that if you need your deployment to hold connections open for a longer period of time, this value needs to be increased.
* [`keepalive_requests`](https://nginx.org/en/docs/http/ngx_http_core_module.html#keepalive_requests):
  * This directive sets the number of requests that can be served through a single connection before it is closed by Nginx.
  * The default is 1000 which could be too small for some use cases. If you know that individual clients will make numerous requests on a single connection, it is important to increase this setting. Otherwise performance penalties will be paid to reestablish connections.
* [`access_log`](https://nginx.org/en/docs/http/ngx_http_log_module.html#access_log):
  * The access log directive is off by default. It is shown here to emphasize that if this is turned on, it will impact performance significantly. This negative performance impact can be reduced by tuning on the buffer for the access log.
* [`error_log`](https://nginx.org/en/docs/ngx_core_module.html#error_log):
  * The error log is on by default. There is no significant impact to performance if Nginx is functioning properly (i.e. not reporting errors). If errors are being reported, this logging may impact performance, but this is a moot point because the errors should be addressed anyway.

  ### File server configuration

A tuned file server configuration file (`/etc/nginx/conf.d/fileserver.conf`) is shown below. Only performance relevant directives will be discussed.

```
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

* [`listen`](https://nginx.org/en/docs/http/ngx_http_core_module.html#listen):
  * This directive is used to select the port and protocol of the file server.
  * `reuseport` is a common optimization that allows Nginx to distribute incoming connections across worker processes.
  * `backlog` sets the maximum length of the pending connection queue. Set this to whatever `net.core.somaxconn` is set to. However, if `net.core.somaxconn` is set to a value that is smaller than 512; set this parameter to 512.
* [`open_file_cache`](https://nginx.org/en/docs/http/ngx_http_core_module.html#open_file_cache):
  * This directive sets up a cache that stores information on open file descriptors. This can significantly increase performance.
* [`ssl_ciphers`](https://nginx.org/en/docs/http/ngx_http_ssl_module.html#ssl_ciphers):
  * The cipher suite used for HTTPS can greatly impact performance. It is important to understand both the security and performance implications of the chosen cipher suite.
  * The version of OpenSSL and how it was compiled can also impact the performance of the cipher suite. This was discussed in the [Kernel, compiler, and OpenSSL](/learning-paths/servers-and-cloud-computing/nginx_tune/kernel_comp_lib/) section of this learning path. 
