---
title: NGINX Baseline Testing 
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---


### Baseline testing with a static website on NGINX
Perform baseline testing of NGINX on an **Ubuntu Pro 24.04 LTS** virtual machine by deploying a custom static HTML page. This verifies that NGINX is correctly serving content on the Arm64 platform.

1. Create a Static Website Directory:

Prepare a folder to host your HTML content.
```console
mkdir -p ~/my-static-site
```
2. Create an HTML file and Web page:

Create a HTML file `nano my-static-site/index.html` with the content below to design a visually appealing static landing page.

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
    <h1> Welcome to NGINX on Azure Ubuntu Pro 24.04 LTS!</h1>
    <p>Your static site is running beautifully on ARM64 </p>
  </div>
</body>
</html>
```
3. Move the Website to NGINX's Accessible Directory:

Since NGINX runs under the `www-data` user and may not have access to files inside `/home/ubuntu`, move the site to a directory where NGINX has permissions by default:

```console
sudo mkdir -p /var/www/my-static-site
sudo cp -r ~/my-static-site/* /var/www/my-static-site/
sudo chown -R www-data:www-data /var/www/my-static-site
```

4. Create NGINX Config File to Serve Static Website:

Point NGINX to serve your static HTML content.
```console
sudo nano /etc/nginx/conf.d/static-site.conf
```
Now, add the following configuration:

```NGINX
server {
    listen 80;
    server_name localhost;

    location / {
        root /var/www/my-static-site;
        index index.html;
    }

    access_log /var/log/nginx/static-access.log;
    error_log /var/log/nginx/static-error.log;
}
```
Make sure `/home/ubuntu/my-static-site` is the correct path to your **index.html**.

5. Test the NGINX Configuration:

```console
sudo nginx -t
```
You should see an output similar to:
```output
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

6. Reload or Restart NGINX:

Apply configuration changes and restart the web server.
```console
sudo nginx -s reload
sudo systemctl restart nginx
```

7. Test the Static Website on browser:

Access your website at your public IP on port 80.
```console
http://<your-vm-public-ip>/
```
Make sure port 80 is open in your Azure Network Security Group (NSG).

8. You should see the NGINX welcome page confirming a successful deployment:

![Static Website Screenshot](images/nginx-web.png)

This verifies the basic functionality of NGINX installation before proceeding to the benchmarking.
