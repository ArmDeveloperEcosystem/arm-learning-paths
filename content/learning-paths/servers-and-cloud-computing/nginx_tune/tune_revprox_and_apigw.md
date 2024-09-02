---
title: "Tune a Reverse Proxy or API Gateway"
weight: 5
layout: "learningpathall"
---

Use the information below as general guidance for tuning Nginx.

##  Nginx Reverse Proxy and API Gateway Configuration

In the [Setup Reverse Proxy and API Gateway](/learning-paths/servers-and-cloud-computing/nginx/basic_static_file_server) section of the [Learn how to deploy Nginx](/learning-paths/servers-and-cloud-computing/nginx/) learning path, a bare minimum Reverse Proxy and API Gateway configuration was discussed. In this section, you will look at a tuned configuration.

### Top Level nginx.conf

The same top level config used in [Tune a static file server](/learning-paths/servers-and-cloud-computing/nginx_tune/tune_static_file_server) is suggested.

  ### Reverse Proxy and API Gateway configuration

A tuned configuration (`/etc/nginx/conf.d/loadbalancer.conf`) is shown below. Only performance relevant directives that were not discussed in the [file server section](/learning-paths/servers-and-cloud-computing/nginx_tune/tune_static_file_server) are explained here.
```
# Upstreams for https
upstream ssl_file_server_com {
  server <fileserver_1_ip_or_dns>:443;
  server <fileserver_2_ip_or_dns>:443;
  keepalive 1024;
}

# HTTPS reverse proxy and API Gateway
server {
  listen 443 ssl reuseport backlog=65535;
  root /usr/share/nginx/html;
  index index.html index.htm;
  server_name $hostname;

  ssl_certificate /etc/nginx/ssl/ecdsa.crt;
  ssl_certificate_key /etc/nginx/ssl/ecdsa.key;
  ssl_ciphers ECDHE-ECDSA-AES256-GCM-SHA384;

  # API Gateway Path
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

  # Reverse Proxy Path
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

* [`keepalive`](https://nginx.org/en/docs/http/ngx_http_upstream_module.html#keepalive):
  * This directive enables connection caching for upstream servers.
  * This is disabled by default. It should be turned on because it can improve performance significantly. This value should be increased further when more upstream servers are added to the `upstream` block.
  * The value of 1024 shown above is probably more than enough for most production deployments. It is recommended that you test in order to find an appropriate value for your deployment.
  * When this directive is used, the `proxy_http_version` should be set to 1.1 and `proxy_set_header` connection header should be cleared for upstream keep alive to work properly.
* [`proxy_cache_path`](https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_cache_path)
  * This directive is not in the configuration above. However it is worth mentioning because it can impact performance greatly. This enables a cache within the Reverse Proxy or API Gateway.
  * When this directive is used, both `proxy_cache_lock` and `proxy_cache_valid` should be considered as additional optimizations.
  * The [Nginx admin-guide](https://docs.nginx.com/nginx/admin-guide/) has a section on [content-caching](https://docs.nginx.com/nginx/admin-guide/content-cache/content-caching/) that should be explored.
