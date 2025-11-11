---
title: NGINX Baseline Testing 
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Baseline test NGINX with a static website

Once NGINX is installed and serving the default welcome page, verify that it can serve your own content. A baseline test with a simple static HTML site confirms that NGINX is correctly configured and working as expected on your Ubuntu Pro 24.04 LTS virtual machine.

## Create a static website directory  
Prepare a folder to host your HTML content:
```console
mkdir -p /var/www/my-static-site
cd /var/www/my-static-site
```

## Create an HTML file

Create a simple HTML page to replace the default NGINX welcome page. Using a file editor of your choice, create `index.html` with the following content:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Welcome to NGINX on Azure Ubuntu Pro</title>
  <style>
    body {
      background: linear-gradient(to right, #4facfe, #00f2fe);
      font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
      color: white;
      text-align: center;
    }
    .box {
      background: rgba(0, 0, 0, 0.3);
      padding: 40px;
      border-radius: 12px;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.4);
    }
    h1 {
      margin-bottom: 10px;
      font-size: 2.5rem;
    }
    p {
      font-size: 1.2rem;
    }
  </style>
</head>
<body>
  <div class="box">
    <h1>Welcome to NGINX on Azure Ubuntu Pro 24.04 LTS!</h1>
    <p>Your static site is running beautifully on Arm64</p>
  </div>
</body>
</html>
```

## Adjust permissions  
Ensure that NGINX (running as the `www-data` user) can read the files in your custom site directory:
```console
sudo chown -R www-data:www-data /var/www/my-static-site
```

## Update NGINX configuration
Point NGINX to serve files from your new directory by creating a dedicated configuration file under `/etc/nginx/conf.d/`:
```console
sudo nano /etc/nginx/conf.d/static-site.conf
```
Add the following configuration:
```console
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name _;

    root /var/www/my-static-site;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }

    access_log /var/log/nginx/static-access.log;
    error_log  /var/log/nginx/static-error.log;
}
```
This server block listens on port 80 for both IPv4 and IPv6, serves files from `/var/www/my-static-site/`, and uses `index.html` as the default page. It also writes access and error events to dedicated log files to simplify troubleshooting.

{{% notice Note %}}
Make sure the path to your `index.html` file is correct before saving.
{{% /notice %}}

## Disable the default site  
NGINX ships with a packaged default site configuration. Since you created a custom config, disable the default to avoid conflicts:
```console
sudo unlink /etc/nginx/sites-enabled/default
```

## Test the NGINX configuration  
Before applying your changes, test the configuration for syntax errors:
```console
sudo nginx -t
```
Expected output:
```output
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

## Reload or restart NGINX  
Apply your changes by reloading or restarting the NGINX service:
```console
sudo nginx -s reload
sudo systemctl restart nginx
```

## Test the static website in a browser  
Access your website at your public IP on port 80:
```console
http://<your-vm-public-ip>/
```

## Verify the page renders  
You should see your custom page instead of the default welcome page:
![Custom static website served by NGINX on Azure VM alt-text#center](images/nginx-web.webp "Custom static website served by NGINX on an Azure Arm64 VM")

This verifies the basic functionality of the NGINX installation. You can now proceed to benchmarking NGINX performance on your Arm-based Azure VM.
