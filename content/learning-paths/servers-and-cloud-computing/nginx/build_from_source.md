---
title: "Build Nginx from source"
weight: 3
layout: "learningpathall"
---

## Before you begin

Before building from source. It's helpful to first take a look at the build configuration of a prebuilt version of Nginx. If you haven't done so already, take a look at the previous section to see how you can [install Nginx via a package manager and check its build configuration](/learning-paths/servers-and-cloud-computing/nginx/install_from_package). If you already have a good understanding of how to configure an Nginx build, you can skip trying out a prebuilt and continue reading.

## Build Nginx from source

The [nginx.com documentation](https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/#compiling-and-installing-from-source) explains how to compile and install Nginx from source. However, it doesn't give guidance on configuration and compile options (it just gives examples of how to select options). Information on all of the configuration options can also be found on the [nginx.org documentation](http://nginx.org/en/docs/configure.html), however, it too doesn't give guidance on configuration options. The good news is that Nginx is quite performant and doesn't need a significant amount of configuration. As long as you enable the features you need, it will work well. That said, this learning path will provide some supplemental information that will help you decide how to configure Nginx beyond what is noted in the documentation.

### Configuration and compile options

A great starting point for selecting build options is to use the same options that are used on a prebuilt version of Nginx. Getting the configuration and build options used for an install of Nginx was discussed in the section called [install Nginx via a package manager and check its build configuration](/learning-paths/servers-and-cloud-computing/nginx/install_from_package). Below is an example of a build config from a prebuilt:

```output
nginx version: nginx/1.18.0
built with OpenSSL 3.0.2 15 Mar 2022
TLS SNI support enabled
configure arguments: --with-cc-opt='-g -O2 -ffile-prefix-map=/build/nginx-glNPkO/nginx-1.18.0=. -flto=auto -ffat-lto-objects -flto=auto -ffat-lto-objects -fstack-protector-strong -Wformat -Werror=format-security -fPIC -Wdate-time -D_FORTIFY_SOURCE=2' --with-ld-opt='-Wl,-Bsymbolic-functions -flto=auto -ffat-lto-objects -flto=auto -Wl,-z,relro -Wl,-z,now -fPIC' --prefix=/usr/share/nginx --conf-path=/etc/nginx/nginx.conf --http-log-path=/var/log/nginx/access.log --error-log-path=/var/log/nginx/error.log --lock-path=/var/lock/nginx.lock --pid-path=/run/nginx.pid --modules-path=/usr/lib/nginx/modules --http-client-body-temp-path=/var/lib/nginx/body --http-fastcgi-temp-path=/var/lib/nginx/fastcgi --http-proxy-temp-path=/var/lib/nginx/proxy --http-scgi-temp-path=/var/lib/nginx/scgi --http-uwsgi-temp-path=/var/lib/nginx/uwsgi --with-compat --with-debug --with-pcre-jit --with-http_ssl_module --with-http_stub_status_module --with-http_realip_module --with-http_auth_request_module --with-http_v2_module --with-http_dav_module --with-http_slice_module --with-threads --add-dynamic-module=/build/nginx-glNPkO/nginx-1.18.0/debian/modules/http-geoip2 --with-http_addition_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_sub_module
```

When Nginx is tested at Arm, most options are kept. The options that are dropped are those that have a random hash, appear directly related to a particular distribution of Linux, or options that can be overridden by an application configuration.

Applying this idea to the example output above, there are two configuration switches that have what appears to be a hash of `glNPko`. These are the GCC switch `-ffile-prefix-map` and the Nginx configuration option `--add-dynamic-module`. `--add-dynamic-module` also appears to have a reference to the distribution this prebuilt was built for (debian). This is another reason to consider removing this option.

Before removing these two options, the GCC & Nginx documentation should be checked to understand `-ffile-prefix-map` and `--add-dynamic-module` respectively. If it appears that removing these won't impact performance or functionality, they can be removed. You should search what these two switches do, and see if you agree with their removal.

After removing these more obvious switches, the remaining options should be investigated to understand how they might impact functionality and performance. First, it's a good idea to understand what you are building. Second, it's good to simplify the configuration by shortening it. Upon further inspection of the example output above, there are various Nginx build options that end with `-temp-path` which can be overridden in the Nginx runtime configuration file. Thus, these can be removed as well. The final build configuration is now reduced to the below:

```output
--with-cc-opt='-g -O2 -flto=auto -ffat-lto-objects -flto=auto -ffat-lto-objects -fstack-protector-strong -Wformat -Werror=format-security -fPIC -Wdate-time -D_FORTIFY_SOURCE=2' --with-ld-opt='-Wl,-Bsymbolic-functions -flto=auto -ffat-lto-objects -flto=auto -Wl,-z,relro -Wl,-z,now -fPIC' --prefix=/usr/share/nginx --conf-path=/etc/nginx/nginx.conf --http-log-path=/var/log/nginx/access.log --error-log-path=/var/log/nginx/error.log --lock-path=/var/lock/nginx.lock --pid-path=/run/nginx.pid --modules-path=/usr/lib/nginx/modules --with-compat --with-debug --with-pcre-jit --with-http_ssl_module --with-http_stub_status_module --with-http_realip_module --with-http_auth_request_module --with-http_v2_module --with-http_dav_module --with-http_slice_module --with-threads --with-http_addition_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_sub_module
```

The key point to understand, is that you will have to use your judgement to figure out if you should keep or drop a configuration option. In a more advanced Nginx learning path, GCC options that could be used to improve the performance of Nginx will be explored. That said, using these options is usually very optimized as it is.

### Building Nginx & Dependencies

Once you know your configuration options, you can follow the build [instructions](https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/#compiling-and-installing-from-source). With respect to the three dependencies of PCRE, zlib, and OpenSSL; you can also install prebuilts of those libraries using a package manager to skip having to build them as the instructions explain. That said, it may be advantageous to build these as additional performance benefits could be gained. This point will be explored in an advanced Nginx learning path.


### Running Nginx as a service

You should create a service file to run Nginx as a service. A service file can be taken from a prebuilt version of Nginx as discussed in the section called [install Nginx via a package manager and check its build configuration](/learning-paths/servers-and-cloud-computing/nginx/install_from_package). Alternatively, you can make you own. Once this file is created, you can use `service` as shown below.


```console
sudo service nginx start
```

To confirm Nginx is running, check the status:

```console
sudo service nginx status
```

The output from this command will look like:

```output
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
     Active: active (running) ...
```
Nginx is successfully running as shown.