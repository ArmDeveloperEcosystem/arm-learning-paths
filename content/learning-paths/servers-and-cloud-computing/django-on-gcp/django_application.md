---
title: Build a Django REST API with PostgreSQL and Redis
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Django REST API with PostgreSQL and Redis

This guide walks you through building a production-ready Django REST API that connects to PostgreSQL for data and Redis for caching. You will create a backend that is cloud-deployable and compatible with containerized Kubernetes environments.

### Create Django project

Set up a clean Python virtual environment and install all runtime dependencies required for Django, PostgreSQL, Redis, and production serving with Gunicorn.

```bash
mkdir ~/django_api && cd ~/django_api
python3 -m venv venv
source venv/bin/activate
sudo zypper install postgresql-devel libpq5 postgresql15-server-devel gcc make python3-devel
```

Also, please run:

```bash
which pg_config
pip install psycopg2-binary django djangorestframework psycopg2-binary django-redis gunicorn
```

Finally, run:

```bash
django-admin startproject django_api .
django-admin startapp api
```

The Django project structure is ready with all required libraries for database, cache, and API support.

### Enable Django apps

Django must be told which components are active. Enable the REST framework and the API app so that Django can expose HTTP endpoints. Edit `django_api/settings.py` and add 'rest_framework' and 'api' to INSTALLED_APPS. Set DEBUG to False. Finally add '*' to ALLOWED_HOSTS. 

```python
DEBUG = False

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
 'django.contrib.admin',
 'django.contrib.auth',
 'django.contrib.contenttypes',
 'django.contrib.sessions',
 'django.contrib.messages',
 'django.contrib.staticfiles',
 'rest_framework',
 'api',
]
```

Django is configured to run as an API server.

### Configure PostgreSQL and Redis

This step connects Django to external managed services instead of local SQLite. This mirrors how real production systems operate.

Edit `django_api/settings.py` and replace the DATABASES configuration with this:  

```python
DATABASES = {
 'default': {
   'ENGINE': 'django.db.backends.postgresql',
   'NAME': 'django_db',
   'USER': 'django_user',
   'PASSWORD': 'password',
   'HOST': 'CLOUDSQL_IP',
   'PORT': '5432',
 }
}
```

Edit the above addition and set "CLOUDSQL_IP" to the actual IP address that you saved from earlier. 

Additionally, add the CACHES configuration per below to the same file and save:

```python
CACHES = {
 "default": {
   "BACKEND": "django_redis.cache.RedisCache",
   "LOCATION": "redis://REDIS_IP:6379/1",
 }
}
```

Edit the above addition and set `REDIS_IP` to the actual IP address that you saved earlier.

The application is configured to use PostgreSQL and Redis.

### Migrate the database
Django creates tables, metadata, and user models inside PostgreSQL.

```bash
python manage.py migrate
python manage.py createsuperuser
```

The PostgreSQL instance contains all Django system tables.

### Create a health API endpoint

A health endpoint allows Kubernetes and load balancers to verify if the service is running.

Add code below in `api/views.py` file:

```python
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET"])
def health(request):
    return Response({"status":"ok"})
```

Add code below in `django_api/urls.py` file:

```python
from django.urls import path
from api.views import health

urlpatterns = [
    path("healthz/", health),
]
```

The health endpoint is configured.

### Validate locally
Before containerizing or deploying, validate that everything works end-to-end.

```bash
python manage.py runserver 0.0.0.0:8000
```

In a separate SSH session, run:

```bash
curl http://127.0.0.1:8000/healthz/
```

The expected output is:

```output
{"status":"ok"}
```

The Django API is functional with PostgreSQL and Redis connected.

## What you've accomplished and what's next

In this section, you built a cloud-ready Django REST API that:

- Uses PostgreSQL for persistent data storage
- Uses Redis for caching
- Exposes a health endpoint for Kubernetes probes
- Is ready for containerization and deployment on GKE Axion

Next, you'll containerize this application and deploy it to your Axion-powered GKE cluster.

