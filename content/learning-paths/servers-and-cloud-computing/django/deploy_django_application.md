---
title: Deploy the Django application
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Configuring the database
Open the file `myproject/settings.py` and scroll to `DATABASES` and replace the
code with the following:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "myprojectdb",
        "USER": "usr",
        "PASSWORD": "mypassword",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```
Replace the HOST IP address with the IP address of your machine or use `localhost` as per the example above.

Now you need to create the database and its user with the above data.
Type the following command:

```bash
sudo -u postgres psql
```
You should see the PostgreSQL prompt:
```output
postgres=#
```

Now type the following command into the `psql` prompt to create the database,
the user and to give the right permissions to the user:

```SQL
CREATE DATABASE myprojectdb;
CREATE USER usr WITH ENCRYPTED PASSWORD 'mypassword';
ALTER ROLE usr SET client_encoding TO 'utf8';
ALTER ROLE usr SET default_transaction_isolation TO 'read committed';
ALTER ROLE usr SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myprojectdb TO usr;
GRANT postgres TO usr;
```
Quit the `psql` prompt by typing `\q`.

You are ready now to test the connection to the database:

```bash
python manage.py migrate
```
The output should look similar to:

```output
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

If you see the above output, it means that Django was able to apply migrations to the database.

## Configuring the web server
Now it's time to configure the web server that will serve the http requests to
the user. You are going to set up Gunicorn and then Nginx.

### Set up Gunicorn
Set up Gunicorn with systemd

Create the file `/etc/systemd/system/gunicorn.socket` with the following
content:

```console
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```

Create the file `/etc/systemd/system/gunicorn.service` with the following
content:

```console
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=USER
Group=www-data
WorkingDirectory=/home/USER/myproject/
ExecStart=/home/USER/venv/bin/gunicorn --access-logfile - --workers 10 --bind unix:/run/gunicorn.sock myproject.wsgi:application

[Install]
WantedBy=multi-user.target
```

Replace `USER` in the above configuration file with the real user of your machine.

Start and check the status of gunicorn.socket:

```bash
sudo systemctl start gunicorn.socket
systemctl status gunicorn.socket
```
The output should look similar to:

```output
gunicorn.socket - gunicorn socket
     Loaded: loaded (/etc/systemd/system/gunicorn.socket; disabled; vendor preset: enabled)
     Active: active (listening) since Wed 2023-11-08 15:26:25 UTC; 8s ago
   Triggers: gunicorn.service
     Listen: /run/gunicorn.sock (Stream)
     CGroup: /system.slice/gunicorn.socket
```

Testing the configuration by querying the gunicorn using `curl`:

```bash
curl --unix-socket /run/gunicorn.sock localhost/aarch64app/
```

You should see the hello world message you saw earlier in the browser.

```output
Hello world from an aarch64 machine.
```
### Configure Nginx

The last step is to configure Nginx by pointing to the gunicorn service.
Create a file named `/etc/nginx/sites-available/myproject` with the following content:

```console
upstream app_server_myproject {
    server localhost:8000 fail_timeout=0;
}

server {
    listen   80; ## listen for ipv4
    server_name myproject.something.com;

    access_log  /var/log/nginx/myproject.access.log;
    error_log  /var/log/nginx/myproject.error.log;

    # path for static files
    location = /favicon.ico { access_log off; log_not_found off; }
    location ~ ^/static/(.*)$ {
        alias /home/USER/myproject/sitestatic/$1;
    }

    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_redirect off;
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```

Create a symbolic link to enable the Nginx configuration, remove the default configuration and then restart and check the status of Nginx.


```bash
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo touch /etc/nginx/sites-enabled/default
sudo systemctl restart nginx
systemctl status nginx
```

The output should look similar to:

```output
nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
     Active: active (running) since Wed 2023-11-08 15:46:43 UTC; 4min 18s ago
       Docs: man:nginx(8)
    Process: 7836 ExecStartPre=/usr/sbin/nginx -t -q -g daemon on; master_process on; (code=exited, >
    Process: 7837 ExecStart=/usr/sbin/nginx -g daemon on; master_process on; (code=exited, status=0/>
   Main PID: 7838 (nginx)
      Tasks: 7 (limit: 6919)
     Memory: 6.3M
        CPU: 39ms
     CGroup: /system.slice/nginx.service
             7838 "nginx: master process /usr/sbin/nginx -g daemon on; master_process on;"
             7839 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "">
             7840 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "">
             7841 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "">
             7842 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "">
             7843 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "">
             7844 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "">
```

If you open your browser and point it to http://localhost/aarch64app you should see the hello world message.

{{% notice Note %}}
For more detailed installation information, refer to [the Django documentation](https://docs.djangoproject.com/en/4.2/howto/deployment/).
{{% /notice %}}

The Django application is now served via Nginx and connected
to PostgreSQL.
