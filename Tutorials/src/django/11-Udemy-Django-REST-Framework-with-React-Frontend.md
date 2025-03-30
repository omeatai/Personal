# DJANGO REST FRAMEWORK WITH REACT FRONTEND

## [COURSE](https://www.udemy.com/course/django-django-rest-framework-build-rest-api-in-python/)

+BUILDING BLOG APPLICATION IN DJANGO

<details>
  <summary>1. Introduction </summary>

Install virtual env:

```py
python -m venv venv_dj_blog
```

Activate virtual env:

```py
source venv_dj_blog/bin/activate
```

Install Django:

```py
python -m pip install Django
pip install Django
pip install Django==4.1.5
```

Upgrade pip:

```py
python -m pip install --upgrade pip
```

Create Requirements:

```py
pip freeze > requirements.txt
```

Create Project:

```py
django-admin startproject Blog
django-admin startproject Blog .
```

Run Migrations:

```py
#python manage.py makemigrations
python manage.py migrate
```

Start local Server:

```py
python manage.py runserver
```

</details>

<details>
  <summary>2. Create Super User</summary>

```py
python manage.py createsuperuser
```

```py
# Username (leave blank to use 'ifeanyiomeata'): admin
# Email address: admin@gmail.com
# Password:
# Password (again):
# This password is too short. It must contain at least 8 characters.
# This password is too common.
# This password is entirely numeric.
# Bypass password validation and create user anyway? [y/N]: y
# Superuser created successfully.
# (venv-djblog) ifeanyiomeata@Ifeanyis-MacBook-Air djblog %
```

```py
python manage.py runserver
```

http://127.0.0.1:8000/admin/:

![](https://user-images.githubusercontent.com/32337103/215768567-5d80987f-c627-444a-b384-9591a942f9fb.png)

![](https://user-images.githubusercontent.com/32337103/215768464-b29c8b45-2baa-4271-8bdb-17478160e42e.png)

</details>

<details>
  <summary>3. Create App - articles </summary>

```py
python manage.py startapp articles
```

Register App in Settings.py:

```py

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'articles'
]

```

</details>

<details>
  <summary>4. Create a Function View  </summary>

articles/views.py:

```py
from django.shortcuts import render, HttpResponse

# Create your views here.

def article_list(request):
    return HttpResponse("This is our first view for articles")
```

articles/urls.py:

```py
from django.urls import path
from .views import article_list

urlpatterns = [
    path('', article_list, name='article_list')
]

```

djblog/urls.py:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('articles.urls') )
]

```

![](https://user-images.githubusercontent.com/32337103/215846696-05e3e185-0a45-40d4-a0ef-ea06625a9169.png)

</details>

<details>
  <summary>5. Create Article model</summary>

articles/models.py:

```py
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)
    published = models.DateTimeField (auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
```

Run Migrations:

```py
python manage.py makemigrations
python manage.py migrate
```

</details>

<details>
  <summary>6. Types of Model Relationships</summary>

Many to One Relationship:

```py
class Category(models.Model):
  name = models.CharField(max_length=30)

class Article(models.Model):
  title = models.CharField(max_length=30)
  description = models.CharField(max_length=100)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
```

One to One Relationship:

```py
class Place(models.Model):
  name = models.CharField(max_length=50)
  address = models.CharField(max_length=80)

class Restaurant(models.Model):
  place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
  serves_hot_dogs = models.BooleanField(default=False)
  serves_pizza = models.BooleanField(default=False)
```

Many to Many Relationship:

```py
class Publication(models.Model):
  title = models.CharField(max_length=30)

class Article(models.Model):
  headline = models.CharField(max_length=100)
  publications = models.ManyToManyField(Publication)
```

</details>

<details>
  <summary>7. Register Article Model in Admin</summary>

![](https://user-images.githubusercontent.com/32337103/215871020-7c6ebe88-6df2-4fa3-8d8a-f378481b3315.png)

article/admin.py:

```py
from django.contrib import admin
from .models import Article

# Register your models here.
admin.site.register(Article)
```

![](https://user-images.githubusercontent.com/32337103/215872036-54c00bc1-9ecb-46e4-86af-2fd266b1fc00.png)

![](https://user-images.githubusercontent.com/32337103/215872428-284492e9-a096-486e-a602-d52469d37f7a.png)

![](https://user-images.githubusercontent.com/32337103/215872531-f492e5bb-65e3-43e0-8e56-f0d026e9e381.png)

article/models.py:

```py
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)
    published = models.DateTimeField (auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
```

![](https://user-images.githubusercontent.com/32337103/215873268-146b239e-df87-4444-858f-8b032f0e38a6.png)

article/admin.py:

```py
from django.contrib import admin
from .models import Article

# Register your models here.
#admin.site.register(Article)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'author')
    date_hierarchy = 'published'
    search_fields = ('title', 'description')
```

![](https://user-images.githubusercontent.com/32337103/215874163-e718c175-a845-437c-9e79-fb07cc9a3ee1.png)

</details>

<details>
  <summary>8. Create Django Templates </summary>

Required arguments:

- request: The request object is used to generate the response.
- template_name: The full name of a template to use or sequence of template names.

Optional Arguments:

- context: A dictionary of values to add to the template context. By default, this is an
  empty dictionary. If a value in the dictionary is callable, the view will call it just before rendering the template.
- content_type: The MIME type to use for the resulting document. Defaults to 'text/html".
- status: The status code for the response. Defaults to 200.

There are two types of Templates:

- App labeled templates
- Project labeled templates

App labeled templates -

articles/templates/articles.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Article List</title>
  </head>
  <body>
    <h1>Article List</h1>
    <p>This is the place to render articles from Database.</p>
  </body>
</html>
```

articles/views.py:

```py
from django.shortcuts import render, HttpResponse

# Create your views here.

def article_list(request):
    # return HttpResponse("This is our first view for articles")
    return render(request, 'articles.html')

```

![](https://user-images.githubusercontent.com/32337103/215956850-66d70521-554a-4453-9ba1-8ede5bb0b7c6.png)

</details>

<details>
  <summary>9. Render Context in Template </summary>

articles/views.py:

```py
from django.shortcuts import render, HttpResponse

# Create your views here.

def article_list(request):
    article = "This is my first article title"
    return render(request, 'articles.html', {'article':article})

```

articles/templates/articles.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Article List</title>
  </head>
  <body>
    <h1>Article List</h1>
    <p>This is the place to render articles from Database.</p>
    <p>{{article}}</p>
  </body>
</html>
```

![](https://user-images.githubusercontent.com/32337103/215957683-f601ae19-f429-40bb-a551-b2a0f516294c.png)

</details>

<details>
  <summary>10. Project Labeled Templates</summary>

articles/views.py:

```py
from django.shortcuts import render, HttpResponse

# Create your views here.

def article_list(request):
    article = "This is my first article title"
    return render(request, 'articles.html', {'article':article})

```

djblog/templates/articles.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Article List</title>
  </head>
  <body>
    <h1>Article List</h1>
    <p>This is the place to render articles from Database.</p>
    <p>{{article}}</p>
  </body>
</html>
```

djblog/settings.py:

```py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'], #<--------- Add your own template directory
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

![](https://user-images.githubusercontent.com/32337103/215957683-f601ae19-f429-40bb-a551-b2a0f516294c.png)

</details>

<details>
  <summary>11. Template Inheritance - Using Layouts </summary>

articles/views.py:

```py
from django.shortcuts import render, HttpResponse

# Create your views here.

def article_list(request):
    article = "This is my first article title"
    return render(request, 'articles.html', {'article':article})

```

articles/templates/base.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{% block title %}{% endblock title %}</title>
    {% block style %}{% endblock style %}
  </head>
  <body>
    {% block body %}{% endblock body %}
  </body>
</html>
```

articles/templates/articles.html:

```py
{% extends 'base.html' %}

{% block title %} Article List {% endblock title%}

{%block body %}
<h1>Article List</h1>
<p>This is the place to render articles from Database.</p>
<p>{{article}}</p>
{% endblock body %}

```

![](https://user-images.githubusercontent.com/32337103/215979562-be0db0b4-0836-44bf-b048-91f6218e09b2.png)

</details>

<details>
  <summary>12. Adding CSS and Bootstrap without Static</summary>

articles/templates/base.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{% block title %}{% endblock title %}</title>
    {% block style %}{% endblock style %}
  </head>
  <body>
    {% block body %}{% endblock body %}
  </body>
</html>
```

articles/templates/articles.html:

```py
{% extends 'base.html' %}

{% block title %} Article List {% endblock title%}

{% block style %}
<style>
    .h1-style {
        color: red;
    }
</style>
{% endblock style %}

{%block body %}
<h1 class="h1-style">Article List</h1>
<p>This is the place to render articles from Database.</p>
<p>{{article}}</p>
{% endblock body %}

```

![](https://user-images.githubusercontent.com/32337103/215998482-7e12958b-e985-4576-af4d-6ba1ddb29200.png)

</details>

<details>
  <summary>13. Adding Bootstrap Styles </summary>

```bs
https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
```

```bs
https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.min.js

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.min.js" integrity="sha384-cuYeSxntonz0PPNlHhBs68uyIAVpIIOZZ5JqeqvYYIcEL727kskC66kF92t6Xl2V" crossorigin="anonymous"></script>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
```

articles/templates/base.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{% block title %}{% endblock title %}</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD"
      crossorigin="anonymous"
    />
    {% block style %}{% endblock style %}
  </head>
  <body>
    {% block body %}{% endblock body %}
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```

![](https://user-images.githubusercontent.com/32337103/216303473-6288b019-e6d3-4179-b0ad-db6500e4f1e0.png)

</details>

<details>
  <summary>14. What are signals? </summary>

- Django includes a “signal dispatcher” which helps decoupled applications get notified when actions occur elsewhere in the framework.
- In a nutshell, signals allow certain senders to notify a set of receivers that some action has taken place.
- They’re especially useful when many pieces of code may be interested in the same events.
- For example, a third-party app can register to be notified of settings changes.

```py
from django.apps import AppConfig
from django.core.signals import setting_changed

def my_callback(sender, **kwargs):
    print("Setting changed!")

class MyAppConfig(AppConfig):
    ...

    def ready(self):
        setting_changed.connect(my_callback)
```

```py
from django.core.signals import request_finished

request_finished.connect(my_callback)

def my_callback(sender, **kwargs):
    print("Request finished!")
```

```py
Signal.connect(receiver, sender=None, weak=True, dispatch_uid=None)
```

- receiver – The callback function which will be connected to this signal.
- sender – Specifies a particular sender to receive signals from.
- weak – Django stores signal handlers as weak references by default. Thus, if your receiver is a local function, it may be garbage collected. To prevent this, pass weak=False when you call the signal’s connect() method.
- dispatch_uid – A unique identifier for a signal receiver in cases where duplicate signals may be sent.

Model signals -

- All built-in signals are sent using the send() method.
- The django.db.models.signals module defines a set of signals sent by the model system.
- Signals can make your code harder to maintain.
- Consider implementing a helper method on a custom manager, to both update your models and perform additional logic, or else overriding model methods before using model signals.
- Many of these signals are sent by various model methods like \_init\_\_() or save() that you can override in your own code.
- If you override these methods on your model, you must call the parent class’ methods for these signals to be sent.
- Note also that Django stores signal handlers as weak references by default, so if your handler is a local function, it may be garbage collected.
- To prevent this, pass weak=False when you call the signal’s connect().
- For performance reasons, you shouldn’t perform queries in receivers of pre_init or post_init signals because they would be executed for each instance returned during queryset iteration.

pre_init -

```py
django.db.models.signals.pre_init
```

- Whenever you instantiate a Django model, this signal is sent at the beginning of the model’s \_init\_\_() method.

Arguments sent with this signal:

- sender - The model class that just had an instance created.
- args - A list of positional arguments passed to \_init\_\_().
- kwargs - A dictionary of keyword arguments passed to \_init\_\_().

post_init -

```py
django.db.models.signals.post_init
```

- Like pre_init, but this one is sent when the \_init\_\_() method finishes.

Arguments sent with this signal:

- sender - The model class that just had an instance created.
- instance - The actual instance of the model that’s just been created.

pre_save -

```py
django.db.models.signals.pre_save
```

- This is sent at the beginning of a model’s save() method.

Arguments sent with this signal:

- sender - The model class.
- instance - The actual instance being saved.
- raw - A boolean; True if the model is saved exactly as presented (i.e. when loading a fixture). One should not query/modify other records in the database as the database might not be in a consistent state yet.
- using - The database alias being used.
- update_fields - The set of fields to update as passed to Model.save(), or None if update_fields wasn’t passed to save().

post_save -

```py
django.db.models.signals.post_save
```

- Like pre_save, but sent at the end of the save() method.

Arguments sent with this signal:

- sender - The model class.
- instance - The actual instance being saved.
- created - A boolean; True if a new record was created.
- raw - A boolean; True if the model is saved exactly as presented (i.e. when loading a fixture). One should not query/modify other records in the database as the database might not be in a consistent state yet.
- using - The database alias being used.
- update_fields - The set of fields to update as passed to Model.save(), or None if update_fields wasn’t passed to save().

pre_delete -

```py
django.db.models.signals.pre_delete
```

- Sent at the beginning of a model’s delete() method and a queryset’s delete() method.

Arguments sent with this signal:

- sender - The model class.
- instance - The actual instance being deleted.
- using - The database alias being used.

post_delete -

```py
django.db.models.signals.post_delete
```

- Like pre_delete, but sent at the end of a model’s delete() method and a queryset’s delete() method.

Arguments sent with this signal:

- sender - The model class.
- instance - The actual instance being deleted.
  Note that the object will no longer be in the database, so be very careful what you do with this instance.
- using - The database alias being used.

Examples -

django post_save signals

Let’s have a look on the post_save built-in signal. Its code lives in the django.db.models.signals module. This particular signal fires right after a model finish executing its save method.

```py
from django.contrib.auth.models import User
from django.db.models.signals import post_save

def save_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(save_profile, sender=User)
```

Another way to register a signal, is by using the @receiver decorator:

```py
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
```

```py
from django.dispatch import receiver

from djoser.signals import user_activated

@receiver(user_activated)
def my_handler(user, request):
    # do what you need here
```

More Explanation of Django signals:

- The Django Signals is a strategy to allow decoupled applications to get notified when certain events occur
- There are two key elements in the signals machinary: the senders and the receivers.
- As the name suggests, the sender is the one responsible to dispatch a signal, and the receiver is the one who will receive this signal and then do something.
- A receiver must be a function or an instance method which is to receive signals.
- A sender must either be a Python object, or None to receive events from any sender.
- The connection between the senders and the receivers is done through “signal dispatchers”, which are instances of Signal, via the connect method.
- So to receive a signal, you need to register a receiver function that gets called when the signal is sent by using the Signal.connect() method.

django built-in signals:

- Django provides a set of built-in signals that let user code get notified by Django itself of certain actions.

These include some useful notifications:

- django.db.models.signals.pre_save & django.db.models.signals.post_save:
  Sent before or after a model's save() method is called.

- django.db.models.signals.pre_delete & django.db.models.signals.post_delete:
  Sent before or after a model's delete() method or queryset's delete() method is called.

- django.db.models.signals.m2m_changed :
  Sent when a ManyToManyField on a model is changed.

- django.core.signals.request_started & django.core.signals.request_finished:
  Sent when Django starts or finishes an HTTP request.

</details>

<details>
  <summary>15. Dynamic Slugs with signals </summary>

articles/signals.py:

```py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Article
from django.utils.text import slugify


@receiver(pre_save, sender=Article)
def add_slug(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify (instance.title)
        instance.slug = slug
```

articles/apps.py:

```py
from django.apps import AppConfig


class ArticlesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'articles'

    def ready(self):
        import articles.signals

```

articles/init.py:

```py
default_app_config = "articles.apps.ArticlesConfig"
```

articles/models.py:

```py
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)
    published = models.DateTimeField (auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
```

```py
python manage.py shell
```

```bs
from django.contrib.auth import get_user_model
from articles.models import Article
user = get_user_model()
 u = user.objects.first()
 >>> u
<User: admin>

article = Article(title='the first article',description='this is the article',author=u)
article.save()
```

```bs
>>> Article.objects.all().last()
```

```py
# <Article: the first article>
```

```bs
>>> Article.objects.all().last().__dict__
```

```py
# {'_state': <django.db.models.base.ModelState object at 0x1044d1100>, 'id': 2, 'title': 'the first article', 'description': 'this is the article', 'slug': 'the-first-article', 'published': datetime.datetime(2023, 2, 2, 12, 31, 24, 759019, tzinfo=datetime.timezone.utc), 'author_id': 1}
```

```bs
>>> Article.objects.all().last().slug
```

```py
# 'the-first-article'
```

```bs
>>> Article.objects.get(author=u, title='the first article')
```

```py
# <Article: the first article>
```

![](https://user-images.githubusercontent.com/32337103/216329675-2b6a670c-ed46-4491-b8cd-17571c12f220.png)

![](https://user-images.githubusercontent.com/32337103/216329839-a8c8d2a8-1b71-4c8c-9f7a-b17b7024f80e.png)

</details>

<details>
  <summary>16. Retrieving Data from Model </summary>

articles/views.py:

```py
from django.shortcuts import render, HttpResponse
from .models import Article

# Create your views here.

def article_list(request):
    articles = Article.objects.all().order_by('-published')
    return render(request, 'articles.html', {'articles':articles})

```

articles/templates/base.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{% block title %}{% endblock title %}</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD"
      crossorigin="anonymous"
    />
    {% block style %}{% endblock style %}
  </head>
  <body>
    {% block body %}{% endblock body %}
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```

articles/templates/articles.html:

```py
{% extends 'base.html' %}

{% block title %} Article List {% endblock title%}

{% block style %}
<style>
    .link-style {
        text-decoration: none;
        color:black;
    }
    .link-style:hover {
        text-decoration: none;
        color:gray;
    }
</style>
{% endblock style %}

{%block body %}
<section class="container">
    <h1>Article List</h1>
    {% for article in articles %}
        <span class="badge rounded-pill text-bg-success">Author: {{article.author}}</span>
        <h1><a class="link-style" href="">{{article.title}}</a></h1>
    {% endfor %}
</section>

{% endblock body %}

```

![](https://user-images.githubusercontent.com/32337103/216396649-ec8013a9-c735-4925-836d-5da5514493e8.png)

</details>

<details>
  <summary>17. Adding Bootstrap Navbar </summary>

articles/templates/navbar.html:

```html
<nav class="navbar navbar-expand-lg" style="background-color: #e3f2fd;">
  <div class="container">
    <a class="navbar-brand" href="#">Django-Blog</a>
    <button
      class="navbar-toggler"
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#navbarNavDropdown"
      aria-controls="navbarNavDropdown"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link disabled">Welcome, Adam.</a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Add Article</a>
        </li>
        <li class="nav-item dropdown">
          <a
            class="nav-link dropdown-toggle"
            href="#"
            role="button"
            data-bs-toggle="dropdown"
            aria-expanded="false"
          >
            Profile
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Change Password</a></li>
            <li><a class="dropdown-item" href="#">Logout</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Login</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Register</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
```

articles/templates/base.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{% block title %}{% endblock title %}</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD"
      crossorigin="anonymous"
    />
    {% block style %}{% endblock style %}
  </head>
  <body>
    {% block nav %} {% include 'navbar.html' %} {% endblock nav %} {% block body
    %}{% endblock body %}
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```

articles/templates/articles.html:

```py
{% extends 'base.html' %}

{% block title %} Article List {% endblock title%}

{% block style %}
<style>
    .h1-style {
        margin: 2rem 0;
        color: #2c9df0;
    }
    .link-style {
        text-decoration: none;
        color:black;
    }
    .link-style:hover {
        text-decoration: none;
        color:gray;
    }
</style>
{% endblock style %}

{%block body %}
<section class="container">
    <h1 class="h1-style">Article List</h1>
    {% for article in articles %}
        <span class="badge rounded-pill text-bg-success">Author: {{article.author}}</span>
        <h1><a class="link-style" href="">{{article.title}}</a></h1>
    {% endfor %}
</section>

{% endblock body %}

```

![](https://user-images.githubusercontent.com/32337103/216427207-449b2da7-1cdc-4515-a942-10ed1173046c.png)

</details>

<details>
  <summary>18. Getting the details of Articles </summary>

articles/views.py:

```py
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Article

# Create your views here.

def article_list(request):
    articles = Article.objects.all().order_by('-published')
    return render(request, 'articles.html', {'articles':articles})

def article_details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'details.html', {'article':article})

```

articles/urls.py:

```py
from django.urls import path
from .views import article_list, article_details

urlpatterns = [
    path('articles/', article_list, name='article_list'),
    path('articles/<slug:slug>/', article_details, name='article_details')
]
```

articles/templates/base.html:

```py
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{% block title %}{% endblock title %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    {% block style %}{% endblock style %}
  </head>
  <body>
    {% block nav %}
      {% include 'navbar.html' %}
    {% endblock nav %}
    {% block body %}{% endblock body %}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
  </body>
</html>

```

articles/templates/details.html:

```py
{% extends 'base.html' %}

{% block title %}{% endblock title %}

{% block style %}{% endblock style %}

{% block body %}
    <div class="container mt-4">
        <h1>{{article.title}}</h1>
        <h6>Published {{article.published}} by <i>{{article.author}}</i></h6>
        <br>
        <p>{{article.description}}</p>
    </div>
{% endblock body %}
```

![](https://user-images.githubusercontent.com/32337103/216662571-196525d5-33c2-4fa9-9908-3af531d9de89.png)

</details>

<details>
  <summary>19. Django Forms - Form vs Model Form </summary>

Form -

```py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.
class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
```

```py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)
```

```py
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
```

```py
from django import forms

class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100)
    title = forms.CharField(
        max_length=3,
        widget=forms.Select(choices=TITLE_CHOICES),
    )
    birth_date = forms.DateField(required=False)

class BookForm(forms.Form):
    name = forms.CharField(max_length=100)
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
```

```py
from django.core.mail import send_mail

if form.is_valid():
    subject = form.cleaned_data['subject']
    message = form.cleaned_data['message']
    sender = form.cleaned_data['sender']
    cc_myself = form.cleaned_data['cc_myself']

    recipients = ['info@example.com']
    if cc_myself:
        recipients.append(sender)

    send_mail(subject, message, sender, recipients)
    return HttpResponseRedirect('/thanks/')
```

Example:

```py
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
```

```py
<form action="/your-name/" method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Submit">
</form>
```

```py
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
```

Model Form -

```py
from django.forms import ModelForm
from myapp.models import Article

# Create the form class.
class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['pub_date', 'headline', 'content', 'reporter']

# Creating a form to add an article.
>>> form = ArticleForm()

# Creating a form to change an existing article.
>>> article = Article.objects.get(pk=1)
>>> form = ArticleForm(instance=article)
```

```py
from django.db import models
from django.forms import ModelForm

TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]

class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title', 'birth_date']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors']
```

```py
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import ModelForm

class ArticleForm(ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
```

```py
>>> from myapp.models import Article
>>> from myapp.forms import ArticleForm

# Create a form instance from POST data.
>>> f = ArticleForm(request.POST)

# Save a new Article object from the form's data.
>>> new_article = f.save()

# Create a form to edit an existing Article, but use
# POST data to populate the form.
>>> a = Article.objects.get(pk=1)
>>> f = ArticleForm(request.POST, instance=a)
>>> f.save()
```

```py
# Create a form instance with POST data.
>>> f = AuthorForm(request.POST)

# Create, but don't save the new author instance.
>>> new_author = f.save(commit=False)

# Modify the author in some way.
>>> new_author.some_field = 'some_value'

# Save the new instance.
>>> new_author.save()

# Now, save the many-to-many data for the form.
>>> f.save_m2m()
```

```py
# Create a form instance with POST data.
>>> a = Author()
>>> f = AuthorForm(request.POST, instance=a)

# Create and save the new author instance. There's no need to do anything else.
>>> new_author = f.save()
```

```py
from django.forms import ModelForm

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
```

```py
class PartialAuthorForm(ModelForm):
    class Meta:
        model = Author
        exclude = ['title']
```

```py
author = Author(title='Mr')
form = PartialAuthorForm(request.POST, instance=author)
form.save()

form = PartialAuthorForm(request.POST)
author = form.save(commit=False)
author.title = 'Mr'
author.save()
```

```py
from django.forms import ModelForm, Textarea
from myapp.models import Author

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'title', 'birth_date')
        widgets = {
            'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
```

```py
from django.utils.translation import gettext_lazy as _

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'title', 'birth_date')
        labels = {
            'name': _('Writer'),
        }
        help_texts = {
            'name': _('Some useful help text.'),
        }
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }

```

```py
from django.forms import ModelForm
from myapp.models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['pub_date', 'headline', 'content', 'reporter', 'slug']
        field_classes = {
            'slug': MySlugFormField,
        }
```

```py
from django.forms import CharField, ModelForm
from myapp.models import Article

class ArticleForm(ModelForm):
    slug = CharField(validators=[validate_slug])

    class Meta:
        model = Article
        fields = ['pub_date', 'headline', 'content', 'reporter', 'slug']
```

```py
class Article(models.Model):
    headline = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text='Use puns liberally',
    )
    content = models.TextField()

class ArticleForm(ModelForm):
    headline = MyFormField(
        max_length=200,
        required=False,
        help_text='Use puns liberally',
    )

    class Meta:
        model = Article
        fields = ['headline', 'content']
```

```py
>>> article = Article.objects.get(pk=1)
>>> article.headline
'My headline'
>>> form = ArticleForm(initial={'headline': 'Initial headline'}, instance=article)
>>> form['headline'].value()
'Initial headline'
```

```py
>>> from django.forms import modelform_factory
>>> from myapp.models import Book
>>> BookForm = modelform_factory(Book, fields=("author", "title"))

>>> from django.forms import Textarea
>>> Form = modelform_factory(Book, form=BookForm,
                          widgets={"title": Textarea()})
```

```py
from django import forms

class ProductForm(forms.ModelForm):
  	### here date is the field name in the model ###
    date = forms.DateTimeField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Product
        fields = "__all__"

############## or ##############

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs["class"] = "form-control"

############## or ##############

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
		widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control'})
        }
### you can use the attrs to style the fields ###
```

</details>

<details>
  <summary>20. Create Login System with Django Forms</summary>

articles/forms.py:

```py
from django import forms
from django.utils.html import format_html

class LoginForm (forms.Form):
    username = forms.CharField(
        label='Username',
        initial='',
        required=True,
        max_length=50,
        help_text=format_html('<span class="red">50 characters max.</span>'),
        widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(
        label='Password',
        required=True,
        max_length=50,
        help_text=format_html('<span class="red">50 characters max.</span>'),
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
```

articles/views.py:

```py
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login

from .models import Article
from .forms import LoginForm

# Create your views here.

def article_list(request):
    articles = Article.objects.all().order_by('-published')
    return render(request, 'articles.html', {'articles':articles})

def article_details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'details.html', {'article':article})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is None:
                return HttpResponse("Invalid Login")
            login(request, user)
            return HttpResponse("You are authenticated")
    else:
        form = LoginForm()
        # form.fields['username'].initial = ''
    return render(request, 'account/login.html', {'form':form})

```

articles/templates/account/login.html:

```py
{% extends "base.html" %}

{% block title %}Login{% endblock title %}

{% block style %}
    <style>
        .red {
            color: red;
        }
    </style>
{% endblock style %}

{% block body %}
<div class="container">
    <h1>Login User</h1>
    <p>Use the following form for the login</p>
    <form action="" method="post" novalidate>
        {% csrf_token %}
        {{form.as_p}}
        <input type="submit" value="Login" class="btn btn-success">
    </form>
</div>
{% endblock body %}
```

articles/urls.py:

```py
from django.urls import path
from .views import article_list, article_details, user_login

urlpatterns = [
    path('articles/', article_list, name='article_list'),
    path('articles/<slug:slug>/', article_details, name='article_details'),
    path('login/', user_login, name='login')
]
```

![](https://user-images.githubusercontent.com/32337103/216727185-7ee4ce9e-415d-4133-802a-599418db98f9.png)

</details>

<details>
  <summary>21. Install Django Crispy Forms Library</summary>

```bs
pip install django-crispy-forms
```

```py
# In Settings
INSTALLED_APPS = [
	'crispy_forms',
]

# Very Bottom of Settings
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Top of HTML page
{% load crispy_forms_tags %}

# Apply styling to form
{{ form | crispy }}
```

Crispy-Bootstrap5 -

```bs
### 1- install library ###
pip install crispy-bootstrap5
```

```py
### 2- add the following 2 lines to installed apps in settings.py  ###
"crispy_forms",
"crispy_bootstrap5",

### 3- add the following 2 lines in settings.py ###
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

### 4- now load crispy forms tags and use crispy filter in your html file  ###
{% extends "main/base.html" %}

{% load crispy_forms_tags %}

{% block content %}
<form method="post">
    {% csrf_token %}
    {{form|crispy}}
</form>

{% endblock %}
```

Crispy-Tailwind -

```bs
### install library ###
pip install crispy-tailwind
```

```py
INSTALLED_APPS = (
    ...
    "crispy_forms",
    "crispy_tailwind",
    ...
)

CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"

CRISPY_TEMPLATE_PACK = "tailwind"

### Now load crispy forms tags and use crispy filter in your html file  ###
{% extends "main/base.html" %}
{% load tailwind_filters %}

{% block content %}
<form method="post">
    {% csrf_token %}
    {{form|crispy}}
</form>

{% endblock %}
```

</details>

<details>
  <summary>22. Create Registration System with ModelForm and Crispy Forms</summary>

```py
pip install crispy-bootstrap5
```

```py
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'articles',
    "crispy_forms",
    "crispy_bootstrap5",
]
```

```py
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
```

articles/forms.py:

```py
from django import forms
from django.utils.html import format_html
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        initial='',
        required=True,
        max_length=50,
        help_text=format_html('<span class="red">50 characters max.</span>'),
        widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(
        label='Password',
        required=True,
        max_length=50,
        help_text=format_html('<span class="red">50 characters max.</span>'),
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class UserRegistration(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match')
        else:
            return cd['password2']

```

articles/views.py:

```py
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login

from .models import Article
from .forms import LoginForm, UserRegistration


# Create your views here.

def article_list(request):
    articles = Article.objects.all().order_by('-published')
    return render(request, 'articles.html', {'articles':articles})

def article_details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'details.html', {'article':article})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is None:
                return HttpResponse("Invalid Login")
            login(request, user)
            return HttpResponse("You are authenticated")
    else:
        form = LoginForm()
        # form.fields['username'].initial = ''
    return render(request, 'account/login.html', {'form':form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistration(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'user_form': user_form})
    else:
        user_form = UserRegistration()
    return render(request, 'account/register.html', {'user_form': user_form})

```

articles/urls.py:

```py
from django.urls import path
from .views import article_list, article_details, user_login, register

urlpatterns = [
    path('articles/', article_list, name='article_list'),
    path('articles/<slug:slug>/', article_details, name='article_details'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
]
```

articles/templates/account/register.html:

```py
{% extends "base.html" %}

{% load crispy_forms_tags %}

{% block title %}Registration{% endblock title %}

{% block style %}
    <style>
        .register_style {
            width: 500px;
            margin: auto;
        }
    </style>
{% endblock style %}

{% block body %}
<div class="container my-4 register_style">
    <h3>Register an account </h3>
    <p>Use the following form for Registration.</p>
    <form action="" method="post" novalidate>
        {% csrf_token %}
        {{user_form | crispy}}
        <input type="submit" value="Create Account" class="btn btn-success">
    </form>
</div>
{% endblock body %}

```

articles/templates/account/register_done.html:

```py
{% extends "base.html" %}

{% block title %}Done{% endblock title %}

{% block body %}
<div class="container">
    <h3>Welcome, {{new_user.username}}</h3>
    <p>Your Account has been created, you can <a href="{% url 'login' %}">Login Here</a>.</p>
</div>
{% endblock body %}
```

![](https://user-images.githubusercontent.com/32337103/216756087-a47a6683-66cd-4b10-97d8-6af375e03456.png)

![](https://user-images.githubusercontent.com/32337103/216756103-6ea9235c-3843-440e-9b44-9e1df060e055.png)

![](https://user-images.githubusercontent.com/32337103/216756124-b462ce08-2eca-4933-a324-8314b3e72364.png)

![](https://user-images.githubusercontent.com/32337103/216756132-585e7bd2-6517-4636-8fa6-d690ffa91632.png)

![](https://user-images.githubusercontent.com/32337103/216756149-2055825a-9340-4549-ae57-2fcdb9c30f6d.png)

</details>

<details>
  <summary>23. Use Django Class LoginView for Login </summary>

djblog/articles/urls.py:

```py
from django.urls import path
from .views import article_list, article_details, user_login, register
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('articles/', article_list, name='article_list'),
    path('articles/<slug:slug>/', article_details, name='article_details'),
    # path('login/', user_login, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', register, name='register'),
]
```

djblog/djblog/settings.py:

```py

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

LOGIN_REDIRECT_URL = 'article_list'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
```

djblog/articles/templates/registration/login.html:

```py
{% extends "base.html" %}

{% load crispy_forms_tags %}

{% block title %}Login{% endblock title %}

{% block style %}
    <style>
        .red {
            color: red;
        }
        .login_style {
            width: 500px;
            margin: auto;
        }
    </style>
{% endblock style %}

{% block body %}
<div class="container my-4 login_style">
    <h1>Login User</h1>

    {% if form.errors %}
        <p class="red">Incorrect Username or Password!</p>
    {% else %}
        <p>Use the following form below for the login.</p>
    {% endif  %}
    <form action="" method="post" novalidate>
        {% csrf_token %}
        {{form | crispy}}
        <input type="hidden" name="next" value="{{next}}" />
        <input type="submit" value="Login" class="btn btn-success" />
    </form>
</div>
{% endblock body %}

```

![](https://user-images.githubusercontent.com/32337103/216801732-ff7d1432-44c2-483d-9bda-2304270cdacf.png)

![](https://user-images.githubusercontent.com/32337103/216801734-f5cd4dd0-20c5-4a1b-8e4d-ae1648d73fbe.png)

</details>

<details>
  <summary>24. Use Django Class LogoutView for Logout </summary>

djblog/articles/urls.py:

```py
from django.urls import path
from .views import article_list, article_details, user_login, register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('articles/', article_list, name='article_list'),
    path('articles/<slug:slug>/', article_details, name='article_details'),
    # path('login/', user_login, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]
```

djblog/djblog/settings.py:

```py
# Application definition

INSTALLED_APPS = [
    'articles', # raise app to the first item in the list
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "crispy_forms",
    "crispy_bootstrap5",
]

```

djblog/articles/templates/registration/logged_out.html:

```py
{% extends "base.html" %}

{% block title %}Logged out{% endblock title %}

{% block body %}
<div class="container my-4">
    <p>You have been logged out.</p>
    <p>You can <a href="{% url 'login' %}">Login Back</a>.</p>

</div>
{% endblock body %}
```

![](https://user-images.githubusercontent.com/32337103/216802222-c873061a-a9d4-4b1d-a570-0c3e2e31c3a4.png)

![](https://user-images.githubusercontent.com/32337103/216802235-9e0636d5-1274-4d57-8fdf-a978b0b45608.png)

![](https://user-images.githubusercontent.com/32337103/216802250-ba0c5ea3-1375-40bb-a008-825323e408dc.png)

</details>

<details>
  <summary>25. Restricting/Hiding menu in Navbar with user.is_authenticated </summary>

```html
<li class="nav-item">
  {% if request.user.is_anonymous %}
  <a class="nav-link disabled">Welcome, Visitor.</a>
  {% else %}
  <a class="nav-link disabled">Welcome, {{request.user.username | title}}.</a>
  {% endif %}
</li>
```

djblog/articles/templates/navbar.html:

```py
<nav class="navbar navbar-expand-lg" style="background-color: #e3f2fd;">
    <div class="container">
      <a class="navbar-brand" href="{% url 'article_list' %}">Django-Blog</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav">

            {% if request.user.is_authenticated %}

            <li class="nav-item mx-5">
                <a class="nav-link disabled">Welcome, {{request.user.username | title}}.</a>
            </li>
            <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="{% url 'article_list' %}">Home</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#">Add Article</a>
            </li>
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Profile
                </a>
                <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Change Password</a></li>
                <li><a class="dropdown-item" href="{% url 'logout' %}">Logout</a></li>
                </ul>
            </li>

            {% else %}

            <li class="nav-item mx-5">
              <a class="nav-link disabled">Welcome, Visitor.</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="{% url 'login' %}">Login</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="{% url 'register' %}">Register</a>
            </li>

            {% endif %}
        </ul>
      </div>
    </div>
  </nav>
```

![](https://user-images.githubusercontent.com/32337103/216804185-0b81f25d-d0cb-48f9-8776-25d7c71cde73.png)

![](https://user-images.githubusercontent.com/32337103/216804194-c965dd1a-7e19-4efa-9f4b-67391e5a800a.png)

</details>

<details>
  <summary>26. Password Change with PasswordChangeView </summary>

djblog/articles/urls.py:

```py
from django.urls import path
from .views import article_list, article_details, user_login, register
from django.contrib.auth.views import (LoginView, LogoutView, PasswordChangeView,
                                       PasswordChangeDoneView)

urlpatterns = [
    path('articles/', article_list, name='article_list'),
    path('articles/<slug:slug>/', article_details, name='article_details'),
    # path('login/', user_login, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
]

# from django.urls import path, include
# from django.contrib.auth import views as auth_views
# from . import views
# from django.urls import reverse_lazy

# app_name = 'account'

# urlpatterns = [
#     #Password Changes URLs
#     path('password_change/', auth_views.PasswordChangeView.as_view(
#         success_url=reverse_lazy('account:password_change_done')
#     ), name='password_change'),
#     path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
# ]
```

djblog/articles/templates/registration/password_change_form.html:

```py
{% extends "base.html" %}

{% load crispy_forms_tags %}

{% block title %}Password Change{% endblock title %}

{% block style %}
    <style>
        .register_style {
            width: 500px;
            margin: auto;
        }
    </style>
{% endblock style %}

{% block body %}
<div class="container my-5 register_style">
    <h3>Change Your Password </h3>
    <form action="" method="post" novalidate>
        {% csrf_token %}
        {{form | crispy}}
        <input type="submit" value="Change Password" class="btn btn-success" />
    </form>
</div>
{% endblock body %}
```

djblog/articles/templates/registration/password_change_done.html:

```py
{% extends "base.html" %}

{% block title %}Password Change Done{% endblock title %}

{% block body %}
<div class="container my-5">
    <h3>Password Changed </h3>
    <p>Your password has been changed!</p>
</div>
{% endblock body %}
```

djblog/articles/templates/navbar.html:

```py
<nav class="navbar navbar-expand-lg" style="background-color: #e3f2fd;">
    <div class="container">
      <a class="navbar-brand" href="{% url 'article_list' %}">Django-Blog</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav">

            {% if request.user.is_authenticated %}

            <li class="nav-item mx-5">
                <a class="nav-link disabled">Welcome, {{request.user.username | title}}.</a>
            </li>
            <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="{% url 'article_list' %}">Home</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#">Add Article</a>
            </li>
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Profile
                </a>
                <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="{% url 'password_change' %}">Change Password</a></li>
                <li><a class="dropdown-item" href="{% url 'logout' %}">Logout</a></li>
                </ul>
            </li>

            {% else %}

            <li class="nav-item mx-5">
              <a class="nav-link disabled">Welcome, Visitor.</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="{% url 'login' %}">Login</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="{% url 'register' %}">Register</a>
            </li>

            {% endif %}
        </ul>
      </div>
    </div>
  </nav>
```

![](https://user-images.githubusercontent.com/32337103/216840877-9cba86b3-6a0e-4ea0-b08c-17d7e95f54a8.png)

![](https://user-images.githubusercontent.com/32337103/216840894-cfc8b155-60c1-4589-848b-0cd8cf671cfe.png)

![](https://user-images.githubusercontent.com/32337103/216840932-488bb0dc-f53b-4812-8858-a76d11a2ce75.png)

</details>

<details>
  <summary>27. Add Article with ArticleRegistrationForm </summary>

djblog/articles/forms.py:

```py
from django import forms
from django.utils.html import format_html
from django.contrib.auth.models import User
from .models import Article

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        initial='',
        required=True,
        max_length=50,
        help_text=format_html('<span class="red">50 characters max.</span>'),
        widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(
        label='Password',
        required=True,
        max_length=50,
        help_text=format_html('<span class="red">50 characters max.</span>'),
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class UserRegistration(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match')
        else:
            return cd['password2']

class ArticleRegistrationForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'description')
```

djblog/articles/views.py:

```py
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth import authenticate, login

from .models import Article
from .forms import LoginForm, UserRegistration, ArticleRegistrationForm


# Create your views here.

def article_list(request):
    articles = Article.objects.all().order_by('-published')
    return render(request, 'articles.html', {'articles':articles})

def article_details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'details.html', {'article':article})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is None:
                return HttpResponse("Invalid Login")
            login(request, user)
            return HttpResponse("You are authenticated")
    else:
        form = LoginForm()
        # form.fields['username'].initial = ''
    return render(request, 'account/login.html', {'form':form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistration(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'user_form': user_form})
    else:
        user_form = UserRegistration()
    return render(request, 'account/register.html', {'user_form': user_form})

def article_form(request):
    if not request.user.is_authenticated:
        return redirect('article_list') # <--- Protect Route for Add Article
    if request.method == 'POST':
        article_form = ArticleRegistrationForm(request.POST)

        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_list')
    else:
        article_form = ArticleRegistrationForm()
    return render(request, 'account/add_article.html', {'article_form': article_form})

```

djblog/articles/templates/account/add_article.html:

```py
{% extends "base.html" %}

{% load crispy_forms_tags %}

{% block title %}Add Article{% endblock title %}

{% block style %}
    <style>
        .article_style {
            width: 500px;
            margin: auto;
        }
    </style>
{% endblock style %}

{% block body %}
<div class="container mt-4 article_style">
    <h1>Add Article</h1>
    <p>Use the following form below to add an Article.</p>
    <form action="" method="post" novalidate>
        {% csrf_token %}
        {{article_form | crispy}}
        <input type="submit" value="Add Article" class="btn btn-success">
    </form>
</div>
{% endblock body %}

```

djblog/articles/urls.py:

```py
from django.urls import path
from .views import article_list, article_details, user_login, register, article_form
from django.contrib.auth.views import (LoginView, LogoutView, PasswordChangeView,
                                       PasswordChangeDoneView)

urlpatterns = [
    path('articles/', article_list, name='article_list'),
    path('articles/<slug:slug>/', article_details, name='article_details'),
    path('add/', article_form, name='article_form'), # <---- Add Article
    # path('login/', user_login, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
]

```

![](https://user-images.githubusercontent.com/32337103/216846064-d648a52d-7c9b-4817-913c-74cf64131447.png)

![](https://user-images.githubusercontent.com/32337103/216846089-7d2df4d1-dc28-4d87-82f0-2c88b9ea77cf.png)

</details>

<details>
  <summary>28. Update Article with ArticleUpdateForm </summary>

djblog/articles/forms.py:

```py
from django import forms
from django.utils.html import format_html
from django.contrib.auth.models import User
from .models import Article

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        initial='',
        required=True,
        max_length=50,
        help_text=format_html('<span class="red">50 characters max.</span>'),
        widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(
        label='Password',
        required=True,
        max_length=50,
        help_text=format_html('<span class="red">50 characters max.</span>'),
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class UserRegistration(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match')
        else:
            return cd['password2']

class ArticleRegistrationForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'description')

class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'description')
```

djblog/articles/views.py:

```py
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth import authenticate, login

from .models import Article
from .forms import LoginForm, UserRegistration, ArticleRegistrationForm, ArticleUpdateForm


# Create your views here.

def article_list(request):
    articles = Article.objects.all().order_by('-published')
    return render(request, 'articles.html', {'articles':articles})

def article_details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'details.html', {'article':article})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is None:
                return HttpResponse("Invalid Login")
            login(request, user)
            return HttpResponse("You are authenticated")
    else:
        form = LoginForm()
        # form.fields['username'].initial = ''
    return render(request, 'account/login.html', {'form':form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistration(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'user_form': user_form})
    else:
        user_form = UserRegistration()
    return render(request, 'account/register.html', {'user_form': user_form})

def article_form(request):
    if not request.user.is_authenticated:
        return redirect('article_list') # <--- Protect Route for Add Article
    if request.method == 'POST':
        article_form = ArticleRegistrationForm(request.POST)

        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_list')
    else:
        article_form = ArticleRegistrationForm()
    return render(request, 'account/add_article.html', {'article_form': article_form})


def update_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    form = ArticleUpdateForm(request.POST or None, instance=article)

    if form.is_valid():
        form.save()
        return redirect('article_list')
    return render(request, 'account/update.html', {'form': form})
```

djblog/articles/urls.py:

```py
from django.urls import path
from .views import (article_list, article_details, user_login, register,
                    article_form, update_article)
from django.contrib.auth.views import (LoginView, LogoutView, PasswordChangeView,
                                       PasswordChangeDoneView)

urlpatterns = [
    path('articles/', article_list, name='article_list'),
    path('articles/<slug:slug>/', article_details, name='article_details'),
    path('add/', article_form, name='article_form'),
    path('update/<slug:slug>/', update_article, name='update_article'),
    # path('login/', user_login, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
]

```

djblog/articles/templates/account/update.html:

```py
{% extends "base.html" %}

{% load crispy_forms_tags %}

{% block title %}{{form.title}}{% endblock title %}

{% block style %}
    <style>
        .update_style {
            width: 700px;
            margin: auto;
        }
    </style>
{% endblock style %}

{% block body %}
<div class="container my-4 update_style">
    <h3>Update Article </h3>
    <p>Use the following form to update the Article.</p>
    <form action="" method="post" novalidate>
        {% csrf_token %}
        {{form | crispy}}
        <input type="submit" value="Update Article" class="btn btn-success">
    </form>
</div>
{% endblock body %}

```

djblog/articles/templates/details.html:

```py
{% extends 'base.html' %}

{% block title %}{% endblock title %}

{% block style %}{% endblock style %}

{% block body %}
    <div class="container mt-4">
        <h1>{{article.title}}</h1>
        <h6>Published {{article.published}} by <i>{{article.author}}</i></h6>
        <br>
        <p>{{article.description}}</p>

        {% if request.user == article.author %}
        <a class="btn btn-danger mx-3 mt-3" href="">Delete</a>
        <a class="btn btn-success mx-3 mt-3" href="{% url 'update_article' article.slug %}">Update</a>
        {% endif %}
    </div>
{% endblock body %}
```

![](https://user-images.githubusercontent.com/32337103/216848734-2ec4c3ae-58fc-495a-a5f5-d8289876475e.png)

![](https://user-images.githubusercontent.com/32337103/216848744-bd133608-c568-4229-8e56-53af614f2bf7.png)

![](https://user-images.githubusercontent.com/32337103/216848774-4f3a7fe8-3964-4485-b2a6-b0817697a97c.png)

![](https://user-images.githubusercontent.com/32337103/216848806-06fb89ae-c05b-4199-88e6-33c3b0184dbd.png)

</details>

<details>
  <summary>29. Delete Article </summary>

djblog/articles/views.py:

```py
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth import authenticate, login

from .models import Article
from .forms import LoginForm, UserRegistration, ArticleRegistrationForm, ArticleUpdateForm


def article_list(request):
    articles = Article.objects.all().order_by('-published')
    return render(request, 'articles.html', {'articles':articles})

def article_details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'details.html', {'article':article})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is None:
                return HttpResponse("Invalid Login")
            login(request, user)
            return HttpResponse("You are authenticated")
    else:
        form = LoginForm()
        # form.fields['username'].initial = ''
    return render(request, 'account/login.html', {'form':form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistration(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'user_form': user_form})
    else:
        user_form = UserRegistration()
    return render(request, 'account/register.html', {'user_form': user_form})

def article_form(request):
    if not request.user.is_authenticated:
        return redirect('article_list') # <--- Protect Route for Add Article
    if request.method == 'POST':
        article_form = ArticleRegistrationForm(request.POST)

        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_list')
    else:
        article_form = ArticleRegistrationForm()
    return render(request, 'account/add_article.html', {'article_form': article_form})


def update_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    form = ArticleUpdateForm(request.POST or None, instance=article)

    if form.is_valid():
        form.save()
        return redirect('article_list')
    return render(request, 'account/update.html', {'form': form})

def delete_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article.delete()
    return redirect('article_list')
```

djblog/articles/urls.py:

```py
from django.urls import path
from .views import (article_list, article_details, user_login, register,
                    article_form, update_article, delete_article)
from django.contrib.auth.views import (LoginView, LogoutView, PasswordChangeView,
                                       PasswordChangeDoneView)

urlpatterns = [
    path('articles/', article_list, name='article_list'),
    path('articles/<slug:slug>/', article_details, name='article_details'),
    path('add/', article_form, name='article_form'),
    path('update/<slug:slug>/', update_article, name='update_article'),
    path('delete/<slug:slug>/', delete_article, name='delete_article'),
    # path('login/', user_login, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
]

```

djblog/articles/templates/details.html:

```py
{% extends 'base.html' %}

{% block title %}{% endblock title %}

{% block style %}{% endblock style %}

{% block body %}
    <div class="container mt-4">
        <h1>{{article.title}}</h1>
        <h6>Published {{article.published}} by <i>{{article.author}}</i></h6>
        <br>
        <p>{{article.description}}</p>

        {% if request.user == article.author %}
        <a class="btn btn-danger mx-3 mt-3" href="{% url 'delete_article' article.slug %}">Delete</a>
        <a class="btn btn-success mx-3 mt-3" href="{% url 'update_article' article.slug %}">Update</a>
        {% endif %}
    </div>
{% endblock body %}
```

![](https://user-images.githubusercontent.com/32337103/216925835-de1396f5-a5c9-4639-af24-40fe46c72164.png)

![](https://user-images.githubusercontent.com/32337103/216925897-d5c9a5c9-2ecf-4635-96f7-ec867ed27fc4.png)

![](https://user-images.githubusercontent.com/32337103/216925943-ad390b72-9243-4351-bf99-6530cf64d4cc.png)

</details>

<details>
  <summary>30. Django Pagination </summary>

```bs
def article_list(request):
    article_list = Article.objects.all().order_by('-published')
    paginator = Paginator(article_list, 2)
    page = request.GET.get('page')

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, 'articles.html', {'articles':articles, 'page': page})
```

djblog/articles/views.py:

```py
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Article
from .forms import LoginForm, UserRegistration, ArticleRegistrationForm, ArticleUpdateForm


# Create your views here.

def article_list(request):
    article_list = Article.objects.all().order_by('-published')
    paginator = Paginator(article_list, 2)
    page = request.GET.get('page')

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, 'articles.html', {'articles':articles, 'page': page})

def article_details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'details.html', {'article':article})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is None:
                return HttpResponse("Invalid Login")
            login(request, user)
            return HttpResponse("You are authenticated")
    else:
        form = LoginForm()
        # form.fields['username'].initial = ''
    return render(request, 'account/login.html', {'form':form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistration(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'user_form': user_form})
    else:
        user_form = UserRegistration()
    return render(request, 'account/register.html', {'user_form': user_form})

def article_form(request):
    if not request.user.is_authenticated:
        return redirect('article_list') # <--- Protect Route for Add Article
    if request.method == 'POST':
        article_form = ArticleRegistrationForm(request.POST)

        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_list')
    else:
        article_form = ArticleRegistrationForm()
    return render(request, 'account/add_article.html', {'article_form': article_form})


def update_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    form = ArticleUpdateForm(request.POST or None, instance=article)

    if form.is_valid():
        form.save()
        return redirect('article_list')
    return render(request, 'account/update.html', {'form': form})

def delete_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article.delete()
    return redirect('article_list')
```

djblog/articles/templates/account/pagination.html:

```py
<style type="text/css">
    .paginator,
    .paginator-next,
    .paginator-prev {
        color:white;
        background:black;
        font-size:12px;
        padding: 10px;
        text-decoration: none;
        font-weight: bold;
    }
    .paginator-next {
        border-radius: 0 10px 10px 0;
        background:gray;
    }
    .paginator-prev {
        border-radius: 10px 0 0 10px;
        background:gray;
    }
</style>

<nav aria-label="page navigation example">
    <ul class="pagination" style="margin-top: 30px;">
        <li class="page-item">
            {% if page.has_previous %}
            <a class="paginator-prev" href="?page={{page.previous_page_number}}">Previous</a>
            {% comment %} class="page-link" {% endcomment %}
            {% endif %}
        </li>

        <li class="page-item">
            <a class="paginator">Page {{page.number}} of {{page.paginator.num_pages}}</a>
        </li>

        <li class="page-item" >
            {% if page.has_next %}
            <a class="paginator-next" href="?page={{page.next_page_number}}">Next</a>
            {% endif %}
        </li>
    </ul>
</nav>
```

djblog/articles/templates/articles.html:

```py
{% extends 'base.html' %}

{% block title %} Article List {% endblock title%}

{% block style %}
<style>
    .h1-style {
        margin: 2rem 0;
        color: #2c9df0;
    }
    .link-style {
        text-decoration: none;
        color:black;
    }
    .link-style:hover {
        text-decoration: none;
        color:gray;
    }
</style>
{% endblock style %}

{%block body %}
<section class="container">
    <h1 class="h1-style">Article List</h1>
    {% for article in articles %}
        <span class="badge rounded-pill text-bg-success">Author: {{article.author}}</span>
        <h1><a class="link-style" href="{% url 'article_details' article.slug %}">{{article.title}}</a></h1>
    {% endfor %}

    {% include 'account/pagination.html' with page=articles %}

</section>

{% endblock body %}

```

![](https://user-images.githubusercontent.com/32337103/216942190-717c3fe3-a503-4609-8cb1-acb8abcabf2d.png)

![](https://user-images.githubusercontent.com/32337103/216942243-a567777e-aebf-4eba-9273-0f5daa3b55da.png)

</details>

<details>
  <summary>31. Using Login_required Decorator to restrict access to pages </summary>

djblog/articles/urls.py:

```py
from django.urls import path
from .views import (article_list, article_details, user_login, register,
                    article_form, update_article, delete_article)
from django.contrib.auth.views import (LoginView, LogoutView, PasswordChangeView,
                                       PasswordChangeDoneView)

urlpatterns = [
    path('', article_list, name='article_list'),
    path('articles/<slug:slug>/', article_details, name='article_details'),
    path('add/', article_form, name='article_form'),
    path('update/<slug:slug>/', update_article, name='update_article'),
    path('delete/<slug:slug>/', delete_article, name='delete_article'),
    # path('login/', user_login, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
]

```

```bs
@login_required
def article_form(request):
    # if not request.user.is_authenticated:
    #     return redirect('article_list') # <--- Protect Route for Add Article
    if request.method == 'POST':
        article_form = ArticleRegistrationForm(request.POST)

        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_list')
    else:
        article_form = ArticleRegistrationForm()
    return render(request, 'account/add_article.html', {'article_form': article_form})
```

djblog/articles/views.py:

```py
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from .models import Article
from .forms import LoginForm, UserRegistration, ArticleRegistrationForm, ArticleUpdateForm


# Create your views here.

def article_list(request):
    article_list = Article.objects.all().order_by('-published')
    paginator = Paginator(article_list, 2)
    page = request.GET.get('page')

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, 'articles.html', {'articles':articles, 'page': page})

def article_details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'details.html', {'article':article})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is None:
                return HttpResponse("Invalid Login")
            login(request, user)
            return HttpResponse("You are authenticated")
    else:
        form = LoginForm()
        # form.fields['username'].initial = ''
    return render(request, 'account/login.html', {'form':form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistration(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'user_form': user_form})
    else:
        user_form = UserRegistration()
    return render(request, 'account/register.html', {'user_form': user_form})

@login_required
def article_form(request):
    # if not request.user.is_authenticated:
    #     return redirect('article_list') # <--- Protect Route for Add Article
    if request.method == 'POST':
        article_form = ArticleRegistrationForm(request.POST)

        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_list')
    else:
        article_form = ArticleRegistrationForm()
    return render(request, 'account/add_article.html', {'article_form': article_form})

@login_required
def update_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    form = ArticleUpdateForm(request.POST or None, instance=article)

    if form.is_valid():
        form.save()
        return redirect('article_list')
    return render(request, 'account/update.html', {'form': form})

@login_required
def delete_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article.delete()
    return redirect('article_list')
```

![](https://user-images.githubusercontent.com/32337103/216984681-9345b074-47ba-4a96-8345-924af1f3c498.png)

</details>

<details>
  <summary>32. Deploy Django App to Heroku </summary>

Install Dependencies/Modules:

```py
pip install whitenoise
```

```py
pip install gunicorn
```

Create requirements.txt file:

```py
pip freeze > requirements.txt
```

Configure Settings.py file for Production:

```py
pip install python-dotenv
```

```bs
import os
from dotenv import load_dotenv
load_dotenv()  # loads the configs from .env

if 'SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = False

ALLOWED_HOSTS = [] if DEBUG else ["*"]
```

Make sure staticfiles is configured correctly:

```bs
STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "static/"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# STATIC_ROOT = os.path.join(BASE_DIR, '/staticfiles')
# MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
# STATICFILES_DIRS = [ BASE_DIR / "articles/static"]
```

```bs
{% load static %}
<img src="{% static "images/hi.jpg" %}" alt="Hi!">
```

Enable WhiteNoise:

```bs
MIDDLEWARE = [
    # ...
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # ...
]
```

Add compression and caching support:

```bs
STORAGES = {
    # ...
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
```

```bs
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
```

Using WhiteNoise in development:

- You can disable Django’s static file handling and allow WhiteNoise to take over simply by passing the --nostatic option to the runserver command, but you need to remember to add this option every time you call runserver.
- An easier way is to edit your settings.py file and add whitenoise.runserver_nostatic to the top of your INSTALLED_APPS list:

```bs
INSTALLED_APPS = [
    # ...
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    # ...
]
```

djblog/djblog/settings.py:

```py
"""
Django settings for djblog project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()  # loads the configs from .env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
if 'SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ["SECRET_KEY"]
    # SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [] if DEBUG else ["*"]

# Application definition

INSTALLED_APPS = [
    'articles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "crispy_forms",
    "crispy_bootstrap5",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'djblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

LOGIN_REDIRECT_URL = 'article_list'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "static/"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# STATIC_ROOT = os.path.join(BASE_DIR, '/static')
# MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
# STATICFILES_DIRS = [ BASE_DIR / "articles/static"]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

```

djblog/articles/static/css/index.css:

```css
body {
  background: #ccced6;
  /* background: #000; */
}

.h1-style {
  margin: 2rem 0;
  color: #003d5b;
}

.link-style {
  text-decoration: none;
  color: black;
}

.link-style:hover {
  text-decoration: none;
  color: gray;
}

.article_style {
  width: 500px;
  margin: auto;
}

.register_style {
  width: 500px;
  margin: auto;
}

.update_style {
  width: 700px;
  margin: auto;
}

.red {
  color: red;
}

.paginator,
.paginator-next,
.paginator-prev {
  color: white;
  background: black;
  font-size: 12px;
  padding: 10px;
  text-decoration: none;
  font-weight: bold;
}
.paginator-next {
  border-radius: 0 10px 10px 0;
  background: gray;
}
.paginator-prev {
  border-radius: 10px 0 0 10px;
  background: gray;
}
```

djblog/articles/templates/articles.html

```py
{% extends 'base.html' %}

{% block title %} Article List {% endblock title%}

{% block style %}{% endblock style %}

{%block body %}
<section class="container">
    <h1 class="h1-style">Articles</h1>
    {% for article in articles %}
        <span class="badge rounded-pill text-bg-success">Author: {{article.author}}</span>
        <h1><a class="link-style" href="{% url 'article_details' article.slug %}">{{article.title}}</a></h1>
    {% endfor %}

    {% include 'account/pagination.html' with page=articles %}

</section>

{% endblock body %}
```

Run Collectstatic to collect static files:

```bs
python manage.py collectstatic
```

Install the Heroku CLI:

```bs
brew tap heroku/brew && brew install heroku
brew install heroku
brew upgrade heroku
```

Check Installed Heroku Version:

```bs
heroku --version
```

Login to Heroku Account:

```bs
heroku login
```

Check Heroku Account details:

```bs
heroku auth:whoami
heroku auth:token
heroku authorizations
heroku authorizations:info 059ed27c-d04a-4349-9dba-83a0169277ae
```

```bs
Create .gitignore file
```

```bs
git init
git add .
git commit -m "Initial commit"
```

Create Heroku app:

```bs
heroku create
#Creating app... done, ⬢ rocky-wildwood-72845

heroku create <project-name>
```

Check remote Heroku apps:

```bs
heroku apps
```

Set remote Heroku app location:

```bs
heroku git:remote -a rocky-wildwood-72845
heroku git:remote --app rocky-wildwood-72845
```

```bs
create Procfile
```

Procfile:

```bs
web: gunicorn djblog.wsgi
```

Choose the Python Version (optional):

```bs
echo python-3.9.6 > runtime.txt
git add runtime.txt
git commit -m "Request a specific Python version"
```

Make final commit and push to Heroku:

```bs
git add .
git commit -m "Created Procfile"
git push heroku master
```

```bs
https://rocky-wildwood-72845.herokuapp.com/ deployed to Heroku
```

</details>

<details>
  <summary>33. Protect Secrets with Python-dotenv </summary>

```bs
pip install python-dotenv
```

.env:

```py
SECRET_KEY = 'YOUR SECRET KEY'

GITHUB_KEY = 'YOUR GITHUB KEY'
GITHUB_SECRET = 'YOUR GITHUB SECRET KEY'

GOOGLE_KEY = 'YOUR GOOGLE KEY'
GOOGLE_SECRET = 'YOUR GOOGLE SECRET KEY'
```

settings.py:

```py
import os
from dotenv import load_dotenv
load_dotenv()  # loads the configs from .env

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = str(os.getenv('SECRET_KEY'))
SECRET_KEY = os.environ["SECRET_KEY"]

# social auth configs for github
#SOCIAL_AUTH_GITHUB_KEY = str(os.getenv('GITHUB_KEY'))
#SOCIAL_AUTH_GITHUB_SECRET = str(os.getenv('GITHUB_SECRET'))
SECRET_KEY = os.environ["GITHUB_KEY"]
SECRET_KEY = os.environ["GITHUB_SECRET"]

# social auth configs for google
#SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = str(os.getenv('GOOGLE_KEY'))
#SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = str(os.getenv('GOOGLE_SECRET'))
SECRET_KEY = os.environ["GOOGLE_KEY"]
SECRET_KEY = os.environ["GOOGLE_SECRET"]
```

</details>

<details>
  <summary>34. Set Heroku Config .env Values </summary>

View current configuration values:

```py
heroku config
```

```py
# GITHUB_USERNAME: joesmith
# OTHER_VAR:    production
```

Get a single configuration value:

```py
heroku config:get GITHUB_USERNAME
```

```py
# joesmith
```

Set/add a configuration value:

```py
heroku config:set GITHUB_USERNAME=joesmith
```

```py
# Adding config vars and restarting myapp... done, v12
# GITHUB_USERNAME: joesmith
```

Remove a configuration value:

```py
heroku config:unset GITHUB_USERNAME
```

```py
# Unsetting GITHUB_USERNAME and restarting myapp... done, v13
```

</details>

<details>
  <summary>35. Renaming Heroku Remote App </summary>

```py
heroku apps:rename newname
```

```py
# Renaming oldname to newname... done
# http://newname.herokuapp.com/ | git@herokuapp.com:newname.git
# Git remote heroku updated
```

```py
heroku apps:rename newname --app oldname
```

```py
# http://newname.herokuapp.com/ | git@herokuapp.com:newname.git
```

Updating Git remotes:

```py
git remote rm heroku
heroku git:remote -a newname
```

```py
# If you're working on the heroku remote (default):
heroku git:remote -a [app name]

# If you want to specify a different remote, use the -r argument:
heroku git:remote -a [app name] -r [remote]

# Delete the current remote reference with
git remote rm origin

# Add the new remote
git remote add origin <URL to new heroku app>

# push to new domain
git push -u origin master

# View Remote URLs
git remote -v

# Remove Heroku remote URL
git remote rm heroku

# Set new Heroku URL
heroku git:remote -a  ############

git remote set-url heroku <repo git>
git remote -v
```

</details>

<details>
  <summary>36. Migrating to PostgreSQL </summary>

Install Python Adapter for Database Migration:

```py
pip install psycopg2
python -m pip install psycopg2-binary
```

```py
pip freeze > requirements.txt
```

Install Postgresql:

```py
https://postgresapp.com/
```

Install pgAdmin:

```py
https://www.pgadmin.org/
```

```py
psql --version
psql -U postgres

# List Databases:
\list
\l

# List Tables:
\dt

# Quit terminal:
\q
```

Settings for Postgresql connection:

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_user_password',
        'HOST': '',
        'PORT': 'db_port_number',
    }
}
```

```py
# Just after the default DATABASE configuration add this in settings.py

POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")

POSTGRES_READY = (
    POSTGRES_DB is not None
    and POSTGRES_PASSWORD is not None
    and POSTGRES_USER is not None
    and POSTGRES_HOST is not None
    and POSTGRES_PORT is not None
)

if POSTGRES_READY:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": POSTGRES_DB,
            "USER": POSTGRES_USER,
            "PASSWORD": POSTGRES_PASSWORD,
            "HOST": POSTGRES_HOST,
            "PORT": POSTGRES_PORT,
        }
    }

```

Settings for LOCAL Postgresql connection:

```py
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }

    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
```

```py
python manage.py createsuperuser
```

![](https://user-images.githubusercontent.com/32337103/217245031-7cf49cc6-bfe2-400b-a536-b6e3fcdda90c.png)
![](https://user-images.githubusercontent.com/32337103/217245135-7b117e31-d69b-47d5-9e39-62afbfb7ea5f.png)

Settings for REMOTE Postgresql connection (with Railway):

```py
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }

    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("PGDATABASE"),
        'USER': os.environ.get("PGUSER"),
        'PASSWORD': os.environ.get("PGPASSWORD"),
        'HOST':  os.environ.get("PGHOST"),
        'PORT': os.environ.get("PGPORT"),
    }
}
```

```py
python manage.py migrate
```

```py
git add .
git commit -m "Connected to Postgresql"
git push heroku master
```

</details>

+BUILDING QUESTION AND ANSWER APP IN DJANGO

<details>
  <summary>37. Introduction </summary>

Install Venv:

```py
python -m venv venv_djqa
source venv_djqa/bin/activate
```

Install Django

```py
pip install Django
```

Upgrade pip:

```py
python -m pip install --upgrade pip
```

Create Django Project:

```py
django-admin startproject djqa .
```

Create Users app:

```py
python manage.py startapp users
```

</details>

<details>
  <summary>38. Create CustomUser Model </summary>

djqa/users/models.py:

```py
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    pass
```

djqa/djqa/settings.py:

```py
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
]

#Set Model User
AUTH_USER_MODEL = 'users.CustomUser'

```

Make migrations:

```py
python manage.py makemigrations

```

```py
# Migrations for 'users':
#   users/migrations/0001_initial.py
#     - Create model CustomUser
```

Run Migration:

```py
python manage.py migrate
```

```py
# Operations to perform:
#   Apply all migrations: admin, auth, contenttypes, sessions, users
# Running migrations:
#   Applying contenttypes.0001_initial... OK
#   Applying contenttypes.0002_remove_content_type_name... OK
#   Applying auth.0001_initial... OK
#   Applying auth.0002_alter_permission_name_max_length... OK
#   Applying auth.0003_alter_user_email_max_length... OK
#   Applying auth.0004_alter_user_username_opts... OK
#   Applying auth.0005_alter_user_last_login_null... OK
#   Applying auth.0006_require_contenttypes_0002... OK
#   Applying auth.0007_alter_validators_add_error_messages... OK
#   Applying auth.0008_alter_user_username_max_length... OK
#   Applying auth.0009_alter_user_last_name_max_length... OK
#   Applying auth.0010_alter_group_name_max_length... OK
#   Applying auth.0011_update_proxy_permissions... OK
#   Applying auth.0012_alter_user_first_name_max_length... OK
#   Applying users.0001_initial... OK
#   Applying admin.0001_initial... OK
#   Applying admin.0002_logentry_remove_auto_add... OK
#   Applying admin.0003_logentry_add_action_flag_choices... OK
#   Applying sessions.0001_initial... OK
```

Run server:

```py
python manage.py runserver
```

```py
# Watching for file changes with StatReloader
# Performing system checks...

# System check identified no issues (0 silenced).
# February 10, 2023 - 19:58:17
# Django version 4.1.6, using settings 'djqa.settings'
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CONTROL-C.
```

![](https://user-images.githubusercontent.com/32337103/218186250-0178f098-5e14-4ebb-b34f-da5eb23d043f.png)

Create Super User:

```py
python manage.py createsuperuser
```

```py
# Username: admin
# Email address: admin@gmail.com
# Password:
# Password (again):
# This password is too short. It must contain at least 8 characters.
# This password is too common.
# This password is entirely numeric.
# Bypass password validation and create user anyway? [y/N]: y
# Superuser created successfully.
```

http://127.0.0.1:8000/admin:

![](https://user-images.githubusercontent.com/32337103/218187218-279ccd88-243a-478c-b682-84ede19e3b5a.png)

![](https://user-images.githubusercontent.com/32337103/218187292-cfc00c72-3d3f-49c6-961a-c5476d028ec2.png)

Add CustomUser Model to Admin -

djqa/users/admin.py:

```py
from django.contrib import admin
from .models import CustomUser

# Register your models here.
admin.site.register(CustomUser)
```

![](https://user-images.githubusercontent.com/32337103/218187813-f2473d5d-3f35-4cc3-9937-f701f770d1da.png)

![](https://user-images.githubusercontent.com/32337103/218188052-fc6cbcaa-3bb9-4d80-ad17-273fa9e996d9.png)

</details>

<details>
  <summary>39. Create Questions App</summary>

```py
python manage.py startapp questions
```

djqa/djqa/settings.py:

```py
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'questions',
]
```

</details>

<details>
  <summary>40. Create Question and Answer Models </summary>

djqa/questions/models.py:

```py
from django.db import models
from django.conf import settings

# Create your models here.
class Question(models.Model):
    title= models.CharField(max_length=250)
    body = models.TextField()
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='questions')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    description = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username
```

Make Migrations:

```py
python manage.py makemigrations
```

```py
# Migrations for 'questions':
#   questions/migrations/0001_initial.py
#     - Create model Question
#     - Create model Answer
```

Run Migration:

```py
python manage.py migrate
```

```py
# Operations to perform:
#   Apply all migrations: admin, auth, contenttypes, questions, sessions, users
# Running migrations:
#   Applying questions.0001_initial... OK
```

Add Models to Admin -

djqa/questions/admin.py:

```py
from django.contrib import admin
from .models import Question, Answer

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
```

![](https://user-images.githubusercontent.com/32337103/218191785-7d0e6793-1bc1-4df2-872b-ed70301fe856.png)

</details>

<details>
  <summary>41. Create dynamic Slugs for Questions with signals </summary>

djqa/questions/signals.py:

```py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Question
from django.utils.text import slugify

@receiver(pre_save, sender=Question)
def add_slug(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.title)
        instance.slug = slug
```

djqa/questions/apps.py:

```py
from django.apps import AppConfig


class QuestionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'questions'

    def ready(self):
        import questions.signals
```

djqa/questions/init.py:

```py
default_app_config = "questions.apps.QuestionsConfig"
```

Open Python Shell:

```py
python manage.py shell
```

```py
# from django.contrib.auth import get_user_model
# user = get_user_model()
# u = user.objects.first()
# from questions.models import Question
# q = Question(title = "This is my question", body = 'This is the question body', author=u)
# q.save()
# exit()
```

```py
python manage.py runserver
```

![](https://user-images.githubusercontent.com/32337103/218195342-7b5c8e51-91c1-478d-be6d-b083ca31d9fd.png)

![](https://user-images.githubusercontent.com/32337103/218195435-74ce77ab-b58c-4086-a3c6-b206ef733573.png)

</details>

<details>
  <summary>42. Render Question List Page </summary>

djqa/djqa/urls.py:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('questions.urls'))
]

```

djqa/questions/urls.py:

```py
from django.urls import path
from .views import question_list

urlpatterns = [
    path('question/', question_list, name='question_list')
]
```

djqa/questions/views.py:

```py
from django.shortcuts import render
from .models import Question

# Create your views here.
def question_list(request):
    question_list = Question.objects.all().order_by('-created_at')
    return render(request, 'questionList.html', {'question_list': question_list})

```

djqa/templates/questionList.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Question List</title>
  </head>
  <body>
    <h1>Question 1</h1>
    <p>What is the Capital of Nigeria?</p>
  </body>
</html>
```

djqa/djqa/settings.py:

```py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

![](https://user-images.githubusercontent.com/32337103/218429996-5ff4a211-a5bf-4c6b-8adf-83d382e75b91.png)

</details>

<details>
  <summary>43. Modify Template with Bootstrap </summary>

djqa/templates/base.html:

```py
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock title %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    {% block style %}{% endblock style %}
</head>
<body>
    {% block body %}{% endblock body %}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
</body>
</html>
```

djqa/templates/questionList.html:

```py
{% extends 'base.html' %}

{% block title %}Question List{% endblock title %}

{% block style%}{% endblock style%}

{% block body%}
<div class="container">
{% for question in question_list %}
    <div class="card mt-3 shadow">
        <div class="card-body">
            <h5 class="card-title"><a href="">{{question.title}}</a></h5>
            <p class="card-text">{{question.body}}</p>
        </div>
    </div>
{% endfor %}
</div>
{% endblock body%}
<body>

```

![](https://user-images.githubusercontent.com/32337103/218435813-7cdd2c49-7472-479c-868f-7d0874910c8b.png)

![](https://user-images.githubusercontent.com/32337103/218434831-94970245-a6bb-4e5d-93cb-dfd362ed3c86.png)

djqa/templates/questionList.html:

```py
{% extends 'base.html' %}

{% block title %}Question List{% endblock title %}

{% block style%}
    <style>
        .link-style {
            text-decoration:none;
            color: #00798C;
        }
        .link-style:hover {
            text-decoration:none;
            color:gray;
        }
    </style>
{% endblock style%}

{% block body%}
<div class="container">
{% for question in question_list %}
    <div class="card mt-3 shadow">
        <div class="card-body">
            <h5 class="card-title"><a class="link-style" href="">{{question.title}}</a></h5>
            <p class="card-text">{{question.body}}</p>
        </div>
        <div class="card-footer">
            <div class="row">
                <div class="col col-md-auto">
                    Posted By: {{question.author.username}}
                </div>
                <div class="col col-md-auto">
                    Answers: {{question.answers.count}}
                </div>
            </div>
        </div>
    </div>
{% endfor %}
</div>
{% endblock body%}
<body>

```

djqa/questions/models.py:

```py
from django.db import models
from django.conf import settings

# Create your models here.
class Question(models.Model):
    title= models.CharField(max_length=250)
    body = models.TextField()
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='questions')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    description = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username
```

![](https://user-images.githubusercontent.com/32337103/218442066-0780b24e-5783-4d8f-8efd-6bd8e6732afb.png)

</details>

<details>
  <summary>44. Adding Bootstrap Navbar </summary>

djqa/templates/navbar.html:

```py
<style>
    .text-style {
        font-size: 30px !important;
        font-family: fantasy !important;
        color: brown !important;
        font-weight: bold !important;
    }
</style>

<nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand text-style" href="#">Question Hub</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link disabled">Welcome, Alex.</a>
          </li>
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>

          <li class="nav-item">
            <a class="nav-link" href="#">Add Question</a>
          </li>

          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Profile
            </a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">Change Password</a></li>
              <li><a class="dropdown-item" href="#">Change Account</a></li>
              <li><a class="dropdown-item" href="#">Question & Answer</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#">Logout</a></li>
            </ul>
          </li>

          <li class="nav-item">
            <a class="nav-link" href="#">Login</a>
          </li>

          <li class="nav-item">
            <a class="nav-link" href="#">Register</a>
          </li>
        </ul>
        <form class="d-flex" role="search">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success" type="submit">Search</button>
        </form>
      </div>
    </div>
  </nav>
```

djqa/templates/base.html:

```py
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock title %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    {% block style %}{% endblock style %}
</head>
<body>
    {% include 'navbar.html' %}
    {% block body %}{% endblock body %}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
</body>
</html>
```

![](https://user-images.githubusercontent.com/32337103/218559989-e236eedd-ccfb-4e41-be4b-0e2c43768965.png)

</details>

<details>
  <summary>45. Create Details Page for Questions </summary>

Cloud-Django/djqa/questions/urls.py:

```py
from django.urls import path
from .views import question_list, question_details

urlpatterns = [
    path('question/', question_list, name='question_list'),
    path('question/<slug:slug>/', question_details, name='question_details')
]
```

Cloud-Django/djqa/questions/views.py:

```py
from django.shortcuts import render, get_object_or_404
from .models import Question

# Create your views here.
def question_list(request):
    question_list = Question.objects.all().order_by('-created_at')
    return render(request, 'questionList.html', {'question_list': question_list})

def question_details(request, slug):
    question = get_object_or_404(Question, slug=slug )
    return render(request, 'questionDetails.html', {'question': question})
```

Cloud-Django/djqa/templates/questionDetails.html:

```py
{% extends 'base.html' %}

{% block title %} Question Details {% endblock title %}

{% block body %}
<div class="container mt-3">
    <h1>{{question.title}}</h1>
    <p>{{question.body}}</p>
    <h6>
        Posted By: <i>{{question.author}} </i>
    </h6>
    <p>Published {{question.created_at}}</p>
</div>
{% endblock body %}
```

Cloud-Django/djqa/templates/questionList.html:

```htmlx
<h5 class="card-title"><a class="link-style" href="{% url 'question_details' question.slug %}">{{question.title}}</a></h5>
```

```py
{% extends 'base.html' %}

{% block title %}Question List{% endblock title %}

{% block style%}
    <style>
        .link-style {
            text-decoration:none;
            color: #00798C;
        }
        .link-style:hover {
            text-decoration:none;
            color:gray;
        }
    </style>
{% endblock style%}

{% block body%}
<div class="container">
{% for question in question_list %}
    <div class="card mt-3 shadow">
        <div class="card-body">
            <h5 class="card-title"><a class="link-style" href="{% url 'question_details' question.slug %}">{{question.title}}</a></h5>
            <p class="card-text">{{question.body}}</p>
        </div>
        <div class="card-footer">
            <div class="row">
                <div class="col col-md-auto">
                    Posted By: {{question.author.username}}
                </div>
                <div class="col col-md-auto">
                    Answers: {{question.answers.count}}
                </div>
            </div>
        </div>
    </div>
{% endfor %}
</div>
{% endblock body%}
<body>

```

![](https://user-images.githubusercontent.com/32337103/218563663-b9e44fad-01bc-4ca4-b387-5bd0293d56f4.png)

![](https://user-images.githubusercontent.com/32337103/218563694-58952ba7-0bc1-4a9e-8334-c963858e6025.png)

![](https://user-images.githubusercontent.com/32337103/218563733-d484e09c-139d-48fe-a95b-a7eef7b4adc7.png)

</details>

<details>
  <summary>46. Create Login Page </summary>

```bs
pip install django-crispy-forms
```

```bs
pip install crispy-bootstrap5
```

Cloud-Django/djqa/djqa/settings.py:

```py
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "crispy_forms",
    "crispy_bootstrap5",
    'users',
    'questions',
]


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

LOGIN_REDIRECT_URL = 'question_list'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

```

Cloud-Django/djqa/users/urls.py:

```py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
```

Cloud-Django/djqa/djqa/urls.py:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('questions.urls')),
    path('', include('users.urls'))
]

```

Cloud-Django/djqa/templates/navbar.html:

```bs
<li><a class="dropdown-item" href="{% url 'logout' %}">Logout</a></li>

<a class="nav-link" href="{% url 'login' %}">Login</a>
```

```py
<style>
    .text-style {
        font-size: 30px !important;
        font-family: fantasy !important;
        color: brown !important;
        font-weight: bold !important;
    }
</style>

<nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand text-style" href="#">Question Hub</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link disabled">Welcome, Alex.</a>
          </li>
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>

          <li class="nav-item">
            <a class="nav-link" href="#">Add Question</a>
          </li>

          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Profile
            </a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">Change Password</a></li>
              <li><a class="dropdown-item" href="#">Change Account</a></li>
              <li><a class="dropdown-item" href="#">Question & Answer</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="{% url 'logout' %}">Logout</a></li>
            </ul>
          </li>

          <li class="nav-item">
            <a class="nav-link" href="{% url 'login' %}">Login</a>
          </li>

          <li class="nav-item">
            <a class="nav-link" href="#">Register</a>
          </li>
        </ul>
        <form class="d-flex" role="search">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success" type="submit">Search</button>
        </form>
      </div>
    </div>
  </nav>
```

Cloud-Django/djqa/templates/registration/login.html:

```py
{% extends 'base.html' %}
{% load crispy_forms_tags %}


{% block title %} Login {% endblock title %}

{% block style %}
<style>
    .login-style {
        width:500px;
        height: auto;
    }
</style>
{% endblock style %}

{% block body %}
<div class="container mt-4 login-style">
    <h1>Login User</h1>

    <form action="" method="post" novalidate>
        {% csrf_token %}
        {{form | crispy}}

        <input type="hidden" name="text" value="{{next}}"/>
        <input type="submit" value="Login" class="btn btn-success">
    </form>
</div>
{% endblock body %}
```

![](https://user-images.githubusercontent.com/32337103/219012659-9023e028-b4c6-489a-9e69-fd2f21199a41.png)

![](https://user-images.githubusercontent.com/32337103/219013062-8b08cc85-0b54-48d5-99a8-97bf5e20b581.png)

</details>

<details>
  <summary>47. Create Logout Page </summary>

Cloud-Django/djqa/templates/registration/logged_out.html:

```py
{% extends 'base.html' %}

{% block title %} Logout {% endblock title %}

{% block style %}
<style>
    .login-style {
        width:500px;
        height: auto;
    }
</style>
{% endblock style %}

{% block body %}
<div class="container">
    <p>You have been logout. You can <a class="" href="{% url 'login' %}">Login Here</a>.</p>
</div>
{% endblock body %}
```

![](https://user-images.githubusercontent.com/32337103/219015533-9cf4daf1-a9d8-4258-8d17-ca4b81b7d90b.png)

</details>

<details>
  <summary>48. Create User Registration Page </summary>

Cloud-Django/djqa/questions/forms.py:

```py
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
```

Cloud-Django/djqa/questions/views.py:

```py
from django.shortcuts import render, get_object_or_404
from .models import Question
from .forms import UserRegistrationForm

# Create your views here.
def question_list(request):
    question_list = Question.objects.all().order_by('-created_at')
    return render(request, 'questionList.html', {'question_list': question_list})

def question_details(request, slug):
    question = get_object_or_404(Question, slug=slug )
    return render(request, 'questionDetails.html', {'question': question})

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register_done.html', {'user_form':user_form})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form':user_form})
```

Cloud-Django/djqa/templates/register.html:

```py
{% extends 'base.html' %}
{% load crispy_forms_tags %}


{% block title %} Register {% endblock title %}

{% block style %}
<style>
    .register-style {
        width:500px;
        height: auto;
    }
</style>
{% endblock style %}

{% block body %}
<div class="container mt-4 register-style">
    <h3>Register an account</h3>
    <form action="" method="post" novalidate>
        {% csrf_token %}
        {{user_form | crispy}}

        <input type="submit" value="Create Account" class="btn btn-success">
    </form>
</div>
{% endblock body %}
```

Cloud-Django/djqa/templates/register_done.html:

```py
{% extends 'base.html' %}

{% block title %} Register Done {% endblock title %}

{% block body %}
<div class="container mt-4">
    <p>Your account has been created, You can <a href="{% url 'login' %}">Login HERE</a>.</p>

</div>
{% endblock body %}
```

Cloud-Django/djqa/questions/urls.py:

```py
from django.urls import path
from .views import question_list, question_details, register

urlpatterns = [
    path('question/', question_list, name='question_list'),
    path('question/<slug:slug>/', question_details, name='question_details'),
    path('register/', register, name='register'),
]
```

Cloud-Django/djqa/templates/navbar.html:

```bsx
<a class="nav-link disabled">Welcome, {{request.user.username | title}}.</a>

<li class="nav-item">
  <a class="nav-link" href="{% url 'register' %}">Register</a>
</li>

```

```py
<style>
    .text-style {
        font-size: 30px !important;
        font-family: fantasy !important;
        color: brown !important;
        font-weight: bold !important;
    }
</style>

<nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand text-style" href="#">Question Hub</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link disabled">Welcome, {{request.user.username | title}}.</a>
          </li>
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>

          <li class="nav-item">
            <a class="nav-link" href="#">Add Question</a>
          </li>

          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Profile
            </a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">Change Password</a></li>
              <li><a class="dropdown-item" href="#">Change Account</a></li>
              <li><a class="dropdown-item" href="#">Question & Answer</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="{% url 'logout' %}">Logout</a></li>
            </ul>
          </li>

          <li class="nav-item">
            <a class="nav-link" href="{% url 'login' %}">Login</a>
          </li>

          <li class="nav-item">
            <a class="nav-link" href="{% url 'register' %}">Register</a>
          </li>
        </ul>
        <form class="d-flex" role="search">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success" type="submit">Search</button>
        </form>
      </div>
    </div>
  </nav>
```

![](https://user-images.githubusercontent.com/32337103/219070714-81862d60-505b-49f3-b4c6-197b254bd1ab.png)

![](https://user-images.githubusercontent.com/32337103/219070916-38b420bf-4df7-4184-9ca7-ce76c64e5e76.png)

![](https://user-images.githubusercontent.com/32337103/219070981-20e819ec-b57b-4002-a86e-15dd5c8a31bf.png)

![](https://user-images.githubusercontent.com/32337103/219071080-e21a3ed8-3acc-4337-a798-ae5c69914e98.png)

</details>

<details>
  <summary>49. Restricting Navbar from unauthorized Users </summary>

Cloud-Django/djqa/templates/navbar.html:

```bsx
{% if request.user.is_authenticated %}
---
{% else %}
---
{% endif %}
```

```py
<style>
    .text-style {
        font-size: 30px !important;
        font-family: fantasy !important;
        color: brown !important;
        font-weight: bold !important;
    }
</style>

<nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand text-style" href="{% url 'question_list' %}">Question Hub</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">

          {% if request.user.is_authenticated %}

          <li class="nav-item mx-3">
            <a class="nav-link disabled">Welcome, {{request.user.username | title}}.</a>
          </li>

          <form class="d-flex" role="search">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button>
          </form>

          <li class="nav-item mx-3">
            <a class="nav-link active" aria-current="page" href="{% url 'question_list' %}">Home</a>
          </li>

          <li class="nav-item">
            <a class="nav-link" href="#">Add Question</a>
          </li>

          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Profile
            </a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">Change Password</a></li>
              <li><a class="dropdown-item" href="#">Change Account</a></li>
              <li><a class="dropdown-item" href="#">Question & Answer</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="{% url 'logout' %}">Logout</a></li>
            </ul>
          </li>

          {% else %}

          <li class="nav-item">
            <a class="nav-link" href="{% url 'login' %}">Login</a>
          </li>

          <li class="nav-item">
            <a class="nav-link" href="{% url 'register' %}">Register</a>
          </li>

          {% endif %}
        </ul>

      </div>
    </div>
  </nav>
```

![](https://user-images.githubusercontent.com/32337103/219075501-966aa47a-a128-43a4-9160-ace0525f561a.png)

![](https://user-images.githubusercontent.com/32337103/219075571-ffda94c6-7f0f-4a37-9bc8-304cef526529.png)

![](https://user-images.githubusercontent.com/32337103/219075682-96850d19-e4ba-400c-8841-7ad2e10f6a68.png)

</details>

<details>
  <summary>50. Creating Questions </summary>

Cloud-Django/djqa/questions/forms.py:

```py
from django import forms
from django.contrib.auth import get_user_model
from .models import Question

User = get_user_model()

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class QuestionRegistrationForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'body',)
```

Cloud-Django/djqa/questions/models.py:

```py
from django.db import models
from django.conf import settings

# Create your models here.
class Question(models.Model):
    title= models.CharField(max_length=250)
    body = models.TextField()
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='questions')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    description = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username
```

Cloud-Django/djqa/questions/views.py:

```py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from .forms import UserRegistrationForm, QuestionRegistrationForm

# Create your views here.
def question_list(request):
    question_list = Question.objects.all().order_by('-created_at')
    return render(request, 'questionList.html', {'question_list': question_list})

def question_details(request, slug):
    question = get_object_or_404(Question, slug=slug )
    return render(request, 'questionDetails.html', {'question': question})

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register_done.html', {'user_form':user_form})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form':user_form})

def create_question(request):
    if request.method == "POST":
        question_form = QuestionRegistrationForm(request.POST)

        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.author = request.user
            question = question_form.save()
            return redirect('question_list')
    else:
        question_form = QuestionRegistrationForm()
    return render(request, 'add_question.html', {'question_form': question_form})

```

Cloud-Django/djqa/templates/add_question.html:

```py
{% extends 'base.html' %}
{% load crispy_forms_tags %}


{% block title %} Add Question {% endblock title %}

{% block style %}
<style>
    .question-style {
        width:700px;
        height: auto;
    }
</style>
{% endblock style %}

{% block body %}
<div class="container mt-5 question-style">
    <h3>Add Question</h3>

    <form action="" method="post" novalidate>
        {% csrf_token %}
        {{question_form | crispy}}

        <input type="submit" value="Add Question" class="btn btn-success">
    </form>
</div>
{% endblock body %}
```

Cloud-Django/djqa/questions/urls.py:

```py
from django.urls import path
from .views import question_list, question_details, register, create_question

urlpatterns = [
    path('question/', question_list, name='question_list'),
    path('question/<slug:slug>/', question_details, name='question_details'),
    path('register/', register, name='register'),
    path('add/', create_question, name='create_question'),
]
```

Cloud-Django/djqa/templates/navbar.html:

```py
<style>
    .text-style {
        font-size: 30px !important;
        font-family: fantasy !important;
        color: brown !important;
        font-weight: bold !important;
    }
</style>

<nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand text-style" href="{% url 'question_list' %}">Question Hub</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">

          {% if request.user.is_authenticated %}

          <li class="nav-item mx-3">
            <a class="nav-link disabled">Welcome, {{request.user.username | title}}.</a>
          </li>

          <form class="d-flex" role="search">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button>
          </form>

          <li class="nav-item mx-3">
            <a class="nav-link active" aria-current="page" href="{% url 'question_list' %}">Home</a>
          </li>

          <li class="nav-item">
            <a class="nav-link" href="{% url 'create_question' %}">Add Question</a>
          </li>

          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Profile
            </a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">Change Password</a></li>
              <li><a class="dropdown-item" href="#">Change Account</a></li>
              <li><a class="dropdown-item" href="#">Question & Answer</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="{% url 'logout' %}">Logout</a></li>
            </ul>
          </li>

          {% else %}

          <li class="nav-item">
            <a class="nav-link" href="{% url 'login' %}">Login</a>
          </li>

          <li class="nav-item">
            <a class="nav-link" href="{% url 'register' %}">Register</a>
          </li>

          {% endif %}
        </ul>

      </div>
    </div>
  </nav>
```

![](https://user-images.githubusercontent.com/32337103/219086040-acc824f0-239a-4f15-add4-2ac761bf00e7.png)

![](https://user-images.githubusercontent.com/32337103/219086151-9f413ecd-2696-40f7-8430-34b5e14b1682.png)

![](https://user-images.githubusercontent.com/32337103/219086289-0718d64e-04a4-4a83-9531-9354b5b97205.png)

</details>

<details>
  <summary>51. Listing Answers </summary>

Cloud-Django/djqa/questions/views.py:

```bsx
def question_details(request, slug):
  question = get_object_or_404(Question, slug=slug)
  answer_list = Answer.objects.filter(question=question)
  return render(request, 'questionDetails.html', {'question': question, 'answer_list': answer_list})
```

```py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from .forms import UserRegistrationForm, QuestionRegistrationForm

# Create your views here.
def question_list(request):
    question_list = Question.objects.all().order_by('-created_at')
    return render(request, 'questionList.html', {'question_list': question_list})

def question_details(request, slug):
    question = get_object_or_404(Question, slug=slug)
    answer_list = Answer.objects.filter(question=question)
    return render(request, 'questionDetails.html', {'question': question, 'answer_list': answer_list})

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register_done.html', {'user_form':user_form})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form':user_form})

def create_question (request):
    if request.method == "POST":
        question_form = QuestionRegistrationForm(request.POST)

        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.author = request.user
            question = question_form.save()
            return redirect('question_list')
    else:
        question_form = QuestionRegistrationForm()
    return render(request, 'add_question.html', {'question_form': question_form})

```

Cloud-Django/djqa/questions/models.py:

```py
from django.db import models
from django.conf import settings

# Create your models here.
class Question(models.Model):
    title= models.CharField(max_length=250)
    body = models.TextField()
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='questions')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    description = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.question.title}"
```

Cloud-Django/djqa/templates/questionDetails.html:

```py
{% extends 'base.html' %}

{% block title %} Question Details {% endblock title %}

{% block style %}
<style>
    .author {
        color: gray;
    }
    .answer {
        color: #000;
        font-weight: bold;
    }
</style>
{% endblock style %}

{% block body %}
<div class="container mt-3">
    <h1>{{question.title}}</h1>
    <p>{{question.body}}</p>
    <h6>
        Posted By: <i>{{question.author}} </i>
    </h6>
    <p>Published {{question.created_at}}</p>
    <hr>
</div>

<!-- Listing the answers -->
<div class="container">
    {% for answers in answer_list %}
        <div class="card mt-4 py-3 shadow">
            <div class="card-body">
                <p class="card-text answer">{{answers.description}}</p>
                <hr>
                <div class="row author">
                    <div class="col col-md-auto">
                        Answered By : {{answers.author.username}}
                    </div>
                    <div class="col col-md-auto">
                        Answered Time : {{answers.created_at}}
                    </div>
                </div>
            </div>
        </div>
    {% endfor %}
</div>
{% endblock body %}
```

![](https://user-images.githubusercontent.com/32337103/219168538-55678dc8-588e-4e66-8ea2-7acb4d693b34.png)

![](https://user-images.githubusercontent.com/32337103/219168808-ebd511da-0455-4712-a4f7-2ae9cf44d3a2.png)

![](https://user-images.githubusercontent.com/32337103/219167926-1b510cba-3b14-4010-adc1-bc29d8109bc0.png)

</details>

<details>
  <summary>52. Adding Answers </summary>

Cloud-Django/djqa/questions/forms.py:

```py
from django import forms
from django.contrib.auth import get_user_model
from .models import Question, Answer

User = get_user_model()

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class QuestionRegistrationForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'body',)

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('description',)
```

Cloud-Django/djqa/questions/models.py:

```py
from django.db import models
from django.conf import settings

# Create your models here.
class Question(models.Model):
    title= models.CharField(max_length=250)
    body = models.TextField()
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='questions')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    description = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.question.title}"
```

Cloud-Django/djqa/questions/views.py:

```bsx
def question_details(request, slug):
    question = get_object_or_404(Question, slug=slug)
    answer_list = Answer.objects.filter(question=question)

    #adding answer
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer = form.save()
            return redirect('question_details', slug=question.slug)
    else:
        form = AnswerForm()

    return render(request, 'questionDetails.html', {'question': question, 'answer_list': answer_list, 'form':form})
```

```py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from .forms import UserRegistrationForm, QuestionRegistrationForm, AnswerForm

# Create your views here.
def question_list(request):
    question_list = Question.objects.all().order_by('-created_at')
    return render(request, 'questionList.html', {'question_list': question_list})

def question_details(request, slug):
    question = get_object_or_404(Question, slug=slug)
    answer_list = Answer.objects.filter(question=question)

    #adding answer
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer = form.save()
            return redirect('question_details', slug=question.slug)
    else:
        form = AnswerForm()

    return render(request, 'questionDetails.html', {'question': question, 'answer_list': answer_list, 'form':form})

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register_done.html', {'user_form':user_form})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form':user_form})

def create_question (request):
    if request.method == "POST":
        question_form = QuestionRegistrationForm(request.POST)

        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.author = request.user
            question = question_form.save()
            return redirect('question_list')
    else:
        question_form = QuestionRegistrationForm()
    return render(request, 'add_question.html', {'question_form': question_form})

```

Cloud-Django/djqa/templates/questionDetails.html:

```py
{% extends 'base.html' %}
{% load crispy_forms_tags %}

{% block title %} Question Details {% endblock title %}

{% block style %}
<style>
    .author {
        color: gray;
    }
    .answer {
        color: #000;
        font-weight: bold;
    }
</style>
{% endblock style %}

{% block body %}
<div class="container mt-3">
    <h1>{{question.title}}</h1>
    <p>{{question.body}}</p>
    <h6>
        Posted By: <i>{{question.author}} </i>
    </h6>
    <p>Published {{question.created_at}}</p>
    <hr>
</div>

<!-- Listing the answers -->
<div class="container">
    {% for answers in answer_list %}
        <div class="card mt-4 py-3 shadow">
            <div class="card-body">
                <p class="card-text answer">{{answers.description}}</p>
                <hr>
                <div class="row author">
                    <div class="col col-md-auto">
                        Answered By : {{answers.author.username}}
                    </div>
                    <div class="col col-md-auto">
                        Answered Time : {{answers.created_at}}
                    </div>
                </div>
            </div>
        </div>
    {% endfor %}
</div>

<!-- Adding answers -->
<div class="container">
    <div class="card mt-4">
        <form method="post" novalidate>
            <h5 class="card-header">Add Answer</h5>
            <div class="card-body">
                {% csrf_token %}
                {{form | crispy}}
                <input type="submit" value="Add Answer" class="btn btn-primary">
            </div>
        </form>
    </div>
</div>


{% endblock body %}
```

![](https://user-images.githubusercontent.com/32337103/219849974-2df538a0-6cd2-4b04-9535-8b30af9041df.png)

![](https://user-images.githubusercontent.com/32337103/219850048-8e556589-6746-4658-8ca0-cfcf0287dd92.png)

![](https://user-images.githubusercontent.com/32337103/219850059-68db8b90-8d2a-4eed-9756-d0fc70112fa5.png)

</details>

<details>
  <summary>53. Update Question </summary>

Cloud-Django/djqa/templates/questionDetails.html:

```bsx
{% if request.user == question.author %}
    <a class="btn btn-danger" href="">Delete</a>
    <a class="btn btn-success" href="{% url 'update_question' question.slug %}">Update</a>
{% endif %}
```

```py
{% extends 'base.html' %}
{% load crispy_forms_tags %}

{% block title %} Question Details {% endblock title %}

{% block style %}
<style>
    .author {
        color: gray;
    }
    .answer {
        color: #000;
        font-weight: bold;
    }
</style>
{% endblock style %}

{% block body %}
<div class="container mt-3">
    <h1>{{question.title}}</h1>
    <p>{{question.body}}</p>
    <h6>
        Posted By: <i>{{question.author}} </i>
    </h6>
    <p>Published {{question.created_at}}</p>
    <hr>
    {% if request.user == question.author %}
        <a class="btn btn-danger" href="">Delete</a>
        <a class="btn btn-success" href="{% url 'update_question' question.slug %}">Update</a>
    {% endif %}

</div>

<!-- Listing the answers -->
<div class="container">
    {% for answers in answer_list %}
        <div class="card mt-4 py-3 shadow">
            <div class="card-body">
                <p class="card-text answer">{{answers.description}}</p>
                <hr>
                <div class="row author">
                    <div class="col col-md-auto">
                        Answered By : {{answers.author.username}}
                    </div>
                    <div class="col col-md-auto">
                        Answered Time : {{answers.created_at}}
                    </div>
                </div>
            </div>
        </div>
    {% endfor %}
</div>

<!-- Adding answers -->
<div class="container">
    <div class="card mt-4">
        <form method="post" novalidate>
            <h5 class="card-header">Add Answer</h5>
            <div class="card-body">
                {% csrf_token %}
                {{form | crispy}}
                <input type="submit" value="Add Answer" class="btn btn-primary">
            </div>
        </form>
    </div>
</div>


{% endblock body %}
```

Cloud-Django/djqa/questions/forms.py:

```bsx
class QuestionUpdateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'body')
```

```py
from django import forms
from django.contrib.auth import get_user_model
from .models import Question, Answer

User = get_user_model()

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class QuestionRegistrationForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'body',)

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('description',)

class QuestionUpdateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'body')
```

Cloud-Django/djqa/questions/models.py:

```py
from django.db import models
from django.conf import settings

# Create your models here.
class Question(models.Model):
    title= models.CharField(max_length=250)
    body = models.TextField()
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='questions')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    description = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.question.title}"
```

Cloud-Django/djqa/questions/views.py:

```bsx
def update_question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    form = QuestionUpdateForm(request.POST or None, instance=question)

    if form.is_valid():
        form.save()
        return redirect('question_list')
    return render (request, 'update.html', {'form': form})
```

```py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from .forms import UserRegistrationForm, QuestionRegistrationForm, AnswerForm, QuestionUpdateForm

# Create your views here.
def question_list(request):
    question_list = Question.objects.all().order_by('-created_at')
    return render(request, 'questionList.html', {'question_list': question_list})

def question_details(request, slug):
    question = get_object_or_404(Question, slug=slug)
    answer_list = Answer.objects.filter(question=question)

    #adding answer
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer = form.save()
            return redirect('question_details', slug=question.slug)
    else:
        form = AnswerForm()

    return render(request, 'questionDetails.html', {'question': question, 'answer_list': answer_list, 'form':form})

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register_done.html', {'user_form':user_form})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form':user_form})

def create_question(request):
    if request.method == "POST":
        question_form = QuestionRegistrationForm(request.POST)

        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.author = request.user
            question = question_form.save()
            return redirect('question_list')
    else:
        question_form = QuestionRegistrationForm()
    return render(request, 'add_question.html', {'question_form': question_form})

def update_question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    form = QuestionUpdateForm(request.POST or None, instance=question)

    if form.is_valid():
        form.save()
        return redirect('question_list')
    return render (request, 'update.html', {'form': form})

```

Cloud-Django/djqa/templates/update.html:

```py
{% extends 'base.html' %}
{% load crispy_forms_tags %}


{% block title %} Update Question {% endblock title %}

{% block style %}
<style>
    .update-style {
        width:700px;
        height: auto;
    }
</style>
{% endblock style %}

{% block body %}
<div class="container mt-5 update-style">
    <h3>Update Question</h3>

    <form action="" method="post" novalidate>
        {% csrf_token %}
        {{form | crispy}}

        <input type="submit" value="Update Question" class="btn btn-success">
    </form>
</div>
{% endblock body %}
```

Cloud-Django/djqa/questions/urls.py:

```py
from django.urls import path
from .views import question_list, question_details, register, create_question, update_question

urlpatterns = [
    path('question/', question_list, name='question_list'),
    path('question/<slug:slug>/', question_details, name='question_details'),
    path('register/', register, name='register'),
    path('add/', create_question, name='create_question'),
    path('update/<slug:slug>/', update_question, name='update_question'),
]
```

![](https://user-images.githubusercontent.com/32337103/219851544-1c2caaff-582d-4679-8464-acf2ace3c192.png)

![](https://user-images.githubusercontent.com/32337103/219851567-7c8a26a0-84e6-47a0-8dc3-0d5709c3ef8a.png)

![](https://user-images.githubusercontent.com/32337103/219851600-e8efbbb7-4560-4022-b1bf-660c928e8b83.png)

![](https://user-images.githubusercontent.com/32337103/219851614-9154d4dd-e8d3-44d8-88e0-db4529226a6f.png)

</details>

<details>
  <summary>54. Delete Question </summary>

Cloud-Django/djqa/questions/views.py:

```bsx
def delete_question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    question.delete()
    return redirect('question_list')
```

```py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from .forms import UserRegistrationForm, QuestionRegistrationForm, AnswerForm, QuestionUpdateForm

# Create your views here.
def question_list(request):
    question_list = Question.objects.all().order_by('-created_at')
    return render(request, 'questionList.html', {'question_list': question_list})

def question_details(request, slug):
    question = get_object_or_404(Question, slug=slug)
    answer_list = Answer.objects.filter(question=question)

    #adding answer
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer = form.save()
            return redirect('question_details', slug=question.slug)
    else:
        form = AnswerForm()

    return render(request, 'questionDetails.html', {'question': question, 'answer_list': answer_list, 'form':form})

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register_done.html', {'user_form':user_form})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form':user_form})

def create_question(request):
    if request.method == "POST":
        question_form = QuestionRegistrationForm(request.POST)

        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.author = request.user
            question = question_form.save()
            return redirect('question_list')
    else:
        question_form = QuestionRegistrationForm()
    return render(request, 'add_question.html', {'question_form': question_form})

def update_question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    form = QuestionUpdateForm(request.POST or None, instance=question)

    if form.is_valid():
        form.save()
        return redirect('question_list')
    return render (request, 'update.html', {'form': form})

def delete_question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    question.delete()
    return redirect('question_list')

```

Cloud-Django/djqa/questions/urls.py:

```py
from django.urls import path
from .views import question_list, question_details, register, create_question, update_question, delete_question

urlpatterns = [
    path('question/', question_list, name='question_list'),
    path('question/<slug:slug>/', question_details, name='question_details'),
    path('register/', register, name='register'),
    path('add/', create_question, name='create_question'),
    path('update/<slug:slug>/', update_question, name='update_question'),
    path('delete/<slug:slug>/', delete_question, name='delete_question'),
]
```

Cloud-Django/djqa/templates/questionDetails.html:

```bsx
{% if request.user == question.author %}
    <a class="btn btn-danger" href="{% url 'delete_question' question.slug %}">Delete</a>
    <a class="btn btn-success" href="{% url 'update_question' question.slug %}">Update</a>
{% endif %}
```

```py
{% extends 'base.html' %}
{% load crispy_forms_tags %}

{% block title %} Question Details {% endblock title %}

{% block style %}
<style>
    .author {
        color: gray;
    }
    .answer {
        color: #000;
        font-weight: bold;
    }
</style>
{% endblock style %}

{% block body %}
<div class="container mt-3">
    <h1>{{question.title}}</h1>
    <p>{{question.body}}</p>
    <h6>
        Posted By: <i>{{question.author}} </i>
    </h6>
    <p>Published {{question.created_at}}</p>
    <hr>
    {% if request.user == question.author %}
        <a class="btn btn-danger" href="{% url 'delete_question' question.slug %}">Delete</a>
        <a class="btn btn-success" href="{% url 'update_question' question.slug %}">Update</a>
    {% endif %}

</div>

<!-- Listing the answers -->
<div class="container">
    {% for answers in answer_list %}
        <div class="card mt-4 py-3 shadow">
            <div class="card-body">
                <p class="card-text answer">{{answers.description}}</p>
                <hr>
                <div class="row author">
                    <div class="col col-md-auto">
                        Answered By : {{answers.author.username}}
                    </div>
                    <div class="col col-md-auto">
                        Answered Time : {{answers.created_at}}
                    </div>
                </div>
            </div>
        </div>
    {% endfor %}
</div>

<!-- Adding answers -->
<div class="container">
    <div class="card mt-4">
        <form method="post" novalidate>
            <h5 class="card-header">Add Answer</h5>
            <div class="card-body">
                {% csrf_token %}
                {{form | crispy}}
                <input type="submit" value="Add Answer" class="btn btn-primary">
            </div>
        </form>
    </div>
</div>


{% endblock body %}
```

![](https://user-images.githubusercontent.com/32337103/219852301-32c69887-a6f9-4648-a15f-0c4073fd1918.png)

![](https://user-images.githubusercontent.com/32337103/219852326-99c887b1-b825-4ff5-8a29-0ee4c88c7a1b.png)

![](https://user-images.githubusercontent.com/32337103/219852344-974956db-afab-407b-8d68-35e1457603f4.png)

</details>

<details>
  <summary>55. Update Answer </summary>

Cloud-Django/djqa/questions/forms.py:

```bsx
class AnswerUpdateForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('description',)
```

```py
from django import forms
from django.contrib.auth import get_user_model
from .models import Question, Answer

User = get_user_model()

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class QuestionRegistrationForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'body',)

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('description',)

class QuestionUpdateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'body')

class AnswerUpdateForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('description',)
```

Cloud-Django/djqa/questions/views.py:

```bsx
def update_answer(request, id):
    answer = get_object_or_404(Answer, id=id)

    form = AnswerUpdateForm(request.POST or None, instance=answer)
    if form.is_valid():
        form.save()
        return redirect('question_details', slug=answer.question.slug)
    return render(request, 'update_answer.html', {'form': form})
```

```py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from .forms import UserRegistrationForm, QuestionRegistrationForm, AnswerForm, QuestionUpdateForm, AnswerUpdateForm

# Create your views here.
def question_list(request):
    question_list = Question.objects.all().order_by('-created_at')
    return render(request, 'questionList.html', {'question_list': question_list})

def question_details(request, slug):
    question = get_object_or_404(Question, slug=slug)
    answer_list = Answer.objects.filter(question=question)

    #adding answer
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer = form.save()
            return redirect('question_details', slug=question.slug)
    else:
        form = AnswerForm()

    return render(request, 'questionDetails.html', {'question': question, 'answer_list': answer_list, 'form':form})

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register_done.html', {'user_form':user_form})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form':user_form})

def create_question(request):
    if request.method == "POST":
        question_form = QuestionRegistrationForm(request.POST)

        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.author = request.user
            question = question_form.save()
            return redirect('question_list')
    else:
        question_form = QuestionRegistrationForm()
    return render(request, 'add_question.html', {'question_form': question_form})

def update_question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    form = QuestionUpdateForm(request.POST or None, instance=question)

    if form.is_valid():
        form.save()
        return redirect('question_list')
    return render (request, 'update.html', {'form': form})

def delete_question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    question.delete()
    return redirect('question_list')


def update_answer(request, id):
    answer = get_object_or_404(Answer, id=id)

    form = AnswerUpdateForm(request.POST or None, instance=answer)
    if form.is_valid():
        form.save()
        return redirect('question_details', slug=answer.question.slug)
    return render(request, 'update_answer.html', {'form': form})
```

Cloud-Django/djqa/templates/update_answer.html:

```py
{% extends 'base.html' %}
{% load crispy_forms_tags %}


{% block title %} Update Answer {% endblock title %}

{% block style %}
<style>
    .update-style {
        width:700px;
        height: auto;
    }
</style>
{% endblock style %}

{% block body %}
<div class="container mt-5 update-style">
    <h3>Update Answer</h3>

    <form action="" method="post" novalidate>
        {% csrf_token %}
        {{form | crispy}}

        <input type="submit" value="Update Answer" class="btn btn-success">
    </form>
</div>
{% endblock body %}
```

Cloud-Django/djqa/questions/urls.py:

```py
from django.urls import path
from .views import question_list, question_details, register, create_question, update_question, delete_question, update_answer

urlpatterns = [
    path('question/', question_list, name='question_list'),
    path('question/<slug:slug>/', question_details, name='question_details'),
    path('register/', register, name='register'),
    path('add/', create_question, name='create_question'),
    path('update/<slug:slug>/', update_question, name='update_question'),
    path('delete/<slug:slug>/', delete_question, name='delete_question'),
    path('answer/update/<int:id>/', update_answer, name='update_answer'),
]
```

Cloud-Django/djqa/templates/questionDetails.html:

```bsx
{% if request.user == answers.author %}
    <a class="btn btn-outline-danger btn-sm mt-3" href="">Delete</a>
    <a class="btn btn-outline-success btn-sm mt-3" href="{% url 'update_answer' answers.id %}">Update</a>
{% endif %}
```

```py
{% extends 'base.html' %}
{% load crispy_forms_tags %}

{% block title %} Question Details {% endblock title %}

{% block style %}
<style>
    .author {
        color: gray;
    }
    .answer {
        color: #000;
        font-weight: bold;
    }
</style>
{% endblock style %}

{% block body %}
<div class="container mt-3">
    <h1>{{question.title}}</h1>
    <p>{{question.body}}</p>
    <h6>
        Posted By: <i>{{question.author}} </i>
    </h6>
    <p>Published {{question.created_at}}</p>
    <hr>
    {% if request.user == question.author %}
        <a class="btn btn-danger" href="{% url 'delete_question' question.slug %}">Delete</a>
        <a class="btn btn-success" href="{% url 'update_question' question.slug %}">Update</a>
    {% endif %}

</div>

<!-- Listing the answers -->
<div class="container">
    {% for answers in answer_list %}
        <div class="card mt-4 py-3 shadow">
            <div class="card-body">
                <p class="card-text answer">{{answers.description}}</p>
                <hr>
                <div class="row author">
                    <div class="col col-md-auto">
                        Answered By : {{answers.author.username}}
                    </div>
                    <div class="col col-md-auto">
                        Answered Time : {{answers.created_at}}
                    </div>
                </div>
                {% if request.user == answers.author %}
                    <a class="btn btn-outline-danger btn-sm mt-3" href="">Delete</a>
                    <a class="btn btn-outline-success btn-sm mt-3" href="{% url 'update_answer' answers.id %}">Update</a>
                {% endif %}
            </div>
        </div>
    {% endfor %}
</div>

<!-- Adding answers -->
<div class="container">
    <div class="card mt-4">
        <form method="post" novalidate>
            <h5 class="card-header">Add Answer</h5>
            <div class="card-body">
                {% csrf_token %}
                {{form | crispy}}
                <input type="submit" value="Add Answer" class="btn btn-primary">
            </div>
        </form>
    </div>
</div>


{% endblock body %}
```

![](https://user-images.githubusercontent.com/32337103/219855053-9e452132-fb30-455c-b8e5-a004477a0fd8.png)

![](https://user-images.githubusercontent.com/32337103/219855084-44a50818-bf5f-45b8-ab25-ec76778e8b23.png)

![](https://user-images.githubusercontent.com/32337103/219855110-a868d59e-9f4b-4adf-ab21-5f2c1bede579.png)

![](https://user-images.githubusercontent.com/32337103/219855127-da664022-8b67-432b-9feb-405cc353bace.png)

</details>

<details>
  <summary>56. Delete Answer </summary>

Cloud-Django/djqa/questions/views.py:

```pybs
def delete_answer(request, id):
    answer = get_object_or_404(Answer, id=id)
    answer.delete()
    return redirect('question_details', slug = answer.question.slug)
```

```py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from .forms import UserRegistrationForm, QuestionRegistrationForm, AnswerForm, QuestionUpdateForm, AnswerUpdateForm

# Create your views here.
def question_list(request):
    question_list = Question.objects.all().order_by('-created_at')
    return render(request, 'questionList.html', {'question_list': question_list})

def question_details(request, slug):
    question = get_object_or_404(Question, slug=slug)
    answer_list = Answer.objects.filter(question=question)

    #adding answer
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer = form.save()
            return redirect('question_details', slug=question.slug)
    else:
        form = AnswerForm()

    return render(request, 'questionDetails.html', {'question': question, 'answer_list': answer_list, 'form':form})

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register_done.html', {'user_form':user_form})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form':user_form})

def create_question(request):
    if request.method == "POST":
        question_form = QuestionRegistrationForm(request.POST)

        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.author = request.user
            question = question_form.save()
            return redirect('question_list')
    else:
        question_form = QuestionRegistrationForm()
    return render(request, 'add_question.html', {'question_form': question_form})

def update_question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    form = QuestionUpdateForm(request.POST or None, instance=question)

    if form.is_valid():
        form.save()
        return redirect('question_list')
    return render (request, 'update.html', {'form': form})

def delete_question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    question.delete()
    return redirect('question_list')


def update_answer(request, id):
    answer = get_object_or_404(Answer, id=id)

    form = AnswerUpdateForm(request.POST or None, instance=answer)
    if form.is_valid():
        form.save()
        return redirect('question_details', slug=answer.question.slug)
    return render(request, 'update_answer.html', {'form': form})

def delete_answer(request, id):
    answer = get_object_or_404(Answer, id=id)
    answer.delete()
    return redirect('question_details', slug = answer.question.slug)
```

Cloud-Django/djqa/questions/urls.py:

```py
from django.urls import path
from .views import (question_list, question_details, register, create_question,
                    update_question, delete_question, update_answer, delete_answer)

urlpatterns = [
    path('question/', question_list, name='question_list'),
    path('question/<slug:slug>/', question_details, name='question_details'),
    path('register/', register, name='register'),
    path('add/', create_question, name='create_question'),
    path('update/<slug:slug>/', update_question, name='update_question'),
    path('delete/<slug:slug>/', delete_question, name='delete_question'),
    path('answer/update/<int:id>/', update_answer, name='update_answer'),
    path('answer/delete/<int:id>/', delete_answer, name='delete_answer'),
]
```

Cloud-Django/djqa/templates/questionDetails.html:

```pybs
{% if request.user == answers.author %}
    <a class="btn btn-outline-danger btn-sm mt-3" href="{% url 'delete_answer' answers.id %}">Delete</a>
    <a class="btn btn-outline-success btn-sm mt-3" href="{% url 'update_answer' answers.id %}">Update</a>
{% endif %}
```

```py
{% extends 'base.html' %}
{% load crispy_forms_tags %}

{% block title %} Question Details {% endblock title %}

{% block style %}
<style>
    .author {
        color: gray;
    }
    .answer {
        color: #000;
        font-weight: bold;
    }
</style>
{% endblock style %}

{% block body %}
<div class="container mt-3">
    <h1>{{question.title}}</h1>
    <p>{{question.body}}</p>
    <h6>
        Posted By: <i>{{question.author}} </i>
    </h6>
    <p>Published {{question.created_at}}</p>
    <hr>
    {% if request.user == question.author %}
        <a class="btn btn-danger" href="{% url 'delete_question' question.slug %}">Delete</a>
        <a class="btn btn-success" href="{% url 'update_question' question.slug %}">Update</a>
    {% endif %}

</div>

<!-- Listing the answers -->
<div class="container">
    {% for answers in answer_list %}
        <div class="card mt-4 py-3 shadow">
            <div class="card-body">
                <p class="card-text answer">{{answers.description}}</p>
                <hr>
                <div class="row author">
                    <div class="col col-md-auto">
                        Answered By : {{answers.author.username}}
                    </div>
                    <div class="col col-md-auto">
                        Answered Time : {{answers.created_at}}
                    </div>
                </div>
                {% if request.user == answers.author %}
                    <a class="btn btn-outline-danger btn-sm mt-3" href="{% url 'delete_answer' answers.id %}">Delete</a>
                    <a class="btn btn-outline-success btn-sm mt-3" href="{% url 'update_answer' answers.id %}">Update</a>
                {% endif %}
            </div>
        </div>
    {% endfor %}
</div>

<!-- Adding answers -->
<div class="container">
    <div class="card mt-4">
        <form method="post" novalidate>
            <h5 class="card-header">Add Answer</h5>
            <div class="card-body">
                {% csrf_token %}
                {{form | crispy}}
                <input type="submit" value="Add Answer" class="btn btn-primary">
            </div>
        </form>
    </div>
</div>


{% endblock body %}
```

![](https://user-images.githubusercontent.com/32337103/221179897-8351d8c3-18df-4a2d-81e3-a4ec42c66ed9.png)
![](https://user-images.githubusercontent.com/32337103/221180036-ff8fb197-7e82-4276-9e89-28a369c1a814.png)
![](https://user-images.githubusercontent.com/32337103/221180095-e9371ec1-3c32-45dc-aa94-34426ef73129.png)

</details>

<details>
  <summary>57. Change Password </summary>

Cloud-Django/djqa/users/urls.py:

```py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
]
```

Cloud-Django/djqa/templates/registration/password_change_form.html:

```py
{% extends 'base.html' %}
{% load crispy_forms_tags %}


{% block title %} Password Change {% endblock title %}

{% block style %}
<style>
    .login-style {
        width:500px;
        height: auto;
    }
</style>
{% endblock style %}

{% block body %}
<div class="container mt-4 login-style">
    <h3>Change Your Password</h3>

    <form action="" method="post" novalidate>
        {% csrf_token %}
        {{form | crispy}}

        <input type="submit" value="Change Password" class="btn btn-success">
    </form>
</div>
{% endblock body %}
```

Cloud-Django/djqa/templates/registration/password_change_done.html:

```py
{% extends 'base.html' %}
{% load crispy_forms_tags %}


{% block title %} Change Done {% endblock title %}

{% block body %}
<div class="container mt-4">
    <h3>Password Changed</h3>
    <p>Your Password has been changed.</p>
</div>
{% endblock body %}
```

Cloud-Django/djqa/templates/navbar.html:

```pybs
<li><a class="dropdown-item" href="{% url 'password_change' %}">Change Password</a></li>
```

```py
<style>
    .text-style {
        font-size: 30px !important;
        font-family: fantasy !important;
        color: brown !important;
        font-weight: bold !important;
    }
</style>

<nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand text-style" href="{% url 'question_list' %}">Question Hub</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">

          {% if request.user.is_authenticated %}

          <li class="nav-item mx-3">
            <a class="nav-link disabled">Welcome, {{request.user.username | title}}.</a>
          </li>

          <form class="d-flex" role="search">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button>
          </form>

          <li class="nav-item mx-3">
            <a class="nav-link active" aria-current="page" href="{% url 'question_list' %}">Home</a>
          </li>

          <li class="nav-item">
            <a class="nav-link" href="{% url 'create_question' %}">Add Question</a>
          </li>

          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Profile
            </a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="{% url 'password_change' %}">Change Password</a></li>
              <li><a class="dropdown-item" href="#">Change Account</a></li>
              <li><a class="dropdown-item" href="#">Question & Answer</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="{% url 'logout' %}">Logout</a></li>
            </ul>
          </li>

          {% else %}

          <li class="nav-item">
            <a class="nav-link" href="{% url 'login' %}">Login</a>
          </li>

          <li class="nav-item">
            <a class="nav-link" href="{% url 'register' %}">Register</a>
          </li>

          {% endif %}
        </ul>

      </div>
    </div>
  </nav>
```

![](https://user-images.githubusercontent.com/32337103/221259754-71d7b2ed-a136-470c-a08d-0eb27338f184.png)

![](https://user-images.githubusercontent.com/32337103/221259568-8a7ecdeb-736c-4d56-a2f6-5849342bb49f.png)

</details>

<details>
  <summary>58. Change Account Information </summary>

Cloud-Django/djqa/questions/forms.py:

```pybs
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
```

```py
from django import forms
from django.contrib.auth import get_user_model
from .models import Question, Answer

User = get_user_model()

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class QuestionRegistrationForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'body',)

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('description',)

class QuestionUpdateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'body')

class AnswerUpdateForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('description',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

```

Cloud-Django/djqa/questions/views.py:

```pybs
def change_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile has been updated successfully')

    form = ProfileForm(instance=request.user)
    return render(request, 'registration/profile.html', {'form': form})
```

```py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from django.contrib import messages
from .forms import UserRegistrationForm, QuestionRegistrationForm, AnswerForm, QuestionUpdateForm, AnswerUpdateForm, ProfileForm

# Create your views here.
def question_list(request):
    question_list = Question.objects.all().order_by('-created_at')
    return render(request, 'questionList.html', {'question_list': question_list})

def question_details(request, slug):
    question = get_object_or_404(Question, slug=slug)
    answer_list = Answer.objects.filter(question=question)

    #adding answer
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer = form.save()
            return redirect('question_details', slug=question.slug)
    else:
        form = AnswerForm()

    return render(request, 'questionDetails.html', {'question': question, 'answer_list': answer_list, 'form':form})

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register_done.html', {'user_form':user_form})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form':user_form})

def create_question(request):
    if request.method == "POST":
        question_form = QuestionRegistrationForm(request.POST)

        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.author = request.user
            question = question_form.save()
            return redirect('question_list')
    else:
        question_form = QuestionRegistrationForm()
    return render(request, 'add_question.html', {'question_form': question_form})

def update_question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    form = QuestionUpdateForm(request.POST or None, instance=question)

    if form.is_valid():
        form.save()
        return redirect('question_list')
    return render (request, 'update.html', {'form': form})

def delete_question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    question.delete()
    return redirect('question_list')


def update_answer(request, id):
    answer = get_object_or_404(Answer, id=id)

    form = AnswerUpdateForm(request.POST or None, instance=answer)
    if form.is_valid():
        form.save()
        return redirect('question_details', slug=answer.question.slug)
    return render(request, 'update_answer.html', {'form': form})

def delete_answer(request, id):
    answer = get_object_or_404(Answer, id=id)
    answer.delete()
    return redirect('question_details', slug = answer.question.slug)

def change_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile has been updated successfully')

    form = ProfileForm(instance=request.user)
    return render(request, 'registration/profile.html', {'form': form})

```

Cloud-Django/djqa/templates/registration/profile.html:

```py
{% extends 'base.html' %}
{% load crispy_forms_tags %}


{% block title %} Profile {% endblock title %}

{% block style %}
<style>
    .profile-style {
        width:500px;
        height: auto;
    }
</style>
{% endblock style %}

{% block body %}
<div class="container mt-4 profile-style">

    {% if messages %}
        {% for msg in messages %}
            <div class="alert alert-{{msg.level_tag}}" role="alert">
                {{msg.message}}
            </div>
        {% endfor %}
    {% endif %}

    <h2>Change Profile</h2>

    <form action="" method="post" novalidate>
        {% csrf_token %}
        {{form | crispy}}

        <input type="submit" value="Change Account" class="btn btn-success">
    </form>
</div>
{% endblock body %}
```

Cloud-Django/djqa/questions/urls.py:

```py
from django.urls import path
from .views import (question_list, question_details, register, create_question,
                    update_question, delete_question, update_answer, delete_answer, change_profile)

urlpatterns = [
    path('question/', question_list, name='question_list'),
    path('question/<slug:slug>/', question_details, name='question_details'),
    path('register/', register, name='register'),
    path('add/', create_question, name='create_question'),
    path('update/<slug:slug>/', update_question, name='update_question'),
    path('delete/<slug:slug>/', delete_question, name='delete_question'),
    path('answer/update/<int:id>/', update_answer, name='update_answer'),
    path('answer/delete/<int:id>/', delete_answer, name='delete_answer'),
    path('profile/', change_profile, name='profile'),
]
```

Cloud-Django/djqa/templates/navbar.html:

```pybs
<li><a class="dropdown-item" href="{% url 'profile' %}">Change Account</a></li>
```

```py
<style>
    .text-style {
        font-size: 30px !important;
        font-family: fantasy !important;
        color: brown !important;
        font-weight: bold !important;
    }
</style>

<nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand text-style" href="{% url 'question_list' %}">Question Hub</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">

          {% if request.user.is_authenticated %}

          <li class="nav-item mx-3">
            <a class="nav-link disabled">Welcome, {{request.user.username | title}}.</a>
          </li>

          <form class="d-flex" role="search">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button>
          </form>

          <li class="nav-item mx-3">
            <a class="nav-link active" aria-current="page" href="{% url 'question_list' %}">Home</a>
          </li>

          <li class="nav-item">
            <a class="nav-link" href="{% url 'create_question' %}">Add Question</a>
          </li>

          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Profile
            </a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="{% url 'password_change' %}">Change Password</a></li>
              <li><a class="dropdown-item" href="{% url 'profile' %}">Change Account</a></li>
              <li><a class="dropdown-item" href="#">Question & Answer</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="{% url 'logout' %}">Logout</a></li>
            </ul>
          </li>

          {% else %}

          <li class="nav-item">
            <a class="nav-link" href="{% url 'login' %}">Login</a>
          </li>

          <li class="nav-item">
            <a class="nav-link" href="{% url 'register' %}">Register</a>
          </li>

          {% endif %}
        </ul>

      </div>
    </div>
  </nav>
```

![](https://user-images.githubusercontent.com/32337103/221277283-13267bbc-203c-4e70-8217-7815542e8288.png)

![](https://user-images.githubusercontent.com/32337103/221277769-8be787e5-797a-403a-b773-8271f33f29c3.png)

</details>

<details>
  <summary>59. Listing Questions and Answers for User</summary>

Cloud-Django/djqa/questions/views.py:

```pybs
def list_info(request):
    questions = Question.objects.filter(author=request.user).order_by('-created_at')
    answers = Answer.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'list_info.html', {'questions': questions, 'answers': answers})
```

```py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from django.contrib import messages
from .forms import UserRegistrationForm, QuestionRegistrationForm, AnswerForm, QuestionUpdateForm, AnswerUpdateForm, ProfileForm

# Create your views here.
def question_list(request):
    question_list = Question.objects.all().order_by('-created_at')
    return render(request, 'questionList.html', {'question_list': question_list})

def question_details(request, slug):
    question = get_object_or_404(Question, slug=slug)
    answer_list = Answer.objects.filter(question=question)

    #adding answer
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer = form.save()
            return redirect('question_details', slug=question.slug)
    else:
        form = AnswerForm()

    return render(request, 'questionDetails.html', {'question': question, 'answer_list': answer_list, 'form':form})

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register_done.html', {'user_form':user_form})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form':user_form})

def create_question(request):
    if request.method == "POST":
        question_form = QuestionRegistrationForm(request.POST)

        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.author = request.user
            question = question_form.save()
            return redirect('question_list')
    else:
        question_form = QuestionRegistrationForm()
    return render(request, 'add_question.html', {'question_form': question_form})

def update_question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    form = QuestionUpdateForm(request.POST or None, instance=question)

    if form.is_valid():
        form.save()
        return redirect('question_list')
    return render (request, 'update.html', {'form': form})

def delete_question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    question.delete()
    return redirect('question_list')


def update_answer(request, id):
    answer = get_object_or_404(Answer, id=id)

    form = AnswerUpdateForm(request.POST or None, instance=answer)
    if form.is_valid():
        form.save()
        return redirect('question_details', slug=answer.question.slug)
    return render(request, 'update_answer.html', {'form': form})

def delete_answer(request, id):
    answer = get_object_or_404(Answer, id=id)
    answer.delete()
    return redirect('question_details', slug = answer.question.slug)

def change_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile has been updated successfully')

    form = ProfileForm(instance=request.user)
    return render(request, 'registration/profile.html', {'form': form})


def list_info(request):
    questions = Question.objects.filter(author=request.user).order_by('-created_at')
    answers = Answer.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'list_info.html', {'questions': questions, 'answers': answers})

```

Cloud-Django/djqa/questions/urls.py:

```py
from django.urls import path
from .views import (question_list, question_details, register, create_question,
                    update_question, delete_question, update_answer, delete_answer, change_profile,
                    list_info)

urlpatterns = [
    path('question/', question_list, name='question_list'),
    path('question/<slug:slug>/', question_details, name='question_details'),
    path('register/', register, name='register'),
    path('add/', create_question, name='create_question'),
    path('update/<slug:slug>/', update_question, name='update_question'),
    path('delete/<slug:slug>/', delete_question, name='delete_question'),
    path('answer/update/<int:id>/', update_answer, name='update_answer'),
    path('answer/delete/<int:id>/', delete_answer, name='delete_answer'),
    path('profile/', change_profile, name='profile'),
    path('list/', list_info, name='list'),
]
```

Cloud-Django/djqa/templates/list_info.html:

```py
{% extends 'base.html' %}

{% block title %}Listing Questions{% endblock title %}

{% block style%}
    <style>
        .link-style {
            text-decoration:none;
            color: #00798C;
        }
        .link-style:hover {
            text-decoration:none;
            color:gray;
        }
    </style>
{% endblock style%}

{% block body%}
<div class="container mt-5">
    <ul class="nav nav-tabs" id="myTab" role="tablist">
        <li class="nav-item" role="presentation">
          <button class="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#home-tab-pane" type="button" role="tab" aria-controls="home-tab-pane" aria-selected="true">Question</button>
        </li>
        <li class="nav-item" role="presentation">
          <button class="nav-link" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile-tab-pane" type="button" role="tab" aria-controls="profile-tab-pane" aria-selected="false">Answer</button>
        </li>
    </ul>
    <div class="tab-content" id="myTabContent">
        <div class="tab-pane fade show active" id="home-tab-pane" role="tabpanel" aria-labelledby="home-tab" tabindex="0">
            <div class="card mt-4 py-3 shadow">
                <h4 class="card-header">You have asked {{questions.count}} question{% if questions.count > 1%}s{% endif %}.</h4>
                <div class="card-body">
                    {% for question in questions %}
                    <h5 class="card-text"><a class="link-style" href="{% url 'question_details' question.slug %}">{{question.title}}</a></h5>
                    <a class="btn btn-outline-danger btn-sm mt-3" href="{% url 'delete_question' question.slug %}">Delete</a>
                    <a class="btn btn-outline-success btn-sm mt-3" href="{% url 'update_question' question.slug %}">Update</a>
                    <hr>
                    {% endfor %}
                </div>
            </div>
        </div>
        <div class="tab-pane fade" id="profile-tab-pane" role="tabpanel" aria-labelledby="profile-tab" tabindex="0">
            <div class="card mt-4 py-3 shadow">
                <h4 class="card-header">You have answered {{answers.count}} time{% if answers.count > 1%}s{% endif %}.</h4>
                <div class="card-body">
                    {% for answer in answers %}
                    <p class="card-text">{{answer.description}}</p>
                    <a class="btn btn-outline-danger btn-sm mt-3" href="{% url 'delete_answer' answer.id %}">Delete</a>
                    <a class="btn btn-outline-success btn-sm mt-3" href="{% url 'update_answer' answer.id %}">Update</a>
                    <hr>
                    {% endfor %}
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock body%}
```

Cloud-Django/djqa/templates/navbar.html:

```pybs
 <li><a class="dropdown-item" href="{% url 'list' %}">Question & Answer</a></li>
```

```py
<style>
    .text-style {
        font-size: 30px !important;
        font-family: fantasy !important;
        color: brown !important;
        font-weight: bold !important;
    }
</style>

<nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand text-style" href="{% url 'question_list' %}">Question Hub</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">

          {% if request.user.is_authenticated %}

          <li class="nav-item mx-3">
            <a class="nav-link disabled">Welcome, {{request.user.username | title}}.</a>
          </li>

          <form class="d-flex" role="search">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button>
          </form>

          <li class="nav-item mx-3">
            <a class="nav-link active" aria-current="page" href="{% url 'question_list' %}">Home</a>
          </li>

          <li class="nav-item">
            <a class="nav-link" href="{% url 'create_question' %}">Add Question</a>
          </li>

          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Profile
            </a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="{% url 'password_change' %}">Change Password</a></li>
              <li><a class="dropdown-item" href="{% url 'profile' %}">Change Account</a></li>
              <li><a class="dropdown-item" href="{% url 'list' %}">Question & Answer</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="{% url 'logout' %}">Logout</a></li>
            </ul>
          </li>

          {% else %}

          <li class="nav-item">
            <a class="nav-link" href="{% url 'login' %}">Login</a>
          </li>

          <li class="nav-item">
            <a class="nav-link" href="{% url 'register' %}">Register</a>
          </li>

          {% endif %}
        </ul>

      </div>
    </div>
  </nav>
```

![](https://user-images.githubusercontent.com/32337103/221382018-af7b5ac6-a4b6-4e0a-a9f4-e5e3220ec411.png)
![](https://user-images.githubusercontent.com/32337103/221382025-9ec05b15-0f64-4f99-aacf-7a5551319824.png)

</details>

<details>
  <summary>60. Login Required - Protected Routes </summary>

Cloud-Django/djqa/users/urls.py:

```py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
]
```

Cloud-Django/djqa/questions/views.py:

```pybs
from django.contrib.auth.decorators import login_required
```

```py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from django.contrib import messages
from .forms import UserRegistrationForm, QuestionRegistrationForm, AnswerForm, QuestionUpdateForm, AnswerUpdateForm, ProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def question_list(request):
    question_list = Question.objects.all().order_by('-created_at')
    return render(request, 'questionList.html', {'question_list': question_list})

@login_required
def question_details(request, slug):
    question = get_object_or_404(Question, slug=slug)
    answer_list = Answer.objects.filter(question=question)

    #adding answer
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer = form.save()
            return redirect('question_details', slug=question.slug)
    else:
        form = AnswerForm()

    return render(request, 'questionDetails.html', {'question': question, 'answer_list': answer_list, 'form':form})

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register_done.html', {'user_form':user_form})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form':user_form})

@login_required
def create_question(request):
    if request.method == "POST":
        question_form = QuestionRegistrationForm(request.POST)

        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.author = request.user
            question = question_form.save()
            return redirect('question_list')
    else:
        question_form = QuestionRegistrationForm()
    return render(request, 'add_question.html', {'question_form': question_form})

@login_required
def update_question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    form = QuestionUpdateForm(request.POST or None, instance=question)

    if form.is_valid():
        form.save()
        return redirect('question_list')
    return render (request, 'update.html', {'form': form})

@login_required
def delete_question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    question.delete()
    return redirect('question_list')

@login_required
def update_answer(request, id):
    answer = get_object_or_404(Answer, id=id)

    form = AnswerUpdateForm(request.POST or None, instance=answer)
    if form.is_valid():
        form.save()
        return redirect('question_details', slug=answer.question.slug)
    return render(request, 'update_answer.html', {'form': form})

@login_required
def delete_answer(request, id):
    answer = get_object_or_404(Answer, id=id)
    answer.delete()
    return redirect('question_details', slug = answer.question.slug)

@login_required
def change_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile has been updated successfully')

    form = ProfileForm(instance=request.user)
    return render(request, 'registration/profile.html', {'form': form})

@login_required
def list_info(request):
    questions = Question.objects.filter(author=request.user).order_by('-created_at')
    answers = Answer.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'list_info.html', {'questions': questions, 'answers': answers})

```

![](https://user-images.githubusercontent.com/32337103/221382778-c833d03f-0d99-4f38-83d4-5aa14c29264a.png)

</details>

<details>
  <summary>61. Search Functionality</summary>

Cloud-Django/djqa/templates/navbar.html:

```pybs
<input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" name="q">
```

```py
<style>
    .text-style {
        font-size: 30px !important;
        font-family: fantasy !important;
        color: brown !important;
        font-weight: bold !important;
    }
</style>

<nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand text-style" href="{% url 'question_list' %}">Question Hub</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">

          {% if request.user.is_authenticated %}

          <li class="nav-item mx-3">
            <a class="nav-link disabled">Welcome, {{request.user.username | title}}.</a>
          </li>

          <form class="d-flex" role="search">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" name="q">
            <button class="btn btn-outline-success" type="submit">Search</button>
          </form>

          <li class="nav-item mx-3">
            <a class="nav-link active" aria-current="page" href="{% url 'question_list' %}">Home</a>
          </li>

          <li class="nav-item">
            <a class="nav-link" href="{% url 'create_question' %}">Add Question</a>
          </li>

          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Profile
            </a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="{% url 'password_change' %}">Change Password</a></li>
              <li><a class="dropdown-item" href="{% url 'profile' %}">Change Account</a></li>
              <li><a class="dropdown-item" href="{% url 'list' %}">Question & Answer</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="{% url 'logout' %}">Logout</a></li>
            </ul>
          </li>

          {% else %}

          <li class="nav-item">
            <a class="nav-link" href="{% url 'login' %}">Login</a>
          </li>

          <li class="nav-item">
            <a class="nav-link" href="{% url 'register' %}">Register</a>
          </li>

          {% endif %}
        </ul>

      </div>
    </div>
  </nav>
```

Cloud-Django/djqa/questions/views.py:

```pybs
@login_required
def question_list(request):
    if 'q' in request.GET:
        q = request.GET['q']
        question_list = Question.objects.filter(title__icontains=q).order_by('-created_at')
    else:
        question_list = Question.objects.all().order_by('-created_at')
    return render(request, 'questionList.html', {'question_list': question_list})
```

```py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from django.contrib import messages
from .forms import UserRegistrationForm, QuestionRegistrationForm, AnswerForm, QuestionUpdateForm, AnswerUpdateForm, ProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def question_list(request):
    if 'q' in request.GET:
        q = request.GET['q']
        question_list = Question.objects.filter(title__icontains=q).order_by('-created_at')
    else:
        question_list = Question.objects.all().order_by('-created_at')
    return render(request, 'questionList.html', {'question_list': question_list})

@login_required
def question_details(request, slug):
    question = get_object_or_404(Question, slug=slug)
    answer_list = Answer.objects.filter(question=question)

    #adding answer
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer = form.save()
            return redirect('question_details', slug=question.slug)
    else:
        form = AnswerForm()

    return render(request, 'questionDetails.html', {'question': question, 'answer_list': answer_list, 'form':form})

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register_done.html', {'user_form':user_form})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form':user_form})

@login_required
def create_question(request):
    if request.method == "POST":
        question_form = QuestionRegistrationForm(request.POST)

        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.author = request.user
            question = question_form.save()
            return redirect('question_list')
    else:
        question_form = QuestionRegistrationForm()
    return render(request, 'add_question.html', {'question_form': question_form})

@login_required
def update_question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    form = QuestionUpdateForm(request.POST or None, instance=question)

    if form.is_valid():
        form.save()
        return redirect('question_list')
    return render (request, 'update.html', {'form': form})

@login_required
def delete_question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    question.delete()
    return redirect('question_list')

@login_required
def update_answer(request, id):
    answer = get_object_or_404(Answer, id=id)

    form = AnswerUpdateForm(request.POST or None, instance=answer)
    if form.is_valid():
        form.save()
        return redirect('question_details', slug=answer.question.slug)
    return render(request, 'update_answer.html', {'form': form})

@login_required
def delete_answer(request, id):
    answer = get_object_or_404(Answer, id=id)
    answer.delete()
    return redirect('question_details', slug = answer.question.slug)

@login_required
def change_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile has been updated successfully')

    form = ProfileForm(instance=request.user)
    return render(request, 'registration/profile.html', {'form': form})

@login_required
def list_info(request):
    questions = Question.objects.filter(author=request.user).order_by('-created_at')
    answers = Answer.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'list_info.html', {'questions': questions, 'answers': answers})

```

Cloud-Django/djqa/templates/questionList.html:

```pybs
{% if not question_list%}
<div class="card mt-3 shadow">
    <div class="card-body">
        <h5 class="card-title"><a class="link-style" href="">Sorry, No records were found.</a></h5>
    </div>
    <div class="card-footer">
        <div class="row">
            <a href="{% url 'question_list'%}"><button class="btn btn-success">Return</button></a>
        </div>
    </div>
</div>
{% endif %}
```

```py
{% extends 'base.html' %}

{% block title %}Question List{% endblock title %}

{% block style%}
    <style>
        .link-style {
            text-decoration:none;
            color: #00798C;
        }
        .link-style:hover {
            text-decoration:none;
            color:gray;
        }
    </style>
{% endblock style%}

{% block body%}
<div class="container">
{% for question in question_list %}
    <div class="card mt-3 shadow">
        <div class="card-body">
            <h5 class="card-title"><a class="link-style" href="{% url 'question_details' question.slug %}">{{question.title}}</a></h5>
            <p class="card-text">{{question.body}}</p>
        </div>
        <div class="card-footer">
            <div class="row">
                <div class="col col-md-auto">
                    Posted By: {{question.author.username}}
                </div>
                <div class="col col-md-auto">
                    Answers: {{question.answers.count}}
                </div>
            </div>
        </div>
    </div>
{% endfor %}
{% if not question_list%}
<div class="card mt-3 shadow">
    <div class="card-body">
        <h5 class="card-title"><a class="link-style" href="">Sorry, No records were found.</a></h5>
    </div>
    <div class="card-footer">
        <div class="row">
            <a href="{% url 'question_list'%}"><button class="btn btn-success">Return</button></a>
        </div>
    </div>
</div>
{% endif %}
</div>
{% endblock body%}
```

![](https://user-images.githubusercontent.com/32337103/221398472-d8fc81a4-5688-4364-ad9b-ebb719be4319.png)
![](https://user-images.githubusercontent.com/32337103/221398486-bfad61ed-1a94-457e-95ff-175e9697fa9e.png)
![](https://user-images.githubusercontent.com/32337103/221398498-78173b1b-5202-4647-9654-385d37b8e11e.png)
![](https://user-images.githubusercontent.com/32337103/221398504-147e72d5-3a3a-47c3-a1f8-732e8b2d3c0d.png)

</details>

<details>
  <summary>62. Deploy App in Python Everywhere</summary>

```pybs
https://www.pythonanywhere.com/
```

Cloud-Django/djqa/djqa/settings.py:

```pybs
DEBUG = False
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '<username>.pythonanywhere.com']

import os
'DIRS': [os.path.join(BASE_DIR, 'templates')]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

```py
"""
Django settings for djqa project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x_$lqqwi86ny6o@j3l0est&=57qqr93)@a^(8*^7h2bmpc+ts$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'omeatai.pythonanywhere.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "crispy_forms",
    "crispy_bootstrap5",
    'users',
    'questions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djqa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': ['templates'],
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

WSGI_APPLICATION = 'djqa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

AUTH_USER_MODEL = 'users.CustomUser'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

LOGIN_REDIRECT_URL = 'question_list'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

```

```pybs
python manage.py collectstatic
```

```pybs
pip freeze > requirements.txt
```

```pybs
Create Github Repository - djqa
```

```pybs
echo "# djqa" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/omeatai/djqa.git
git push -u origin main
OR
git remote add origin https://github.com/omeatai/djqa.git
git branch -M main
git push -u origin main
```

```pybs
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/omeatai/djqa.git
git push -u origin main
```

```pybs
git reset
git reset --hard HEAD~1
git reset --hard <sha1 of desired commit>

git reflog OR git log -g
git reset --hard HEAD@{3}
```

pythonanywhere -> console -> Bash

![](https://user-images.githubusercontent.com/32337103/221400346-2680602a-cd2c-466d-8167-fc60fd3fa94f.png)

```pybs
git clone https://github.com/omeatai/djqa.git
```

![](https://user-images.githubusercontent.com/32337103/221400544-ba22fa83-7609-429b-ac21-a34aaf97d7d5.png)

```pybs
cd djqa
ls
mkvirtualenv --python=/usr/bin/python3.9 myvenv
```

![](https://user-images.githubusercontent.com/32337103/221400769-1928daba-1b01-4396-af75-4b4c635323c1.png)

```pybs
pip install -r requirements.txt
```

![](https://user-images.githubusercontent.com/32337103/221401205-36e79beb-e337-4616-a4a4-fc2c5356da6b.png)

```pybs
Web -> Add a new Web App -> Manual configuration (including virtualenvs) -> Python 3.9 -> Next
```

![](https://user-images.githubusercontent.com/32337103/221401282-0de38a25-1f10-4e92-ab5c-767286d7c639.png)

![](https://user-images.githubusercontent.com/32337103/221402342-492b3f23-5503-41f6-ab4f-30c721ca61f4.png)
![](https://user-images.githubusercontent.com/32337103/221402376-65586274-da56-45c6-b1a2-1097d24e263a.png)
![](https://user-images.githubusercontent.com/32337103/221402450-041b83b9-0da4-4fde-9907-3b54b7cf74e6.png)
![](https://user-images.githubusercontent.com/32337103/221402508-8b3fc187-51ba-441a-8940-e79ab9c58a6f.png)

```pybs
import os
import sys

path = ''
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application ()
```

![](https://user-images.githubusercontent.com/32337103/221402746-2ee45331-4db0-4f6c-9646-4803a1fceeca.png)
![](https://user-images.githubusercontent.com/32337103/221403046-9e8007ce-c405-4557-8517-dd150d86ef46.png)
![](https://user-images.githubusercontent.com/32337103/221403101-597168d7-572b-4582-8ddd-f7aedced20cd.png)
![](https://user-images.githubusercontent.com/32337103/221403154-484bdd66-cca4-456c-9fc9-7a9798f4346c.png)

</details>

<details>
  <summary>63. Check for Upgrades </summary>

List outdated packages:

```pybs
pip list --outdated
```

requirements.txt:

```pybs
asgiref>=3.4.1
crispy-bootstrap5>=0.6
Django>=3.2.7
django-crispy-forms>=1.13.0
pytz>=2021.3
sqlparse>=0.4.2
```

```pybs
pip install -r requirements.txt --upgrade
```

```pybs
pip frèeze > requirements.txt
```

</details>

+DJANGO REST FRAMEWORK

<details>
  <summary>64. Introduction </summary>

Install Venv:

```pybs
python -m venv venv
source venv/bin/activate
```

Install django:

```pybs
pip install django
```

Install Project:

```pybs
django-admin startproject blogapi .
```

Install Django Rest Framework:

```pybs
pip install djangorestframework
```

Cloud-Django/djrest/blogapi/settings.py:

```pybs
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

```pybs
python manage.py migrate
```

```pybs
python manage.py runserver
```

</details>

<details>
  <summary>65. Create App Models</summary>

Create django App:

```pybs
python manage.py startapp backend
```

Cloud-Django/djrest/blogapi/settings.py:

```pybs
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'backend',
]
```

Cloud-Django/djrest/backend/models.py:

```py
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

```pybs
python manage.py makemigrations
```

```py
python manage.py migrate
```

</details>

<details>
  <summary>66. Create SuperUser </summary>

```py
python manage.py createsuperuser
```

![](https://user-images.githubusercontent.com/32337103/221493725-854335c1-868f-4b0c-b9dd-6d11911407be.png)
![](https://user-images.githubusercontent.com/32337103/221493783-013cf70e-4017-4a9f-9edb-317b7b7040f8.png)
![](https://user-images.githubusercontent.com/32337103/221493822-d8da89b3-9d95-443b-b17b-477e6886ddbb.png)

</details>

<details>
  <summary>67. Register Model to Admin </summary>

Cloud-Django/djrest/backend/admin.py:

```py
from django.contrib import admin
from .models import Article

# Register your models here.
admin.site.register(Article)
```

![](https://user-images.githubusercontent.com/32337103/221494744-1baf320b-5ee7-488b-b422-e3f18ac8ca38.png)
![](https://user-images.githubusercontent.com/32337103/221494920-a49cc9fa-3982-4f41-aa5c-04f4d4afac99.png)
![](https://user-images.githubusercontent.com/32337103/221494988-c0cc3aa5-1222-44d7-8526-6ba29ad11d25.png)

</details>

<details>
  <summary>68. Create Dynamic Slugs with Django Signals</summary>

Cloud-Django/djrest/backend/signals.py:

```py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Article
from django.utils.text import slugify


@receiver(pre_save, sender=Article)
def add_slug(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.title)
        instance.slug = slug
```

Cloud-Django/djrest/backend/apps.py:

```py
from django.apps import AppConfig


class BackendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend'

    def ready(self):
        import backend.signals

```

Cloud-Django/djrest/backend/init.py:

```py
default_app_config = 'backend.apps. Backend Config'
```

Start Django Shell:

```pybs
python manage.py shell
```

```pybs
>>> from django.contrib.auth import get_user_model
>>> user = get_user_model()
>>> u = user.objects.first()
>>> from backend.models import Article
>>> article = Article(title="This is my title", description = "This is my description")
>>> article.save()
```

![](https://user-images.githubusercontent.com/32337103/221498835-55a3cca3-103a-41aa-8756-602451122bf6.png)
![](https://user-images.githubusercontent.com/32337103/221498969-d2464fa4-e788-42a8-8357-010bf7d84836.png)
![](https://user-images.githubusercontent.com/32337103/221499036-f0671ce6-4fb5-45aa-90f9-2c64a89ed143.png)

</details>

<details>
  <summary>69. Serialization </summary>

Cloud-Django/djrest/backend/serializers.py:

```py
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    slug = serializers.SlugField(max_length=200)
    published = serializers.DateTimeField(read_only=True)

def create(self, validated_data):
    return Article.objects.create(**validated_data)

def update(self, instance, validated_data):
    instance.title = validated_data.get('title', instance.title)
    instance.description = validated_data.get('description', instance.description)
    instance.slug = validated_data.get('slug', instance.slug)
    instance.published = validated_data.get('published', instance.published)
    instance.save()
    return instance
```

SERIALIZATION:

```pybs
>>> from backend.models import Article
>>> from backend.serializers import ArticleSerializer
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser
>>> a = Article(title="This is my title for serializtion",description="This is my description")
>>> a.save()
>>> serializer = ArticleSerializer(a)
>>> serializer.data
```

```pybs
{'title': 'This is my title for serializtion', 'description': 'This is my description', 'slug': 'this-is-my-title-for-serializtion', 'published': '2023-02-27T10:19:33.988149Z'}
```

![](https://user-images.githubusercontent.com/32337103/221537700-4ac54e5f-8b10-40e5-b5f8-2b0bce2a974e.png)

```pybs
>>> content = JSONRenderer().render(serializer.data)
>>> content
```

```pybs
b'{
    "title":"This is my title for serializtion",
    "description":"This is my description",
    "slug":"this-is-my-title-for-serializtion",
    "published":"2023-02-27T10:19:33.988149Z"
}'
```

DESERIALIZATION:

```pybs
>>> import io
>>> stream = io.BytesIO(content)
>>> data = JSONParser().parse(stream)
>>> serializer = ArticleSerializer(data=data)
>>> serializer.is_valid()
True
>>> serializer.validated_data
```

```pybs
OrderedDict([('title', 'This is my title for serializtion'), ('description', 'This is my description'), ('slug', 'this-is-my-title-for-serializtion')])
```

![](https://user-images.githubusercontent.com/32337103/221553790-cd69469d-b05a-4214-a829-e4b523622404.png)

```pybs
>>> serializer = ArticleSerializer(Article.objects.all(), many=True)
>>> serializer.data
```

![](https://user-images.githubusercontent.com/32337103/221554352-b542cc79-ff36-4d5d-a57f-989abc335d3d.png)

</details>

<details>
  <summary>70. Model Serializer </summary>

Cloud-Django/djrest/backend/serializers.py:

```py
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     description = serializers.CharField()
#     slug = serializers.SlugField(max_length=200)
#     published = serializers.DateTimeField(read_only=True)

# def create(self, validated_data):
#     return Article.objects.create(**validated_data)

# def update(self, instance, validated_data):
#     instance.title = validated_data.get('title', instance.title)
#     instance.description = validated_data.get('description', instance.description)
#     instance.slug = validated_data.get('slug', instance.slug)
#     instance.published = validated_data.get('published', instance.published)
#     instance.save()
#     return instance
```

```pybs
>>> from backend.serializers import ArticleSerializer
>>> serializer = ArticleSerializer()
>>> print(repr(serializer))
```

![](https://user-images.githubusercontent.com/32337103/221588611-f7133f72-1a62-4fd2-bf6c-e45984f34134.png)

Cloud-Django/djrest/backend/serializers.py:

```py
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'description']

# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     description = serializers.CharField()
#     slug = serializers.SlugField(max_length=200)
#     published = serializers.DateTimeField(read_only=True)

# def create(self, validated_data):
#     return Article.objects.create(**validated_data)

# def update(self, instance, validated_data):
#     instance.title = validated_data.get('title', instance.title)
#     instance.description = validated_data.get('description', instance.description)
#     instance.slug = validated_data.get('slug', instance.slug)
#     instance.published = validated_data.get('published', instance.published)
#     instance.save()
#     return instance
```

```pybs
>>> from backend.serializers import ArticleSerializer
>>> serializer = ArticleSerializer()
>>> print(repr(serializer))
```

![](https://user-images.githubusercontent.com/32337103/221589601-c7c37852-6f2a-4310-a822-90f3fa127dd0.png)

</details>

<details>
  <summary>71. API View Functions for GET and POST </summary>

Cloud-Django/djrest/backend/views.py:

```py
from django.shortcuts import render
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

# Create your views here.
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
```

Cloud-Django/djrest/backend/urls.py:

```py
from django.urls import path
from .views import article_list

urlpatterns = [
    path('articles/', article_list, name='article_list')
]
```

Cloud-Django/djrest/blogapi/urls.py:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.urls'))
]
```

```pybs
python manage.py runserver
```

http://127.0.0.1:8000/articles/

![](https://user-images.githubusercontent.com/32337103/221601140-6a19e4f4-0a64-43c6-9549-787dbd736def.png)

</details>

<details>
  <summary>72. Using POSTMAN for GET and POST requests </summary>

Using POSTMAN -

GET:

![](https://user-images.githubusercontent.com/32337103/221603833-bfc988ea-74d3-4bf7-a1f5-7d7f3e3653f4.png)

POST:

![](https://user-images.githubusercontent.com/32337103/221605285-8eeee239-57de-40e2-9341-5aceb41a248a.png)

CSRF Exempt -

Cloud-Django/djrest/backend/views.py:

```py
from django.shortcuts import render
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
```

Cloud-Django/djrest/backend/serializers.py:

```pybs
slug = serializers.SlugField(read_only=True)
```

```py
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    class Meta:
        model = Article
        fields = '__all__'

# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     description = serializers.CharField()
#     slug = serializers.SlugField(max_length=200)
#     published = serializers.DateTimeField(read_only=True)

# def create(self, validated_data):
#     return Article.objects.create(**validated_data)

# def update(self, instance, validated_data):
#     instance.title = validated_data.get('title', instance.title)
#     instance.description = validated_data.get('description', instance.description)
#     instance.slug = validated_data.get('slug', instance.slug)
#     instance.published = validated_data.get('published', instance.published)
#     instance.save()
#     return instance
```

POST:

![](https://user-images.githubusercontent.com/32337103/221606733-6e74b9e1-7b73-4a3f-874b-45937dc818ea.png)

GET:

![](https://user-images.githubusercontent.com/32337103/221607611-ffa3e954-04dc-472b-a95a-0b87c143df87.png)

</details>

<details>
  <summary>73. API View Functions for Article Details for GET (Details), PUT, DELETE </summary>

Cloud-Django/djrest/backend/views.py:

```pybs
@csrf_exempt
def article_details(request, slug):
    try:
        article = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        article.delete()
        return HttpResponse(status=204)
```

```py
from django.shortcuts import render, HttpResponse
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def article_details(request, slug):
    try:
        article = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        article.delete()
        return HttpResponse(status=204)

```

Cloud-Django/djrest/backend/urls.py:

```py
from django.urls import path
from .views import article_list, article_details

urlpatterns = [
    path('articles/', article_list, name='article_list'),
    path('articles/<slug:slug>/', article_details, name='article_details'),
]
```

GET:

![](https://user-images.githubusercontent.com/32337103/221613958-dbdabb95-8121-4b40-98f1-dc5efb0fc2b9.png)

![](https://user-images.githubusercontent.com/32337103/221615645-87395944-3767-4fd4-af59-7f973bb85dc1.png)

PUT:

![](https://user-images.githubusercontent.com/32337103/221616380-23137256-ed99-479e-bf5b-8814f12c1156.png)

![](https://user-images.githubusercontent.com/32337103/221616665-76bec988-3a5f-4229-a098-d8d78e6f0f9b.png)

DELETE:

![](https://user-images.githubusercontent.com/32337103/221617930-2746d8ef-9c45-416c-b2ba-14485771af8b.png)
![](https://user-images.githubusercontent.com/32337103/221620102-366e5847-d664-481b-adde-230ea2f8946d.png)

</details>

<details>
  <summary>74. API View Decorators (@api_view) for GET and POST </summary>

backend/views.py:

```pybs
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

```py
from django.shortcuts import render, HttpResponse
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#API VIEW FUNCTIONS

# @csrf_exempt
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)

#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == "DELETE":
#         article.delete()
#         return HttpResponse(status=204)

```

backend/urls.py:

```py
from django.urls import path
from .views import article_list

urlpatterns = [
    path('articles/', article_list, name='article_list'),
    # path('articles/<slug:slug>/', article_details, name='article_details'),
]
```

GET:

http://127.0.0.1:8000/articles/

![](https://user-images.githubusercontent.com/32337103/221639333-5a1f831b-b0a8-4905-9080-798f44a7f04d.png)

POST:

![](https://user-images.githubusercontent.com/32337103/221639622-e0e6db4e-dc36-4af4-873a-1ba920a49786.png)

![](https://user-images.githubusercontent.com/32337103/221639801-2f1dc0d7-80d4-4499-a347-6ff3b5f339bc.png)

![](https://user-images.githubusercontent.com/32337103/221640281-8198d3df-cfed-40bc-b102-8b209524aaba.png)

</details>

<details>
  <summary>75. API View Decorators (@api_view) for GET (Details), PUT, DELETE </summary>

backend/views.py:

```pybs
@api_view (['GET', 'PUT', 'DELETE'])
def article_details(request, slug):
    try:
        article = Article.objects.get(slug=slug)
    except Article.DoesNotExist():
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

```py
from django.shortcuts import render, HttpResponse
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view (['GET', 'PUT', 'DELETE'])
def article_details(request, slug):
    try:
        article = Article.objects.get(slug=slug)
    except Article.DoesNotExist():
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#API VIEW FUNCTIONS

# @csrf_exempt
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)

#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == "DELETE":
#         article.delete()
#         return HttpResponse(status=204)

```

backend/urls.py:

```py
from django.urls import path
from .views import article_list, article_details

urlpatterns = [
    path('articles/', article_list, name='article_list'),
    path('articles/<slug:slug>/', article_details, name='article_details'),
]
```

GET:

![](https://user-images.githubusercontent.com/32337103/221644610-1cdc9305-43f0-4f06-98ad-77a7d57f3efd.png)
![](https://user-images.githubusercontent.com/32337103/221644802-52768726-879e-432c-936b-8a83f34ef833.png)

PUT:

![](https://user-images.githubusercontent.com/32337103/221645642-be9bde4f-078b-43b5-a973-f4f07b36f067.png)
![](https://user-images.githubusercontent.com/32337103/221645716-280129d6-ae96-43fc-9f11-c6820bc78f8f.png)

DELETE:

![](https://user-images.githubusercontent.com/32337103/221646064-c9c65b18-9512-43ae-a203-a968e71ff0e4.png)
![](https://user-images.githubusercontent.com/32337103/221646127-64652c42-450c-4085-9e04-673e999566b4.png)
![](https://user-images.githubusercontent.com/32337103/221646183-6dee1776-7bf6-41f1-b54f-14ea02162192.png)
![](https://user-images.githubusercontent.com/32337103/221646229-53dd74aa-a5a4-40be-a491-c53f724ff916.png)

</details>

<details>
  <summary>76. Class Based API Views for GET and POST </summary>

backend/views.py:

```pybs
class ArticleList(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)
```

```py
from django.shortcuts import render, HttpResponse
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView

class ArticleList(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)

# DECORATOR API VIEWS

# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response (serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view (['GET', 'PUT', 'DELETE'])
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist():
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#API VIEW FUNCTIONS

# @csrf_exempt
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)

#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == "DELETE":
#         article.delete()
#         return HttpResponse(status=204)

```

backend/urls.py:

```py
from django.urls import path
from .views import ArticleList

urlpatterns = [
    path('articles/', ArticleList.as_view())
]
```

![](https://user-images.githubusercontent.com/32337103/221688961-1387f7c4-16cf-4bf1-8dcc-0f15046fa5b2.png)
![](https://user-images.githubusercontent.com/32337103/221689481-0ba9c499-d72b-41a5-b71d-eea789916c35.png)
![](https://user-images.githubusercontent.com/32337103/221689607-18f3903e-8dc4-4a97-ad3a-44c4bf6e203b.png)
![](https://user-images.githubusercontent.com/32337103/221689738-ca9987c4-5f7e-445e-94e7-f9e646d64664.png)

</details>

<details>
  <summary>77. Class Based API Views for GET (Details), PUT and DELETE </summary>

GET -

backend/views.py:

```pybs
class ArticleDetails (APIView):
    def get_object(self, slug):
        try:
            return Article.objects.get(slug=slug)
        except Article.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, slug):
        article = self.get_object(slug)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
```

```py
from django.shortcuts import render, HttpResponse
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404


class ArticleList(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)

class ArticleDetails(APIView):
    def get_object(self, slug):
        try:
            return Article.objects.get(slug=slug)
        except Article.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, slug):
        article = self.get_object(slug)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

# DECORATOR API VIEWS

# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response (serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view (['GET', 'PUT', 'DELETE'])
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist():
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#API VIEW FUNCTIONS

# @csrf_exempt
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)

#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == "DELETE":
#         article.delete()
#         return HttpResponse(status=204)

```

backend/urls.py:

```py
from django.urls import path
from .views import ArticleList, ArticleDetails

urlpatterns = [
    path('articles/', ArticleList.as_view()),
    path('articles/<slug:slug>/', ArticleDetails.as_view())
]
```

![](https://user-images.githubusercontent.com/32337103/221694878-61d5959f-2a13-4e7c-84ea-38dfc00cc88a.png)
![](https://user-images.githubusercontent.com/32337103/221695043-2b159827-e19e-4808-9ebf-f3a7072e91ba.png)

PUT and DELETE -

backend/views.py:

```pybs
class ArticleDetails(APIView):
    def get_object(self, slug):
        try:
            return Article.objects.get(slug=slug)
        except Article.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, slug):
        article = self.get_object(slug)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, slug):
        article = self.get_object(slug)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        article = self.get_object(slug)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

```py
from django.shortcuts import render, HttpResponse
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404


class ArticleList(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)

class ArticleDetails(APIView):
    def get_object(self, slug):
        try:
            return Article.objects.get(slug=slug)
        except Article.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, slug):
        article = self.get_object(slug)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, slug):
        article = self.get_object(slug)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        article = self.get_object(slug)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# DECORATOR API VIEWS

# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response (serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view (['GET', 'PUT', 'DELETE'])
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist():
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#API VIEW FUNCTIONS

# @csrf_exempt
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)

#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == "DELETE":
#         article.delete()
#         return HttpResponse(status=204)
```

backend/urls.py:

```py
from django.urls import path
from .views import ArticleList, ArticleDetails

urlpatterns = [
    path('articles/', ArticleList.as_view()),
    path('articles/<slug:slug>/', ArticleDetails.as_view())
]
```

![](https://user-images.githubusercontent.com/32337103/221702347-92485680-731b-42c0-93a2-484e92e8d588.png)
![](https://user-images.githubusercontent.com/32337103/221702508-84a5e581-eb8b-48bc-b8c3-b2717fc669e0.png)
![](https://user-images.githubusercontent.com/32337103/221702660-8751e521-5bc8-4923-8d9c-e26c1b5ce5c1.png)
![](https://user-images.githubusercontent.com/32337103/221702860-df5ca62d-3ed5-441b-affd-037a6b01fa3d.png)
![](https://user-images.githubusercontent.com/32337103/221702904-41e864b0-b9df-42c8-94d9-688cf71ea3f4.png)

</details>

<details>
  <summary>78. Using Mixins for GET and POST Requests </summary>

backend/views.py:

```pybs
class ArticleList(mixins.ListModelMixin,mixins.CreateModelMixin,
                generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```

```py
from django.shortcuts import render, HttpResponse
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

from rest_framework import mixins
from rest_framework import generics


class ArticleList(mixins.ListModelMixin,mixins.CreateModelMixin,
                generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# CLASS BASED API VIEWS

# class ArticleList(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)

# class ArticleDetails(APIView):
#     def get_object(self, slug):
#         try:
#             return Article.objects.get(slug=slug)
#         except Article.DoesNotExist as e:
#             raise Http404 from e

#     def get(self, request, slug):
#         article = self.get_object(slug)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     def put(self, request, slug):
#         article = self.get_object(slug)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, slug):
#         article = self.get_object(slug)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# DECORATOR API VIEWS

# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response (serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view (['GET', 'PUT', 'DELETE'])
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist():
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#API VIEW FUNCTIONS

# @csrf_exempt
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)

#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == "DELETE":
#         article.delete()
#         return HttpResponse(status=204)

```

backend/urls.py:

```py
from django.urls import path
from .views import ArticleList

urlpatterns = [
    path('articles/', ArticleList.as_view()),
    # path('articles/<slug:slug>/', ArticleDetails.as_view())
]
```

![](https://user-images.githubusercontent.com/32337103/221709324-4e52a780-3fa2-4056-8ac7-d52e7763ebd8.png)
![](https://user-images.githubusercontent.com/32337103/221709621-3631975c-61e9-4de1-9c11-5367be3167b9.png)
![](https://user-images.githubusercontent.com/32337103/221709640-33fd8139-35b4-4dc3-8be0-765e7f6acda8.png)
![](https://user-images.githubusercontent.com/32337103/221709673-ebf7ef25-d78f-430f-b84a-fb6a83040408.png)

</details>

<details>
  <summary>79. Using Mixins for GET (Details), PUT and DELETE </summary>

backend/views.py:

```pybs
class ArticleDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'

    def get(self, request, slug, *args, **kwargs):
        return self.retrieve(request, slug=slug)

    def put(self, request, slug, *args, **kwargs):
        return self.update (request, slug=slug)

    def delete (self, request, slug):
        return self.destroy(request, slug=slug)
```

```py
from django.shortcuts import render, HttpResponse
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

from rest_framework import mixins
from rest_framework import generics


class ArticleList(mixins.ListModelMixin,mixins.CreateModelMixin,
                generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ArticleDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'

    def get(self, request, slug, *args, **kwargs):
        return self.retrieve(request, slug=slug)

    def put(self, request, slug, *args, **kwargs):
        return self.update (request, slug=slug)

    def delete (self, request, slug):
        return self.destroy(request, slug=slug)

# CLASS BASED API VIEWS

# class ArticleList(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)

# class ArticleDetails(APIView):
#     def get_object(self, slug):
#         try:
#             return Article.objects.get(slug=slug)
#         except Article.DoesNotExist as e:
#             raise Http404 from e

#     def get(self, request, slug):
#         article = self.get_object(slug)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     def put(self, request, slug):
#         article = self.get_object(slug)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, slug):
#         article = self.get_object(slug)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# DECORATOR API VIEWS

# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response (serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view (['GET', 'PUT', 'DELETE'])
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist():
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#API VIEW FUNCTIONS

# @csrf_exempt
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)

#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == "DELETE":
#         article.delete()
#         return HttpResponse(status=204)

```

backend/urls.py:

```py
from django.urls import path
from .views import ArticleList, ArticleDetails

urlpatterns = [
    path('articles/', ArticleList.as_view()),
    path('articles/<slug:slug>/', ArticleDetails.as_view())
]
```

GET:

![](https://user-images.githubusercontent.com/32337103/221778205-fbb39122-7a0b-4372-8c36-1176952e4790.png)
![](https://user-images.githubusercontent.com/32337103/221778259-92cbe221-749a-4cdf-9c49-60ebece9baf5.png)

UPDATE:

![](https://user-images.githubusercontent.com/32337103/221778414-69b489b0-499e-4f1f-860a-713961a212c0.png)
![](https://user-images.githubusercontent.com/32337103/221778450-fa13c326-3ed9-402b-b0ad-a5773fca5ae3.png)

DELETE:

![](https://user-images.githubusercontent.com/32337103/221778505-f299dbe7-5e10-4534-bec9-7c80e5fb3689.png)
![](https://user-images.githubusercontent.com/32337103/221778536-8c8b3001-fbad-473e-aae8-bc29136a4cef.png)
![](https://user-images.githubusercontent.com/32337103/221778588-b8bd584c-ecb0-4143-a066-5cdc4abe0e09.png)

</details>

<details>
  <summary>80. Generic Class Based Views for GET and POST</summary>

backend/views.py:

```pybs
class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
```

```py
from django.shortcuts import render, HttpResponse
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

from rest_framework import mixins
from rest_framework import generics


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

# Using Mixins

# class ArticleList(mixins.ListModelMixin,mixins.CreateModelMixin,
#                 generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ArticleDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     lookup_field = 'slug'

#     def get(self, request, slug, *args, **kwargs):
#         return self.retrieve(request, slug=slug)

#     def put(self, request, slug, *args, **kwargs):
#         return self.update (request, slug=slug)

#     def delete (self, request, slug):
#         return self.destroy(request, slug=slug)

# CLASS BASED API VIEWS

# class ArticleList(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)

# class ArticleDetails(APIView):
#     def get_object(self, slug):
#         try:
#             return Article.objects.get(slug=slug)
#         except Article.DoesNotExist as e:
#             raise Http404 from e

#     def get(self, request, slug):
#         article = self.get_object(slug)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     def put(self, request, slug):
#         article = self.get_object(slug)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, slug):
#         article = self.get_object(slug)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# DECORATOR API VIEWS

# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response (serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view (['GET', 'PUT', 'DELETE'])
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist():
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#API VIEW FUNCTIONS

# @csrf_exempt
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)

#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == "DELETE":
#         article.delete()
#         return HttpResponse(status=204)

```

backend/urls.py:

```py
from django.urls import path
from .views import ArticleList

urlpatterns = [
    path('articles/', ArticleList.as_view()),
    # path('articles/<slug:slug>/', ArticleDetails.as_view())
]
```

GET:

![](https://user-images.githubusercontent.com/32337103/221780608-52d38e63-79cd-46e7-9d27-0f1266826a9b.png)

POST:

![](https://user-images.githubusercontent.com/32337103/221780780-cbd0e86f-c041-4fd7-9f15-c3cb9f49da4d.png)
![](https://user-images.githubusercontent.com/32337103/221780827-dcf70f73-de2d-48ea-b66d-de71130ce92b.png)
![](https://user-images.githubusercontent.com/32337103/221780876-de1d1a8b-99fd-4684-b393-9eabf52fad66.png)

</details>

<details>
  <summary>81. Generic Class Based Views for GET (Details), UPDATE, DELETE </summary>

backend/views.py:

```pybs
class ArticleDetails(generics. RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'
```

```py
from django.shortcuts import render, HttpResponse
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

from rest_framework import mixins
from rest_framework import generics


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetails(generics. RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'

# Using Mixins

# class ArticleList(mixins.ListModelMixin,mixins.CreateModelMixin,
#                 generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ArticleDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     lookup_field = 'slug'

#     def get(self, request, slug, *args, **kwargs):
#         return self.retrieve(request, slug=slug)

#     def put(self, request, slug, *args, **kwargs):
#         return self.update (request, slug=slug)

#     def delete (self, request, slug):
#         return self.destroy(request, slug=slug)

# CLASS BASED API VIEWS

# class ArticleList(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)

# class ArticleDetails(APIView):
#     def get_object(self, slug):
#         try:
#             return Article.objects.get(slug=slug)
#         except Article.DoesNotExist as e:
#             raise Http404 from e

#     def get(self, request, slug):
#         article = self.get_object(slug)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     def put(self, request, slug):
#         article = self.get_object(slug)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, slug):
#         article = self.get_object(slug)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# DECORATOR API VIEWS

# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response (serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view (['GET', 'PUT', 'DELETE'])
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist():
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#API VIEW FUNCTIONS

# @csrf_exempt
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)

#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == "DELETE":
#         article.delete()
#         return HttpResponse(status=204)

```

backend/urls.py:

```py
from django.urls import path
from .views import ArticleList, ArticleDetails

urlpatterns = [
    path('articles/', ArticleList.as_view()),
    path('articles/<slug:slug>/', ArticleDetails.as_view())
]
```

GET (Details):

![](https://user-images.githubusercontent.com/32337103/221782870-492c9f40-3f31-400e-8074-32ef292a3415.png)
![](https://user-images.githubusercontent.com/32337103/221782969-7ae5b116-6985-498c-aafe-4ea4b4f177f6.png)

UPDATE:

![](https://user-images.githubusercontent.com/32337103/221783057-675e40d8-57e9-4dbe-890e-d3550f57b4b0.png)
![](https://user-images.githubusercontent.com/32337103/221783111-b1185b57-7866-4826-97fa-46a82b9ea74f.png)

DELETE:

![](https://user-images.githubusercontent.com/32337103/221783179-603c50ad-d16b-4097-b022-f5bd40e3a4c8.png)
![](https://user-images.githubusercontent.com/32337103/221783220-76c4b6f6-0075-4f6a-8177-201531d8289a.png)
![](https://user-images.githubusercontent.com/32337103/221783277-cc36c466-8ae7-4fa8-b8ef-e6bf86bdd28f.png)

</details>

<details>
  <summary>82. Viewsets and Routers for GET and POST </summary>

backend/views.py:

```pybs
class ArticleViewSet(viewsets.ViewSet):
    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)
```

```py
from django.shortcuts import render, HttpResponse
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics

from rest_framework import viewsets


class ArticleViewSet(viewsets.ViewSet):
    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)

# GENERIC API VIEWS

# class ArticleList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleDetails(generics. RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     lookup_field = 'slug'

# USING MIXINS

# class ArticleList(mixins.ListModelMixin,mixins.CreateModelMixin,
#                 generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ArticleDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     lookup_field = 'slug'

#     def get(self, request, slug, *args, **kwargs):
#         return self.retrieve(request, slug=slug)

#     def put(self, request, slug, *args, **kwargs):
#         return self.update (request, slug=slug)

#     def delete (self, request, slug):
#         return self.destroy(request, slug=slug)

# CLASS BASED API VIEWS

# class ArticleList(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)

# class ArticleDetails(APIView):
#     def get_object(self, slug):
#         try:
#             return Article.objects.get(slug=slug)
#         except Article.DoesNotExist as e:
#             raise Http404 from e

#     def get(self, request, slug):
#         article = self.get_object(slug)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     def put(self, request, slug):
#         article = self.get_object(slug)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, slug):
#         article = self.get_object(slug)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# DECORATOR API VIEWS

# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response (serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view (['GET', 'PUT', 'DELETE'])
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist():
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#API VIEW FUNCTIONS

# @csrf_exempt
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)

#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == "DELETE":
#         article.delete()
#         return HttpResponse(status=204)

```

backend/urls.py:

```py
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')

urlpatterns = [
    # path('articles/', ArticleList.as_view()),
    # path('articles/<slug:slug>/', ArticleDetails.as_view())
    path('', include(router.urls))
]
```

GET:

![](https://user-images.githubusercontent.com/32337103/221788133-0b571002-b7e3-4da2-848f-92efb77f8298.png)

POST:

![](https://user-images.githubusercontent.com/32337103/221788447-8f1ae365-f874-4c2c-86db-9367dd5f9c87.png)
![](https://user-images.githubusercontent.com/32337103/221788509-32bbe1f9-f0fd-4021-af05-c64c7a571c4e.png)
![](https://user-images.githubusercontent.com/32337103/221788558-a9d6b789-585c-4f21-9c7d-cd3f5b58ea42.png)

</details>

<details>
  <summary>83. Viewsets and Routers for GET (Details), UPDATE and DELETE </summary>

backend/views.py:

```pybs
class ArticleDetailsViewSet(viewsets.ViewSet):
    queryset = Article.objects.all()

    def retrieve(self, request, pk=None):
        article = get_object_or_404(self.queryset, id=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, id=pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, id=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

```py
from django.shortcuts import render, HttpResponse
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics

from rest_framework import viewsets
from django.shortcuts import get_object_or_404


class ArticleViewSet(viewsets.ViewSet):
    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)

class ArticleDetailsViewSet(viewsets.ViewSet):
    queryset = Article.objects.all()

    def retrieve(self, request, pk=None):
        article = get_object_or_404(self.queryset, id=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, id=pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, id=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# GENERIC API VIEWS

# class ArticleList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleDetails(generics. RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     lookup_field = 'slug'

# USING MIXINS

# class ArticleList(mixins.ListModelMixin,mixins.CreateModelMixin,
#                 generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ArticleDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     lookup_field = 'slug'

#     def get(self, request, slug, *args, **kwargs):
#         return self.retrieve(request, slug=slug)

#     def put(self, request, slug, *args, **kwargs):
#         return self.update (request, slug=slug)

#     def delete (self, request, slug):
#         return self.destroy(request, slug=slug)

# CLASS BASED API VIEWS

# class ArticleList(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)

# class ArticleDetails(APIView):
#     def get_object(self, slug):
#         try:
#             return Article.objects.get(slug=slug)
#         except Article.DoesNotExist as e:
#             raise Http404 from e

#     def get(self, request, slug):
#         article = self.get_object(slug)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     def put(self, request, slug):
#         article = self.get_object(slug)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, slug):
#         article = self.get_object(slug)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# DECORATOR API VIEWS

# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response (serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view (['GET', 'PUT', 'DELETE'])
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist():
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#API VIEW FUNCTIONS

# @csrf_exempt
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)

#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == "DELETE":
#         article.delete()
#         return HttpResponse(status=204)

```

backend/urls.py:

```py
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, ArticleDetailsViewSet

app_name = 'backend'

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
router.register('articles', ArticleDetailsViewSet, basename='articles')
urlpatterns = router.urls

# urlpatterns = [
#     path('', include(router.urls))
# ]
```

GET (Details):

![](https://user-images.githubusercontent.com/32337103/221915985-de032869-7caa-4b18-9e8e-953de20a8522.png)
![](https://user-images.githubusercontent.com/32337103/221921137-b7cf1928-b1c0-47b1-873a-59d04d4c33f3.png)

UPDATE:

![](https://user-images.githubusercontent.com/32337103/221921351-35556d19-fbd9-4244-be4d-b6dcf87f5c1d.png)
![](https://user-images.githubusercontent.com/32337103/221921447-b4c208c1-f40c-4c81-9806-1b99a734e155.png)

DELETE:

![](https://user-images.githubusercontent.com/32337103/221921513-e3cd010a-bd69-4f3b-8f17-ba0c03127d63.png)
![](https://user-images.githubusercontent.com/32337103/221921560-60b91ce6-b785-48ea-a43e-53d51f047a25.png)
![](https://user-images.githubusercontent.com/32337103/221921634-a46792b2-dafb-4712-8eda-9010bd853688.png)

</details>

<details>
  <summary>84. Generic Viewset for GET and POST </summary>

backend/views.py:

```pybs
class ArticleViewSet (viewsets.GenericViewSet, mixins.ListModelMixin,
                    mixins.CreateModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
```

```py
from django.shortcuts import render, HttpResponse
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics

from rest_framework import mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


class ArticleViewSet (viewsets.GenericViewSet, mixins.ListModelMixin,
                    mixins.CreateModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

# VIEWSETS AND ROUTERS

# class ArticleViewSet(viewsets.ViewSet):
#     def list(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)

# class ArticleDetailsViewSet(viewsets.ViewSet):
#     queryset = Article.objects.all()

#     def retrieve(self, request, pk=None):
#         article = get_object_or_404(self.queryset, id=pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     def update(self, request, pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset, id=pk)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset, id=pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# GENERIC API VIEWS

# class ArticleList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleDetails(generics. RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     lookup_field = 'slug'

# USING MIXINS

# class ArticleList(mixins.ListModelMixin,mixins.CreateModelMixin,
#                 generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ArticleDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     lookup_field = 'slug'

#     def get(self, request, slug, *args, **kwargs):
#         return self.retrieve(request, slug=slug)

#     def put(self, request, slug, *args, **kwargs):
#         return self.update (request, slug=slug)

#     def delete (self, request, slug):
#         return self.destroy(request, slug=slug)

# CLASS BASED API VIEWS

# class ArticleList(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)

# class ArticleDetails(APIView):
#     def get_object(self, slug):
#         try:
#             return Article.objects.get(slug=slug)
#         except Article.DoesNotExist as e:
#             raise Http404 from e

#     def get(self, request, slug):
#         article = self.get_object(slug)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     def put(self, request, slug):
#         article = self.get_object(slug)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, slug):
#         article = self.get_object(slug)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# DECORATOR API VIEWS

# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response (serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view (['GET', 'PUT', 'DELETE'])
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist():
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#API VIEW FUNCTIONS

# @csrf_exempt
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)

#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == "DELETE":
#         article.delete()
#         return HttpResponse(status=204)

```

backend/urls.py:

```py
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet

app_name = 'backend'

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
# router.register('articles', ArticleDetailsViewSet, basename='articles')
urlpatterns = router.urls

# urlpatterns = [
#     path('', include(router.urls))
# ]
```

GET:

![](https://user-images.githubusercontent.com/32337103/221924334-d7a79a3d-05f2-4310-b4e0-1d7a5ae0ee83.png">

POST:

![](https://user-images.githubusercontent.com/32337103/221924484-ba433311-155e-4afa-875a-2c5149c7d0cc.png)
![](https://user-images.githubusercontent.com/32337103/221924539-b9a7b0cd-3283-4d8a-83bf-199dde79a4d9.png)
![](https://user-images.githubusercontent.com/32337103/221924613-b7c78051-0199-4221-a5b1-b2cc52e43e6d.png)

</details>

<details>
  <summary>85. Generic Viewset for GET (Details), UPDATE and DELETE </summary>

backend/views.py:

```pybs
class ArticleDetailsViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
```

```py
from django.shortcuts import render, HttpResponse
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics

from rest_framework import mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                    mixins.CreateModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetailsViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # lookup_field = 'slug'


# VIEWSETS AND ROUTERS

# class ArticleViewSet(viewsets.ViewSet):
#     def list(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)

# class ArticleDetailsViewSet(viewsets.ViewSet):
#     queryset = Article.objects.all()

#     def retrieve(self, request, pk=None):
#         article = get_object_or_404(self.queryset, id=pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     def update(self, request, pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset, id=pk)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset, id=pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# GENERIC API VIEWS

# class ArticleList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleDetails(generics. RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     lookup_field = 'slug'

# USING MIXINS

# class ArticleList(mixins.ListModelMixin,mixins.CreateModelMixin,
#                 generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ArticleDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     lookup_field = 'slug'

#     def get(self, request, slug, *args, **kwargs):
#         return self.retrieve(request, slug=slug)

#     def put(self, request, slug, *args, **kwargs):
#         return self.update (request, slug=slug)

#     def delete (self, request, slug):
#         return self.destroy(request, slug=slug)

# CLASS BASED API VIEWS

# class ArticleList(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)

# class ArticleDetails(APIView):
#     def get_object(self, slug):
#         try:
#             return Article.objects.get(slug=slug)
#         except Article.DoesNotExist as e:
#             raise Http404 from e

#     def get(self, request, slug):
#         article = self.get_object(slug)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     def put(self, request, slug):
#         article = self.get_object(slug)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, slug):
#         article = self.get_object(slug)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# DECORATOR API VIEWS

# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response (serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view (['GET', 'PUT', 'DELETE'])
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist():
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#API VIEW FUNCTIONS

# @csrf_exempt
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)

#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == "DELETE":
#         article.delete()
#         return HttpResponse(status=204)

```

backend/urls.py:

```py
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, ArticleDetailsViewSet

app_name = 'backend'

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
router.register('articles', ArticleDetailsViewSet, basename='articles')
urlpatterns = router.urls

# urlpatterns = [
#     path('', include(router.urls))
# ]
```

GET(Details):

![](https://user-images.githubusercontent.com/32337103/221933882-913a661c-7dbd-4700-b056-f6312a2e14bd.png)

UPDATE:

![](https://user-images.githubusercontent.com/32337103/221933968-0a6ef85d-2436-47b2-bb5e-46ac75e19164.png)
![](https://user-images.githubusercontent.com/32337103/221934010-21dfdc89-f86d-4942-8894-b0eee0c39307.png)

DELETE:

![](https://user-images.githubusercontent.com/32337103/221934112-7078fc4c-e357-4595-8387-984300f86412.png)
![](https://user-images.githubusercontent.com/32337103/221934141-f47e0cb4-67bd-4854-9a06-26961fc3100b.png)
![](https://user-images.githubusercontent.com/32337103/221934327-066a65e1-2a3d-4e96-a59f-99b4231ccb29.png)

</details>

<details>
  <summary>86. Model Viewset for GET, POST, GET(Details), UPDATE and DELETE</summary>

backend/views.py:

```pybs
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'
```

```py
from django.shortcuts import render, HttpResponse
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics

from rest_framework import mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'


# GENERIC VIEWSETS

# class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
#                     mixins.CreateModelMixin):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleDetailsViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin,
#                             mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     # lookup_field = 'slug'


# VIEWSETS AND ROUTERS

# class ArticleViewSet(viewsets.ViewSet):
#     def list(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)

# class ArticleDetailsViewSet(viewsets.ViewSet):
#     queryset = Article.objects.all()

#     def retrieve(self, request, pk=None):
#         article = get_object_or_404(self.queryset, id=pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     def update(self, request, pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset, id=pk)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset, id=pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# GENERIC API VIEWS

# class ArticleList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleDetails(generics. RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     lookup_field = 'slug'

# USING MIXINS

# class ArticleList(mixins.ListModelMixin,mixins.CreateModelMixin,
#                 generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ArticleDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     lookup_field = 'slug'

#     def get(self, request, slug, *args, **kwargs):
#         return self.retrieve(request, slug=slug)

#     def put(self, request, slug, *args, **kwargs):
#         return self.update (request, slug=slug)

#     def delete (self, request, slug):
#         return self.destroy(request, slug=slug)

# CLASS BASED API VIEWS

# class ArticleList(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)

# class ArticleDetails(APIView):
#     def get_object(self, slug):
#         try:
#             return Article.objects.get(slug=slug)
#         except Article.DoesNotExist as e:
#             raise Http404 from e

#     def get(self, request, slug):
#         article = self.get_object(slug)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     def put(self, request, slug):
#         article = self.get_object(slug)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, slug):
#         article = self.get_object(slug)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# DECORATOR API VIEWS

# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response (serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view (['GET', 'PUT', 'DELETE'])
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist():
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#API VIEW FUNCTIONS

# @csrf_exempt
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)

#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == "DELETE":
#         article.delete()
#         return HttpResponse(status=204)
```

backend/urls.py:

```py
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet

app_name = 'backend'

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
# router.register('articles', ArticleDetailsViewSet, basename='articles')
urlpatterns = router.urls

# urlpatterns = [
#     path('', include(router.urls))
# ]
```

GET:

<img width="1157" alt="image" src="https://user-images.githubusercontent.com/32337103/221937211-d8987365-769b-4f23-83de-317947a5e150.png">

POST:

![](https://user-images.githubusercontent.com/32337103/221945601-ebe2b304-bcf8-496e-b85f-d0111d591f2a.png)
![](https://user-images.githubusercontent.com/32337103/221945691-051beea3-d473-4314-a0a9-32bc1f859e82.png)
![](https://user-images.githubusercontent.com/32337103/221945644-57d978a3-8705-4dc1-889a-3e7fa437a765.png)

GET(Details):

![](https://user-images.githubusercontent.com/32337103/221949605-b738f31d-d7a0-4530-892b-2a13f1493048.png)

UPDATE:

![](https://user-images.githubusercontent.com/32337103/221949712-23dea395-9b8e-4bca-8493-ab2230b13f17.png)
![](https://user-images.githubusercontent.com/32337103/221949776-157a9e3a-95f5-42ef-93cd-0c2a773a955a.png)

DELETE:

![](https://user-images.githubusercontent.com/32337103/221949834-352f99a5-8b7e-4a45-833b-bf2d7492a4a4.png)
![](https://user-images.githubusercontent.com/32337103/221949887-2c5e826a-c139-4887-995d-b57e4f3c8b85.png)

</details>

<details>
  <summary>87. Global Token Authentication </summary>

backend/models.py:

```py
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")

    def __str__(self):
        return self.title
```

```pybs
DELETE db.sqlite3 and Migration Files
```

```pybs
python manage.py makemigrations
```

```pybs
python manage.py migrate
```

```pybs
python manage.py createsuperuser
```

![](https://user-images.githubusercontent.com/32337103/221964220-551016b7-be45-42e6-a73e-a5b4bb282844.png)

```pybs
python manage.py runserver
```

http://127.0.0.1:8000/admin/

![](https://user-images.githubusercontent.com/32337103/221964849-71c93127-95bd-4484-80db-238323a027d5.png)
![](https://user-images.githubusercontent.com/32337103/221964888-f52d0981-bc9a-4a7f-9fc0-d4aeae598ea6.png)
![](https://user-images.githubusercontent.com/32337103/221965140-568bb593-ef01-4cc8-b1ba-7fdde53474aa.png)
![](https://user-images.githubusercontent.com/32337103/221965181-a62722d1-6543-4b11-a7f0-1f9dbe67762e.png)

blogapi/settings.py:

```pybs
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        #'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}
```

```pybs
INSTALLED_APPS = [
    ...
    'rest_framework.authtoken',
]
```

```pybs
python manage.py migrate
```

![](https://user-images.githubusercontent.com/32337103/221966541-adf3d12c-7ba8-4276-8bef-8cfb41b50d26.png)
![](https://user-images.githubusercontent.com/32337103/221966776-f71a6d90-89ca-4f86-aa2e-59e91bacb157.png)
![](https://user-images.githubusercontent.com/32337103/221967066-2925e16a-28d5-4cf7-b0dd-5955e9e086cf.png)

blogapi/urls.py:

```pybs
urlpatterns = [
    ---
    path('api-auth/', include('rest_framework.urls'))
]
```

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
```

The default permission policy may be set globally, using the DEFAULT_PERMISSION_CLASSES setting.

```pybs
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

If not specified, this setting defaults to allowing unrestricted access:

```pybs
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
    'rest_framework.permissions.AllowAny',
    ]
}
```

blogapi/settings.py:

```py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        #'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

![](https://user-images.githubusercontent.com/32337103/221989072-4a93fa5d-29c6-4a24-ad47-3a04551a55a9.png)
![](https://user-images.githubusercontent.com/32337103/221989128-93924aad-51a5-4ee9-9fe8-4ba04f80192d.png)

Using Postman:

![](https://user-images.githubusercontent.com/32337103/221989893-b364a925-171c-4a73-ab81-ab2c07858ac2.png)
![](https://user-images.githubusercontent.com/32337103/221990049-fd12ac23-f0e2-423f-bb29-044c2f215273.png)
![](https://user-images.githubusercontent.com/32337103/221990294-4d325290-9ddb-4207-8869-0da7a0025672.png)

</details>

<details>
  <summary>88. Class Based Token Authentication </summary>

blogapi/settings.py:

```py
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         #'rest_framework.authentication.BasicAuthentication',
#         'rest_framework.authentication.TokenAuthentication',
#         'rest_framework.authentication.SessionAuthentication',
#     ],
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticated',
#     ]
# }

```

backend/views.py:

```pybs
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'

    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, SessionAuthentication)
```

```py
from django.shortcuts import render, HttpResponse
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'

    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, SessionAuthentication)

# GENERIC VIEWSETS

# class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
#                     mixins.CreateModelMixin):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleDetailsViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin,
#                             mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     # lookup_field = 'slug'


# VIEWSETS AND ROUTERS

# class ArticleViewSet(viewsets.ViewSet):
#     def list(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)

# class ArticleDetailsViewSet(viewsets.ViewSet):
#     queryset = Article.objects.all()

#     def retrieve(self, request, pk=None):
#         article = get_object_or_404(self.queryset, id=pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     def update(self, request, pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset, id=pk)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset, id=pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# GENERIC API VIEWS

# class ArticleList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleDetails(generics. RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     lookup_field = 'slug'

# USING MIXINS

# class ArticleList(mixins.ListModelMixin,mixins.CreateModelMixin,
#                 generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ArticleDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     lookup_field = 'slug'

#     def get(self, request, slug, *args, **kwargs):
#         return self.retrieve(request, slug=slug)

#     def put(self, request, slug, *args, **kwargs):
#         return self.update (request, slug=slug)

#     def delete (self, request, slug):
#         return self.destroy(request, slug=slug)

# CLASS BASED API VIEWS

# class ArticleList(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)

# class ArticleDetails(APIView):
#     def get_object(self, slug):
#         try:
#             return Article.objects.get(slug=slug)
#         except Article.DoesNotExist as e:
#             raise Http404 from e

#     def get(self, request, slug):
#         article = self.get_object(slug)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     def put(self, request, slug):
#         article = self.get_object(slug)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, slug):
#         article = self.get_object(slug)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# DECORATOR API VIEWS

# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response (serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view (['GET', 'PUT', 'DELETE'])
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist():
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#API VIEW FUNCTIONS

# @csrf_exempt
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)

#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == "DELETE":
#         article.delete()
#         return HttpResponse(status=204)

```

backend/urls.py:

```py
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet

app_name = 'backend'

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
# router.register('articles', ArticleDetailsViewSet, basename='articles')
urlpatterns = router.urls

# urlpatterns = [
#     path('', include(router.urls))
# ]
```

![](https://user-images.githubusercontent.com/32337103/222083634-3ff1f890-6b1b-434e-8cf3-843f5d7d676d.png)
![](https://user-images.githubusercontent.com/32337103/222084097-47b2761f-7e62-4dba-8621-c988b9685622.png)
![](https://user-images.githubusercontent.com/32337103/222084200-5d8b6113-81d3-4691-b6d9-815f27e885d3.png)
![](https://user-images.githubusercontent.com/32337103/222084708-41705490-46b0-479f-a245-319a36eb25fc.png)
![](https://user-images.githubusercontent.com/32337103/222084877-e1b9f08e-2563-4fd8-aac1-f60278f97088.png)

backend/serializers.py:

```pybs
author = serializers.StringRelatedField()
```

```py
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    author = serializers.StringRelatedField()
    class Meta:
        model = Article
        fields = '__all__'

# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     description = serializers.CharField()
#     slug = serializers.SlugField(max_length=200)
#     published = serializers.DateTimeField(read_only=True)

# def create(self, validated_data):
#     return Article.objects.create(**validated_data)

# def update(self, instance, validated_data):
#     instance.title = validated_data.get('title', instance.title)
#     instance.description = validated_data.get('description', instance.description)
#     instance.slug = validated_data.get('slug', instance.slug)
#     instance.published = validated_data.get('published', instance.published)
#     instance.save()
#     return instance
```

![](https://user-images.githubusercontent.com/32337103/222086299-2f02efb7-06e2-498f-8777-589b19296b2e.png)

</details>

<details>
  <summary>89. Using DJ Rest Auth for User Registration </summary>

```pybs
pip install dj-rest-auth
```

blogapi/settings.py:

```pybs
INSTALLED_APPS = (
    ...,
    'rest_framework',
    'rest_framework.authtoken',
    ...,
    'dj_rest_auth'
)
```

```py
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'backend',
]
```

blogapi/urls.py:

```pybs
urlpatterns = [
    ...,
    path('dj-rest-auth/', include('dj_rest_auth.urls'))
]
```

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls'))
]
```

```pybs
python manage.py migrate
```

```pybs
pip install django-allauth
```

blogapi/settings.py:

```pybs
INSTALLED_APPS = (
    ...,
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
)

SITE_ID = 1
```

```py
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'backend',
]

SITE_ID = 1
```

blogapi/urls.py:

```pybs
urlpatterns = [
    ...,
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))
]
```

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))
]

```

```pybs
python manage.py migrate
```

![](https://user-images.githubusercontent.com/32337103/222104712-3c0b8477-cb3f-435b-817a-c4942ec991ad.png)
![](https://user-images.githubusercontent.com/32337103/222105622-ddd61373-c75b-44c6-bd1a-e244f953e12a.png)
![](https://user-images.githubusercontent.com/32337103/222105909-b8ca29cf-b798-44c1-96d5-c884e675667a.png)

blogapi/settings.py:

```pybs
ACCOUNT_EMAIL_VERIFICATION = 'none' # "mandatory | optional"
ACCOUNT_AUTHENTICATION_METHOD = 'username' # 'email'
ACCOUNT_EMAIL_REQUIRED = False
```

![](https://user-images.githubusercontent.com/32337103/222210623-4a193ca4-9c6d-4fbc-be81-de8cff647e1b.png)

http://127.0.0.1:8000/dj-rest-auth/

![](https://user-images.githubusercontent.com/32337103/222211170-1d5cc22f-fd3a-4682-b868-6e4115f5fcba.png)

http://127.0.0.1:8000/dj-rest-auth/registration/

![](https://user-images.githubusercontent.com/32337103/222211602-1ff30f24-ab62-43b6-b4d9-8612f091d4e5.png)
![](https://user-images.githubusercontent.com/32337103/222211927-f02075a4-4ddd-4f4e-82db-2e5246bb5604.png)

http://127.0.0.1:8000/dj-rest-auth/login/

![](https://user-images.githubusercontent.com/32337103/222212275-cb6c31ea-5707-45b7-8638-16fcf166d2a0.png)
![](https://user-images.githubusercontent.com/32337103/222212374-63fe536c-e69a-408d-ba10-5fe431360a6f.png)
![](https://user-images.githubusercontent.com/32337103/222212455-1a864ee4-2b6b-4c16-83b2-20596f0e4acf.png)

http://127.0.0.1:8000/dj-rest-auth/logout/

![](https://user-images.githubusercontent.com/32337103/222213293-0d8f22c9-e048-4729-9716-a4f8be82499e.png)
![](https://user-images.githubusercontent.com/32337103/222213391-ccd51bc8-4929-4469-ae3d-5a276e5a6aff.png)
![](https://user-images.githubusercontent.com/32337103/222213820-6479e884-ad98-4707-930a-204afc4e97e4.png)

Using Postman:

![](https://user-images.githubusercontent.com/32337103/222214363-9e2003b9-b816-47d0-90c8-c24a628973c1.png)
![](https://user-images.githubusercontent.com/32337103/222214509-cb9972fc-3c89-4b77-a1ef-4552e4236dfb.png)
![](https://user-images.githubusercontent.com/32337103/222214564-100fb4b5-e7fa-4258-8d5f-e438834cff82.png)

</details>

<details>
  <summary>90. Overriding perform_create Method </summary>

backend/views.py:

```pybs
def perform_create(self, serializer):
        serializer.save(author=self.request.user)
```

```py
from django.shortcuts import render, HttpResponse
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'

    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, SessionAuthentication)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# GENERIC VIEWSETS

# class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
#                     mixins.CreateModelMixin):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleDetailsViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin,
#                             mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     # lookup_field = 'slug'


# VIEWSETS AND ROUTERS

# class ArticleViewSet(viewsets.ViewSet):
#     def list(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)

# class ArticleDetailsViewSet(viewsets.ViewSet):
#     queryset = Article.objects.all()

#     def retrieve(self, request, pk=None):
#         article = get_object_or_404(self.queryset, id=pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     def update(self, request, pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset, id=pk)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset, id=pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# GENERIC API VIEWS

# class ArticleList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleDetails(generics. RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     lookup_field = 'slug'

# USING MIXINS

# class ArticleList(mixins.ListModelMixin,mixins.CreateModelMixin,
#                 generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ArticleDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     lookup_field = 'slug'

#     def get(self, request, slug, *args, **kwargs):
#         return self.retrieve(request, slug=slug)

#     def put(self, request, slug, *args, **kwargs):
#         return self.update (request, slug=slug)

#     def delete (self, request, slug):
#         return self.destroy(request, slug=slug)

# CLASS BASED API VIEWS

# class ArticleList(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)

# class ArticleDetails(APIView):
#     def get_object(self, slug):
#         try:
#             return Article.objects.get(slug=slug)
#         except Article.DoesNotExist as e:
#             raise Http404 from e

#     def get(self, request, slug):
#         article = self.get_object(slug)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     def put(self, request, slug):
#         article = self.get_object(slug)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, slug):
#         article = self.get_object(slug)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# DECORATOR API VIEWS

# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response (serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view (['GET', 'PUT', 'DELETE'])
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist():
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#API VIEW FUNCTIONS

# @csrf_exempt
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)

#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == "DELETE":
#         article.delete()
#         return HttpResponse(status=204)

```

![](https://user-images.githubusercontent.com/32337103/222216588-ee24cc50-96b5-4d32-af80-ee6c0bdc271d.png)
![](https://user-images.githubusercontent.com/32337103/222216667-684dac34-afe0-42fd-9183-0f5faf9e6292.png)
![](https://user-images.githubusercontent.com/32337103/222216727-e2cf55be-e2f8-423d-a8b1-f2aaae753c5a.png)

</details>

<details>
  <summary>91. Custom Permission </summary>

backend/permissions.py:

```py
from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
```

backend/views.py:

```py
from django.shortcuts import render, HttpResponse
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .permissions import IsAuthor

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'

    permission_classes = [IsAuthenticated, IsAuthor]
    authentication_classes = (TokenAuthentication, SessionAuthentication)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# GENERIC VIEWSETS

# class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
#                     mixins.CreateModelMixin):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleDetailsViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin,
#                             mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     # lookup_field = 'slug'


# VIEWSETS AND ROUTERS

# class ArticleViewSet(viewsets.ViewSet):
#     def list(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)

# class ArticleDetailsViewSet(viewsets.ViewSet):
#     queryset = Article.objects.all()

#     def retrieve(self, request, pk=None):
#         article = get_object_or_404(self.queryset, id=pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     def update(self, request, pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset, id=pk)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset, id=pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# GENERIC API VIEWS

# class ArticleList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleDetails(generics. RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     lookup_field = 'slug'

# USING MIXINS

# class ArticleList(mixins.ListModelMixin,mixins.CreateModelMixin,
#                 generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ArticleDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     lookup_field = 'slug'

#     def get(self, request, slug, *args, **kwargs):
#         return self.retrieve(request, slug=slug)

#     def put(self, request, slug, *args, **kwargs):
#         return self.update (request, slug=slug)

#     def delete (self, request, slug):
#         return self.destroy(request, slug=slug)

# CLASS BASED API VIEWS

# class ArticleList(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)

# class ArticleDetails(APIView):
#     def get_object(self, slug):
#         try:
#             return Article.objects.get(slug=slug)
#         except Article.DoesNotExist as e:
#             raise Http404 from e

#     def get(self, request, slug):
#         article = self.get_object(slug)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     def put(self, request, slug):
#         article = self.get_object(slug)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, slug):
#         article = self.get_object(slug)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# DECORATOR API VIEWS

# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response (serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view (['GET', 'PUT', 'DELETE'])
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist():
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#API VIEW FUNCTIONS

# @csrf_exempt
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)

#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == "DELETE":
#         article.delete()
#         return HttpResponse(status=204)
```

![](https://user-images.githubusercontent.com/32337103/222218773-531043f3-bcac-479d-99a5-23ccb52945f1.png)
![](https://user-images.githubusercontent.com/32337103/222218881-3b2dede6-bb6c-421e-b51a-306e3fe232ee.png)
![](https://user-images.githubusercontent.com/32337103/222218982-11769bb5-aae8-49a3-bad6-e9f898aecf0c.png)
![](https://user-images.githubusercontent.com/32337103/222219031-0c844d13-2306-47fb-be76-74d3737d8adf.png)
![](https://user-images.githubusercontent.com/32337103/222219080-73419723-b744-4b9f-ac85-bd1958869bcb.png)
![](https://user-images.githubusercontent.com/32337103/222219141-6dc009bb-e0c7-4afe-aa91-2a1b197d7bb6.png)

</details>

<details>
  <summary>92. Deploy Django Rest Framework to Heroku </summary>

```pybs
pip install whitenoise
```

blogapi/settings.py:

```pybs
MIDDLEWARE = [
    # ...
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # ...
]
```

```py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

```

```pybs
STATIC_ROOT = BASE_DIR / "staticfiles"
OR
import os
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

```py
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

```pybs
 python manage.py collectstatic
```

```pybs
pip install gunicorn
```

```pybs
pip freeze > requirements.txt
```

```pybs
Create Github Repository - blogapi
```

```pybs
Create a .gitignore file
```

Create Procfile -

Procfile:

```pybs
web: gunicorn blogapi.wsgi
```

Push to Github -

```pybs
echo "# blogapi" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/omeatai/blogapi.git
git push -u origin main

git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/omeatai/blogapi.git
git push -u origin main
```

![](https://user-images.githubusercontent.com/32337103/222231832-5542b392-94d6-4fe4-8120-8b777f0ea4a5.png)

Deploy App on Heroku:

![](https://user-images.githubusercontent.com/32337103/222233403-6d3215c9-f404-4955-94f2-1ce1d9bada7a.png)
![](https://user-images.githubusercontent.com/32337103/222233802-557909da-aa95-4c95-8117-aa8105247aa0.png)
![](https://user-images.githubusercontent.com/32337103/222235459-e85766a8-7342-423b-9719-2e57a7aad13f.png)

blogapi/settings.py:

```py
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['blog-api-ifeanyi.herokuapp.com', '127.0.0.1', 'localhost']
```

```pybs
git add .
git add -f db.sqlite3
git commit -m "next commit"
git push
```

![](https://user-images.githubusercontent.com/32337103/222238082-b567a7d2-4cae-4197-89fc-24be6cae52dc.png)
![](https://user-images.githubusercontent.com/32337103/222238211-00e19fda-84d3-47b1-ac11-46585936195e.png)
![](https://user-images.githubusercontent.com/32337103/222274339-b937a549-3137-49fe-80c4-2ac6bc0862cd.png)
![](https://user-images.githubusercontent.com/32337103/222274436-e7157567-4dac-45d0-8220-78d55b1f55b8.png)

</details>

<details>
  <summary>93. Migrate from SQLite to PostgreSQL </summary>

```pybs
pip install psycopg2
```

```pybs
pip install python-dotenv
```

```pybs
pip install dj_database_url
```

```pybs
pip freeze > requirements.txt
```

.env:

```pybs
PGDATABASE= railway
PGHOST= *******PGHOST*******
PGPASSWORD= ********PGPASSWORD******
PGPORT= 5622
PGUSER= ****PGUSER****
SECRET_KEY="***********SECRET_KEY********"
DATABASE_URL=postgresql://****PGUSER****:********PGPASSWORD******@******PGHOST*******:5622/railway
```

blogapi/settings.py:

```pybs
from pathlib import Path

import dj_database_url
import os
from dotenv import load_dotenv
load_dotenv()  # loads the configs from .env

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(),
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # },
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': os.environ["PGDATABASE"],
    #     'USER': os.environ["PGUSER"],
    #     'PASSWORD': os.environ["PGPASSWORD"],
    #     'HOST': os.environ["PGHOST"],
    #     'PORT': os.environ["PGPORT"]
    # }

}
```

```py
"""
Django settings for blogapi project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import dj_database_url
import os
from dotenv import load_dotenv
load_dotenv()  # loads the configs from .env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['blog-api-ifeanyi.herokuapp.com', '127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'backend',
]

SITE_ID = 1

# REST_USE_JWT = True
# JWT_AUTH_COOKIE = 'jwt-auth'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'blogapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'blogapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(),
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # },
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': os.environ["PGDATABASE"],
    #     'USER': os.environ["PGUSER"],
    #     'PASSWORD': os.environ["PGPASSWORD"],
    #     'HOST': os.environ["PGHOST"],
    #     'PORT': os.environ["PGPORT"]
    # }

}

ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'username' # 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none' # "mandatory | optional"

# AUTH_USER_MODEL = 'users.CustomUser'
# LOGIN_REDIRECT_URL = 'xxx:index'
# DEFAULT_FROM_EMAIL = 'tttt@gmail.com'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'
# ACCOUNT_LOGOUT_ON_GET = True
# ACCOUNT_EMAIL_SUBJECT_PREFIX = ''
# ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
# ACCOUNT_UNIQUE_USERNAME = True
# ACCOUNT_USER_EMAIL_FIELD = 'email'

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         #'rest_framework.authentication.BasicAuthentication',
#         'rest_framework.authentication.TokenAuthentication',
#         'rest_framework.authentication.SessionAuthentication',
#     ],
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticated',
#     ]
# }

# AUTHENTICATION_BACKENDS = [
#     # allauth specific authentication methods, such as login by e-mail
#     'allauth.account.auth_backends.AuthenticationBackend',
#     # Needed to login by username in Django admin, regardless of allauth
#     'django.contrib.auth.backends.ModelBackend',
# ]

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE =  'django.contrib.staticfiles.storage.StaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

```

```pybs
python manage.py migrate
```

```pybs
python manage.py createsuperuser
```

Railway Postgresql Database:

![](https://user-images.githubusercontent.com/32337103/222377245-e125397c-1ec3-46ce-87fb-27ad037bad5f.png)
![](https://user-images.githubusercontent.com/32337103/222377314-7720eb41-ba70-4723-b222-0cc1ee4ac820.png)

```pybs
git add .
git commit -m "Postgresql commit"
git branch -M main
git push -u origin main
```

![](https://user-images.githubusercontent.com/32337103/222379807-48df3bee-132b-4523-8c96-a802e91573bd.png)
![](https://user-images.githubusercontent.com/32337103/222379921-3e176eb3-cce7-4586-9a58-aaf82e422539.png)

</details>

+BACKEND REST API FOR QUESTION AND ANSWER APP

<details>
  <summary>94. Introduction </summary>

```pybs
 python -m venv venv
 source venv/bin/activate
```

```pybs
pip install --upgrade pip
```

```pybs
pip install django
pip install djangorestframework
```

```pybs
django-admin startproject DJRESTQA .
```

```pybs
pip install dj-rest-auth
```

DJRESTQA/settings.py:

```pybs
INSTALLED_APPS = (
    ...,
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
)
```

```py
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
]
```

DJRESTQA/urls.py:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
]
```

```pybs
pip install django-allauth
```

DJRESTQA/settings.py:

```pybs
INSTALLED_APPS = (
    ...,
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
)

SITE_ID = 1
```

```py
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
]

SITE_ID = 1
```

DJRESTQA/urls.py:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))
]
```

DJRESTQA/settings.py:

```pybs
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = False
```

```py
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = False
```

```pybs
python manage.py makemigrations
```

```pybs
python manage.py migrate
```

```py
python manage.py createsuperuser
```

```py
python manage.py runserver
```

![](https://user-images.githubusercontent.com/32337103/222427057-dc4033c4-d7dd-4e52-93e1-28ec9c8212f6.png)
![](https://user-images.githubusercontent.com/32337103/222427282-4478fcfe-f955-4994-8940-6161cb3e723d.png)
![](https://user-images.githubusercontent.com/32337103/222427406-46b55921-39b8-4a2f-900a-d5c613b66dc7.png)
![](https://user-images.githubusercontent.com/32337103/222427648-43899095-1391-402c-ad65-7e67c95f9143.png)
![](https://user-images.githubusercontent.com/32337103/222427679-d281e028-e86e-4096-917e-ca75582f1a77.png)

</details>

<details>
  <summary>95. Create App and Models </summary>

```pybs
python manage.py startapp qa
```

DJRESTQA/settings.py:

```py
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'qa',
]
```

qa/models.py:

```py
from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name=' answers')
    description = models.TextField()
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.question.title} - {self.question.author.username}"
```

```pybs
python manage.py makemigrations
python manage.py migrate
```

qa/admin.py:

```py
from django.contrib import admin
from .models import Question, Answer
# Register your models here.


admin.site.register(Question)
admin.site.register (Answer)
```

```pybs
python manage.py runserver
```

![](https://user-images.githubusercontent.com/32337103/222462366-9ddfc7d4-77c6-4472-afb7-6acaa9db3757.png)
![](https://user-images.githubusercontent.com/32337103/222462888-6311184d-7e13-4d0a-8827-f220329d1b8e.png)
![](https://user-images.githubusercontent.com/32337103/222463005-fa010c66-f638-4ac6-8a61-78d0ad88b021.png)
![](https://user-images.githubusercontent.com/32337103/222463652-86c2aa85-6238-4f88-843a-8c5b0a246e36.png)
![](https://user-images.githubusercontent.com/32337103/222464288-e74febab-ff64-4dae-ba72-3e655956b08a.png)

</details>

<details>
  <summary>96. Create Dynamic Slug </summary>

qa/signals.py:

```py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Question
from django.utils.text import slugify


@receiver (pre_save, sender=Question)
def add_slug(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.title)
        instance.slug = slug
```

qa/apps.py:

```py
from django.apps import AppConfig


class QaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'qa'

    def ready(self):
        import qa.signals
```

qa/init.py:

```py
default_app_config = 'qa.apps.QaConfig'
```

qa/models.py:

```py
from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    description = models.TextField()
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.question.title} - {self.question.author.username}"
```

```pybs
python manage.py shell
```

```pybs
>>> from django.contrib.auth import get_user_model
>>> user = get_user_model()
>>> u = user.objects.first()
>>> from qa.models import Question
>>> q = Question(title = 'This is my title', body='This is my description', author=u)
>>> q.save()
```

![](https://user-images.githubusercontent.com/32337103/222468666-01778daa-7672-471c-8961-a5318b0a2f05.png)
![](https://user-images.githubusercontent.com/32337103/222468759-ac5ed344-d28b-479e-9e69-6316fc26641e.png)

</details>

<details>
  <summary>97. Creating Serializers and Viewsets for Questions </summary>

qa/serializers.py:

```py
from rest_framework import serializers
from .models import Question, Answer


class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Answer
        fields = '__all__'
```

qa/views.py:

```py
from django.shortcuts import render
from rest_framework import viewsets
from .models import Question
from .serializers import QuestionSerializer
# Create your views here.


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
```

DJRESTQA/urls.py:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('', include('qa.urls')),
]
```

qa/urls.py:

```py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet


router = DefaultRouter ()
router.register('question', QuestionViewSet)


urlpatterns = [
    path('', include(router.urls))
]
```

![](https://user-images.githubusercontent.com/32337103/222477230-e48abf92-f4e3-4b17-85a1-340e9c99031d.png)
![](https://user-images.githubusercontent.com/32337103/222477989-2fc3ad5b-bb44-495c-85ef-f6a21ca25cbe.png)
![](https://user-images.githubusercontent.com/32337103/222478053-860596b1-1da5-4e2c-9c5f-52415f755afc.png)
![](https://user-images.githubusercontent.com/32337103/222478466-c8510675-8494-4d66-8887-2cc59a90f268.png)

qa/views.py:

```pybs
lookup_field = 'slug'
```

```py
from django.shortcuts import render
from rest_framework import viewsets
from .models import Question
from .serializers import QuestionSerializer
# Create your views here.


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
```

![](https://user-images.githubusercontent.com/32337103/222480072-7fd84cf0-5e43-458e-83ea-cee25cc21a17.png)
![](https://user-images.githubusercontent.com/32337103/222480225-3a39e315-a017-4717-8acb-66ca5afa094a.png)
![](https://user-images.githubusercontent.com/32337103/222480791-3d672b63-99f9-4b39-ba46-fcf7f639091b.png)
![](https://user-images.githubusercontent.com/32337103/222480862-9723b5aa-0707-4aa3-b6ce-ff061e4bfcd2.png)
![](https://user-images.githubusercontent.com/32337103/222480945-5d0fac81-b78c-40fa-86f8-999077c7713b.png)

</details>

<details>
  <summary>98. Creating Viewsets for Answers (GET, POST) </summary>

qa/views.py:

```py
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer
from rest_framework import generics


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class AnswerCreate(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        user = self.request.user
        slug = self.kwargs.get('slug')
        question = get_object_or_404(Question, slug=slug)
        serializer.save(author=user, question=question)

class AnswerList(generics.ListAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Answer.objects.filter(question__slug=slug)
```

qa/serializers.py:

```py
from rest_framework import serializers
from .models import Question, Answer


class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Answer
        exclude = ['question']
        # fields = '__all__'
```

qa/models.py:

```py
from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    description = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.question.title} - {self.author.username}"
```

qa/urls.py:

```py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, AnswerCreate, AnswerList


router = DefaultRouter ()
router.register('question', QuestionViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('question/<slug:slug>/answercreate/', AnswerCreate.as_view()),
    path('question/<slug:slug>/answers/', AnswerList.as_view()),
]
```

![](https://user-images.githubusercontent.com/32337103/222544304-a68e1464-107a-4cd9-a896-c5d78d5d1435.png)
![](https://user-images.githubusercontent.com/32337103/222546832-6a7a11f7-a330-466e-a1c1-ed0b2ef82586.png)
![](https://user-images.githubusercontent.com/32337103/222546996-8c20c731-cf4f-4f4e-a064-4e7e1e8711fd.png)
![](https://user-images.githubusercontent.com/32337103/222547177-5526d094-29bd-4bff-b10e-8b7e7c4279bf.png)
![](https://user-images.githubusercontent.com/32337103/222547219-6e0227ba-2040-4161-84ee-7630237b4a69.png)

</details>

<details>
  <summary>99. Creating Viewsets for Answers (GET [Details], UPDATE, DELETE) </summary>

qa/views.py:

```pybs
class AnswerDeleteUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
```

```py
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer
from rest_framework import generics


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class AnswerCreate(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        user = self.request.user
        slug = self.kwargs.get('slug')
        question = get_object_or_404(Question, slug=slug)
        serializer.save(author=user, question=question)

class AnswerList(generics.ListAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Answer.objects.filter(question__slug=slug)

class AnswerDeleteUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
```

qa/serializers.py:

```py
from rest_framework import serializers
from .models import Question, Answer


class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Answer
        exclude = ['question']
        # fields = '__all__'
```

qa/models.py:

```py
from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    description = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.question.title} - {self.author.username}"
```

qa/urls.py:

```py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, AnswerCreate, AnswerList, AnswerDeleteUpdate


router = DefaultRouter ()
router.register('question', QuestionViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('question/<slug:slug>/answercreate/', AnswerCreate.as_view()),
    path('question/<slug:slug>/answers/', AnswerList.as_view()),
    path('answers/<int:pk>/', AnswerDeleteUpdate.as_view()),
]
```

![](https://user-images.githubusercontent.com/32337103/222800196-a9e44153-2f5b-4077-a443-9c6e8d2d30f5.png)
![](https://user-images.githubusercontent.com/32337103/222800296-cc61ef13-7e86-4e29-af02-c7d6feab0bdb.png)
![](https://user-images.githubusercontent.com/32337103/222800490-1f3eb5c4-66f2-4252-8b58-ba799f2ac1c9.png)
![](https://user-images.githubusercontent.com/32337103/222800527-77f779a0-eeda-4ece-8b7d-8eb43323d513.png)
![](https://user-images.githubusercontent.com/32337103/222800858-5e790897-da19-44db-b6c2-1e1e8996c86a.png)

</details>

<details>
  <summary>100. Registering New User </summary>

![](https://user-images.githubusercontent.com/32337103/222801927-78deb37f-b953-4ab1-93c7-79e68f896891.png)
![](https://user-images.githubusercontent.com/32337103/222802027-cd07bf70-5a66-4329-8df2-85e4821a1f78.png)

DJRESTQA/urls.py:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('', include('qa.urls')),
]

```

![](https://user-images.githubusercontent.com/32337103/222801895-eb7e8cdf-0378-4224-b0fe-4956abe2087b.png)
![](https://user-images.githubusercontent.com/32337103/222802153-c87ef447-d354-4f84-b3fc-b3b209ab4207.png)
![](https://user-images.githubusercontent.com/32337103/222802477-f4d79dcb-5623-4cee-8023-fe1a92f2c237.png)
![](https://user-images.githubusercontent.com/32337103/222802373-8cc050a7-da3c-40e5-a770-b6cefae3bcf6.png)
![](https://user-images.githubusercontent.com/32337103/222802640-81ab3799-e8ab-49a8-94c4-b52b743c6f7a.png)
![](https://user-images.githubusercontent.com/32337103/222802667-3560427d-fd62-47f0-a929-12d16fbfb385.png)
![](https://user-images.githubusercontent.com/32337103/222802727-7dbff1d8-3684-4177-ac21-0996d861a918.png)
![](https://user-images.githubusercontent.com/32337103/222803104-9eb2a3bb-d1f2-4544-b099-5851ab9c558c.png)
![](https://user-images.githubusercontent.com/32337103/222803154-765aab0f-fa38-48ce-94fb-666debde25ba.png)
![](https://user-images.githubusercontent.com/32337103/222803202-7a775ddf-e302-45e0-84b0-0508258d42c6.png)

</details>

<details>
  <summary>101. Using Token Authentication to restrict Users from Accessing Content</summary>

DJRESTQA/settings.py:

```pybs
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
    'rest_framework.authentication.TokenAuthentication',
    'rest_framework.authentication.SessionAuthentication',
    ]
}

```

```py
"""
Django settings for DJRESTQA project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ""

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'qa',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DJRESTQA.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'DJRESTQA.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
    'rest_framework.authentication.TokenAuthentication',
    'rest_framework.authentication.SessionAuthentication',
    ]
}

ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = False


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

```

qa/views.py:

```pybs
from rest_framework.permissions import IsAuthenticated

permission_classes = [IsAuthenticated]
```

```py
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class AnswerCreate(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        slug = self.kwargs.get('slug')
        question = get_object_or_404(Question, slug=slug)
        serializer.save(author=user, question=question)

class AnswerList(generics.ListAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Answer.objects.filter(question__slug=slug)

class AnswerDeleteUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
```

![](https://user-images.githubusercontent.com/32337103/222808157-2bea333c-bc03-421a-a175-f6a395a05d0a.png)
![](https://user-images.githubusercontent.com/32337103/222808208-80ff52b5-9ae9-49dd-85cd-65bf0c6443f1.png)
![](https://user-images.githubusercontent.com/32337103/222808270-0619ba0a-5f99-4de8-94a1-30cc9a9f0d49.png)
![](https://user-images.githubusercontent.com/32337103/222808336-6146a4af-9e60-4bb0-8389-2c4a0d0b656e.png)
![](https://user-images.githubusercontent.com/32337103/222808771-f4ef1309-1625-4e99-a94f-2b2ba343dddc.png)
![](https://user-images.githubusercontent.com/32337103/222808858-86e3abd3-e630-43aa-acee-aa3a4263d33c.png)

</details>

<details>
  <summary>102. Custom Permissions for restricting Users from editing others content</summary>

![](https://user-images.githubusercontent.com/32337103/222897912-503be374-3642-4e54-a38a-996a3a8e2360.png)
![](https://user-images.githubusercontent.com/32337103/222898019-7e4b25d3-dc9f-4429-8ace-d8f47716f009.png)

The default permission policy may be set globally, using the DEFAULT_PERMISSION_CLASSES setting. For example.

```pybs
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

If not specified, this setting defaults to allowing unrestricted access:

```pybs
'DEFAULT_PERMISSION_CLASSES': [
   'rest_framework.permissions.AllowAny',
]
```

You can also set the authentication policy on a per-view, or per-viewset basis, using the APIView class-based views.

```pybs
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class ExampleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)
```

Or, if you're using the @api_view decorator with function based views.

```pybs
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'status': 'request was permitted'
    }
    return Response(content)
```

- Note: when you set new permission classes via the class attribute or decorators you're telling the view to ignore the default list set in the settings.py file.

- Provided they inherit from rest_framework.permissions.BasePermission, permissions can be composed using standard Python bitwise operators. For example, IsAuthenticatedOrReadOnly could be written:

```pybs
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class ExampleView(APIView):
    permission_classes = [IsAuthenticated|ReadOnly]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)
```

AllowAny:

- The AllowAny permission class will allow unrestricted access, regardless of if the request was authenticated or unauthenticated.

- This permission is not strictly required, since you can achieve the same result by using an empty list or tuple for the permissions setting, but you may find it useful to specify this class because it makes the intention explicit.

IsAuthenticated:

- The IsAuthenticated permission class will deny permission to any unauthenticated user, and allow permission otherwise.

- This permission is suitable if you want your API to only be accessible to registered users.

IsAdminUser:

- The IsAdminUser permission class will deny permission to any user, unless user.is_staff is True in which case permission will be allowed.

- This permission is suitable if you want your API to only be accessible to a subset of trusted administrators.

IsAuthenticatedOrReadOnly:

- The IsAuthenticatedOrReadOnly will allow authenticated users to perform any request. Requests for unauthorised users will only be permitted if the request method is one of the "safe" methods; GET, HEAD or OPTIONS.

- This permission is suitable if you want to your API to allow read permissions to anonymous users, and only allow write permissions to authenticated users.

Custom permissions -

To implement a custom permission, override BasePermission and implement either, or both, of the following methods:

- .has_permission(self, request, view)
- .has_object_permission(self, request, view, obj)

The methods should return True if the request should be granted access, and False otherwise.

- If you need to test if a request is a read operation or a write operation, you should check the request method against the constant SAFE_METHODS, which is a tuple containing 'GET', 'OPTIONS' and 'HEAD'. For example:

```pybs
if request.method in permissions.SAFE_METHODS:
    # Check permissions for read-only request
else:
    # Check permissions for write request
```

The following is an example of a permission class that checks the incoming request's IP address against a blocklist, and denies the request if the IP has been blocked.

```pybs
from rest_framework import permissions

class BlocklistPermission(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        blocked = Blocklist.objects.filter(ip_addr=ip_addr).exists()
        return not blocked
```

You can also create object-level permissions, that are only run against operations that affect a particular object instance. For example:

```pybs
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user
```

qa/permissions.py:

```py
from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
```

qa/views.py:

```pybs
from .permissions import IsAuthor

permission_classes = [IsAuthenticated, IsAuthor]
```

```py
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthor


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, IsAuthor]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class AnswerCreate(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        slug = self.kwargs.get('slug')
        question = get_object_or_404(Question, slug=slug)
        serializer.save(author=user, question=question)

class AnswerList(generics.ListAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Answer.objects.filter(question__slug=slug)

class AnswerDeleteUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, IsAuthor]
```

![](https://user-images.githubusercontent.com/32337103/222931803-8a4ec010-c35f-4b84-95b6-92abdd2a5d10.png)
![](https://user-images.githubusercontent.com/32337103/222931822-bb5d831d-24f9-4234-a440-0c8bb9c9a5b2.png)
![](https://user-images.githubusercontent.com/32337103/222931833-14eed223-010e-4636-9f87-d58e22f14984.png)

</details>

<details>
  <summary>103. **Using Signals in Model to create Token for User </summary>

Go to settings.py and add the following:

```py
INSTALLED_APPS = (
    'rest_framework',
    'rest_framework.authtoken',
    'myapp',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}
```

Add the following code in myapp's models.py:

```py
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# This code is triggered whenever a new user has been created and saved to the database
#@receiver(post_save, sender=User)
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
```

Alternatively, if you want to be more explicit, create a file named signals.py under myapp project. Put the code above in it, then in **init**.py, write import signals.

```py
python manage.py migrate
python manage.py makemigrations
```

- Take a look in your database, a table named authtoken_token should be created with the following fields: key (this is the token value), created (the datetime it was created), user_id (a foreign key that references the auth_user table's id column).

- create a superuser with python manage.py createsuperuser. Now, take a look at the authtoken_token table in your DB with select \* from authtoken_token;, you should see a new entry has been added.

Using curl or a much simpler alternative httpie to test access to your api, I am using httpie:

```pybs
http GET 127.0.0.1:8000/whatever 'Authorization: Token your_token_value'
```

That's it. From now on, for any API access, you need to include the following value in the HTTP header (pay attention to the whitespaces):

```pybs
Authorization: Token your_token_value
```

(Optional) DRF also provides the ability to return a user's token if you supply the username and password. All you have to do is to include the following in urls.py:

```py
from rest_framework.authtoken import views

urlpatterns = [
    ...
    url(r'^api-token-auth/', views.obtain_auth_token),
]
```

Using httpie to verify:

```pybs
http POST 127.0.0.1:8000/api-token-auth/ username='admin' password='whatever'
```

In the return body, you should see this:

```pybs
{
    "token": "blah_blah_blah"
}
```

If tokens should only be created at certain times, then in your view code, you need to create and save the token at the appropriate time. Once the token is created (and saved), it will be usable for authentication:

```py
# View Pseudocode
from rest_framework.authtoken.models import Token

def token_request(request):
    if user_requested_token() and token_request_is_warranted():
        new_token = Token.objects.create(user=request.user)
```

If you've got a custom user manager that handles user creation (and activation), you may also perform this task like so:

```py
from rest_framework.authtoken.models import Token
# Other imports

class UserManager(BaseUserManager):

    def create_user(self, **kwargs):
        """
        This is your custom method for creating user instances.
        IMHO, if you're going to do this, you might as well use a signal.

        """
        # user = self.model(**kwargs) ...
        Token.objects.create(user=user)

    #You may also choose to handle this upon user activation.
    #Again, a signal works as well here.

    def activate_user(**kwargs):
        # user = ...
        Token.objects.create(user=user)
```

If you already have users created, then you may drop down into the python shell in your terminal and create Tokens for all the users in your db.

```pybs
>>> from django.contrib.auth.models import User
>>> from rest_framework.authtoken.models import Token
>>> for user in User.objects.all():
>>> ...    Token.objects.create(user=user)
```

```pybs
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
u = User.objects.get(username='admin')
token = Token.objects.create(user=u)
print token.key
```

</details>

<details>
  <summary>104. Using JWT Token Authentication </summary>

```py
pip install djangorestframework-simplejwt
```

DJRESTQA/settings.py:

```py
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    # 'rest_framework.authtoken',
    'dj_rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'qa',
]
```

```pybs
REST_FRAMEWORK = {
    ...
    'DEFAULT_AUTHENTICATION_CLASSES': (
        ...
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
    ...
}

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}
```

```py
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
    # 'rest_framework.authentication.TokenAuthentication',
    'rest_framework_simplejwt.authentication.JWTAuthentication',
    'rest_framework.authentication.SessionAuthentication',
    ],
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # ),
    'TOKEN_MODEL': None, #'app_name.ModelName', replace app_name and ModelName with custom token model
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = False
```

DJRESTQA/urls.py:

```pybs
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    ...
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ...
]
```

```py
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('', include('qa.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

```

![](https://user-images.githubusercontent.com/32337103/223049509-ac2b6dd1-86a5-4f00-90ca-e21af895686f.png)
![](https://user-images.githubusercontent.com/32337103/223078550-471c1898-02e8-4da9-ab48-591d9e483d2f.png)
![](https://user-images.githubusercontent.com/32337103/223079550-ed5d96d2-3082-4ee5-a36e-319170191897.png)
![](https://user-images.githubusercontent.com/32337103/223080091-3d567dc9-ded3-4dcb-970c-ff0917726898.png)

After 5 minutes:

![](https://user-images.githubusercontent.com/32337103/223079822-7e12eb16-0a2f-4540-a7fc-6f871b67d7c1.png)
![](https://user-images.githubusercontent.com/32337103/223081838-aa72a26a-099a-4f78-8a9b-70f21b1559a9.png)
![](https://user-images.githubusercontent.com/32337103/223081951-1808d692-6120-4b5e-8281-08f98e87b239.png)

</details>

<details>
  <summary>105. Deploy Django App to Python AnyWhere </summary>

DJRESTQA/settings.py:

```pybs
DEBUG = False

ALLOWED_HOSTS = ['localhost', 'omeatai.pythonanywhere.com']

import os

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

```pybs
python manage.py collectstatic
```

```pybs
pip freeze > requirements.txt
```

```pybs
Create Repository - djrestqa
```

```pybs
Create .gitignore file
```

```pybs
echo "# djrestqa" >> README.md

git init
git add . / git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/omeatai/djrestqa.git
git push -u origin main
```

![](https://user-images.githubusercontent.com/32337103/223110723-79a807d1-e2a9-49d0-abe5-ebde9285df0e.png)
![](https://user-images.githubusercontent.com/32337103/223111040-303d7fd3-2c54-4879-8eed-cb3aae28356f.png)

```pybs
git clone https://github.com/omeatai/djrestqa.git

cd djrestqa
mkvirtualenv --python=/usr/bin/python3.9 myenv
pip install -r requirements.txt
```

![](https://user-images.githubusercontent.com/32337103/223112838-9382345d-db25-4b39-a5f5-f99f4b474c7e.png)

![](https://user-images.githubusercontent.com/32337103/223116183-fef0ff7a-2488-491a-9737-ae99ebae335b.png)
![](https://user-images.githubusercontent.com/32337103/223117146-9397e1df-de76-4f42-9a77-e1616948216e.png)
![](https://user-images.githubusercontent.com/32337103/223117230-5c8767f0-04e5-4db4-9720-5c063ef647c6.png)
![](https://user-images.githubusercontent.com/32337103/223117419-947bfdcf-ffa1-4e3f-bb68-615354307dd4.png)

```pybs
import os
import sys

path = '/home/omeatai/djrestqa'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'DJRESTQA.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

![](https://user-images.githubusercontent.com/32337103/223118220-f43bd0bd-5c03-4d76-9ae0-82755a0f89c8.png)
![](https://user-images.githubusercontent.com/32337103/223118399-26a128ec-4402-4ebb-8eb2-16b49699c547.png)

https://omeatai.pythonanywhere.com/

![](https://user-images.githubusercontent.com/32337103/223118570-f7dee65f-6194-4b66-b729-aff270edf3fa.png)
![](https://user-images.githubusercontent.com/32337103/223118658-7a648f3c-1094-4285-bc9e-e76d42875195.png)
![](https://user-images.githubusercontent.com/32337103/223118777-d539531c-9de3-466b-be2f-5ddfc36a2b58.png)
![](https://user-images.githubusercontent.com/32337103/223119034-d040aa02-3173-489e-ac1a-ac5cf6157689.png)

</details>

+BACKEND INTEGRATION WITH REACTJS

<details>
  <summary>106. ReactJS Introduction </summary>

```pybs
npx create-react-app my-app
cd my-app
npm start
```

```pybs
npx create-react-app frontend
npm run start
```

frontend/src/index.js:

```pybs
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<h1>Hello, world!</h1>);
```

```js
import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
```

frontend/src/App.js:

```js
import React from "react";
import FirstComponent from "./components/FirstComponent";
import SecondComponent from "./components/SecondComponent";

function App() {
  return (
    <div>
      <h2>Welcome to DRF.</h2>
      <FirstComponent />
      <SecondComponent />
    </div>
  );
}

export default App;
```

frontend/src/components/FirstComponent.jsx:

```jsx
import React from "react";

const FirstComponent = () => {
  return <h2>This is our FirstComponent.</h2>;
};

export default FirstComponent;
```

frontend/src/components/SecondComponent.jsx:

```jsx
import React from "react";

const SecondComponent = () => {
  return <h2>This is our SecondComponent.</h2>;
};

export default SecondComponent;
```

![](https://user-images.githubusercontent.com/32337103/223979668-2af4c2d3-c0da-4cc6-8707-70af0bcff1d8.png)

</details>

<details>
  <summary>107. Class Components </summary>

frontend/src/App.js:

```js
import React from "react";
import FirstComponent from "./components/FirstComponent";
import SecondComponent from "./components/SecondComponent";
import ClassFirstComponent from "./components/ClassFirstComponent";

function App() {
  return (
    <div>
      <h2>Welcome to DRF.</h2>
      <FirstComponent />
      <SecondComponent />
      <ClassFirstComponent />
    </div>
  );
}

export default App;
```

frontend/src/components/ClassFirstComponent.jsx:

```jsx
import { Component } from "react";

class ClassFirstComponent extends Component {
  render() {
    return <h3>This is a class component</h3>;
  }
}
export default ClassFirstComponent;
```

![](https://user-images.githubusercontent.com/32337103/223984194-1214c285-eee3-414c-bd46-db87739839a4.png)

</details>

<details>
  <summary>108. Props </summary>

frontend/src/App.js:

```js
import React from "react";
import FirstComponent from "./components/FirstComponent";
import ClassFirstComponent from "./components/ClassFirstComponent";

function App() {
  return (
    <div>
      <h2>Welcome to DRF.</h2>
      <FirstComponent firstname="Ben" lastname="James" />
      <ClassFirstComponent email="ben@gmail.com" />
    </div>
  );
}

export default App;
```

frontend/src/components/FirstComponent.jsx:

```jsx
import React from "react";

const FirstComponent = (props) => {
  return (
    <>
      <h2>This is our FirstComponent.</h2>
      <h3>FirstName: {props.firstname}</h3>
      <h3>LastName: {props.lastname}</h3>
    </>
  );
};

export default FirstComponent;
```

frontend/src/components/ClassFirstComponent.jsx:

```jsx
import { Component } from "react";

class ClassFirstComponent extends Component {
  render() {
    return (
      <>
        <h2>This is a class component</h2>
        <h3>Email: {this.props.email}</h3>
      </>
    );
  }
}
export default ClassFirstComponent;
```

![](https://user-images.githubusercontent.com/32337103/223987240-bbedfb19-ea90-48dc-bcbb-64fe79f3ccf1.png)

</details>

<details>
  <summary>109. Event Handling </summary>

frontend/src/App.js:

```js
import React from "react";
import FirstComponent from "./components/FirstComponent";
import ClassFirstComponent from "./components/ClassFirstComponent";

function App() {
  return (
    <div>
      <h2>Welcome to DRF.</h2>
      <FirstComponent name="Ben James" />
      <ClassFirstComponent email="ben@gmail.com" />
    </div>
  );
}

export default App;
```

frontend/src/components/FirstComponent.jsx:

```jsx
import React from "react";

const FirstComponent = (props) => {
  function clickMe() {
    alert("Button was clicked");
  }

  return (
    <>
      <h2>This is our FirstComponent.</h2>
      <h3>Name: {props.name}</h3>
      <button onClick={clickMe}>Click Me</button>
    </>
  );
};

export default FirstComponent;
```

![](https://user-images.githubusercontent.com/32337103/223993637-9a52bcd9-1166-45cc-9df3-62a9098bd7ca.png)

frontend/src/App.js:

```js
import React from "react";
import FirstComponent from "./components/FirstComponent";
import ClassFirstComponent from "./components/ClassFirstComponent";

function App() {
  return (
    <div>
      <h2>Welcome to DRF.</h2>
      <FirstComponent name="Ben James" />
      <ClassFirstComponent email="ben@gmail.com" />
    </div>
  );
}

export default App;
```

frontend/src/components/ClassFirstComponent.jsx:

```jsx
import { Component } from "react";

class ClassFirstComponent extends Component {
  clickMe() {
    alert("Class component Button was clicked");
  }

  render() {
    return (
      <>
        <h2>This is a class component</h2>
        <h3>Email: {this.props.email}</h3>
        <button onClick={this.clickMe}>Click Me</button>
      </>
    );
  }
}
export default ClassFirstComponent;
```

![](https://user-images.githubusercontent.com/32337103/223995518-b94a4c7d-ac0b-45c1-97e9-a5f77761128e.png)

frontend/src/App.js:

```js
import React from "react";
import FirstComponent from "./components/FirstComponent";
import ClassFirstComponent from "./components/ClassFirstComponent";

function App() {
  function clickMe() {
    alert("Button was clicked - Using Events as Props.");
  }

  return (
    <div>
      <h2>Welcome to DRF.</h2>
      <FirstComponent name="Ben James" />
      <ClassFirstComponent email="ben@gmail.com" clickMe={clickMe} />
    </div>
  );
}

export default App;
```

frontend/src/components/ClassFirstComponent.jsx:

```jsx
import { Component } from "react";

class ClassFirstComponent extends Component {
  render() {
    return (
      <>
        <h2>This is a class component</h2>
        <h3>Email: {this.props.email}</h3>
        <button onClick={this.props.clickMe}>Click Me</button>
      </>
    );
  }
}
export default ClassFirstComponent;
```

![](https://user-images.githubusercontent.com/32337103/224105168-94759723-a14e-410c-b869-2197b841b64e.png)

</details>

<details>
  <summary>110. Install Bootstrap </summary>

```pybs
npm install bootstrap
```

frontend/src/index.js:

```pybs
import 'bootstrap/dist/css/bootstrap.min.css';
```

```js
import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import "bootstrap/dist/css/bootstrap.min.css";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
```

frontend/src/App.js:

```js
import React from "react";
import FirstComponent from "./components/FirstComponent";
// import ClassFirstComponent from "./components/ClassFirstComponent";

function App() {
  function clickMe() {
    alert("Button was clicked - Using Events as Props.");
  }

  return (
    <div>
      <h2>Welcome to DRF.</h2>
      <FirstComponent name="Ben James" clickMe={clickMe} />
      {/* <ClassFirstComponent email="ben@gmail.com" clickMe={clickMe} /> */}
    </div>
  );
}

export default App;
```

frontend/src/components/FirstComponent.jsx:

```jsx
import React from "react";

const FirstComponent = (props) => {
  // function clickMe() {
  //   alert("Button was clicked");
  // }

  return (
    <div className="container mt-5">
      <h2>This is our FirstComponent.</h2>
      <h3>Name: {props.name}</h3>
      <button className="btn btn-success" onClick={props.clickMe}>
        Click Me
      </button>
    </div>
  );
};

export default FirstComponent;
```

![](https://user-images.githubusercontent.com/32337103/224107797-060584e2-90cf-4cc8-840b-6412124a9cc1.png)

frontend/src/App.js:

```jsx
import React from "react";
import FirstComponent from "./components/FirstComponent";
import ClassFirstComponent from "./components/ClassFirstComponent";

function App() {
  function clickMe() {
    alert("Button was clicked - Using Events as Props.");
  }

  return (
    <div>
      <h2>Welcome to DRF.</h2>
      <FirstComponent name="Ben James" clickMe={clickMe} />
      <ClassFirstComponent email="ben@gmail.com" clickMe={clickMe} />
    </div>
  );
}

export default App;
```

frontend/src/components/ClassFirstComponent.jsx:

```jsx
import { Component } from "react";

class ClassFirstComponent extends Component {
  render() {
    return (
      <div className="container mt-5">
        <h2>This is a class component</h2>
        <h3>Email: {this.props.email}</h3>
        <button className="btn btn-danger" onClick={this.props.clickMe}>
          Click Me
        </button>
      </div>
    );
  }
}
export default ClassFirstComponent;
```

![](https://user-images.githubusercontent.com/32337103/224108920-0b9eea13-9f06-4c9d-9468-026a144ea06e.png)

</details>

<details>
  <summary>111. React State </summary>

frontend/src/App.js:

```js
import React from "react";
import FirstComponent from "./components/FirstComponent";
import ClassFirstComponent from "./components/ClassFirstComponent";

function App() {
  function clickMe() {
    alert("Button was clicked - Using Events as Props.");
  }

  return (
    <div>
      <h2>Welcome to DRF.</h2>
      <FirstComponent name="Ben James" clickMe={clickMe} />
      <ClassFirstComponent email="ben@gmail.com" clickMe={clickMe} />
    </div>
  );
}

export default App;
```

frontend/src/components/ClassFirstComponent.jsx:

```jsx
import { Component } from "react";

class ClassFirstComponent extends Component {
  constructor() {
    super();
    this.state = {
      name: "Ifeanyi",
    };
  }

  changeName = () => {
    // this.setState({ name: "Ben" });
    this.setState({ name: this.state.name === "Ifeanyi" ? "Ben" : "Ifeanyi" });
  };

  render() {
    return (
      <div className="container mt-5">
        <h2>My name is {this.state.name}.</h2>
        <h3>Email: {this.props.email}</h3>
        <button className="btn btn-danger" onClick={this.props.clickMe}>
          Click Me
        </button>
        <button onClick={() => this.changeName()} className="btn btn-primary">
          Change Name
        </button>
      </div>
    );
  }
}
export default ClassFirstComponent;
```

![](https://user-images.githubusercontent.com/32337103/224137447-7f6bb6e2-61dc-48f6-8b73-4ee86e1d0e1c.png)
![](https://user-images.githubusercontent.com/32337103/224137633-1f27d224-2f29-4489-834f-a04ab1cb563f.png)

</details>

<details>
  <summary>112. Map Function </summary>

frontend/src/App.js:

```js
import React from "react";
// import FirstComponent from "./components/FirstComponent";
import ClassFirstComponent from "./components/ClassFirstComponent";
import MapFunc from "./components/MapFunc";

function App() {
  function clickMe() {
    alert("Button was clicked - Using Events as Props.");
  }

  return (
    <div>
      <ClassFirstComponent email="ben@gmail.com" clickMe={clickMe} />
      <MapFunc names={["Python", "Java", "C#", "C++"]} />
    </div>
  );
}

export default App;
```

frontend/src/components/MapFunc.jsx:

```jsx
import { Component } from "react";

class MapFunc extends Component {
  myElements = (names) => {
    return names.map((name) => <div key={name}>{`${name}`}</div>);
  };

  render() {
    return (
      <div className="container mt-5">
        <h2>{this.myElements(this.props.names)}</h2>
      </div>
    );
  }
}
export default MapFunc;
```

![](https://user-images.githubusercontent.com/32337103/224152208-a3d5eb7a-d225-49bd-bd37-4516efbaa67c.png)

</details>

<details>
  <summary>113. Forms </summary>

frontend/src/App.js:

```js
import React from "react";
// import FirstComponent from "./components/FirstComponent";
import ClassFirstComponent from "./components/ClassFirstComponent";
import MapFunc from "./components/MapFunc";
import Forms from "./components/Forms";

function App() {
  function clickMe() {
    alert("Button was clicked - Using Events as Props.");
  }

  return (
    <div>
      <ClassFirstComponent email="ben@gmail.com" clickMe={clickMe} />
      <MapFunc names={["Python", "Java", "C#", "C++"]} />
      <Forms />
    </div>
  );
}

export default App;
```

frontend/src/components/Forms.jsx:

```jsx
import { Component } from "react";

class Forms extends Component {
  constructor() {
    super();

    this.state = {
      username: "",
      password: "",
    };
  }

  render() {
    return (
      <div className="container">
        <input
          type="text"
          className="form-control"
          placeholder="Please Enter Name"
          value={this.state.username}
          onChange={(e) => this.setState({ username: e.target.value })}
        />
        <input
          type="password"
          className="form-control"
          placeholder="Please Enter Password"
          value={this.state.password}
          onChange={(e) => this.setState({ password: e.target.value })}
        />
        <button className="btn btn-primary">Login</button>
        <div>{this.state.username}</div>
        <div>{this.state.password}</div>
      </div>
    );
  }
}

export default Forms;
```

![](https://user-images.githubusercontent.com/32337103/224298477-7472c60c-47ce-43db-b7a2-0fd9873a13c1.png)

</details>

<details>
  <summary>114. Lifecycle Methods </summary>

frontend/src/App.js:

```jsx
import React from "react";
// import FirstComponent from "./components/FirstComponent";
import ClassFirstComponent from "./components/ClassFirstComponent";
import MapFunc from "./components/MapFunc";
import Forms from "./components/Forms";

function App() {
  function clickMe() {
    alert("Button was clicked - Using Events as Props.");
  }

  return (
    <div>
      <ClassFirstComponent email="ben@gmail.com" clickMe={clickMe} />
      <MapFunc names={["Python", "Java", "C#", "C++"]} />
      <Forms />
    </div>
  );
}

export default App;
```

frontend/src/components/Forms.jsx:

```jsx
import { Component } from "react";

class Forms extends Component {
  constructor() {
    super();

    this.state = {
      username: "",
      password: "",
      posts: [],
    };
  }

  componentDidMount() {
    this.setState({ username: "Adam" });
    fetch("https://jsonplaceholder.typicode.com/posts")
      .then((resp) => resp.json())
      .then((result) => {
        this.setState({ posts: result });
      });
  }

  render() {
    const { posts } = this.state;
    return (
      <div className="container mt-3">
        <input
          type="text"
          className="form-control"
          placeholder="Please Enter Name"
          value={this.state.username}
          onChange={(e) => this.setState({ username: e.target.value })}
        />
        <input
          type="password"
          className="form-control"
          placeholder="Please Enter Password"
          value={this.state.password}
          onChange={(e) => this.setState({ password: e.target.value })}
        />
        <button className="btn btn-primary">Login</button>
        <div>
          <h2>{this.state.username}</h2>
        </div>
        <div>
          {posts.map((post) => (
            <p key={post.id}>{post.title}</p>
          ))}
        </div>
      </div>
    );
  }
}

export default Forms;
```

![](https://user-images.githubusercontent.com/32337103/224302978-f05b0869-628c-48fa-aaa4-ef17c600a476.png)

</details>

<details>
  <summary>115. React Router </summary>

```pybs
npm install react-router-dom
npm i react-router-dom
```

frontend/src/index.js:

```jsbs
import { BrowserRouter } from "react-router-dom";

<BrowserRouter>
    <App />
</BrowserRouter>
```

```js
import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import "bootstrap/dist/css/bootstrap.min.css";
import { BrowserRouter } from "react-router-dom";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>
);
```

frontend/src/App.js:

```jsbs
import { Routes, Route } from "react-router-dom";

<Routes>
    <Route path="/" element={<Home />}></Route>
</Routes>
```

```js
import React from "react";
import Home from "./components/Home";
import FirstComponent from "./components/FirstComponent";
import ClassFirstComponent from "./components/ClassFirstComponent";
import Forms from "./components/Forms";
import { Routes, Route } from "react-router-dom";

function App() {
  function clickMe() {
    alert("Button was clicked - Using Events as Props.");
  }

  return (
    <div>
      <Routes>
        <Route path="/" element={<Home />}></Route>
        <Route
          path="/classfirstcomp"
          element={
            <ClassFirstComponent email="ben@gmail.com" clickMe={clickMe} />
          }
        ></Route>
        <Route
          path="/firstcomp"
          element={<FirstComponent name="Mike" clickMe={clickMe} />}
        ></Route>
        <Route path="/forms" element={<Forms />}></Route>
      </Routes>
    </div>
  );
}

export default App;
```

frontend/src/components/Home.jsx:

```jsx
import React from "react";

const Home = () => {
  return (
    <div className="container mt-5">
      <h2>This is the Home Page.</h2>
    </div>
  );
};

export default Home;
```

![](https://user-images.githubusercontent.com/32337103/224306678-33fc0bb4-30e9-4ec8-a2bc-d68adba3df62.png)
![](https://user-images.githubusercontent.com/32337103/224306815-123e0779-fba3-4858-b53d-c6066bf78885.png)
![](https://user-images.githubusercontent.com/32337103/224306894-1d6b4ad7-cac0-478e-9ecd-469dcf3f0cf8.png)
![](https://user-images.githubusercontent.com/32337103/224306963-bff64f32-1866-4702-9e74-709e308314ea.png)

frontend/src/App.js:

```jsx
import React from "react";
import Home from "./components/Home";
import FirstComponent from "./components/FirstComponent";
import ClassFirstComponent from "./components/ClassFirstComponent";
import Forms from "./components/Forms";
import { Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";

function App() {
  function clickMe() {
    alert("Button was clicked - Using Events as Props.");
  }

  return (
    <div>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />}></Route>
        <Route
          path="/classfirstcomp"
          element={
            <ClassFirstComponent email="ben@gmail.com" clickMe={clickMe} />
          }
        ></Route>
        <Route
          path="/firstcomp"
          element={<FirstComponent name="Mike" clickMe={clickMe} />}
        ></Route>
        <Route path="/forms" element={<Forms />}></Route>
      </Routes>
    </div>
  );
}

export default App;
```

frontend/src/components/Navbar.jsx:

```jsx
import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <div className="navbar navbar-expand-lg navbar-light bg-light">
      <h2>Navbar</h2>
      <div className="container ">
        <ul className="navbar-nav">
          <li className="nav-item mx-3">
            <Link to="/">Home</Link>
          </li>
          <li className="nav-item mx-3">
            <Link to="/classfirstcomp">Class-First-Component</Link>
          </li>
          <li className="nav-item mx-3">
            <Link to="/firstcomp">Functional-First-Component</Link>
          </li>
          <li className="nav-item mx-3">
            <Link to="/forms">Forms</Link>
          </li>
        </ul>
      </div>
    </div>
  );
};

export default Navbar;
```

![](https://user-images.githubusercontent.com/32337103/224341742-967e8a0e-6459-4dc8-b033-09f0140e1db5.png)

</details>

<details>
  <summary>116. React Context </summary>

frontend/src/App.js:

```js
import React from "react";
// import Home from "./components/Home";
// import FirstComponent from "./components/FirstComponent";
// import ClassFirstComponent from "./components/ClassFirstComponent";
// import Forms from "./components/Forms";
// import { Routes, Route } from "react-router-dom";
// import Navbar from "./components/Navbar";
import ComponentA from "./components/ComponentA";

export const MyContext = React.createContext();

function App() {
  return (
    <div>
      <MyContext.Provider
        value={{ name: "Alex", comment: "This is the data from context." }}
      >
        <ComponentA />
      </MyContext.Provider>
    </div>
  );
}

export default App;
```

frontend/src/components/ComponentA.jsx:

```js
import React from "react";
import ComponentB from "./ComponentB";

const ComponentA = () => {
  return <ComponentB />;
};

export default ComponentA;
```

frontend/src/components/ComponentB.jsx:

```js
import React from "react";
import { MyContext } from "../App";

const ComponentB = () => {
  return (
    <div>
      <MyContext.Consumer>
        {(data) => {
          return (
            <>
              <h2>Author: {data.name}</h2>
              <h2>Comment: {data.comment}</h2>
            </>
          );
        }}
      </MyContext.Consumer>
    </div>
  );
};

export default ComponentB;
```

![](https://user-images.githubusercontent.com/32337103/224346781-85f46388-ad4b-44bf-9350-342052a61f06.png)

</details>

<details>
  <summary>117. useState Hooks </summary>

frontend/src/App.js:

```js
import React from "react";
// import Home from "./components/Home";
// import FirstComponent from "./components/FirstComponent";
// import ClassFirstComponent from "./components/ClassFirstComponent";
// import Forms from "./components/Forms";
// import { Routes, Route } from "react-router-dom";
// import Navbar from "./components/Navbar";
// import ComponentA from "./components/ComponentA";
// export const MyContext = React.createContext();
import Counter from "./components/Counter";

function App() {
  return (
    <div>
      <Counter />
    </div>
  );
}

export default App;
```

frontend/src/components/Counter.jsx:

```js
import React, { Component } from "react";

class Counter extends Component {
  constructor(props) {
    super(props);

    this.state = {
      count: 0,
    };
  }

  increase = () => {
    this.setState({ count: this.state.count + 1 });
  };

  decrease = () => {
    this.setState({ count: this.state.count - 1 });
  };

  render() {
    return (
      <div className="container">
        <h2>{this.state.count}</h2>
        <button onClick={this.increase} className="btn btn-primary">
          Increase
        </button>
        <button onClick={this.decrease} className="btn btn-danger">
          Decrease
        </button>
      </div>
    );
  }
}

export default Counter;
```

![](https://user-images.githubusercontent.com/32337103/224479623-92b039ba-f030-4825-8127-b70d8bdaf20e.png)

Using NUMBER values for Hooks -

frontend/src/App.js:

```js
import React from "react";
// import Home from "./components/Home";
// import FirstComponent from "./components/FirstComponent";
// import ClassFirstComponent from "./components/ClassFirstComponent";
// import Forms from "./components/Forms";
// import { Routes, Route } from "react-router-dom";
// import Navbar from "./components/Navbar";
// import ComponentA from "./components/ComponentA";
// export const MyContext = React.createContext();
// import Counter from "./components/Counter";
import CounterFunctional from "./components/CounterFunctional";

function App() {
  return (
    <div>
      <CounterFunctional />
    </div>
  );
}

export default App;
```

frontend/src/components/CounterFunctional.jsx:

```js
import React, { useState } from "react";

const CounterFunctional = () => {
  const [counter, setCounter] = useState(0);
  return (
    <div>
      <h1>{counter}</h1>
      <button
        className="btn btn-primary"
        onClick={() => setCounter((prev) => prev + 1)}
      >
        Increase
      </button>
      <button
        className="btn btn-danger"
        onClick={() => setCounter((prev) => prev - 1)}
      >
        Decrease
      </button>
    </div>
  );
};

export default CounterFunctional;
```

![](https://user-images.githubusercontent.com/32337103/224509526-c9892aec-9804-412a-a68c-920e8c970b6b.png)

Using STRING values for Hooks -

frontend/src/App.js:

```js
import React from "react";
// import Home from "./components/Home";
// import FirstComponent from "./components/FirstComponent";
// import ClassFirstComponent from "./components/ClassFirstComponent";
// import Forms from "./components/Forms";
// import { Routes, Route } from "react-router-dom";
// import Navbar from "./components/Navbar";
// import ComponentA from "./components/ComponentA";
// export const MyContext = React.createContext();
// import Counter from "./components/Counter";
import CounterFunctional from "./components/CounterFunctional";

function App() {
  return (
    <div>
      <CounterFunctional />
    </div>
  );
}

export default App;
```

frontend/src/components/CounterFunctional.jsx:

```js
import React, { useState } from "react";

const CounterFunctional = () => {
  const [counter, setCounter] = useState(0);
  const [text, setText] = useState("Ifeanyi");
  return (
    <div>
      <h1>{counter}</h1>
      <h2>{text}</h2>
      <button
        className="btn btn-primary"
        onClick={() => setCounter((prev) => prev + 1)}
      >
        Increase
      </button>
      <button
        className="btn btn-danger"
        onClick={() => setCounter((prev) => prev - 1)}
      >
        Decrease
      </button>
      <button
        className="btn btn-success"
        onClick={() => setText(text === "Ifeanyi" ? "James" : "Ifeanyi")}
      >
        Change Text
      </button>
    </div>
  );
};

export default CounterFunctional;
```

![](https://user-images.githubusercontent.com/32337103/224509762-77c1a263-2378-461a-a1b4-ae7ba1ec69e6.png)

Using OBJECT values for Hooks -

frontend/src/components/CounterFunctional.jsx:

```js
import React, { useState } from "react";

const CounterFunctional = () => {
  const [counter, setCounter] = useState(0);
  const [text, setText] = useState("Ifeanyi");
  const [info, setInfo] = useState({ name: "", email: "" });

  return (
    <div>
      <h1>{counter}</h1>
      <h2>{text}</h2>
      <button
        className="btn btn-primary"
        onClick={() => setCounter((prev) => prev + 1)}
      >
        Increase
      </button>
      <button
        className="btn btn-danger"
        onClick={() => setCounter((prev) => prev - 1)}
      >
        Decrease
      </button>
      <button
        className="btn btn-success"
        onClick={() => setText(text === "Ifeanyi" ? "James" : "Ifeanyi")}
      >
        Change Text
      </button>

      <br />
      <br />
      <input
        type="text"
        className="form-control"
        placeholder="Please enter name"
        value={info.name}
        onChange={(e) => setInfo({ ...info, name: e.target.value })}
      />
      <input
        type="email"
        className="form-control"
        placeholder="Please enter email"
        value={info.email}
        onChange={(e) => setInfo({ ...info, email: e.target.value })}
      />
      <h2>Name is : {info.name}</h2>
      <h2>Email is : {info.email}</h2>
    </div>
  );
};

export default CounterFunctional;
```

![](https://user-images.githubusercontent.com/32337103/224510221-bfd15279-986b-42de-beeb-d0a78297bae0.png)

Using ARRAY values for Hooks -

frontend/src/components/CounterFunctional.jsx:

```js
import React, { useState } from "react";

const CounterFunctional = () => {
  const [counter, setCounter] = useState(0);
  const [text, setText] = useState("Ifeanyi");
  const [info, setInfo] = useState({ name: "", email: "" });
  const [articles, setArticles] = useState([
    "Article One",
    "Article Two",
    "Article Three",
  ]);

  return (
    <div>
      <h1>{counter}</h1>
      <h2>{text}</h2>
      <button
        className="btn btn-primary"
        onClick={() => setCounter((prev) => prev + 1)}
      >
        Increase
      </button>
      <button
        className="btn btn-danger"
        onClick={() => setCounter((prev) => prev - 1)}
      >
        Decrease
      </button>
      <button
        className="btn btn-success"
        onClick={() => setText(text === "Ifeanyi" ? "James" : "Ifeanyi")}
      >
        Change Text
      </button>

      <br />
      <br />
      <input
        type="text"
        className="form-control"
        placeholder="Please enter name"
        value={info.name}
        onChange={(e) => setInfo({ ...info, name: e.target.value })}
      />
      <input
        type="email"
        className="form-control"
        placeholder="Please enter email"
        value={info.email}
        onChange={(e) => setInfo({ ...info, email: e.target.value })}
      />
      <h2>Name is : {info.name}</h2>
      <h2>Email is : {info.email}</h2>
      <div>
        {articles.map((article) => {
          return <h3 key={article}>{article}</h3>;
        })}
      </div>
    </div>
  );
};

export default CounterFunctional;
```

![](https://user-images.githubusercontent.com/32337103/224510376-7884dab3-b896-4b56-a01d-bb451bbd7a0b.png)

frontend/src/components/CounterFunctional.jsx:

```js
import React, { useState } from "react";

const CounterFunctional = () => {
  const [counter, setCounter] = useState(0);
  const [text, setText] = useState("Ifeanyi");
  const [info, setInfo] = useState({ name: "", email: "" });
  const [articles, setArticles] = useState([
    "Article One",
    "Article Two",
    "Article Three",
  ]);

  const addArticle = () => {
    setArticles([...articles, `Article ${articles.length + 1}`]);
  };

  return (
    <div>
      <h1>{counter}</h1>
      <h2>{text}</h2>
      <button
        className="btn btn-primary"
        onClick={() => setCounter((prev) => prev + 1)}
      >
        Increase
      </button>
      <button
        className="btn btn-danger"
        onClick={() => setCounter((prev) => prev - 1)}
      >
        Decrease
      </button>
      <button
        className="btn btn-success"
        onClick={() => setText(text === "Ifeanyi" ? "James" : "Ifeanyi")}
      >
        Change Text
      </button>

      <br />
      <br />
      <input
        type="text"
        className="form-control"
        placeholder="Please enter name"
        value={info.name}
        onChange={(e) => setInfo({ ...info, name: e.target.value })}
      />
      <input
        type="email"
        className="form-control"
        placeholder="Please enter email"
        value={info.email}
        onChange={(e) => setInfo({ ...info, email: e.target.value })}
      />
      <h2>Name is : {info.name}</h2>
      <h2>Email is : {info.email}</h2>
      <div>
        {articles.map((article) => {
          return <h3 key={article}>{article}</h3>;
        })}
      </div>
      <button className="btn btn-primary" onClick={addArticle}>
        Add Article
      </button>
    </div>
  );
};

export default CounterFunctional;
```

![](https://user-images.githubusercontent.com/32337103/224510729-7cf2447d-436a-47d6-a4c0-8fa2647a9edd.png)

</details>

<details>
  <summary>118. useEffect Hooks </summary>

frontend/src/App.js:

```js
import React from "react";
// import Home from "./components/Home";
// import FirstComponent from "./components/FirstComponent";
// import ClassFirstComponent from "./components/ClassFirstComponent";
// import Forms from "./components/Forms";
// import { Routes, Route } from "react-router-dom";
// import Navbar from "./components/Navbar";
// import ComponentA from "./components/ComponentA";
// export const MyContext = React.createContext();
// import Counter from "./components/Counter";
import CounterFunctional from "./components/CounterFunctional";

function App() {
  return (
    <div>
      <CounterFunctional />
    </div>
  );
}

export default App;
```

frontend/src/components/CounterFunctional.jsx:

```jsbs
useEffect(() => {
    document.title = `You have clicked ${counter} times`;
    console.log("useEffect is called");
  }, [info, counter]);
```

```js
import React, { useState, useEffect } from "react";

const CounterFunctional = () => {
  const [counter, setCounter] = useState(0);
  const [text, setText] = useState("Ifeanyi");
  const [info, setInfo] = useState({ name: "", email: "" });
  const [articles, setArticles] = useState([
    "Article One",
    "Article Two",
    "Article Three",
  ]);

  const addArticle = () => {
    setArticles([...articles, `Article ${articles.length + 1}`]);
  };

  useEffect(() => {
    document.title = `You have clicked ${counter} times`;
    console.log("useEffect is called");
  }, [info, counter]);

  return (
    <div>
      <h1>{counter}</h1>
      <h2>{text}</h2>
      <button
        className="btn btn-primary"
        onClick={() => setCounter((prev) => prev + 1)}
      >
        Increase
      </button>
      <button
        className="btn btn-danger"
        onClick={() => setCounter((prev) => prev - 1)}
      >
        Decrease
      </button>
      <button
        className="btn btn-success"
        onClick={() => setText(text === "Ifeanyi" ? "James" : "Ifeanyi")}
      >
        Change Text
      </button>

      <br />
      <br />
      <input
        type="text"
        className="form-control"
        placeholder="Please enter name"
        value={info.name}
        onChange={(e) => setInfo({ ...info, name: e.target.value })}
      />
      <input
        type="email"
        className="form-control"
        placeholder="Please enter email"
        value={info.email}
        onChange={(e) => setInfo({ ...info, email: e.target.value })}
      />
      <h2>Name is : {info.name}</h2>
      <h2>Email is : {info.email}</h2>
      <div>
        {articles.map((article) => {
          return <h3 key={article}>{article}</h3>;
        })}
      </div>
      <button className="btn btn-primary" onClick={addArticle}>
        Add Article
      </button>
    </div>
  );
};

export default CounterFunctional;
```

![](https://user-images.githubusercontent.com/32337103/224563900-c5085a15-2c87-4adf-815d-2ec330f94334.png)

frontend/src/App.js:

```js
import React from "react";
// import Home from "./components/Home";
// import FirstComponent from "./components/FirstComponent";
// import ClassFirstComponent from "./components/ClassFirstComponent";
// import Forms from "./components/Forms";
// import { Routes, Route } from "react-router-dom";
// import Navbar from "./components/Navbar";
// import ComponentA from "./components/ComponentA";
// export const MyContext = React.createContext();
// import Counter from "./components/Counter";
// import CounterFunctional from "./components/CounterFunctional";
import FetchData from "./components/FetchData";

function App() {
  return (
    <div>
      <FetchData />
    </div>
  );
}

export default App;
```

frontend/src/components/FetchData.jsx:

```js
import React, { useState, useEffect } from "react";

function FetchData() {
  const [articles, setArticles] = useState([]);
  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/posts")
      .then((resp) => resp.json())
      .then((result) => {
        // console.log(result);
        setArticles(result);
      });
  }, []);

  return (
    <div>
      {articles.map((article) => {
        return (
          <div key={article.id}>
            <h1>{article.title}</h1>
            <p>{article.body}</p>
          </div>
        );
      })}
    </div>
  );
}
export default FetchData;
```

![](https://user-images.githubusercontent.com/32337103/224565372-45ca1aaf-3cb2-4f3d-b656-5313b99a68bc.png)

</details>

<details>
  <summary>119. useContext Hooks </summary>

frontend/src/App.js:

```js
import React from "react";
// import Home from "./components/Home";
// import FirstComponent from "./components/FirstComponent";
// import ClassFirstComponent from "./components/ClassFirstComponent";
// import Forms from "./components/Forms";
// import { Routes, Route } from "react-router-dom";
// import Navbar from "./components/Navbar";
// import Counter from "./components/Counter";
// import CounterFunctional from "./components/CounterFunctional";
// import FetchData from "./components/FetchData";

import ComponentA from "./components/ComponentA";
export const MyContext = React.createContext();

function App() {
  return (
    <div>
      <MyContext.Provider value={{ name: "Ifeanyi Omeata", comment: "Hi!" }}>
        <ComponentA />
      </MyContext.Provider>
    </div>
  );
}

export default App;
```

frontend/src/components/ComponentA.jsx:

```js
import React from "react";
import ComponentB from "./ComponentB";

const ComponentA = () => {
  return <ComponentB />;
};

export default ComponentA;
```

frontend/src/components/ComponentB.jsx:

```js
import { useContext } from "react";
import { MyContext } from "../App";

const ComponentB = () => {
  const data = useContext(MyContext);
  return (
    <>
      <h2>Author: {data.name}</h2>
      <h2>Comment: {data.comment}</h2>
    </>
  );
};

export default ComponentB;
```

![](https://user-images.githubusercontent.com/32337103/224964315-09c91100-b345-4d8b-8ddc-2da110dc772b.png)

</details>

<details>
  <summary>120. useReducer Hooks </summary>

frontend/src/App.js:

```js
import React from "react";
// import Home from "./components/Home";
// import FirstComponent from "./components/FirstComponent";
// import ClassFirstComponent from "./components/ClassFirstComponent";
// import Forms from "./components/Forms";
// import { Routes, Route } from "react-router-dom";
// import Navbar from "./components/Navbar";
// import Counter from "./components/Counter";
// import CounterFunctional from "./components/CounterFunctional";
// import FetchData from "./components/FetchData";
// import ComponentA from "./components/ComponentA";
// export const MyContext = React.createContext();
import ReducerHook from "./components/ReducerHook";

function App() {
  return (
    <div>
      <ReducerHook />
    </div>
  );
}

export default App;
```

frontend/src/components/ReducerHook.js:

```js
import { useReducer } from "react";

const initialState = { count: 0 };

const reducer = (state, action) => {
  switch (action.type) {
    case "INCREMENT":
      return { count: state.count + 1 };

    case "DECREMENT":
      return { count: state.count - 1 };

    default:
      return { count: state.count };
  }
};

const ReducerHook = () => {
  const [state, dispatch] = useReducer(reducer, initialState);
  return (
    <div>
      <h2>Count: {state.count}</h2>
      <button
        onClick={() => dispatch({ type: "INCREMENT" })}
        className="btn btn-primary"
      >
        Increase
      </button>
      <button
        onClick={() => dispatch({ type: "DECREMENT" })}
        className="btn btn-danger"
      >
        Decrease
      </button>
    </div>
  );
};

export default ReducerHook;
```

![](https://user-images.githubusercontent.com/32337103/224967923-dd3c608e-57bf-441e-9fe7-bcce392b9b4c.png)

frontend/src/App.js:

```js
import React from "react";
// import Home from "./components/Home";
// import FirstComponent from "./components/FirstComponent";
// import ClassFirstComponent from "./components/ClassFirstComponent";
// import Forms from "./components/Forms";
// import { Routes, Route } from "react-router-dom";
// import Navbar from "./components/Navbar";
// import Counter from "./components/Counter";
// import CounterFunctional from "./components/CounterFunctional";
// import FetchData from "./components/FetchData";
// import ComponentA from "./components/ComponentA";
// export const MyContext = React.createContext();
// import ReducerHook from "./components/ReducerHook";

import FetchData2 from "./components/FetchData2";

function App() {
  return (
    <div>
      <FetchData2 />
    </div>
  );
}

export default App;
```

frontend/src/components/FetchData2.jsx:

```js
import { useEffect, useReducer } from "react";

const initialState = {
  loading: true,
  article: {},
  error: "",
};

const reducer = (state, action) => {
  switch (action.type) {
    case "SUCCESS":
      return {
        loading: false,
        article: action.payload,
        error: "",
      };
    case "FAIL":
      return {
        loading: false,
        article: {},
        error: "Error în data fetching",
      };
    default:
      return {};
  }
};

const FetchData2 = () => {
  const [state, dispatch] = useReducer(reducer, initialState);

  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/posts/1")
      .then((resp) => resp.json())
      .then((result) => {
        dispatch({ type: "SUCCESS", payload: result });
      })
      .catch((error) => {
        dispatch({ type: "FAIL" });
      });
  }, []);

  return (
    <div>
      {state.loading ? "Loading...." : state.article.body}
      {state.error ? state.error : null}
    </div>
  );
};

export default FetchData2;
```

![](https://user-images.githubusercontent.com/32337103/224999738-564648d4-64b3-4dbc-86d3-15ae5dc0c2a6.png)

</details>

<details>
  <summary>121. Fetching Data from BLOG REST API backend</summary>

![](https://user-images.githubusercontent.com/32337103/225009557-47455754-d4b3-4014-bb36-f8eaf77ee381.png)

frontend/src/App.js:

```js
import React from "react";
import FetchData from "./components/FetchData";

function App() {
  return (
    <div>
      <FetchData />
    </div>
  );
}

export default App;
```

frontend/src/components/FetchData.jsx:

```js
import React, { useState, useEffect } from "react";

function FetchData() {
  const [articles, setArticles] = useState(["Article One", "Article Two"]);
  useEffect(() => {
    fetch("https://blog-api-ifeanyi.herokuapp.com/articles/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Token a417323bea774f4a8fbb7a34f7b54f41e79a2363",
      },
    })
      .then((resp) => resp.json())
      .then((result) => {
        console.log(result);
        // setArticles(result);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <div>
      <>
        {articles.map((article) => {
          return <h2 key={article}>{article}</h2>;
        })}
      </>
      {/* {articles.map((article) => {
        return (
          <div key={article.id}>
            <h1>{article.title}</h1>
            <p>{article.body}</p>
          </div>
        );
      })} */}
    </div>
  );
}
export default FetchData;
```

![](https://user-images.githubusercontent.com/32337103/225014655-b296388c-a605-47e9-a261-356d044bb3d4.png)

![](https://user-images.githubusercontent.com/32337103/225014703-be250ebe-7474-4e9f-8bc5-4f02275fa960.png)

```jsbs
pip install django-cors-headers
python -m pip install django-cors-headers

pip freeze > requirements.txt
```

```jsbs
INSTALLED_APPS = [
    ...,
    "corsheaders",
    ...,
]
```

```jsbs
MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    ...,
]
```

```jsbs
CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000",
]

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

CORS_ALLOWED_ORIGINS = [
    "http://read.only.com",
    "http://change.allowed.com",
]

CSRF_TRUSTED_ORIGINS = [
    "http://change.allowed.com",
]
```

backend/blogapi/settings.py:

```py
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders', # <---- Add this
    'dj_rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'backend',
]

SITE_ID = 1

# REST_USE_JWT = True
# JWT_AUTH_COOKIE = 'jwt-auth'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware", # <---- Add this
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000", # <---- Add this
]

```

```jsbs
git add .
git commit -m "cors Commit"
git branch -M main
git push -u origin main
```

![](https://user-images.githubusercontent.com/32337103/225056858-6367fd92-a0c7-4f2d-9b05-48bbaafabeeb.png)
![](https://user-images.githubusercontent.com/32337103/225056921-670805cb-8112-4ecf-9ca4-fcfd669422a6.png)
![](https://user-images.githubusercontent.com/32337103/225057472-3fa5f6eb-dc3a-441d-bfbc-2b9f985e0c08.png)

frontend/src/App.js:

```js
import React from "react";
import FetchData from "./components/FetchData";

function App() {
  return (
    <div>
      <FetchData />
    </div>
  );
}

export default App;
```

frontend/src/components/FetchData.jsx:

```js
import React, { useState, useEffect } from "react";

function FetchData() {
  const [articles, setArticles] = useState(["Article One", "Article Two"]);
  useEffect(() => {
    fetch("https://blog-api-ifeanyi.herokuapp.com/articles/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Token a417323bea774f4a8fbb7a34f7b54f41e79a2363",
      },
    })
      .then((resp) => resp.json())
      .then((result) => {
        // console.log(result);
        setArticles(result);
        return true;
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <div>
      {articles.map((article, index) => {
        return (
          // <div key={article}>{article}</div>
          //   <div key={index}>
          <div key={article.id}>
            <h2>{article.title}</h2>
            <p>{article.description}</p>
          </div>
        );
      })}
    </div>
  );
}
export default FetchData;
```

![](https://user-images.githubusercontent.com/32337103/225158047-ea595b77-18de-40b0-84cc-7781da78c97f.png)

</details>

<details>
  <summary>122. Adding Bootstrap </summary>

```jsbs
npm install bootstrap
```

frontend/src/index.js:

```jsbs
import 'bootstrap/dist/css/bootstrap.min.css';
```

```js
import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import "bootstrap/dist/css/bootstrap.min.css";
import { BrowserRouter } from "react-router-dom";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>
);
```

frontend/src/App.js:

```js
import React from "react";
import FetchData from "./components/FetchData";
import "./App.css";

function App() {
  return (
    <div>
      <FetchData />
    </div>
  );
}

export default App;
```

frontend/src/components/FetchData.jsx:

```js
import React, { useState, useEffect } from "react";

function FetchData() {
  const [articles, setArticles] = useState(["Article One", "Article Two"]);
  useEffect(() => {
    fetch("https://blog-api-ifeanyi.herokuapp.com/articles/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Token a417323bea774f4a8fbb7a34f7b54f41e79a2363",
      },
    })
      .then((resp) => resp.json())
      .then((result) => {
        // console.log(result);
        setArticles(result);
        return true;
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <div>
      {articles.map((article, index) => {
        return (
          // <div key={article}>{article}</div>
          <div className="container mt-3" key={article.id}>
            <span className="badge rounded-pill bg-success">
              Author: {article.author}
            </span>
            <h2>
              <a className="link-style" href="#">
                {article.title}
              </a>
            </h2>
          </div>
        );
      })}
    </div>
  );
}
export default FetchData;
```

frontend/src/App.css:

```css
.link-style {
  text-decoration: none;
  color: black;
}

.link-style:hover {
  text-decoration: none;
  color: gray;
}
```

![](https://user-images.githubusercontent.com/32337103/225224441-1d03ff71-508c-41e0-aada-3e4a62f1a02e.png)

</details>

<details>
  <summary>123. Article List </summary>

frontend/src/App.js:

```js
import React from "react";
import FetchData from "./components/FetchData";
import "./App.css";

function App() {
  return (
    <div>
      <FetchData />
    </div>
  );
}

export default App;
```

frontend/src/components/FetchData.jsx:

```js
import React, { useState, useEffect } from "react";
import ArticleList from "./ArticleList";

function FetchData() {
  const [articles, setArticles] = useState(["Article One", "Article Two"]);
  useEffect(() => {
    fetch("https://blog-api-ifeanyi.herokuapp.com/articles/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Token a417323bea774f4a8fbb7a34f7b54f41e79a2363",
      },
    })
      .then((resp) => resp.json())
      .then((result) => {
        // console.log(result);
        setArticles(result);
        return true;
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <div>
      <ArticleList articles={articles} />
    </div>
  );
}
export default FetchData;
```

frontend/src/components/ArticleList.jsx:

```js
import React from "react";

const ArticleList = (props) => {
  return (
    <div>
      {props.articles[0] &&
        props.articles.map((article, index) => {
          return (
            // <div key={article}>{article}</div>
            <div className="container mt-3" key={article.id}>
              <span className="badge rounded-pill bg-success">
                Author: {article.author}
              </span>
              <h2>
                <a className="link-style" href="#">
                  {article.title}
                </a>
              </h2>
            </div>
          );
        })}
    </div>
  );
};

export default ArticleList;
```

![](https://user-images.githubusercontent.com/32337103/225229237-4067cc2f-293b-4224-86df-e86b206c80f3.png)

</details>

<details>
  <summary>124. Setup Navbar </summary>

frontend/src/App.js:

```js
import React from "react";
import "./App.css";
import FetchData from "./components/FetchData";
import Navbar from "./components/Navbar";

function App() {
  return (
    <div>
      <Navbar />
      <FetchData />
    </div>
  );
}

export default App;
```

frontend/src/components/Navbar.jsx:

```js
import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="navbar navbar-expand-lg bg-body-tertiary">
      <div className="container">
        <a className="navbar-brand" href="#">
          Django Blog
        </a>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav">
            <li className="nav-item">
              <a className="nav-link disabled"> Welcome, Alex.</a>
            </li>
            <li className="nav-item">
              <a className="nav-link active" aria-current="page" href="#">
                Home
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">
                Add Article
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">
                Logout
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">
                Login
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">
                Register
              </a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
```

frontend/src/components/FetchData.jsx:

```js
import React, { useState, useEffect } from "react";
import ArticleList from "./ArticleList";

function FetchData() {
  const [articles, setArticles] = useState(["Article One", "Article Two"]);
  useEffect(() => {
    fetch("https://blog-api-ifeanyi.herokuapp.com/articles/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Token a417323bea774f4a8fbb7a34f7b54f41e79a2363",
      },
    })
      .then((resp) => resp.json())
      .then((result) => {
        // console.log(result);
        setArticles(result);
        return true;
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <div>
      <ArticleList articles={articles} />
    </div>
  );
}
export default FetchData;
```

![](https://user-images.githubusercontent.com/32337103/225272247-2b886cee-b101-41e6-b0f7-0533974fda8b.png)

</details>

<details>
  <summary>125. Adding React Router </summary>

```jsbs
npm install react-router-dom
```

frontend/src/index.js:

```js
import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import "bootstrap/dist/css/bootstrap.min.css";
import { BrowserRouter } from "react-router-dom";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>
);
```

frontend/src/App.js:

```js
import React from "react";
import "./App.css";
import FetchData from "./components/FetchData";
import Navbar from "./components/Navbar";
import Login from "./components/Login";

import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <div>
      <Navbar />
      <Routes>
        <Route path="/" element={<Login />}></Route>
        <Route path="/articles" element={<FetchData />}></Route>
      </Routes>
    </div>
  );
}

export default App;
```

frontend/src/components/Login.jsx:

```js
import React from "react";

const Login = () => {
  return (
    <div>
      <h1>Please Login Here</h1>
    </div>
  );
};

export default Login;
```

frontend/src/components/FetchData.jsx:

```js
import React, { useState, useEffect } from "react";
import ArticleList from "./ArticleList";

function FetchData() {
  const [articles, setArticles] = useState([]);
  useEffect(() => {
    fetch("https://blog-api-ifeanyi.herokuapp.com/articles/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Token a417323bea774f4a8fbb7a34f7b54f41e79a2363",
      },
    })
      .then((resp) => resp.json())
      .then((result) => {
        // console.log(result);
        setArticles(result);
        return true;
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <div>
      <ArticleList articles={articles} />
    </div>
  );
}
export default FetchData;
```

frontend/src/components/ArticleList.jsx:

```js
import React from "react";

const ArticleList = (props) => {
  return (
    <div>
      {props.articles[0] &&
        props.articles.map((article, index) => {
          return (
            // <div key={article}>{article}</div>
            <div className="container mt-3" key={article.id}>
              <span className="badge rounded-pill bg-success">
                Author: {article.author}
              </span>
              <h2>
                <a className="link-style" href="#">
                  {article.title}
                </a>
              </h2>
            </div>
          );
        })}
    </div>
  );
};

export default ArticleList;
```

![](https://user-images.githubusercontent.com/32337103/225275882-c130820a-38db-43b7-b41a-304c1b6dfb3e.png)
![](https://user-images.githubusercontent.com/32337103/225275957-3efea751-8ac4-4e6b-8a7c-1520ead3b470.png)

</details>

<details>
  <summary>126. Fetching Article Details </summary>

frontend/src/App.js:

```js
import React from "react";
import "./App.css";
import FetchData from "./components/FetchData";
import Navbar from "./components/Navbar";
import Login from "./components/Login";
import ArticleDetails from "./components/ArticleDetails";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <div>
      <Navbar />
      <Routes>
        <Route path="/" element={<Login />}></Route>
        <Route path="/articles" element={<FetchData />}></Route>
        <Route path="/articles/:slug" element={<ArticleDetails />}></Route>
      </Routes>
    </div>
  );
}

export default App;
```

frontend/src/components/ArticleDetails.jsx:

```js
import React from "react";
import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";

const ArticleDetails = () => {
  const params = useParams();
  const [article, setArticle] = useState({});

  useEffect(() => {
    fetch(`https://blog-api-ifeanyi.herokuapp.com/articles/${params.slug}/`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Token a417323bea774f4a8fbb7a34f7b54f41e79a2363",
      },
    })
      .then((resp) => resp.json())
      .then((result) => {
        // console.log(params);
        setArticle(result);
        return true;
      })
      .catch((error) => {
        console.log(error);
      });
  }, [params]);

  return (
    <div className="container mt-4">
      <h1>{article.title}</h1>
      <h6>
        Published {article.published} by <i>{article.author}</i>
      </h6>
      <br />
      <p>{article.description}</p>
    </div>
  );
};

export default ArticleDetails;
```

frontend/src/components/FetchData.jsx:

```js
import React, { useState, useEffect } from "react";
import ArticleList from "./ArticleList";

function FetchData() {
  const [articles, setArticles] = useState([]);
  useEffect(() => {
    fetch("https://blog-api-ifeanyi.herokuapp.com/articles/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Token a417323bea774f4a8fbb7a34f7b54f41e79a2363",
      },
    })
      .then((resp) => resp.json())
      .then((result) => {
        console.log(result);
        setArticles(result);
        return true;
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <div>
      <ArticleList articles={articles} />
    </div>
  );
}
export default FetchData;
```

frontend/src/components/ArticleList.jsx:

```js
import React from "react";
import { Link } from "react-router-dom";

const ArticleList = (props) => {
  return (
    <div>
      {props.articles[0] &&
        props.articles.map((article, index) => {
          return (
            // <div key={article}>{article}</div>
            <div className="container mt-3" key={article.id}>
              <span className="badge rounded-pill bg-success">
                Author: {article.author}
              </span>
              <h2>
                <Link
                  to={`/articles/${article.slug}`}
                  className="link-style"
                  href="#"
                >
                  {article.title}
                </Link>
              </h2>
            </div>
          );
        })}
    </div>
  );
};

export default ArticleList;
```

![](https://user-images.githubusercontent.com/32337103/225369503-126d9634-9312-466e-bb2c-848bfd9b8265.png)
![](https://user-images.githubusercontent.com/32337103/225369618-7c5bac5b-5659-4184-8171-abb07353244f.png)
![](https://user-images.githubusercontent.com/32337103/225369816-b1781b7e-3d67-423d-806e-a462dc289d11.png)
![](https://user-images.githubusercontent.com/32337103/225369878-43575758-4063-46a2-8973-ce1c3ee3494b.png)
![](https://user-images.githubusercontent.com/32337103/225369937-d2237224-512a-4bf2-a1ee-050ea8d29ea6.png)
![](https://user-images.githubusercontent.com/32337103/225370013-ed8deff2-75d4-49a0-bf22-6ac4996857d3.png)

</details>

<details>
  <summary>127. React - Login System </summary>

![](https://user-images.githubusercontent.com/32337103/225685534-73775cee-e140-4eb4-bb3c-885a6d1d6f6c.png)

frontend/src/App.js:

```js
import React from "react";
import "./App.css";
import FetchData from "./components/FetchData";
import Navbar from "./components/Navbar";
import Login from "./components/Login";
import ArticleDetails from "./components/ArticleDetails";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <div>
      <Navbar />
      <Routes>
        <Route path="/" element={<Login />}></Route>
        <Route path="/articles" element={<FetchData />}></Route>
        <Route path="/articles/:slug" element={<ArticleDetails />}></Route>
      </Routes>
    </div>
  );
}

export default App;
```

frontend/src/components/Login.jsx:

```js
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  let navigate = useNavigate();

  const login = () => {
    fetch("https://blog-api-ifeanyi.herokuapp.com/dj-rest-auth/login/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username: username, password: password }),
    })
      .then((resp) => resp.json())
      .then((result) => {
        if (result.key === undefined) {
          setError("Invalid username or password");
          return;
        }
        localStorage.setItem("mytoken", result.key);
        navigate("/articles");
      });
  };

  return (
    <div className=" container mt-4">
      <br />

      {error ? (
        <div className="alert alert-danger alert-dismissible" role="alert">
          <p>{error}</p>
          <button
            type="button"
            className="btn-close"
            data-bs-dismiss="alert"
            aria-label="Close"
          ></button>
        </div>
      ) : null}

      <h1>Please Login Here</h1>
      <div className="my-3">
        <input
          type="text"
          className="form-control"
          name="username"
          placeholder="Please Enter Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
      </div>
      <div className="mb-3">
        <input
          type="password"
          className="form-control"
          name="password"
          placeholder="Please Enter Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </div>
      <div className="mb-3">
        <button onClick={login} className="btn btn-success">
          Login
        </button>
      </div>
    </div>
  );
};

export default Login;
```

![](https://user-images.githubusercontent.com/32337103/225691594-197e4c96-b757-4362-84c5-c6e82de631f3.png)

![](https://user-images.githubusercontent.com/32337103/225691359-6daa6d3c-9271-4f9b-88cb-cd527e385e0a.png)

frontend/src/components/FetchData.jsx:

```jsbs
const token = localStorage.getItem("mytoken");

Authorization: `Token ${token}`,
```

```js
import React, { useState, useEffect } from "react";
import ArticleList from "./ArticleList";

function FetchData() {
  const [articles, setArticles] = useState([]);
  const token = localStorage.getItem("mytoken");

  useEffect(() => {
    fetch("https://blog-api-ifeanyi.herokuapp.com/articles/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`,
      },
    })
      .then((resp) => resp.json())
      .then((result) => {
        console.log(result);
        setArticles(result);
        return true;
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <div>
      <ArticleList articles={articles} />
    </div>
  );
}
export default FetchData;
```

frontend/src/components/ArticleDetails.jsx:

```jsbs
const token = localStorage.getItem("mytoken");

Authorization: `Token ${token}`,
```

```js
import React from "react";
import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";

const ArticleDetails = () => {
  const params = useParams();
  const [article, setArticle] = useState({});
  const token = localStorage.getItem("mytoken");

  useEffect(() => {
    fetch(`https://blog-api-ifeanyi.herokuapp.com/articles/${params.slug}/`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`,
      },
    })
      .then((resp) => resp.json())
      .then((result) => {
        // console.log(params);
        setArticle(result);
        return true;
      })
      .catch((error) => {
        console.log(error);
      });
  }, [params, token]);

  return (
    <div className="container mt-4">
      <h1>{article.title}</h1>
      <h6>
        Published {article.published} by <i>{article.author}</i>
      </h6>
      <br />
      <p>{article.description}</p>
    </div>
  );
};

export default ArticleDetails;
```

![](https://user-images.githubusercontent.com/32337103/225694158-3f41d9f0-e222-47cf-8706-cb75b6bd799a.png)
![](https://user-images.githubusercontent.com/32337103/225694226-48d0a347-1b39-4684-9921-7b300b458acc.png)
![](https://user-images.githubusercontent.com/32337103/225694336-8b99eb63-9144-4945-9361-36f34cd208c3.png)

</details>

<details>
  <summary>128. React - Login Redirect </summary>

frontend/src/App.js:

```js
import React from "react";
import "./App.css";
import FetchData from "./components/FetchData";
import Navbar from "./components/Navbar";
import Login from "./components/Login";
import ArticleDetails from "./components/ArticleDetails";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <div>
      <Navbar />
      <Routes>
        <Route path="/" element={<Login />}></Route>
        <Route path="/articles" element={<FetchData />}></Route>
        <Route path="/articles/:slug" element={<ArticleDetails />}></Route>
      </Routes>
    </div>
  );
}

export default App;
```

frontend/src/components/FetchData.jsx:

```js
import React, { useState, useEffect } from "react";
import ArticleList from "./ArticleList";
import { useNavigate } from "react-router-dom";

function FetchData() {
  const [articles, setArticles] = useState([]);
  const token = localStorage.getItem("mytoken");

  let navigate = useNavigate();

  useEffect(() => {
    fetch("https://blog-api-ifeanyi.herokuapp.com/articles/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`,
      },
    })
      .then((resp) => resp.json())
      .then((result) => {
        // console.log(result);
        setArticles(result);
        return true;
      })
      .catch((error) => {
        console.log(error);
      });
  }, [token]);

  useEffect(() => {
    if (!token) {
      navigate("/");
    }
  }, [token, navigate]);

  return (
    <div>
      <ArticleList articles={articles} />
    </div>
  );
}
export default FetchData;
```

![](https://user-images.githubusercontent.com/32337103/225698696-b3f1fb89-07ce-48b2-88f2-8cb6fa794fbc.png)
![](https://user-images.githubusercontent.com/32337103/225698776-05019aa5-efc8-41d3-ba22-5c2c97d1aac8.png)

</details>

<details>
  <summary>129. React - Adding Article</summary>

frontend/src/App.js:

```js
import React from "react";
import "./App.css";
import FetchData from "./components/FetchData";
import Navbar from "./components/Navbar";
import Login from "./components/Login";
import ArticleDetails from "./components/ArticleDetails";
import AddArticle from "./components/AddArticle";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <div>
      <Navbar />
      <Routes>
        <Route path="/" element={<Login />}></Route>
        <Route path="/articles" element={<FetchData />}></Route>
        <Route path="/articles/:slug" element={<ArticleDetails />}></Route>
        <Route path="/add" element={<AddArticle />}></Route>
      </Routes>
    </div>
  );
}

export default App;
```

frontend/src/components/AddArticle.jsx:

```js
import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import APIService from "./APIService";

const AddArticle = () => {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [error, setError] = useState("");
  const token = localStorage.getItem("mytoken");

  let navigate = useNavigate();

  const addArticle = () => {
    APIService.InsertArticle({ title, description }, token);
  };

  useEffect(() => {
    if (!token) {
      navigate("/");
    }
  }, [token, navigate]);

  useEffect(() => {
    fetch("https://blog-api-ifeanyi.herokuapp.com/articles/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`,
      },
    })
      .then((resp) => resp.json())
      .then((result) => {
        // console.log(result);
        if (result.detail === "Invalid token.") {
          navigate("/");
        }
        // return true;
      })
      .catch((error) => {
        console.log(error);
      });
  }, [token, navigate]);

  return (
    <div className="container mt-5">
      <h2>Add Article</h2>
      <div className="mb-3">
        <input
          type="text"
          className="form-control"
          placeholder="Please Enter Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        ></input>
      </div>
      <div className="mb-3">
        <textarea
          className="form-control"
          rows="5"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
      </div>
      <div className="mb-3">
        <button onClick={addArticle} className="btn btn-success">
          Add Article
        </button>
      </div>
    </div>
  );
};

export default AddArticle;
```

frontend/src/components/APIService.js:

```js
export default class APIService {
  static InsertArticle(body, token) {
    fetch("https://blog-api-ifeanyi.herokuapp.com/articles/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`,
      },
      body: JSON.stringify(body),
    })
      .then((resp) => resp.json())
      .then((result) => {
        console.log(result);
        // return true;
      })
      .catch((error) => {
        console.log(error);
      });
  }
}
```

![](https://user-images.githubusercontent.com/32337103/225930193-aa594a2a-15a0-4252-96a5-42491ee368bb.png)
![](https://user-images.githubusercontent.com/32337103/225931534-6f911e14-c1c2-4977-9d58-217bf327d921.png)
![](https://user-images.githubusercontent.com/32337103/225931763-9d145aa5-55e7-41e0-bf0e-a1f0fc4ee0e0.png)
![](https://user-images.githubusercontent.com/32337103/225931947-23c5e966-5b28-460b-b4b7-38c193411118.png)
![](https://user-images.githubusercontent.com/32337103/225932096-a433ec34-f87d-4fe6-bb62-6304d01e2897.png)

frontend/src/components/APIService.js:

```jsbs
export default class APIService {
  static async InsertArticle(body, token) {
    let res = "";
    await fetch("https://blog-api-ifeanyi.herokuapp.com/articles/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`,
      },
      body: JSON.stringify(body),
    })
      .then((resp) => resp.json())
      .then((result) => {
        res = result;
        // console.log(result);
      })
      .catch((error) => {
        console.log(error);
      });
    return res;
  }
}

```

frontend/src/components/AddArticle.jsx:

```jsbs
const addArticle = async () => {
    const result = await APIService.InsertArticle(
      { title, description },
      token
    );
    console.log(result);
    navigate("/articles");
  };
```

```js
import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import APIService from "./APIService";

const AddArticle = () => {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [error, setError] = useState("");
  const token = localStorage.getItem("mytoken");

  let navigate = useNavigate();

  const addArticle = async () => {
    const result = await APIService.InsertArticle(
      { title, description },
      token
    );
    console.log(result);
    navigate("/articles");
  };

  useEffect(() => {
    if (!token) {
      navigate("/");
    }
  }, [token, navigate]);

  useEffect(() => {
    fetch("https://blog-api-ifeanyi.herokuapp.com/articles/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`,
      },
    })
      .then((resp) => resp.json())
      .then((result) => {
        // console.log(result);
        if (result.detail === "Invalid token.") {
          navigate("/");
        }
        // return true;
      })
      .catch((error) => {
        console.log(error);
      });
  }, [token, navigate]);

  return (
    <div className="container mt-5">
      <h2>Add Article</h2>
      <div className="mb-3">
        <input
          type="text"
          className="form-control"
          placeholder="Please Enter Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        ></input>
      </div>
      <div className="mb-3">
        <textarea
          className="form-control"
          rows="5"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
      </div>
      <div className="mb-3">
        <button onClick={addArticle} className="btn btn-success">
          Add Article
        </button>
      </div>
    </div>
  );
};

export default AddArticle;
```

![](https://user-images.githubusercontent.com/32337103/225950864-925a1f26-b53c-44ce-a991-27eddb4235c5.png)
![](https://user-images.githubusercontent.com/32337103/225950939-c83d7de3-7295-4230-8bde-8dc8c14b46bf.png)
![](https://user-images.githubusercontent.com/32337103/225951292-3f4b7712-9655-404c-8612-ebd9bce69997.png)

</details>

<details>
  <summary>130. React - Adding Validation to Fields </summary>

frontend/src/App.js:

```js
import React from "react";
import "./App.css";
import FetchData from "./components/FetchData";
import Navbar from "./components/Navbar";
import Login from "./components/Login";
import ArticleDetails from "./components/ArticleDetails";
import AddArticle from "./components/AddArticle";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <div>
      <Navbar />
      <Routes>
        <Route path="/" element={<Login />}></Route>
        <Route path="/articles" element={<FetchData />}></Route>
        <Route path="/articles/:slug" element={<ArticleDetails />}></Route>
        <Route path="/add" element={<AddArticle />}></Route>
      </Routes>
    </div>
  );
}

export default App;
```

frontend/src/components/AddArticle.jsx:

```jsbs
if (title === "" || description === "") {
    setError("Please add all fields");
    return;
}

{error ? (
    <div className="alert alert-danger alert-dismissible" role="alert">
        <p>{error}</p>
    </div>
) : null}
```

```js
import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import APIService from "./APIService";

const AddArticle = () => {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [error, setError] = useState("");
  const token = localStorage.getItem("mytoken");

  let navigate = useNavigate();

  const addArticle = async () => {
    if (title === "" || description === "") {
      setError("Please add all fields");
      return;
    }

    const result = await APIService.InsertArticle(
      { title, description },
      token
    );
    console.log(result);
    navigate("/articles");
  };

  useEffect(() => {
    if (!token) {
      navigate("/");
    }
  }, [token, navigate]);

  useEffect(() => {
    fetch("https://blog-api-ifeanyi.herokuapp.com/articles/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`,
      },
    })
      .then((resp) => resp.json())
      .then((result) => {
        // console.log(result);
        if (result.detail === "Invalid token.") {
          navigate("/");
        }
        // return true;
      })
      .catch((error) => {
        console.log(error);
      });
  }, [token, navigate]);

  return (
    <div className="container mt-5">
      {error ? (
        <div className="alert alert-danger alert-dismissible" role="alert">
          <p>{error}</p>
        </div>
      ) : null}

      <h2>Add Article</h2>
      <div className="mb-3">
        <input
          type="text"
          className="form-control"
          placeholder="Please Enter Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        ></input>
      </div>
      <div className="mb-3">
        <textarea
          className="form-control"
          rows="5"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
      </div>
      <div className="mb-3">
        <button onClick={addArticle} className="btn btn-success">
          Add Article
        </button>
      </div>
    </div>
  );
};

export default AddArticle;
```

![](https://user-images.githubusercontent.com/32337103/225991664-55477946-0004-486e-a3fe-08e367180c1d.png)

</details>

<details>
  <summary>131. React - Navbar Links </summary>

frontend/src/App.js:

```js
import React from "react";
import "./App.css";
import FetchData from "./components/FetchData";
import Navbar from "./components/Navbar";
import Login from "./components/Login";
import ArticleDetails from "./components/ArticleDetails";
import AddArticle from "./components/AddArticle";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <div>
      <Navbar />
      <Routes>
        <Route path="/" element={<Login />}></Route>
        <Route path="/articles" element={<FetchData />}></Route>
        <Route path="/articles/:slug" element={<ArticleDetails />}></Route>
        <Route path="/add" element={<AddArticle />}></Route>
      </Routes>
    </div>
  );
}

export default App;
```

frontend/src/components/Navbar.jsx:

```js
import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  const token = localStorage.getItem("mytoken");
  return (
    <nav className="navbar navbar-expand-lg bg-body-tertiary">
      <div className="container">
        <Link
          to={token ? "/articles" : "/"}
          className="navbar-brand text-style"
        >
          Django Blog
        </Link>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav">
            <li className="nav-item">
              <Link className="nav-link disabled"> Welcome, Alex.</Link>
            </li>
            <li className="nav-item">
              <Link
                to="/articles"
                className="nav-link active"
                aria-current="page"
              >
                Home
              </Link>
            </li>
            <li className="nav-item">
              <Link to="/add" className="nav-link">
                Add Article
              </Link>
            </li>
            <li className="nav-item">
              <Link to="" className="nav-link">
                Logout
              </Link>
            </li>
            <li className="nav-item">
              <Link to="/" className="nav-link">
                Login
              </Link>
            </li>
            <li className="nav-item">
              <Link to="" className="nav-link">
                Register
              </Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
```

frontend/src/App.css:

```css
.link-style {
  text-decoration: none;
  color: black;
}

.link-style:hover {
  text-decoration: none;
  color: gray;
}

.text-style {
  font-size: 40px !important;
  font-family: fantasy !important;
  color: brown !important;
  font-weight: 700 !important;
}
```

frontend/src/components/AddArticle.jsx:

```jsbs
  useEffect(() => {
    if (!token) {
      navigate("/");
      return;
    }
    navigate("/add");
  }, [token, navigate]);
```

```js
import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import APIService from "./APIService";

const AddArticle = () => {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [error, setError] = useState("");
  const token = localStorage.getItem("mytoken");

  let navigate = useNavigate();

  const addArticle = async () => {
    if (title === "" || description === "") {
      setError("Please add all fields");
      return;
    }

    const result = await APIService.InsertArticle(
      { title, description },
      token
    );
    console.log(result);
    navigate("/articles");
  };

  useEffect(() => {
    if (!token) {
      navigate("/");
      return;
    }
    navigate("/add");
  }, [token, navigate]);

  useEffect(() => {
    fetch("https://blog-api-ifeanyi.herokuapp.com/articles/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`,
      },
    })
      .then((resp) => resp.json())
      .then((result) => {
        // console.log(result);
        if (result.detail === "Invalid token.") {
          navigate("/");
        }
        // return true;
      })
      .catch((error) => {
        console.log(error);
      });
  }, [token, navigate]);

  return (
    <div className="container mt-5">
      {error ? (
        <div className="alert alert-danger alert-dismissible" role="alert">
          <p>{error}</p>
        </div>
      ) : null}

      <h2>Add Article</h2>
      <div className="mb-3">
        <input
          type="text"
          className="form-control"
          placeholder="Please Enter Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        ></input>
      </div>
      <div className="mb-3">
        <textarea
          className="form-control"
          rows="5"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
      </div>
      <div className="mb-3">
        <button onClick={addArticle} className="btn btn-success">
          Add Article
        </button>
      </div>
    </div>
  );
};

export default AddArticle;
```

frontend/src/components/Login.jsx:

```jsbs
useEffect(() => {
    if (token) {
      navigate("/articles");
    }
  }, [token, navigate]);
```

```js
import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const token = localStorage.getItem("mytoken");

  let navigate = useNavigate();

  useEffect(() => {
    if (token) {
      navigate("/articles");
    }
  }, [token, navigate]);

  const login = () => {
    fetch("https://blog-api-ifeanyi.herokuapp.com/dj-rest-auth/login/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username: username, password: password }),
    })
      .then((resp) => resp.json())
      .then((result) => {
        if (result.key === undefined) {
          setError("Invalid username or password");
          return;
        }
        localStorage.setItem("mytoken", result.key);
        navigate("/articles");
      });
  };

  return (
    <div className=" container mt-4">
      <br />

      {error ? (
        <div className="alert alert-danger alert-dismissible" role="alert">
          <p>{error}</p>
          <button
            type="button"
            className="btn-close"
            data-bs-dismiss="alert"
            aria-label="Close"
          ></button>
        </div>
      ) : null}

      <h1>Please Login Here</h1>
      <div className="my-3">
        <input
          type="text"
          className="form-control"
          name="username"
          placeholder="Please Enter Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
      </div>
      <div className="mb-3">
        <input
          type="password"
          className="form-control"
          name="password"
          placeholder="Please Enter Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </div>
      <div className="mb-3">
        <button onClick={login} className="btn btn-success">
          Login
        </button>
      </div>
    </div>
  );
};

export default Login;
```

![](https://user-images.githubusercontent.com/32337103/226101569-ed456f93-fc61-4375-86a2-fa52ea89999c.png)

</details>

<details>
  <summary>132. Hiding or Restricting the Navbar </summary>

frontend/src/App.js:

```js
import React from "react";
import "./App.css";
import FetchData from "./components/FetchData";
import Navbar from "./components/Navbar";
import Login from "./components/Login";
import ArticleDetails from "./components/ArticleDetails";
import AddArticle from "./components/AddArticle";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <div>
      <Navbar />
      <Routes>
        <Route path="/" element={<Login />}></Route>
        <Route path="/articles" element={<FetchData />}></Route>
        <Route path="/articles/:slug" element={<ArticleDetails />}></Route>
        <Route path="/add" element={<AddArticle />}></Route>
      </Routes>
    </div>
  );
}

export default App;
```

frontend/src/components/Navbar.jsx:

```js
import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  const token = localStorage.getItem("mytoken");
  return (
    <nav className="navbar navbar-expand-lg bg-body-tertiary">
      <div className="container">
        <Link
          to={token ? "/articles" : "/"}
          className="navbar-brand text-style"
        >
          Django Blog
        </Link>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav">
            {token ? (
              <>
                <li className="nav-item">
                  <Link className="nav-link disabled"> Welcome, Alex.</Link>
                </li>
                <li className="nav-item">
                  <Link
                    to="/articles"
                    className="nav-link active"
                    aria-current="page"
                  >
                    Home
                  </Link>
                </li>
                <li className="nav-item">
                  <Link to="/add" className="nav-link">
                    Add Article
                  </Link>
                </li>
                <li className="nav-item">
                  <Link to="" className="nav-link">
                    Logout
                  </Link>
                </li>
              </>
            ) : (
              <>
                <li className="nav-item">
                  <Link to="/" className="nav-link">
                    Login
                  </Link>
                </li>
                <li className="nav-item">
                  <Link to="" className="nav-link">
                    Register
                  </Link>
                </li>
              </>
            )}
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
```

![](https://user-images.githubusercontent.com/32337103/226101980-5dfd54b6-1cb3-4e2e-905f-314d3e452d9d.png)

![](https://user-images.githubusercontent.com/32337103/226102142-f5de8f56-d53c-4f68-b772-4c8e1e839db4.png)

</details>

<details>
  <summary>133. Showing Current User</summary>

frontend/src/App.js:

```js
import React from "react";
import "./App.css";
import FetchData from "./components/FetchData";
import Navbar from "./components/Navbar";
import Login from "./components/Login";
import ArticleDetails from "./components/ArticleDetails";
import AddArticle from "./components/AddArticle";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <div>
      <Navbar />
      <Routes>
        <Route path="/" element={<Login />}></Route>
        <Route path="/articles" element={<FetchData />}></Route>
        <Route path="/articles/:slug" element={<ArticleDetails />}></Route>
        <Route path="/add" element={<AddArticle />}></Route>
      </Routes>
    </div>
  );
}

export default App;
```

frontend/src/components/Login.jsx:

```js
import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [token, setToken] = useState(localStorage.getItem("mytoken"));

  let navigate = useNavigate();

  useEffect(() => {
    if (token) {
      navigate("/articles");
    }
  }, [token, navigate]);

  const login = () => {
    fetch("https://blog-api-ifeanyi.herokuapp.com/dj-rest-auth/login/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username: username, password: password }),
    })
      .then((resp) => resp.json())
      .then((result) => {
        if (result.key === undefined) {
          setError("Invalid username or password");
          return;
        }
        localStorage.setItem("mytoken", result.key);
        localStorage.setItem("myuser", username);
        setToken(result.key);
        navigate("/articles");
      });
  };

  return (
    <div className=" container mt-4">
      <br />

      {error ? (
        <div className="alert alert-danger alert-dismissible" role="alert">
          <p>{error}</p>
          <button
            type="button"
            className="btn-close"
            data-bs-dismiss="alert"
            aria-label="Close"
          ></button>
        </div>
      ) : null}

      <h1>Please Login Here</h1>
      <div className="my-3">
        <input
          type="text"
          className="form-control"
          name="username"
          placeholder="Please Enter Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
      </div>
      <div className="mb-3">
        <input
          type="password"
          className="form-control"
          name="password"
          placeholder="Please Enter Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </div>
      <div className="mb-3">
        <button onClick={login} className="btn btn-success">
          Login
        </button>
      </div>
    </div>
  );
};

export default Login;
```

frontend/src/components/Navbar.jsx:

```js
import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  const token = localStorage.getItem("mytoken");
  const user = localStorage.getItem("myuser");

  return (
    <nav className="navbar navbar-expand-lg bg-body-tertiary">
      <div className="container">
        <Link
          to={token ? "/articles" : "/"}
          className="navbar-brand text-style"
        >
          Django Blog
        </Link>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav">
            {token ? (
              <>
                <li className="nav-item">
                  <Link className="nav-link disabled"> Welcome, {user}.</Link>
                </li>
                <li className="nav-item">
                  <Link
                    to="/articles"
                    className="nav-link active"
                    aria-current="page"
                  >
                    Home
                  </Link>
                </li>
                <li className="nav-item">
                  <Link to="/add" className="nav-link">
                    Add Article
                  </Link>
                </li>
                <li className="nav-item">
                  <Link to="" className="nav-link">
                    Logout
                  </Link>
                </li>
              </>
            ) : (
              <>
                <li className="nav-item">
                  <Link to="/" className="nav-link">
                    Login
                  </Link>
                </li>
                <li className="nav-item">
                  <Link to="" className="nav-link">
                    Register
                  </Link>
                </li>
              </>
            )}
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
```

![](https://user-images.githubusercontent.com/32337103/226103504-635f7bbd-bd90-4f08-b613-70de90cf04fe.png)

</details>

<details>
  <summary>134. React - Logout </summary>

frontend/src/components/Navbar.jsx:

```jsbs
 <li className="nav-item">
    <Link to="" className="nav-link" onClick={() => localStorage.clear()}>
    Logout
    </Link>
</li>
```

```js
import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  const token = localStorage.getItem("mytoken");
  const user = localStorage.getItem("myuser");

  return (
    <nav className="navbar navbar-expand-lg bg-body-tertiary">
      <div className="container">
        <Link
          to={token ? "/articles" : "/"}
          className="navbar-brand text-style"
        >
          Django Blog
        </Link>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav">
            {token ? (
              <>
                <li className="nav-item">
                  <Link className="nav-link disabled"> Welcome, {user}.</Link>
                </li>
                <li className="nav-item">
                  <Link
                    to="/articles"
                    className="nav-link active"
                    aria-current="page"
                  >
                    Home
                  </Link>
                </li>
                <li className="nav-item">
                  <Link to="/add" className="nav-link">
                    Add Article
                  </Link>
                </li>
                <li className="nav-item">
                  <Link
                    to=""
                    className="nav-link"
                    onClick={() => localStorage.clear()}
                  >
                    Logout
                  </Link>
                </li>
              </>
            ) : (
              <>
                <li className="nav-item">
                  <Link to="/" className="nav-link">
                    Login
                  </Link>
                </li>
                <li className="nav-item">
                  <Link to="" className="nav-link">
                    Register
                  </Link>
                </li>
              </>
            )}
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
```

![](https://user-images.githubusercontent.com/32337103/226104055-19dd6264-8b91-4570-8bfa-6ce8b88ec6bf.png)

</details>

<details>
  <summary>135. React - User Registration </summary>

```js

```

```js

```

```js

```

</details>
