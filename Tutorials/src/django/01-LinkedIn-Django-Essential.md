
## +LinkedIn - Django Essential Training

## [COURSE](https://www.linkedin.com/learning/django-essential-training/what-is-django)

<details>
<summary>1. Creating a New Django Project </summary>

# Creating a New Django Project

## Install venv

```py
python -m venv venv
```

## Activate venv

```py
# venv\Scripts\activate
source venv/bin/activate
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
django-admin startproject project_smartnotes .
```

## Start Local Server

```py
python manage.py runserver
```

```x
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
June 16, 2024 - 03:23:31
Django version 5.0.6, using settings 'project_smartnotes.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

<img width="1403" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/fda6f2a5-f8d9-48aa-8780-5262056dfd43">
<img width="960" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/6fb2dc02-b2b2-4a94-ac66-e007f1d4f94f">

# #END</details>

<details>
<summary>2. Create new App - Home </summary>

# Create new App - Home

[https://github.com/omeatai/src-python-flask-django/commit/0959e138fcee4d7829ef38e9ca8ff24a5c443a23](https://github.com/omeatai/src-python-flask-django/commit/0959e138fcee4d7829ef38e9ca8ff24a5c443a23)

## Create App

```py
django-admin startapp home
```

### smartnotes.settings:

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
    'home',
]
```

<img width="1447" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/9d0869ef-4e16-417f-9b18-526bee136a9b">


# #END</details>

<details>
<summary>3. Create View </summary>

# Create View

[https://github.com/omeatai/src-python-flask-django/commit/c1680ccc9d7982ae87252859481cb3d64db13260](https://github.com/omeatai/src-python-flask-django/commit/c1680ccc9d7982ae87252859481cb3d64db13260)

### smartnotes.urls:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]
```

### home.urls:

```py
from django.urls import path
from home import views

urlpatterns = [
    path('home', views.home),
]
```

### home.views:

```py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("<h1>Hello World!</h1>")
```

<img width="1413" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ac80da1e-8b1a-4bc7-aa4f-528bd887843b">
<img width="1280" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/897bdc04-e787-467e-8194-5a5bcc99c229">
<img width="1280" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1292f08d-6ebc-4d3d-a0c0-460ed2869b57">
<img width="1280" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/5c024f37-a954-4ae3-89a0-db735d3a7504">

# #END</details>

<details>
<summary>4. Creating your first Django template </summary>

# Creating your first Django template

[https://github.com/omeatai/src-python-flask-django/commit/6f788cf2b56c91f44b960178d8576c35bbebd11a](https://github.com/omeatai/src-python-flask-django/commit/6f788cf2b56c91f44b960178d8576c35bbebd11a)

### smartnotes.settings:

```py
# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Denver'

USE_I18N = True

USE_TZ = True
```

### home.views:

```py
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.


def home(request):
    # return HttpResponse("<h1>Hello World!</h1>")
    return render(request, 'home/welcome.html', {'name': 'John Doe', 'date': datetime.now()})
```

### home/templates/home/welcome.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>SmartNotes</title>
  </head>

  <body>
    <h1>Welcome to SmartNotes Home Page - {{name}}.</h1>
    <h2>Today is {{date}}</h2>
  </body>
</html>
```

<img width="1413" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/360b36a5-c3e9-4767-81b6-50a6969bbe2c">
<img width="1280" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b117ad99-4daa-4910-9b8d-7581139d5bac">
<img width="1280" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/7f247c75-ff40-4fa4-9f30-266cf411a8f3">
<img width="1280" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/7a366f68-7d08-423b-a7c9-c400262a04af">

# #END</details>

<details>
<summary>5. Migrate Changes </summary>

# Migrate Changes

```py
python manage.py makemigrations
```

```py
python manage.py migrate
```

<img width="449" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/7b035ec1-9768-47cb-82b2-99171cccee67">

# #END</details>

<details>
<summary>6. Create Super User</summary>

# Create Super User

```py
python manage.py createsuperuser
```

# Run Dev Server

```py
python manage.py runserver
```

<img width="448" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/07bc212b-b444-4f42-804e-6212abf24964">
<img width="1330" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/eb04a65d-2c5e-4040-830c-1e1618cd1767">
<img width="1442" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/f883b789-fdf6-46d6-b729-f730c87c7ed6">
<img width="1319" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/97ccec8d-6dcf-4929-b8e0-a8a189fbf2be">

# #END</details>

<details>
<summary>7. Basic User Authentication</summary>

# Basic User Authentication

[https://github.com/omeatai/src-python-flask-django/commit/d5e5549f294eff2e8802a0cbfb499be02c648d31](https://github.com/omeatai/src-python-flask-django/commit/d5e5549f294eff2e8802a0cbfb499be02c648d31)

### home.urls:

```py
from django.urls import path
from home import views

urlpatterns = [
    path('home', views.home),
    path('authorized', views.authorized),
]
```

### home.views:

```py
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    # return HttpResponse("<h1>Hello World!</h1>")
    return render(request, 'home/welcome.html', {'name': 'John Doe', 'date': datetime.now()})


@login_required
def authorized(request):
    return render(request, 'home/authorized.html', {})
```

### home/authorized.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Restricted Area</title>
  </head>

  <body>
    <h1>You are in a restricted area!</h1>
  </body>
</html>
```

<img width="1442" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/4e2e5a7b-8123-4e02-bc14-c92f6b71066b">
<img width="1442" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/60489590-edb1-4fbe-9d9a-7fac08eadf1d">
<img width="1442" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/739ecf40-3968-476a-8119-141a4335c8d9">
<img width="1442" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/9f3c23f0-cc96-4e2e-9066-5eedc5ad5c95">

# #END</details>

<details>
<summary>8. Basic User Authentication 2 - Force Redirect on failed Login</summary>

# Basic User Authentication 2 - Force Redirect on failed Login

[https://github.com/omeatai/src-python-flask-django/commit/ee29ba256602e97df09bcec992f4c0efda93286b](https://github.com/omeatai/src-python-flask-django/commit/ee29ba256602e97df09bcec992f4c0efda93286b)

### home.views:

```py
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    # return HttpResponse("<h1>Hello World!</h1>")
    return render(request, 'home/welcome.html', {'name': 'John Doe', 'date': datetime.now()})


@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html', {})
```

<img width="1442" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/000601ab-8f95-4b1f-a720-34ccf24eb623">

# #END</details>

<details>
<summary>9. Create Notes Model</summary>

# Create Notes Model

[https://github.com/omeatai/src-python-flask-django/commit/09253493e7a3e2e425681639f18e15110a5d6092](https://github.com/omeatai/src-python-flask-django/commit/09253493e7a3e2e425681639f18e15110a5d6092)

## Create new app - notes

```py
django-admin startapp notes
```

### smartnotes.settings:

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
    'home',
    'notes',
]
```

### notes.models:

```py
from django.db import models

# Create your models here.


class Notes(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

## Run migrations

```py
python manage.py makemigrations
python manage.py migrate
```

# #END</details>

<details>
<summary>10. Setup Admin for data creation and manipulation</summary>

# Setup Admin for data creation and manipulation

[https://github.com/omeatai/src-python-flask-django/commit/fe4590e92ae3f0ac735f5950c8660cf79aed015b](https://github.com/omeatai/src-python-flask-django/commit/fe4590e92ae3f0ac735f5950c8660cf79aed015b)

### notes.admin:

```py
from django.contrib import admin
from . import models
# Register your models here.


class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated',)

    # def get_model_name(self):
    #     return "Notes"


admin.site.register(models.Notes, NotesAdmin)
```

### notes.models:

```py
from django.db import models

# Create your models here.


class Notes(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self):
        return self.title
```

## Run migrations

```py
python manage.py makemigrations
python manage.py migrate
```

<img width="1280" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/44e70011-13a8-4329-98e8-de55d982840e">
<img width="1280" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/d2b2e809-b98c-4bf9-97bc-a539bb352808">
<img width="1458" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/354f952d-e64f-4956-ada8-c9c1461ed99c">
<img width="1458" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/6c302e29-1e1d-4400-a752-c38955302f1f">
<img width="1458" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e187c091-b598-40e3-82f4-10f61cbe8d95">

# #END</details>

<details>
<summary>11. Using Django shell for creating and querying data</summary>

# Using Django shell for creating and querying data

## Run Shell:

```py
python manage.py shell
```

## Get Instance of Model Object

```py
from notes.models import Notes
mynote = Notes.objects.get(pk=1)

mynote.title
# 'Make food'

mynote.content
# 'This is how to make the food'
```

## Get all Object Instances

```py
 Notes.objects.all()
# <QuerySet [<Notes: Make food>]>
```

## Create New Object Instance

```py
new_note = Notes.objects.create(title="The second note", content="This is the second note.")

Notes.objects.all()
# <QuerySet [<Notes: Make food>, <Notes: The second note>]>
```

## Filter and Exclude contents

```py
Notes.objects.filter(title__startswith="The")
# <QuerySet [<Notes: The second note>]>

Notes.objects.filter(content__icontains="food")
#  <QuerySet [<Notes: Make food>]>

Notes.objects.exclude(content__icontains="food")
# <QuerySet [<Notes: The second note>]>

Notes.objects.filter(content__icontains="food").exclude(content__icontains="second")
# <QuerySet [<Notes: Make food>]>
```

# #END</details>

<details>
<summary>12. Creating Dynamic Templates - Display all Notes </summary>

# Creating Dynamic Templates - Display all Notes

[https://github.com/omeatai/src-python-flask-django/commit/a135c2a03da27f098e6d5e3a508ffa2746745e96](https://github.com/omeatai/src-python-flask-django/commit/a135c2a03da27f098e6d5e3a508ffa2746745e96)

### notes.models:

```py
from django.db import models

# Create your models here.


class Notes(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self):
        return self.title
```

### smartnotes.urls:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('smart/', include('notes.urls')),
]
```

### notes.urls:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.list),
]
```

### notes.views:

```py
from django.shortcuts import render
from .models import Notes

# Create your views here.


def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})
```

### notes/notes_list.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Notes</title>
  </head>

  <body>
    <h1>Note List</h1>
    <h2>These are the notes:</h2>
    <ul>
      {% for note in notes %}
      <li>{{note.title}}</li>
      {% endfor %}
    </ul>
  </body>
</html>
```

<img width="1409" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a93749d6-a319-421f-b211-3288eecc3786">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ebcd35d1-e9b4-4dd9-88de-028296c7ef34">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/0ccaf7cd-59bb-47b9-bf10-1dd7123819dd">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1b70d099-f746-4499-a1bb-99f82baaa8ab">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/2422a6ee-56fd-4479-baca-80f33bb664e4">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/330aee64-8204-45ba-975c-d34e33a16019">

# #END</details>

<details>
<summary>13. Creating Dynamic Templates - Display content of a single note w 404 Page </summary>

# Creating Dynamic Templates - Display content of a single note w 404 Page

[https://github.com/omeatai/src-python-flask-django/commit/6a213c7aa46ec24c6017a44bad60269918eaf2a0](https://github.com/omeatai/src-python-flask-django/commit/6a213c7aa46ec24c6017a44bad60269918eaf2a0)

### smartnotes.settings:

```py
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  # True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # apps
    'home',
    'notes',
]
```

### notes.urls:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.list),
    path('notes/<int:pk>', views.detail),
]
```

### notes.views:

```py
from django.shortcuts import render
from django.http import Http404

from .models import Notes

# Create your views here.


def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})


def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note does not exist")
    return render(request, 'notes/notes_detail.html', {'note': note})
```

### notes/notes_detail.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Note Detail</title>
  </head>

  <body>
    <h1>{{note.title | title}}</h1>
    <h3>{{note.content}}</h3>
  </body>
</html>
```

### notes/templates/404.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>404 Page</title>
  </head>

  <body>
    <h1>404 - Ooops!</h1>
    <h2>I cannot find the file you requested!</h2>
  </body>
</html>
```

<img width="1409" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/10aa4c56-be8b-4bc6-ba6b-fe52dcf11389">
<img width="1409" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/01259842-9e6f-4a09-9091-10b36c1e636d">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/43c1eb4e-fbfd-4ffb-930f-37db29b0e50d">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e6dabf44-5720-492e-9272-6f2e7f8bae55">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/f637fb96-364d-4acd-9c64-3aed91a93080">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ff107b00-75b3-4da7-891a-28b40ad0b797">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/0a26901f-dad5-4686-9fd6-cc9b18970de1">

# #END</details>

<details>
<summary>14. Django Class Based Views - TemplateView </summary>

# Django Class Based Views - TemplateView

[https://github.com/omeatai/src-python-flask-django/commit/1e10260f38b8bf5b6804d6f45b9f4bf61b1c2edf](https://github.com/omeatai/src-python-flask-django/commit/1e10260f38b8bf5b6804d6f45b9f4bf61b1c2edf)

### home.views:

```py
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'name': 'John Doe', 'date': datetime.now()}


# def home(request):
#     # return HttpResponse("<h1>Hello World!</h1>")
#     return render(request, 'home/welcome.html', {'name': 'John Doe', 'date': datetime.now()})


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    extra_context = {}
    login_url = '/admin'


# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})
```

### home.urls:

```py
from django.urls import path
from home import views

urlpatterns = [
    # path('home', views.home),
    path('home', views.HomeView.as_view()),
    # path('authorized', views.authorized),
    path('authorized', views.AuthorizedView.as_view()),
]
```

<img width="1458" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/27480e31-f225-49ee-aba2-b9a149a9323d">
<img width="1458" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/fb460d21-b9a7-4799-961f-56bc751d5121">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1b2b17f3-5d1c-48bd-9364-25374c1ce361">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/2c4dbd20-39b2-4adb-bc28-ffcac9089466">

# #END</details>

<details>
<summary>15. Django Class Based Views - ListView </summary>

# Django Class Based Views - ListView

[https://github.com/omeatai/src-python-flask-django/commit/3f935498be33171d56e127482e771f199787ab6c](https://github.com/omeatai/src-python-flask-django/commit/3f935498be33171d56e127482e771f199787ab6c)

### notes.views:

```py
from typing import Any
from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView

from .models import Notes

# Create your views here.


class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    ordering = ['-created']
    paginate_by = 10


# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note does not exist")
    return render(request, 'notes/notes_detail.html', {'note': note})
```

### notes.urls:

```py
from django.urls import path
from . import views

urlpatterns = [
    # path('notes', views.list),
    path('notes', views.NotesListView.as_view()),
    path('notes/<int:pk>', views.detail),
]
```

### notes/templates/notes/notes_list.html:

```py
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notes</title>
</head>

<body>
    <h1>Note List</h1>
    <h2>These are the notes:</h2>
    <ul>
        {% for note in notes %}
        <li>{{note.title}}</li>
        {% endfor %}
    </ul>
</body>

</html>
```

<img width="1383" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/8023729d-604c-4b71-9dfa-89fa4501c7cc">
<img width="1208" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/47e33038-8d50-413c-a88e-1eca9978a27d">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/c369c75a-203c-46f5-9844-00796ae8904a">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/0b3720e2-b860-4c42-b7bc-2eccb67e8fb8">

# #END</details>

<details>
<summary>16. Django Class Based Views - DetailView </summary>

# Django Class Based Views - DetailView

[https://github.com/omeatai/src-python-flask-django/commit/3dbc4628a9a8892e9098e455c03cb8c63e4253f5](https://github.com/omeatai/src-python-flask-django/commit/3dbc4628a9a8892e9098e455c03cb8c63e4253f5)

### smartnotes.urls:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('smart/', include('notes.urls')),
]
```

### notes.urls:

```py
from django.urls import path
from . import views

urlpatterns = [
    # path('notes', views.list),
    path('notes', views.NotesListView.as_view(), name='notes-list'),
    # path('notes/<int:pk>', views.detail),
    path('notes/<int:pk>', views.NotesDetailView.as_view(),
         name='notes-detail-list'),
]
```

### notes.views:

```py
from typing import Any
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Notes

# Create your views here.


class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    ordering = ['-created']
    paginate_by = 10


# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            return "404 - Sorry, the requested note does not exist!"


# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note does not exist")
#     return render(request, 'notes/notes_detail.html', {'note': note})
```

### notes/templates/notes/notes_list.html:

```py
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notes</title>
</head>

<body>
    <h1>Note List</h1>
    <h2>These are the notes:</h2>
    <ul>
        {% for note in notes %}
        <li>{{note.title}}</li>
        {% endfor %}
    </ul>
</body>

</html>
```

<img width="1383" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1be41d27-ca7b-421b-95f5-18d52c56fde7">
<img width="1383" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/72c45b25-dd04-409d-87a4-b5cf9c34d48d">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e5f7626e-d377-45eb-9ad2-ca78c7de2074">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/07094330-2eb9-4153-9b6e-a8796c2468ac">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/74a02860-d5d8-44cf-9dab-7e9ee5412633">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/fdbf20ef-4a65-4623-a7cb-ba067f2a68ce">

# #END</details>

<details>
<summary>17. Static Files in Django - CSS in Template </summary>

# Static Files in Django - CSS in Template

[https://github.com/omeatai/src-python-flask-django/commit/c9a69902fd55e8eff47d658603800dab25cb0ab8](https://github.com/omeatai/src-python-flask-django/commit/c9a69902fd55e8eff47d658603800dab25cb0ab8)

### smartnotes.settings:

```py
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

### static/notes/css/style.css:

```css
.note-li {
  color: blue;
  font-size: 18px;
  font-weight: 800;
}
```

### notes/templates/notes/notes_list.html:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="{% static 'notes/css/style.css' %}" />
    <title>Notes</title>
  </head>

  <body>
    <h1>Note List</h1>
    <h2>These are the notes:</h2>
    <ul>
      {% for note in notes %}
      <li class="note-li">{{note.title}}</li>
      {% endfor %}
    </ul>
  </body>
</html>
```

<img width="1383" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b43b561f-4547-41f3-afe7-de0ffe54d353">
<img width="1383" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/9326acdd-5ae5-4bc8-b01d-3a87961fdec2">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/139b36d2-137b-4366-b175-103d50f6489c">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/c2a15c08-1cb5-48f9-87a5-47d3bbea48f8">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/65ed74a3-2119-45ba-8bca-905b770b895c">

# #END</details>

<details>
<summary>18. Base HTML for Templates </summary>

# Base HTML for Templates

[https://github.com/omeatai/src-python-flask-django/commit/9e009fac7c4d43b7c5cae36dd13301e35079146e](https://github.com/omeatai/src-python-flask-django/commit/9e009fac7c4d43b7c5cae36dd13301e35079146e)

### smartnotes.settings:

```py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'static/templates',
        ],
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

### static/notes/css/style.css:

```css
.note-li {
  color: purple;
  font-size: 18px;
  font-weight: 800;
}

h2 {
  color: cadetblue;
}
```

### static/templates/notes/base.html:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="{% static 'notes/css/style.css' %}" />
    <title>Notes</title>
  </head>

  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```

### static/templates/notes/notes_list.html:

```py
{% extends 'notes/base.html' %}

{% block content %}
<h1>Note List</h1>
<h2>These are the notes:</h2>
<ul>
    {% for note in notes %}
    <li class="note-li">{{note.title}}</li>
    {% endfor %}
</ul>
{% endblock content %}
```

<img width="1430" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/047a9f2c-1e33-4827-8cab-c825ab3dd210">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/79af28af-7378-431b-abaa-b208e67194b5">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/c2ef70e3-dd93-4455-83c5-f9d285bdb87b">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/4423d5ed-de11-41c9-98f7-58d85515e682">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/0ac816c0-cb25-49c5-843a-276784f40f71">

# #END</details>

<details>
<summary>19. Styling with Bootstrap and Linking Pages </summary>

# Styling with Bootstrap and Linking Pages

[https://github.com/omeatai/src-python-flask-django/commit/61b4a649138fba4700ea7ecac34d5babea955e80](https://github.com/omeatai/src-python-flask-django/commit/61b4a649138fba4700ea7ecac34d5babea955e80)

### notes.urls:

```py
from django.urls import path
from . import views

urlpatterns = [
    # path('notes', views.list),
    path('notes', views.NotesListView.as_view(), name='notes-list'),
    # path('notes/<int:pk>', views.detail),
    path('notes/<int:pk>', views.NotesDetailView.as_view(),
         name='notes-detail-list'),
]
```

### templates/home/base.html:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
      crossorigin="anonymous"
    />
    <title>SmartNotes</title>
  </head>

  <body>
    <div class="my-5 text-center container">
      {% block content %} {% endblock content %}
    </div>

    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```

### home/templates/home/welcome.html:

```html
{% extends 'home/base.html' %} {% block content %}
<h1>Welcome to SmartNotes Home Page - {{name}}.</h1>
<h2>Today is {{date}}</h2>
<a href="{% url 'notes-list' %}" class="btn btn-primary"
  >Check out these SmartNotes</a
>
{% endblock content %}
```

### templates/notes/base.html:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
      crossorigin="anonymous"
    />
    <link rel="stylesheet" href="{% static 'notes/css/style.css' %}" />
    <title>Notes</title>
  </head>

  <body>
    <div class="my-5 text-center container">
      {% block content %} {% endblock content %}
    </div>

    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```

### notes/templates/notes/notes_list.html:

```html
{% extends 'notes/base.html' %} {% block content %}
<h1>Note List</h1>
<h2 class="mb-5">These are the notes:</h2>

<div class="row row-cols3 g-2">
  {% for note in notes %}
  <div class="col">
    <div class="p-3 border">
      <a
        href="{% url 'notes-detail-list' pk=note.id %}"
        class="text-dark text-decoration-none"
      >
        <h3>{{note.title | title}}</h3>
      </a>
      <p>{{note.content | truncatechars:30}}</p>
    </div>
  </div>
  {% endfor %}
</div>

{% endblock content %}
```

### notes/templates/notes/notes_detail.html:

```html
{% extends 'notes/base.html' %} {% block content %}
<div class="border round">
  <h1 class="my-5">{{note.title | title}}</h1>
  <p>{{note.content}}</p>
</div>

{% endblock content %}
```

<img width="1453" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a9a658c5-2846-4604-92b0-a1f2b73c5e5d">
<img width="1453" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/340f8b96-1493-42ae-b0a3-5fe1a8c7cedb">
<img width="1453" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/25d5c2c3-fa4f-4976-89e3-de46118d1aea">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/63f9b354-057c-4c3a-b3a2-d9e526685efd">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/f12343af-535e-4817-9ea2-b8aaa055e3fd">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/3528ba4f-38f1-40d9-9e52-5c85a9a73c2a">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/f8acfc54-55cc-471c-a24a-45841e71760f">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/91d083ca-a9b7-4696-ac40-507d024ec472">
<img width="1252" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e3e639e1-3b09-413c-8493-50c61914e06c">

# #END</details>

<details>
<summary>20. Django Class Based Views - CreateView </summary>

# Django Class Based Views - CreateView

[https://github.com/omeatai/src-python-flask-django/commit/2f833971f6a3e9d78c730e912bcb08105d79e8c9](https://github.com/omeatai/src-python-flask-django/commit/2f833971f6a3e9d78c730e912bcb08105d79e8c9)

### smartnotes.urls:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('smart/', include('notes.urls')),
]
```

### notes.urls:

```py
from django.urls import path
from . import views

urlpatterns = [
    # path('notes', views.list),
    path('notes', views.NotesListView.as_view(), name='notes-list'),
    # path('notes/<int:pk>', views.detail),
    path('notes/<int:pk>', views.NotesDetailView.as_view(),
         name='notes-detail-list'),
    path('notes/create', views.NotesCreateView.as_view(), name='notes-create'),
]
```

### notes.views:

```py
from typing import Any
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from .models import Notes

# Create your views here.


class NotesCreateView(CreateView):
    model = Notes
    fields = ['title', 'content']
    success_url = '/smart/notes'
    template_name = 'notes/notes_create.html'


class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    ordering = ['-created']
    paginate_by = 10


# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            # return render(self.request, '404.html', {})
            # return HttpResponseRedirect(reverse('notes-detail-list', args=[1]))
            # return HttpResponseRedirect(reverse('notes-list'))
            return "404 - Sorry, the requested note does not exist!"


# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note does not exist")
#     return render(request, 'notes/notes_detail.html', {'note': note})
```

### notes/templates/notes/notes_create.html:

```py
{% extends 'notes/base.html' %}

{% block content %}
<form action="{% url 'notes-create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-primary my-5">Submit</button>
</form>

{% endblock content %}
```

<img width="1411" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1b131ba3-80fe-4ccd-9b3f-fc6fb1684f05">
<img width="1411" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/269ca0b6-300e-42de-abd4-94a63760f233">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/0b81c59f-d6a6-46d0-8b6c-d91b224c1909">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/937c3f1a-7146-49d5-a646-822e7a71e42a">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e34fd8f9-3302-454b-ab2f-a4c8df055f8f">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ac2fdb6a-b470-4fc5-93e4-cfaf999cd9f9">

# #END</details>

<details>
<summary>21. Using Model Forms </summary>

# Using Model Forms

[https://github.com/omeatai/src-python-flask-django/commit/5afb11cc82683921b2d35eeb2928fe655b2a59c1](https://github.com/omeatai/src-python-flask-django/commit/5afb11cc82683921b2d35eeb2928fe655b2a59c1)

### notes.forms:

```py
from django import forms

from .models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content']
        labels = {
            'title': 'Title',
            'content': 'Content',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError(
                "Title must be at least 5 characters long.")
        if "Django" not in title:
            raise forms.ValidationError(
                "Title must contain the word 'Django'. We only accept notes about Django.")
        return title
```

### notes.views:

```py
from typing import Any
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from .models import Notes
from .forms import NotesForm

# Create your views here.


class NotesCreateView(CreateView):
    model = Notes
    # fields = ['title', 'content']
    success_url = '/smart/notes'
    template_name = 'notes/notes_create.html'
    form_class = NotesForm


class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    ordering = ['-created']
    paginate_by = 10


# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            # return render(self.request, '404.html', {})
            # return HttpResponseRedirect(reverse('notes-detail-list', args=[1]))
            # return HttpResponseRedirect(reverse('notes-list'))
            return "404 - Sorry, the requested note does not exist!"


# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note does not exist")
#     return render(request, 'notes/notes_detail.html', {'note': note})
```

### notes/templates/notes/notes_create.html:

```html
{% extends 'notes/base.html' %} {% block content %}
<form action="{% url 'notes-create' %}" method="POST">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit" class="btn btn-primary my-5">Submit</button>
</form>

{% if form.errors %}
<div class="alert alert-danger my-5">
  <div><strong>Oops!</strong> Something went wrong.</div>
  {{ form.errors.title.as_text }}
  <div>
    {% for field in form %} {% for error in field.errors %}
    <p>{{ error }}</p>
    {% endfor %} {% endfor %}
  </div>
</div>
{% endif %} {% endblock content %}
```

### templates/notes/base.html:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
      crossorigin="anonymous"
    />
    <link rel="stylesheet" href="{% static 'notes/css/style.css' %}" />
    <title>Notes</title>
  </head>

  <body>
    <div class="my-5 text-center container">
      {% block content %} {% endblock content %}
    </div>

    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```

### static/notes/css/style.css:

```css
.note-li {
  color: purple;
  font-size: 18px;
  font-weight: 800;
}

h2 {
  color: cadetblue;
}

ul.errorlist {
  display: none;
  color: red;
}
```

<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a19e43ff-810f-4c52-bce2-f63665e9d520">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/128c4e30-94e7-4154-bf9e-0c68c227dc41">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/9d71c552-9a5f-4159-bda8-951b60657f6a">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b7d2b308-70b8-490a-8ee5-a7a61a022abc">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/3d358e29-53a3-45ca-aead-7e89a8a6dbb3">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/d60a4b5e-d4a5-4ff3-a87e-d7c49e4316a3">

# #END</details>

<details>
<summary>22. Django Class Based Views - UpdateView </summary>

# Django Class Based Views - UpdateView

[https://github.com/omeatai/src-python-flask-django/commit/86fd903694ab1879f984b8c104499ca3980903bf](https://github.com/omeatai/src-python-flask-django/commit/86fd903694ab1879f984b8c104499ca3980903bf)

### notes.urls:

```py
from django.urls import path
from . import views

urlpatterns = [
    # path('notes', views.list),
    path('notes', views.NotesListView.as_view(), name='notes-list'),
    # path('notes/<int:pk>', views.detail),
    path('notes/<int:pk>', views.NotesDetailView.as_view(),
         name='notes-detail-list'),
    path('notes/create', views.NotesCreateView.as_view(), name='notes-create'),
    path('notes/<int:pk>/edit',
         views.NotesUpdateView.as_view(), name='notes-update'),
]
```

### notes.views:

```py
from typing import Any
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Notes
from .forms import NotesForm

# Create your views here.


class NotesUpdateView(UpdateView):
    model = Notes
    # fields = ['title', 'content']
    success_url = '/smart/notes'
    template_name = 'notes/notes_update.html'
    form_class = NotesForm


class NotesCreateView(CreateView):
    model = Notes
    # fields = ['title', 'content']
    success_url = '/smart/notes'
    template_name = 'notes/notes_create.html'
    form_class = NotesForm


class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    ordering = ['-created']
    paginate_by = 10


# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            # return render(self.request, '404.html', {})
            # return HttpResponseRedirect(reverse('notes-detail-list', args=[1]))
            # return HttpResponseRedirect(reverse('notes-list'))
            return "404 - Sorry, the requested note does not exist!"


# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note does not exist")
#     return render(request, 'notes/notes_detail.html', {'note': note})
```

### notes/templates/notes/notes_detail.html:

```py
{% extends 'notes/base.html' %}

{% block content %}
<div class="border round">
    <h1 class="my-5">{{note.title | title}}</h1>
    <p>{{note.content}}</p>
</div>

<a href="{% url 'notes-list' %}" class="btn btn-secondary my-5">Back</a>
<a href="{% url 'notes-update' pk=note.id %}" class="btn btn-secondary my-5">Edit</a>

{% endblock content %}
```

### notes/templates/notes/notes_update.html:

```py
{% extends 'notes/base.html' %}

{% block content %}
<form method="POST" class="my-5">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-primary">Submit</button>
</form>

{% if form.errors %}
<div class="alert alert-danger my-5">
    <div><strong>Oops!</strong> Something went wrong.</div>
    {{ form.errors.title.as_text }}
    <div>
        {% for field in form %}
        {% for error in field.errors %}
        <p>{{ error }}</p>
        {% endfor %}
        {% endfor %}
    </div>
</div>
{% endif %}

<a href="{% url 'notes-list' %}" class="btn btn-secondary">Cancel</a>

{% endblock content %}
```

<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/8f757657-d69e-4d8c-8e5e-95e1c885246e">
<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ea7ea682-5762-43b2-9bd4-1c63a639abf7">
<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/d05d8190-65c0-4ebf-a481-c424005a3ab4">
<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/d3179dc8-05e7-43e6-8d9b-51669c6e9c5b">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a34446f2-c19a-41e8-a214-a786bc2cdf89">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a113079c-ae1f-4f0f-9ae8-2055abe7b575">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b1df57b1-b143-49c0-ba5a-7d07b55c7765">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a53b4b3e-6dae-492b-9aa0-bf3834631ec4">

# #END</details>

<details>
<summary>23. Django Class Based Views - DeleteView </summary>

# Django Class Based Views - DeleteView

[https://github.com/omeatai/src-python-flask-django/commit/ce92ed9ce5332eb39a9b48c0ff0ee6d0364b1cbc](https://github.com/omeatai/src-python-flask-django/commit/ce92ed9ce5332eb39a9b48c0ff0ee6d0364b1cbc)

### notes.urls:

```py
from django.urls import path
from . import views

urlpatterns = [
    # path('notes', views.list),
    path('notes', views.NotesListView.as_view(), name='notes-list'),
    # path('notes/<int:pk>', views.detail),
    path('notes/<int:pk>', views.NotesDetailView.as_view(),
         name='notes-detail-list'),
    path('notes/create', views.NotesCreateView.as_view(), name='notes-create'),
    path('notes/<int:pk>/edit',
         views.NotesUpdateView.as_view(), name='notes-update'),
    path('notes/<int:pk>/delete',
         views.NotesDeleteView.as_view(), name='notes-delete'),
]
```

### notes.views:

```py
from typing import Any
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Notes
from .forms import NotesForm

# Create your views here.


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'


class NotesUpdateView(UpdateView):
    model = Notes
    # fields = ['title', 'content']
    success_url = '/smart/notes'
    template_name = 'notes/notes_update.html'
    form_class = NotesForm


class NotesCreateView(CreateView):
    model = Notes
    # fields = ['title', 'content']
    success_url = '/smart/notes'
    template_name = 'notes/notes_create.html'
    form_class = NotesForm


class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    ordering = ['-created']
    paginate_by = 10


# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            # return render(self.request, '404.html', {})
            # return HttpResponseRedirect(reverse('notes-detail-list', args=[1]))
            # return HttpResponseRedirect(reverse('notes-list'))
            return "404 - Sorry, the requested note does not exist!"


# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note does not exist")
#     return render(request, 'notes/notes_detail.html', {'note': note})

```

### notes/templates/notes/notes_delete.html:

```py
{% extends 'notes/base.html' %}

{% block content %}
<form method="POST" class="my-5">
    {% csrf_token %}
    {{ form.as_p }}
    <p>Are you sure you want to delete "{{notes.title}}"?</p>
    <p>This action can't be undone.</p>
    <button type="submit" class="btn btn-danger">Confirm</button>
</form>

{% if form.errors %}
<div class="alert alert-danger my-5">
    <div><strong>Oops!</strong> Something went wrong.</div>
    {{ form.errors.title.as_text }}
    <div>
        {% for field in form %}
        {% for error in field.errors %}
        <p>{{ error }}</p>
        {% endfor %}
        {% endfor %}
    </div>
</div>
{% endif %}

<a href="{% url 'notes-list' %}" class="btn btn-secondary">Cancel</a>

{% endblock content %}
```

### notes/templates/notes/notes_detail.html:

```py
{% extends 'notes/base.html' %}

{% block content %}
<div class="border round">
    <h1 class="my-5">{{note.title | title}}</h1>
    <p>{{note.content}}</p>
</div>

<a href="{% url 'notes-list' %}" class="btn btn-secondary my-5">Back</a>
<a href="{% url 'notes-update' pk=note.id %}" class="btn btn-secondary my-5">Edit</a>
<a href="{% url 'notes-delete' pk=note.id %}" class="btn btn-danger my-5">Delete</a>

{% endblock content %}
```

<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/11968d06-a6a0-4a13-b9f9-523704622728">
<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/eb5a165c-012d-4279-b796-17ab6135c727">
<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/4ef12d30-fc42-43b9-aced-7c5115290249">
<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/2c0dd2f5-d6f4-401a-90f1-7ecb8fb15d00">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/92e3e804-c948-4903-9b0d-56ef2c3a22c5">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ebc9e374-d39b-4ff6-a131-bbbcf6e258e7">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/d2b82cbb-c3ad-4562-8b85-9e4ad48a9108">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/2d9a1e2f-b050-46d1-b785-657a0b3cfcad">

# #END</details>

<details>
<summary>24. Django Model - ForeignKey Relationships </summary>

# Django Model - ForeignKey Relationships

[https://github.com/omeatai/src-python-flask-django/commit/2f06d43716aeec0be8dfd79e9e70f503c95f9cb3](https://github.com/omeatai/src-python-flask-django/commit/2f06d43716aeec0be8dfd79e9e70f503c95f9cb3)

### notes.models:

```py
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Notes(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='notes')

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self):
        return self.title
```

## Run Migration:

```py
python manage.py makemigrations
python manage.py migrate
```

```x
➜  myproject git:(main) ✗ python manage.py makemigrations
It is impossible to add a non-nullable field 'user' to notes without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.
Select an option: 1
Please enter the default value as valid Python.
The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
Type 'exit' to exit this prompt
>>> 1
Migrations for 'notes':
  notes/migrations/0003_notes_user.py
    - Add field user to notes
➜  myproject git:(main) ✗ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, notes, sessions
Running migrations:
  Applying notes.0003_notes_user... OK
➜  myproject git:(main) ✗
```

## Run Django Shell

```py
python manage.py shell
```

```x
➜  myproject git:(main) ✗ python manage.py shell
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.20.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from django.contrib.auth.models import User

In [2]: user = User.objects.get(pk=1)

In [3]: user
Out[3]: <User: admin>

In [4]: user.notes.count()
Out[4]: 1

In [5]: user.notes.all()
Out[5]: <QuerySet [<Notes: Make food>]>

In [6]:

```

<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/89948b35-4faf-4e0c-b5ce-ff1404490ab7">

# #END</details>

<details>
<summary>25. Displaying Logged User Data with LoginRequiredMixin </summary>

# Displaying Logged User Data with LoginRequiredMixin

[https://github.com/omeatai/src-python-flask-django/commit/f14e0baa6a7c6e609002003120b5fc74ed461452](https://github.com/omeatai/src-python-flask-django/commit/f14e0baa6a7c6e609002003120b5fc74ed461452)

[https://ccbv.co.uk/](https://ccbv.co.uk/)

### notes.views:

```py
from typing import Any
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Notes
from .forms import NotesForm

# Create your views here.


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'


class NotesUpdateView(UpdateView):
    model = Notes
    # fields = ['title', 'content']
    success_url = '/smart/notes'
    template_name = 'notes/notes_update.html'
    form_class = NotesForm


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    # fields = ['title', 'content']
    success_url = '/smart/notes'
    template_name = 'notes/notes_create.html'
    form_class = NotesForm

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    ordering = ['-created']
    paginate_by = 10
    login_url = '/admin'

    def get_queryset(self):
        # return Notes.objects.filter(user=self.request.user).order_by('-created')
        return self.request.user.notes.all().order_by('-created')


# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            # return render(self.request, '404.html', {})
            # return HttpResponseRedirect(reverse('notes-detail-list', args=[1]))
            # return HttpResponseRedirect(reverse('notes-list'))
            return "404 - Sorry, the requested note does not exist!"


# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note does not exist")
#     return render(request, 'notes/notes_detail.html', {'note': note})
```

### notes.models:

```py
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Notes(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='notes')

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self):
        return self.title
```

<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/5f0c9a42-25ec-4d2f-8dbe-6968a85cb2f4">
<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a2f8a5d4-6dd1-409e-99ef-1b543d9e1621">
<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b7080570-2ea6-40f1-b54d-420e87fbe425">
<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/4313ab0d-b0d4-4c40-8952-446c4bda0714">
<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/bce92f56-1d35-4d3d-9941-d9d63e0322b9">
<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1a38113d-ace7-4186-be6c-d1e78953d14d">
<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1b628141-0818-44e6-b721-c57963b1239e">

# #END</details>

<details>
<summary>26. Login and Logout Functionality </summary>

# Login and Logout Functionality

[https://github.com/omeatai/src-python-flask-django/commit/c9570d056b9827de59c53f69197a19baabf48d50](https://github.com/omeatai/src-python-flask-django/commit/c9570d056b9827de59c53f69197a19baabf48d50)

### smartnotes.settings:

```py
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/smart/notes'
LOGIN_URL = '/login'
```

### home.urls:

```py
from django.urls import path
from home import views

urlpatterns = [
    # path('home', views.home),
    path('', views.HomeView.as_view(), name='home'),
    # path('authorized', views.authorized),
    path('authorized', views.AuthorizedView.as_view(), name='authorized'),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
]
```

### home.views:

```py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, logout, login


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'
    http_method_names = ['get', 'post', 'options']
    next_page = 'login'

    def dispatch(self, request, *args, **kwargs):
        # return super().dispatch(request, *args, **kwargs)
        # Redirect to a specific URL after logout
        logout(request)
        return redirect('login')


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'
    # next_page = 'list'


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'name': 'James Doe', 'date': datetime.now()}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    extra_context = {}
    login_url = 'login'

```

### src-python/django-essentials/myproject/home/templates/home/login.html:

```html
{% extends 'home/base.html' %} {% block content %}
<h1>Login</h1>

<form method="post">
  {% csrf_token %} {{ form.as_p }}
  <input type="submit" class="btn btn-secondary" />
</form>
{% endblock content %}
```

### src-python/django-essentials/myproject/home/templates/home/logout.html:

```html
{% extends 'home/base.html' %} {% block content %}
<h1>Logout</h1>
<h2>Hope to see you soon :)</h2>
<p>You have successfully logged out.</p>
{% endblock content %}
```

<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/80339acd-97c4-4b62-ba7a-c3b8913c698b">
<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/3606efeb-5dc5-4aa0-b3ce-0474a32eeee1">
<img width="1471" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/4bfc1e9b-4f3a-43a6-a348-b0dd8cad4f02">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/f155eb3c-094c-4f9c-b516-39306b1ad39b">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/5ff1d47c-9d01-413d-beb4-8f6b5c4ea402">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ce7fa2a6-aac4-4633-af32-c0dedd5e408f">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/f768f703-993e-4519-9b07-ec003630d695">
<img width="1249" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/170cbc76-bb7f-475e-8f07-853ce2fa5aa6">

# #END</details>

<details>
<summary>27. Signup/Register Functionality </summary>

# Signup/Register Functionality

[https://github.com/omeatai/src-python-flask-django/commit/691b2d3a6dbc30a423f7be44f4bea53ef099b2ef](https://github.com/omeatai/src-python-flask-django/commit/691b2d3a6dbc30a423f7be44f4bea53ef099b2ef)

### home.urls:

```py
from django.urls import path
from home import views

urlpatterns = [
    # path('home', views.home),
    path('', views.HomeView.as_view(), name='home'),
    # path('authorized', views.authorized),
    path('authorized', views.AuthorizedView.as_view(), name='authorized'),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup', views.SignupView.as_view(), name='signup'),
]
```

### home.views:

```py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


class UserSignupForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = False
        user.is_superuser = False
        if commit:
            user.save()
        return user


class SignupView(CreateView):
    form_class = UserSignupForm  # UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'
    # model = User

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes-list')
        return super().get(request, *args, **kwargs)


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'
    http_method_names = ['get', 'post', 'options']

    def dispatch(self, request, *args, **kwargs):
        # return super().dispatch(request, *args, **kwargs)
        # Redirect to a specific URL after logout
        return redirect('/login')


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'name': 'John Doe', 'date': datetime.now()}


# def home(request):
#     # return HttpResponse("<h1>Hello World!</h1>")
#     return render(request, 'home/welcome.html', {'name': 'John Doe', 'date': datetime.now()})


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    extra_context = {}
    login_url = '/admin'


# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})


# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
#
# class RegisterForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


# ### in views.py ###
# from django.contrib.auth import login as auth_login
# from .forms import RegisterForm
#
# def sign_up(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#     else:
#         form = RegisterForm()
#
#     return render(request, 'sign_up.html', {'form': form})
```

### notes.views:

```py
from typing import Any
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Notes
from .forms import NotesForm

# Create your views here.


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'


class NotesUpdateView(UpdateView):
    model = Notes
    # fields = ['title', 'content']
    success_url = '/smart/notes'
    template_name = 'notes/notes_update.html'
    form_class = NotesForm


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    # fields = ['title', 'content']
    success_url = '/smart/notes'
    template_name = 'notes/notes_create.html'
    form_class = NotesForm

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    ordering = ['-created']
    paginate_by = 10
    login_url = '/login'

    def get_queryset(self):
        # return Notes.objects.filter(user=self.request.user).order_by('-created')
        return self.request.user.notes.all().order_by('-created')


# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            # return render(self.request, '404.html', {})
            # return HttpResponseRedirect(reverse('notes-detail-list', args=[1]))
            # return HttpResponseRedirect(reverse('notes-list'))
            return "404 - Sorry, the requested note does not exist!"


# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note does not exist")
#     return render(request, 'notes/notes_detail.html', {'note': note})
```

### src-python/django-essentials/myproject/home/templates/home/register.html:

```py
{% extends 'home/base.html' %}

{% block content %}
<h1>Register</h1>

<form method="POST" style="text-align: left; margin: 0 auto; width: 600px">
    {% csrf_token %}
    {{ form.non_field_errors }}
    {% for field in form %}
    <div class="my-3">
        {% comment %} <label for="{{ form.field.id_for_label }}">Your {{field.label_tag}}</label> {% endcomment %}
        {{ field.label_tag }}
        {{ field }}
        {{ field.errors }}
    </div>
    {% endfor %}
    <input type='submit' class="btn btn-secondary" name="submit" />
</form>

<hr />

<form method="POST" style="text-align: left; margin: 0 auto; width: 600px">
    {% csrf_token %}
    {{ form.non_field_errors }}
    {{ form.as_p }}
    <input type='submit' class="btn btn-secondary" name="submit" />
</form>

{% endblock content %}
```

<img width="1367" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b318e50a-1ec6-4d74-9906-4c87cdb366cf">
<img width="1367" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/0a8e48a8-5621-489b-8612-2c2208702998">
<img width="1367" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/0705c63c-0aa1-465d-b7cf-e139ee16e720">
<img width="1171" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ef5c18af-283c-4850-979e-c6aa6251a747">
<img width="1171" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b9e26ef9-c351-4a64-87cc-36ed5161f809">
<img width="1171" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/504f4ad6-ff04-4e2d-b778-c5f23425b6d5">
<img width="1171" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/23df12a4-5734-4058-8a11-7cb53f4b4c44">

# #END</details>

<details>
<summary>28. Creating Nav Menu </summary>

# Creating Nav Menu

[https://github.com/omeatai/src-python-flask-django/commit/02788d37cbaf2ec7804ba1e66fb9c39ca166903f](https://github.com/omeatai/src-python-flask-django/commit/02788d37cbaf2ec7804ba1e66fb9c39ca166903f)

### home.urls:

```py
from django.urls import path
from home import views

urlpatterns = [
    # path('home', views.home),
    path('', views.HomeView.as_view(), name='home'),
    # path('authorized', views.authorized),
    path('authorized', views.AuthorizedView.as_view(), name='authorized'),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup', views.SignupView.as_view(), name='signup'),
]
```

### home.views:

```py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

# Create your views here.


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'
    http_method_names = ['get', 'post', 'options']

    def dispatch(self, request, *args, **kwargs):
        super().dispatch(request, *args, **kwargs)
        logout(request)
        # Redirect to a specific URL after logout
        return redirect('/login')


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)


class UserSignupForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = False
        user.is_superuser = False
        if commit:
            user.save()
        return user


class SignupView(CreateView):
    form_class = UserSignupForm  # UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'
    # model = User

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes-list')
        return super().get(request, *args, **kwargs)


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'name': 'John Doe', 'date': datetime.now()}
    login_url = '/login'


# def home(request):
#     # return HttpResponse("<h1>Hello World!</h1>")
#     return render(request, 'home/welcome.html', {'name': 'John Doe', 'date': datetime.now()})


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    extra_context = {}
    login_url = '/login'


# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})


# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
#
# class RegisterForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


# ### in views.py ###
# from django.contrib.auth import login as auth_login
# from .forms import RegisterForm
#
# def sign_up(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#     else:
#         form = RegisterForm()
#
#     return render(request, 'sign_up.html', {'form': form})

```

### src-python/django-essentials/myproject/templates/home/base.html:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
      crossorigin="anonymous"
    />
    <title>SmartNotes</title>
  </head>

  <body>
    <nav class="navbar navbar-dark bg-dark">
      <div class="ms-auto">
        <div class="navbar-nav ms-auto flex-row my-2">
          {% if user.is_authenticated %}
          <a class="btn btn-outline-light me-1" href="{% url 'home' %}">Home</a>
          <a class="btn btn-outline-light me-1" href="{% url 'notes-list' %}"
            >Notes</a
          >
          <a class="btn btn-outline-light me-1" href="{% url 'notes-create' %}"
            >Create Note</a
          >
          <a class="btn btn-outline-light me-1" href="{% url 'logout' %}"
            >Logout</a
          >

          {% else %}

          <a class="btn btn-outline-light me-1" href="{% url 'login' %}"
            >Login</a
          >
          <a class="btn btn-outline-light me-1" href="{% url 'signup' %}"
            >Register</a
          >

          {% endif %}
        </div>
      </div>
    </nav>
    <div class="my-5 text-center container">
      {% block content %} {% endblock content %}
    </div>

    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```

### src-python/django-essentials/myproject/templates/notes/base.html:

```py
{% load static %}

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="{% static 'notes/css/style.css' %}">
    <title>Notes</title>
</head>

<body>

    <nav class="navbar navbar-dark bg-dark">
        <div class="ms-auto">
            <div class="navbar-nav ms-auto flex-row my-2">

                {% if user.is_authenticated %}
                <a class="btn btn-outline-light me-1" href="{% url 'home' %}">Home</a>
                <a class="btn btn-outline-light me-1" href="{% url 'notes-list' %}">Notes</a>
                <a class="btn btn-outline-light me-1" href="{% url 'notes-create' %}">Create Note</a>
                <a class="btn btn-outline-light me-1" href="{% url 'logout' %}">Logout</a>

                {% else %}

                <a class="btn btn-outline-light me-1" href="{% url 'login' %}">Login</a>
                <a class="btn btn-outline-light me-1" href="{% url 'signup' %}">Register</a>

                {% endif %}

            </div>
        </div>
    </nav>
    <div class="my-5 text-center container">
        {% block content %}
        {% endblock content %}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous">
    </script>
</body>

</html>
```

<img width="1474" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b4c676ce-9151-47a0-8b77-48f1c9c44eb3">
<img width="1474" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/675aa88b-b303-4145-afd8-145d42718841">
<img width="1474" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/0e50370e-0462-4ca2-84e2-8bbaed473bbd">
<img width="1474" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/5d6afec2-d8c6-4f7e-86c2-fe862e0046ff">
<img width="1474" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/4ae490ee-34fe-4700-a096-f70509858fe3">

# #END</details>

# #END



# DEMO

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/3520dba9-8728-4306-bf5a-fe2890d51c88)


