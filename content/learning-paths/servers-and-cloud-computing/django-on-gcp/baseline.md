---
title: Verify Django installation and run the development server
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Verify Django is working on your Arm-based VM

In this section, you'll confirm that Django is installed correctly and can serve web requests on your Google Cloud C4A VM. You'll create a Django project, run the development server, and access it from your browser. This hands-on verification ensures your environment is ready for development and testing.

By the end of this section, you'll have:
- Created a Django project with proper directory structure
- Configured Django to accept requests from your VM's external IP
- Run the development server and accessed it from your browser
- Built a simple Django app with custom routing and views
- Verified that Django can handle HTTP requests and render responses

Let's get started!

## Create and test a basic Django project

Run the following command to create a new Django project named `myproject`:

```console
django-admin startproject myproject
cd myproject
```

This generates the following directory structure:

```markdown
myproject/
├── manage.py
└── myproject/
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

The `manage.py` file is Django's command-line utility for project management. The inner `myproject/` folder contains your project's core settings and URL configuration.

## Run initial database migrations

Set up your project's database by running migrations, which create the required tables for Django's built-in apps:

```console
python3 manage.py migrate
```

The output shows all migrations applied successfully (marked "OK").

## Configure ALLOWED_HOSTS for external access

Before starting the Django development server, you must configure your `ALLOWED_HOSTS` setting to allow access from your VM's external IP. This ensures that Django accepts HTTP requests from outside localhost (for example, when testing in a browser from another machine).

Navigate to your project settings directory:

```console
cd ~/myproject/myproject/
```

Open `settings.py` using a text editor:

  ```console
  edit myproject/settings.py
  ```
  
- Locate the `ALLOWED_HOSTS` Line
  Inside the file, find the following line:

```python
ALLOWED_HOSTS = []
```

Update it to allow your VM's external IP address:

- Allow All Hosts (for Testing Only)
  To make your Django app accessible from your VM’s external IP address, update it to:
  ```python
  ALLOWED_HOSTS = ['*']
  ```
{{% notice Note %}}
For development and testing only, you can use `ALLOWED_HOSTS = ['*']` to allow all hosts. However, for production deployments, always specify explicit domain names or IP addresses such as `ALLOWED_HOSTS = ['your-external-ip', 'your-domain.com']`.
{{% /notice %}}

```python
ALLOWED_HOSTS = ['your-external-ip', 'your-domain.com']
```

Now that you've configured `ALLOWED_HOSTS`, start the development server:

```console
python3 manage.py runserver 0.0.0.0:8000
```

This starts the Django development server on port 8000, listening on all network interfaces.

## Access Django in your browser

Open a web browser on your local machine and navigate to:

```
http://<YOUR_VM_EXTERNAL_IP>:8000
```

Replace `<YOUR_VM_EXTERNAL_IP>` with the public IP address of your GCP VM.

You should see the Django welcome page with the message "The install worked successfully!":

![Screenshot of the Django welcome page displayed in a web browser. The page features a large heading stating The install worked successfully followed by a subheading congratulating the user on successfully installing Django. Below are instructions for the next steps, including editing the settings file and reading the Django documentation. The page has a clean white background with blue highlights. alt-text#center](images/django-welcome-page.png "Django welcome page")

## Build a simple Django app with custom routing

This section demonstrates that Django's application routing and view rendering work correctly by creating a simple app with a custom view.

## Stop the server

Press **Ctrl + C** in your terminal to stop the Django development server.

## Create a new Django app

Within your Django project directory, create a new app named `hello`:

```console
python3 manage.py startapp hello
```

This generates the following directory structure with files for views, models, configuration, and more:

```output
hello/
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── views.py
└── urls.py
```

## Define a view function

Edit `hello/views.py` and replace the entire file with:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello, Django on GCP SUSE ARM64!</h1>")
```

This simple view function returns a basic HTML message as an HTTP response.

## Create URL configuration for your app

Create a new file `hello/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

This maps the root URL path to your `home()` view function.

## Include the app in your project's main URLs

Edit `myproject/urls.py` to include the `hello` app's URLs:

```python
"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hello.urls')),
]
```

This tells Django to route the root path to your `hello` app.

## Register the app in Django settings

Django needs to know about your new app. Edit `myproject/settings.py` and add `'hello'` to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hello',
]
```

## Start the server again

Restart the Django development server:

```console
python3 manage.py runserver 0.0.0.0:8000
```

## Test your custom app

Open your browser and navigate to:

```
http://<YOUR_VM_EXTERNAL_IP>:8000
```

You should now see your custom message displayed:

![Screenshot of a web browser displaying a Django app with a large heading that reads Hello, Django on Arm centered on a clean white background. The page contains no additional content or navigation, creating a straightforward and welcoming tone. alt-text#center](images/django-app.png "Django custom app")

## Summary and what's next

You've successfully verified that Django is installed and working on your Arm-based VM. Your application can serve web requests, handle routing, and render custom views. Great job, you're ready to benchmark your Django application!
