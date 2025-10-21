---
title: Install PHP
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install PHP 
In this section, you will install PHP together with the Apache web server and several commonly used PHP extensions on a SUSE Arm-based virtual machine. This forms the foundation for running and serving dynamic PHP applications on Arm-based machines.

### Update the system
Before installing any software, make sure your system has the latest packages and security patches:

```console
sudo zypper refresh
sudo zypper update -y
```

### Install PHP, Apache, and common extensions
Now install PHP, PHP-FPM, Apache web server, and some commonly used PHP extensions by using the following command:

```console
sudo zypper install -y php php-cli php-fpm php-mysql php-xml php-mbstring php-opcache apache2
```
Package breakdown:
| Package          | Description                                                                                      |
| ---------------- | ------------------------------------------------------------------------------------------------ |
| **php**          | Core PHP interpreter used to run web applications.                                               |
| **php-cli**      | Enables running PHP scripts from the command line. Useful for testing and automation.            |
| **php-fpm**      | FastCGI Process Manager — manages PHP worker processes and improves concurrency and performance. |
| **php-mysql**    | Provides MySQL/MariaDB database connectivity for PHP.                                            |
| **php-xml**      | Adds support for parsing and manipulating XML data.                                              |
| **php-mbstring** | Adds multi-byte string handling, required by many web frameworks.                                |
| **php-opcache**  | Boosts performance by caching precompiled PHP bytecode in memory, reducing runtime overhead.     |
| **apache2**      | Installs the Apache HTTP web server, which will serve PHP files via mod_php or FastCGI.          |


### Enable and start Apache:
Once Apache is installed, enable and start the service so that it runs automatically on boot and begins serving HTTP requests immediately:
```console
sudo systemctl enable apache2
sudo systemctl start apache2
sudo systemctl status apache2
```
If everything starts correctly, the output should look similar to:

```output
● apache2.service - The Apache Webserver
     Loaded: loaded (/usr/lib/systemd/system/apache2.service; enabled; vendor preset: disabled)
     Active: active (running) since Wed 2025-10-15 18:55:30 UTC; 3s ago
   Main PID: 4184 (httpd-prefork)
     Status: "Processing requests..."
      Tasks: 6
        CPU: 18ms
     CGroup: /system.slice/apache2.service
             ├─ 4184 /usr/sbin/httpd-prefork -DSYSCONFIG -C "PidFile /run/httpd.pid" -C "Include /etc/apache2/>
             ├─ 4225 /usr/sbin/httpd-prefork -DSYSCONFIG -C "PidFile /run/httpd.pid" -C "Include /etc/apache2/>
             ├─ 4226 /usr/sbin/httpd-prefork -DSYSCONFIG -C "PidFile /run/httpd.pid" -C "Include /etc/apache2/>
             ├─ 4227 /usr/sbin/httpd-prefork -DSYSCONFIG -C "PidFile /run/httpd.pid" -C "Include /etc/apache2/>
             ├─ 4228 /usr/sbin/httpd-prefork -DSYSCONFIG -C "PidFile /run/httpd.pid" -C "Include /etc/apache2/>
             └─ 4229 /usr/sbin/httpd-prefork -DSYSCONFIG -C "PidFile /run/httpd.pid" -C "Include /etc/apache2/>

Oct 15 18:55:30 pareena-php-test systemd[1]: Starting The Apache Webserver...
Oct 15 18:55:30 pareena-php-test systemd[1]: Started The Apache Webserver.
```

### Verify PHP installation
After installation, verify that PHP is installed correctly and view the installed version:

```console
php -v
```
You should see output similar to:
```output
PHP 8.0.30 (cli) (built: Nov 25 2024 12:00:00) ( NTS )
Copyright (c) The PHP Group
Zend Engine v4.0.30, Copyright (c) Zend Technologies
with Zend OPcache v8.0.30, Copyright (c), by Zend Technologies
```
You can now proceed to the baseline testing section, where you’ll create and load a simple PHP web page to confirm that Apache and PHP are working together on your SUSE Arm-based virtual machine.
