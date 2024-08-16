---
title: "Install Nginx using a package manager and check the build configuration"
weight: 2
layout: "learningpathall"
---

## Before you begin

There are two versions of Nginx, an open source version and a licensed version. The licensed version is called Nginx Plus. This Learning Path uses the open source version. The open source version is referred to as simply Nginx.
 
If you plan to build Nginx from source, you can skip to the next section. However, it might be helpful to look at a prebuilt install of Nginx first. This will help you understand how to configure a source build of Nginx.

## About Nginx documentation

There are two sets of Nginx documentation. [Documentation](https://nginx.org/en/docs/) on [nginx.org](https://nginx.org) and [documentation](https://docs.nginx.com/nginx/) from [www.f5.com/products/nginx/nginx-plus](https://www.f5.com/products/nginx/nginx-plus). The nginx.org documentation covers the open source version of Nginx and the docs.nginx.com documentation covers Nginx Plus. Even if you are working with the open source version, you should explore the documentation on docs.nginx.com and the helpful [Admin Guide](https://docs.nginx.com/nginx/admin-guide/).

You can explore the documentation to gain key insights that will help with deployment, configuration, and performance. 

## Install an Nginx prebuilt package

To install Nginx using a package manager, you can follow the [nginx.org install instructions](http://nginx.org/en/linux_packages.html) or the [nginx.com install instructions](https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/). Both yield the same result.

### Getting the Nginx build config

It might be useful to know the build configuration of the installed version of Nginx. Especially if you plan to build Nginx from source and are unsure of how to configure the build.

Run the following command to get the complete build options for the prebuilt install:

```bash
nginx -V
```
The output from this command will look similar to:

```output
nginx version: nginx/1.18.0
built with OpenSSL 3.0.2 15 Mar 2022
TLS SNI support enabled
configure arguments: --with-cc-opt='-g -O2 -ffile-prefix-map=/build/nginx-glNPkO/nginx-1.18.0=. -flto=auto -ffat-lto-objects -flto=auto -ffat-lto-objects -fstack-protector-strong -Wformat -Werror=format-security -fPIC -Wdate-time -D_FORTIFY_SOURCE=2' --with-ld-opt='-Wl,-Bsymbolic-functions -flto=auto -ffat-lto-objects -flto=auto -Wl,-z,relro -Wl,-z,now -fPIC' --prefix=/usr/share/nginx --conf-path=/etc/nginx/nginx.conf --http-log-path=/var/log/nginx/access.log --error-log-path=/var/log/nginx/error.log --lock-path=/var/lock/nginx.lock --pid-path=/run/nginx.pid --modules-path=/usr/lib/nginx/modules --http-client-body-temp-path=/var/lib/nginx/body --http-fastcgi-temp-path=/var/lib/nginx/fastcgi --http-proxy-temp-path=/var/lib/nginx/proxy --http-scgi-temp-path=/var/lib/nginx/scgi --http-uwsgi-temp-path=/var/lib/nginx/uwsgi --with-compat --with-debug --with-pcre-jit --with-http_ssl_module --with-http_stub_status_module --with-http_realip_module --with-http_auth_request_module --with-http_v2_module --with-http_dav_module --with-http_slice_module --with-threads --add-dynamic-module=/build/nginx-glNPkO/nginx-1.18.0/debian/modules/http-geoip2 --with-http_addition_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_sub_module
```

The output shows key pieces of information that can help you understand the features and expected performance of Nginx. For example, the output lists the version of Nginx, the version of OpenSSL, and GCC compile flags like `-O2` (listed in the `--with-cc-opt` switch). 

The latest versions of Nginx and OpenSSL are recommended for best performance on Arm. 

This information can be used as a starting point for configuring a build from source.

### Getting the Nginx service file

If you plan to build the Nginx source code, you should save a copy of the Nginx service file that is installed with the prebuilt version. It is typically located at `/lib/systemd/system/nginx.service`. Changes to the file can be made as needed. 

Below is a sample service file:

```console
[Unit]
Description=The NGINX HTTP and reverse proxy server
After=syslog.target network-online.target remote-fs.target nss-lookup.target
Wants=network-online.target

[Service]
Type=forking
PIDFile=/run/nginx.pid
ExecStartPre=/usr/share/nginx/sbin/nginx -t
ExecStart=/usr/share/nginx/sbin/nginx
ExecReload=/usr/share/nginx/sbin/nginx -s reload
ExecStop=/bin/kill -s QUIT $MAINPID
ExecStopPost=/bin/rm -f /run/nginx.pid
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```