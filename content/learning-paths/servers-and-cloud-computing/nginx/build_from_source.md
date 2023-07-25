---
title: "Build Nginx from source"
weight: 3
layout: "learningpathall"
---

## Before you begin

Before building from source, it's helpful to look at the build configuration of a prebuilt version of Nginx. Refer to the previous section, [Install Nginx via a package manager](/learning-paths/servers-and-cloud-computing/nginx/install_from_package) for more information. 

## Build Nginx from source

The [nginx.com documentation](https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/#compiling-and-installing-from-source) explains how to compile and install Nginx from source. The documentation does not provide specific guidance on configuration and compile options. Additional information about the configuration options can also be found on the [nginx.org documentation](http://nginx.org/en/docs/configure.html).

Nginx is quite performant and doesn't need a significant amount of configuration. As long as you enable the features you need, it should work well. Supplemental information that will help you decide how to configure Nginx is provided below.

### Configuration and compile options

A good starting point for selecting build options is to use the same options that are used on a prebuilt version of Nginx. This was covered in the previous section. 

Below is an example output of the `nginx -V` command from a prebuilt package:

```output
nginx version: nginx/1.18.0
built with OpenSSL 3.0.2 15 Mar 2022
TLS SNI support enabled
configure arguments: --with-cc-opt='-g -O2 -ffile-prefix-map=/build/nginx-glNPkO/nginx-1.18.0=. -flto=auto -ffat-lto-objects -flto=auto -ffat-lto-objects -fstack-protector-strong -Wformat -Werror=format-security -fPIC -Wdate-time -D_FORTIFY_SOURCE=2' --with-ld-opt='-Wl,-Bsymbolic-functions -flto=auto -ffat-lto-objects -flto=auto -Wl,-z,relro -Wl,-z,now -fPIC' --prefix=/usr/share/nginx --conf-path=/etc/nginx/nginx.conf --http-log-path=/var/log/nginx/access.log --error-log-path=/var/log/nginx/error.log --lock-path=/var/lock/nginx.lock --pid-path=/run/nginx.pid --modules-path=/usr/lib/nginx/modules --http-client-body-temp-path=/var/lib/nginx/body --http-fastcgi-temp-path=/var/lib/nginx/fastcgi --http-proxy-temp-path=/var/lib/nginx/proxy --http-scgi-temp-path=/var/lib/nginx/scgi --http-uwsgi-temp-path=/var/lib/nginx/uwsgi --with-compat --with-debug --with-pcre-jit --with-http_ssl_module --with-http_stub_status_module --with-http_realip_module --with-http_auth_request_module --with-http_v2_module --with-http_dav_module --with-http_slice_module --with-threads --add-dynamic-module=/build/nginx-glNPkO/nginx-1.18.0/debian/modules/http-geoip2 --with-http_addition_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_sub_module
```

You may want to drop the options that have a random hash, appear directly related to a particular Linux distribution, or can be overridden using runtime configuration.

In the output above, there are two configuration switches that have a hash of `glNPko`. These are the GCC switch `-ffile-prefix-map` and the Nginx configuration option `--add-dynamic-module`. The `--add-dynamic-module` option also has a reference to the Debian Linux distribution this version is built for. 

Before removing these two options, check the GCC and Nginx documentation to understand `-ffile-prefix-map` and `--add-dynamic-module` respectively. If it appears that removing these does not impact performance or functionality, you can remove them. You should search what these two switches do, and see if you agree with their removal.

After removing these switches, the remaining options should be investigated to understand how they might impact functionality and performance. First, it's a good idea to understand what you are building. Second, it's good to simplify the configuration by shortening it. Upon further inspection of the example output above, there are various Nginx build options that end with `-temp-path` which can be overridden in the Nginx runtime configuration file. These can be removed as well. 

The final build configuration is now reduced to:

```output
--with-cc-opt='-g -O2 -flto=auto -ffat-lto-objects -flto=auto -ffat-lto-objects -fstack-protector-strong -Wformat -Werror=format-security -fPIC -Wdate-time -D_FORTIFY_SOURCE=2' --with-ld-opt='-Wl,-Bsymbolic-functions -flto=auto -ffat-lto-objects -flto=auto -Wl,-z,relro -Wl,-z,now -fPIC' --prefix=/usr/share/nginx --conf-path=/etc/nginx/nginx.conf --http-log-path=/var/log/nginx/access.log --error-log-path=/var/log/nginx/error.log --lock-path=/var/lock/nginx.lock --pid-path=/run/nginx.pid --modules-path=/usr/lib/nginx/modules --with-compat --with-debug --with-pcre-jit --with-http_ssl_module --with-http_stub_status_module --with-http_realip_module --with-http_auth_request_module --with-http_v2_module --with-http_dav_module --with-http_slice_module --with-threads --with-http_addition_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_sub_module
```

Use your judgment to decide if you should keep or drop each configuration option. 

### Building Nginx and dependencies

Once you decide on configuration options, you can follow the [build instructions](https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/#compiling-and-installing-from-source). 

Nginx has three dependencies: PCRE, zlib, and OpenSSL. You can build them from source as described in the instructions or you can also install prebuilt versions of each library using a package manager. 

### Running Nginx as a service

Create a service file to run Nginx as a service. A service file can be taken from a prebuilt version of Nginx, as discussed in the previous section, or you can create your own. 

Use the `service` command to start Nginx: 

```console
sudo service nginx start
```

To confirm Nginx is running, check the status:

```console
sudo service nginx status
```

The output from this command will look similar to:

```output
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
     Active: active (running) ...
```

Nginx is now running.