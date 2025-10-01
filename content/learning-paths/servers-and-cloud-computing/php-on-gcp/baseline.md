---
title: PHP baseline testing on Google Axion C4A Arm Virtual Machine
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Baseline Setup for PHP-FPM
This section covers the installation and configuration of **PHP and Apache** on a SUSE Arm-based GCP VM. It includes setting up **PHP-FPM** with a Unix socket, verifying PHP functionality via a test page, and ensuring Apache and PHP-FPM work together correctly.  

### Configure the PHP-FPM Pool

**PHP-FPM:** A FastCGI Process Manager that runs PHP scripts efficiently, handling multiple requests separately from the web server for better performance and security.

A **pool** is basically a set of PHP worker processes that handle requests.  

### Copy the Default Configuration (if missing)

Run this command to create a working config file:

```console
sudo cp /etc/php8/fpm/php-fpm.d/www.conf.default /etc/php8/fpm/php-fpm.d/www.conf
```

### Edit the Configuration

Open the config file in a text editor:

```console
sudo vi /etc/php8/fpm/php-fpm.d/www.conf
```

Update the file to use a Unix socket:

Find this line `; listen = 127.0.0.1:9000`. Replace it with these lines.

```ini
listen = /run/php-fpm/www.sock
listen.owner = wwwrun
listen.group = www
listen.mode = 0660
```
- `listen = /run/php-fpm/www.sock` → PHP will talk to Apache using a local “socket file” instead of a network port.  
- `listen.owner = wwwrun` → `wwwrun` is Apache’s default user on SUSE, so Apache can access the socket.  
- `listen.group = www` → sets the group to match Apache’s group.  
- `listen.mode = 0660` → gives read/write permission to both Apache and PHP-FPM.

### Start and Enable PHP-FPM

Restart PHP-FPM so it picks up the changes:

```console
sudo systemctl restart php-fpm
```

## Test PHP
Now that PHP and Apache are installed, let’s verify that everything is working correctly.  

### Create a Test Page
We will make a simple PHP file that shows details about the PHP setup.

```console
echo "<?php phpinfo(); ?>" | sudo tee /srv/www/htdocs/info.php
```
This creates a file named **info.php** inside Apache’s web root directory `(/srv/www/htdocs/)`. When you open this file in a browser, it will display the PHP configuration page.

### Test from Inside the VM
Run the following command:

```console
curl http://localhost/info.php
```
- `curl` fetches the page from the local Apache server.  
- If PHP is working, you’ll see a large block of HTML code as output.  
- This confirms that PHP is correctly connected with Apache.  

You should see an output similar to:

```output
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"><head>
<style type="text/css">
body {background-color: #fff; color: #222; font-family: sans-serif;}
pre {margin: 0; font-family: monospace;}
a:link {color: #009; text-decoration: none; background-color: #fff;}
a:hover {text-decoration: underline;}
table {border-collapse: collapse; border: 0; width: 934px; box-shadow: 1px 2px 3px rgba(0, 0, 0, 0.2);}
.center {text-align: center;}
.center table {margin: 1em auto; text-align: left;}
.center th {text-align: center !important;}
td, th {border: 1px solid #666; font-size: 75%; vertical-align: baseline; padding: 4px 5px;}
th {position: sticky; top: 0; background: inherit;}
h1 {font-size: 150%;}
h2 {font-size: 125%;}
h2 a:link, h2 a:visited{color: inherit; background: inherit;}
```
Basically, it is the HTML output that confirms PHP is working.

### Test from Your Browser
Now, let’s test it from outside the VM. Open a web browser on your local machine (Chrome, Firefox, Edge, etc.) and enter the following URL in the address bar:

```console
http://<YOUR_VM_PUBLIC_IP>/info.php
```
- Replace `<YOUR_VM_PUBLIC_IP>` with the public IP of your GCP VM.

If everything is set up correctly, you will see a PHP Info page in your browser. It looks like this:

![PHP-info page alt-text#center](images/php-web.png "Figure 1: PHP info")

This verifies the basic functionality of the PHP installation before proceeding to the benchmarking.
