
## +Udemy - Django A-Z Build and Deploy Web Project

## [COURSE](https://www.udemy.com/course/complete-django-masterclass/)

<details>
<summary>1. Creating a New Django Project </summary>

# Creating a New Django Project

## Install venv

```py
python -m venv myproject-env
```

## Activate venv

```py
# myproject-env\Scripts\activate
source myproject-env/bin/activate
```

## Install Django

```py
python -m pip install Django
pip install django
pip install django==5.0
```

## Get dependencies

```py
pip freeze
```

```x
asgiref==3.7.2
Django==5.0.3
sqlparse==0.4.4
```

## Save Dependencies to Requirements.txt

```py
pip freeze > requirements.txt
```

## Install requirements from Requirements.txt

```py
pip install -r requirements.txt
```

## Deactivate a virtual environment

```py
deactivate
```

## Create Django Project

```py
django-admin startproject taskmate .
```

## Make Migrations

```py
python manage.py makemigrations
python manage.py migrate
```

## Start Local Server

```py
python manage.py runserver
```

```x
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
April 03, 2024 - 19:56:32
Django version 5.0.4, using settings 'taskmate.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/22df5e9a-3927-4360-bffc-40c6cfb95033)

<img width="1529" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e087d565-d986-4697-b1d6-3e1a239d5689">

# #END</details>

<details>
<summary>2. Create new App - TodoList </summary>

# Create new App - TodoList

[https://github.com/omeatai/src-python-flask-django/commit/fbf231bb53a548dc15c021d4041212fa10ffc13b](https://github.com/omeatai/src-python-flask-django/commit/fbf231bb53a548dc15c021d4041212fa10ffc13b)

## Create App

```py
python manage.py startapp todolist
django-admin startapp todolist
```

### taskmate.settings:

```x
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # apps
    'todolist',
]
```

<img width="1529" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/0df79c8a-1bcd-44c9-8941-cae421178859">

# #END</details>

<details>
<summary>3. Create Urls and Views </summary>

# Create Urls and Views

### taskmate.urls:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', include('todolist.urls')),
]
```

### todolist.urls:

```py
from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.todolist, name="todolist"),
]
```

### todolist.views:

```py
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def todolist(request):
    return HttpResponse("<h1>Welcome to the Task Page</h1>")
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/00dc48de-9654-4228-9306-b1e13ebdebef)
<img width="1529" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/428fa1e7-2306-4ed8-8d4d-92f0aff97760">
<img width="1529" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e0b80bad-7cdc-4a7c-b993-0d9fd4a5ccd2">
<img width="1529" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ca3b2339-c5b3-41b8-a5cd-6bf04e8e7dd6">

# #END</details>

<details>
<summary>4. Create Template </summary>

# Create Template

[https://github.com/omeatai/src-python-flask-django/commits/main/](https://github.com/omeatai/src-python-flask-django/commits/main/)

### todolist.urls:

```py
from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.todolist, name="todolist"),
]

```

### todolist.views:

```py
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def todolist(request):
    # return HttpResponse("<h1>Welcome to the Task Page</h1>")
    return render(request, 'todolist.html', {})

```

### src-python/udemy/django-A-Z/todolist/templates/todolist.html:

```py
<h1>Welcome to the New Task Page on Template!</h1>
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/d396c262-ed1e-4f1c-bf43-fa520ea9c3af)

<img width="1473" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/cfbc6f64-928f-4080-ba25-8ebcc3d0a6de">
<img width="1473" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/4dd585bd-dfd6-4303-8744-62592671234a">
<img width="1473" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/86cd6c65-0954-43fd-a751-6a9473475cf4">

# #END</details>

<details>
<summary>5. Using Bootstrap Template </summary>

# Using Bootstrap Template

[https://github.com/omeatai/src-python-flask-django/commit/5e9fe522da16c264556fb6d4e37d64bb80d1747b](https://github.com/omeatai/src-python-flask-django/commit/5e9fe522da16c264556fb6d4e37d64bb80d1747b)

## Bootstrap Main Template

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Bootstrap demo</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
      crossorigin="anonymous"
    />
  </head>
  <body>
    <h1>Hello, world!</h1>
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```

## Navbar Template

```html
<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button
      class="navbar-toggler"
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#navbarNav"
      aria-controls="navbarNav"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Features</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Pricing</a>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" aria-disabled="true">Disabled</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
```

### src-python/udemy/django-A-Z/todolist/templates/todolist.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />

    <!-- Bootstrap CSS -->
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ"
      crossorigin="anonymous"
    />

    <title>Todo List - Taskmate</title>
  </head>

  <body>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Navbar</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="#">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Features</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Pricing</a>
            </li>
            <li class="nav-item">
              <a class="nav-link disabled" aria-disabled="true">Disabled</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <main class="container">
      <h1>Welcome to the New Task Page on Template!</h1>
    </main>

    <!-- Optional JavaScript; choose one of the two! -->
    <!-- jQuery and Bootstrap Bundle (includes Popper) -->
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/446ff51f-5e68-4fab-9ee5-1b2cd918856d)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/34ea1c8a-0430-4406-8548-f7a842f7633c)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/e975baa4-d57f-4a83-9615-bfe89045f5eb)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/4f3ff341-162f-41c5-baa4-37f70e1ee5ae)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/c34349cd-1660-490d-8a99-3960b0e1360b)

<img width="1473" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/7e064467-6a7e-46d9-9b8b-4a40e7aeea92">

# #END</details>

<details>
<summary>6. Base Templating with Jinja 2 </summary>

# Base Templating with Jinja 2

[https://github.com/omeatai/src-python-flask-django/commits/main/](https://github.com/omeatai/src-python-flask-django/commits/main/)

### taskmate.settings:

```py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [BASE_DIR / 'templates'],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### taskmate.urls:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', include('todolist.urls')),
]

```

### todolist.urls:

```py
from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.todolist, name="todolist"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
]

```

### todolist.views:

```py
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def todolist(request):
    context = {
        "welcome_text": "Welcome to your Todo List!"
    }
    # return HttpResponse("<h1>Welcome to the Task Page</h1>")
    return render(request, 'todolist.html', context)


def about(request):
    context = {
        "welcome_text": "Welcome to the About Page!"
    }
    return render(request, 'about.html', context)


def contact(request):
    context = {
        "welcome_text": "Welcome to the Contact Page!"
    }
    return render(request, 'contact.html', context)

```

### src-python/udemy/django-A-Z/templates/todolist/base.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />

    <!-- Bootstrap CSS -->
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ"
      crossorigin="anonymous"
    />

    <title>Todo List Manager - {% block title %}{% endblock title %}</title>
  </head>

  <body>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Task Mate</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a
                class="nav-link active"
                aria-current="page"
                href="{% url 'todolist' %}"
                >Home</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'todolist' %}">Todo List</a>
              {% comment %} <a class="nav-link" href="/task">Todo List</a> {%
              endcomment %}
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'about' %}">About Us</a>
              {% comment %}
              <a class="nav-link" href="/task/about">About Us</a> {% endcomment
              %}
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'contact' %}">Contact Us</a>
              {% comment %}
              <a class="nav-link" href="/task/contact">Contact Us</a> {%
              endcomment %}
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <main class="container">
      <h1>Taskmate</h1>
      {% block content %} {% endblock content %}
    </main>

    <!-- Optional JavaScript; choose one of the two! -->
    <!-- jQuery and Bootstrap Bundle (includes Popper) -->
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```

### src-python/udemy/django-A-Z/todolist/templates/todolist.html:

```html
{% extends "todolist/base.html" %} {% block title %} Welcome {% endblock title
%} {% block content %}
<h2>{{ welcome_text }}</h2>
{% endblock content %}
```

### src-python/udemy/django-A-Z/todolist/templates/about.html:

```html
{% extends "todolist/base.html" %} {% block title %} About Us {% endblock title
%} {% block content %}
<h2>{{ welcome_text }}</h2>
{% endblock content %}
```

### src-python/udemy/django-A-Z/todolist/templates/contact.html:

```html
{% extends "todolist/base.html" %} {% block title %} Contact Us {% endblock
title %} {% block content %}
<h2>{{ welcome_text }}</h2>
{% endblock content %}
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/cf0018f9-f76d-4331-9a12-6e593e93388b)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/4c1a659a-e02e-4100-bd7d-e8642b1827b5)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/c3df0c22-7edc-4e21-912d-f3d99900780b)
<img width="1429" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/404412e4-8604-4713-8743-16acc5cb9ac5">
<img width="1473" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a17c5e5f-fcbc-4441-8ed1-f9f7072c28f4">
<img width="1473" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/95719a7d-890b-4a25-bbc3-2c6c89c8b1dc">
<img width="1473" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/15c80222-f800-406c-828f-c4c8bc2ce164">
<img width="1473" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/958b11f8-8a51-4bf7-9248-72d3a4c4a14a">
<img width="1473" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e5d94c38-773f-4bef-aeb3-68d5e0eed1cd">
<img width="1473" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/82861d69-ab2b-4767-9e65-fe2017da7056">
<img width="1473" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/c2707449-f9fe-44c6-bd18-412d76ada279">

# #END</details>

<details>
<summary>7. Setup Static Folder </summary>

# Setup Static Folder

[https://github.com/omeatai/src-python-flask-django/commit/b727b0e70a83ddb22c3cc2845e28d8128f0a19b9](https://github.com/omeatai/src-python-flask-django/commit/b727b0e70a83ddb22c3cc2845e28d8128f0a19b9)

### taskmate.settings:

```py
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

### src-python/udemy/django-A-Z/templates/todolist/base.html:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />

    <!-- Bootstrap CSS -->
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ"
      crossorigin="anonymous"
    />

    <title>Todo List Manager - {% block title %}{% endblock title %}</title>
  </head>

  <body>
    <nav class="navbar navbar-expand-lg bg-body-dark navbar-dark bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="{% url 'todolist' %}"
          ><img
            src="{% static 'todolist/images/logo-1.png' %}"
            alt="Taskmate Logo"
        /></a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a
                class="nav-link active"
                aria-current="page"
                href="{% url 'todolist' %}"
                >Home</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'todolist' %}">Todo List</a>
              {% comment %} <a class="nav-link" href="/task">Todo List</a> {%
              endcomment %}
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'about' %}">About Us</a>
              {% comment %}
              <a class="nav-link" href="/task/about">About Us</a> {% endcomment
              %}
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'contact' %}">Contact Us</a>
              {% comment %}
              <a class="nav-link" href="/task/contact">Contact Us</a> {%
              endcomment %}
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <main class="container">
      <h1>Taskmate</h1>
      {% block content %} {% endblock content %}
    </main>

    <!-- Optional JavaScript; choose one of the two! -->
    <!-- jQuery and Bootstrap Bundle (includes Popper) -->
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```

### src-python/udemy/django-A-Z/todolist/templates/todolist.html:

```py
{% extends "todolist/base.html" %}

{% block title %}
Welcome
{% endblock title %}

{% block content %}
<h2>{{ welcome_text }}</h2>
{% endblock content %}
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/a2277918-c10d-4288-9da7-5b432584721b)

<img width="1473" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/9df594d4-54de-4364-82f0-3a284055392f">
<img width="1473" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/3bc02c76-03e0-4a8f-9378-a031239ecf0b">
<img width="1473" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b220e88c-809f-41f0-8ae3-09afe5965650">

# #END</details>

<details>
<summary>8. Create Super User for Admin Panel </summary>

# Create Super User for Admin Panel

## Create Super User

```py
python manage.py createsuperuser
```

## Run Local Server

```py
python manage.py runserver
```

<img width="510" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/77949caa-8709-4791-a7e5-2afdec7fba00">
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/b0543452-5fe3-4bcb-82fa-383316494102)
<img width="1400" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/6f3861bb-a0fb-4586-81ce-ef572f8a5222">

# #END</details>

<details>
<summary>9. Setup Django Model and Migration </summary>

# Setup Django Model and Migration

[https://github.com/omeatai/src-python-flask-django/commit/d3985ea132dfa34bb55905b46db68e27b9d763b3](https://github.com/omeatai/src-python-flask-django/commit/d3985ea132dfa34bb55905b46db68e27b9d763b3)

### todolist.models:

```py
from django.db import models

# Create your models here.


class TaskList(models.Model):
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    # description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

```

### todolist.admin:

```py
from django.contrib import admin
from .models import TaskList

# Register your models here.
admin.site.register(TaskList)

```

## Make Migrations

```py
python manage.py makemigrations
python manage.py migrate
```

## Run Local Server

```py
python manage.py runserver
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/f69b55f9-7c06-45d9-b90f-95705d619746)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/efc83b7a-c85c-46fd-9381-3d673105a4ee)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/cc5ba05b-068b-4920-8670-f7abc38f04ad)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/1ec8e6a8-e448-4bc6-a8f9-2d296a99fbd5)

<img width="1400" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/6c89310a-d2c6-4e4b-9ebb-a82cf387cab9">
<img width="1400" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/addfbe9c-e4ae-4dd3-af38-f60ee9b8d031">

# #END</details>

<details>
<summary>10. Fetch Data from Database </summary>

# Fetch Data from Database

[https://github.com/omeatai/src-python-flask-django/commit/36b1e3ea6eecc65fecc913682d0829684a876ebd](https://github.com/omeatai/src-python-flask-django/commit/36b1e3ea6eecc65fecc913682d0829684a876ebd)

[https://getbootstrap.com/docs/5.3/content/tables/](https://getbootstrap.com/docs/5.3/content/tables/)

## Bootstrap Table Format:

```html
<table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">First</th>
      <th scope="col">Last</th>
      <th scope="col">Handle</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>Mark</td>
      <td>Otto</td>
      <td>@mdo</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>Jacob</td>
      <td>Thornton</td>
      <td>@fat</td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td colspan="2">Larry the Bird</td>
      <td>@twitter</td>
    </tr>
  </tbody>
</table>
```

### todolist.views:

```py
from django.shortcuts import render
from django.http import HttpResponse
from .models import TaskList
# Create your views here.


def todolist(request):
    tasks = TaskList.objects.all()
    context = {
        'tasks': tasks,
        "welcome_text": "Welcome to your Todo List!"
    }
    # return HttpResponse("<h1>Welcome to the Task Page</h1>")
    return render(request, 'todolist.html', context)


def about(request):
    context = {
        "welcome_text": "Welcome to the About Page!"
    }
    return render(request, 'about.html', context)


def contact(request):
    context = {
        "welcome_text": "Welcome to the Contact Page!"
    }
    return render(request, 'contact.html', context)

```

### src-python/udemy/django-A-Z/todolist/templates/todolist.html:

```html
{% extends "todolist/base.html" %} {% block title %} Welcome {% endblock title
%} {% block content %}
<h2>{{ welcome_text }}</h2>

{% comment %}
<table class="table table-dark table-striped">
  {% endcomment %}
  <table class="table table-light table-striped table-hover table-bordered">
    <thead>
      <tr class="table-dark">
        <th scope="col">Task</th>
        <th scope="col">Done</th>
        <th scope="col">Edit</th>
        <th scope="col">Delete</th>
      </tr>
    </thead>
    <tbody>
      {% for todo in tasks %} {% if todo.done %}
      <tr class="table-success">
        <th scope="row">{{ todo.task }}</th>
        <td>YES</td>
        <td>
          <a href="" type="button" class="btn btn-warning btn-sm">Edit</a>
        </td>
        <td>
          <a href="" type="button" class="btn btn-danger btn-sm">Delete</a>
        </td>
      </tr>
      {% else %}
      <tr>
        <th scope="row">{{ todo.task }}</th>
        <td>NO</td>
        <td>
          <a href="" type="button" class="btn btn-warning btn-sm">Edit</a>
        </td>
        <td>
          <a href="" type="button" class="btn btn-danger btn-sm">Delete</a>
        </td>
      </tr>
      {% endif %} {% endfor %}
    </tbody>
  </table>

  {% for todo in tasks %}
  <div class="todo">
    <h3>{{ todo.task }} - {{ todo.done }}</h3>
  </div>

  {% endfor %} {% endblock content %}
</table>
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/02124501-e51e-44a8-9433-e90626c05762)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/1eec6917-7f8f-4ef9-8c26-b6f16b130988)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/a04a4aed-1075-4144-b7e2-db3cb0cc7cbb)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/db8b9ea7-1016-44a0-8550-646e391acd3c)

<img width="1400" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/9c32960b-e69b-4f62-8313-e599cb6771b5">
<img width="1400" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/5049d062-2360-44a7-a134-414b3d9c14b5">

# #END</details>

<details>
<summary>11. Using Django Forms to Create Tasks </summary>

# Using Django Forms to Create Tasks

[https://getbootstrap.com/docs/5.3/forms/overview/](https://getbootstrap.com/docs/5.3/forms/overview/)

## Bootstrap Form Format:

```html
<form>
  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Email address</label>
    <input
      type="email"
      class="form-control"
      id="exampleInputEmail1"
      aria-describedby="emailHelp"
    />
    <div id="emailHelp" class="form-text">
      We'll never share your email with anyone else.
    </div>
  </div>
  <div class="mb-3">
    <label for="exampleInputPassword1" class="form-label">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1" />
  </div>
  <div class="mb-3 form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1" />
    <label class="form-check-label" for="exampleCheck1">Check me out</label>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

### todolist.forms:

```py
from django import forms
from .models import TaskList


class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['task', 'done']

```

### todolist.views:

```py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TaskList
from .forms import TaskForm
# Create your views here.


def todolist(request):
    note = None
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.done = False
            form.save()
        note = "Your new Task has been added successfully!"
    tasks = TaskList.objects.all()
    context = {
        'tasks': tasks,
        "welcome_text": "Welcome to your Todo List!",
        "note": note
    }
    return render(request, 'todolist.html', context)
    # return redirect('todolist')


def about(request):
    context = {
        "welcome_text": "Welcome to the About Page!"
    }
    return render(request, 'about.html', context)


def contact(request):
    context = {
        "welcome_text": "Welcome to the Contact Page!"
    }
    return render(request, 'contact.html', context)

```

### src-python/udemy/django-A-Z/todolist/templates/todolist.html:

```html
{% extends "todolist/base.html" %} {% block title %} Welcome {% endblock title
%} {% block content %}
<h2>{{ welcome_text }}</h2>

<form method="POST" class="my-3">
  {% csrf_token %} {% if note %}
  <div class="alert alert-success" role="alert">{{ note }}</div>
  {% endif %}

  <div class="mb-3">
    <label for="task" class="form-label">Add Task</label>
    <input
      type="text"
      class="form-control"
      id="task"
      name="task"
      aria-describedby="textHelp"
      placeholder="Call Alex..."
    />
    <div id="textHelp" class="form-text">What would you want to do?</div>
  </div>
  <button type="submit" class="btn btn-primary">ADD TASK</button>
</form>

<table class="table table-light table-striped table-hover table-bordered">
  <thead>
    <tr class="table-dark">
      <th scope="col">Task</th>
      <th scope="col">Done</th>
      <th scope="col">Edit</th>
      <th scope="col">Delete</th>
    </tr>
  </thead>
  <tbody>
    {% for todo in tasks %} {% if todo.done %}
    <tr class="table-success">
      <th scope="row">{{ todo.task }}</th>
      <td>YES</td>
      <td><a href="" type="button" class="btn btn-warning btn-sm">Edit</a></td>
      <td><a href="" type="button" class="btn btn-danger btn-sm">Delete</a></td>
    </tr>
    {% else %}
    <tr>
      <th scope="row">{{ todo.task }}</th>
      <td>NO</td>
      <td><a href="" type="button" class="btn btn-warning btn-sm">Edit</a></td>
      <td><a href="" type="button" class="btn btn-danger btn-sm">Delete</a></td>
    </tr>
    {% endif %} {% endfor %}
  </tbody>
</table>

{% endblock content %}
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/8afc0f90-f618-4ac8-aefc-478857e50dbe)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/5d8b4547-5156-43c1-ada2-84d89ea33cdb)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/a0ac350c-628a-4532-bc46-21c48f266abc)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/115ac876-d1e4-40bd-915b-d9b7ffa680a5)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/43c0a4c2-fc8d-4320-b49f-407036a94eba)

<img width="1400" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/57c4415d-d405-448e-9bb8-983c30dc37ca">
<img width="1400" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/def193eb-d990-4848-90eb-41cf3b3820bb">
<img width="1400" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/2095b37c-9c3b-413b-a050-8f9b306bcdfe">
<img width="1400" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/57649b4d-8987-42f7-ab9f-18077b67601b">

# #END</details>

<details>
<summary>12. Using Django Messages for Alert </summary>

# Using Django Messages for Alert

[https://github.com/omeatai/src-python-flask-django/commit/f7595ceae38ddf8f9d4557b33d9dd1385b1d75b4](https://github.com/omeatai/src-python-flask-django/commit/f7595ceae38ddf8f9d4557b33d9dd1385b1d75b4)
[https://getbootstrap.com/docs/5.3/components/alerts/](https://getbootstrap.com/docs/5.3/components/alerts/)

## Bootstrap Alert Formats:

```html
<div class="alert alert-primary" role="alert">
  A simple primary alert—check it out!
</div>
<div class="alert alert-secondary" role="alert">
  A simple secondary alert—check it out!
</div>
<div class="alert alert-success" role="alert">
  A simple success alert—check it out!
</div>
<div class="alert alert-danger" role="alert">
  A simple danger alert—check it out!
</div>
<div class="alert alert-warning" role="alert">
  A simple warning alert—check it out!
</div>
<div class="alert alert-info" role="alert">
  A simple info alert—check it out!
</div>
<div class="alert alert-light" role="alert">
  A simple light alert—check it out!
</div>
<div class="alert alert-dark" role="alert">
  A simple dark alert—check it out!
</div>
```

```html
<div class="alert alert-warning alert-dismissible fade show" role="alert">
  <strong>Holy guacamole!</strong> You should check in on some of those fields
  below.
  <button
    type="button"
    class="btn-close"
    data-bs-dismiss="alert"
    aria-label="Close"
  ></button>
</div>
```

### todolist.views:

```py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import TaskList
from .forms import TaskForm
# Create your views here.


def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.done = False
            form.save()
            messages.success(
                request, "Awesome! Your new Task has been added successfully!")
        # note = "Your new Task has been added successfully!"
    tasks = TaskList.objects.all()
    context = {
        'tasks': tasks,
        "welcome_text": "Welcome to your Todo List!",
    }
    return render(request, 'todolist.html', context)


def about(request):
    context = {
        "welcome_text": "Welcome to the About Page!"
    }
    return render(request, 'about.html', context)


def contact(request):
    context = {
        "welcome_text": "Welcome to the Contact Page!"
    }
    return render(request, 'contact.html', context)

```

### src-python/udemy/django-A-Z/todolist/templates/todolist.html:

```html
{% extends "todolist/base.html" %} {% block title %} Welcome {% endblock title
%} {% block content %}
<h2>{{ welcome_text }}</h2>

<form method="POST" class="my-3">
  {% csrf_token %} {% if messages %} {% for message in messages %} {% comment %}
  <div class="alert alert-success" role="alert">{{ message }}</div>
  {% endcomment %}

  <div class="alert alert-success alert-dismissible fade show" role="alert">
    {{ message }}
    <button
      type="button"
      class="btn-close"
      data-bs-dismiss="alert"
      aria-label="Close"
    ></button>
  </div>

  {% endfor %} {% endif %}

  <div class="mb-3">
    <label for="task" class="form-label">Add Task</label>
    <input
      type="text"
      class="form-control"
      id="task"
      name="task"
      aria-describedby="textHelp"
      placeholder="Call Alex..."
    />
    <div id="textHelp" class="form-text">What would you want to do?</div>
  </div>
  <button type="submit" class="btn btn-primary">ADD TASK</button>
</form>

<table class="table table-light table-striped table-hover table-bordered">
  <thead>
    <tr class="table-dark">
      <th scope="col">Task</th>
      <th scope="col">Done</th>
      <th scope="col">Edit</th>
      <th scope="col">Delete</th>
    </tr>
  </thead>
  <tbody>
    {% if tasks %} {% for todo in tasks %} {% if todo.done %}
    <tr class="table-success">
      <th scope="row">{{ todo.task }}</th>
      <td>YES</td>
      <td><a href="" type="button" class="btn btn-warning btn-sm">Edit</a></td>
      <td><a href="" type="button" class="btn btn-danger btn-sm">Delete</a></td>
    </tr>
    {% else %}
    <tr>
      <th scope="row">{{ todo.task }}</th>
      <td>NO</td>
      <td><a href="" type="button" class="btn btn-warning btn-sm">Edit</a></td>
      <td><a href="" type="button" class="btn btn-danger btn-sm">Delete</a></td>
    </tr>
    {% endif %} {% endfor %} {% endif %}
  </tbody>
</table>

{% endblock content %}
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/517a9dd3-823e-4dc7-8e85-fd193c699f63)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/60adead8-b2cd-4e83-b129-b5298b2456f7)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/161b66c4-e1d9-44b2-8990-a23df0dc86ae)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/2d72e0aa-bc86-4224-86ca-32689a5c77d5)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/75d1697b-d560-48e8-901f-eebc11d6324c)

<img width="1400" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b0974a5c-390b-4a5b-a2c6-644c8b35ef1b">
<img width="1400" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/4cb1326a-a41b-45cd-b6b3-486e82eaffed">

# #END</details>

<details>
<summary>13. Delete Tasks </summary>

# Delete Tasks

[https://github.com/omeatai/src-python-flask-django/commit/9eb57b3f196c9a625b1883007a9d963ca70b3d03](https://github.com/omeatai/src-python-flask-django/commit/9eb57b3f196c9a625b1883007a9d963ca70b3d03)

### todolist.urls:

```py
from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.todolist, name="todolist"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('delete/<int:id>', views.delete_task, name="delete-task"),
]

```

### todolist.views:

```py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import TaskList
from .forms import TaskForm
# Create your views here.


def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.done = False
            form.save()
            messages.success(
                request, "Awesome! Your new Task has been added successfully!")
        # note = "Your new Task has been added successfully!"
    tasks = TaskList.objects.all()
    context = {
        'tasks': tasks,
        "welcome_text": "Welcome to your Todo List!",
    }
    return render(request, 'todolist.html', context)


def delete_task(request, id):
    task = TaskList.objects.get(pk=id)
    task.delete()
    messages.success(request, "Task has been deleted successfully!")
    return redirect('todolist')


def about(request):
    context = {
        "welcome_text": "Welcome to the About Page!"
    }
    return render(request, 'about.html', context)


def contact(request):
    context = {
        "welcome_text": "Welcome to the Contact Page!"
    }
    return render(request, 'contact.html', context)

```

### src-python/udemy/django-A-Z/todolist/templates/todolist.html:

```py
{% extends "todolist/base.html" %}

{% block title %}
Welcome
{% endblock title %}

{% block content %}
<h2>{{ welcome_text }}</h2>

<form method="POST" class="row my-3">
    {% csrf_token %}

    {% if messages %}

    {% for message in messages %}
    {% comment %} <div class="alert alert-success" role="alert">
        {{ message }}
    </div> {% endcomment %}

    <div class="alert alert-success alert-dismissible fade show" role="alert">
        {{ message }}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>

    {% endfor %}

    {% endif %}

    <div class="mb-3">
        <label for="task" class="form-label">Add Task</label>
        <input type="text" class="form-control" id="task" name="task" aria-describedby="textHelp"
            placeholder="Call Alex...">
        <div id="textHelp" class="form-text">What would you want to do?</div>
    </div>
    <button type="submit" class="btn btn-primary">ADD TASK</button>
</form>


<table class="table table-light table-striped table-hover table-bordered">
    <thead>
        <tr class="table-dark">
            <th scope="col">Task</th>
            <th scope="col">Done</th>
            <th scope="col">Edit</th>
            <th scope="col">Delete</th>
        </tr>
    </thead>
    <tbody>
        {% if tasks %}

        {% for todo in tasks %}

        {% if todo.done %}
        <tr class="table-success">
            <th scope="row">{{ todo.id }} | {{ todo.task }}</th>
            <td>YES</td>
            <td><a href="" type="button" class="btn btn-warning btn-sm">Edit</a></td>
            <td><a href="{% url 'delete-task' todo.id %}" type="button" class="btn btn-danger btn-sm">Delete</a></td>
        </tr>
        {% else %}
        <tr>
            <th scope="row">{{ todo.id }} | {{ todo.task }}</th>
            <td>NO</td>
            <td><a href="" type="button" class="btn btn-warning btn-sm">Edit</a></td>
            <td><a href="{% url 'delete-task' todo.id %}" type="button" class="btn btn-danger btn-sm">Delete</a></td>
        </tr>
        {% endif %}

        {% endfor %}

        {% endif %}
    </tbody>
</table>


{% endblock content %}
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/d8037a7b-5c93-4ae2-81b0-2fb983c5289b)

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a1daed4b-7fd1-4b94-86fd-d227b4e87a3a">
<img width="1441" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/3bddcff2-4dc8-4606-a86c-b07ea8221247">
<img width="1441" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/878de8d9-5022-4a11-b3fb-9e270bfb9849">
<img width="1441" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/97d438f0-911b-4b71-9f50-d7d7d8291660">

# #END</details>

<details>
<summary>14. Edit Tasks </summary>

# Edit Tasks

[https://github.com/omeatai/src-python-flask-django/commit/5b431c4a4c4af67bd8b0ed70c091670358ab47be](https://github.com/omeatai/src-python-flask-django/commit/5b431c4a4c4af67bd8b0ed70c091670358ab47be)

### todolist.urls:

```py
from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.todolist, name="todolist"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('edit/<int:id>', views.edit_task, name="edit-task"),
    path('delete/<int:id>', views.delete_task, name="delete-task"),
]

```

### todolist.views:

```py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import TaskList
from .forms import TaskForm
# Create your views here.


def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.done = False
            form.save()
            messages.success(
                request, "Awesome! Your new Task has been added successfully!")
        # note = "Your new Task has been added successfully!"
    tasks = TaskList.objects.all()
    context = {
        'tasks': tasks,
        "welcome_text": "Welcome to your Todo List!",
    }
    return render(request, 'todolist.html', context)


def edit_task(request, id):
    if request.method == "POST":
        form = TaskForm(request.POST or None,
                        instance=TaskList.objects.get(pk=id))
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your new Task has been updated successfully!")
            return redirect('todolist')
    else:
        task = TaskList.objects.get(pk=id)
        context = {
            'task': task,
        }
        return render(request, 'edit.html', context)


def delete_task(request, id):
    task = TaskList.objects.get(pk=id)
    task.delete()
    messages.success(request, "Task has been deleted successfully!")
    return redirect('todolist')


def about(request):
    context = {
        "welcome_text": "Welcome to the About Page!"
    }
    return render(request, 'about.html', context)


def contact(request):
    context = {
        "welcome_text": "Welcome to the Contact Page!"
    }
    return render(request, 'contact.html', context)

```

### src-python/udemy/django-A-Z/todolist/templates/edit.html:

```html
{% extends "todolist/base.html" %} {% block title %} Welcome {% endblock title
%} {% block content %}
<h2>{{ welcome_text }}</h2>

<form method="POST" class="row my-3">
  {% csrf_token %} {% if messages %} {% for message in messages %}

  <div class="alert alert-success alert-dismissible fade show" role="alert">
    {{ message }}
    <button
      type="button"
      class="btn-close"
      data-bs-dismiss="alert"
      aria-label="Close"
    ></button>
  </div>

  {% endfor %} {% endif %}

  <div class="mb-3">
    <label for="task" class="form-label">Edit Task</label>
    <input
      type="text"
      class="form-control"
      id="task"
      name="task"
      value="{{ task.task }}"
      aria-describedby="textHelp"
      placeholder="{{ task.task }}"
    />
    <div id="textHelp" class="form-text">Make your changes</div>
  </div>
  <div class="mb-3">
    {% comment %} <input type="hidden" name="done" value="{{ task.done }}" /> {%
    endcomment %}

    <label for="done" class="form-label">Is it Done?</label>
    <select
      class="form-select"
      id="done"
      name="done"
      aria-label="Default select example"
    >
      <option value="False" {% if not task.done %} selected {% endif %}>
        NO
      </option>
      <option value="True" {% if task.done %} selected {% endif %}>YES</option>
    </select>
  </div>
  <button type="submit" class="btn btn-primary my-2">Update TASK</button>
  <a href="{% url 'todolist' %}" class="btn btn-danger my-2">Back</a>
</form>

{% endblock content %}
```

### src-python/udemy/django-A-Z/todolist/templates/todolist.html:

```html
{% extends "todolist/base.html" %} {% block title %} Welcome {% endblock title
%} {% block content %}
<h2>{{ welcome_text }}</h2>

<form method="POST" class="row my-3">
  {% csrf_token %} {% if messages %} {% for message in messages %} {% comment %}
  <div class="alert alert-success" role="alert">{{ message }}</div>
  {% endcomment %}

  <div class="alert alert-success alert-dismissible fade show" role="alert">
    {{ message }}
    <button
      type="button"
      class="btn-close"
      data-bs-dismiss="alert"
      aria-label="Close"
    ></button>
  </div>

  {% endfor %} {% endif %}

  <div class="mb-3">
    <label for="task" class="form-label">Add Task</label>
    <input
      type="text"
      class="form-control"
      id="task"
      name="task"
      aria-describedby="textHelp"
      placeholder="Call Alex..."
    />
    <div id="textHelp" class="form-text">What would you want to do?</div>
  </div>
  <button type="submit" class="btn btn-primary">ADD TASK</button>
</form>

<table class="table table-light table-striped table-hover table-bordered">
  <thead>
    <tr class="table-dark">
      <th scope="col">Task</th>
      <th scope="col">Done</th>
      <th scope="col">Edit</th>
      <th scope="col">Delete</th>
    </tr>
  </thead>
  <tbody>
    {% if tasks %} {% for todo in tasks %} {% if todo.done %}
    <tr class="table-success">
      <th scope="row">{{ todo.id }} | {{ todo.task }}</th>
      <td>YES</td>
      <td>
        <a
          href="{% url 'edit-task' todo.id %}"
          type="button"
          class="btn btn-warning btn-sm"
          >Edit</a
        >
      </td>
      <td>
        <a
          href="{% url 'delete-task' todo.id %}"
          type="button"
          class="btn btn-danger btn-sm"
          >Delete</a
        >
      </td>
    </tr>
    {% else %}
    <tr>
      <th scope="row">{{ todo.id }} | {{ todo.task }}</th>
      <td>NO</td>
      <td>
        <a
          href="{% url 'edit-task' todo.id %}"
          type="button"
          class="btn btn-warning btn-sm"
          >Edit</a
        >
      </td>
      <td>
        <a
          href="{% url 'delete-task' todo.id %}"
          type="button"
          class="btn btn-danger btn-sm"
          >Delete</a
        >
      </td>
    </tr>
    {% endif %} {% endfor %} {% endif %}
  </tbody>
</table>

{% endblock content %}
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/f1916e5e-8010-43b6-a546-712b9d8b92f2)
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/71fea5e5-ad70-4a76-bd3c-b3a89f3addd8">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/55525c60-ff7b-45f0-8b6e-c914293905d9">
<img width="1441" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b87be038-0546-4ba7-9ca8-b08b3f0d7ac5">
<img width="1441" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1017bfaf-45dd-4cad-a5c6-97386b55a1c2">
<img width="1441" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/bc47c73b-882f-4beb-b4dc-738f1032a1ff">
<img width="1441" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/0f814752-599a-481d-8cfa-523f465d373a">

# #END</details>

<details>
<summary>15. Mark Tasks as Completed or Pending </summary>

# Mark Tasks as Completed or Pending

[https://github.com/omeatai/src-python-flask-django/commit/5b431c4a4c4af67bd8b0ed70c091670358ab47be](https://github.com/omeatai/src-python-flask-django/commit/5b431c4a4c4af67bd8b0ed70c091670358ab47be)

### todolist.urls:

```py
from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.todolist, name="todolist"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('edit/<int:id>', views.edit_task, name="edit-task"),
    path('delete/<int:id>', views.delete_task, name="delete-task"),
    path('completed/<int:id>', views.completed, name="completed"),
    path('pending/<int:id>', views.pending, name="pending"),
]

```

### todolist.views:

```py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import TaskList
from .forms import TaskForm
# Create your views here.


def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.done = False
            form.save()
            messages.success(
                request, "Awesome! Your new Task has been added successfully!")
        # note = "Your new Task has been added successfully!"
    tasks = TaskList.objects.all()
    context = {
        'tasks': tasks,
        "welcome_text": "Welcome to your Todo List!",
    }
    return render(request, 'todolist.html', context)


def edit_task(request, id):
    if request.method == "POST":
        form = TaskForm(request.POST or None,
                        instance=TaskList.objects.get(pk=id))
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your new Task has been updated successfully!")
            return redirect('todolist')
    else:
        task = TaskList.objects.get(pk=id)
        context = {
            'task': task,
        }
        return render(request, 'edit.html', context)


def completed(request, id):
    task = TaskList.objects.get(pk=id)
    task.done = True
    task.save()
    return redirect('todolist')


def pending(request, id):
    task = TaskList.objects.get(pk=id)
    task.done = False
    task.save()
    return redirect('todolist')


def delete_task(request, id):
    task = TaskList.objects.get(pk=id)
    task.delete()
    messages.success(request, "Task has been deleted successfully!")
    return redirect('todolist')


def about(request):
    context = {
        "welcome_text": "Welcome to the About Page!"
    }
    return render(request, 'about.html', context)


def contact(request):
    context = {
        "welcome_text": "Welcome to the Contact Page!"
    }
    return render(request, 'contact.html', context)

```

### src-python/udemy/django-A-Z/todolist/templates/todolist.html:

```html
{% extends "todolist/base.html" %} {% block title %} Welcome {% endblock title
%} {% block content %}
<h2>{{ welcome_text }}</h2>

<form method="POST" class="row my-3">
  {% csrf_token %} {% if messages %} {% for message in messages %} {% comment %}
  <div class="alert alert-success" role="alert">{{ message }}</div>
  {% endcomment %}

  <div class="alert alert-success alert-dismissible fade show" role="alert">
    {{ message }}
    <button
      type="button"
      class="btn-close"
      data-bs-dismiss="alert"
      aria-label="Close"
    ></button>
  </div>

  {% endfor %} {% endif %}

  <div class="mb-3">
    <label for="task" class="form-label">Add Task</label>
    <input
      type="text"
      class="form-control"
      id="task"
      name="task"
      aria-describedby="textHelp"
      placeholder="Call Alex..."
    />
    <div id="textHelp" class="form-text">What would you want to do?</div>
  </div>
  <button type="submit" class="btn btn-primary">ADD TASK</button>
</form>

<table class="table table-light table-striped table-hover table-bordered">
  <thead>
    <tr class="table-dark">
      <th scope="col">Task</th>
      <th scope="col">Done</th>
      <th scope="col">Edit</th>
      <th scope="col">Delete</th>
    </tr>
  </thead>
  <tbody>
    {% if tasks %} {% for todo in tasks %} {% if todo.done %}
    <tr class="table-success">
      <th scope="row">{{ todo.id }} | {{ todo.task }}</th>
      <td>
        <a
          href="{% url 'pending' todo.id %}"
          type="button"
          class="btn btn-success btn-sm"
          >YES - Mark as Pending</a
        >
      </td>
      <td>
        <a
          href="{% url 'edit-task' todo.id %}"
          type="button"
          class="btn btn-warning btn-sm"
          >Edit</a
        >
      </td>
      <td>
        <a
          href="{% url 'delete-task' todo.id %}"
          type="button"
          class="btn btn-danger btn-sm"
          >Delete</a
        >
      </td>
    </tr>
    {% else %}
    <tr>
      <th scope="row">{{ todo.id }} | {{ todo.task }}</th>
      <td>
        <a
          href="{% url 'completed' todo.id %}"
          type="button"
          class="btn btn-danger btn-sm"
          >NO - Mark as Completed</a
        >
      </td>
      <td>
        <a
          href="{% url 'edit-task' todo.id %}"
          type="button"
          class="btn btn-warning btn-sm"
          >Edit</a
        >
      </td>
      <td>
        <a
          href="{% url 'delete-task' todo.id %}"
          type="button"
          class="btn btn-danger btn-sm"
          >Delete</a
        >
      </td>
    </tr>
    {% endif %} {% endfor %} {% endif %}
  </tbody>
</table>

{% endblock content %}
```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a9253b7e-bee3-4fe4-9edd-0430a610fda7">
<img width="1441" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/4b87c611-dde2-4111-ab00-b73fdf9d8d48">
<img width="1441" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/960dc91d-0e91-4be1-ade4-8fcab1eef1f6">
<img width="1441" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/5e982354-79e9-48d9-bf99-64edba4b4e5a">

# #END</details>

<details>
<summary>16. Using Django Pagination </summary>

# Using Django Pagination

[https://github.com/omeatai/src-python-flask-django/commit/6717a9bee64a99ecffe19d9d989a2e6bdb4fd416](https://github.com/omeatai/src-python-flask-django/commit/6717a9bee64a99ecffe19d9d989a2e6bdb4fd416)

## Pagination Format

```html
<nav aria-label="Page navigation example">
  <ul class="pagination justify-content-center">
    <li class="page-item disabled">
      <a class="page-link">Previous</a>
    </li>
    <li class="page-item"><a class="page-link" href="#">1</a></li>
    <li class="page-item"><a class="page-link" href="#">2</a></li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
    <li class="page-item">
      <a class="page-link" href="#">Next</a>
    </li>
  </ul>
</nav>
```

### todolist.urls:

```py
from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.todolist, name="todolist"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('edit/<int:id>', views.edit_task, name="edit-task"),
    path('delete/<int:id>', views.delete_task, name="delete-task"),
    path('completed/<int:id>', views.completed, name="completed"),
    path('pending/<int:id>', views.pending, name="pending"),
]

```

### todolist.models:

```py
from django.db import models

# Create your models here.


class TaskList(models.Model):
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    # description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self) -> str:
        return f"{self.task} - {self.done}"

```

### todolist.views:

```py
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator
from urllib.parse import urlparse, parse_qs

from .models import TaskList
from .forms import TaskForm
# Create your views here.


def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.done = False
            form.save()
            messages.success(
                request, "Awesome! Your new Task has been added successfully!")
        res = redirect('todolist')
    else:
        tasks = TaskList.objects.all()
        no_per_pages = 5
        paginator = Paginator(tasks, no_per_pages)
        page = request.GET.get('pg')
        tasks = paginator.get_page(page)

        context = {
            'tasks': tasks,
            "welcome_text": "Welcome to your Todo List!",
        }
        return render(request, 'todolist.html', context)


def edit_task(request, id):
    if request.method == "POST":
        form = TaskForm(request.POST or None,
                        instance=TaskList.objects.get(pk=id))
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your new Task has been updated successfully!")
            return redirect('todolist')
    else:
        task = TaskList.objects.get(pk=id)
        context = {
            'task': task,
        }
        return render(request, 'edit.html', context)


def completed(request, id):
    task = TaskList.objects.get(pk=id)
    task.done = True
    task.save()
    # GET previous url
    previous_url = request.META.get('HTTP_REFERER')
    parsed_url = urlparse(previous_url)
    query_params = parse_qs(parsed_url.query)
    pg_value = query_params.get('pg', [None])[0]

    res = reverse('todolist') + f"?pg={pg_value}"
    return redirect(res)


def pending(request, id):
    task = TaskList.objects.get(pk=id)
    task.done = False
    task.save()
    # GET previous url
    previous_url = request.META.get('HTTP_REFERER')
    parsed_url = urlparse(previous_url)
    query_params = parse_qs(parsed_url.query)
    pg_value = query_params.get('pg', [None])[0]

    res = reverse('todolist') + f"?pg={pg_value}"
    return redirect(res)
    # return redirect('todolist')


def delete_task(request, id):
    task = TaskList.objects.get(pk=id)
    task.delete()
    messages.success(request, "Task has been deleted successfully!")
    return redirect('todolist')


def about(request):
    context = {
        "welcome_text": "Welcome to the About Page!"
    }
    return render(request, 'about.html', context)


def contact(request):
    context = {
        "welcome_text": "Welcome to the Contact Page!"
    }
    return render(request, 'contact.html', context)

```

### src-python/udemy/django-A-Z/todolist/templates/todolist.html:

```html
{% extends "todolist/base.html" %} {% block title %} Welcome {% endblock title
%} {% block content %}
<h2>{{ welcome_text }}</h2>

<form method="POST" class="row my-3">
  {% csrf_token %} {% if messages %} {% for message in messages %} {% comment %}
  <div class="alert alert-success" role="alert">{{ message }}</div>
  {% endcomment %}

  <div class="alert alert-success alert-dismissible fade show" role="alert">
    {{ message }}
    <button
      type="button"
      class="btn-close"
      data-bs-dismiss="alert"
      aria-label="Close"
    ></button>
  </div>

  {% endfor %} {% endif %}

  <div class="mb-3">
    <label for="task" class="form-label">Add Task</label>
    <input
      type="text"
      class="form-control"
      id="task"
      name="task"
      aria-describedby="textHelp"
      placeholder="Call Alex..."
    />
    <div id="textHelp" class="form-text">What would you want to do?</div>
  </div>
  <button type="submit" class="btn btn-primary">ADD TASK</button>
</form>

<table class="table table-light table-striped table-hover table-bordered">
  <thead>
    <tr class="table-dark">
      <th scope="col">Task</th>
      <th scope="col">Done</th>
      <th scope="col">Edit</th>
      <th scope="col">Delete</th>
    </tr>
  </thead>
  <tbody>
    {% if tasks %} {% for todo in tasks %} {% if todo.done %}
    <tr class="table-success">
      <th scope="row">{{ todo.id }} | {{ todo.task }}</th>
      <td>
        <a
          href="{% url 'pending' todo.id %}"
          type="button"
          class="btn btn-success btn-sm"
          >YES - Mark as Pending</a
        >
      </td>
      <td>
        <a
          href="{% url 'edit-task' todo.id %}"
          type="button"
          class="btn btn-warning btn-sm"
          >Edit</a
        >
      </td>
      <td>
        <a
          href="{% url 'delete-task' todo.id %}"
          type="button"
          class="btn btn-danger btn-sm"
          >Delete</a
        >
      </td>
    </tr>
    {% else %}
    <tr>
      <th scope="row">{{ todo.id }} | {{ todo.task }}</th>
      <td>
        <a
          href="{% url 'completed' todo.id %}"
          type="button"
          class="btn btn-danger btn-sm"
          >NO - Mark as Completed</a
        >
      </td>
      <td>
        <a
          href="{% url 'edit-task' todo.id %}"
          type="button"
          class="btn btn-warning btn-sm"
          >Edit</a
        >
      </td>
      <td>
        <a
          href="{% url 'delete-task' todo.id %}"
          type="button"
          class="btn btn-danger btn-sm"
          >Delete</a
        >
      </td>
    </tr>
    {% endif %} {% endfor %} {% endif %}
  </tbody>
</table>

<nav aria-label="Page navigation example">
  <ul class="pagination justify-content-center">
    {% comment %} {% for i in tasks.paginator.page_range %}{% endfor %}{%
    endcomment %}

    <li class="page-item {% if not tasks.has_previous %} disabled {% endif %}">
      <a class="page-link" href="?pg=1">First</a>
    </li>

    {% if tasks.has_previous %}
    <li class="page-item">
      <a class="page-link" href="?pg={{ tasks.previous_page_number }}"
        >Previous</a
      >
    </li>

    <li class="page-item">
      <a class="page-link" href="?pg={{ tasks.previous_page_number }}"
        >{{ tasks.previous_page_number }}</a
      >
    </li>
    {% endif %}

    <li class="page-item active">
      <a class="page-link" href="#">{{ tasks.number }}</a>
    </li>

    {% if tasks.has_next %}
    <li class="page-item">
      <a class="page-link" href="?pg={{ tasks.next_page_number }}"
        >{{ tasks.next_page_number }}</a
      >
    </li>

    <li class="page-item">
      <a class="page-link" href="?pg={{ tasks.next_page_number }}">Next</a>
    </li>
    {% endif %}

    <li class="page-item {% if not tasks.has_next %} disabled {% endif %}">
      <a class="page-link" href="?pg={{ tasks.paginator.num_pages }}">Last</a>
    </li>
  </ul>
</nav>

{% endblock content %}
```

<img width="1402" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/5a62d9d0-6e6b-4509-87d4-d4bfeb500217">
<img width="1402" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b5c017a0-5974-413b-a6ac-15f1dd07df98">

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/1d8410b8-083c-495e-a65d-26582710f04c)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/90aadddc-6dbf-48fb-882b-890072028d17)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/93840e33-4778-4816-a3ff-fd404fcccf26)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/c14ad119-bd1e-4b0d-8200-8c2da8f3a62f)

<img width="1396" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/f8be2323-0489-4681-908a-686338658626">
<img width="1396" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e7c4b243-8f57-42e7-8507-9a88f11b9813">
<img width="1396" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/349b9cad-191e-4cff-b614-e0e517736faa">
<img width="1396" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ce1ac473-c04d-4305-811d-cbd88dfb01c4">

# #END</details>

<details>
<summary>17. Setup HomePage </summary>

# Setup HomePage

[https://github.com/omeatai/src-python-flask-django/commit/cccec3cbe9d4a96abbbc1ed9d9ddb682938063a1](https://github.com/omeatai/src-python-flask-django/commit/cccec3cbe9d4a96abbbc1ed9d9ddb682938063a1)

[https://unsplash.com/s/photos/notes](https://unsplash.com/s/photos/notes)

### taskmate.urls:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todolist.urls')),
]

```

### todolist.urls:

```py
from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.home, name="home"),
    path('todolist/', views.todolist, name="todolist"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('edit/<int:id>', views.edit_task, name="edit-task"),
    path('delete/<int:id>', views.delete_task, name="delete-task"),
    path('completed/<int:id>', views.completed, name="completed"),
    path('pending/<int:id>', views.pending, name="pending"),
]

```

### todolist.views:

```py
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator
from urllib.parse import urlparse, parse_qs

from .models import TaskList
from .forms import TaskForm
# Create your views here.


def home(request):
    context = {
        "welcome_text": "Welcome to the Home Page!"
    }
    return render(request, 'home.html', context)


def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.done = False
            form.save()
            messages.success(
                request, "Awesome! Your new Task has been added successfully!")
        res = redirect('todolist')
    else:
        tasks = TaskList.objects.all()
        no_per_pages = 5
        paginator = Paginator(tasks, no_per_pages)
        page = request.GET.get('pg')
        tasks = paginator.get_page(page)

        context = {
            'tasks': tasks,
            "welcome_text": "Welcome to your Todo List!",
        }
        return render(request, 'todolist.html', context)


def edit_task(request, id):
    if request.method == "POST":
        form = TaskForm(request.POST or None,
                        instance=TaskList.objects.get(pk=id))
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your new Task has been updated successfully!")
            return redirect('todolist')
    else:
        task = TaskList.objects.get(pk=id)
        context = {
            'task': task,
        }
        return render(request, 'edit.html', context)


def completed(request, id):
    task = TaskList.objects.get(pk=id)
    task.done = True
    task.save()
    # GET previous url
    previous_url = request.META.get('HTTP_REFERER')
    parsed_url = urlparse(previous_url)
    query_params = parse_qs(parsed_url.query)
    pg_value = query_params.get('pg', [None])[0]

    res = reverse('todolist') + f"?pg={pg_value}"
    return redirect(res)


def pending(request, id):
    task = TaskList.objects.get(pk=id)
    task.done = False
    task.save()
    # GET previous url
    previous_url = request.META.get('HTTP_REFERER')
    parsed_url = urlparse(previous_url)
    query_params = parse_qs(parsed_url.query)
    pg_value = query_params.get('pg', [None])[0]

    res = reverse('todolist') + f"?pg={pg_value}"
    return redirect(res)
    # return redirect('todolist')


def delete_task(request, id):
    task = TaskList.objects.get(pk=id)
    task.delete()
    messages.success(request, "Task has been deleted successfully!")
    return redirect('todolist')


def about(request):
    context = {
        "welcome_text": "Welcome to the About Page!"
    }
    return render(request, 'about.html', context)


def contact(request):
    context = {
        "welcome_text": "Welcome to the Contact Page!"
    }
    return render(request, 'contact.html', context)

```

### src-python/udemy/django-A-Z/templates/todolist/base.html:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />

    <!-- Bootstrap CSS -->
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ"
      crossorigin="anonymous"
    />
    <link
      rel="icon"
      href="{% static 'todolist/images/favicon.ico' %}"
      type="image/gif"
      sizes="16x16"
    />

    <title>Todo List Manager - {% block title %}{% endblock title %}</title>
  </head>

  <body class="bg-light">
    <nav class="navbar navbar-expand-lg bg-body-dark navbar-dark bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="{% url 'home' %}"
          ><img
            src="{% static 'todolist/images/logo-1.png' %}"
            alt="Taskmate Logo"
        /></a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a
                class="nav-link active"
                aria-current="page"
                href="{% url 'home' %}"
                >Home</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'todolist' %}">Todo List</a>
              {% comment %} <a class="nav-link" href="/task">Todo List</a> {%
              endcomment %}
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'about' %}">About Us</a>
              {% comment %}
              <a class="nav-link" href="/task/about">About Us</a> {% endcomment
              %}
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'contact' %}">Contact Us</a>
              {% comment %}
              <a class="nav-link" href="/task/contact">Contact Us</a> {%
              endcomment %}
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <main class="container">
      <h1>Taskmate</h1>
      {% block content %} {% endblock content %}
    </main>

    <!-- Optional JavaScript; choose one of the two! -->
    <!-- jQuery and Bootstrap Bundle (includes Popper) -->
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```

### src-python/udemy/django-A-Z/todolist/templates/home.html:

```html
{% extends "todolist/base.html" %}
{% load static %}

{% block title %}
Welcome
{% endblock title %}

{% block content %}
<h2>{{ welcome_text }}</h2>

<div class="text-center">
  <div class="row mt-5">
    <div class="col-lg-4">
      <img src="{% static 'todolist/images/stickynotes-1.jpg' %}" alt='stickynotes' width="360" height="250" class="rounded-lg shadow-lg"></img>
    </div>
    <div class="col-lg-4">
      <img src="{% static 'todolist/images/stickynotes-2.jpg' %}" alt='stickynotes' width="360" height="250" class="rounded-lg shadow-lg"></img>
    </div>
    <div class="col-lg-4">
      <img src="{% static 'todolist/images/stickynotes-3.jpg' %}" alt='stickynotes' width="360" height="250" class="rounded-lg shadow-lg"></img>
    </div>
  </div>

  <div class="row mt-5">
    <div class="col-md-10 offset-md-1">
        <p class="h1 text-success">Quick And Easy To Use, Anytime, Anywhere!</p>
        <p class="h2 mt-3">"Plan Your Day Better, Get Your Life Organized"</p>
        <p class="h5">TASKMATE Lets You Keep Track Of Your Task In One Place.</p>
        <a href="{% url 'todolist' %}" type="button" class="btn btn-primary btn-lg mt-3 shadow-lg">Let's Get Started!</a>
    </div>
  </div>
</div>

{% endblock content %}
```

### src-python/udemy/django-A-Z/todolist/templates/todolist.html:

```html
{% extends "todolist/base.html" %} {% block title %} Welcome {% endblock title
%} {% block content %}
<h2>{{ welcome_text }}</h2>

<form method="POST" class="row my-3">
  {% csrf_token %} {% if messages %} {% for message in messages %} {% comment %}
  <div class="alert alert-success" role="alert">{{ message }}</div>
  {% endcomment %}

  <div class="alert alert-success alert-dismissible fade show" role="alert">
    {{ message }}
    <button
      type="button"
      class="btn-close"
      data-bs-dismiss="alert"
      aria-label="Close"
    ></button>
  </div>

  {% endfor %} {% endif %}

  <div class="mb-3">
    <label for="task" class="form-label">Add Task</label>
    <input
      type="text"
      class="form-control"
      id="task"
      name="task"
      aria-describedby="textHelp"
      placeholder="Call Alex..."
    />
    <div id="textHelp" class="form-text">What would you want to do?</div>
  </div>
  <button type="submit" class="btn btn-primary">ADD TASK</button>
</form>

<table
  class="table table-light table-striped table-hover table-bordered text-center"
>
  <thead>
    <tr class="table-dark row">
      <th class="col-7">Task</th>
      <th class="col-3">Done</th>
      <th class="col-1">Edit</th>
      <th class="col-1">Delete</th>
    </tr>
  </thead>
  <tbody>
    {% if tasks %} {% for todo in tasks %} {% if todo.done %}
    <tr class="table-success row">
      <th class="col-7">{{ todo.task }}</th>
      <td class="col-3">
        <a
          href="{% url 'pending' todo.id %}"
          type="button"
          class="btn btn-success btn-sm"
          >YES - Mark as Pending</a
        >
      </td>
      <td class="col-1">
        <a
          href="{% url 'edit-task' todo.id %}"
          type="button"
          class="btn btn-warning"
          >Edit</a
        >
      </td>
      <td class="col-1">
        <a
          href="{% url 'delete-task' todo.id %}"
          type="button"
          class="btn btn-danger"
          >Delete</a
        >
      </td>
    </tr>
    {% else %}
    <tr class="row">
      <th class="col-7">{{ todo.task }}</th>
      <td class="col-3">
        <a
          href="{% url 'completed' todo.id %}"
          type="button"
          class="btn btn-danger btn-sm"
          >NO - Mark as Completed</a
        >
      </td>
      <td class="col-1">
        <a
          href="{% url 'edit-task' todo.id %}"
          type="button"
          class="btn btn-warning"
          >Edit</a
        >
      </td>
      <td class="col-1">
        <a
          href="{% url 'delete-task' todo.id %}"
          type="button"
          class="btn btn-danger"
          >Delete</a
        >
      </td>
    </tr>
    {% endif %} {% endfor %} {% endif %}
  </tbody>
</table>

<nav aria-label="Page navigation example">
  <ul class="pagination justify-content-center">
    {% comment %} {% for i in tasks.paginator.page_range %}{% endfor %}{%
    endcomment %}

    <li class="page-item {% if not tasks.has_previous %} disabled {% endif %}">
      <a class="page-link" href="?pg=1">First</a>
    </li>

    {% if tasks.has_previous %}
    <li class="page-item">
      <a class="page-link" href="?pg={{ tasks.previous_page_number }}"
        >Previous</a
      >
    </li>

    <li class="page-item">
      <a class="page-link" href="?pg={{ tasks.previous_page_number }}"
        >{{ tasks.previous_page_number }}</a
      >
    </li>
    {% endif %}

    <li class="page-item active">
      <a class="page-link" href="#">{{ tasks.number }}</a>
    </li>

    {% if tasks.has_next %}
    <li class="page-item">
      <a class="page-link" href="?pg={{ tasks.next_page_number }}"
        >{{ tasks.next_page_number }}</a
      >
    </li>

    <li class="page-item">
      <a class="page-link" href="?pg={{ tasks.next_page_number }}">Next</a>
    </li>
    {% endif %}

    <li class="page-item {% if not tasks.has_next %} disabled {% endif %}">
      <a class="page-link" href="?pg={{ tasks.paginator.num_pages }}">Last</a>
    </li>
  </ul>
</nav>

{% endblock content %}
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/cf3f7b77-2f22-4de4-bb9f-18b99cf26757)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/492e8aa7-c89c-4922-9a86-55f4a4e8cad5)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/a5d38adc-26d3-471d-8d1e-c8368bd07169)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/91d6e012-3c45-4808-a78b-df57f7406007)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/2433351e-2e6e-4b7d-996f-cdc6bfe500de)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/10ae459e-a070-4b31-95c0-83fc1e1ea562)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/36c29504-0069-4311-9103-3f7ea2f94748)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/58096026-7c9a-4087-9310-70419bd8bf87)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/14ce4007-3c1e-49f4-b2b9-639c9af4033d)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/516d72c5-c66d-44f2-b5e2-46f31f484537)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/8c5756d5-d482-4511-a4b0-6e25d3687113)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/ddcf4e06-07d1-4f1a-a9e6-110e6a106a5d)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/628c02f1-4e54-40b5-9e90-7176f133cfb5)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/138600da-b0ad-4708-9c39-a163a9223ab5)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/dabb6bb7-d14e-407b-b915-f5465510c62e)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/5d7399a9-d188-4f74-b2f0-f0d7af03210f)

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/bc09af4c-f39d-454a-bff4-3212121f512a)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/e355e3f0-1038-4dbd-8e68-347c0a99a544)

<img width="1396" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ec865bef-7c88-4720-9ea8-52f5b9b18ca2">
<img width="1396" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/5b350bda-4be3-424b-a10e-d3e1d4cd5b66">
<img width="1396" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/89c12ac8-a650-4132-8124-db2470f2b637">
<img width="1396" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/7aefe9c3-c94c-4e5a-8bda-aac412a3f9f6">
<img width="1396" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/74ebaebc-4d46-4f50-b5c2-0f7637280f67">
<img width="1396" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/25cb6276-4c08-4594-a3ec-b3c0d9d0e36b">

# #END</details>

<details>
<summary>18. Setup User Authentication App </summary>

# Setup User Authentication App

[https://github.com/omeatai/src-python-flask-django/commit/071b0e57d5f1903d870b67c2bec349bef8770c9b](https://github.com/omeatai/src-python-flask-django/commit/071b0e57d5f1903d870b67c2bec349bef8770c9b)

### Create User App

```py
python manage.py startapp user_auth
```

### taskmate.settings:

```py
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # apps
    'todolist',
    'user_auth',
]
```

### taskmate.urls:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todolist.urls')),
    path('account/', include('user_auth.urls')),
]
```

### user_auth.urls:

```py
from django.urls import path
from user_auth import views

urlpatterns = [
    path('register/', views.register, name="register"),

    # path('signup/', views.signup, name="signup"),
    # path('login/', views.login_user, name="login"),
    # path('logout/', views.logout_user, name="logout"),
    # path('profile/', views.profile, name="profile"),
    # path('edit-profile/', views.edit_profile, name="edit-profile"),
    # path('change-password/', views.change_password, name="change-password"),
    # path('reset-password/', views.reset_password, name="reset-password"),
    # path('reset-password-done/', views.reset_password_done, name="reset-password-done"),
    # path('reset-password-confirm/<uidb64>/<token>/', views.reset_password_confirm, name="reset-password-confirm"),
    # path('reset-password-complete/', views.reset_password_complete, name="reset-password-complete"),
    # path('delete-account/', views.delete_account, name="delete-account"),
]

```

### user_auth.views:

```py
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def register(request):
    return HttpResponse("<h1>User registration Page is working!</h1>")
    # return render(request, 'register.html', {})

```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/e4a251f1-43e0-4416-a791-862ec83beed2)

<img width="1396" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/46946c8a-2738-4526-9e41-e07251234608">
<img width="1396" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e906c58e-310f-44da-81ad-9a085d9e6ce6">
<img width="1396" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/90398f9e-5c4c-4898-9910-aae10b343f05">
<img width="1396" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/3bc0762d-c8f6-483e-a7ab-4f5769133b0b">

# #END</details>

<details>
<summary>19. Setup Registration userCreationForm, Views and Template with Errors and Messages </summary>

# Setup Registration userCreationForm, Views and Template with Errors and Messages

[https://github.com/omeatai/src-python-flask-django/commit/a9d6c021a3d5cf2bdf7591043b5b21dcfc894940](https://github.com/omeatai/src-python-flask-django/commit/a9d6c021a3d5cf2bdf7591043b5b21dcfc894940)

### user_auth.views:

```py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == "POST":
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(
                request, "Awesome! Your new account has been created successfully! Login to Get Started.")
            return redirect('register')
        else:
            messages.error(
                request, "Sorry! Your new account could not be created. Please try again.")
            return render(request, 'user_auth/register.html', {'register_form': register_form})
    else:
        register_form = UserCreationForm()
        return render(request, 'user_auth/register.html', {'register_form': register_form})

```

### src-python/udemy/django-A-Z/user_auth/templates/user_auth/register.html:

```html
{% extends "todolist/base.html" %} {% block title %} Sign Up - Taskmate {%
endblock title %} {% block content %}

<div>
  <form action="" method="POST" class="form-group my-3">
    {% csrf_token %} {% if messages %} {% for message in messages %}

    <div
      class="alert {% if message.tags == 'error' %} alert-danger {% elif message.tags == 'success' %} alert-success {% else %} alert-warning {% endif %} alert-dismissible fade show"
      role="alert"
    >
      {{ message }}
      <button
        type="button"
        class="btn-close"
        data-bs-dismiss="alert"
        aria-label="Close"
      ></button>
    </div>

    {% endfor %} {% endif %}

    <hr />

    {% if register_form.errors %} {% for field in register_form %} {{
    field.errors }} {% endfor %} {% endif %}

    <hr />

    {% if register_form.errors %} {% for field in register_form %} {% for error
    in field.errors %}
    <div class="alert alert-danger alert-dismissible fade show" role="alert">
      {{ error|escape }}
      <button
        type="button"
        class="btn-close"
        data-bs-dismiss="alert"
        aria-label="Close"
      ></button>
    </div>
    {% endfor %} {% endfor %} {% endif %}

    <hr />

    {% if register_form.non_field_errors %} {% for error in
    register_form.non_field_errors %}
    <div class="alert alert-danger alert-dismissible fade show" role="alert">
      {{ error|escape }}
      <button
        type="button"
        class="btn-close"
        data-bs-dismiss="alert"
        aria-label="Close"
      ></button>
    </div>
    {% endfor %} {% endif %}

    <hr />

    {{ register_form.as_p}}

    <button type="submit" class="btn btn-primary">Sign Up</button>
  </form>
</div>
{% endblock content %}
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/8a3212cc-4284-461c-bd13-3e334a1a281d)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/56eef428-a699-4462-bc72-ad15a5e5768d)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/b3866b11-26b3-4403-9488-cf4c9466e712)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/7462171d-5d6c-4f08-abb5-e5162463312a)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/0a1aacd4-81bb-496a-b194-b05c79763967)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/79beffcf-e612-4499-a038-04f8270d7095)

# #END</details>

<details>
<summary>20. Add Email Field to Form with forms.py </summary>

# Add Email Field to Form with forms.py

[https://github.com/omeatai/src-python-flask-django/commit/d3c63eda49bdb6f0cfd92c935930d850010d4126](https://github.com/omeatai/src-python-flask-django/commit/d3c63eda49bdb6f0cfd92c935930d850010d4126)

### user_auth.forms:

```py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text="Required")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

```

### user_auth.views:

```py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import CustomRegistrationForm
# Create your views here.


def register(request):
    if request.method == "POST":
        register_form = CustomRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(
                request, "Awesome! Your new account has been created successfully! Login to Get Started.")
            return redirect('register')
        else:
            messages.error(
                request, "Sorry! Your new account could not be created. Please try again.")
            return render(request, 'user_auth/register.html', {'register_form': register_form})
    else:
        register_form = CustomRegistrationForm()
        return render(request, 'user_auth/register.html', {'register_form': register_form})

```

### src-python/udemy/django-A-Z/user_auth/templates/user_auth/register.html:

```html
{% extends "todolist/base.html" %} {% block title %} Sign Up - Taskmate {%
endblock title %} {% block content %}

<div>
  <form action="" method="POST" class="form-group my-3">
    {% csrf_token %} {% if messages %} {% for message in messages %}

    <div
      class="alert
        {% if message.tags == 'error' %} alert-danger
        {% elif message.tags == 'success' %} alert-success
        {% else %} alert-warning
        {% endif %} alert-dismissible fade show"
      role="alert"
    >
      {{ message }}
      <button
        type="button"
        class="btn-close"
        data-bs-dismiss="alert"
        aria-label="Close"
      ></button>
    </div>

    {% endfor %} {% endif %} {% if register_form.errors %} {% for field in
    register_form %} {% for error in field.errors %}
    <div class="alert alert-danger alert-dismissible fade show" role="alert">
      {{ error|escape }}
      <button
        type="button"
        class="btn-close"
        data-bs-dismiss="alert"
        aria-label="Close"
      ></button>
    </div>
    {% endfor %} {% endfor %} {% endif %} {{ register_form.as_p}}

    <button type="submit" class="btn btn-primary">Sign Up</button>
  </form>
</div>
{% endblock content %}
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/f0fef2cd-8bf0-42fb-bf1b-80032ff682d9)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/c1253e16-e4be-463a-b4f7-a74f942de281)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/2f237133-d42c-471e-bc56-181b8c631fa1)

<img width="1377" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/908fed7d-8b70-4886-ac79-027087017e59">
<img width="1377" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/124d7dd2-bca9-4523-83bc-0886f7386f31">
<img width="1377" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/d73fb41c-6967-4489-908b-902721ad6181">

# #END</details>

<details>
<summary>21. Redesign the Register Page with Crispy Forms </summary>

# Redesign the Register Page with Crispy Forms

[https://github.com/omeatai/src-python-flask-django/commit/9ea3288a858fe8e5a453b400794e894cfe16a213](https://github.com/omeatai/src-python-flask-django/commit/9ea3288a858fe8e5a453b400794e894cfe16a213)

## Install Crispy Forms

```x
pip install crispy-bootstrap5
```

### taskmate.settings:

```py
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # apps
    'todolist',
    'user_auth',
    'crispy_forms',
    'crispy_bootstrap5',
]


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = 'bootstrap5'
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'

```

### src-python/udemy/django-A-Z/user_auth/templates/user_auth/register.html:

```html
{% extends "todolist/base.html" %} {% load crispy_forms_tags %} {% block title
%} Sign Up - Taskmate {% endblock title %} {% block content %}

<div>
  <h2>Sign Up</h2>
  <form action="" method="POST" class="form-group my-3 col-6">
    {% csrf_token %} {% if messages %} {% for message in messages %}

    <div
      class="alert
        {% if message.tags == 'error' %} alert-danger
        {% elif message.tags == 'success' %} alert-success
        {% else %} alert-warning
        {% endif %} alert-dismissible fade show"
      role="alert"
    >
      {{ message }}
      <button
        type="button"
        class="btn-close"
        data-bs-dismiss="alert"
        aria-label="Close"
      ></button>
    </div>

    {% endfor %} {% endif %} {% if register_form.errors %} {% for field in
    register_form %} {% for error in field.errors %}
    <div class="alert alert-danger alert-dismissible fade show" role="alert">
      {{ error|escape }}
      <button
        type="button"
        class="btn-close"
        data-bs-dismiss="alert"
        aria-label="Close"
      ></button>
    </div>
    {% endfor %} {% endfor %} {% endif %} {{ register_form|crispy }}

    <button type="submit" class="btn btn-primary">Sign Up</button>
  </form>
</div>
{% endblock content %}
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/92e7f747-7986-4410-af6d-95c8e83a4527)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/f19ad3d6-4d0c-49e8-a619-bdfecff9c029)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/f488d0f0-1734-44bd-b8de-fba7e47134b9)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/dba5eccb-5065-48d8-a0b5-69e3a4ed0096)

<img width="1447" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b4ac9c23-ae6e-4cb9-9e26-79513d47fece">
<img width="1447" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/36e9fbc4-35c1-4e66-bdf0-6a41ace252d7">

# #END</details>

<details>
<summary>22. Login Functionality </summary>

# Login Functionality

[https://github.com/omeatai/src-python-flask-django/commit/6cd6828e1377c2306776d47d8f21e5c13b3dd1a8](https://github.com/omeatai/src-python-flask-django/commit/6cd6828e1377c2306776d47d8f21e5c13b3dd1a8)

### taskmate.settings:

```py
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = 'bootstrap5'
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'

LOGIN_REDIRECT_URL = 'todolist'
```

### user_auth.urls:

```py
from django.urls import path
from user_auth import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='user_auth/login.html'), name="login"),
    # path('logout/', auth_views.LogoutView.as_view(), name="logout"),

    # path('signup/', views.signup, name="signup"),
    # path('login/', views.login_user, name="login"),
    # path('logout/', views.logout_user, name="logout"),
    # path('profile/', views.profile, name="profile"),
    # path('edit-profile/', views.edit_profile, name="edit-profile"),
    # path('change-password/', views.change_password, name="change-password"),
    # path('reset-password/', views.reset_password, name="reset-password"),
    # path('reset-password-done/', views.reset_password_done, name="reset-password-done"),
    # path('reset-password-confirm/<uidb64>/<token>/', views.reset_password_confirm, name="reset-password-confirm"),
    # path('reset-password-complete/', views.reset_password_complete, name="reset-password-complete"),
    # path('delete-account/', views.delete_account, name="delete-account"),
]

```

### src-python/udemy/django-A-Z/user_auth/templates/user_auth/login.html:

```html
{% extends "todolist/base.html" %} {% load crispy_forms_tags %} {% block title
%} Sign In - Taskmate {% endblock title %} {% block content %}

<div>
  <h2>Sign In</h2>
  <form action="" method="POST" class="form-group my-3 col-6">
    {% csrf_token %} {% if messages %} {% for message in messages %}

    <div
      class="alert
        {% if message.tags == 'error' %} alert-danger
        {% elif message.tags == 'success' %} alert-success
        {% else %} alert-warning
        {% endif %} alert-dismissible fade show"
      role="alert"
    >
      {{ message }}
      <button
        type="button"
        class="btn-close"
        data-bs-dismiss="alert"
        aria-label="Close"
      ></button>
    </div>

    {% endfor %} {% endif %} {% if register_form.errors %} {% for field in
    register_form %} {% for error in field.errors %}
    <div class="alert alert-danger alert-dismissible fade show" role="alert">
      {{ error|escape }}
      <button
        type="button"
        class="btn-close"
        data-bs-dismiss="alert"
        aria-label="Close"
      ></button>
    </div>
    {% endfor %} {% endfor %} {% endif %} {{ form|crispy }}

    <button type="submit" class="btn btn-primary">Sign In</button>
  </form>
</div>
{% endblock content %}
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/ced09a03-fb3d-4c64-b01a-bbfb1df602d9)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/f6421499-d2da-45e5-acc6-7e1ca124b53c)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/1d4896ff-b121-43ac-8f40-d5044f27fc5a)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/b278fdfa-68b0-47d6-b4e2-fac4b2d5e95b)

<img width="1447" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/023f6b2d-e771-438b-bb2d-9d06cb1b1b79">
<img width="1447" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/851925dd-fa3a-4743-b7ac-473c0eaea69a">
<img width="1447" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1acc64db-a3df-477c-bfc3-e7561f93b6c7">

# #END</details>

<details>
<summary>23. Logout Functionality and Username in Navbar </summary>

# Logout Functionality and Username in Navbar

[https://github.com/omeatai/src-python-flask-django/commit/a8686d606c7ce2e0a6a988dd3e345b8ccd2be50a](https://github.com/omeatai/src-python-flask-django/commit/a8686d606c7ce2e0a6a988dd3e345b8ccd2be50a)

### user_auth.urls:

```py
from django.urls import path
from user_auth import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='user_auth/login.html'), name="login"),
    path('logout/', views.logout, name="logout"),

    # path('signup/', views.signup, name="signup"),
    # path('login/', views.login_user, name="login"),
    # path('logout/', views.logout_user, name="logout"),
    # path('profile/', views.profile, name="profile"),
    # path('edit-profile/', views.edit_profile, name="edit-profile"),
    # path('change-password/', views.change_password, name="change-password"),
    # path('reset-password/', views.reset_password, name="reset-password"),
    # path('reset-password-done/', views.reset_password_done, name="reset-password-done"),
    # path('reset-password-confirm/<uidb64>/<token>/', views.reset_password_confirm, name="reset-password-confirm"),
    # path('reset-password-complete/', views.reset_password_complete, name="reset-password-complete"),
    # path('delete-account/', views.delete_account, name="delete-account"),
]

```

### user_auth.views:

```py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.views import View
from django.contrib.auth.views import LogoutView

from .forms import CustomRegistrationForm
# Create your views here.


def register(request):
    if request.method == "POST":
        register_form = CustomRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(
                request, "Awesome! Your new account has been created successfully! Login to Get Started.")
            return redirect('register')
        else:
            messages.error(
                request, "Sorry! Your new account could not be created. Please try again.")
            return render(request, 'user_auth/register.html', {'register_form': register_form})
    else:
        register_form = CustomRegistrationForm()
        return render(request, 'user_auth/register.html', {'register_form': register_form})


def logout(request):
    if request.method == 'POST':
        messages.success(
            request, "Awesome! You have been logged out successfully!")
        return LogoutView.as_view(next_page='login')(request)
    else:
        return render(request, 'user_auth/logout.html')


# class UserLogoutView(LogoutView):
#     def get(self, request):
#         logout(request)
#         return redirect('login')

```

### src-python/udemy/django-A-Z/templates/todolist/base.html:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />

    <!-- Bootstrap CSS -->
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ"
      crossorigin="anonymous"
    />
    <link
      rel="icon"
      href="{% static 'todolist/images/favicon.ico' %}"
      type="image/gif"
      sizes="16x16"
    />

    <title>Todo List Manager - {% block title %}{% endblock title %}</title>
  </head>

  <body class="bg-light">
    <nav class="navbar navbar-dark bg-dark navbar-expand-lg bg-body-dark mb-4">
      <div class="container-fluid">
        <a class="navbar-brand" href="{% url 'home' %}"
          ><img
            src="{% static 'todolist/images/logo-1.png' %}"
            alt="Taskmate Logo"
        /></a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a
                class="nav-link active"
                aria-current="page"
                href="{% url 'home' %}"
                >Home</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'todolist' %}">Todo List</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'about' %}">About Us</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'contact' %}">Contact Us</a>
            </li>
          </ul>
          {% if user.is_authenticated %}
          <div class="d-flex text-secondary mx-2">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item dropdown">
                <a
                  class="nav-link dropdown-toggle"
                  href="#"
                  role="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  Welcome, {{ user.username|title }}
                </a>
                <ul class="dropdown-menu">
                  <li><a class="dropdown-item" href="#">Profile</a></li>
                  <li><a class="dropdown-item" href="#">Change Password</a></li>
                  <li><hr class="dropdown-divider" /></li>
                  <li><a class="dropdown-item" href="#">Settings</a></li>
                </ul>
              </li>
            </ul>
          </div>
          <div class="d-flex mx-2">
            <a href="{% url 'logout' %}" class="btn btn-danger" type="submit"
              >Logout</a
            >
          </div>
          {% else %}
          <div class="d-flex mx-2">
            <a href="{% url 'login' %}" class="btn btn-success" type="submit"
              >Login</a
            >
          </div>
          <div class="d-flex mx-2">
            <a href="{% url 'register' %}" class="btn btn-primary" type="submit"
              >Register</a
            >
          </div>
          {% endif %}
        </div>
      </div>
    </nav>

    <main class="container">
      <h1>Taskmate</h1>
      {% block content %} {% endblock content %}
    </main>

    <!-- Optional JavaScript; choose one of the two! -->
    <!-- jQuery and Bootstrap Bundle (includes Popper) -->
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```

### src-python/udemy/django-A-Z/user_auth/templates/user_auth/logout.html:

```html
{% extends "todolist/base.html" %} {% block title %} Logged Out - Taskmate {%
endblock title %} {% block content %}

<div>
  <form action="{% url 'logout' %}" method="POST" class="form-group my-3 col-6">
    {% csrf_token %} {% if messages %} {% for message in messages %}

    <div
      class="alert
        {% if message.tags == 'error' %} alert-danger
        {% elif message.tags == 'success' %} alert-success
        {% else %} alert-warning
        {% endif %} alert-dismissible fade show"
      role="alert"
    >
      {{ message }}
      <button
        type="button"
        class="btn-close"
        data-bs-dismiss="alert"
        aria-label="Close"
      ></button>
    </div>

    {% endfor %} {% endif %}

    <h2 class="text-secondary">Sure you want to Logout of Taskmate?</h2>

    <button type="submit" class="btn btn-danger">Logout</button>
  </form>
</div>
{% endblock content %}
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/7c7e0b1a-a083-4019-8037-6b79ef1f1eac)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/170123a2-d524-4809-ac1a-ce44213feb86)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/3b019d45-f235-4f14-99c3-4b384bf30ba5)

<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ceaaf8c7-f786-4154-bfc1-f48615ebda56">
<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/67be9e97-ef33-4f58-875c-3e11781e19ce">
<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/6b6ce0ff-9357-4e0b-92bb-4608e2ff7955">
<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/43f565e8-c61e-436f-8b5a-ec4278959f3a">

# #END</details>

<details>
<summary>24. Login Manually with authenticate and login </summary>

# Login Manually with authenticate and login

[https://github.com/omeatai/src-python-flask-django/commit/783ee1680b9f55b5b86f5ee8eab2d787531046fc](https://github.com/omeatai/src-python-flask-django/commit/783ee1680b9f55b5b86f5ee8eab2d787531046fc)

## Logic for Creating users

```py
>>> from django.contrib.auth.models import User
>>> user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")

# At this point, user is a User object that has already been saved
# to the database. You can continue to change its attributes
# if you want to change other fields.
>>> user.last_name = "Lennon"
>>> user.save()
```

## Command for creating SuperUser from Prompt

```py
python manage.py createsuperuser --username=joe --email=joe@example.com
```

## Logic for changing Passwords

```py
>>> from django.contrib.auth.models import User
>>> u = User.objects.get(username="john")
>>> u.set_password("new password")
>>> u.save()
```

## Logic for Authenticating users manually

```py
from django.contrib.auth import authenticate

user = authenticate(username="john", password="secret")
if user is not None:
    # A backend authenticated the credentials
else:
    # No backend authenticated the credentials
```

```py
from django.contrib.auth import authenticate, login


def my_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
    else:
        # Return an 'invalid login' error message.
```

### user_auth.urls:

```py
from django.urls import path
from user_auth import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name="register"),
    # path('login/', auth_views.LoginView.as_view(template_name='user_auth/login.html'), name="login"),
    path('login/', views.auth_login, name="login"),
    path('logout/', views.logout, name="logout"),

    # path('signup/', views.signup, name="signup"),
    # path('login/', views.login_user, name="login"),
    # path('logout/', views.logout_user, name="logout"),
    # path('profile/', views.profile, name="profile"),
    # path('edit-profile/', views.edit_profile, name="edit-profile"),
    # path('change-password/', views.change_password, name="change-password"),
    # path('reset-password/', views.reset_password, name="reset-password"),
    # path('reset-password-done/', views.reset_password_done, name="reset-password-done"),
    # path('reset-password-confirm/<uidb64>/<token>/', views.reset_password_confirm, name="reset-password-confirm"),
    # path('reset-password-complete/', views.reset_password_complete, name="reset-password-complete"),
    # path('delete-account/', views.delete_account, name="delete-account"),
]

```

### user_auth.views:

```py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.views import View
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate, logout, login

from .forms import CustomRegistrationForm
# Create your views here.


def register(request):
    if request.method == "POST":
        register_form = CustomRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(
                request, "Awesome! Your new account has been created successfully! Login to Get Started.")
            return redirect('register')
        else:
            messages.error(
                request, "Sorry! Your new account could not be created. Please try again.")
            return render(request, 'user_auth/register.html', {'register_form': register_form})
    else:
        register_form = CustomRegistrationForm()
        return render(request, 'user_auth/register.html', {'register_form': register_form})


def auth_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # username = request.POST["username"]
        # password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist')
        else:
            messages.error(
                request, "Sorry! Your credentials could not be validated. Please try again.")
            return redirect('login')
    else:
        return render(request, 'user_auth/login_manual.html')


def logout(request):
    if request.method == 'POST':
        messages.success(
            request, "Awesome! You have been logged out successfully!")
        return LogoutView.as_view(next_page='login')(request)
    else:
        return render(request, 'user_auth/logout.html')


# class UserLogoutView(LogoutView):
#     def get(self, request):
#         logout(request)
#         return redirect('login')

```

### src-python/udemy/django-A-Z/user_auth/templates/user_auth/login_manual.html:

```py
{% extends "todolist/base.html" %}
{% load crispy_forms_tags %}

{% block title %}
Sign In - Taskmate
{% endblock title %}

{% block content %}

<div>
    <h2>Sign In</h2>
    <form action="{% url 'login' %}" method="POST" class="form-group my-3 col-6">
        {% csrf_token %}

        {% if messages %}
        {% for message in messages %}

        <div class="alert
        {% if message.tags == 'error' %} alert-danger
        {% elif message.tags == 'success' %} alert-success
        {% else %} alert-warning
        {% endif %} alert-dismissible fade show"
        role="alert">
            {{ message }}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>

        {% endfor %}
        {% endif %}

        {% if register_form.errors %}
        {% for field in register_form %}
            {% for error in field.errors %}
            <div class="alert alert-danger alert-dismissible fade show" role="alert">
                {{ error|escape }}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
            {% endfor %}
        {% endfor %}
        {% endif %}

        <div class="mb-3">
            <label for="username" class="form-label">Username</label>
            <input type="text" class="form-control" id="username" name="username" placeholder="Enter your username">
        </div>
        <div class="mb-3">
            <label for="password" class="form-label">Password</label>
            <input type="password" class="form-control" id="password" name="password" placeholder="Enter your password">
        </div>

        <button type="submit" class="btn btn-primary">Sign In</button>
    </form>
</div>
{% endblock content %}
```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/5f48f582-9988-4d85-af9d-3e8632159d81">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/d5255ec2-66eb-4741-8ef6-019891312111">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b0518f62-982c-4d1a-aff3-bfd6790f9b78">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/7df9b66e-1e73-420b-a772-d14c3adf2ccb">

<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/c3a052d9-b46a-43f4-9217-d4ce5f2f6c73">
<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/c626753a-c0b9-4492-bbd5-d57783bd52ba">
<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1cd66482-7585-4ce3-8456-13ff487e89b1">

# #END</details>

<details>
<summary>25. Logout Manually with logout </summary>

# Logout Manually with logout

[https://github.com/omeatai/src-python-flask-django/commit/96a65ce7e583625918360741f65d6262c5bcec7e](https://github.com/omeatai/src-python-flask-django/commit/96a65ce7e583625918360741f65d6262c5bcec7e)

## Logic to Logout user

```py
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    # Redirect to a success page.
```

### user_auth.urls:

```py
from django.urls import path
from user_auth import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name="register"),
    # path('login/', auth_views.LoginView.as_view(template_name='user_auth/login.html'), name="login"),
    path('login/', views.auth_login, name="login"),
    path('logout/', views.auth_logout, name="logout"),
]

```

### user_auth.views:

```py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.views import View
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate, logout, login

from .forms import CustomRegistrationForm
# Create your views here.


def register(request):
    if request.method == "POST":
        register_form = CustomRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(
                request, "Awesome! Your new account has been created successfully! Login to Get Started.")
            return redirect('register')
        else:
            messages.error(
                request, "Sorry! Your new account could not be created. Please try again.")
            return render(request, 'user_auth/register.html', {'register_form': register_form})
    else:
        register_form = CustomRegistrationForm()
        return render(request, 'user_auth/register.html', {'register_form': register_form})


def auth_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # username = request.POST["username"]
        # password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist')
        else:
            messages.error(
                request, "Sorry! Your credentials could not be validated. Please try again.")
            return redirect('login')
    else:
        return render(request, 'user_auth/login_manual.html')


def auth_logout(request):
    if request.method == 'POST':
        messages.success(
            request, "Awesome! You have been logged out successfully!")
        logout(request)
        return redirect('login')
    else:
        return render(request, 'user_auth/logout.html')


# def logout(request):
#     if request.method == 'POST':
#         messages.success(
#             request, "Awesome! You have been logged out successfully!")
#         return LogoutView.as_view(next_page='login')(request)
#     else:
#         return render(request, 'user_auth/logout.html')

# class UserLogoutView(LogoutView):
#     def get(self, request):
#         logout(request)
#         return redirect('login')

```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/917adbcb-da8c-414c-8600-558eab84afa6)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/875647ac-661f-447d-be16-426b87d56378)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/b32b8e06-94cb-429a-bf27-673815b9bef6)

<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/f51cb95d-5d8c-47db-8e2e-682c68024aaf">
<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/9c1512bc-b101-4fc4-9777-341b9fb7050b">

# #END</details>

<details>
<summary>26. Auth Page Restrictions </summary>

# Auth Page Restrictions

[https://github.com/omeatai/src-python-flask-django/commit/b4056b0987df08efd47c40f81287360628340a9a](https://github.com/omeatai/src-python-flask-django/commit/b4056b0987df08efd47c40f81287360628340a9a)

## Logic for Limiting access to logged-in users

```py
from django.conf import settings
from django.shortcuts import redirect


def my_view(request):
    if not request.user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
```

```py
from django.shortcuts import render


def my_view(request):
    if not request.user.is_authenticated:
        return render(request, "myapp/login_error.html")
```

```py
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='next', login_url='login')
def my_view(request):
    pass
```

### todolist.urls:

```py
from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.home, name="home"),
    path('todolist/', views.todolist, name="todolist"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('edit/<int:id>', views.edit_task, name="edit-task"),
    path('delete/<int:id>', views.delete_task, name="delete-task"),
    path('completed/<int:id>', views.completed, name="completed"),
    path('pending/<int:id>', views.pending, name="pending"),
]

```

### taskmate.settings:

```py
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = 'bootstrap5'
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'

LOGIN_REDIRECT_URL = 'todolist'
LOGIN_URL = 'login'

```

### todolist.views:

```py
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator
from urllib.parse import urlparse, parse_qs
from django.contrib.auth.decorators import login_required

from .models import TaskList
from .forms import TaskForm
# Create your views here.


def home(request):
    context = {
        "welcome_text": "Welcome to the Home Page!"
    }
    return render(request, 'home.html', context)


@login_required(login_url='login')
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.done = False
            form.save()
            messages.success(
                request, "Awesome! Your new Task has been added successfully!")
            redirect('todolist')
    else:
        tasks = TaskList.objects.all()
        no_per_pages = 5
        paginator = Paginator(tasks, no_per_pages)
        page = request.GET.get('pg')
        tasks = paginator.get_page(page)

        context = {
            'tasks': tasks,
            "welcome_text": "Welcome to your Todo List!",
        }
        return render(request, 'todolist.html', context)


@login_required
def edit_task(request, id):
    if request.method == "POST":
        form = TaskForm(request.POST or None,
                        instance=TaskList.objects.get(pk=id))
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your new Task has been updated successfully!")
            return redirect('todolist')
    else:
        task = TaskList.objects.get(pk=id)
        context = {
            'task': task,
        }
        return render(request, 'edit.html', context)


def completed(request, id):
    task = TaskList.objects.get(pk=id)
    task.done = True
    task.save()
    # GET previous url
    previous_url = request.META.get('HTTP_REFERER')
    parsed_url = urlparse(previous_url)
    query_params = parse_qs(parsed_url.query)
    pg_value = query_params.get('pg', [None])[0]

    res = reverse('todolist') + f"?pg={pg_value}"
    return redirect(res)


def pending(request, id):
    task = TaskList.objects.get(pk=id)
    task.done = False
    task.save()
    # GET previous url
    previous_url = request.META.get('HTTP_REFERER')
    parsed_url = urlparse(previous_url)
    query_params = parse_qs(parsed_url.query)
    pg_value = query_params.get('pg', [None])[0]

    res = reverse('todolist') + f"?pg={pg_value}"
    return redirect(res)
    # return redirect('todolist')


@login_required
def delete_task(request, id):
    task = TaskList.objects.get(pk=id)
    task.delete()
    messages.success(request, "Task has been deleted successfully!")
    return redirect('todolist')


def about(request):
    context = {
        "welcome_text": "Welcome to the About Page!"
    }
    return render(request, 'about.html', context)


@login_required
def contact(request):
    context = {
        "welcome_text": "Welcome to the Contact Page!"
    }
    return render(request, 'contact.html', context)
```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/5d98a05e-65f7-48c5-ab43-790ee183ddb7">
<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/3f8612c5-453c-406b-8300-8e360cdbe030">
<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/8f604bfb-003e-49c1-bcc0-3826f710a831">
<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/c5d58131-bb38-4d92-a4e0-2c35d6be2193">

# #END</details>

<details>
<summary>27. Relationship between User to Task </summary>

# Relationship between User to Task

[https://github.com/omeatai/src-python-flask-django/commit/1be6a912f9b2beedb658c1d66d0bbba390d02722](https://github.com/omeatai/src-python-flask-django/commit/1be6a912f9b2beedb658c1d66d0bbba390d02722)

## Make Migrations

```py
python manage.py makemigrations
python manage.py migrate
```

### todolist.models:

```py
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TaskList(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, default=None)
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    # description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self) -> str:
        return f"{self.task} - {self.done} (by {self.owner})"

```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/8018cdbb-7c36-4375-abc2-20494ab58204">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/c797c459-c6d7-494c-ab1e-0ff1f8ed3e02">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/37615109-bd40-4d9e-8f9f-51c9c0aee3ce">
<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/be18e020-040f-4347-96d2-d0b8eb8e90f6">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/bdc66f6f-fecf-4390-95e8-a069a673b77b">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ae23443a-b580-43d9-b913-55690e852ca6">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/f62994e3-8a2f-47ee-b26b-109db254e151">
<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/11a0c0c9-4990-40be-bf16-bdc2c8ddafc9">

# #END</details>

<details>
<summary>28. Creating Task with User </summary>

# Creating Task with User

[https://github.com/omeatai/src-python-flask-django/commit/04beb8749f460cf1395eeb32366a47e1949cb775](https://github.com/omeatai/src-python-flask-django/commit/04beb8749f460cf1395eeb32366a47e1949cb775)

### todolist.views:

```py
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator
from urllib.parse import urlparse, parse_qs
from django.contrib.auth.decorators import login_required

from .models import TaskList
from .forms import TaskForm
# Create your views here.


def home(request):
    context = {
        "welcome_text": "Welcome to the Home Page!"
    }
    return render(request, 'home.html', context)


@login_required(login_url='login')
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.done = False
            instance.owner = request.user
            instance.save()
            messages.success(
                request, "Awesome! Your new Task has been added successfully!")
            return redirect('todolist')
    else:
        tasks = TaskList.objects.all()
        no_per_pages = 5
        paginator = Paginator(tasks, no_per_pages)
        page = request.GET.get('pg')
        tasks = paginator.get_page(page)

        context = {
            'tasks': tasks,
            "welcome_text": "Welcome to your Todo List!",
        }
        return render(request, 'todolist.html', context)


@login_required
def edit_task(request, id):
    if request.method == "POST":
        form = TaskForm(request.POST or None,
                        instance=TaskList.objects.get(pk=id))
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your new Task has been updated successfully!")
            return redirect('todolist')
    else:
        task = TaskList.objects.get(pk=id)
        context = {
            'task': task,
        }
        return render(request, 'edit.html', context)


def completed(request, id):
    task = TaskList.objects.get(pk=id)
    task.done = True
    task.save()
    # GET previous url
    previous_url = request.META.get('HTTP_REFERER')
    parsed_url = urlparse(previous_url)
    query_params = parse_qs(parsed_url.query)
    pg_value = query_params.get('pg', [None])[0]

    res = reverse('todolist') + f"?pg={pg_value}"
    return redirect(res)


def pending(request, id):
    task = TaskList.objects.get(pk=id)
    task.done = False
    task.save()
    # GET previous url
    previous_url = request.META.get('HTTP_REFERER')
    parsed_url = urlparse(previous_url)
    query_params = parse_qs(parsed_url.query)
    pg_value = query_params.get('pg', [None])[0]

    res = reverse('todolist') + f"?pg={pg_value}"
    return redirect(res)
    # return redirect('todolist')


@login_required
def delete_task(request, id):
    task = TaskList.objects.get(pk=id)
    task.delete()
    messages.success(request, "Task has been deleted successfully!")
    return redirect('todolist')


def about(request):
    context = {
        "welcome_text": "Welcome to the About Page!"
    }
    return render(request, 'about.html', context)


@login_required
def contact(request):
    context = {
        "welcome_text": "Welcome to the Contact Page!"
    }
    return render(request, 'contact.html', context)

```

### todolist.models:

```py
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TaskList(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, default=None)
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    # description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self) -> str:
        return f"{self.task} - {self.done} (by {self.owner})"

```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/0258fa19-5d19-4dc4-8d88-0b1eac716fde">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/9da45c4f-1564-4410-ac51-4dd4efbfdc62">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a01cfe23-14f6-452a-a49e-48df7a0d2984">
<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/bdfd047b-67eb-4876-a868-45c45cb9169a">
<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1fa1e8c3-3858-46a9-91d5-9553d424254c">

# #END</details>

<details>
<summary>29. Showing Task of Logged-In User only </summary>

# Showing Task of Logged-In User only

[https://github.com/omeatai/src-python-flask-django/commit/484dbe8a3eb8f7d1657c71ad04e5337318e4bb83](https://github.com/omeatai/src-python-flask-django/commit/484dbe8a3eb8f7d1657c71ad04e5337318e4bb83)

### todolist.views:

```py
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator
from urllib.parse import urlparse, parse_qs
from django.contrib.auth.decorators import login_required

from .models import TaskList
from .forms import TaskForm
# Create your views here.


def home(request):
    context = {
        "welcome_text": "Welcome to the Home Page!"
    }
    return render(request, 'home.html', context)


@login_required(login_url='login')
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.done = False
            instance.owner = request.user
            instance.save()
            messages.success(
                request, "Awesome! Your new Task has been added successfully!")
            return redirect('todolist')
    else:
        # tasks = TaskList.objects.all()
        tasks = TaskList.objects.filter(owner=request.user)
        no_per_pages = 5
        paginator = Paginator(tasks, no_per_pages)
        page = request.GET.get('pg')
        tasks = paginator.get_page(page)

        context = {
            'tasks': tasks,
            "welcome_text": "Welcome to your Todo List!",
        }
        return render(request, 'todolist.html', context)


@login_required
def edit_task(request, id):
    if request.method == "POST":
        form = TaskForm(request.POST or None,
                        instance=TaskList.objects.get(pk=id))
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your new Task has been updated successfully!")
            return redirect('todolist')
    else:
        task = TaskList.objects.get(pk=id)
        context = {
            'task': task,
        }
        return render(request, 'edit.html', context)


def completed(request, id):
    task = TaskList.objects.get(pk=id)
    task.done = True
    task.save()
    # GET previous url
    previous_url = request.META.get('HTTP_REFERER')
    parsed_url = urlparse(previous_url)
    query_params = parse_qs(parsed_url.query)
    pg_value = query_params.get('pg', [None])[0]

    res = reverse('todolist') + f"?pg={pg_value}"
    return redirect(res)


def pending(request, id):
    task = TaskList.objects.get(pk=id)
    task.done = False
    task.save()
    # GET previous url
    previous_url = request.META.get('HTTP_REFERER')
    parsed_url = urlparse(previous_url)
    query_params = parse_qs(parsed_url.query)
    pg_value = query_params.get('pg', [None])[0]

    res = reverse('todolist') + f"?pg={pg_value}"
    return redirect(res)
    # return redirect('todolist')


@login_required
def delete_task(request, id):
    task = TaskList.objects.get(pk=id)
    task.delete()
    messages.success(request, "Task has been deleted successfully!")
    return redirect('todolist')


def about(request):
    context = {
        "welcome_text": "Welcome to the About Page!"
    }
    return render(request, 'about.html', context)


@login_required
def contact(request):
    context = {
        "welcome_text": "Welcome to the Contact Page!"
    }
    return render(request, 'contact.html', context)

```

### src-python/udemy/django-A-Z/todolist/templates/todolist.html:

```py
{% extends "todolist/base.html" %}

{% block title %}
Welcome
{% endblock title %}

{% block content %}
<h2>{{ welcome_text }}</h2>

<form method="POST" class="row my-3">
    {% csrf_token %}

    {% if messages %}

    {% for message in messages %}
    {% comment %} <div class="alert alert-success" role="alert">
        {{ message }}
    </div> {% endcomment %}

    <div class="alert alert-success alert-dismissible fade show" role="alert">
        {{ message }}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>

    {% endfor %}

    {% endif %}

    <div class="mb-3">
        <label for="task" class="form-label">Add Task</label>
        <input type="text" class="form-control" id="task" name="task" aria-describedby="textHelp"
            placeholder="Call Alex...">
        <div id="textHelp" class="form-text">What would you want to do?</div>
    </div>
    <button type="submit" class="btn btn-primary">ADD TASK</button>
</form>


<table class="table table-light table-striped table-hover table-bordered text-center">
    <thead>
        <tr class="table-dark row">
            <th class="col-7">Task</th>
            <th class="col-3">Done</th>
            <th class="col-1">Edit</th>
            <th class="col-1">Delete</th>
        </tr>
    </thead>
    <tbody>
        {% if tasks %}

        {% for todo in tasks %}

        {% if todo.done %}
        <tr class="table-success row">
            <th class="col-7"><del>{{ todo.task }}</del> <small>(by {{ todo.owner|title }})</small></th>
            <td class="col-3"><a href="{% url 'pending' todo.id %}" type="button" class="btn btn-success btn-sm">YES - Mark as Pending</a></td>
            <td class="col-1"><a href="{% url 'edit-task' todo.id %}" type="button" class="btn btn-warning">Edit</a></td>
            <td class="col-1"><a href="{% url 'delete-task' todo.id %}" type="button" class="btn btn-danger">Delete</a></td>
        </tr>
        {% else %}
        <tr class="row">
            <th class="col-7">{{ todo.task }} <small>(by {{ todo.owner|title }})</small></th>
            <td class="col-3"><a href="{% url 'completed' todo.id %}" type="button" class="btn btn-danger btn-sm">NO - Mark as Completed</a></td>
            <td class="col-1"><a href="{% url 'edit-task' todo.id %}" type="button" class="btn btn-warning">Edit</a></td>
            <td class="col-1"><a href="{% url 'delete-task' todo.id %}" type="button" class="btn btn-danger">Delete</a></td>
        </tr>
        {% endif %}

        {% endfor %}

        {% endif %}
    </tbody>
</table>

<nav aria-label="Page navigation example">
  <ul class="pagination justify-content-center">

    {% comment %} {% for i in tasks.paginator.page_range %}{% endfor %}{% endcomment %}

    <li class="page-item {% if not tasks.has_previous %} disabled {% endif %}">
      <a class="page-link" href="?pg=1">First</a>
    </li>

    {% if tasks.has_previous %}
    <li class="page-item">
      <a class="page-link" href="?pg={{ tasks.previous_page_number }}">Previous</a>
    </li>

    <li class="page-item"><a class="page-link" href="?pg={{ tasks.previous_page_number }}">{{ tasks.previous_page_number }}</a></li>
    {% endif %}

     <li class="page-item active"><a class="page-link" href="#">{{ tasks.number }}</a></li>


    {% if tasks.has_next %}
    <li class="page-item"><a class="page-link" href="?pg={{ tasks.next_page_number }}">{{ tasks.next_page_number }}</a></li>

    <li class="page-item">
      <a class="page-link" href="?pg={{ tasks.next_page_number }}">Next</a>
    </li>
    {% endif %}

    <li class="page-item {% if not tasks.has_next %} disabled {% endif %}">
      <a class="page-link" href="?pg={{ tasks.paginator.num_pages }}">Last</a>
    </li>
  </ul>
</nav>


{% endblock content %}
```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ee798918-a0e5-4814-a3f3-e04c35176d00">
<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1bf29b62-4325-4717-9382-f0780d996acf">
<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/8063b383-0de8-490b-9a89-77fd7c327550">

# #END</details>

<details>
<summary>30. Allow only Owners to Update, Delete or changes Status of their Tasks </summary>

# Allow only Owners to Update, Delete or changes Status of their Tasks

[https://github.com/omeatai/src-python-flask-django/commit/6f5f8d6591a65b34dd77615fdc78dca64fe6958b](https://github.com/omeatai/src-python-flask-django/commit/6f5f8d6591a65b34dd77615fdc78dca64fe6958b)

### todolist.views:

```py
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator
from urllib.parse import urlparse, parse_qs
from django.contrib.auth.decorators import login_required

from .models import TaskList
from .forms import TaskForm
# Create your views here.


def home(request):
    context = {
        "welcome_text": "Welcome to the Home Page!"
    }
    return render(request, 'home.html', context)


@login_required(login_url='login')
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.done = False
            instance.owner = request.user
            instance.save()
            messages.success(
                request, "Awesome! Your new Task has been added successfully!")
            return redirect('todolist')
    else:
        # tasks = TaskList.objects.all()
        tasks = TaskList.objects.filter(owner=request.user)
        no_per_pages = 5
        paginator = Paginator(tasks, no_per_pages)
        page = request.GET.get('pg')
        tasks = paginator.get_page(page)

        context = {
            'tasks': tasks,
            "welcome_text": "Welcome to your Todo List!",
        }
        return render(request, 'todolist.html', context)


@login_required
def edit_task(request, id):
    if request.method == "POST":
        form = TaskForm(request.POST or None,
                        instance=TaskList.objects.get(pk=id))
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your new Task has been updated successfully!")
            return redirect('todolist')
    else:
        task = TaskList.objects.get(pk=id)
        context = {
            'task': task,
        }
        return render(request, 'edit.html', context)


@login_required
def completed(request, id):
    task = TaskList.objects.get(pk=id)
    if task.owner == request.user:
        task.done = True
        task.save()
        # GET previous url
        previous_url = request.META.get('HTTP_REFERER')
        parsed_url = urlparse(previous_url)
        query_params = parse_qs(parsed_url.query)
        pg_value = query_params.get('pg', [None])[0]

        res = reverse('todolist') + f"?pg={pg_value}"
        return redirect(res)
    else:
        messages.error(
            request, "You are not allowed to mark this task as completed!")
        return redirect('todolist')


@login_required
def pending(request, id):
    task = TaskList.objects.get(pk=id)
    if task.owner == request.user:
        task.done = False
        task.save()
        # GET previous url
        previous_url = request.META.get('HTTP_REFERER')
        parsed_url = urlparse(previous_url)
        query_params = parse_qs(parsed_url.query)
        pg_value = query_params.get('pg', [None])[0]

        res = reverse('todolist') + f"?pg={pg_value}"
        return redirect(res)
    else:
        messages.error(
            request, "You are not allowed to mark this task as pending!")
        return redirect('todolist')


@login_required
def delete_task(request, id):
    task = TaskList.objects.get(pk=id)
    if task.owner == request.user:
        task.delete()
        messages.success(request, "Task has been deleted successfully!")
    else:
        messages.error(
            request, "You are not allowed to delete this task!")
    return redirect('todolist')


def about(request):
    context = {
        "welcome_text": "Welcome to the About Page!"
    }
    return render(request, 'about.html', context)


@login_required
def contact(request):
    context = {
        "welcome_text": "Welcome to the Contact Page!"
    }
    return render(request, 'contact.html', context)

```

### src-python/udemy/django-A-Z/todolist/templates/edit.html:

```py
{% extends "todolist/base.html" %}

{% block title %}
Welcome
{% endblock title %}

{% block content %}
<h2>{{ welcome_text }}</h2>

{% if task.owner == request.user %}

<form method="POST" class="row my-3">
    {% csrf_token %}

    {% if messages %}

    {% for message in messages %}

    <div class="alert alert-success alert-dismissible fade show" role="alert">
        {{ message }}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>

    {% endfor %}

    {% endif %}

    <div class="mb-3">
        <label for="task" class="form-label">Edit Task</label>
        <input type="text" class="form-control" id="task" name="task" value="{{ task.task }}" aria-describedby="textHelp"
            placeholder="{{ task.task }}">
        <div id="textHelp" class="form-text">Make your changes</div>
    </div>
    <div class="mb-3">
        {% comment %} <input type='hidden' name="done" value="{{ task.done }}" /> {% endcomment %}

        <label for="done" class="form-label">Is it Done?</label>
        <select class="form-select" id="done" name="done" aria-label="Default select example">
            <option value=False {% if not task.done %} selected {% endif %}>NO</option>
            <option value=True {% if task.done %} selected {% endif %}>YES</option>
        </select>
    </div>
    <button type="submit" class="btn btn-primary my-2">Update TASK</button>
    <a href="{% url 'todolist' %}" class="btn btn-danger my-2">Back</a>
</form>

{% else %}

<h2>Access Denied! You are Not the Owner of this Post!</h2>
<a href="{% url 'todolist' %}" class="btn btn-danger my-2">Go To Your Todolist</a>

{% endif %}

{% endblock content %}
```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/caeaf8ef-43bc-48d0-99f7-1a454b84645b">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/05a13074-87ef-4209-ac2b-79314ddfbef9">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e01329e7-6110-4a24-92f1-268570fcf576">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/7eb5f0a8-2e96-448b-b085-621abe52e4e8">

# #END</details>

<details>
<summary>31. Connect PostgreSQL Database </summary>

# Connect PostgreSQL Database

[https://github.com/omeatai/src-python-flask-django/commit/5bb357bc434afaed09e1113094a862a01d515897](https://github.com/omeatai/src-python-flask-django/commit/5bb357bc434afaed09e1113094a862a01d515897)

## Install psycopg2

```py
pip install psycopg2
```

### taskmate.settings:

```py
# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

```

## Make Migrations

```py
python manage.py makemigrations
python manage.py migrate
```

## Create SuperUser

```py
python manage.py createsuperuser
```

## Run Dev Server

```py
python manage.py runserver
```

<img width="763" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/9f325a9d-21ba-403b-88cb-48618213066c">
<img width="1426" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/360aa47c-e52b-4e49-8ba5-0c7e1f4c9be6">
<img width="1350" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/71c3dc64-e62a-421a-8f7f-dd5f68413b93">
<img width="1382" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a6051e6d-a525-4491-b8a8-77a682053b49">

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/7567daca-eed8-4a71-af3d-a1716efd60ca)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/55e2f81e-c9f9-4e6a-97e2-faa0e3885b05)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/55b2c7b7-9520-4aff-81ab-7d2411181a4a)

<img width="1394" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/14708696-36fa-486f-a296-53fa90f14fe5">

# #END</details>

<details>
<summary>32. Deploy to Production </summary>

# Deploy to Production

## Install latest version of git

```py
brew install git
```

## Install venv

```py
python -m venv myproject-env
source myproject-env/bin/activate
```

```py
pip install virtualenv
virtualenv myproject-env
```

## Install Django

```py
python -m pip install Django
```

## Upgrade Django Version

```py
pip install --upgrade django==4.2
pip install django --upgrade
python -m pip install Django==5.0.4
```

## Install Crispy Forms

```py
pip install crispy-bootstrap5
```

## Install psycopg2

```py
pip install psycopg2
```

## Save Dependencies to Requirements.txt

```py
pip freeze
pip freeze > requirements.txt
```

## Install requirements from Requirements.txt

```py
pip install -r requirements.txt
```

## Deactivate a virtual environment

```py
deactivate
```

### .gitignore File:

```txt
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class
Ex_Files/
exercise_files/

# C extensions
*.so

# Distribution / packaging
dist/
build/
*.egg-info/
*.egg

# Virtual environments
venv/
env/
env.bak/
env1/
env2/

# IDEs and editors
.idea/
.vscode/
*.sublime-project
*.sublime-workspace

# Logs and databases
*.log
*.sqlite3
*.db

# OS generated files
.DS_Store
Thumbs.db

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/#use-with-ide
.pdm.toml

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/
```

## Install django-environ

```py
pip install django-environ
```

Create .env file in same directory where settings.py exists and add the following:

- DJANGO_SECRET_KEY=XXX
- DJANGO_DEBUG=True

- DJANGO_DB_NAME=postgres
- DJANGO_DB_USER=postgres
- DJANGO_DB_PASSWORD=
- DJANGO_DB_HOST=localhost
- DJANGO_DB_PORT=5432

### taskmate.settings:

```py
from pathlib import Path
import os

import environ

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DJANGO_DEBUG")

ALLOWED_HOSTS = ALLOWED_HOSTS = ["localhost", "127.0.0.1", "*"]
CSRF_TRUSTED_ORIGINS = ['https://your-base-domain']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DJANGO_DB_NAME'),
        'USER': env('DJANGO_DB_USER'),
        'PASSWORD': env('DJANGO_DB_PASSWORD'),
        'HOST': env('DJANGO_DB_HOST'),
        'PORT': env('DJANGO_DB_PORT'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

```

## Run Collectstatic

```py
python manage.py collectstatic
```

## Install Whitenoise

```py
pip install whitenoise
```

### taskmate.settings:

```py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', #added whitenoise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

```

## Create Github Project - Taskmate

## Set email and name

```py
git config --global user.name "o"
git config --global user.email "o@gmail.com"
```

### create a new repository on the command line

```py
echo "# project-django-taskmate" >> README.md
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add taskmate https://github.com/omeatai/project-django-taskmate.git
git push -u taskmate main
```

### push an existing repository from the command line

```py
git remote add taskmate https://github.com/omeatai/project-django-taskmate.git
git branch -M main
git push -u taskmate main
```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/130b9f54-a98b-4ec2-b479-feb9d75e8a8d">

## Configure SamKirkland/FTP-Deploy for Namecheap hosting

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/1ecd3b8b-ac17-440c-8ae1-d5ef19541868)

### /.github/workflows/main.yml

[https://github.com/SamKirkland/FTP-Deploy-Action](https://github.com/SamKirkland/FTP-Deploy-Action)

[Deploy To Shared Hosting With Github Actions](https://youtu.be/UNWIXYSZfZY?si=KpqsJOvREIEQ3dfV)

[Deploy Django 4.0 to Shared Hosting](https://youtu.be/nvq7NNSfKdw?si=LVJOM3xW6VukdtWi)

[https://pythonfusion.com/deploy-django-on-shared-hosting/](https://pythonfusion.com/deploy-django-on-shared-hosting/)

[https://www.namecheap.com/support/knowledgebase/article.aspx/1249/89/how-to-remotely-connect-to-a-mysql-database-located-on-our-shared-server/](https://www.namecheap.com/support/knowledgebase/article.aspx/1249/89/how-to-remotely-connect-to-a-mysql-database-located-on-our-shared-server/)

```py
on: push
name: 🚀 Deploy taskmate website on push
jobs:
  web-deploy:
    name: 🎉 Deploy
    runs-on: ubuntu-latest
    steps:
      - name: 🚚 Get latest code
        uses: actions/checkout@v4

      - name: 📂 Sync files
        uses: SamKirkland/FTP-Deploy-Action@v4.3.5
        with:
          server: ftp.ifeanyiomeata.com
          username: taskmate@ifeanyiomeata.com
          password: ${{ secrets.ftp_password }}
          protocol: ftp
          port: 21
          server-dir: /public_html/projects/taskmate/

```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/ee315874-29bf-4a36-9eb0-daddb9b260e0)

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/22204623-ffc9-4745-be92-52797a0bbe78">
<img width="1414" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/d6ea157f-e6a9-416e-913b-f7c2a7379ba1">

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/9fa1abb8-987e-490f-b717-2515a71d82a1)

## Install requirements

```py
pip install -r requirements.txt

pip install django==3.1 psycopg2-binary django-environ whitenoise crispy-bootstrap4
pip install django psycopg2 django-environ whitenoise crispy-bootstrap5

source /home/omeatai/virtualenv/taskmate/3.9/bin/activate && cd /home/omeatai/taskmate
cd ../public_html/project_taskmate/
psql -p 5432 <dbname> <dbuser>

psql -V
psql --version
```

## Make Migrations

```py
python manage.py makemigrations
python manage.py migrate
```

## For MySQL Database (Edit the **init**.py file)

```py
pip install mysqlclient

pip install pymysql
```

```py
import pymysql

pymysql.install_as_MySQLdb()
```

```py
 'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'databasename',
        'USER': 'databaseusername',
        'PASSWORD': 'databasepassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
```

# Revert to Crispy-Forms Bootstrap 4

[https://getbootstrap.com/docs/4.6/getting-started/introduction/](https://getbootstrap.com/docs/4.6/getting-started/introduction/)

[https://pypi.org/project/crispy-bootstrap4/](https://pypi.org/project/crispy-bootstrap4/)

## Install Crispy-Bootstrap4

```py
pip install crispy-bootstrap4
```

## Update INSTALLED_APPS in settings.py

```py
INSTALLED_APPS = (
    ...
    "crispy_forms",
    "crispy_bootstrap4",
    ...
)
```

## Add CRISPY_TEMPLATE_PACK in settings.py

```py
CRISPY_TEMPLATE_PACK = "bootstrap4"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
```

# Revert to Crispy-Forms Bootstrap 5

[https://getbootstrap.com/](https://getbootstrap.com/)

[https://github.com/django-crispy-forms/crispy-bootstrap5](https://github.com/django-crispy-forms/crispy-bootstrap5)

## Install Crispy-Bootstrap5

```py
pip install crispy-bootstrap5
```

## Update INSTALLED_APPS in settings.py

```py
INSTALLED_APPS = (
    ...
    "crispy_forms",
    "crispy_bootstrap5",
    ...
)
```

## Add CRISPY_TEMPLATE_PACK in settings.py

```py
CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
```

# Setup passenger_wsgi.py

```py
# from taskmate.wsgi import application

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

def application(environ, start_response):
    start_response('200 OK', [(Content-Type, 'text/plain')])
    message = 'It works!'
    response = message
    return [response.encode()]
```

[taskmate.ifeanyiomeata.com/todolist/](taskmate.ifeanyiomeata.com/todolist/)

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/e68abb6f-bbab-4cb7-9b08-3d53f8532845)

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/45ded09c-b989-486d-8b50-0fc0fec5f1bf)

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/7bde54ca-daa0-4422-b4d8-099aa64365c2)

## Run collectstatic

```py
python manage.py collectstatic
```

## Run createsuperuser

```py
python manage.py createsuperuser
```

## Export all the data from the database to a json file

```py
python manage.py dumpdata>data.json
```

## Clear the new database

```py
python manage.py flush
```

## Load the data from the data.json file into the new database

```py
python manage.py loaddata data.json
```

# #END</details>

# #END
