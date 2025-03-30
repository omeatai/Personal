    
## +LinkedIn - Building a Personal Portfolio with Django

## [COURSE](https://www.linkedin.com/learning/building-a-personal-portfolio-with-django/creating-a-website-with-python)

<details>
<summary>1. Creating a New Django Project </summary>

# Creating a New Django Project

## Install venv

```py
python -m venv myproject-env
source myproject-env/bin/activate
```

## Install Django

```py
python -m pip install Django
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
django-admin startproject portfolio .
```

## Start Local Server

```py
python manage.py runserver
```

# #END</details>

<details>
<summary>2. Creating Django App - Jobs </summary>

# Creating Django App - Jobs

[https://github.com/omeatai/src-python-flask-django/commit/227ea7c95e1918f8136d184a859f5690c367e5c5](https://github.com/omeatai/src-python-flask-django/commit/227ea7c95e1918f8136d184a859f5690c367e5c5)

## Create App

```py
django-admin startapp jobs
```

### portfolio.settings:

```py
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'jobs',
]
```

## Run Local Server

```py
python manage.py runserver
```

<img width="1420" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a8b0bbba-4445-4199-849d-9a8f8b046759">
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/fe28f420-5507-4ca2-bc5a-58eed67a590e)

# #END</details>

<details>
<summary>3. Setup URL, Views and Templates </summary>

# Setup URL, Views and Templates

[https://github.com/omeatai/src-python-flask-django/commit/1ce588a46d2e149c513207c96865ff7bf07c0ea7](https://github.com/omeatai/src-python-flask-django/commit/1ce588a46d2e149c513207c96865ff7bf07c0ea7)

### portfolio.urls:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobs.urls')),
]
```

### jobs.urls:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
]

```

### jobs.views:

```py
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'jobs/home.html', {})

```

### src-python/linkedin/django-personal-portfolio/jobs/templates/jobs/home.html:

```py
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HomePage</title>
</head>

<body>
    <h1>Hello World!</h1>
</body>

</html>
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/970501cd-942b-4527-a718-b0cea40380d3)
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/2a33a870-eff3-4c4c-b697-14801e23cf83">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/59e4d4d6-459f-480b-96aa-45ffb27ea8f8">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/bb30e39c-efe7-40dc-be48-a5243416de54">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/96eaa040-50a5-4f2a-b3e4-40370b4e7aaf">

# #END</details>

<details>
<summary>4. Creating Models in Django </summary>

# Creating Models in Django

[https://github.com/omeatai/src-python-flask-django/commit/780144938397964962e4b786cfd724dc145045a8](https://github.com/omeatai/src-python-flask-django/commit/780144938397964962e4b786cfd724dc145045a8)

## Install Pillow

```py
pip install pillow
```

## Run Local Server

```py
python manage.py runserver
```

### jobs.models:

```py
from django.db import models
# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # date = models.DateField()
    # description = models.TextField()
    # url = models.URLField()
    # company = models.CharField(max_length=100)
    # position = models.CharField(max_length=100)
    # location = models.CharField(max_length=100)

```

<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/659e18a7-99fc-44f0-bb89-5745f661bbf1">

# #END</details>

<details>
<summary>5. Setup PostgreSQL for Django </summary>

# Setup PostgreSQL for Django

[https://github.com/omeatai/src-python-flask-django/commit/5aaa98696ea594578f7e3f1c555d12d09660e028](https://github.com/omeatai/src-python-flask-django/commit/5aaa98696ea594578f7e3f1c555d12d09660e028)

[https://www.postgresql.org/](https://www.postgresql.org/)

## Create Password for Postgres

```x
postgres=# \password postgres
Enter new password for user "postgres": 
Enter it again: 
postgres=# 
```

## Create Portfolio Database

```py
postgres=# CREATE DATABASE portfoliodb;
CREATE DATABASE
postgres=# 
```

## Install Psycopg2

```py
pip install psycopg2
```

## Install Django-environ

```py
pip install django-environ
```

- In the same directory as settings.py, create a file called ‘.env’
- Declare your environment variables in .env
- Make sure you don’t use quotations around strings.
- IMPORTANT: Add your .env file to .gitignore

```x
DATABASE_NAME=portfoliodb
DATABASE_USER=postgres
DATABASE_PASS=supersecretpassword
```

### portfolio.settings:

```py
import environ
env = environ.Env()
environ.Env.read_env()


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfoliodb',
        'USER': 'postgres',
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': 'localhost',  # 127.0.0.1
        'PORT': '5432',
    }
}
```

## Run Migrations

```py
python manage.py makemigrations
python manage.py migrate
```

## Run Local Server

```py
python manage.py runserver
```

<img width="219" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/8496d476-8a7b-45c5-a341-90a38678b92b">

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/f9f8740a-553c-4c7b-a15f-3db5666610ff)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/1fac7b3b-53ea-4502-8f20-4059048635a0)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/4ea617c9-716f-467d-bad9-aa8a0e041790)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/ad3b1721-236b-443a-a965-8d66e25f6da9)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/624f2fb3-e3aa-40e1-88b4-5d19962d5835)

<img width="763" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/afbe7d2d-4a88-4086-bcf7-b85fef9180a4">
<img width="763" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ecbf236f-1aa8-485e-aced-918c2e01e41a">
<img width="682" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/0c4e4d73-ef28-41cd-a513-ba24628a81c4">
<img width="671" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ff5df38d-cfcd-44fb-bf94-83126f6914be">
<img width="763" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/819787d6-f111-4cd0-9d46-75b4ba63c086">
<img width="862" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/776130c5-d56d-40e8-8a9b-6611d90afbcd">
<img width="1426" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/eaf5ffd0-c3b0-4e4c-b9ac-ce00a39cc110">
<img width="1426" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/26b48359-2810-4a22-a895-d0a7c3d3055a">

# #END</details>

<details>
<summary>6. Setup Django Admin Panel  </summary>

# Setup Django Admin Panel 

[https://github.com/omeatai/src-python-flask-django/commit/f453a68d89b1d7c15c30a0b643a6a951daeed426](https://github.com/omeatai/src-python-flask-django/commit/f453a68d89b1d7c15c30a0b643a6a951daeed426)

## Create Django Superuser

```py
python manage.py createsuperuser
```

### jobs.admin:

```py
from django.contrib import admin
from .models import Job

# Register your models here.
admin.site.register(Job)

```

<img width="1420" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/8fb2e7d4-8286-4c98-898c-28ca77657600">

### http://127.0.0.1:8000/admin:

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/11c7e95e-81bd-464a-a64f-1fa552505d75)

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/f08f528c-a223-40d9-86bb-972822a792fd">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/0a39b127-762a-44e6-b6b4-b87125f1b672">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/913b54ae-1451-4141-b26d-64f749744be1">

# #END</details>

<details>
<summary>7. Create Jobs in Admin Panel  </summary>

# Create Jobs in Admin Panel 

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/14c47c31-3ff2-4291-98cc-b1710bfa2fb7">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b2104630-2119-4ea8-aa59-f40c8b96e0d6">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/26bcbd51-d1b1-419d-bfa2-5f1f815c3eae">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b89e3927-91d1-4ed4-9067-5abc0a89b47e">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e98c9874-92a5-4554-909e-36a1e18d69ed">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a3ad9af0-961d-4f84-8536-ca38ce711f76">

# #END</details>

<details>
<summary>8. Pulling Objects from Database  </summary>

# Pulling Objects from Database

[https://github.com/omeatai/src-python-flask-django/commit/500292e12ff3a34d76c09906963794c007e6987f](https://github.com/omeatai/src-python-flask-django/commit/500292e12ff3a34d76c09906963794c007e6987f)

### jobs.views:

```py
from django.shortcuts import render
from .models import Job
# Create your views here.


def home(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/home.html', {'jobs': jobs})

```

### src-python/linkedin/django-personal-portfolio/jobs/templates/jobs/home.html:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HomePage</title>
</head>

<body>
    <h1>All my Jobs</h1>
    {% for job in jobs %}
    <h2>{{ job.title }}</h2>
    <p>{{ job.summary }}</p>
    <img src='/images/1.webp' alt='{{ job.title }}' />
    {% endfor %}
</body>

</html>
```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ebf8c8de-6df9-4d65-bd75-e6fb86dfee69">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/be86c166-c5eb-414b-b684-5f76cedc83e8">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/7b9adf65-1756-4326-bb5f-4ad5456e29b9">

# #END</details>

<details>
<summary>9. Bootstrap Layout and Template </summary>

# Bootstrap Layout and Template

[https://github.com/omeatai/src-python-flask-django/commit/ea34e8361eb8fcc0bce828ecb85bc80626af85e0](https://github.com/omeatai/src-python-flask-django/commit/ea34e8361eb8fcc0bce828ecb85bc80626af85e0)

[https://getbootstrap.com/](https://getbootstrap.com/)
[https://getbootstrap.com/docs/5.3/examples/album/](https://getbootstrap.com/docs/5.3/examples/album/)

### jobs.models:

```py
from django.db import models
# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # date = models.DateField()
    # description = models.TextField()
    # url = models.URLField()
    # company = models.CharField(max_length=100)
    # position = models.CharField(max_length=100)
    # location = models.CharField(max_length=100)

```

### jobs.views:

```py
from django.shortcuts import render
from .models import Job
# Create your views here.


def home(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/home.html', {'jobs': jobs})

```

### src-python/linkedin/django-personal-portfolio/jobs/templates/jobs/home.html:

```html
<!DOCTYPE html>
<html lang="en" data-bs-theme="auto">

<head>
    <script src="https://getbootstrap.com/docs/5.3/assets/js/color-modes.js"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Hugo 0.122.0">
    <title>Ifeanyi Omeata</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/5.3/examples/album/">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@docsearch/css@3">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">

    <!-- Favicons -->
    <link rel="apple-touch-icon" href="/docs/5.3/assets/img/favicons/apple-touch-icon.png" sizes="180x180">
    <link rel="icon" href="/docs/5.3/assets/img/favicons/favicon-32x32.png" sizes="32x32" type="image/png">
    <link rel="icon" href="/docs/5.3/assets/img/favicons/favicon-16x16.png" sizes="16x16" type="image/png">
    <link rel="manifest" href="/docs/5.3/assets/img/favicons/manifest.json">
    <link rel="mask-icon" href="/docs/5.3/assets/img/favicons/safari-pinned-tab.svg" color="#712cf9">
    <link rel="icon" href="/docs/5.3/assets/img/favicons/favicon.ico">
    <meta name="theme-color" content="#712cf9">


    <style>
        .bd-placeholder-img {
            font-size: 1.125rem;
            text-anchor: middle;
            -webkit-user-select: none;
            -moz-user-select: none;
            user-select: none;
        }

        @media (min-width: 768px) {
            .bd-placeholder-img-lg {
                font-size: 3.5rem;
            }
        }

        .b-example-divider {
            width: 100%;
            height: 3rem;
            background-color: rgba(0, 0, 0, .1);
            border: solid rgba(0, 0, 0, .15);
            border-width: 1px 0;
            box-shadow: inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15);
        }

        .b-example-vr {
            flex-shrink: 0;
            width: 1.5rem;
            height: 100vh;
        }

        .bi {
            vertical-align: -.125em;
            fill: currentColor;
        }

        .nav-scroller {
            position: relative;
            z-index: 2;
            height: 2.75rem;
            overflow-y: hidden;
        }

        .nav-scroller .nav {
            display: flex;
            flex-wrap: nowrap;
            padding-bottom: 1rem;
            margin-top: -1px;
            overflow-x: auto;
            text-align: center;
            white-space: nowrap;
            -webkit-overflow-scrolling: touch;
        }

        .btn-bd-primary {
            --bd-violet-bg: #712cf9;
            --bd-violet-rgb: 112.520718, 44.062154, 249.437846;

            --bs-btn-font-weight: 600;
            --bs-btn-color: var(--bs-white);
            --bs-btn-bg: var(--bd-violet-bg);
            --bs-btn-border-color: var(--bd-violet-bg);
            --bs-btn-hover-color: var(--bs-white);
            --bs-btn-hover-bg: #6528e0;
            --bs-btn-hover-border-color: #6528e0;
            --bs-btn-focus-shadow-rgb: var(--bd-violet-rgb);
            --bs-btn-active-color: var(--bs-btn-hover-color);
            --bs-btn-active-bg: #5a23c8;
            --bs-btn-active-border-color: #5a23c8;
        }

        .bd-mode-toggle {
            z-index: 1500;
        }

        .bd-mode-toggle .dropdown-menu .active .bi {
            display: block !important;
        }
    </style>


</head>

<body>

    <svg xmlns="http://www.w3.org/2000/svg" class="d-none">
        <symbol id="check2" viewBox="0 0 16 16">
            <path
                d="M13.854 3.646a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L6.5 10.293l6.646-6.647a.5.5 0 0 1 .708 0z" />
        </symbol>
        <symbol id="circle-half" viewBox="0 0 16 16">
            <path d="M8 15A7 7 0 1 0 8 1v14zm0 1A8 8 0 1 1 8 0a8 8 0 0 1 0 16z" />
        </symbol>
        <symbol id="moon-stars-fill" viewBox="0 0 16 16">
            <path
                d="M6 .278a.768.768 0 0 1 .08.858 7.208 7.208 0 0 0-.878 3.46c0 4.021 3.278 7.277 7.318 7.277.527 0 1.04-.055 1.533-.16a.787.787 0 0 1 .81.316.733.733 0 0 1-.031.893A8.349 8.349 0 0 1 8.344 16C3.734 16 0 12.286 0 7.71 0 4.266 2.114 1.312 5.124.06A.752.752 0 0 1 6 .278z" />
            <path
                d="M10.794 3.148a.217.217 0 0 1 .412 0l.387 1.162c.173.518.579.924 1.097 1.097l1.162.387a.217.217 0 0 1 0 .412l-1.162.387a1.734 1.734 0 0 0-1.097 1.097l-.387 1.162a.217.217 0 0 1-.412 0l-.387-1.162A1.734 1.734 0 0 0 9.31 6.593l-1.162-.387a.217.217 0 0 1 0-.412l1.162-.387a1.734 1.734 0 0 0 1.097-1.097l.387-1.162zM13.863.099a.145.145 0 0 1 .274 0l.258.774c.115.346.386.617.732.732l.774.258a.145.145 0 0 1 0 .274l-.774.258a1.156 1.156 0 0 0-.732.732l-.258.774a.145.145 0 0 1-.274 0l-.258-.774a1.156 1.156 0 0 0-.732-.732l-.774-.258a.145.145 0 0 1 0-.274l.774-.258c.346-.115.617-.386.732-.732L13.863.1z" />
        </symbol>
        <symbol id="sun-fill" viewBox="0 0 16 16">
            <path
                d="M8 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0zm0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13zm8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5zM3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8zm10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0zm-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0zm9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707zM4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708z" />
        </symbol>
    </svg>

    <div class="dropdown position-fixed bottom-0 end-0 mb-3 me-3 bd-mode-toggle">
        <button class="btn btn-bd-primary py-2 dropdown-toggle d-flex align-items-center" id="bd-theme" type="button"
            aria-expanded="false" data-bs-toggle="dropdown" aria-label="Toggle theme (auto)">
            <svg class="bi my-1 theme-icon-active" width="1em" height="1em">
                <use href="#circle-half"></use>
            </svg>
            <span class="visually-hidden" id="bd-theme-text">Toggle theme</span>
        </button>
        <ul class="dropdown-menu dropdown-menu-end shadow" aria-labelledby="bd-theme-text">
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="light"
                    aria-pressed="false">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#sun-fill"></use>
                    </svg>
                    Light
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="dark"
                    aria-pressed="false">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#moon-stars-fill"></use>
                    </svg>
                    Dark
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center active" data-bs-theme-value="auto"
                    aria-pressed="true">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#circle-half"></use>
                    </svg>
                    Auto
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
        </ul>
    </div>


    <header data-bs-theme="dark">
        <div class="collapse text-bg-dark" id="navbarHeader">
            <div class="container">
                <div class="row">
                    <div class="col-sm-8 col-md-7 py-4">
                        <h4>About</h4>
                        <p class="text-body-secondary">Hi! I am Ifeanyi, a Software Engineer and Full-Stack
                            Developer based here in the beautiful province of Alberta, Canada. With a track record of
                            over 6 years in the field, I excel in creating resilient, scalable, and user-centric web,
                            mobile and data-driven applications that tackle real-world challenges head-on.</p>
                    </div>
                    <div class="col-sm-4 offset-md-1 py-4">
                        <h4>Contact</h4>
                        <ul class="list-unstyled">
                            <li><a href="https://twitter.com/iomeata" target="_blank" class="text-white">Follow on
                                    Twitter</a></li>
                            <li><a href="https://www.linkedin.com/in/omeatai/" target="_blank" class="text-white">Follow
                                    on LinkedIn</a></li>
                            <li><a href="mailto:omeatai@gmail.com?subject=Contact Form on Website&cc="
                                    class="text-white">Email me</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        <div class="navbar navbar-dark bg-dark shadow-sm">
            <div class="container">
                <a href="#" class="navbar-brand d-flex align-items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" stroke="currentColor"
                        stroke-linecap="round" stroke-linejoin="round" stroke-width="2" aria-hidden="true" class="me-2"
                        viewBox="0 0 24 24">
                        <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z" />
                        <circle cx="12" cy="13" r="4" /></svg>
                    <strong>Ifeanyi Omeata</strong>
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarHeader"
                    aria-controls="navbarHeader" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
            </div>
        </div>
    </header>

    <main>

        <section class="py-2 text-center container">
            <div class="row py-lg-5">
                <div class="col-lg-6 col-md-8 mx-auto">
                    <h1 class="fw-light">Ifeanyi Omeata</h1>
                    <p class="lead text-body-secondary">Hi! My name is Ifeanyi Omeata, a Software Engineer and
                        Full-Stack
                        Developer based here in the beautiful province of Alberta, Canada. With a track record of
                        over 6 years in the field, I excel in creating resilient, scalable, and user-centric web,
                        mobile and data-driven applications that tackle real-world challenges head-on.</p>
                    <p>
                        <a href="#all-jobs" class="btn btn-primary my-2">View my Jobs</a>
                        <a href="mailto:omeatai@gmail.com?subject=Contact Form on Website&cc="
                            class="btn btn-secondary my-2">Email me</a>
                    </p>
                </div>
            </div>
        </section>

        <div class="album py-2 bg-body-tertiary">
            <div class="container">

                <h1 id="all-jobs" class="text-center pb-2">My Jobs</h1>

                <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">

                    {% for job in jobs %}

                    <div class="col">
                        <div class="card shadow-sm">
                            <svg class="bd-placeholder-img card-img-top" width="100%" height="225"
                                xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Thumbnail"
                                preserveAspectRatio="xMidYMid slice" focusable="false">
                                <title>{{ job.title }}</title>
                                <rect width="100%" height="100%" fill="#55595c" /><text x="50%" y="50%" fill="#eceeef"
                                    dy=".3em">{{ job.title }}</text>
                            </svg>
                            <div class="card-body">
                                <p class="card-text">{{ job.summary }}</p>
                                <div class="d-flex justify-content-between align-items-center">
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                                        <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
                                    </div>
                                    <small class="text-body-secondary">{{ job.image }}</small>
                                </div>
                            </div>
                        </div>
                    </div>

                    {% endfor %}
                </div>
            </div>
        </div>
    </main>

    <footer class="text-body-secondary py-5">
        <div class="container">
            <p class="float-end mb-1">
                <a href="#">Back to top</a>
            </p>
            <p class="mb-1">Copyright. Ifeanyi omeata &copy; 2024.</p>
            <p class="mb-0">Need to know more? <a href="https://twitter.com/iomeata" target="_blank">Visit my
                    Twitter.</a> or <a href="https://www.linkedin.com/in/omeatai/" target="_blank">view my LinkedIn</a>.
            </p>
        </div>
    </footer>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous">
    </script>

</body>

</html>
```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/92c7b2f9-8bd5-4b19-a1be-4df99bbe6d6e">

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/83029a5f-39fb-474d-8e5f-f9dbd9fef106)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/60bb6b74-5edf-4af6-bf21-f4bb419eb45f)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/b08f30c9-4d92-4bc2-8c36-6ee3a4887014)

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/88573e62-ac0b-445d-b7f2-a088ef498a45">

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/93eda305-2d48-4c6f-b04a-c50ed160e03e)

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/63ef7e7f-96d3-482b-85c2-884f601d06c8)

<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/fd7570c6-d16f-4de1-b85e-286b87b821be">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b3f13f6b-5571-4af2-926b-f308b6d23bbb">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b7e89d03-3817-40c4-9e90-a6a6172c7e42">

# #END</details>

<details>
<summary>10. Adding Static Images to Django </summary>

# Adding Static Images to Django

[https://github.com/omeatai/src-python-flask-django/commit/58911b297ac32d5da5a9921c81ac4acb2cd90bd5](https://github.com/omeatai/src-python-flask-django/commit/58911b297ac32d5da5a9921c81ac4acb2cd90bd5)

## Run Collectstatic (To add all static folders into a single main folder)

```py
python manage.py collectstatic
```

### portfolio.settings:

```py
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

### portfolio.urls:

```py
"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobs.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

### src-python/linkedin/django-personal-portfolio/jobs/templates/jobs/home.html:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en" data-bs-theme="auto">

<head>
    <script src="https://getbootstrap.com/docs/5.3/assets/js/color-modes.js"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Hugo 0.122.0">
    <title>Ifeanyi Omeata</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/5.3/examples/album/">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@docsearch/css@3">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">

    <!-- Favicons -->
    <link rel="apple-touch-icon" href="/docs/5.3/assets/img/favicons/apple-touch-icon.png" sizes="180x180">
    <link rel="icon" href="/docs/5.3/assets/img/favicons/favicon-32x32.png" sizes="32x32" type="image/png">
    <link rel="icon" href="/docs/5.3/assets/img/favicons/favicon-16x16.png" sizes="16x16" type="image/png">
    <link rel="manifest" href="/docs/5.3/assets/img/favicons/manifest.json">
    <link rel="mask-icon" href="/docs/5.3/assets/img/favicons/safari-pinned-tab.svg" color="#712cf9">
    <link rel="icon" href="/docs/5.3/assets/img/favicons/favicon.ico">
    <meta name="theme-color" content="#712cf9">


    <style>
        .bd-placeholder-img {
            font-size: 1.125rem;
            text-anchor: middle;
            -webkit-user-select: none;
            -moz-user-select: none;
            user-select: none;
        }

        @media (min-width: 768px) {
            .bd-placeholder-img-lg {
                font-size: 3.5rem;
            }
        }

        .b-example-divider {
            width: 100%;
            height: 3rem;
            background-color: rgba(0, 0, 0, .1);
            border: solid rgba(0, 0, 0, .15);
            border-width: 1px 0;
            box-shadow: inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15);
        }

        .b-example-vr {
            flex-shrink: 0;
            width: 1.5rem;
            height: 100vh;
        }

        .bi {
            vertical-align: -.125em;
            fill: currentColor;
        }

        .nav-scroller {
            position: relative;
            z-index: 2;
            height: 2.75rem;
            overflow-y: hidden;
        }

        .nav-scroller .nav {
            display: flex;
            flex-wrap: nowrap;
            padding-bottom: 1rem;
            margin-top: -1px;
            overflow-x: auto;
            text-align: center;
            white-space: nowrap;
            -webkit-overflow-scrolling: touch;
        }

        .btn-bd-primary {
            --bd-violet-bg: #712cf9;
            --bd-violet-rgb: 112.520718, 44.062154, 249.437846;

            --bs-btn-font-weight: 600;
            --bs-btn-color: var(--bs-white);
            --bs-btn-bg: var(--bd-violet-bg);
            --bs-btn-border-color: var(--bd-violet-bg);
            --bs-btn-hover-color: var(--bs-white);
            --bs-btn-hover-bg: #6528e0;
            --bs-btn-hover-border-color: #6528e0;
            --bs-btn-focus-shadow-rgb: var(--bd-violet-rgb);
            --bs-btn-active-color: var(--bs-btn-hover-color);
            --bs-btn-active-bg: #5a23c8;
            --bs-btn-active-border-color: #5a23c8;
        }

        .bd-mode-toggle {
            z-index: 1500;
        }

        .bd-mode-toggle .dropdown-menu .active .bi {
            display: block !important;
        }
    </style>


</head>

<body>

    <svg xmlns="http://www.w3.org/2000/svg" class="d-none">
        <symbol id="check2" viewBox="0 0 16 16">
            <path
                d="M13.854 3.646a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L6.5 10.293l6.646-6.647a.5.5 0 0 1 .708 0z" />
        </symbol>
        <symbol id="circle-half" viewBox="0 0 16 16">
            <path d="M8 15A7 7 0 1 0 8 1v14zm0 1A8 8 0 1 1 8 0a8 8 0 0 1 0 16z" />
        </symbol>
        <symbol id="moon-stars-fill" viewBox="0 0 16 16">
            <path
                d="M6 .278a.768.768 0 0 1 .08.858 7.208 7.208 0 0 0-.878 3.46c0 4.021 3.278 7.277 7.318 7.277.527 0 1.04-.055 1.533-.16a.787.787 0 0 1 .81.316.733.733 0 0 1-.031.893A8.349 8.349 0 0 1 8.344 16C3.734 16 0 12.286 0 7.71 0 4.266 2.114 1.312 5.124.06A.752.752 0 0 1 6 .278z" />
            <path
                d="M10.794 3.148a.217.217 0 0 1 .412 0l.387 1.162c.173.518.579.924 1.097 1.097l1.162.387a.217.217 0 0 1 0 .412l-1.162.387a1.734 1.734 0 0 0-1.097 1.097l-.387 1.162a.217.217 0 0 1-.412 0l-.387-1.162A1.734 1.734 0 0 0 9.31 6.593l-1.162-.387a.217.217 0 0 1 0-.412l1.162-.387a1.734 1.734 0 0 0 1.097-1.097l.387-1.162zM13.863.099a.145.145 0 0 1 .274 0l.258.774c.115.346.386.617.732.732l.774.258a.145.145 0 0 1 0 .274l-.774.258a1.156 1.156 0 0 0-.732.732l-.258.774a.145.145 0 0 1-.274 0l-.258-.774a1.156 1.156 0 0 0-.732-.732l-.774-.258a.145.145 0 0 1 0-.274l.774-.258c.346-.115.617-.386.732-.732L13.863.1z" />
        </symbol>
        <symbol id="sun-fill" viewBox="0 0 16 16">
            <path
                d="M8 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0zm0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13zm8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5zM3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8zm10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0zm-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0zm9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707zM4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708z" />
        </symbol>
    </svg>

    <div class="dropdown position-fixed bottom-0 end-0 mb-3 me-3 bd-mode-toggle">
        <button class="btn btn-bd-primary py-2 dropdown-toggle d-flex align-items-center" id="bd-theme" type="button"
            aria-expanded="false" data-bs-toggle="dropdown" aria-label="Toggle theme (auto)">
            <svg class="bi my-1 theme-icon-active" width="1em" height="1em">
                <use href="#circle-half"></use>
            </svg>
            <span class="visually-hidden" id="bd-theme-text">Toggle theme</span>
        </button>
        <ul class="dropdown-menu dropdown-menu-end shadow" aria-labelledby="bd-theme-text">
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="light"
                    aria-pressed="false">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#sun-fill"></use>
                    </svg>
                    Light
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="dark"
                    aria-pressed="false">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#moon-stars-fill"></use>
                    </svg>
                    Dark
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center active" data-bs-theme-value="auto"
                    aria-pressed="true">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#circle-half"></use>
                    </svg>
                    Auto
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
        </ul>
    </div>


    <header data-bs-theme="dark">
        <div class="collapse text-bg-dark" id="navbarHeader">
            <div class="container">
                <div class="row">
                    <div class="col-sm-8 col-md-7 py-4">
                        <h4>About</h4>
                        <p class="text-body-secondary">Hi! I am Ifeanyi, a Software Engineer and Full-Stack
                            Developer based here in the beautiful province of Alberta, Canada. With a track record of
                            over 6 years in the field, I excel in creating resilient, scalable, and user-centric web,
                            mobile and data-driven applications that tackle real-world challenges head-on.</p>
                        <img src="{% static 'picofme.png' %}" width="100" alt="my profile pic" />
                    </div>

                    <div class="col-sm-4 offset-md-1 py-4">
                        <h4>Contact</h4>
                        <ul class="list-unstyled">
                            <li><a href="https://twitter.com/iomeata" target="_blank" class="text-white">Follow on
                                    Twitter</a></li>
                            <li><a href="https://www.linkedin.com/in/omeatai/" target="_blank" class="text-white">Follow
                                    on LinkedIn</a></li>
                            <li><a href="mailto:omeatai@gmail.com?subject=Contact Form on Website&cc="
                                    class="text-white">Email me</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        <div class="navbar navbar-dark bg-dark shadow-sm">
            <div class="container">
                <a href="#" class="navbar-brand d-flex align-items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" stroke="currentColor"
                        stroke-linecap="round" stroke-linejoin="round" stroke-width="2" aria-hidden="true" class="me-2"
                        viewBox="0 0 24 24">
                        <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z" />
                        <circle cx="12" cy="13" r="4" /></svg>
                    <strong>Ifeanyi Omeata</strong>
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarHeader"
                    aria-controls="navbarHeader" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
            </div>
        </div>
    </header>

    <main>

        <section class="py-2 text-center container">
            <div class="row py-lg-5">
                <div class="col-lg-6 col-md-8 mx-auto">
                    <h1 class="fw-light">Ifeanyi Omeata</h1>
                    <p class="lead text-body-secondary">Hi! My name is Ifeanyi Omeata, a Software Engineer and
                        Full-Stack
                        Developer based here in the beautiful province of Alberta, Canada. With a track record of
                        over 6 years in the field, I excel in creating resilient, scalable, and user-centric web,
                        mobile and data-driven applications that tackle real-world challenges head-on.</p>
                    <p>
                        <a href="#all-jobs" class="btn btn-primary my-2">View my Jobs</a>
                        <a href="mailto:omeatai@gmail.com?subject=Contact Form on Website&cc="
                            class="btn btn-secondary my-2">Email me</a>
                    </p>
                    <img src="{% static 'picofme.png' %}" width="300" alt="my profile pic" />
                </div>
            </div>
        </section>

        <div class="album py-2 bg-body-tertiary">
            <div class="container">

                <h1 id="all-jobs" class="text-center pb-2">My Jobs</h1>

                <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">

                    {% for job in jobs %}

                    <div class="col">
                        <div class="card shadow-sm">
                            <img src="{% static job.image %}" alt='{{job.title}}'
                                class="bd-placeholder-img card-img-top p-2 bg-black" width="100%" height="225" />
                            {% comment %} <svg class="bd-placeholder-img card-img-top" width="100%" height="225"
                                xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Thumbnail"
                                preserveAspectRatio="xMidYMid slice" focusable="false">
                                <title>{{ job.title }}</title>
                                <rect width="100%" height="100%" fill="#55595c" /><text x="50%" y="50%" fill="#eceeef"
                                    dy=".3em">{{ job.title }}</text>
                            </svg> {% endcomment %}
                            <div class="card-body">
                                <h4>{{ job.title }}</h4>
                                <p class="card-text">{{ job.summary }}</p>
                                <div class="d-flex justify-content-between align-items-center">
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                                        <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
                                    </div>
                                    <small class="text-body-secondary">{{ job.image }}</small>
                                </div>
                            </div>
                        </div>
                    </div>

                    {% endfor %}
                </div>
            </div>
        </div>
    </main>

    <footer class="text-body-secondary py-5">
        <div class="container">
            <p class="float-end mb-1">
                <a href="#">Back to top</a>
            </p>
            <p class="mb-1">Copyright. Ifeanyi omeata &copy; 2024.</p>
            <p class="mb-0">Need to know more? <a href="https://twitter.com/iomeata" target="_blank">Visit my
                    Twitter.</a> or <a href="https://www.linkedin.com/in/omeatai/" target="_blank">view my LinkedIn</a>.
            </p>
        </div>
    </footer>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous">
    </script>

</body>

</html>
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/a0f520c5-a879-4ba2-979c-7626dafa8666)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/7d0588a4-d71b-4dee-8a36-46766e05b0da)

<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/4a5ba522-ba48-4f40-8260-6b8bfa9ec0db">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e51c9fec-d7e7-454a-b3a4-2c43608946ea">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/185ec6e9-c5f4-4450-b90f-8b96a6de83b6">

# #END</details>

<details>
<summary>11. Using Bootstrap Static Assets </summary>

# Using Bootstrap Static Assets

[https://github.com/omeatai/src-python-flask-django/commit/485bd4e3992354075db72461810cc21900f74677](https://github.com/omeatai/src-python-flask-django/commit/485bd4e3992354075db72461810cc21900f74677)

## Run Collectstatic (To add Bootstrap and Jquery static files into the main Static folder)

```py
python manage.py collectstatic
```

### src-python/linkedin/django-personal-portfolio/jobs/templates/jobs/home.html:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en" data-bs-theme="auto">

<head>
    <script src="https://getbootstrap.com/docs/5.3/assets/js/color-modes.js"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <title>Ifeanyi Omeata</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/5.3/examples/album/">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@docsearch/css@3">
    {% comment %}
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    {% endcomment %}
    <link href="{% static 'css/bootstrap.min.css' %}" rel="stylesheet">
    <meta name="theme-color" content="#712cf9">


    <style>
        .bd-placeholder-img {
            font-size: 1.125rem;
            text-anchor: middle;
            -webkit-user-select: none;
            -moz-user-select: none;
            user-select: none;
        }

        @media (min-width: 768px) {
            .bd-placeholder-img-lg {
                font-size: 3.5rem;
            }
        }

        .b-example-divider {
            width: 100%;
            height: 3rem;
            background-color: rgba(0, 0, 0, .1);
            border: solid rgba(0, 0, 0, .15);
            border-width: 1px 0;
            box-shadow: inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15);
        }

        .b-example-vr {
            flex-shrink: 0;
            width: 1.5rem;
            height: 100vh;
        }

        .bi {
            vertical-align: -.125em;
            fill: currentColor;
        }

        .nav-scroller {
            position: relative;
            z-index: 2;
            height: 2.75rem;
            overflow-y: hidden;
        }

        .nav-scroller .nav {
            display: flex;
            flex-wrap: nowrap;
            padding-bottom: 1rem;
            margin-top: -1px;
            overflow-x: auto;
            text-align: center;
            white-space: nowrap;
            -webkit-overflow-scrolling: touch;
        }

        .btn-bd-primary {
            --bd-violet-bg: #712cf9;
            --bd-violet-rgb: 112.520718, 44.062154, 249.437846;

            --bs-btn-font-weight: 600;
            --bs-btn-color: var(--bs-white);
            --bs-btn-bg: var(--bd-violet-bg);
            --bs-btn-border-color: var(--bd-violet-bg);
            --bs-btn-hover-color: var(--bs-white);
            --bs-btn-hover-bg: #6528e0;
            --bs-btn-hover-border-color: #6528e0;
            --bs-btn-focus-shadow-rgb: var(--bd-violet-rgb);
            --bs-btn-active-color: var(--bs-btn-hover-color);
            --bs-btn-active-bg: #5a23c8;
            --bs-btn-active-border-color: #5a23c8;
        }

        .bd-mode-toggle {
            z-index: 1500;
        }

        .bd-mode-toggle .dropdown-menu .active .bi {
            display: block !important;
        }
    </style>


</head>

<body>

    <svg xmlns="http://www.w3.org/2000/svg" class="d-none">
        <symbol id="check2" viewBox="0 0 16 16">
            <path
                d="M13.854 3.646a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L6.5 10.293l6.646-6.647a.5.5 0 0 1 .708 0z" />
        </symbol>
        <symbol id="circle-half" viewBox="0 0 16 16">
            <path d="M8 15A7 7 0 1 0 8 1v14zm0 1A8 8 0 1 1 8 0a8 8 0 0 1 0 16z" />
        </symbol>
        <symbol id="moon-stars-fill" viewBox="0 0 16 16">
            <path
                d="M6 .278a.768.768 0 0 1 .08.858 7.208 7.208 0 0 0-.878 3.46c0 4.021 3.278 7.277 7.318 7.277.527 0 1.04-.055 1.533-.16a.787.787 0 0 1 .81.316.733.733 0 0 1-.031.893A8.349 8.349 0 0 1 8.344 16C3.734 16 0 12.286 0 7.71 0 4.266 2.114 1.312 5.124.06A.752.752 0 0 1 6 .278z" />
            <path
                d="M10.794 3.148a.217.217 0 0 1 .412 0l.387 1.162c.173.518.579.924 1.097 1.097l1.162.387a.217.217 0 0 1 0 .412l-1.162.387a1.734 1.734 0 0 0-1.097 1.097l-.387 1.162a.217.217 0 0 1-.412 0l-.387-1.162A1.734 1.734 0 0 0 9.31 6.593l-1.162-.387a.217.217 0 0 1 0-.412l1.162-.387a1.734 1.734 0 0 0 1.097-1.097l.387-1.162zM13.863.099a.145.145 0 0 1 .274 0l.258.774c.115.346.386.617.732.732l.774.258a.145.145 0 0 1 0 .274l-.774.258a1.156 1.156 0 0 0-.732.732l-.258.774a.145.145 0 0 1-.274 0l-.258-.774a1.156 1.156 0 0 0-.732-.732l-.774-.258a.145.145 0 0 1 0-.274l.774-.258c.346-.115.617-.386.732-.732L13.863.1z" />
        </symbol>
        <symbol id="sun-fill" viewBox="0 0 16 16">
            <path
                d="M8 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0zm0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13zm8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5zM3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8zm10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0zm-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0zm9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707zM4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708z" />
        </symbol>
    </svg>

    <div class="dropdown position-fixed bottom-0 end-0 mb-3 me-3 bd-mode-toggle">
        <button class="btn btn-bd-primary py-2 dropdown-toggle d-flex align-items-center" id="bd-theme" type="button"
            aria-expanded="false" data-bs-toggle="dropdown" aria-label="Toggle theme (auto)">
            <svg class="bi my-1 theme-icon-active" width="1em" height="1em">
                <use href="#circle-half"></use>
            </svg>
            <span class="visually-hidden" id="bd-theme-text">Toggle theme</span>
        </button>
        <ul class="dropdown-menu dropdown-menu-end shadow" aria-labelledby="bd-theme-text">
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="light"
                    aria-pressed="false">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#sun-fill"></use>
                    </svg>
                    Light
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="dark"
                    aria-pressed="false">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#moon-stars-fill"></use>
                    </svg>
                    Dark
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center active" data-bs-theme-value="auto"
                    aria-pressed="true">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#circle-half"></use>
                    </svg>
                    Auto
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
        </ul>
    </div>


    <header data-bs-theme="dark">
        <div class="collapse text-bg-dark" id="navbarHeader">
            <div class="container">
                <div class="row">
                    <div class="col-sm-8 col-md-7 py-4">
                        <h4>About</h4>
                        <p class="text-body-secondary">Hi! I am Ifeanyi, a Software Engineer and Full-Stack
                            Developer based here in the beautiful province of Alberta, Canada. With a track record of
                            over 6 years in the field, I excel in creating resilient, scalable, and user-centric web,
                            mobile and data-driven applications that tackle real-world challenges head-on.</p>
                        <img src="{% static 'picofme.png' %}" width="100" alt="my profile pic" />
                    </div>

                    <div class="col-sm-4 offset-md-1 py-4">
                        <h4>Contact</h4>
                        <ul class="list-unstyled">
                            <li><a href="https://twitter.com/iomeata" target="_blank" class="text-white">Follow on
                                    Twitter</a></li>
                            <li><a href="https://www.linkedin.com/in/omeatai/" target="_blank" class="text-white">Follow
                                    on LinkedIn</a></li>
                            <li><a href="mailto:omeatai@gmail.com?subject=Contact Form on Website&cc="
                                    class="text-white">Email me</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        <div class="navbar navbar-dark bg-dark shadow-sm">
            <div class="container">
                <a href="#" class="navbar-brand d-flex align-items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" stroke="currentColor"
                        stroke-linecap="round" stroke-linejoin="round" stroke-width="2" aria-hidden="true" class="me-2"
                        viewBox="0 0 24 24">
                        <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z" />
                        <circle cx="12" cy="13" r="4" /></svg>
                    <strong>Ifeanyi Omeata</strong>
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarHeader"
                    aria-controls="navbarHeader" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
            </div>
        </div>
    </header>

    <main>

        <section class="py-2 text-center container">
            <div class="row py-lg-5">
                <div class="col-lg-6 col-md-8 mx-auto">
                    <h1 class="fw-light">Ifeanyi Omeata</h1>
                    <p class="lead text-body-secondary">Hi! My name is Ifeanyi Omeata, a Software Engineer and
                        Full-Stack
                        Developer based here in the beautiful province of Alberta, Canada. With a track record of
                        over 6 years in the field, I excel in creating resilient, scalable, and user-centric web,
                        mobile and data-driven applications that tackle real-world challenges head-on.</p>
                    <p>
                        <a href="#all-jobs" class="btn btn-primary my-2">View my Jobs</a>
                        <a href="mailto:omeatai@gmail.com?subject=Contact Form on Website&cc="
                            class="btn btn-secondary my-2">Email me</a>
                    </p>
                    <img src="{% static 'picofme.png' %}" width="300" alt="my profile pic" />
                </div>
            </div>
        </section>

        <div class="album py-2 bg-body-tertiary">
            <div class="container">

                <h1 id="all-jobs" class="text-center pb-2">My Jobs</h1>

                <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">

                    {% for job in jobs %}

                    <div class="col">
                        <div class="card shadow-sm">
                            <img src="{% static job.image %}" alt='{{job.title}}'
                                class="bd-placeholder-img card-img-top p-2 bg-black" width="100%" height="225" />
                            {% comment %} <svg class="bd-placeholder-img card-img-top" width="100%" height="225"
                                xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Thumbnail"
                                preserveAspectRatio="xMidYMid slice" focusable="false">
                                <title>{{ job.title }}</title>
                                <rect width="100%" height="100%" fill="#55595c" /><text x="50%" y="50%" fill="#eceeef"
                                    dy=".3em">{{ job.title }}</text>
                            </svg> {% endcomment %}
                            <div class="card-body">
                                <h4>{{ job.title }}</h4>
                                <p class="card-text">{{ job.summary }}</p>
                                <div class="d-flex justify-content-between align-items-center">
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                                        <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
                                    </div>
                                    <small class="text-body-secondary">{{ job.image }}</small>
                                </div>
                            </div>
                        </div>
                    </div>

                    {% endfor %}
                </div>
            </div>
        </div>
    </main>

    <footer class="text-body-secondary py-5">
        <div class="container">
            <p class="float-end mb-1">
                <a href="#">Back to top</a>
            </p>
            <p class="mb-1">Copyright. Ifeanyi omeata &copy; 2024.</p>
            <p class="mb-0">Need to know more? <a href="https://twitter.com/iomeata" target="_blank">Visit my
                    Twitter.</a> or <a href="https://www.linkedin.com/in/omeatai/" target="_blank">view my LinkedIn</a>.
            </p>
        </div>
    </footer>
    <script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>
    {% comment %} <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous">
    </script> {% endcomment %}

</body>

</html>
```

#### Bootstrap Assets
[https://getbootstrap.com/docs/5.3/getting-started/download/](https://getbootstrap.com/docs/5.3/getting-started/download/)

#### JQuery Assets
[https://jquery.com/download/](https://jquery.com/download/)

#### Popper Assets
[https://github.com/vusion/popper.js/](https://github.com/vusion/popper.js/)

#### Popper.js now Floating-ui CDN
[https://github.com/floating-ui/floating-ui#installation](https://github.com/floating-ui/floating-ui#installation)
[https://floating-ui.com/docs/getting-started#cdn](https://floating-ui.com/docs/getting-started#cdn)

```html
<script src="https://cdn.jsdelivr.net/npm/@floating-ui/core@1.6.0"></script>
<script src="https://cdn.jsdelivr.net/npm/@floating-ui/dom@1.6.3"></script>
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/86e47226-c7c0-474f-bfe5-dbf0500cfb4b)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/65b9c8d5-aeb7-4037-be7d-62e239d150e0)

<img width="1450" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/da652915-3973-472e-aecb-440d58559528">

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/6ad250cc-6c94-4330-9cfc-5379d5cc4221)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/acfe694b-16bb-45f8-81c6-66e3f8afc627)

<img width="932" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/8f849af8-f756-429b-8f8b-695887ffe3a7">

# #END</details>

<details>
<summary>12. Setup Media Folder for Media Files </summary>

# Setup Media Folder for Media Files

[https://github.com/omeatai/src-python-flask-django/commit/77db2bc76db3f37538be9094a42d1e1f546e51df](https://github.com/omeatai/src-python-flask-django/commit/77db2bc76db3f37538be9094a42d1e1f546e51df)

### portfolio.settings:

```py
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

### portfolio.urls:

```py
"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobs.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

### src-python/linkedin/django-personal-portfolio/jobs/templates/jobs/home.html:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en" data-bs-theme="auto">

<head>
    <script src="https://getbootstrap.com/docs/5.3/assets/js/color-modes.js"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <title>Ifeanyi Omeata</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/5.3/examples/album/">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@docsearch/css@3">
    {% comment %}
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    {% endcomment %}
    <link href="{% static 'css/bootstrap.min.css' %}" rel="stylesheet">
    <meta name="theme-color" content="#712cf9">


    <style>
        .bd-placeholder-img {
            font-size: 1.125rem;
            text-anchor: middle;
            -webkit-user-select: none;
            -moz-user-select: none;
            user-select: none;
        }

        @media (min-width: 768px) {
            .bd-placeholder-img-lg {
                font-size: 3.5rem;
            }
        }

        .b-example-divider {
            width: 100%;
            height: 3rem;
            background-color: rgba(0, 0, 0, .1);
            border: solid rgba(0, 0, 0, .15);
            border-width: 1px 0;
            box-shadow: inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15);
        }

        .b-example-vr {
            flex-shrink: 0;
            width: 1.5rem;
            height: 100vh;
        }

        .bi {
            vertical-align: -.125em;
            fill: currentColor;
        }

        .nav-scroller {
            position: relative;
            z-index: 2;
            height: 2.75rem;
            overflow-y: hidden;
        }

        .nav-scroller .nav {
            display: flex;
            flex-wrap: nowrap;
            padding-bottom: 1rem;
            margin-top: -1px;
            overflow-x: auto;
            text-align: center;
            white-space: nowrap;
            -webkit-overflow-scrolling: touch;
        }

        .btn-bd-primary {
            --bd-violet-bg: #712cf9;
            --bd-violet-rgb: 112.520718, 44.062154, 249.437846;

            --bs-btn-font-weight: 600;
            --bs-btn-color: var(--bs-white);
            --bs-btn-bg: var(--bd-violet-bg);
            --bs-btn-border-color: var(--bd-violet-bg);
            --bs-btn-hover-color: var(--bs-white);
            --bs-btn-hover-bg: #6528e0;
            --bs-btn-hover-border-color: #6528e0;
            --bs-btn-focus-shadow-rgb: var(--bd-violet-rgb);
            --bs-btn-active-color: var(--bs-btn-hover-color);
            --bs-btn-active-bg: #5a23c8;
            --bs-btn-active-border-color: #5a23c8;
        }

        .bd-mode-toggle {
            z-index: 1500;
        }

        .bd-mode-toggle .dropdown-menu .active .bi {
            display: block !important;
        }
    </style>


</head>

<body>

    <svg xmlns="http://www.w3.org/2000/svg" class="d-none">
        <symbol id="check2" viewBox="0 0 16 16">
            <path
                d="M13.854 3.646a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L6.5 10.293l6.646-6.647a.5.5 0 0 1 .708 0z" />
        </symbol>
        <symbol id="circle-half" viewBox="0 0 16 16">
            <path d="M8 15A7 7 0 1 0 8 1v14zm0 1A8 8 0 1 1 8 0a8 8 0 0 1 0 16z" />
        </symbol>
        <symbol id="moon-stars-fill" viewBox="0 0 16 16">
            <path
                d="M6 .278a.768.768 0 0 1 .08.858 7.208 7.208 0 0 0-.878 3.46c0 4.021 3.278 7.277 7.318 7.277.527 0 1.04-.055 1.533-.16a.787.787 0 0 1 .81.316.733.733 0 0 1-.031.893A8.349 8.349 0 0 1 8.344 16C3.734 16 0 12.286 0 7.71 0 4.266 2.114 1.312 5.124.06A.752.752 0 0 1 6 .278z" />
            <path
                d="M10.794 3.148a.217.217 0 0 1 .412 0l.387 1.162c.173.518.579.924 1.097 1.097l1.162.387a.217.217 0 0 1 0 .412l-1.162.387a1.734 1.734 0 0 0-1.097 1.097l-.387 1.162a.217.217 0 0 1-.412 0l-.387-1.162A1.734 1.734 0 0 0 9.31 6.593l-1.162-.387a.217.217 0 0 1 0-.412l1.162-.387a1.734 1.734 0 0 0 1.097-1.097l.387-1.162zM13.863.099a.145.145 0 0 1 .274 0l.258.774c.115.346.386.617.732.732l.774.258a.145.145 0 0 1 0 .274l-.774.258a1.156 1.156 0 0 0-.732.732l-.258.774a.145.145 0 0 1-.274 0l-.258-.774a1.156 1.156 0 0 0-.732-.732l-.774-.258a.145.145 0 0 1 0-.274l.774-.258c.346-.115.617-.386.732-.732L13.863.1z" />
        </symbol>
        <symbol id="sun-fill" viewBox="0 0 16 16">
            <path
                d="M8 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0zm0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13zm8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5zM3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8zm10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0zm-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0zm9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707zM4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708z" />
        </symbol>
    </svg>

    <div class="dropdown position-fixed bottom-0 end-0 mb-3 me-3 bd-mode-toggle">
        <button class="btn btn-bd-primary py-2 dropdown-toggle d-flex align-items-center" id="bd-theme" type="button"
            aria-expanded="false" data-bs-toggle="dropdown" aria-label="Toggle theme (auto)">
            <svg class="bi my-1 theme-icon-active" width="1em" height="1em">
                <use href="#circle-half"></use>
            </svg>
            <span class="visually-hidden" id="bd-theme-text">Toggle theme</span>
        </button>
        <ul class="dropdown-menu dropdown-menu-end shadow" aria-labelledby="bd-theme-text">
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="light"
                    aria-pressed="false">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#sun-fill"></use>
                    </svg>
                    Light
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="dark"
                    aria-pressed="false">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#moon-stars-fill"></use>
                    </svg>
                    Dark
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center active" data-bs-theme-value="auto"
                    aria-pressed="true">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#circle-half"></use>
                    </svg>
                    Auto
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
        </ul>
    </div>


    <header data-bs-theme="dark">
        <div class="collapse text-bg-dark" id="navbarHeader">
            <div class="container">
                <div class="row">
                    <div class="col-sm-8 col-md-7 py-4">
                        <h4>About</h4>
                        <p class="text-body-secondary">Hi! I am Ifeanyi, a Software Engineer and Full-Stack
                            Developer based here in the beautiful province of Alberta, Canada. With a track record of
                            over 6 years in the field, I excel in creating resilient, scalable, and user-centric web,
                            mobile and data-driven applications that tackle real-world challenges head-on.</p>
                        <img src="{% static 'picofme.png' %}" width="100" alt="my profile pic" />
                    </div>

                    <div class="col-sm-4 offset-md-1 py-4">
                        <h4>Contact</h4>
                        <ul class="list-unstyled">
                            <li><a href="https://twitter.com/iomeata" target="_blank" class="text-white">Follow on
                                    Twitter</a></li>
                            <li><a href="https://www.linkedin.com/in/omeatai/" target="_blank" class="text-white">Follow
                                    on LinkedIn</a></li>
                            <li><a href="mailto:omeatai@gmail.com?subject=Contact Form on Website&cc="
                                    class="text-white">Email me</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        <div class="navbar navbar-dark bg-dark shadow-sm">
            <div class="container">
                <a href="#" class="navbar-brand d-flex align-items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" stroke="currentColor"
                        stroke-linecap="round" stroke-linejoin="round" stroke-width="2" aria-hidden="true" class="me-2"
                        viewBox="0 0 24 24">
                        <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z" />
                        <circle cx="12" cy="13" r="4" /></svg>
                    <strong>Ifeanyi Omeata</strong>
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarHeader"
                    aria-controls="navbarHeader" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
            </div>
        </div>
    </header>

    <main>

        <section class="py-2 text-center container">
            <div class="row py-lg-5">
                <div class="col-lg-6 col-md-8 mx-auto">
                    <h1 class="fw-light">Ifeanyi Omeata</h1>
                    <p class="lead text-body-secondary">Hi! My name is Ifeanyi Omeata, a Software Engineer and
                        Full-Stack
                        Developer based here in the beautiful province of Alberta, Canada. With a track record of
                        over 6 years in the field, I excel in creating resilient, scalable, and user-centric web,
                        mobile and data-driven applications that tackle real-world challenges head-on.</p>
                    <p>
                        <a href="#all-jobs" class="btn btn-primary my-2">View my Jobs</a>
                        <a href="mailto:omeatai@gmail.com?subject=Contact Form on Website&cc="
                            class="btn btn-secondary my-2">Email me</a>
                    </p>
                    <img src="{% static 'picofme.png' %}" width="300" alt="my profile pic" />
                </div>
            </div>
        </section>

        <div class="album py-2 bg-body-tertiary">
            <div class="container">

                <h1 id="all-jobs" class="text-center pb-2">My Jobs</h1>

                <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">

                    {% for job in jobs %}

                    <div class="col">
                        <div class="card shadow-sm">
                            {% comment %} <img src="{% static job.image %}" alt='{{job.title}}'
                                class="bd-placeholder-img card-img-top p-2 bg-black" width="100%" height="225" />
                            {% endcomment %}
                            <img src="{{ job.image.url }}" alt='{{job.title}}'
                                class="bd-placeholder-img card-img-top p-2 bg-black" width="100%" height="225" />
                            {% comment %} <svg class="bd-placeholder-img card-img-top" width="100%" height="225"
                                xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Thumbnail"
                                preserveAspectRatio="xMidYMid slice" focusable="false">
                                <title>{{ job.title }}</title>
                                <rect width="100%" height="100%" fill="#55595c" /><text x="50%" y="50%" fill="#eceeef"
                                    dy=".3em">{{ job.title }}</text>
                            </svg> {% endcomment %}
                            <div class="card-body">
                                <h4>{{ job.title }}</h4>
                                <p class="card-text">{{ job.summary }}</p>
                                <div class="d-flex justify-content-between align-items-center">
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                                        <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
                                    </div>
                                    <small class="text-body-secondary">{{ job.image }}</small>
                                    <small class="text-body-secondary">{{ job.image.url }}</small>
                                </div>
                            </div>
                        </div>
                    </div>

                    {% endfor %}
                </div>
            </div>
        </div>
    </main>

    <footer class="text-body-secondary py-5">
        <div class="container">
            <p class="float-end mb-1">
                <a href="#">Back to top</a>
            </p>
            <p class="mb-1">Copyright. Ifeanyi omeata &copy; 2024.</p>
            <p class="mb-0">Need to know more? <a href="https://twitter.com/iomeata" target="_blank">Visit my
                    Twitter.</a> or <a href="https://www.linkedin.com/in/omeatai/" target="_blank">view my LinkedIn</a>.
            </p>
        </div>
    </footer>
    <script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>
    {% comment %} <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous">
    </script> {% endcomment %}

</body>

</html>
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/bf2687ce-ab04-47bc-b134-a873e0fd778c)

<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1c1d5dce-9926-43b7-96df-5ace887e52ed">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/3f463b18-9ec5-4f66-b7e4-1f444e997db9">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/882fa493-acdc-4f5c-9f99-f8539f5925e1">

# #END</details>

<details>
<summary>13. Setup Model Default String Name </summary>

# Setup Model Default String Name

[https://github.com/omeatai/src-python-flask-django/commit/77db2bc76db3f37538be9094a42d1e1f546e51df](https://github.com/omeatai/src-python-flask-django/commit/77db2bc76db3f37538be9094a42d1e1f546e51df)

### jobs.models:

```py
from django.db import models
# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # date = models.DateField()
    # description = models.TextField()
    # url = models.URLField()
    # company = models.CharField(max_length=100)
    # position = models.CharField(max_length=100)
    # location = models.CharField(max_length=100)

    def __str__(self):
        return self.title
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/cc8f0e4b-5057-423b-be7a-1187673cd69d)

<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/6f8bf4ef-3568-4ff6-b7fa-ca36c850af47">

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/b198f65d-c54e-430a-a15d-797614f25f1e)

# #END</details>

<details>
<summary>14. Setup URL, View and Template for Details Page </summary>

# Setup URL, View and Template for Details Page

[https://github.com/omeatai/src-python-flask-django/commit/c74f54e88a57b4951d882e75039720ef802a5794](https://github.com/omeatai/src-python-flask-django/commit/c74f54e88a57b4951d882e75039720ef802a5794)

### jobs.urls:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/<int:job_id>', views.job_detail, name='job-detail'),
]

```

### jobs.views:

```py
from django.shortcuts import render, get_object_or_404
from .models import Job
# Create your views here.


def home(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/home.html', {'jobs': jobs})


def job_detail(request, job_id):
    # job = Job.objects.get(id=job_id)
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})

```

### src-python/linkedin/django-personal-portfolio/jobs/templates/jobs/job_detail.html:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en" data-bs-theme="auto">

<head>
    <script src="https://getbootstrap.com/docs/5.3/assets/js/color-modes.js"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <title>Ifeanyi Omeata</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/5.3/examples/album/">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@docsearch/css@3">
    <link href="{% static 'css/bootstrap.min.css' %}" rel="stylesheet">
    <meta name="theme-color" content="#712cf9">


    <style>
        .bd-placeholder-img {
            font-size: 1.125rem;
            text-anchor: middle;
            -webkit-user-select: none;
            -moz-user-select: none;
            user-select: none;
        }

        @media (min-width: 768px) {
            .bd-placeholder-img-lg {
                font-size: 3.5rem;
            }
        }

        .b-example-divider {
            width: 100%;
            height: 3rem;
            background-color: rgba(0, 0, 0, .1);
            border: solid rgba(0, 0, 0, .15);
            border-width: 1px 0;
            box-shadow: inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15);
        }

        .b-example-vr {
            flex-shrink: 0;
            width: 1.5rem;
            height: 100vh;
        }

        .bi {
            vertical-align: -.125em;
            fill: currentColor;
        }

        .nav-scroller {
            position: relative;
            z-index: 2;
            height: 2.75rem;
            overflow-y: hidden;
        }

        .nav-scroller .nav {
            display: flex;
            flex-wrap: nowrap;
            padding-bottom: 1rem;
            margin-top: -1px;
            overflow-x: auto;
            text-align: center;
            white-space: nowrap;
            -webkit-overflow-scrolling: touch;
        }

        .btn-bd-primary {
            --bd-violet-bg: #712cf9;
            --bd-violet-rgb: 112.520718, 44.062154, 249.437846;

            --bs-btn-font-weight: 600;
            --bs-btn-color: var(--bs-white);
            --bs-btn-bg: var(--bd-violet-bg);
            --bs-btn-border-color: var(--bd-violet-bg);
            --bs-btn-hover-color: var(--bs-white);
            --bs-btn-hover-bg: #6528e0;
            --bs-btn-hover-border-color: #6528e0;
            --bs-btn-focus-shadow-rgb: var(--bd-violet-rgb);
            --bs-btn-active-color: var(--bs-btn-hover-color);
            --bs-btn-active-bg: #5a23c8;
            --bs-btn-active-border-color: #5a23c8;
        }

        .bd-mode-toggle {
            z-index: 1500;
        }

        .bd-mode-toggle .dropdown-menu .active .bi {
            display: block !important;
        }
    </style>


</head>

<body>

    <svg xmlns="http://www.w3.org/2000/svg" class="d-none">
        <symbol id="check2" viewBox="0 0 16 16">
            <path
                d="M13.854 3.646a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L6.5 10.293l6.646-6.647a.5.5 0 0 1 .708 0z" />
        </symbol>
        <symbol id="circle-half" viewBox="0 0 16 16">
            <path d="M8 15A7 7 0 1 0 8 1v14zm0 1A8 8 0 1 1 8 0a8 8 0 0 1 0 16z" />
        </symbol>
        <symbol id="moon-stars-fill" viewBox="0 0 16 16">
            <path
                d="M6 .278a.768.768 0 0 1 .08.858 7.208 7.208 0 0 0-.878 3.46c0 4.021 3.278 7.277 7.318 7.277.527 0 1.04-.055 1.533-.16a.787.787 0 0 1 .81.316.733.733 0 0 1-.031.893A8.349 8.349 0 0 1 8.344 16C3.734 16 0 12.286 0 7.71 0 4.266 2.114 1.312 5.124.06A.752.752 0 0 1 6 .278z" />
            <path
                d="M10.794 3.148a.217.217 0 0 1 .412 0l.387 1.162c.173.518.579.924 1.097 1.097l1.162.387a.217.217 0 0 1 0 .412l-1.162.387a1.734 1.734 0 0 0-1.097 1.097l-.387 1.162a.217.217 0 0 1-.412 0l-.387-1.162A1.734 1.734 0 0 0 9.31 6.593l-1.162-.387a.217.217 0 0 1 0-.412l1.162-.387a1.734 1.734 0 0 0 1.097-1.097l.387-1.162zM13.863.099a.145.145 0 0 1 .274 0l.258.774c.115.346.386.617.732.732l.774.258a.145.145 0 0 1 0 .274l-.774.258a1.156 1.156 0 0 0-.732.732l-.258.774a.145.145 0 0 1-.274 0l-.258-.774a1.156 1.156 0 0 0-.732-.732l-.774-.258a.145.145 0 0 1 0-.274l.774-.258c.346-.115.617-.386.732-.732L13.863.1z" />
        </symbol>
        <symbol id="sun-fill" viewBox="0 0 16 16">
            <path
                d="M8 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0zm0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13zm8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5zM3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8zm10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0zm-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0zm9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707zM4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708z" />
        </symbol>
    </svg>

    <div class="dropdown position-fixed bottom-0 end-0 mb-3 me-3 bd-mode-toggle">
        <button class="btn btn-bd-primary py-2 dropdown-toggle d-flex align-items-center" id="bd-theme" type="button"
            aria-expanded="false" data-bs-toggle="dropdown" aria-label="Toggle theme (auto)">
            <svg class="bi my-1 theme-icon-active" width="1em" height="1em">
                <use href="#circle-half"></use>
            </svg>
            <span class="visually-hidden" id="bd-theme-text">Toggle theme</span>
        </button>
        <ul class="dropdown-menu dropdown-menu-end shadow" aria-labelledby="bd-theme-text">
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="light"
                    aria-pressed="false">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#sun-fill"></use>
                    </svg>
                    Light
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="dark"
                    aria-pressed="false">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#moon-stars-fill"></use>
                    </svg>
                    Dark
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center active" data-bs-theme-value="auto"
                    aria-pressed="true">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#circle-half"></use>
                    </svg>
                    Auto
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
        </ul>
    </div>


    <header data-bs-theme="dark">
        <div class="collapse text-bg-dark" id="navbarHeader">
            <div class="container">
                <div class="row">
                    <div class="col-sm-8 col-md-7 py-4">
                        <h4>About</h4>
                        <p class="text-body-secondary">Hi! I am Ifeanyi, a Software Engineer and Full-Stack
                            Developer based here in the beautiful province of Alberta, Canada. With a track record of
                            over 6 years in the field, I excel in creating resilient, scalable, and user-centric web,
                            mobile and data-driven applications that tackle real-world challenges head-on.</p>
                        <img src="{% static 'picofme.png' %}" width="100" alt="my profile pic" />
                    </div>

                    <div class="col-sm-4 offset-md-1 py-4">
                        <h4>Contact</h4>
                        <ul class="list-unstyled">
                            <li><a href="https://twitter.com/iomeata" target="_blank" class="text-white">Follow on
                                    Twitter</a></li>
                            <li><a href="https://www.linkedin.com/in/omeatai/" target="_blank" class="text-white">Follow
                                    on LinkedIn</a></li>
                            <li><a href="mailto:omeatai@gmail.com?subject=Contact Form on Website&cc="
                                    class="text-white">Email me</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        <div class="navbar navbar-dark bg-dark shadow-sm">
            <div class="container">
                <a href="#" class="navbar-brand d-flex align-items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" stroke="currentColor"
                        stroke-linecap="round" stroke-linejoin="round" stroke-width="2" aria-hidden="true" class="me-2"
                        viewBox="0 0 24 24">
                        <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z" />
                        <circle cx="12" cy="13" r="4" /></svg>
                    <strong>Ifeanyi Omeata</strong>
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarHeader"
                    aria-controls="navbarHeader" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
            </div>
        </div>
    </header>

    <main>

        <section class="py-2 text-center container">
            <div class="row py-lg-5">
                <div class="col-lg-6 col-md-8 mx-auto">
                    <h1 class="fw-light">{{job.title}}</h1>
                    <p class="lead text-body-secondary">{{job.summary}}</p>
                    <p>
                        <a href="#" class="btn btn-primary my-2">Github</a>
                        <a href="#" class="btn btn-secondary my-2">View Demo</a>
                        <a href="{% url 'home' %}" class="btn btn-danger my-2">Back</a>
                    </p>
                    <img src="{{ job.image.url }}" alt='{{job.title}}' width="600" />
                </div>
            </div>
        </section>

    </main>

    <script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>

</body>

</html>
```

### src-python/linkedin/django-personal-portfolio/jobs/templates/jobs/home.html:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en" data-bs-theme="auto">

<head>
    <script src="https://getbootstrap.com/docs/5.3/assets/js/color-modes.js"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <title>Ifeanyi Omeata</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/5.3/examples/album/">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@docsearch/css@3">
    {% comment %}
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    {% endcomment %}
    <link href="{% static 'css/bootstrap.min.css' %}" rel="stylesheet">
    <meta name="theme-color" content="#712cf9">


    <style>
        .bd-placeholder-img {
            font-size: 1.125rem;
            text-anchor: middle;
            -webkit-user-select: none;
            -moz-user-select: none;
            user-select: none;
        }

        @media (min-width: 768px) {
            .bd-placeholder-img-lg {
                font-size: 3.5rem;
            }
        }

        .b-example-divider {
            width: 100%;
            height: 3rem;
            background-color: rgba(0, 0, 0, .1);
            border: solid rgba(0, 0, 0, .15);
            border-width: 1px 0;
            box-shadow: inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15);
        }

        .b-example-vr {
            flex-shrink: 0;
            width: 1.5rem;
            height: 100vh;
        }

        .bi {
            vertical-align: -.125em;
            fill: currentColor;
        }

        .nav-scroller {
            position: relative;
            z-index: 2;
            height: 2.75rem;
            overflow-y: hidden;
        }

        .nav-scroller .nav {
            display: flex;
            flex-wrap: nowrap;
            padding-bottom: 1rem;
            margin-top: -1px;
            overflow-x: auto;
            text-align: center;
            white-space: nowrap;
            -webkit-overflow-scrolling: touch;
        }

        .btn-bd-primary {
            --bd-violet-bg: #712cf9;
            --bd-violet-rgb: 112.520718, 44.062154, 249.437846;

            --bs-btn-font-weight: 600;
            --bs-btn-color: var(--bs-white);
            --bs-btn-bg: var(--bd-violet-bg);
            --bs-btn-border-color: var(--bd-violet-bg);
            --bs-btn-hover-color: var(--bs-white);
            --bs-btn-hover-bg: #6528e0;
            --bs-btn-hover-border-color: #6528e0;
            --bs-btn-focus-shadow-rgb: var(--bd-violet-rgb);
            --bs-btn-active-color: var(--bs-btn-hover-color);
            --bs-btn-active-bg: #5a23c8;
            --bs-btn-active-border-color: #5a23c8;
        }

        .bd-mode-toggle {
            z-index: 1500;
        }

        .bd-mode-toggle .dropdown-menu .active .bi {
            display: block !important;
        }
    </style>


</head>

<body>

    <svg xmlns="http://www.w3.org/2000/svg" class="d-none">
        <symbol id="check2" viewBox="0 0 16 16">
            <path
                d="M13.854 3.646a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L6.5 10.293l6.646-6.647a.5.5 0 0 1 .708 0z" />
        </symbol>
        <symbol id="circle-half" viewBox="0 0 16 16">
            <path d="M8 15A7 7 0 1 0 8 1v14zm0 1A8 8 0 1 1 8 0a8 8 0 0 1 0 16z" />
        </symbol>
        <symbol id="moon-stars-fill" viewBox="0 0 16 16">
            <path
                d="M6 .278a.768.768 0 0 1 .08.858 7.208 7.208 0 0 0-.878 3.46c0 4.021 3.278 7.277 7.318 7.277.527 0 1.04-.055 1.533-.16a.787.787 0 0 1 .81.316.733.733 0 0 1-.031.893A8.349 8.349 0 0 1 8.344 16C3.734 16 0 12.286 0 7.71 0 4.266 2.114 1.312 5.124.06A.752.752 0 0 1 6 .278z" />
            <path
                d="M10.794 3.148a.217.217 0 0 1 .412 0l.387 1.162c.173.518.579.924 1.097 1.097l1.162.387a.217.217 0 0 1 0 .412l-1.162.387a1.734 1.734 0 0 0-1.097 1.097l-.387 1.162a.217.217 0 0 1-.412 0l-.387-1.162A1.734 1.734 0 0 0 9.31 6.593l-1.162-.387a.217.217 0 0 1 0-.412l1.162-.387a1.734 1.734 0 0 0 1.097-1.097l.387-1.162zM13.863.099a.145.145 0 0 1 .274 0l.258.774c.115.346.386.617.732.732l.774.258a.145.145 0 0 1 0 .274l-.774.258a1.156 1.156 0 0 0-.732.732l-.258.774a.145.145 0 0 1-.274 0l-.258-.774a1.156 1.156 0 0 0-.732-.732l-.774-.258a.145.145 0 0 1 0-.274l.774-.258c.346-.115.617-.386.732-.732L13.863.1z" />
        </symbol>
        <symbol id="sun-fill" viewBox="0 0 16 16">
            <path
                d="M8 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0zm0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13zm8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5zM3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8zm10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0zm-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0zm9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707zM4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708z" />
        </symbol>
    </svg>

    <div class="dropdown position-fixed bottom-0 end-0 mb-3 me-3 bd-mode-toggle">
        <button class="btn btn-bd-primary py-2 dropdown-toggle d-flex align-items-center" id="bd-theme" type="button"
            aria-expanded="false" data-bs-toggle="dropdown" aria-label="Toggle theme (auto)">
            <svg class="bi my-1 theme-icon-active" width="1em" height="1em">
                <use href="#circle-half"></use>
            </svg>
            <span class="visually-hidden" id="bd-theme-text">Toggle theme</span>
        </button>
        <ul class="dropdown-menu dropdown-menu-end shadow" aria-labelledby="bd-theme-text">
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="light"
                    aria-pressed="false">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#sun-fill"></use>
                    </svg>
                    Light
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="dark"
                    aria-pressed="false">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#moon-stars-fill"></use>
                    </svg>
                    Dark
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center active" data-bs-theme-value="auto"
                    aria-pressed="true">
                    <svg class="bi me-2 opacity-50" width="1em" height="1em">
                        <use href="#circle-half"></use>
                    </svg>
                    Auto
                    <svg class="bi ms-auto d-none" width="1em" height="1em">
                        <use href="#check2"></use>
                    </svg>
                </button>
            </li>
        </ul>
    </div>


    <header data-bs-theme="dark">
        <div class="collapse text-bg-dark" id="navbarHeader">
            <div class="container">
                <div class="row">
                    <div class="col-sm-8 col-md-7 py-4">
                        <h4>About</h4>
                        <p class="text-body-secondary">Hi! I am Ifeanyi, a Software Engineer and Full-Stack
                            Developer based here in the beautiful province of Alberta, Canada. With a track record of
                            over 6 years in the field, I excel in creating resilient, scalable, and user-centric web,
                            mobile and data-driven applications that tackle real-world challenges head-on.</p>
                        <img src="{% static 'picofme.png' %}" width="100" alt="my profile pic" />
                    </div>

                    <div class="col-sm-4 offset-md-1 py-4">
                        <h4>Contact</h4>
                        <ul class="list-unstyled">
                            <li><a href="https://twitter.com/iomeata" target="_blank" class="text-white">Follow on
                                    Twitter</a></li>
                            <li><a href="https://www.linkedin.com/in/omeatai/" target="_blank" class="text-white">Follow
                                    on LinkedIn</a></li>
                            <li><a href="mailto:omeatai@gmail.com?subject=Contact Form on Website&cc="
                                    class="text-white">Email me</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        <div class="navbar navbar-dark bg-dark shadow-sm">
            <div class="container">
                <a href="#" class="navbar-brand d-flex align-items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" stroke="currentColor"
                        stroke-linecap="round" stroke-linejoin="round" stroke-width="2" aria-hidden="true" class="me-2"
                        viewBox="0 0 24 24">
                        <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z" />
                        <circle cx="12" cy="13" r="4" /></svg>
                    <strong>Ifeanyi Omeata</strong>
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarHeader"
                    aria-controls="navbarHeader" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
            </div>
        </div>
    </header>

    <main>

        <section class="py-2 text-center container">
            <div class="row py-lg-5">
                <div class="col-lg-6 col-md-8 mx-auto">
                    <h1 class="fw-light">Ifeanyi Omeata</h1>
                    <p class="lead text-body-secondary">Hi! My name is Ifeanyi Omeata, a Software Engineer and
                        Full-Stack
                        Developer based here in the beautiful province of Alberta, Canada. With a track record of
                        over 6 years in the field, I excel in creating resilient, scalable, and user-centric web,
                        mobile and data-driven applications that tackle real-world challenges head-on.</p>
                    <p>
                        <a href="#all-jobs" class="btn btn-primary my-2">View my Jobs</a>
                        <a href="mailto:omeatai@gmail.com?subject=Contact Form on Website&cc="
                            class="btn btn-secondary my-2">Email me</a>
                    </p>
                    <img src="{% static 'picofme.png' %}" width="300" alt="my profile pic" />
                </div>
            </div>
        </section>

        <div class="album py-2 bg-body-tertiary">
            <div class="container">

                <h1 id="all-jobs" class="text-center pb-2">My Jobs</h1>

                <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">

                    {% for job in jobs %}

                    <div class="col">
                        <div class="card shadow-sm">

                            <a href="{% url 'job-detail' job.id %}"><img src="{{ job.image.url }}" alt='{{job.title}}'
                                    class="bd-placeholder-img card-img-top p-2 bg-black" width="100%"
                                    height="225" /></a>


                            <div class="card-body">
                                <h4>{{ job.title }}</h4>
                                <p class="card-text">{{ job.summary }}</p>
                                <div class="d-flex justify-content-between align-items-center">
                                    <div class="btn-group">
                                        <a href="{% url 'job-detail' job.id %}" type="button"
                                            class="btn btn-sm btn-outline-secondary">View</a>
                                        <a href="{% url 'job-detail' job.id %}" type="button"
                                            class="btn btn-sm btn-outline-secondary">Edit</a>
                                    </div>
                                    <small class="text-body-secondary">{{ job.image }}</small>
                                    <small class="text-body-secondary">{{ job.image.url }}</small>
                                </div>
                            </div>
                        </div>
                    </div>

                    {% endfor %}
                </div>
            </div>
        </div>
    </main>

    <footer class="text-body-secondary py-5">
        <div class="container">
            <p class="float-end mb-1">
                <a href="#">Back to top</a>
            </p>
            <p class="mb-1">Copyright. Ifeanyi omeata &copy; 2024.</p>
            <p class="mb-0">Need to know more? <a href="https://twitter.com/iomeata" target="_blank">Visit my
                    Twitter.</a> or <a href="https://www.linkedin.com/in/omeatai/" target="_blank">view my LinkedIn</a>.
            </p>
        </div>
    </footer>
    <script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>
    {% comment %} <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous">
    </script> {% endcomment %}

</body>

</html>
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/a5ae5547-bba5-4d7c-9702-0ffd26cbcfb5)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/aab1e84c-23ba-46db-a85c-581633f90a52)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/d1aed37e-87c6-4ecd-b461-eef3e457b3cd)

<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/3cd13c6e-9387-463c-897f-712e58c2813e">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/5ddce9b9-0096-419a-8240-b4ab5a12f9c8">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/9a10238f-4581-4dcc-aa82-4a24635ef8bf">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/d7c7ddd8-d42f-4b23-9a64-fb45e6fc36e0">

# #END</details>

# #END
