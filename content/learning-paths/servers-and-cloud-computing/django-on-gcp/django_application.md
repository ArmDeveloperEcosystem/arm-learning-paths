---
title: Build a Django REST API with PostgreSQL and Redis
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Django REST API with PostgreSQL and Redis
This guide walks you through building a **production-ready Django REST API** that connects to **PostgreSQL for data** and **Redis for caching**.  
You will create a backend that is **cloud-deployable** and compatible with **containerized Kubernetes environments**.

### Create Django Project
This step sets up a clean Python virtual environment and installs all runtime dependencies required for Django, PostgreSQL, Redis, and production serving via Gunicorn.

```console
mkdir ~/django_api && cd ~/django_api
python3 -m venv venv
source venv/bin/activate
sudo zypper install postgresql-devel libpq5 postgresql15-server-devel gcc make python3-devel
which pg_config
pip install psycopg2-binary django djangorestframework psycopg2-binary django-redis gunicorn
```

```console
django-admin startproject django_api .
django-admin startapp api
```
You now have a Django project skeleton with all required libraries installed for database, cache, and API support.

### Enable Django Apps
Django must be told which components are active. We enable the REST framework and the API app so that Django can expose HTTP endpoints.
Edit `django_api/settings.py` and add 'rest_framework' and 'api' to INSTALLED_APPS. Set DEBUG to False. Finally add '*' to ALLOWED_HOSTS. 

```python
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

DEBUG = False

ALLOWED_HOSTS = ["*"]
```
Your Django project is now configured to run as an API server instead of a development-only web app.

**Configure PostgreSQL & Redis**

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

Additionally, add the CACHES configuration per below to the same file and save:

```python
CACHES = {
 "default": {
   "BACKEND": "django_redis.cache.RedisCache",
   "LOCATION": "redis://REDIS_IP:6379/1",
 }
}
```

Your application is now wired to a real database and cache, making it production-grade.

### Migrate Database
Django creates tables, metadata, and user models inside PostgreSQL.

```console
python manage.py migrate
python manage.py createsuperuser
```
PostgreSQL instance now contains all Django system tables and is ready to store application data.

### Create Health API
A health endpoint allows Kubernetes and load balancers to verify if the service is running.

Add code below in `api/views.py` file

```console
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET"])
def health(request):
    return Response({"status":"ok"})
```

`django_api/urls.py`

```console
from django.urls import path
from api.views import health

urlpatterns = [
    path("healthz/", health),
]
```
You now have a Kubernetes-compatible health endpoint.

### Validate Locally
Before containerizing or deploying, you validate that everything works end-to-end.

```console
python manage.py runserver 0.0.0.0:8000
curl http://127.0.0.1:8000/healthz/
```
**You must see:**

```output
{"status":"ok"}
```
Your Django API is fully functional with PostgreSQL and Redis connected.

### What you've accomplished
You now have a cloud-ready Django REST API that:

- Uses PostgreSQL for durable data
- Uses Redis for caching
- Exposes a health endpoint for Kubernetes
- Is ready to be containerized and deployed on GKE Axion (Arm)

This is the exact backend you will deploy in the next stage of the learning path.

