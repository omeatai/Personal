## +Udemy-React and Django: A Practical Guide with Docker

## [COURSE](https://www.udemy.com/course/react-django-admin/)

<details>
<summary>1. Creating a New Django Project: admin_project </summary>

# Creating a New Django Project: admin_project

## Install venv

```x
python -m venv venv
```

## Activate venv

```x
# venv\Scripts\activate
source venv/bin/activate
```

## Install Django

```x
python -m pip install Django
pip install django
pip install django==5.0
```

## Install Other Project Dependencies: djangorestframework, markdown, django-filter, mock, Pillow, mysqlclient, django-mysql, python-decouple

```x
pip install djangorestframework markdown django-filter mock pillow django-mysql python-decouple
```

```x
brew install mysql
xcode-select --install
pip install mysqlclient
```

## Get dependencies

```x
pip freeze
```

```x
asgiref==3.8.1
Django==5.0.6
django-filter==24.2
django-mysql==4.14.0
djangorestframework==3.15.2
Markdown==3.6
mock==5.1.0
mysqlclient==2.2.4
pillow==10.4.0
python-decouple==3.8
sqlparse==0.5.0
```

## Save Dependencies to Requirements.txt

```x
pip freeze > requirements.txt
```

## Install requirements from Requirements.txt

```x
pip install -r requirements.txt
```

## Deactivate a virtual environment

```x
deactivate
```

## Create Django Project

```x
django-admin startproject admin_project .
```

## Create Django App - users

```x
python manage.py startapp users_app
```

### src-AI-Software/my_projects/07_react_django_practical/admin_project/settings.py:

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
    'rest_framework',
    'users_app'
]
```

## Run Migrations

```x
python manage.py makemigrations
python manage.py migrate
```

## Start Local Server

```x
python manage.py runserver
```

```x
(venv) ➜  07_react_django_practical git:(main) ✗ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
July 10, 2024 - 19:44:10
Django version 5.0.7, using settings 'admin_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/e39eef9e-8179-4904-83ba-c12faed70e02)

# #END</details>

<details>
<summary>2. Install and Configure Mysql for Django </summary>

# Install and Configure Mysql for Django

## Install Xampp for MAC

## [https://www.apachefriends.org/download.html](https://www.apachefriends.org/download.html)

<img width="782" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/86956fc2-76a0-494c-8737-3fc3129ab6a5">
<img width="782" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/0af54b4b-e1f9-49b6-b789-8e0d81d716be">

### src-AI-Software/my_projects/07_react_django_practical/admin_project/settings.py:

```py
from decouple import config
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

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
    'rest_framework',
    'users_app'
]

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
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('MYSQL_DATABASE'),
        'USER': config('MYSQL_USER'),
        'PASSWORD': config('MYSQL_PASSWORD'),
        'HOST': config('MYSQL_HOST', 'localhost'),
        'PORT': config('MYSQL_PORT', '3306'),
    }
}

```

### src-AI-Software/my_projects/07_react_django_practical/.env:

```py
# Django settings
SECRET_KEY=

# MySQL settings
MYSQL_DATABASE=django_admin
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
```

## Run Migrations

```x
python manage.py makemigrations
python manage.py migrate
```

## Create Super User

```x
python manage.py createsuperuser --email admin@gmail.com
```

## Run Django Server

```x
python manage.py runserver
```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/dee55471-f825-42a2-b179-916973cd6cfa)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/2ac4b996-2062-447c-9ff9-07becae9424c)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/a7e03e05-0c7e-469d-aa23-3a89186cfa87)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/d2c6896a-0b27-4a40-91b2-88119a0775d8)

<img width="1452" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/fe94c7d6-9d4b-434b-82d9-b674bc0575d6">
<img width="1452" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/6a9d93d1-2b36-458b-812c-87e8f8101a1f">

# #END</details>

<details>
<summary>3. Create Rest API Endpoints with URLs and Views </summary>

# Create Rest API Endpoints with URLs and Views

## src-AI-Software/my_projects/07_react_django_practical/admin_project/urls.py:

```py
"""
URL configuration for admin_project project.

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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('users_app.urls')),
]

```

### src-AI-Software/my_projects/07_react_django_practical/users_app/urls.py:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
]

```

### src-AI-Software/my_projects/07_react_django_practical/users_app/views.py:

```py
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def hello(request):
    if request.method == 'GET':
        return Response('This is the GET EndPoint')
        # return render(request, 'index.html')
    elif request.method == 'POST':
        return Response('This is the POST EndPoint')


```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/c181d371-f711-40a0-9a0e-fc82ec8d9199)

<img width="1400" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/26bc0cd7-3b32-41dd-99a0-d152cfb1e58d">
<img width="1400" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/17b999be-5a77-4270-a94d-32110a52e8cd">
<img width="1485" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/d4f79bce-ec17-402f-8913-de7cb64f04e6">

# #END</details>

<details>
<summary>4. Create Models </summary>

# Create Models

### src-AI-Software/my_projects/07_react_django_practical/users_app/models.py:

```py
from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Users'
        verbose_name = 'User'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

```

### src-AI-Software/my_projects/07_react_django_practical/users_app/urls.py:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name='users'),
]

```

### src-AI-Software/my_projects/07_react_django_practical/users_app/views.py:

```py
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User


@api_view(['GET', 'POST'])
def users(request):
    if request.method == 'GET':
        users = User.objects.all()
        context = {
            'users': users
        }
        return Response(context)

    elif request.method == 'POST':
        return Response('This is the POST EndPoint')

```



### src-AI-Software/my_projects/07_react_django_practical/users_app/admin.py:

```py
from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'email', 'created_at', 'updated_at']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['created_at', 'updated_at']
    list_per_page = 10


admin.site.register(models.User, UserAdmin)

```

## Run Migrations

```x
python manage.py makemigrations
python manage.py migrate
```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/713b9025-fcac-4a15-b42b-aaee5ac8d2a5)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/be34981e-27cd-4677-8785-ba57532c15b6)

<img width="1485" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/1ff2c827-8493-4374-bde8-baddba5a3e05">
<img width="1485" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/1bd1b203-4da1-43a8-88b4-56aa4b9e759b">
<img width="1485" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/7843894f-ea6b-4362-b920-fdf49010bc92">


# #END</details>

<details>
<summary>5. Create Serializers for Register Endpoint </summary>

# Create Serializers for Register Endpoint

### src-AI-Software/my_projects/07_react_django_practical/users_app/models.py:

```py
from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Users'
        verbose_name = 'User'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
```

### src-AI-Software/my_projects/07_react_django_practical/users_app/urls.py:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name='users'),
    path('register', views.register, name='register'),
]

```

### src-AI-Software/my_projects/07_react_django_practical/users_app/views.py:

```py
from django.shortcuts import render
from rest_framework import exceptions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer
from .models import User


@api_view(['POST'])
def register(request):
    data = request.data
    if data['password'] != data['password_confirm']:
        raise exceptions.ValidationError('Passwords do not match')

    if User.objects.filter(email=data['email']).exists():
        raise exceptions.ValidationError('Email already exists')

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

    # member = Member.objects.create(
    #     first_name=data['first_name'],
    #     last_name=data['last_name'],
    #     email=data['email'],
    #     password=data['password']
    # )
    # return Response('Member was created successfully')


@api_view(['GET'])
def users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        context = {
            'users': serializer.data
        }
        return Response(context)

```

### src-AI-Software/my_projects/07_react_django_practical/users_app/serializers.py:

```py
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    password_confirm = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name',
                  'email', 'password', 'password_confirm']  # '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError("Passwords do not match")

        user = User.objects.create(**validated_data)
        # user.set_password(password) # Need to hash Password
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        password_confirm = validated_data.pop('password_confirm', None)

        if password and password_confirm and password != password_confirm:
            raise serializers.ValidationError("Passwords do not match")

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance

```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/4a604f5b-e770-4e08-bda2-a406e280e445)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/7014f6b1-321c-4ba4-9fee-560c66c730c6)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/0e3c9020-422e-49cc-894b-783d7c448b62)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/1653963a-6913-4508-ac21-b36e48b6607f)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/70971552-7ce9-41ba-b80c-6902f9dc4b3f)

<img width="1400" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/db8858cd-c26f-45d7-b716-01323eed32e4">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/7c0194c1-058d-4935-a824-0fac8bed4922)

<img width="1485" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/175e99a8-8094-4d0c-a59c-35c188b3572e">
<img width="1485" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/6d3d2b37-5ce4-4916-8101-722df1bf1085">

# #END</details>

<details>
<summary>6. Hash Passwords with Abstract Class </summary>

# Hash Passwords with Abstract Class

### src-AI-Software/my_projects/07_react_django_practical/admin_project/settings.py:

```py
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users_app.User'
```

### src-AI-Software/my_projects/07_react_django_practical/users_app/models.py:

```py
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name_plural = 'Users'
        verbose_name = 'User'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

```

## Run Migrations

```x
python manage.py makemigrations
python manage.py migrate
```

### src-AI-Software/my_projects/07_react_django_practical/users_app/serializers.py:

```py
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    password_confirm = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name',
                  'email', 'password', 'password_confirm']  # '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError("Passwords do not match")

        # user = User.objects.create(**validated_data)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)  # Need to hash Password
        instance.save()
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        password_confirm = validated_data.pop('password_confirm', None)

        if password and password_confirm and password != password_confirm:
            raise serializers.ValidationError("Passwords do not match")

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance

```

### src-AI-Software/my_projects/07_react_django_practical/users_app/admin.py:

```py
from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'email', 'password', 'created_at', 'updated_at']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['created_at', 'updated_at']
    list_per_page = 10


admin.site.register(models.User, UserAdmin)

```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/d83c4521-5a93-41f4-9065-6d38215008de)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/c1985ab6-ac52-455f-b5f2-5710c2eb3522)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/d4fa8034-762a-45aa-a69a-a94c08aac467)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/9de28741-8897-4b78-ab7f-8043d63842bc)

<img width="1485" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/9c38fcac-c0ad-4ab6-9e29-fce693a25abe">

# #END</details>

<details>
<summary>7. Create Login Endpoint </summary>

# Create Login Endpoint

### src-AI-Software/my_projects/07_react_django_practical/users_app/urls.py:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name='users'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
]

```

### src-AI-Software/my_projects/07_react_django_practical/users_app/views.py:

```py
from django.shortcuts import render
from rest_framework import exceptions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer
from .models import User


@api_view(['POST'])
def register(request):
    data = request.data
    if data['password'] != data['password_confirm']:
        raise exceptions.ValidationError('Passwords do not match')

    if User.objects.filter(email=data['email']).exists():
        raise exceptions.ValidationError('Email already exists')

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = User.objects.filter(email=email).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found')
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('Incorrect password')
    serializer = UserSerializer(user)
    return Response({'token': 'success', 'user': serializer.data})


@api_view(['GET'])
def users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        context = {
            'users': serializer.data
        }
        return Response(context)

```

<img width="1400" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/dae80357-866a-4667-92af-21bc4fc057ad">
<img width="1400" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/e0e30590-31e9-4296-b291-1a90137df030">
<img width="1400" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/593aaee9-48c6-42ed-ba23-af1db8859945">

# #END</details>

<details>
<summary>8. Generate JWT Token </summary>

# Generate JWT Token

## Install JWT Package

```x
pip install PyJWT
```

### src-AI-Software/my_projects/07_react_django_practical/users_app/urls.py:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name='users'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
]

```

### src-AI-Software/my_projects/07_react_django_practical/users_app/auth.py:

```py
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

import jwt
import datetime


def generate_access_token(user):
    payload = {
        'user_id': user.id,
        'exp': datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.now(datetime.UTC)
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')


class JWTAuth(BaseAuthentication):

    def authenticate(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            return None

        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('unauthenticated')

        # user = User.objects.filter(id=payload['id']).first()
        user = get_user_model().objects.filter(id=payload['user_id']).first()

        if user is None:
            raise exceptions.AuthenticationFailed('User not found')
        return (user, None)

```

### src-AI-Software/my_projects/07_react_django_practical/users_app/views.py:

```py
from django.shortcuts import render
from rest_framework import exceptions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer
from .models import User
from .auth import generate_access_token


@api_view(['POST'])
def register(request):
    data = request.data
    if data['password'] != data['password_confirm']:
        raise exceptions.ValidationError('Passwords do not match')

    if User.objects.filter(email=data['email']).exists():
        raise exceptions.ValidationError('Email already exists')

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = User.objects.filter(email=email).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found')
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('Incorrect password')

    token = generate_access_token(user)
    # set token to http-only cookie
    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }
    return response


@api_view(['GET'])
def users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        context = {
            'users': serializer.data
        }
        return Response(context)

```

<img width="1491" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/59473f13-d1cd-4ff6-870f-ec2312465852">
<img width="1491" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/40bdeb5e-87ed-474a-9d1c-9de8d62ddf8f">
<img width="1421" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/9a867f8a-53b2-4c74-9946-10319e35c862">

# #END</details>

<details>
<summary>9. Verify UserAuth - Getting Authenticated User </summary>

# Verify UserAuth - Getting Authenticated User

### src-AI-Software/my_projects/07_react_django_practical/users_app/urls.py:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name='users'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('auth', views.AuthUser.as_view(), name='auth'),
]

```

### src-AI-Software/my_projects/07_react_django_practical/users_app/views.py:

```py
# from django.shortcuts import render
from rest_framework import exceptions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# import jwt

from .serializers import UserSerializer
from .models import User
from .auth import generate_access_token, JWTAuth


@api_view(['POST'])
def register(request):
    data = request.data
    if data['password'] != data['password_confirm']:
        raise exceptions.ValidationError('Passwords do not match')

    if User.objects.filter(email=data['email']).exists():
        raise exceptions.ValidationError('Email already exists')

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = User.objects.filter(email=email).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found')
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('Incorrect password')

    token = generate_access_token(user)
    # set token to http-only cookie
    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }
    return response


class AuthUser(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'data': serializer.data})

        # token = request.COOKIES.get('jwt')
        # if not token:
        #     raise exceptions.AuthenticationFailed('Unauthenticated')

        # try:
        #     payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        # except jwt.ExpiredSignatureError:
        #     raise exceptions.AuthenticationFailed('Unauthenticated')

        # user = User.objects.filter(id=payload['id']).first()
        # serializer = UserSerializer(user)
        # return Response(serializer.data)


@api_view(['GET'])
def users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        context = {
            'users': serializer.data
        }
        return Response(context)

```

### src-AI-Software/my_projects/07_react_django_practical/users_app/auth.py:

```py
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

import jwt
import datetime


def generate_access_token(user):
    payload = {
        'user_id': user.id,
        'exp': datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.now(datetime.UTC)
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')


class JWTAuth(BaseAuthentication):

    def authenticate(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            return None

        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('unauthenticated')

        # user = User.objects.filter(id=payload['id']).first()
        user = get_user_model().objects.filter(id=payload['user_id']).first()

        if user is None:
            raise exceptions.AuthenticationFailed('User not found')
        return (user, None)

```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/a8df1435-e312-47a3-bf31-bdcbdd6eb249)

<img width="1497" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/d9118218-fe57-4150-9001-cefa5c0e51b8">

# #END</details>

<details>
<summary>10. Create Logout Endpoint </summary>

# Create Logout Endpoint

### src-AI-Software/my_projects/07_react_django_practical/users_app/urls.py:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name='users'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('auth', views.AuthUser.as_view(), name='auth'),
    path('logout', views.logout, name='logout'),
]

```

### src-AI-Software/my_projects/07_react_django_practical/users_app/views.py:

```py
# from django.shortcuts import render
from rest_framework import exceptions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# import jwt

from .serializers import UserSerializer
from .models import User
from .auth import generate_access_token, JWTAuth


@api_view(['POST'])
def register(request):
    data = request.data
    if data['password'] != data['password_confirm']:
        raise exceptions.ValidationError('Passwords do not match')

    if User.objects.filter(email=data['email']).exists():
        raise exceptions.ValidationError('Email already exists')

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = User.objects.filter(email=email).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found')
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('Incorrect password')

    token = generate_access_token(user)
    # set token to http-only cookie
    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }
    return response


@api_view(['POST'])
def logout(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        'message': 'success'
    }
    return response


class AuthUser(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'data': serializer.data})

        # token = request.COOKIES.get('jwt')
        # if not token:
        #     raise exceptions.AuthenticationFailed('Unauthenticated')

        # try:
        #     payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        # except jwt.ExpiredSignatureError:
        #     raise exceptions.AuthenticationFailed('Unauthenticated')

        # user = User.objects.filter(id=payload['id']).first()
        # serializer = UserSerializer(user)
        # return Response(serializer.data)


@api_view(['GET'])
def users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        context = {
            'users': serializer.data
        }
        return Response(context)

```

<img width="1497" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/0bfdd52a-c940-4dfd-ad9a-0efcf2e128cb">
<img width="1497" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/5a209006-76c1-44c0-b065-2b7c8594ba55">
<img width="1497" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/973ba258-40ee-4423-bdc4-82cb55e4a177">
<img width="1497" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/096f7201-d2dd-4cc4-9975-cdb5082bf934">

# #END</details>

<details>
<summary>11. Create Role and Permission Models </summary>

# Create Role and Permission Models

### src-AI-Software/my_projects/07_react_django_practical/users_app/models.py:

```py
from django.contrib.auth.models import AbstractUser
from django.db import models


class Permission(models.Model):
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Permissions'
        verbose_name = 'Permission'

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=200, null=True, blank=True)
    permissions = models.ManyToManyField(Permission)

    class Meta:
        verbose_name_plural = 'Roles'
        verbose_name = 'Role'

    def __str__(self):
        return self.name


class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    role = models.ForeignKey(
        Role, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name_plural = 'Users'
        verbose_name = 'User'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

```

## Run Migrations

```x
python manage.py makemigrations
python manage.py migrate
```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/f89327d9-113f-46ab-a904-e9e06fb536d3)

<img width="1421" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/b3bdd63c-48af-431d-b8c7-2d9fcdf676f8">

# #END</details>

<details>
<summary>12. Load Data into Permission, Role and User Models using Fixtures </summary>

# Load Data into Permission, Role and User Models using Fixtures

### src-AI-Software/my_projects/07_react_django_practical/users_app/models.py:

```py
from django.contrib.auth.models import AbstractUser
from django.db import models


class Permission(models.Model):
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Permissions'
        verbose_name = 'Permission'

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=200, null=True, blank=True)
    permissions = models.ManyToManyField(Permission)

    class Meta:
        verbose_name_plural = 'Roles'
        verbose_name = 'Role'

    def __str__(self):
        return self.name


class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    role = models.ForeignKey(
        Role, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name_plural = 'Users'
        verbose_name = 'User'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

```

### src-AI-Software/my_projects/07_react_django_practical/fixtures/permissions.json:

```json
[
    {
        "model": "users_app.permission",
        "pk": 1,
        "fields": {
            "name": "view_users_apps"
        }
    },
    {
        "model": "users_app.permission",
        "pk": 2,
        "fields": {
            "name": "edit_users_apps"
        }
    },
    {
        "model": "users_app.permission",
        "pk": 3,
        "fields": {
            "name": "view_roles"
        }
    },
    {
        "model": "users_app.permission",
        "pk": 4,
        "fields": {
            "name": "edit_roles"
        }
    },
    {
        "model": "users_app.permission",
        "pk": 5,
        "fields": {
            "name": "view_products"
        }
    },
    {
        "model": "users_app.permission",
        "pk": 6,
        "fields": {
            "name": "edit_products"
        }
    },
    {
        "model": "users_app.permission",
        "pk": 7,
        "fields": {
            "name": "view_orders"
        }
    },
    {
        "model": "users_app.permission",
        "pk": 8,
        "fields": {
            "name": "edit_orders"
        }
    }
]
```

### src-AI-Software/my_projects/07_react_django_practical/fixtures/roles.json:

```json
[
    {
        "model": "users_app.role",
        "pk": 1,
        "fields": {
            "name": "Admin",
            "permissions": [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8
            ]
        }
    },
    {
        "model": "users_app.role",
        "pk": 2,
        "fields": {
            "name": "Editor",
            "permissions": [
                1,
                2,
                3,
                5,
                6,
                7,
                8
            ]
        }
    },
    {
        "model": "users_app.role",
        "pk": 3,
        "fields": {
            "name": "Viewer",
            "permissions": [
                1,
                3,
                5,
                7
            ]
        }
    }
]
```

### src-AI-Software/my_projects/07_react_django_practical/fixtures/users.json:

```json
[
    {
        "model": "users_app.user",
        "pk": 2,
        "fields": {
            "last_login": null,
            "is_superuser": true,
            "is_staff": false,
            "is_active": true,
            "date_joined": "2020-11-10T11:48:08.084Z",
            "first_name": "Admin",
            "last_name": "Admin",
            "email": "admin@admin.com",
            "password": "pbkdf2_sha256$720000$0iMHAjhkaTvdH975c3yplb$m0Ul71PcDmCZSehzGlCwTXvRlIT5Rn/25NlNxmZVKiI=",
            "role": 1,
            "groups": [],
            "user_permissions": []
        }
    },
    {
        "model": "users_app.user",
        "pk": 3,
        "fields": {
            "last_login": null,
            "is_superuser": true,
            "is_staff": false,
            "is_active": true,
            "date_joined": "2020-11-10T11:48:08.084Z",
            "first_name": "Editor",
            "last_name": "Editor",
            "email": "editor@editor.com",
            "password": "pbkdf2_sha256$720000$0iMHAjhkaTvdH975c3yplb$m0Ul71PcDmCZSehzGlCwTXvRlIT5Rn/25NlNxmZVKiI=",
            "role": 2,
            "groups": [],
            "user_permissions": []
        }
    },
    {
        "model": "users_app.user",
        "pk": 4,
        "fields": {
            "last_login": null,
            "is_superuser": true,
            "is_staff": false,
            "is_active": true,
            "date_joined": "2020-11-10T11:48:08.084Z",
            "first_name": "Viewer",
            "last_name": "Viewer",
            "email": "viewer@viewer.com",
            "password": "pbkdf2_sha256$720000$0iMHAjhkaTvdH975c3yplb$m0Ul71PcDmCZSehzGlCwTXvRlIT5Rn/25NlNxmZVKiI=",
            "role": 3,
            "groups": [],
            "user_permissions": []
        }
    }
]
```

## Run LoadData Permissions.json to Model

```x
python manage.py loaddata fixtures/permissions.json
```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/82962020-0835-41b2-883c-3389ecffa499)

<img width="1465" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/5593de39-ab72-4d22-aa39-5d3de2c5fb35">

## Run LoadData roles.json to Model

```x
python manage.py loaddata fixtures/roles.json
```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/9568c8e9-7d67-4c65-807a-32c7edd0ee6a)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/83fad26b-ff44-49c5-9c16-94de3ebe1f40)

<img width="1465" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/db982029-03dd-4f7f-aa91-443127232ff4">

## Run LoadData users.json to Model

```x
python manage.py loaddata fixtures/users.json
```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/92f9b199-2f70-467e-ad97-9bc08f529d8e)

<img width="1465" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/5ff42ac8-6e73-4bf8-ab30-bffb3078a087">

# #END</details>

<details>
<summary>13. Setup URL, View and Serializer for Permission Model </summary>

# Setup URL, View and Serializer for Permission Model

### src-AI-Software/my_projects/07_react_django_practical/users_app/models.py:

```py
from django.contrib.auth.models import AbstractUser
from django.db import models


class Permission(models.Model):
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Permissions'
        verbose_name = 'Permission'

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=200, null=True, blank=True)
    permissions = models.ManyToManyField(Permission)

    class Meta:
        verbose_name_plural = 'Roles'
        verbose_name = 'Role'

    def __str__(self):
        return self.name


class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    role = models.ForeignKey(
        Role, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name_plural = 'Users'
        verbose_name = 'User'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

```

### src-AI-Software/my_projects/07_react_django_practical/users_app/urls.py:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name='users'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('auth', views.AuthUser.as_view(), name='auth'),
    path('logout', views.logout, name='logout'),
    path('permissions', views.PermissionAPIView.as_view(), name='permissions'),
]

```

### src-AI-Software/my_projects/07_react_django_practical/users_app/views.py:

```py
# from django.shortcuts import render
from rest_framework import exceptions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import PermissionSerializer, UserSerializer
from .models import User, Permission
from .auth import generate_access_token, JWTAuth


class AuthUser(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'data': serializer.data})


class PermissionAPIView(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = PermissionSerializer(Permission.objects.all(), many=True)
        return Response({'data': serializer.data})


@api_view(['POST'])
def register(request):
    data = request.data
    if data['password'] != data['password_confirm']:
        raise exceptions.ValidationError('Passwords do not match')

    if User.objects.filter(email=data['email']).exists():
        raise exceptions.ValidationError('Email already exists')

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = User.objects.filter(email=email).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found')
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('Incorrect password')

    token = generate_access_token(user)
    # set token to http-only cookie
    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }
    return response


@api_view(['POST'])
def logout(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        'message': 'success'
    }
    return response


@api_view(['GET'])
def users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        context = {
            'users': serializer.data
        }
        return Response(context)

```

### src-AI-Software/my_projects/07_react_django_practical/users_app/serializers.py:

```py
from rest_framework import serializers
from .models import User, Permission


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):

    password_confirm = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name',
                  'email', 'password', 'password_confirm']  # '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError("Passwords do not match")

        # user = User.objects.create(**validated_data)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)  # Need to hash Password
        instance.save()
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        password_confirm = validated_data.pop('password_confirm', None)

        if password and password_confirm and password != password_confirm:
            raise serializers.ValidationError("Passwords do not match")

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance

```

![image](https://github.com/user-attachments/assets/63477cb2-b670-446f-8f1d-2c6aa4e9ce5c)
![image](https://github.com/user-attachments/assets/20cac1f2-2909-43f5-b17e-f920f210aba4)

<img width="1497" alt="image" src="https://github.com/user-attachments/assets/0ae855ae-99c3-48a8-933d-da5a7f4887ee">

<img width="1368" alt="image" src="https://github.com/user-attachments/assets/b9b63ab7-5966-489f-a619-8ad652868423">
<img width="1368" alt="image" src="https://github.com/user-attachments/assets/c859b59d-9850-4bd6-a45f-2899f1f38b6b">
<img width="1368" alt="image" src="https://github.com/user-attachments/assets/bb62b212-f6c0-47a7-a73d-1e6d4ece4adb">

# #END</details>

<details>
<summary>14. Setup URL, View and Serializer for Role Model - READ and CREATE ROLE using Viewsets </summary>

# Setup URL, View and Serializer for Role Model - READ and CREATE ROLE using Viewsets

### src-AI-Software/my_projects/07_react_django_practical/users_app/urls.py:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name='users'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('auth', views.AuthUser.as_view(), name='auth'),
    path('logout', views.logout, name='logout'),
    path('permissions', views.PermissionAPIView.as_view(), name='permissions'),
    path('roles', views.RoleViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='roles'),
    path('roles/<int:pk>', views.RoleViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='roles-detail'),
]

```

### src-AI-Software/my_projects/07_react_django_practical/users_app/views.py:

```py
from rest_framework import exceptions, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import PermissionSerializer, UserSerializer, RoleSerializer
from .models import User, Permission, Role
from .auth import generate_access_token, JWTAuth


class AuthUser(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'data': serializer.data})


class PermissionAPIView(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = PermissionSerializer(Permission.objects.all(), many=True)
        return Response({'data': serializer.data})


class RoleViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Role.objects.all()
        serializer = RoleSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def create(self, request):
        serializer = RoleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        pass
        # permission = Role.objects.get(id=pk)
        # serializer = RoleSerializer(permission)
        # return Response({"data": serializer.data})

    def update(self, request, pk=None):
        pass
        # permission = Role.objects.get(id=pk)
        # serializer = RoleSerializer(permission, data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response({"data": serializer.data})

    def destroy(self, request, pk=None):
        pass
        # permission = Role.objects.get(id=pk)
        # permission.delete()
        # return Response({'message': 'Role deleted successfully!'})


@api_view(['POST'])
def register(request):
    data = request.data
    if data['password'] != data['password_confirm']:
        raise exceptions.ValidationError('Passwords do not match')

    if User.objects.filter(email=data['email']).exists():
        raise exceptions.ValidationError('Email already exists')

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = User.objects.filter(email=email).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found')
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('Incorrect password')

    token = generate_access_token(user)
    # set token to http-only cookie
    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }
    return response


@api_view(['POST'])
def logout(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        'message': 'success'
    }
    return response


@api_view(['GET'])
def users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        context = {
            'users': serializer.data
        }
        return Response(context)

```

### src-AI-Software/my_projects/07_react_django_practical/users_app/serializers.py:

```py
from rest_framework import serializers
from .models import User, Permission, Role


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class PermissionRelatedField(serializers.StringRelatedField):
    def to_representation(self, value):
        return PermissionSerializer(value).data

    def to_internal_value(self, data):
        return data


class RoleSerializer(serializers.ModelSerializer):
    # permissions = PermissionSerializer(many=True)
    permissions = PermissionRelatedField(many=True)

    class Meta:
        model = Role
        fields = "__all__"

    def create(self, validated_data):
        permissions = validated_data.pop('permissions', None)

        if permissions == None:
            raise serializers.ValidationError(
                "You must set Permissions for the Role.")

        instance = self.Meta.model(**validated_data)
        instance.save()
        instance.permissions.add(*permissions)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):

    password_confirm = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name',
                  'email', 'password', 'password_confirm']  # '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError("Passwords do not match")

        # user = User.objects.create(**validated_data)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)  # Need to hash Password
        instance.save()
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        password_confirm = validated_data.pop('password_confirm', None)

        if password and password_confirm and password != password_confirm:
            raise serializers.ValidationError("Passwords do not match")

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance

```

## LIST/GET All Roles

```x
GET http://localhost:8000/api/v1/roles
```

<img width="1497" alt="image" src="https://github.com/user-attachments/assets/0620c40e-d940-4606-85a6-bb903ee5b527">
<img width="1453" alt="image" src="https://github.com/user-attachments/assets/37c85b1e-85fd-4a20-9128-6518085a1d6c">

```x
{
    "data": [
        {
            "id": 1,
            "permissions": [
                {
                    "id": 1,
                    "name": "view_users_apps",
                    "code": null
                },
                {
                    "id": 2,
                    "name": "edit_users_apps",
                    "code": null
                },
                {
                    "id": 3,
                    "name": "view_roles",
                    "code": null
                },
                {
                    "id": 4,
                    "name": "edit_roles",
                    "code": null
                },
                {
                    "id": 5,
                    "name": "view_products",
                    "code": null
                },
                {
                    "id": 6,
                    "name": "edit_products",
                    "code": null
                },
                {
                    "id": 7,
                    "name": "view_orders",
                    "code": null
                },
                {
                    "id": 8,
                    "name": "edit_orders",
                    "code": null
                }
            ],
            "name": "Admin",
            "code": null
        },
        {
            "id": 2,
            "permissions": [
                {
                    "id": 1,
                    "name": "view_users_apps",
                    "code": null
                },
                {
                    "id": 2,
                    "name": "edit_users_apps",
                    "code": null
                },
                {
                    "id": 3,
                    "name": "view_roles",
                    "code": null
                },
                {
                    "id": 5,
                    "name": "view_products",
                    "code": null
                },
                {
                    "id": 6,
                    "name": "edit_products",
                    "code": null
                },
                {
                    "id": 7,
                    "name": "view_orders",
                    "code": null
                },
                {
                    "id": 8,
                    "name": "edit_orders",
                    "code": null
                }
            ],
            "name": "Editor",
            "code": null
        },
        {
            "id": 3,
            "permissions": [
                {
                    "id": 1,
                    "name": "view_users_apps",
                    "code": null
                },
                {
                    "id": 3,
                    "name": "view_roles",
                    "code": null
                },
                {
                    "id": 5,
                    "name": "view_products",
                    "code": null
                },
                {
                    "id": 7,
                    "name": "view_orders",
                    "code": null
                }
            ],
            "name": "Viewer",
            "code": null
        }
    ]
}
```

## CREATE/POST a new Role

```x
POST http://localhost:8000/api/v1/roles
```

```x
{
    "name": "new role2",
    "permissions": [1, 2]
}
```

<img width="1497" alt="image" src="https://github.com/user-attachments/assets/5efce313-05e0-4dfa-92c9-f75f8e4c5756">
<img width="1497" alt="image" src="https://github.com/user-attachments/assets/3c18db12-90bf-4651-84a2-71eba012b9a2">

```x
{
    "data": {
        "id": 5,
        "permissions": [
            {
                "id": 1,
                "name": "view_users_apps",
                "code": null
            },
            {
                "id": 2,
                "name": "edit_users_apps",
                "code": null
            }
        ],
        "name": "new role2",
        "code": null
    }
}
```

<img width="1368" alt="image" src="https://github.com/user-attachments/assets/65407769-08a7-4cf3-8111-74505095eaf8">
<img width="1324" alt="image" src="https://github.com/user-attachments/assets/e8414dba-5984-4136-8eca-3f917462e225">
<img width="1368" alt="image" src="https://github.com/user-attachments/assets/b9db950d-1bcb-433b-86de-71f0f16330fe">

# #END</details>

<details>
<summary>15. Setup URL, View and Serializer for Role Model - RETRIEVE, UPDATE and DELETE ROLE using Viewsets </summary>

# Setup URL, View and Serializer for Role Model - RETRIEVE, UPDATE and DELETE ROLE using Viewsets

### src-AI-Software/my_projects/07_react_django_practical/users_app/urls.py:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name='users'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('auth', views.AuthUser.as_view(), name='auth'),
    path('logout', views.logout, name='logout'),
    path('permissions', views.PermissionAPIView.as_view(), name='permissions'),
    path('roles', views.RoleViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='roles'),
    path('roles/<int:pk>', views.RoleViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='roles-detail'),
]

```

### src-AI-Software/my_projects/07_react_django_practical/users_app/views.py:

```py
from rest_framework import exceptions, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import PermissionSerializer, UserSerializer, RoleSerializer
from .models import User, Permission, Role
from .auth import generate_access_token, JWTAuth


class AuthUser(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'data': serializer.data})


class PermissionAPIView(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = PermissionSerializer(Permission.objects.all(), many=True)
        return Response({'data': serializer.data})


class RoleViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Role.objects.all()
        serializer = RoleSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def create(self, request):
        serializer = RoleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(role)
        return Response({"data": serializer.data})

    def update(self, request, pk=None):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(instance=role, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        role = Role.objects.get(id=pk)
        role.delete()
        return Response({'message': 'Role deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def register(request):
    data = request.data
    if data['password'] != data['password_confirm']:
        raise exceptions.ValidationError('Passwords do not match')

    if User.objects.filter(email=data['email']).exists():
        raise exceptions.ValidationError('Email already exists')

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = User.objects.filter(email=email).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found')
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('Incorrect password')

    token = generate_access_token(user)
    # set token to http-only cookie
    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }
    return response


@api_view(['POST'])
def logout(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        'message': 'success'
    }
    return response


@api_view(['GET'])
def users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        context = {
            'users': serializer.data
        }
        return Response(context)

```

### src-AI-Software/my_projects/07_react_django_practical/users_app/serializers.py:

```py
from rest_framework import serializers
from .models import User, Permission, Role


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class PermissionRelatedField(serializers.StringRelatedField):
    def to_representation(self, value):
        return PermissionSerializer(value).data

    def to_internal_value(self, data):
        return data


class RoleSerializer(serializers.ModelSerializer):
    # permissions = PermissionSerializer(many=True)
    permissions = PermissionRelatedField(many=True)

    class Meta:
        model = Role
        fields = "__all__"

    def create(self, validated_data):
        permissions = validated_data.pop('permissions', None)

        if permissions == None:
            raise serializers.ValidationError(
                "You must set Permissions for the Role.")

        instance = self.Meta.model(**validated_data)
        instance.save()
        instance.permissions.add(*permissions)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):

    password_confirm = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name',
                  'email', 'password', 'password_confirm']  # '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError("Passwords do not match")

        # user = User.objects.create(**validated_data)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)  # Need to hash Password
        instance.save()
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        password_confirm = validated_data.pop('password_confirm', None)

        if password and password_confirm and password != password_confirm:
            raise serializers.ValidationError("Passwords do not match")

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance

```

## GET/RETRIEVE a Role

```x
GET http://localhost:8000/api/v1/roles/4
```

<img width="1497" alt="image" src="https://github.com/user-attachments/assets/ce8295dd-9eaa-4e17-b7af-9e53d094d007">
<img width="1497" alt="image" src="https://github.com/user-attachments/assets/29b978bd-b985-4609-bf53-44a85736038c">

```x
{
    "data": {
        "id": 4,
        "permissions": [],
        "name": "new role",
        "code": null
    }
}
```

## UPDATE/PUT a Role

```x
PUT http://localhost:8000/api/v1/roles/4
```

```x
{
    "name": "updated name",
    "permissions": [3,4]
}
```

<img width="1497" alt="image" src="https://github.com/user-attachments/assets/b4af6ae1-73f4-4717-8040-1d9ac4316c9a">
<img width="1497" alt="image" src="https://github.com/user-attachments/assets/8299ffdc-7ec8-4b41-8dbf-adc954e03a77">

```x
{
    "data": {
        "id": 4,
        "permissions": [
            {
                "id": 3,
                "name": "view_roles",
                "code": null
            },
            {
                "id": 4,
                "name": "edit_roles",
                "code": null
            }
        ],
        "name": "updated name",
        "code": null
    }
}
```

## DELETE/DESTROY a Role

```x
DELETE http://localhost:8000/api/v1/roles/4
```

<img width="1497" alt="image" src="https://github.com/user-attachments/assets/e40cbc9b-fd4b-48e7-96d7-0b7aa83a08dd">
<img width="1497" alt="image" src="https://github.com/user-attachments/assets/a4f6edc2-e5ba-45ac-b63c-8d2c97bbbc82">

![image](https://github.com/user-attachments/assets/83e91fca-910e-482d-a230-305edbc467c7)

<img width="1368" alt="image" src="https://github.com/user-attachments/assets/08ece7d5-5ec3-4a2e-ac56-8e81a1b403a0">
<img width="1368" alt="image" src="https://github.com/user-attachments/assets/d1cf10ea-dc3e-4c04-bb42-26c86eb1b885">
<img width="1368" alt="image" src="https://github.com/user-attachments/assets/382e3b7f-9db9-4836-bb25-6da8cc073217">

# #END</details>

<details>
<summary>16. Setup URL and View for User Model - READ and RETRIEVE using Generic API View and Mixins </summary>

# Setup URL and View for User Model - READ and RETRIEVE using Generic API View and Mixins

### src-AI-Software/my_projects/07_react_django_practical/users_app/urls.py:

```py
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.users, name='users'),
    path('users', views.UserGenericAPIView.as_view(), name='users'),
    path('users/<str:pk>', views.UserGenericAPIView.as_view(), name='users-detail'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('auth', views.AuthUser.as_view(), name='auth'),
    path('logout', views.logout, name='logout'),
    path('permissions', views.PermissionAPIView.as_view(), name='permissions'),
    path('roles', views.RoleViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='roles'),
    path('roles/<int:pk>', views.RoleViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='roles-detail'),
]

```

### src-AI-Software/my_projects/07_react_django_practical/users_app/views.py:

```py
from rest_framework import exceptions, viewsets, status, generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import PermissionSerializer, UserSerializer, RoleSerializer
from .models import User, Permission, Role
from .auth import generate_access_token, JWTAuth


# @api_view(['GET'])
# def users(request):
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         context = {
#             'users': serializer.data
#         }
#         return Response(context)


class UserGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, pk=None):
        if pk:
            return Response({"data": self.retrieve(request, pk).data})
        return Response({"data": self.list(request).data})


class AuthUser(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'data': serializer.data})


class PermissionAPIView(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = PermissionSerializer(Permission.objects.all(), many=True)
        return Response({'data': serializer.data})


class RoleViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Role.objects.all()
        serializer = RoleSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def create(self, request):
        serializer = RoleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(role)
        return Response({"data": serializer.data})

    def update(self, request, pk=None):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(instance=role, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        role = Role.objects.get(id=pk)
        role.delete()
        return Response({'message': 'Role deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def register(request):
    data = request.data
    if data['password'] != data['password_confirm']:
        raise exceptions.ValidationError('Passwords do not match')

    if User.objects.filter(email=data['email']).exists():
        raise exceptions.ValidationError('Email already exists')

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = User.objects.filter(email=email).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found')
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('Incorrect password')

    token = generate_access_token(user)
    # set token to http-only cookie
    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }
    return response


@api_view(['POST'])
def logout(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        'message': 'success'
    }
    return response

```

### src-AI-Software/my_projects/07_react_django_practical/users_app/serializers.py:

```py
from rest_framework import serializers
from .models import User, Permission, Role


class UserSerializer(serializers.ModelSerializer):

    password_confirm = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name',
                  'email', 'password', 'password_confirm']  # '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError("Passwords do not match")

        # user = User.objects.create(**validated_data)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)  # Need to hash Password
        instance.save()
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        password_confirm = validated_data.pop('password_confirm', None)

        if password and password_confirm and password != password_confirm:
            raise serializers.ValidationError("Passwords do not match")

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class PermissionRelatedField(serializers.StringRelatedField):
    def to_representation(self, value):
        return PermissionSerializer(value).data

    def to_internal_value(self, data):
        return data


class RoleSerializer(serializers.ModelSerializer):
    # permissions = PermissionSerializer(many=True)
    permissions = PermissionRelatedField(many=True)

    class Meta:
        model = Role
        fields = "__all__"

    def create(self, validated_data):
        permissions = validated_data.pop('permissions', None)

        if permissions == None:
            raise serializers.ValidationError(
                "You must set Permissions for the Role.")

        instance = self.Meta.model(**validated_data)
        instance.save()
        instance.permissions.add(*permissions)
        instance.save()
        return instance

```

### src-AI-Software/my_projects/07_react_django_practical/users_app/models.py:

```py
from django.contrib.auth.models import AbstractUser
from django.db import models


class Permission(models.Model):
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Permissions'
        verbose_name = 'Permission'

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=200, null=True, blank=True)
    permissions = models.ManyToManyField(Permission)

    class Meta:
        verbose_name_plural = 'Roles'
        verbose_name = 'Role'

    def __str__(self):
        return self.name


class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    role = models.ForeignKey(
        Role, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name_plural = 'Users'
        verbose_name = 'User'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

```

## READ/GET all Users

```x
GET http://localhost:8000/api/v1/users
```

<img width="1497" alt="image" src="https://github.com/user-attachments/assets/0a6b8cf0-bdf7-45d3-9d65-fe7b5008d62e">

![image](https://github.com/user-attachments/assets/881536fa-60cc-433d-9b10-5b023995fd2b)

```x
{
    "data": [
        {
            "id": 1,
            "first_name": "Ifeanyi",
            "last_name": "Omeata",
            "email": "ifeanyio@gmail.com"
        },
        {
            "id": 2,
            "first_name": "Admin",
            "last_name": "Admin",
            "email": "admin@admin.com"
        },
        {
            "id": 3,
            "first_name": "Editor",
            "last_name": "Editor",
            "email": "editor@editor.com"
        },
        {
            "id": 4,
            "first_name": "Viewer",
            "last_name": "Viewer",
            "email": "viewer@viewer.com"
        }
    ]
}
```

## RETRIEVE/GET a User

```x
GET http://localhost:8000/api/v1/users/2
```

<img width="1497" alt="image" src="https://github.com/user-attachments/assets/88223fbf-4967-4d2a-819c-70e3b62383a4">


```x
{
    "data": {
        "id": 2,
        "first_name": "Admin",
        "last_name": "Admin",
        "email": "admin@admin.com"
    }
}
```

<img width="1368" alt="image" src="https://github.com/user-attachments/assets/706dc59f-9824-42af-a436-54eaf0efce6c">
<img width="1368" alt="image" src="https://github.com/user-attachments/assets/ab28d9f8-051b-4cbf-9dcd-d3d81806f5de">
<img width="1368" alt="image" src="https://github.com/user-attachments/assets/4a415a45-0f16-457f-8a5d-9febfaace243">

# #END</details>

<details>
<summary>17. Setup URL and View for User Model - CREATE, UPDATE AND DELETE using Generic API View and Mixins </summary>

# Setup URL and View for User Model - CREATE, UPDATE AND DELETE using Generic API View and Mixins

### src-AI-Software/my_projects/07_react_django_practical/users_app/urls.py:

```py
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.users, name='users'),
    path('users', views.UserGenericAPIView.as_view(), name='users'),
    path('users/<str:pk>', views.UserGenericAPIView.as_view(), name='users-detail'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('auth', views.AuthUser.as_view(), name='auth'),
    path('logout', views.logout, name='logout'),
    path('permissions', views.PermissionAPIView.as_view(), name='permissions'),
    path('roles', views.RoleViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='roles'),
    path('roles/<int:pk>', views.RoleViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='roles-detail'),
]

```

### src-AI-Software/my_projects/07_react_django_practical/users_app/views.py:

```py
from rest_framework import exceptions, viewsets, status, generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import PermissionSerializer, UserSerializer, RoleSerializer
from .models import User, Permission, Role
from .auth import generate_access_token, JWTAuth


class UserGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, pk=None):
        if pk:
            return Response({"data": self.retrieve(request, pk).data})
        return Response({"data": self.list(request).data})

    def post(self, request):
        return Response({"data": self.create(request).data})

    def put(self, request, pk=None):
        return Response({"data": self.update(request, pk).data})

    def delete(self, request, pk=None):
        return self.destroy(request, pk)


class AuthUser(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'data': serializer.data})


class PermissionAPIView(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = PermissionSerializer(Permission.objects.all(), many=True)
        return Response({'data': serializer.data})


class RoleViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Role.objects.all()
        serializer = RoleSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def create(self, request):
        serializer = RoleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(role)
        return Response({"data": serializer.data})

    def update(self, request, pk=None):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(instance=role, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        role = Role.objects.get(id=pk)
        role.delete()
        return Response({'message': 'Role deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def register(request):
    data = request.data
    if data['password'] != data['password_confirm']:
        raise exceptions.ValidationError('Passwords do not match')

    if User.objects.filter(email=data['email']).exists():
        raise exceptions.ValidationError('Email already exists')

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = User.objects.filter(email=email).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found')
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('Incorrect password')

    token = generate_access_token(user)
    # set token to http-only cookie
    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }
    return response


@api_view(['POST'])
def logout(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        'message': 'success'
    }
    return response

```

### src-AI-Software/my_projects/07_react_django_practical/users_app/serializers.py:

```py
from rest_framework import serializers
from .models import User, Permission, Role


class UserSerializer(serializers.ModelSerializer):

    password_confirm = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name',
                  'email', 'password', 'password_confirm']  # '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError("Passwords do not match")

        # user = User.objects.create(**validated_data)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)  # Need to hash Password
        instance.save()
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        password_confirm = validated_data.pop('password_confirm', None)

        if password and password_confirm and password != password_confirm:
            raise serializers.ValidationError("Passwords do not match")

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class PermissionRelatedField(serializers.StringRelatedField):
    def to_representation(self, value):
        return PermissionSerializer(value).data

    def to_internal_value(self, data):
        return data


class RoleSerializer(serializers.ModelSerializer):
    # permissions = PermissionSerializer(many=True)
    permissions = PermissionRelatedField(many=True)

    class Meta:
        model = Role
        fields = "__all__"

    def create(self, validated_data):
        permissions = validated_data.pop('permissions', None)

        if permissions == None:
            raise serializers.ValidationError(
                "You must set Permissions for the Role.")

        instance = self.Meta.model(**validated_data)
        instance.save()
        instance.permissions.add(*permissions)
        instance.save()
        return instance

```

## CREATE a User

```x
POST http://localhost:8000/api/v1/users
```

<img width="1497" alt="image" src="https://github.com/user-attachments/assets/d62bb473-9b6e-4114-bc28-99dec1410700">

![image](https://github.com/user-attachments/assets/10988bdb-c649-4a2f-ad3c-c7bd13cf6901)

```x
{
    "data": {
        "id": 5,
        "first_name": "bob",
        "last_name": "henry",
        "email": "bob@gmail.com"
    }
}
```

## UPDATE a User

```x
PUT http://localhost:8000/api/v1/users/5
```

<img width="1497" alt="image" src="https://github.com/user-attachments/assets/2ef3a941-01c9-4b4b-a982-ca59d709239d">

![image](https://github.com/user-attachments/assets/07bc6a35-ad27-454a-8224-9a5c2ec802dd)

```x
{
    "data": {
        "id": 5,
        "first_name": "bob_Updated",
        "last_name": "henry_Updated",
        "email": "bob@gmail.com"
    }
}
```

## DELETE a User

```x
DELETE http://localhost:8000/api/v1/users/5
```

<img width="1497" alt="image" src="https://github.com/user-attachments/assets/7aee949f-08b8-4bb5-8f88-45097767bc9b">

![image](https://github.com/user-attachments/assets/136d078e-d111-42f7-b27e-cb66001e7faa)

<img width="1396" alt="image" src="https://github.com/user-attachments/assets/f64987d5-80bc-46f8-bffc-a091120f5f7a">
<img width="1396" alt="image" src="https://github.com/user-attachments/assets/6efc3e6d-3ba3-43aa-8dcc-47f2f627695c">
<img width="1396" alt="image" src="https://github.com/user-attachments/assets/f9d95fc5-a84a-4ccd-8467-f16dc839f08e">

# #END</details>

<details>
<summary>18. Setup Pagination for User Data </summary>

# Setup Pagination for User Data

### my_projects/07_react_django_practical/users_app/urls.py:

```py
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.users, name='users'),
    path('users', views.UserGenericAPIView.as_view(), name='users'),
    path('users/<str:pk>', views.UserGenericAPIView.as_view(), name='users-detail'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('auth', views.AuthUser.as_view(), name='auth'),
    path('logout', views.logout, name='logout'),
    path('permissions', views.PermissionAPIView.as_view(), name='permissions'),
    path('roles', views.RoleViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='roles'),
    path('roles/<int:pk>', views.RoleViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='roles-detail'),
]

```

### my_projects/07_react_django_practical/users_app/pagination.py:

```py
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 1


class CustomPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = DEFAULT_PAGE_SIZE
    page_size_query_param = "page_size"

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data,
            # added
            "meta": {
                "last_page": self.page.paginator.count,
                "page": int(self.request.GET.get("page", DEFAULT_PAGE)),
                "page_size": int(self.request.GET.get("page_size", self.page_size))
            }
        })

```

### my_projects/07_react_django_practical/users_app/views.py:

```py
from rest_framework import exceptions, viewsets, status, generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import PermissionSerializer, UserSerializer, RoleSerializer
from .models import User, Permission, Role
from .auth import generate_access_token, JWTAuth
from .pagination import CustomPagination


class UserGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({"data": self.retrieve(request, pk).data})
        return Response({"data": self.list(request).data})

    def post(self, request):
        return Response({"data": self.create(request).data})

    def put(self, request, pk=None):
        return Response({"data": self.update(request, pk).data})

    def delete(self, request, pk=None):
        return self.destroy(request, pk)


class AuthUser(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'data': serializer.data})


class PermissionAPIView(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = PermissionSerializer(Permission.objects.all(), many=True)
        return Response({'data': serializer.data})


class RoleViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Role.objects.all()
        serializer = RoleSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def create(self, request):
        serializer = RoleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(role)
        return Response({"data": serializer.data})

    def update(self, request, pk=None):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(instance=role, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        role = Role.objects.get(id=pk)
        role.delete()
        return Response({'message': 'Role deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def register(request):
    data = request.data
    if data['password'] != data['password_confirm']:
        raise exceptions.ValidationError('Passwords do not match')

    if User.objects.filter(email=data['email']).exists():
        raise exceptions.ValidationError('Email already exists')

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = User.objects.filter(email=email).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found')
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('Incorrect password')

    token = generate_access_token(user)
    # set token to http-only cookie
    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }
    return response


@api_view(['POST'])
def logout(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        'message': 'success'
    }
    return response

```

<img width="1404" alt="image" src="https://github.com/user-attachments/assets/fac39f9e-08ca-490c-8ba4-371adda3656e">
<img width="1404" alt="image" src="https://github.com/user-attachments/assets/0daa72de-94d9-42ea-905c-c13ea40e73e7">
<img width="1392" alt="image" src="https://github.com/user-attachments/assets/a8580ae8-5deb-4851-bee0-145be9128f83">

# #END</details>

<details>
<summary>19. Add Role Relationship to User and POST new User </summary>

# Add Role Relationship to User and POST new User

### my_projects/07_react_django_practical/users_app/urls.py:

```py
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.users, name='users'),
    path('users', views.UserGenericAPIView.as_view(), name='users'),
    path('users/<str:pk>', views.UserGenericAPIView.as_view(), name='users-detail'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('auth', views.AuthUser.as_view(), name='auth'),
    path('logout', views.logout, name='logout'),
    path('permissions', views.PermissionAPIView.as_view(), name='permissions'),
    path('roles', views.RoleViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='roles'),
    path('roles/<int:pk>', views.RoleViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='roles-detail'),
]

```

### my_projects/07_react_django_practical/users_app/serializers.py:

```py
from rest_framework import serializers
from .models import User, Permission, Role


class RoleRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return RoleSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)


class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    role = RoleRelatedField(many=False, queryset=Role.objects.all())

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name',
                  'email', 'password', 'password_confirm', 'role']  # '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError("Passwords do not match")

        # user = User.objects.create(**validated_data)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)  # Need to hash Password
        instance.save()
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        password_confirm = validated_data.pop('password_confirm', None)

        if password and password_confirm and password != password_confirm:
            raise serializers.ValidationError("Passwords do not match")

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class PermissionRelatedField(serializers.StringRelatedField):
    def to_representation(self, value):
        return PermissionSerializer(value).data

    def to_internal_value(self, data):
        return data


class RoleSerializer(serializers.ModelSerializer):
    # permissions = PermissionSerializer(many=True)
    permissions = PermissionRelatedField(many=True)

    class Meta:
        model = Role
        fields = "__all__"

    def create(self, validated_data):
        permissions = validated_data.pop('permissions', None)

        if permissions == None:
            raise serializers.ValidationError(
                "You must set Permissions for the Role.")

        instance = self.Meta.model(**validated_data)
        instance.save()
        instance.permissions.add(*permissions)
        instance.save()
        return instance

```

### my_projects/07_react_django_practical/users_app/views.py:

```py
from rest_framework import exceptions, viewsets, status, generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import PermissionSerializer, UserSerializer, RoleSerializer
from .models import User, Permission, Role
from .auth import generate_access_token, JWTAuth
from .pagination import CustomPagination


class UserGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({"data": self.retrieve(request, pk).data})
        return Response({"data": self.list(request).data})

    def post(self, request):
        request.data.update({
            "password": 1234,
            "password_confirm": 1234,
            "role": request.data["role_id"]
        })
        return Response({"data": self.create(request).data})

    def put(self, request, pk=None):
        return Response({"data": self.update(request, pk).data})

    def delete(self, request, pk=None):
        return self.destroy(request, pk)


class AuthUser(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'data': serializer.data})


class PermissionAPIView(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = PermissionSerializer(Permission.objects.all(), many=True)
        return Response({'data': serializer.data})


class RoleViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Role.objects.all()
        serializer = RoleSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def create(self, request):
        serializer = RoleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(role)
        return Response({"data": serializer.data})

    def update(self, request, pk=None):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(instance=role, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        role = Role.objects.get(id=pk)
        role.delete()
        return Response({'message': 'Role deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def register(request):
    data = request.data
    if data['password'] != data['password_confirm']:
        raise exceptions.ValidationError('Passwords do not match')

    if User.objects.filter(email=data['email']).exists():
        raise exceptions.ValidationError('Email already exists')

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = User.objects.filter(email=email).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found')
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('Incorrect password')

    token = generate_access_token(user)
    # set token to http-only cookie
    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }
    return response


@api_view(['POST'])
def logout(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        'message': 'success'
    }
    return response

```

<img width="1404" alt="image" src="https://github.com/user-attachments/assets/727adcd6-e3af-4a11-8503-e291a4bad12b">
<img width="1392" alt="image" src="https://github.com/user-attachments/assets/349dd75d-883f-48b1-bea4-5e0c09557b90">
<img width="1392" alt="image" src="https://github.com/user-attachments/assets/8aaee9b3-27e5-4e53-87f1-5577316aefbd">

# #END</details>

<details>
<summary>20. Update User with Partial Update </summary>

# Update User with Partial Update

### my_projects/07_react_django_practical/users_app/views.py:

```py
from rest_framework import exceptions, viewsets, status, generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import PermissionSerializer, UserSerializer, RoleSerializer
from .models import User, Permission, Role
from .auth import generate_access_token, JWTAuth
from .pagination import CustomPagination


class UserGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({"data": self.retrieve(request, pk).data})
        return Response({"data": self.list(request).data})

    def post(self, request):
        request.data.update({
            "password": 1234,
            "password_confirm": 1234,
            "role": request.data["role_id"]
        })
        return Response({"data": self.create(request).data})

    def put(self, request, pk=None):
        if (request.data['role_id']):
            request.data.update({
                "role": request.data["role_id"]
            })
        # return Response({"data": self.update(request, pk).data})
        return Response({"data": self.partial_update(request, pk).data})

    def delete(self, request, pk=None):
        return self.destroy(request, pk)


class AuthUser(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'data': serializer.data})


class PermissionAPIView(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = PermissionSerializer(Permission.objects.all(), many=True)
        return Response({'data': serializer.data})


class RoleViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Role.objects.all()
        serializer = RoleSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def create(self, request):
        serializer = RoleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(role)
        return Response({"data": serializer.data})

    def update(self, request, pk=None):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(instance=role, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        role = Role.objects.get(id=pk)
        role.delete()
        return Response({'message': 'Role deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def register(request):
    data = request.data
    if data['password'] != data['password_confirm']:
        raise exceptions.ValidationError('Passwords do not match')

    if User.objects.filter(email=data['email']).exists():
        raise exceptions.ValidationError('Email already exists')

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = User.objects.filter(email=email).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found')
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('Incorrect password')

    token = generate_access_token(user)
    # set token to http-only cookie
    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }
    return response


@api_view(['POST'])
def logout(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        'message': 'success'
    }
    return response

```

<img width="1404" alt="image" src="https://github.com/user-attachments/assets/141eb3c4-cfea-45eb-a027-00f60d610a8c">
<img width="1404" alt="image" src="https://github.com/user-attachments/assets/890fec55-d9ec-4404-ab39-dab31df1c5e1">
<img width="1348" alt="image" src="https://github.com/user-attachments/assets/2c789b59-2eb4-4bb2-87b7-7dcd819752fd">

# #END</details>

<details>
<summary>21. Setup Profile API View for updating User Info </summary>

# Setup Profile API View for updating User Info

### my_projects/07_react_django_practical/users_app/urls.py:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('users/info', views.ProfileInfoAPIView.as_view(),
         name='users-profile-info'),
    path('users/password', views.ProfilePasswordAPIView.as_view(),
         name='users-profile-password'),
    path('users', views.UserGenericAPIView.as_view(), name='users'),
    path('users/<str:pk>', views.UserGenericAPIView.as_view(), name='users-detail'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('auth', views.AuthUser.as_view(), name='auth'),
    path('logout', views.logout, name='logout'),
    path('permissions', views.PermissionAPIView.as_view(), name='permissions'),
    path('roles', views.RoleViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='roles'),
    path('roles/<int:pk>', views.RoleViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='roles-detail'),

]

```

### my_projects/07_react_django_practical/users_app/views.py:

```py
from rest_framework import exceptions, viewsets, status, generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import PermissionSerializer, UserSerializer, RoleSerializer
from .models import User, Permission, Role
from .auth import generate_access_token, JWTAuth
from .pagination import CustomPagination


class ProfileInfoAPIView(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk=None):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ProfilePasswordAPIView(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk=None):
        user = request.user
        data = request.data

        if data['password'] != data['password_confirm']:
            raise exceptions.ValidationError('Passwords do not match')

        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

        # user.set_password(data['password'])
        # user.save()
        # return Response({'message': 'Password updated successfully!'})


class UserGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({"data": self.retrieve(request, pk).data})
        return Response({"data": self.list(request).data})

    def post(self, request):
        request.data.update({
            "password": 1234,
            "password_confirm": 1234,
            "role": request.data["role_id"]
        })
        return Response({"data": self.create(request).data})

    def put(self, request, pk=None):
        if (request.data['role_id']):
            request.data.update({
                "role": request.data["role_id"]
            })
        # return Response({"data": self.update(request, pk).data})
        return Response({"data": self.partial_update(request, pk).data})

    def delete(self, request, pk=None):
        return self.destroy(request, pk)


class AuthUser(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'data': serializer.data})


class PermissionAPIView(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = PermissionSerializer(Permission.objects.all(), many=True)
        return Response({'data': serializer.data})


class RoleViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Role.objects.all()
        serializer = RoleSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def create(self, request):
        serializer = RoleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(role)
        return Response({"data": serializer.data})

    def update(self, request, pk=None):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(instance=role, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        role = Role.objects.get(id=pk)
        role.delete()
        return Response({'message': 'Role deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def register(request):
    data = request.data
    if data['password'] != data['password_confirm']:
        raise exceptions.ValidationError('Passwords do not match')

    if User.objects.filter(email=data['email']).exists():
        raise exceptions.ValidationError('Email already exists')

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = User.objects.filter(email=email).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found')
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('Incorrect password')

    token = generate_access_token(user)
    # set token to http-only cookie
    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }
    return response


@api_view(['POST'])
def logout(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        'message': 'success'
    }
    return response

```

### my_projects/07_react_django_practical/users_app/serializers.py:

```py
from rest_framework import serializers
from .models import User, Permission, Role


class RoleRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return RoleSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)


class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    role = RoleRelatedField(many=False, queryset=Role.objects.all())

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name',
                  'email', 'password', 'password_confirm', 'role']  # '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError("Passwords do not match")

        # user = User.objects.create(**validated_data)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)  # Need to hash Password
        instance.save()
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        password_confirm = validated_data.pop('password_confirm', None)

        if password and password_confirm and password != password_confirm:
            raise serializers.ValidationError("Passwords do not match")

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class PermissionRelatedField(serializers.StringRelatedField):
    def to_representation(self, value):
        return PermissionSerializer(value).data

    def to_internal_value(self, data):
        return data


class RoleSerializer(serializers.ModelSerializer):
    # permissions = PermissionSerializer(many=True)
    permissions = PermissionRelatedField(many=True)

    class Meta:
        model = Role
        fields = "__all__"

    def create(self, validated_data):
        permissions = validated_data.pop('permissions', None)

        if permissions == None:
            raise serializers.ValidationError(
                "You must set Permissions for the Role.")

        instance = self.Meta.model(**validated_data)
        instance.save()
        instance.permissions.add(*permissions)
        instance.save()
        return instance

```

<img width="1404" alt="image" src="https://github.com/user-attachments/assets/8eaff98d-407d-4949-a9c0-9b98585c7a45">
<img width="1404" alt="image" src="https://github.com/user-attachments/assets/40258a5e-b43a-4c6a-8f14-f39568133c7b">
<img width="1360" alt="image" src="https://github.com/user-attachments/assets/216c97a9-dc13-4d51-be6a-c2914a5a2ed3">
<img width="1404" alt="image" src="https://github.com/user-attachments/assets/0dd0d948-dbef-44d4-be32-014239e42c32">
<img width="1404" alt="image" src="https://github.com/user-attachments/assets/62554f50-3206-42a6-a054-be0d3ca4d6a6">

![image](https://github.com/user-attachments/assets/7387c37f-0a74-426d-8759-397fe783fc4e)

<img width="1392" alt="image" src="https://github.com/user-attachments/assets/1035c3f0-0008-4882-9645-418538861164">
<img width="1392" alt="image" src="https://github.com/user-attachments/assets/35ddc82a-88de-4dd8-b871-604df3e572e0">

# #END</details>

<details>
<summary>22. Display user Permissions as Text </summary>

# Display user Permissions as Text 

### my_projects/07_react_django_practical/users_app/urls.py:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('users/info', views.ProfileInfoAPIView.as_view(),
         name='users-profile-info'),
    path('users/password', views.ProfilePasswordAPIView.as_view(),
         name='users-profile-password'),
    path('users', views.UserGenericAPIView.as_view(), name='users'),
    path('users/<str:pk>', views.UserGenericAPIView.as_view(), name='users-detail'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('auth', views.AuthUser.as_view(), name='auth'),
    path('logout', views.logout, name='logout'),
    path('permissions', views.PermissionAPIView.as_view(), name='permissions'),
    path('roles', views.RoleViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='roles'),
    path('roles/<int:pk>', views.RoleViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='roles-detail'),

]

```

### my_projects/07_react_django_practical/users_app/views.py:

```py
from rest_framework import exceptions, viewsets, status, generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import PermissionSerializer, UserSerializer, RoleSerializer
from .models import User, Permission, Role
from .auth import generate_access_token, JWTAuth
from .pagination import CustomPagination


class ProfileInfoAPIView(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk=None):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ProfilePasswordAPIView(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk=None):
        user = request.user
        data = request.data

        if data['password'] != data['password_confirm']:
            raise exceptions.ValidationError('Passwords do not match')

        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

        # user.set_password(data['password'])
        # user.save()
        # return Response({'message': 'Password updated successfully!'})


class UserGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({"data": self.retrieve(request, pk).data})
        return Response({"data": self.list(request).data})

    def post(self, request):
        request.data.update({
            "password": 1234,
            "password_confirm": 1234,
            "role": request.data["role_id"]
        })
        return Response({"data": self.create(request).data})

    def put(self, request, pk=None):
        if (request.data['role_id']):
            request.data.update({
                "role": request.data["role_id"]
            })
        # return Response({"data": self.update(request, pk).data})
        return Response({"data": self.partial_update(request, pk).data})

    def delete(self, request, pk=None):
        return self.destroy(request, pk)


class AuthUser(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        data = serializer.data
        data["permissions"] = [
            permission['name'] for permission in data['role']['permissions']]
        return Response({'data': data})


class PermissionAPIView(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = PermissionSerializer(Permission.objects.all(), many=True)
        return Response({'data': serializer.data})


class RoleViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Role.objects.all()
        serializer = RoleSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def create(self, request):
        serializer = RoleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(role)
        return Response({"data": serializer.data})

    def update(self, request, pk=None):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(instance=role, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        role = Role.objects.get(id=pk)
        role.delete()
        return Response({'message': 'Role deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def register(request):
    data = request.data
    if data['password'] != data['password_confirm']:
        raise exceptions.ValidationError('Passwords do not match')

    if User.objects.filter(email=data['email']).exists():
        raise exceptions.ValidationError('Email already exists')

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = User.objects.filter(email=email).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found')
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('Incorrect password')

    token = generate_access_token(user)
    # set token to http-only cookie
    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }
    return response


@api_view(['POST'])
def logout(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        'message': 'success'
    }
    return response

```

<img width="1404" alt="image" src="https://github.com/user-attachments/assets/09fc8c71-5aef-4f4a-969f-a5810138e31a">
<img width="1360" alt="image" src="https://github.com/user-attachments/assets/7d05dcbf-dfc8-46cb-b6a5-2c90bf77c28d">
<img width="1392" alt="image" src="https://github.com/user-attachments/assets/1e3fad15-6ba5-4ded-bb7a-31bb931280f0">

# #END</details>

<details>
<summary>23. Setup Product Model, URL, View and Serializer </summary>

# Setup Product Model, URL, View and Serializer

### Create App - Products

```py
docker-compose exec admin_project sh
python manage.py startapp products_app
```

### my_projects/07_react_django_practical/products_app/models.py:

```py
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    image = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created_at']


```

### my_projects/07_react_django_practical/admin_project/settings.py:

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
    'rest_framework',
    'users_app',
    'products_app'
]
```

### my_projects/07_react_django_practical/admin_project/urls.py:

```py
"""
URL configuration for admin_project project.

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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('users_app.urls')),
    path('api/v1/', include('products_app.urls')),
]

```

### my_projects/07_react_django_practical/products_app/urls.py:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('products', views.ProductGenericAPIView.as_view(), name='products-list'),
    path('products/<str:pk>', views.ProductGenericAPIView.as_view(),
         name='product-detail')
]

```

### my_projects/07_react_django_practical/products_app/views.py:

```py
from django.shortcuts import render
from rest_framework import generics, mixins, status, exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users_app.auth import generate_access_token, JWTAuth
from users_app.pagination import CustomPagination
from .models import Product
from .serializers import ProductSerializer


class ProductGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                            mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({"data": self.retrieve(request, pk).data})
        return Response({"data": self.list(request).data})

    def post(self, request):
        return Response({"data": self.create(request).data})

    def put(self, request, pk=None):
        return Response({"data": self.partial_update(request, pk).data})

    def delete(self, request, pk=None):
        return self.destroy(request, pk)

```

### my_projects/07_react_django_practical/products_app/serializers.py:

```py

from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

```

## Make Migrations

```py
python manage.py makemigrations
python manage.py migrate
```

```x
POST PRODUCTS - http://localhost:8000/api/v1/products
```

<img width="1404" alt="image" src="https://github.com/user-attachments/assets/b47bb38c-6f3e-4790-bc57-98d11092c530">


```x
GET PRODUCTS - http://localhost:8000/api/v1/products
```

<img width="1404" alt="image" src="https://github.com/user-attachments/assets/a1e9eeaf-419a-4a5b-adb4-d01fde4f4c0a">

```x
PUT PRODUCTS - http://localhost:8000/api/v1/products/1
```

<img width="1404" alt="image" src="https://github.com/user-attachments/assets/377b4456-09c3-4439-af21-754d58c8886f">

```x
DELETE PRODUCTS - http://localhost:8000/api/v1/products/1
```

<img width="1404" alt="image" src="https://github.com/user-attachments/assets/9550ab36-2103-460b-a51b-d0606387dd5a">

<img width="1392" alt="image" src="https://github.com/user-attachments/assets/b91d6430-7967-42df-ba1b-fa13c6e394fe">
<img width="1392" alt="image" src="https://github.com/user-attachments/assets/6720f9aa-6829-49b7-978f-82315bc4e901">
<img width="1392" alt="image" src="https://github.com/user-attachments/assets/098dcf81-8fff-465d-9428-96d04a4d72a9">
<img width="1392" alt="image" src="https://github.com/user-attachments/assets/63a7cdd0-2528-4601-8390-15ac1bfae7e6">

# #END</details>

<details>
<summary>24. Setup Uploading Images Functionality </summary>

# Setup Uploading Images Functionality

### my_projects/07_react_django_practical/admin_project/settings.py:

```py
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")  # BASE_DIR /'media'


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users_app.User'
```

### my_projects/07_react_django_practical/products_app/urls.py:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('products', views.ProductGenericAPIView.as_view(), name='products-list'),
    path('products/<str:pk>', views.ProductGenericAPIView.as_view(),
         name='product-detail'),
    path('upload', views.FileUploadView.as_view(), name='upload-file')
]

```

### my_projects/07_react_django_practical/products_app/views.py:

```py
from random import randint, randrange, choice
from string import ascii_letters, digits
from django.shortcuts import render
from django.core.files.storage import default_storage
from rest_framework import generics, mixins, status, exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser

from users_app.auth import generate_access_token, JWTAuth
from users_app.pagination import CustomPagination
from .models import Product
from .serializers import ProductSerializer


class ProductGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                            mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({"data": self.retrieve(request, pk).data})
        return Response({"data": self.list(request).data})

    def post(self, request):
        return Response({"data": self.create(request).data})

    def put(self, request, pk=None):
        return Response({"data": self.partial_update(request, pk).data})

    def delete(self, request, pk=None):
        return self.destroy(request, pk)


class FileUploadView(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def post(self, request):
        file = request.FILES.get('image')
        if not file:
            raise exceptions.ValidationError(
                {"file": "Image file is required."})
        letters_and_digits = ascii_letters + digits
        random_value = ''.join(choice(letters_and_digits)
                               for _ in range(6)) or randrange(100000, 1000000)
        file.name = f"{random_value.lower()}-" + file.name.replace(" ", "_")
        file_name = default_storage.save(file.name, file)
        url = default_storage.url(file_name)
        return Response({"data": {"file": file.name, "url": url}})

```

### my_projects/07_react_django_practical/products_app/models.py:

```py
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    image = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created_at']

```

<img width="1360" alt="image" src="https://github.com/user-attachments/assets/85374fbb-0f64-4b56-a7d9-370e88034bd3">
<img width="1392" alt="image" src="https://github.com/user-attachments/assets/8ae262bd-68f2-473d-83c4-64a5449df284">

<img width="1392" alt="image" src="https://github.com/user-attachments/assets/4f397302-badf-4a4a-9863-00ff1ce570a9">
<img width="1392" alt="image" src="https://github.com/user-attachments/assets/4e42559a-9b1c-4cdf-92b1-899d2c9f1e5e">
<img width="1392" alt="image" src="https://github.com/user-attachments/assets/f8259acd-c190-4aeb-b57a-befe484fd828">

# #END</details>

<details>
<summary>25. Setup Route to View Uploaded Images </summary>

# Setup Route to View Uploaded Images

### my_projects/07_react_django_practical/admin_project/settings.py:

```py
# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [
#        'rest_framework.permissions.IsAuthenticated',
#     ],
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#        'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ],
# }

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")  # BASE_DIR /'media'


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users_app.User'
```

### my_projects/07_react_django_practical/products_app/urls.py:

```py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('products', views.ProductGenericAPIView.as_view(), name='products-list'),
    path('products/<str:pk>', views.ProductGenericAPIView.as_view(),
         name='product-detail'),
    path('upload', views.FileUploadView.as_view(), name='upload-file')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

### my_projects/07_react_django_practical/products_app/views.py:

```py

from random import randint, randrange, choice
from string import ascii_letters, digits
from django.shortcuts import render
from django.core.files.storage import default_storage
from rest_framework import generics, mixins, status, exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser

from users_app.auth import generate_access_token, JWTAuth
from users_app.pagination import CustomPagination
from .models import Product
from .serializers import ProductSerializer


class ProductGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                            mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({"data": self.retrieve(request, pk).data})
        return Response({"data": self.list(request).data})

    def post(self, request):
        return Response({"data": self.create(request).data})

    def put(self, request, pk=None):
        return Response({"data": self.partial_update(request, pk).data})

    def delete(self, request, pk=None):
        return self.destroy(request, pk)


class FileUploadView(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def post(self, request):
        file = request.FILES.get('image')
        if not file:
            raise exceptions.ValidationError(
                {"file": "Image file is required."})
        letters_and_digits = ascii_letters + digits
        random_value = ''.join(choice(letters_and_digits)
                               for _ in range(6)) or randrange(100000, 1000000)
        file.name = f"{random_value.lower()}-" + file.name.replace(" ", "_")
        file_name = default_storage.save(file.name, file)
        url = default_storage.url(file_name)
        return Response({"data": {"file": file.name, "url": "http://localhost:8000/api/v1" + url}})

```

### my_projects/07_react_django_practical/products_app/models.py:

```py
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    image = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created_at']

```


<img width="1404" alt="image" src="https://github.com/user-attachments/assets/6fa178d5-4c75-48de-ae86-44ffbe1ddec7">
<img width="1404" alt="image" src="https://github.com/user-attachments/assets/4c2f3948-43ae-4e16-b189-e5ef688edc5e">

<img width="1392" alt="image" src="https://github.com/user-attachments/assets/a5b2d6b7-3c56-4f1e-9931-e4a0852756b5">
<img width="1392" alt="image" src="https://github.com/user-attachments/assets/dbd1e6b1-f170-4f03-8267-9812fa49251d">

# #END</details>

<details>
<summary>26. Create Orders App </summary>

# Create Orders App

```py
python manage.py startapp orders_app
```

### my_projects/07_react_django_practical/admin_project/settings.py:

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
    'rest_framework',
    'users_app',
    'products_app',
    'orders_app',
]

```

### my_projects/07_react_django_practical/admin_project/urls.py:

```py
"""
URL configuration for admin_project project.

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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('users_app.urls')),
    path('api/v1/', include('products_app.urls')),
    path('api/v1/', include('orders_app.urls')),
]

```

### my_projects/07_react_django_practical/orders_app/urls.py:

```py
from django.urls import path
from . import views


urlpatterns = [
    # path('orders', views.ProductGenericAPIView.as_view(), name='orders-list'),
    # path('orders/<str:pk>', views.ProductGenericAPIView.as_view(),
    #      name='order-detail'),
]

```

### my_projects/07_react_django_practical/orders_app/models.py:

```py
from django.db import models


class Order(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderItem(models.Model):
    product_title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order_items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

```

## Run Migrations:

```py
python manage.py makemigrations
python manage.py migrate
```

<img width="1392" alt="image" src="https://github.com/user-attachments/assets/e00a9604-3506-43bd-ba34-ce2f0be651dc">
<img width="1392" alt="image" src="https://github.com/user-attachments/assets/01d9b701-a80d-49f6-88c0-dfcf89b10e48">
<img width="1392" alt="image" src="https://github.com/user-attachments/assets/6ff04a4c-60cd-46b8-84fa-ad4b9bfb74af">

# #END</details>

<details>
<summary>27. Setup URLs, Views and Serializer for Orders App </summary>

# Setup URLs, Views and Serializer for Orders App

### my_projects/07_react_django_practical/orders_app/models.py:

```py
from django.db import models


class Order(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderItem(models.Model):
    product_title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order_items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

```

### my_projects/07_react_django_practical/orders_app/urls.py:

```py
from django.urls import path
from . import views


urlpatterns = [
    path('orders', views.OrderGenericAPIView.as_view(), name='orders-list'),
    path('orders/<str:pk>', views.OrderGenericAPIView.as_view(),
         name='order-detail'),
]

```

### my_projects/07_react_django_practical/orders_app/views.py:

```py
from rest_framework import generics, mixins, status, exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users_app.auth import generate_access_token, JWTAuth
from users_app.pagination import CustomPagination
from .models import Order
from .serializers import OrderSerializer


class OrderGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({"data": self.retrieve(request, pk).data})
        return Response({"data": self.list(request).data})

```

### my_projects/07_react_django_practical/orders_app/serializers.py:

```py
from rest_framework import serializers

from .models import OrderItem, Order


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

```

<img width="1392" alt="image" src="https://github.com/user-attachments/assets/a7181b4e-1ca1-465f-8469-278776f575b4">
<img width="1392" alt="image" src="https://github.com/user-attachments/assets/867c1830-9e7b-4af6-b7b0-919b2dacc28a">
<img width="1392" alt="image" src="https://github.com/user-attachments/assets/5a5618ac-40d1-421d-9cd4-30c014f9fcc1">
<img width="1392" alt="image" src="https://github.com/user-attachments/assets/f7716362-7c35-4c03-85b1-3bd2bd22f02b">

# #END</details>

<details>
<summary>28. Load Data into Orders App Model using Fixtures </summary>

# Load Data into Orders App Model using Fixtures

### my_projects/07_react_django_practical/orders_app/models.py:

```py
from django.db import models


class Order(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderItem(models.Model):
    product_title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order_items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

```

### my_projects/07_react_django_practical/fixtures/orders.json:

```json
[
    {
        "model": "orders_app.order",
        "pk": 1,
        "fields": {
            "first_name": "First Name #1",
            "last_name": "Last Name #1",
            "email": "Email #1",
            "created_at": "2020-1-1 00:00:00",
            "updated_at": "2020-1-1 00:00:00"
        }
    },
    {
        "model": "orders_app.order",
        "pk": 2,
        "fields": {
            "first_name": "First Name #2",
            "last_name": "Last Name #2",
            "email": "Email #2",
            "created_at": "2020-2-1 00:00:00",
            "updated_at": "2020-2-1 00:00:00"
        }
    },
    {
        "model": "orders_app.order",
        "pk": 3,
        "fields": {
            "first_name": "First Name #3",
            "last_name": "Last Name #3",
            "email": "Email #3",
            "created_at": "2020-3-1 00:00:00",
            "updated_at": "2020-3-1 00:00:00"
        }
    },
    {
        "model": "orders_app.orderitem",
        "pk": 1,
        "fields": {
            "order_id": 1,
            "product_title": "Title #1",
            "price": 10,
            "quantity": 2,
            "created_at": "2020-1-1 00:00:00",
            "updated_at": "2020-1-1 00:00:00"
        }
    },
    {
        "model": "orders_app.orderitem",
        "pk": 2,
        "fields": {
            "order_id": 1,
            "product_title": "Title #2",
            "price": 20,
            "quantity": 3,
            "created_at": "2020-1-1 00:00:00",
            "updated_at": "2020-1-1 00:00:00"
        }
    },
    {
        "model": "orders_app.orderitem",
        "pk": 3,
        "fields": {
            "order_id": 2,
            "product_title": "Title #3",
            "price": 30,
            "quantity": 3,
            "created_at": "2020-2-1 00:00:00",
            "updated_at": "2020-2-1 00:00:00"
        }
    },
    {
        "model": "orders_app.orderitem",
        "pk": 4,
        "fields": {
            "order_id": 2,
            "product_title": "Title #4",
            "price": 40,
            "quantity": 4,
            "created_at": "2020-2-1 00:00:00",
            "updated_at": "2020-2-1 00:00:00"
        }
    },
    {
        "model": "orders_app.orderitem",
        "pk": 5,
        "fields": {
            "order_id": 3,
            "product_title": "Title #5",
            "price": 50,
            "quantity": 5,
            "created_at": "2020-3-1 00:00:00",
            "updated_at": "2020-3-1 00:00:00"
        }
    },
    {
        "model": "orders_app.orderitem",
        "pk": 6,
        "fields": {
            "order_id": 3,
            "product_title": "Title #6",
            "price": 60,
            "quantity": 6,
            "created_at": "2020-3-1 00:00:00",
            "updated_at": "2020-3-1 00:00:00"
        }
    }
]
```

## Load Data into Model:

```x
python manage.py loaddata fixtures/orders.json
```

![image](https://github.com/user-attachments/assets/2facf028-e04f-453f-a6ec-fdf6cae113a4)
![image](https://github.com/user-attachments/assets/c6a7a281-3ad2-4a26-9460-729cbba11a30)
![image](https://github.com/user-attachments/assets/e032bff4-19c3-4d35-a964-509bc6c624fe)

<img width="1404" alt="image" src="https://github.com/user-attachments/assets/ff950c35-25ea-4f9d-adb9-d5ce4ea4a8a0">
<img width="1360" alt="image" src="https://github.com/user-attachments/assets/38346fdc-ad57-4496-97ca-a6ce4c30bd5e">
<img width="1404" alt="image" src="https://github.com/user-attachments/assets/3d220f34-765c-4a56-8580-886e965bb5a9">

# #END</details>

<details>
<summary>29. Calculate Total cost of items with Serializer Method Fields for Orders Serializer </summary>

# Calculate Total cost of items with Serializer Method Fields for Orders Serializer

### my_projects/07_react_django_practical/orders_app/serializers.py:

```py
from rest_framework import serializers

from .models import OrderItem, Order


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField('get_total')

    def get_total(self, obj):
        items = OrderItem.objects.filter(order_id=obj.id)
        return sum((item.price * item.quantity) for item in items)

    class Meta:
        model = Order
        fields = '__all__'

```

<img width="1404" alt="image" src="https://github.com/user-attachments/assets/bf73403b-47a5-40ac-b872-1d97fc20f2eb">
<img width="1404" alt="image" src="https://github.com/user-attachments/assets/ff3c99f7-557a-465a-a4d5-727c0751094c">
<img width="1404" alt="image" src="https://github.com/user-attachments/assets/5d121b77-df93-46d1-83ee-22c512fedd50">
<img width="1392" alt="image" src="https://github.com/user-attachments/assets/f871a5ca-87b3-4544-9a56-f96fc7101a31">

# #END</details>

<details>
<summary>30. Export CSV with Data </summary>

# Export CSV with Data

### my_projects/07_react_django_practical/orders_app/models.py:

```py
from django.db import models


class Order(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'


class OrderItem(models.Model):
    product_title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order_items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

```

### my_projects/07_react_django_practical/orders_app/urls.py:

```py
from django.urls import path
from . import views


urlpatterns = [
    path('orders', views.OrderGenericAPIView.as_view(), name='orders-list'),
    path('orders/export', views.ExportAPIView.as_view(), name='export-orders'),
    path('orders/<str:pk>', views.OrderGenericAPIView.as_view(),
         name='order-detail'),
]

```

### my_projects/07_react_django_practical/orders_app/views.py:

```py
import csv
from django.http import JsonResponse, HttpResponse
from rest_framework import generics, mixins, status, exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users_app.auth import generate_access_token, JWTAuth
from users_app.pagination import CustomPagination
from .models import Order, OrderItem
from .serializers import OrderSerializer


class OrderGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({"data": self.retrieve(request, pk).data})
        return Response({"data": self.list(request).data})


class ExportAPIView(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="orders.csv"'

        orders = Order.objects.all()
        writer = csv.writer(response)

        writer.writerow(
            ['ID', 'Name', 'Email', 'Product Title', 'Price', 'Quantity'])

        for order in orders:
            for item in order.order_items.all():
                writer.writerow([order.id, order.name, order.email,
                                item.product_title, item.price, item.quantity])

        # for order in orders:
        #     writer.writerow([order.id, order.name, order.email, '', '', ''])
        #     orderItems = OrderItem.objects.all().filter(order_id=order.id)

        #     for item in orderItems:
        #         writer.writerow(
        #             ['', '', '', item.product_title, item.price, item.quantity])

        return response

```

```x
http://localhost:8000/api/v1/orders/export
```

<img width="1404" alt="image" src="https://github.com/user-attachments/assets/de929d6f-347f-4a3b-8507-90f02eec36b8">
<img width="1392" alt="image" src="https://github.com/user-attachments/assets/caa6d1e9-9603-4e89-8bb2-ae40fd28f568">
<img width="1392" alt="image" src="https://github.com/user-attachments/assets/9f0faa8a-15a3-45fd-a4aa-fb799a02b991">
<img width="1392" alt="image" src="https://github.com/user-attachments/assets/e5de69db-760a-4c9f-85cc-9a35fc390115">

# #END</details>

<details>
<summary>31. Create ChartAPIView with Raw SQL Queries </summary>

# Create ChartAPIView with Raw SQL Queries

### my_projects/07_react_django_practical/orders_app/models.py:

```py
from django.db import models


class Order(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'


class OrderItem(models.Model):
    product_title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order_items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

```

### my_projects/07_react_django_practical/orders_app/urls.py:

```py
from django.urls import path
from . import views


urlpatterns = [
    path('orders', views.OrderGenericAPIView.as_view(), name='orders-list'),
    path('orders/export', views.ExportAPIView.as_view(), name='export-orders'),
    path('orders/chart', views.ChartAPIView.as_view(), name='chart-orders'),
    path('orders/<str:pk>', views.OrderGenericAPIView.as_view(),
         name='order-detail'),
]

```

### my_projects/07_react_django_practical/orders_app/views.py:

```py
import csv
from django.http import JsonResponse, HttpResponse
from django.db import connection
from rest_framework import generics, mixins, status, exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users_app.auth import generate_access_token, JWTAuth
from users_app.pagination import CustomPagination
from .models import Order, OrderItem
from .serializers import OrderSerializer


class OrderGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({"data": self.retrieve(request, pk).data})
        return Response({"data": self.list(request).data})


class ExportAPIView(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="orders.csv"'

        orders = Order.objects.all()
        writer = csv.writer(response)

        writer.writerow(
            ['ID', 'Name', 'Email', 'Product Title', 'Price', 'Quantity'])

        for order in orders:
            for item in order.order_items.all():
                writer.writerow([order.id, order.name, order.email,
                                item.product_title, item.price, item.quantity])

        # for order in orders:
        #     writer.writerow([order.id, order.name, order.email, '', '', ''])
        #     orderItems = OrderItem.objects.all().filter(order_id=order.id)

        #     for item in orderItems:
        #         writer.writerow(
        #             ['', '', '', item.product_title, item.price, item.quantity])

        return response


class ChartAPIView(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def get(self, _):
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT DATE_FORMAT(o.created_at, '%Y-%m-%d') as date, sum(i.quantity * i.price) as sum
            FROM orders_app_order as o
            JOIN orders_app_orderitem as i ON o.id = i.order_id
            GROUP BY date
            """
        )
        rows = cursor.fetchall()

        data = []
        for row in rows:
            data.append({
                'date': row[0],
                'sum': row[1]
            })
        return Response({'rows': rows, 'data': data}, status=status.HTTP_200_OK)

```

<img width="1360" alt="image" src="https://github.com/user-attachments/assets/2905145e-55f1-44e2-a01a-081fe36d0798">
<img width="1392" alt="image" src="https://github.com/user-attachments/assets/18f2b452-a8c0-4831-942e-697a4efc7edd">
<img width="1392" alt="image" src="https://github.com/user-attachments/assets/c246faf0-8fd9-412f-ad37-a5300f621154">
<img width="1392" alt="image" src="https://github.com/user-attachments/assets/e0201179-bcd7-46ad-a620-d6a038881bc8">

# #END</details>

<details>
<summary>32. Setup Permissions for User Roles </summary>

# Setup Permissions for User Roles

### my_projects/07_react_django_practical/users_app/permissions.py:

```py
from rest_framework import permissions
from users_app.serializers import UserSerializer


class ViewPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        # if request.method == 'GET':
        #     return True
        # return False

        data = UserSerializer(request.user).data

        view_access = any(
            p['name'] == 'view_' + view.permission_object for p in data['role']['permissions'])
        edit_access = any(
            p['name'] == 'edit_' + view.permission_object for p in data['role']['permissions'])

        if request.method == 'GET':
            return view_access or edit_access
        return edit_access

```

### my_projects/07_react_django_practical/users_app/views.py:

```py
from rest_framework import exceptions, viewsets, status, generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import PermissionSerializer, UserSerializer, RoleSerializer
from .models import User, Permission, Role
from .auth import generate_access_token, JWTAuth
from .pagination import CustomPagination
from .permissions import ViewPermissions


class ProfileInfoAPIView(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk=None):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ProfilePasswordAPIView(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk=None):
        user = request.user
        data = request.data

        if data['password'] != data['password_confirm']:
            raise exceptions.ValidationError('Passwords do not match')

        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

        # user.set_password(data['password'])
        # user.save()
        # return Response({'message': 'Password updated successfully!'})


class UserGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated & ViewPermissions]
    permission_object = 'users'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({"data": self.retrieve(request, pk).data})
        return Response({"data": self.list(request).data})

    def post(self, request):
        request.data.update({
            "password": 1234,
            "password_confirm": 1234,
            "role": request.data["role_id"]
        })
        return Response({"data": self.create(request).data})

    def put(self, request, pk=None):
        if (request.data['role_id']):
            request.data.update({
                "role": request.data["role_id"]
            })
        # return Response({"data": self.update(request, pk).data})
        return Response({"data": self.partial_update(request, pk).data})

    def delete(self, request, pk=None):
        return self.destroy(request, pk)


class AuthUser(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        data = serializer.data
        data["permissions"] = [
            permission['name'] for permission in data['role']['permissions']]
        return Response({'data': data})


class PermissionAPIView(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = PermissionSerializer(Permission.objects.all(), many=True)
        return Response({'data': serializer.data})


class RoleViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated & ViewPermissions]
    permission_object = 'roles'

    def list(self, request):
        queryset = Role.objects.all()
        serializer = RoleSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def create(self, request):
        serializer = RoleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(role)
        return Response({"data": serializer.data})

    def update(self, request, pk=None):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(instance=role, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        role = Role.objects.get(id=pk)
        role.delete()
        return Response({'message': 'Role deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def register(request):
    data = request.data
    if data['password'] != data['password_confirm']:
        raise exceptions.ValidationError('Passwords do not match')

    if User.objects.filter(email=data['email']).exists():
        raise exceptions.ValidationError('Email already exists')

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = User.objects.filter(email=email).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found')
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('Incorrect password')

    token = generate_access_token(user)
    # set token to http-only cookie
    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }
    return response


@api_view(['POST'])
def logout(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        'message': 'success'
    }
    return response

```

<img width="1147" alt="image" src="https://github.com/user-attachments/assets/88a08e0e-bb89-4b56-aacd-4efb45078fe0">
<img width="1147" alt="image" src="https://github.com/user-attachments/assets/d97f13c3-9131-45a1-a901-3651ba7eae8c">

# #END</details>

<details>
<summary>33. Setup Cors </summary>

# Setup Cors

```x
pip install django-cors-headers
```

### my_projects/07_react_django_practical/admin_project/settings.py:

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
    'rest_framework',
    'corsheaders', # added
    'users_app',
    'products_app',
    'orders_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # added
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users_app.User'


CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
```

<img width="1329" alt="image" src="https://github.com/user-attachments/assets/8b082e10-cbb1-4ef7-b50e-a1c8238d45d8">

# #END</details>

<details>
<summary>34. Frontend - Install React App </summary>

# Frontend - Install React App

## Check Node Version

```x
node -v
npm -v
```

## Create React app - react-admin

```x
npx create-react-app react-admin --template typescript
```

## Run React App

```x
cd react-admin
npm run start
```

### my_projects/07_react_django_practical/react-admin/src/App.tsx:

```tsx
import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;

```

![image](https://github.com/user-attachments/assets/8861cdeb-08a7-42cd-a64d-5edef6554439)

<img width="1329" alt="image" src="https://github.com/user-attachments/assets/39a7a025-0dc5-4bc7-b4da-572a3dc41727">
<img width="1329" alt="image" src="https://github.com/user-attachments/assets/3421dc61-1b6a-49a7-9ec7-4c71cd5343fc">

# #END</details>

<details>
<summary>35. Frontend - Setup Bootstrap Dashboard Template </summary>

# Frontend - Setup Bootstrap Dashboard Template

## [https://getbootstrap.com/docs/5.3/examples/](https://getbootstrap.com/docs/5.3/examples/)

![image](https://github.com/user-attachments/assets/5478985c-5c82-47e8-8afa-42c803645a4e)
![image](https://github.com/user-attachments/assets/d975bce8-ba16-444b-9138-d0c46cf3ed25)
![image](https://github.com/user-attachments/assets/f0b69830-97b6-4f12-b8bc-fd9ab7477ebc)
![image](https://github.com/user-attachments/assets/15a44eee-fe7f-4353-998d-425488ee82c8)

![image](https://github.com/user-attachments/assets/21e7b403-ae25-4363-96a8-ab8ac52744c3)

### my_projects/07_react_django_practical/react-admin/public/index.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta
      name="description"
      content="Web site created using create-react-app"
    />
    <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
    <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />

    <!-- Custom styles for this template -->
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.min.css"
      rel="stylesheet"
    />
    <!-- Custom styles for this template -->
    <!-- <link href="dashboard.css" rel="stylesheet" /> -->

    <title>React App</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
      crossorigin="anonymous"
    />
  </head>
  <body>
    <div id="root"></div>
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://cdn.jsdelivr.net/npm/chart.js@4.3.2/dist/chart.umd.js"
      integrity="sha384-eI7PSr3L1XLISH8JdDII5YN/njoSsxfbrkCTnJrzXt+ENP5MOVBxD+l6sEG4zoLp"
      crossorigin="anonymous"
    ></script>
    <!-- Custom script for this template -->
    <script type="text/jsx" src="../src/dashboard.js"></script>
  </body>
</html>

```

### my_projects/07_react_django_practical/react-admin/src/dashboard.js:

```js
/* globals Chart:false */

(() => {
  "use strict";

  // Graphs
  const ctx = document.getElementById("myChart");
  // eslint-disable-next-line no-unused-vars
  const myChart = new Chart(ctx, {
    type: "line",
    data: {
      labels: [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
      ],
      datasets: [
        {
          data: [15339, 21345, 18483, 24003, 23489, 24092, 12034],
          lineTension: 0,
          backgroundColor: "transparent",
          borderColor: "#007bff",
          borderWidth: 4,
          pointBackgroundColor: "#007bff",
        },
      ],
    },
    options: {
      plugins: {
        legend: {
          display: false,
        },
        tooltip: {
          boxPadding: 3,
        },
      },
    },
  });
})();

```

### my_projects/07_react_django_practical/react-admin/src/index.tsx:

```tsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
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

### my_projects/07_react_django_practical/react-admin/src/App.tsx:

```tsx
import React from "react";
import logo from "./logo.svg";
import "./App.css";

function App() {
  return (
    <div className="App">
      <svg xmlns="http://www.w3.org/2000/svg" className="d-none">
        <symbol id="check2" viewBox="0 0 16 16">
          <path d="M13.854 3.646a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L6.5 10.293l6.646-6.647a.5.5 0 0 1 .708 0z" />
        </symbol>
        <symbol id="circle-half" viewBox="0 0 16 16">
          <path d="M8 15A7 7 0 1 0 8 1v14zm0 1A8 8 0 1 1 8 0a8 8 0 0 1 0 16z" />
        </symbol>
        <symbol id="moon-stars-fill" viewBox="0 0 16 16">
          <path d="M6 .278a.768.768 0 0 1 .08.858 7.208 7.208 0 0 0-.878 3.46c0 4.021 3.278 7.277 7.318 7.277.527 0 1.04-.055 1.533-.16a.787.787 0 0 1 .81.316.733.733 0 0 1-.031.893A8.349 8.349 0 0 1 8.344 16C3.734 16 0 12.286 0 7.71 0 4.266 2.114 1.312 5.124.06A.752.752 0 0 1 6 .278z" />
          <path d="M10.794 3.148a.217.217 0 0 1 .412 0l.387 1.162c.173.518.579.924 1.097 1.097l1.162.387a.217.217 0 0 1 0 .412l-1.162.387a1.734 1.734 0 0 0-1.097 1.097l-.387 1.162a.217.217 0 0 1-.412 0l-.387-1.162A1.734 1.734 0 0 0 9.31 6.593l-1.162-.387a.217.217 0 0 1 0-.412l1.162-.387a1.734 1.734 0 0 0 1.097-1.097l.387-1.162zM13.863.099a.145.145 0 0 1 .274 0l.258.774c.115.346.386.617.732.732l.774.258a.145.145 0 0 1 0 .274l-.774.258a1.156 1.156 0 0 0-.732.732l-.258.774a.145.145 0 0 1-.274 0l-.258-.774a1.156 1.156 0 0 0-.732-.732l-.774-.258a.145.145 0 0 1 0-.274l.774-.258c.346-.115.617-.386.732-.732L13.863.1z" />
        </symbol>
        <symbol id="sun-fill" viewBox="0 0 16 16">
          <path d="M8 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0zm0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13zm8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5zM3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8zm10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0zm-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0zm9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707zM4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708z" />
        </symbol>
      </svg>

      <div className="dropdown position-fixed bottom-0 end-0 mb-3 me-3 bd-mode-toggle">
        <button
          className="btn btn-bd-primary py-2 dropdown-toggle d-flex align-items-center"
          id="bd-theme"
          type="button"
          aria-expanded="false"
          data-bs-toggle="dropdown"
          aria-label="Toggle theme (auto)"
        >
          <svg className="bi my-1 theme-icon-active" width="1em" height="1em">
            <use href="#circle-half"></use>
          </svg>
          <span className="visually-hidden" id="bd-theme-text">
            Toggle theme
          </span>
        </button>
        <ul
          className="dropdown-menu dropdown-menu-end shadow"
          aria-labelledby="bd-theme-text"
        >
          <li>
            <button
              type="button"
              className="dropdown-item d-flex align-items-center"
              data-bs-theme-value="light"
              aria-pressed="false"
            >
              <svg className="bi me-2 opacity-50" width="1em" height="1em">
                <use href="#sun-fill"></use>
              </svg>
              Light
              <svg className="bi ms-auto d-none" width="1em" height="1em">
                <use href="#check2"></use>
              </svg>
            </button>
          </li>
          <li>
            <button
              type="button"
              className="dropdown-item d-flex align-items-center"
              data-bs-theme-value="dark"
              aria-pressed="false"
            >
              <svg className="bi me-2 opacity-50" width="1em" height="1em">
                <use href="#moon-stars-fill"></use>
              </svg>
              Dark
              <svg className="bi ms-auto d-none" width="1em" height="1em">
                <use href="#check2"></use>
              </svg>
            </button>
          </li>
          <li>
            <button
              type="button"
              className="dropdown-item d-flex align-items-center active"
              data-bs-theme-value="auto"
              aria-pressed="true"
            >
              <svg className="bi me-2 opacity-50" width="1em" height="1em">
                <use href="#circle-half"></use>
              </svg>
              Auto
              <svg className="bi ms-auto d-none" width="1em" height="1em">
                <use href="#check2"></use>
              </svg>
            </button>
          </li>
        </ul>
      </div>

      <svg xmlns="http://www.w3.org/2000/svg" className="d-none">
        <symbol id="calendar3" viewBox="0 0 16 16">
          <path d="M14 0H2a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2zM1 3.857C1 3.384 1.448 3 2 3h12c.552 0 1 .384 1 .857v10.286c0 .473-.448.857-1 .857H2c-.552 0-1-.384-1-.857V3.857z" />
          <path d="M6.5 7a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm-9 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm-9 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2z" />
        </symbol>
        <symbol id="cart" viewBox="0 0 16 16">
          <path d="M0 1.5A.5.5 0 0 1 .5 1H2a.5.5 0 0 1 .485.379L2.89 3H14.5a.5.5 0 0 1 .49.598l-1 5a.5.5 0 0 1-.465.401l-9.397.472L4.415 11H13a.5.5 0 0 1 0 1H4a.5.5 0 0 1-.491-.408L2.01 3.607 1.61 2H.5a.5.5 0 0 1-.5-.5zM3.102 4l.84 4.479 9.144-.459L13.89 4H3.102zM5 12a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm7 0a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm-7 1a1 1 0 1 1 0 2 1 1 0 0 1 0-2zm7 0a1 1 0 1 1 0 2 1 1 0 0 1 0-2z" />
        </symbol>
        <symbol id="chevron-right" viewBox="0 0 16 16">
          <path
            fill-rule="evenodd"
            d="M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708z"
          />
        </symbol>
        <symbol id="door-closed" viewBox="0 0 16 16">
          <path d="M3 2a1 1 0 0 1 1-1h8a1 1 0 0 1 1 1v13h1.5a.5.5 0 0 1 0 1h-13a.5.5 0 0 1 0-1H3V2zm1 13h8V2H4v13z" />
          <path d="M9 9a1 1 0 1 0 2 0 1 1 0 0 0-2 0z" />
        </symbol>
        <symbol id="file-earmark" viewBox="0 0 16 16">
          <path d="M14 4.5V14a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h5.5L14 4.5zm-3 0A1.5 1.5 0 0 1 9.5 3V1H4a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V4.5h-2z" />
        </symbol>
        <symbol id="file-earmark-text" viewBox="0 0 16 16">
          <path d="M5.5 7a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1h-5zM5 9.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5zm0 2a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 0 1h-2a.5.5 0 0 1-.5-.5z" />
          <path d="M9.5 0H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V4.5L9.5 0zm0 1v2A1.5 1.5 0 0 0 11 4.5h2V14a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h5.5z" />
        </symbol>
        <symbol id="gear-wide-connected" viewBox="0 0 16 16">
          <path d="M7.068.727c.243-.97 1.62-.97 1.864 0l.071.286a.96.96 0 0 0 1.622.434l.205-.211c.695-.719 1.888-.03 1.613.931l-.08.284a.96.96 0 0 0 1.187 1.187l.283-.081c.96-.275 1.65.918.931 1.613l-.211.205a.96.96 0 0 0 .434 1.622l.286.071c.97.243.97 1.62 0 1.864l-.286.071a.96.96 0 0 0-.434 1.622l.211.205c.719.695.03 1.888-.931 1.613l-.284-.08a.96.96 0 0 0-1.187 1.187l.081.283c.275.96-.918 1.65-1.613.931l-.205-.211a.96.96 0 0 0-1.622.434l-.071.286c-.243.97-1.62.97-1.864 0l-.071-.286a.96.96 0 0 0-1.622-.434l-.205.211c-.695.719-1.888.03-1.613-.931l.08-.284a.96.96 0 0 0-1.186-1.187l-.284.081c-.96.275-1.65-.918-.931-1.613l.211-.205a.96.96 0 0 0-.434-1.622l-.286-.071c-.97-.243-.97-1.62 0-1.864l.286-.071a.96.96 0 0 0 .434-1.622l-.211-.205c-.719-.695-.03-1.888.931-1.613l.284.08a.96.96 0 0 0 1.187-1.186l-.081-.284c-.275-.96.918-1.65 1.613-.931l.205.211a.96.96 0 0 0 1.622-.434l.071-.286zM12.973 8.5H8.25l-2.834 3.779A4.998 4.998 0 0 0 12.973 8.5zm0-1a4.998 4.998 0 0 0-7.557-3.779l2.834 3.78h4.723zM5.048 3.967c-.03.021-.058.043-.087.065l.087-.065zm-.431.355A4.984 4.984 0 0 0 3.002 8c0 1.455.622 2.765 1.615 3.678L7.375 8 4.617 4.322zm.344 7.646.087.065-.087-.065z" />
        </symbol>
        <symbol id="graph-up" viewBox="0 0 16 16">
          <path
            fill-rule="evenodd"
            d="M0 0h1v15h15v1H0V0Zm14.817 3.113a.5.5 0 0 1 .07.704l-4.5 5.5a.5.5 0 0 1-.74.037L7.06 6.767l-3.656 5.027a.5.5 0 0 1-.808-.588l4-5.5a.5.5 0 0 1 .758-.06l2.609 2.61 4.15-5.073a.5.5 0 0 1 .704-.07Z"
          />
        </symbol>
        <symbol id="house-fill" viewBox="0 0 16 16">
          <path d="M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L8 2.207l6.646 6.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.707 1.5Z" />
          <path d="m8 3.293 6 6V13.5a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 2 13.5V9.293l6-6Z" />
        </symbol>
        <symbol id="list" viewBox="0 0 16 16">
          <path
            fill-rule="evenodd"
            d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5z"
          />
        </symbol>
        <symbol id="people" viewBox="0 0 16 16">
          <path d="M15 14s1 0 1-1-1-4-5-4-5 3-5 4 1 1 1 1h8Zm-7.978-1A.261.261 0 0 1 7 12.996c.001-.264.167-1.03.76-1.72C8.312 10.629 9.282 10 11 10c1.717 0 2.687.63 3.24 1.276.593.69.758 1.457.76 1.72l-.008.002a.274.274 0 0 1-.014.002H7.022ZM11 7a2 2 0 1 0 0-4 2 2 0 0 0 0 4Zm3-2a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM6.936 9.28a5.88 5.88 0 0 0-1.23-.247A7.35 7.35 0 0 0 5 9c-4 0-5 3-5 4 0 .667.333 1 1 1h4.216A2.238 2.238 0 0 1 5 13c0-1.01.377-2.042 1.09-2.904.243-.294.526-.569.846-.816ZM4.92 10A5.493 5.493 0 0 0 4 13H1c0-.26.164-1.03.76-1.724.545-.636 1.492-1.256 3.16-1.275ZM1.5 5.5a3 3 0 1 1 6 0 3 3 0 0 1-6 0Zm3-2a2 2 0 1 0 0 4 2 2 0 0 0 0-4Z" />
        </symbol>
        <symbol id="plus-circle" viewBox="0 0 16 16">
          <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z" />
          <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z" />
        </symbol>
        <symbol id="puzzle" viewBox="0 0 16 16">
          <path d="M3.112 3.645A1.5 1.5 0 0 1 4.605 2H7a.5.5 0 0 1 .5.5v.382c0 .696-.497 1.182-.872 1.469a.459.459 0 0 0-.115.118.113.113 0 0 0-.012.025L6.5 4.5v.003l.003.01c.004.01.014.028.036.053a.86.86 0 0 0 .27.194C7.09 4.9 7.51 5 8 5c.492 0 .912-.1 1.19-.24a.86.86 0 0 0 .271-.194.213.213 0 0 0 .039-.063v-.009a.112.112 0 0 0-.012-.025.459.459 0 0 0-.115-.118c-.375-.287-.872-.773-.872-1.469V2.5A.5.5 0 0 1 9 2h2.395a1.5 1.5 0 0 1 1.493 1.645L12.645 6.5h.237c.195 0 .42-.147.675-.48.21-.274.528-.52.943-.52.568 0 .947.447 1.154.862C15.877 6.807 16 7.387 16 8s-.123 1.193-.346 1.638c-.207.415-.586.862-1.154.862-.415 0-.733-.246-.943-.52-.255-.333-.48-.48-.675-.48h-.237l.243 2.855A1.5 1.5 0 0 1 11.395 14H9a.5.5 0 0 1-.5-.5v-.382c0-.696.497-1.182.872-1.469a.459.459 0 0 0 .115-.118.113.113 0 0 0 .012-.025L9.5 11.5v-.003a.214.214 0 0 0-.039-.064.859.859 0 0 0-.27-.193C8.91 11.1 8.49 11 8 11c-.491 0-.912.1-1.19.24a.859.859 0 0 0-.271.194.214.214 0 0 0-.039.063v.003l.001.006a.113.113 0 0 0 .012.025c.016.027.05.068.115.118.375.287.872.773.872 1.469v.382a.5.5 0 0 1-.5.5H4.605a1.5 1.5 0 0 1-1.493-1.645L3.356 9.5h-.238c-.195 0-.42.147-.675.48-.21.274-.528.52-.943.52-.568 0-.947-.447-1.154-.862C.123 9.193 0 8.613 0 8s.123-1.193.346-1.638C.553 5.947.932 5.5 1.5 5.5c.415 0 .733.246.943.52.255.333.48.48.675.48h.238l-.244-2.855zM4.605 3a.5.5 0 0 0-.498.55l.001.007.29 3.4A.5.5 0 0 1 3.9 7.5h-.782c-.696 0-1.182-.497-1.469-.872a.459.459 0 0 0-.118-.115.112.112 0 0 0-.025-.012L1.5 6.5h-.003a.213.213 0 0 0-.064.039.86.86 0 0 0-.193.27C1.1 7.09 1 7.51 1 8c0 .491.1.912.24 1.19.07.14.14.225.194.271a.213.213 0 0 0 .063.039H1.5l.006-.001a.112.112 0 0 0 .025-.012.459.459 0 0 0 .118-.115c.287-.375.773-.872 1.469-.872H3.9a.5.5 0 0 1 .498.542l-.29 3.408a.5.5 0 0 0 .497.55h1.878c-.048-.166-.195-.352-.463-.557-.274-.21-.52-.528-.52-.943 0-.568.447-.947.862-1.154C6.807 10.123 7.387 10 8 10s1.193.123 1.638.346c.415.207.862.586.862 1.154 0 .415-.246.733-.52.943-.268.205-.415.39-.463.557h1.878a.5.5 0 0 0 .498-.55l-.001-.007-.29-3.4A.5.5 0 0 1 12.1 8.5h.782c.696 0 1.182.497 1.469.872.05.065.091.099.118.115.013.008.021.01.025.012a.02.02 0 0 0 .006.001h.003a.214.214 0 0 0 .064-.039.86.86 0 0 0 .193-.27c.14-.28.24-.7.24-1.191 0-.492-.1-.912-.24-1.19a.86.86 0 0 0-.194-.271.215.215 0 0 0-.063-.039H14.5l-.006.001a.113.113 0 0 0-.025.012.459.459 0 0 0-.118.115c-.287.375-.773.872-1.469.872H12.1a.5.5 0 0 1-.498-.543l.29-3.407a.5.5 0 0 0-.497-.55H9.517c.048.166.195.352.463.557.274.21.52.528.52.943 0 .568-.447.947-.862 1.154C9.193 5.877 8.613 6 8 6s-1.193-.123-1.638-.346C5.947 5.447 5.5 5.068 5.5 4.5c0-.415.246-.733.52-.943.268-.205.415-.39.463-.557H4.605z" />
        </symbol>
        <symbol id="search" viewBox="0 0 16 16">
          <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z" />
        </symbol>
      </svg>

      <header
        className="navbar sticky-top bg-dark flex-md-nowrap p-0 shadow"
        data-bs-theme="dark"
      >
        <a
          className="navbar-brand col-md-3 col-lg-2 me-0 px-3 fs-6 text-white"
          href="#"
        >
          Company name
        </a>

        <ul className="navbar-nav flex-row d-md-none">
          <li className="nav-item text-nowrap">
            <button
              className="nav-link px-3 text-white"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#navbarSearch"
              aria-controls="navbarSearch"
              aria-expanded="false"
              aria-label="Toggle search"
            >
              <svg className="bi">
                <use xlinkHref="#search" />
              </svg>
            </button>
          </li>
          <li className="nav-item text-nowrap">
            <button
              className="nav-link px-3 text-white"
              type="button"
              data-bs-toggle="offcanvas"
              data-bs-target="#sidebarMenu"
              aria-controls="sidebarMenu"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <svg className="bi">
                <use xlinkHref="#list" />
              </svg>
            </button>
          </li>
        </ul>

        <div id="navbarSearch" className="navbar-search w-100 collapse">
          <input
            className="form-control w-100 rounded-0 border-0"
            type="text"
            placeholder="Search"
            aria-label="Search"
          />
        </div>
      </header>

      <div className="container-fluid">
        <div className="row">
          <div className="sidebar border border-right col-md-3 col-lg-2 p-0 bg-body-tertiary">
            <div
              className="offcanvas-md offcanvas-end bg-body-tertiary"
              tabIndex={-1}
              id="sidebarMenu"
              aria-labelledby="sidebarMenuLabel"
            >
              <div className="offcanvas-header">
                <h5 className="offcanvas-title" id="sidebarMenuLabel">
                  Company name
                </h5>
                <button
                  type="button"
                  className="btn-close"
                  data-bs-dismiss="offcanvas"
                  data-bs-target="#sidebarMenu"
                  aria-label="Close"
                ></button>
              </div>
              <div className="offcanvas-body d-md-flex flex-column p-0 pt-lg-3 overflow-y-auto">
                <ul className="nav flex-column">
                  <li className="nav-item">
                    <a
                      className="nav-link d-flex align-items-center gap-2 active"
                      aria-current="page"
                      href="#"
                    >
                      <svg className="bi">
                        <use xlinkHref="#house-fill" />
                      </svg>
                      Dashboard
                    </a>
                  </li>
                  <li className="nav-item">
                    <a
                      className="nav-link d-flex align-items-center gap-2"
                      href="#"
                    >
                      <svg className="bi">
                        <use xlinkHref="#file-earmark" />
                      </svg>
                      Orders
                    </a>
                  </li>
                  <li className="nav-item">
                    <a
                      className="nav-link d-flex align-items-center gap-2"
                      href="#"
                    >
                      <svg className="bi">
                        <use xlinkHref="#cart" />
                      </svg>
                      Products
                    </a>
                  </li>
                  <li className="nav-item">
                    <a
                      className="nav-link d-flex align-items-center gap-2"
                      href="#"
                    >
                      <svg className="bi">
                        <use xlinkHref="#people" />
                      </svg>
                      Customers
                    </a>
                  </li>
                  <li className="nav-item">
                    <a
                      className="nav-link d-flex align-items-center gap-2"
                      href="#"
                    >
                      <svg className="bi">
                        <use xlinkHref="#graph-up" />
                      </svg>
                      Reports
                    </a>
                  </li>
                  <li className="nav-item">
                    <a
                      className="nav-link d-flex align-items-center gap-2"
                      href="#"
                    >
                      <svg className="bi">
                        <use xlinkHref="#puzzle" />
                      </svg>
                      Integrations
                    </a>
                  </li>
                </ul>

                <h6 className="sidebar-heading d-flex justify-content-between align-items-center px-3 mt-4 mb-1 text-body-secondary text-uppercase">
                  <span>Saved reports</span>
                  <a
                    className="link-secondary"
                    href="#"
                    aria-label="Add a new report"
                  >
                    <svg className="bi">
                      <use xlinkHref="#plus-circle" />
                    </svg>
                  </a>
                </h6>
                <ul className="nav flex-column mb-auto">
                  <li className="nav-item">
                    <a
                      className="nav-link d-flex align-items-center gap-2"
                      href="#"
                    >
                      <svg className="bi">
                        <use xlinkHref="#file-earmark-text" />
                      </svg>
                      Current month
                    </a>
                  </li>
                  <li className="nav-item">
                    <a
                      className="nav-link d-flex align-items-center gap-2"
                      href="#"
                    >
                      <svg className="bi">
                        <use xlinkHref="#file-earmark-text" />
                      </svg>
                      Last quarter
                    </a>
                  </li>
                  <li className="nav-item">
                    <a
                      className="nav-link d-flex align-items-center gap-2"
                      href="#"
                    >
                      <svg className="bi">
                        <use xlinkHref="#file-earmark-text" />
                      </svg>
                      Social engagement
                    </a>
                  </li>
                  <li className="nav-item">
                    <a
                      className="nav-link d-flex align-items-center gap-2"
                      href="#"
                    >
                      <svg className="bi">
                        <use xlinkHref="#file-earmark-text" />
                      </svg>
                      Year-end sale
                    </a>
                  </li>
                </ul>

                <hr className="my-3" />

                <ul className="nav flex-column mb-auto">
                  <li className="nav-item">
                    <a
                      className="nav-link d-flex align-items-center gap-2"
                      href="#"
                    >
                      <svg className="bi">
                        <use xlinkHref="#gear-wide-connected" />
                      </svg>
                      Settings
                    </a>
                  </li>
                  <li className="nav-item">
                    <a
                      className="nav-link d-flex align-items-center gap-2"
                      href="#"
                    >
                      <svg className="bi">
                        <use xlinkHref="#door-closed" />
                      </svg>
                      Sign out
                    </a>
                  </li>
                </ul>
              </div>
            </div>
          </div>

          <main className="col-md-9 ms-sm-auto col-lg-10 px-md-4">
            <div className="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
              <h1 className="h2">Dashboard</h1>
              <div className="btn-toolbar mb-2 mb-md-0">
                <div className="btn-group me-2">
                  <button
                    type="button"
                    className="btn btn-sm btn-outline-secondary"
                  >
                    Share
                  </button>
                  <button
                    type="button"
                    className="btn btn-sm btn-outline-secondary"
                  >
                    Export
                  </button>
                </div>
                <button
                  type="button"
                  className="btn btn-sm btn-outline-secondary dropdown-toggle d-flex align-items-center gap-1"
                >
                  <svg className="bi">
                    <use xlinkHref="#calendar3" />
                  </svg>
                  This week
                </button>
              </div>
            </div>

            <canvas
              className="my-4 w-100"
              id="myChart"
              width="900"
              height="380"
            ></canvas>

            <h2>Section title</h2>
            <div className="table-responsive small">
              <table className="table table-striped table-sm">
                <thead>
                  <tr>
                    <th scope="col">#</th>
                    <th scope="col">Header</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>1,001</td>
                    <td>random</td>
                    <td>data</td>
                    <td>placeholder</td>
                    <td>text</td>
                  </tr>
                  <tr>
                    <td>1,015</td>
                    <td>random</td>
                    <td>tabular</td>
                    <td>information</td>
                    <td>text</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </main>
        </div>
      </div>
    </div>
  );
}

export default App;

```

### my_projects/07_react_django_practical/react-admin/src/App.css:

```css
.bi {
  display: inline-block;
  width: 1rem;
  height: 1rem;
}

/*
 * Sidebar
 */

@media (min-width: 768px) {
  .sidebar .offcanvas-lg {
    position: -webkit-sticky;
    position: sticky;
    top: 48px;
  }

  .navbar-search {
    display: block;
  }
}

.sidebar .nav-link {
  font-size: .875rem;
  font-weight: 500;
}

.sidebar .nav-link.active {
  color: #2470dc;
}

.sidebar-heading {
  font-size: .75rem;
}

/*
 * Navbar
 */

.navbar-brand {
  padding-top: .75rem;
  padding-bottom: .75rem;
  background-color: rgba(0, 0, 0, .25);
  box-shadow: inset -1px 0 0 rgba(0, 0, 0, .25);
}

.navbar .form-control {
  padding: .75rem 1rem;
}
```

![image](https://github.com/user-attachments/assets/e0a83e25-35a7-414d-a3cd-324389b0cb88)

<img width="1333" alt="image" src="https://github.com/user-attachments/assets/650fd3a1-6106-4100-998f-cbb7f4331eed">
<img width="1333" alt="image" src="https://github.com/user-attachments/assets/81bb9442-8e6c-47e4-a871-7e6bf9ba5132">
<img width="1333" alt="image" src="https://github.com/user-attachments/assets/244b430d-0756-4ecf-b3b1-8c6985ea4bc2">

# #END</details>

<details>
<summary>36. Frontend - Setup Nav, Menu and Dashboard Components </summary>

# Frontend - Setup Nav, Menu and Dashboard Components

### my_projects/07_react_django_practical/react-admin/src/index.tsx:

```tsx
import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";

const root = ReactDOM.createRoot(
  document.getElementById("root") as HTMLElement
);
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

### my_projects/07_react_django_practical/react-admin/src/App.tsx:

```tsx
import "./App.css";
import Nav from "./components/Nav";
import Menu from "./components/Menu";
import Dashboard from "./components/Dashboard";

function App() {
  return (
    <div className="App">
      <Nav />
      <div className="container-fluid">
        <div className="row">
          <Menu />
          <main className="col-md-9 ms-sm-auto col-lg-10 px-md-4">
            <Dashboard />
          </main>
        </div>
      </div>
    </div>
  );
}

export default App;

```

### my_projects/07_react_django_practical/react-admin/src/components/Nav.tsx:

```tsx
import React from "react";

const Nav = () => (
  <nav>
    <svg xmlns="http://www.w3.org/2000/svg" className="d-none">
      <symbol id="calendar3" viewBox="0 0 16 16">
        <path d="M14 0H2a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2zM1 3.857C1 3.384 1.448 3 2 3h12c.552 0 1 .384 1 .857v10.286c0 .473-.448.857-1 .857H2c-.552 0-1-.384-1-.857V3.857z" />
        <path d="M6.5 7a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm-9 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm-9 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2z" />
      </symbol>
      <symbol id="cart" viewBox="0 0 16 16">
        <path d="M0 1.5A.5.5 0 0 1 .5 1H2a.5.5 0 0 1 .485.379L2.89 3H14.5a.5.5 0 0 1 .49.598l-1 5a.5.5 0 0 1-.465.401l-9.397.472L4.415 11H13a.5.5 0 0 1 0 1H4a.5.5 0 0 1-.491-.408L2.01 3.607 1.61 2H.5a.5.5 0 0 1-.5-.5zM3.102 4l.84 4.479 9.144-.459L13.89 4H3.102zM5 12a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm7 0a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm-7 1a1 1 0 1 1 0 2 1 1 0 0 1 0-2zm7 0a1 1 0 1 1 0 2 1 1 0 0 1 0-2z" />
      </symbol>
      <symbol id="chevron-right" viewBox="0 0 16 16">
        <path
          fill-rule="evenodd"
          d="M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708z"
        />
      </symbol>
      <symbol id="door-closed" viewBox="0 0 16 16">
        <path d="M3 2a1 1 0 0 1 1-1h8a1 1 0 0 1 1 1v13h1.5a.5.5 0 0 1 0 1h-13a.5.5 0 0 1 0-1H3V2zm1 13h8V2H4v13z" />
        <path d="M9 9a1 1 0 1 0 2 0 1 1 0 0 0-2 0z" />
      </symbol>
      <symbol id="file-earmark" viewBox="0 0 16 16">
        <path d="M14 4.5V14a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h5.5L14 4.5zm-3 0A1.5 1.5 0 0 1 9.5 3V1H4a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V4.5h-2z" />
      </symbol>
      <symbol id="file-earmark-text" viewBox="0 0 16 16">
        <path d="M5.5 7a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1h-5zM5 9.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5zm0 2a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 0 1h-2a.5.5 0 0 1-.5-.5z" />
        <path d="M9.5 0H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V4.5L9.5 0zm0 1v2A1.5 1.5 0 0 0 11 4.5h2V14a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h5.5z" />
      </symbol>
      <symbol id="gear-wide-connected" viewBox="0 0 16 16">
        <path d="M7.068.727c.243-.97 1.62-.97 1.864 0l.071.286a.96.96 0 0 0 1.622.434l.205-.211c.695-.719 1.888-.03 1.613.931l-.08.284a.96.96 0 0 0 1.187 1.187l.283-.081c.96-.275 1.65.918.931 1.613l-.211.205a.96.96 0 0 0 .434 1.622l.286.071c.97.243.97 1.62 0 1.864l-.286.071a.96.96 0 0 0-.434 1.622l.211.205c.719.695.03 1.888-.931 1.613l-.284-.08a.96.96 0 0 0-1.187 1.187l.081.283c.275.96-.918 1.65-1.613.931l-.205-.211a.96.96 0 0 0-1.622.434l-.071.286c-.243.97-1.62.97-1.864 0l-.071-.286a.96.96 0 0 0-1.622-.434l-.205.211c-.695.719-1.888.03-1.613-.931l.08-.284a.96.96 0 0 0-1.186-1.187l-.284.081c-.96.275-1.65-.918-.931-1.613l.211-.205a.96.96 0 0 0-.434-1.622l-.286-.071c-.97-.243-.97-1.62 0-1.864l.286-.071a.96.96 0 0 0 .434-1.622l-.211-.205c-.719-.695-.03-1.888.931-1.613l.284.08a.96.96 0 0 0 1.187-1.186l-.081-.284c-.275-.96.918-1.65 1.613-.931l.205.211a.96.96 0 0 0 1.622-.434l.071-.286zM12.973 8.5H8.25l-2.834 3.779A4.998 4.998 0 0 0 12.973 8.5zm0-1a4.998 4.998 0 0 0-7.557-3.779l2.834 3.78h4.723zM5.048 3.967c-.03.021-.058.043-.087.065l.087-.065zm-.431.355A4.984 4.984 0 0 0 3.002 8c0 1.455.622 2.765 1.615 3.678L7.375 8 4.617 4.322zm.344 7.646.087.065-.087-.065z" />
      </symbol>
      <symbol id="graph-up" viewBox="0 0 16 16">
        <path
          fill-rule="evenodd"
          d="M0 0h1v15h15v1H0V0Zm14.817 3.113a.5.5 0 0 1 .07.704l-4.5 5.5a.5.5 0 0 1-.74.037L7.06 6.767l-3.656 5.027a.5.5 0 0 1-.808-.588l4-5.5a.5.5 0 0 1 .758-.06l2.609 2.61 4.15-5.073a.5.5 0 0 1 .704-.07Z"
        />
      </symbol>
      <symbol id="house-fill" viewBox="0 0 16 16">
        <path d="M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L8 2.207l6.646 6.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.707 1.5Z" />
        <path d="m8 3.293 6 6V13.5a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 2 13.5V9.293l6-6Z" />
      </symbol>
      <symbol id="list" viewBox="0 0 16 16">
        <path
          fill-rule="evenodd"
          d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5z"
        />
      </symbol>
      <symbol id="people" viewBox="0 0 16 16">
        <path d="M15 14s1 0 1-1-1-4-5-4-5 3-5 4 1 1 1 1h8Zm-7.978-1A.261.261 0 0 1 7 12.996c.001-.264.167-1.03.76-1.72C8.312 10.629 9.282 10 11 10c1.717 0 2.687.63 3.24 1.276.593.69.758 1.457.76 1.72l-.008.002a.274.274 0 0 1-.014.002H7.022ZM11 7a2 2 0 1 0 0-4 2 2 0 0 0 0 4Zm3-2a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM6.936 9.28a5.88 5.88 0 0 0-1.23-.247A7.35 7.35 0 0 0 5 9c-4 0-5 3-5 4 0 .667.333 1 1 1h4.216A2.238 2.238 0 0 1 5 13c0-1.01.377-2.042 1.09-2.904.243-.294.526-.569.846-.816ZM4.92 10A5.493 5.493 0 0 0 4 13H1c0-.26.164-1.03.76-1.724.545-.636 1.492-1.256 3.16-1.275ZM1.5 5.5a3 3 0 1 1 6 0 3 3 0 0 1-6 0Zm3-2a2 2 0 1 0 0 4 2 2 0 0 0 0-4Z" />
      </symbol>
      <symbol id="plus-circle" viewBox="0 0 16 16">
        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z" />
        <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z" />
      </symbol>
      <symbol id="puzzle" viewBox="0 0 16 16">
        <path d="M3.112 3.645A1.5 1.5 0 0 1 4.605 2H7a.5.5 0 0 1 .5.5v.382c0 .696-.497 1.182-.872 1.469a.459.459 0 0 0-.115.118.113.113 0 0 0-.012.025L6.5 4.5v.003l.003.01c.004.01.014.028.036.053a.86.86 0 0 0 .27.194C7.09 4.9 7.51 5 8 5c.492 0 .912-.1 1.19-.24a.86.86 0 0 0 .271-.194.213.213 0 0 0 .039-.063v-.009a.112.112 0 0 0-.012-.025.459.459 0 0 0-.115-.118c-.375-.287-.872-.773-.872-1.469V2.5A.5.5 0 0 1 9 2h2.395a1.5 1.5 0 0 1 1.493 1.645L12.645 6.5h.237c.195 0 .42-.147.675-.48.21-.274.528-.52.943-.52.568 0 .947.447 1.154.862C15.877 6.807 16 7.387 16 8s-.123 1.193-.346 1.638c-.207.415-.586.862-1.154.862-.415 0-.733-.246-.943-.52-.255-.333-.48-.48-.675-.48h-.237l.243 2.855A1.5 1.5 0 0 1 11.395 14H9a.5.5 0 0 1-.5-.5v-.382c0-.696.497-1.182.872-1.469a.459.459 0 0 0 .115-.118.113.113 0 0 0 .012-.025L9.5 11.5v-.003a.214.214 0 0 0-.039-.064.859.859 0 0 0-.27-.193C8.91 11.1 8.49 11 8 11c-.491 0-.912.1-1.19.24a.859.859 0 0 0-.271.194.214.214 0 0 0-.039.063v.003l.001.006a.113.113 0 0 0 .012.025c.016.027.05.068.115.118.375.287.872.773.872 1.469v.382a.5.5 0 0 1-.5.5H4.605a1.5 1.5 0 0 1-1.493-1.645L3.356 9.5h-.238c-.195 0-.42.147-.675.48-.21.274-.528.52-.943.52-.568 0-.947-.447-1.154-.862C.123 9.193 0 8.613 0 8s.123-1.193.346-1.638C.553 5.947.932 5.5 1.5 5.5c.415 0 .733.246.943.52.255.333.48.48.675.48h.238l-.244-2.855zM4.605 3a.5.5 0 0 0-.498.55l.001.007.29 3.4A.5.5 0 0 1 3.9 7.5h-.782c-.696 0-1.182-.497-1.469-.872a.459.459 0 0 0-.118-.115.112.112 0 0 0-.025-.012L1.5 6.5h-.003a.213.213 0 0 0-.064.039.86.86 0 0 0-.193.27C1.1 7.09 1 7.51 1 8c0 .491.1.912.24 1.19.07.14.14.225.194.271a.213.213 0 0 0 .063.039H1.5l.006-.001a.112.112 0 0 0 .025-.012.459.459 0 0 0 .118-.115c.287-.375.773-.872 1.469-.872H3.9a.5.5 0 0 1 .498.542l-.29 3.408a.5.5 0 0 0 .497.55h1.878c-.048-.166-.195-.352-.463-.557-.274-.21-.52-.528-.52-.943 0-.568.447-.947.862-1.154C6.807 10.123 7.387 10 8 10s1.193.123 1.638.346c.415.207.862.586.862 1.154 0 .415-.246.733-.52.943-.268.205-.415.39-.463.557h1.878a.5.5 0 0 0 .498-.55l-.001-.007-.29-3.4A.5.5 0 0 1 12.1 8.5h.782c.696 0 1.182.497 1.469.872.05.065.091.099.118.115.013.008.021.01.025.012a.02.02 0 0 0 .006.001h.003a.214.214 0 0 0 .064-.039.86.86 0 0 0 .193-.27c.14-.28.24-.7.24-1.191 0-.492-.1-.912-.24-1.19a.86.86 0 0 0-.194-.271.215.215 0 0 0-.063-.039H14.5l-.006.001a.113.113 0 0 0-.025.012.459.459 0 0 0-.118.115c-.287.375-.773.872-1.469.872H12.1a.5.5 0 0 1-.498-.543l.29-3.407a.5.5 0 0 0-.497-.55H9.517c.048.166.195.352.463.557.274.21.52.528.52.943 0 .568-.447.947-.862 1.154C9.193 5.877 8.613 6 8 6s-1.193-.123-1.638-.346C5.947 5.447 5.5 5.068 5.5 4.5c0-.415.246-.733.52-.943.268-.205.415-.39.463-.557H4.605z" />
      </symbol>
      <symbol id="search" viewBox="0 0 16 16">
        <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z" />
      </symbol>
    </svg>

    <header
      className="navbar sticky-top bg-secondary flex-md-nowrap p-0 shadow"
      data-bs-theme="dark"
    >
      <a
        className="navbar-brand col-md-3 col-lg-2 me-0 px-3 fs-6 text-white"
        href="#"
      >
        Company name
      </a>

      <ul className="navbar-nav flex-row d-md-none">
        <li className="nav-item text-nowrap">
          <button
            className="nav-link px-3 text-white"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarSearch"
            aria-controls="navbarSearch"
            aria-expanded="false"
            aria-label="Toggle search"
          >
            <svg className="bi">
              <use xlinkHref="#search" />
            </svg>
          </button>
        </li>
        <li className="nav-item text-nowrap">
          <button
            className="nav-link px-3 text-white"
            type="button"
            data-bs-toggle="offcanvas"
            data-bs-target="#sidebarMenu"
            aria-controls="sidebarMenu"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <svg className="bi">
              <use xlinkHref="#list" />
            </svg>
          </button>
        </li>
      </ul>

      <div id="navbarSearch" className="navbar-search w-100 collapse">
        <input
          className="form-control w-100 rounded-0 border-0"
          type="text"
          placeholder="Search"
          aria-label="Search"
        />
      </div>
    </header>
  </nav>
);

export default Nav;

```

### my_projects/07_react_django_practical/react-admin/src/components/Menu.tsx:

```tsx
import React from "react";

const Menu = () => (
  <div className="sidebar border border-right col-md-3 col-lg-2 p-0 bg-body-tertiary">
    <div
      className="offcanvas-md offcanvas-end bg-body-tertiary"
      tabIndex={-1}
      id="sidebarMenu"
      aria-labelledby="sidebarMenuLabel"
    >
      <div className="offcanvas-header">
        <h5 className="offcanvas-title" id="sidebarMenuLabel">
          Company name
        </h5>
        <button
          type="button"
          className="btn-close"
          data-bs-dismiss="offcanvas"
          data-bs-target="#sidebarMenu"
          aria-label="Close"
        ></button>
      </div>
      <div className="offcanvas-body d-md-flex flex-column p-0 pt-lg-3 overflow-y-auto">
        <ul className="nav flex-column">
          <li className="nav-item">
            <a
              className="nav-link d-flex align-items-center gap-2 active"
              aria-current="page"
              href="#"
            >
              <svg className="bi">
                <use xlinkHref="#house-fill" />
              </svg>
              Dashboard
            </a>
          </li>
          <li className="nav-item">
            <a className="nav-link d-flex align-items-center gap-2" href="#">
              <svg className="bi">
                <use xlinkHref="#file-earmark" />
              </svg>
              Orders
            </a>
          </li>
          <li className="nav-item">
            <a className="nav-link d-flex align-items-center gap-2" href="#">
              <svg className="bi">
                <use xlinkHref="#cart" />
              </svg>
              Products
            </a>
          </li>
          <li className="nav-item">
            <a className="nav-link d-flex align-items-center gap-2" href="#">
              <svg className="bi">
                <use xlinkHref="#people" />
              </svg>
              Customers
            </a>
          </li>
          <li className="nav-item">
            <a className="nav-link d-flex align-items-center gap-2" href="#">
              <svg className="bi">
                <use xlinkHref="#graph-up" />
              </svg>
              Reports
            </a>
          </li>
        </ul>

        <h6 className="sidebar-heading d-flex justify-content-between align-items-center px-3 mt-4 mb-1 text-body-secondary text-uppercase">
          <span>Saved reports</span>
          <a className="link-secondary" href="#" aria-label="Add a new report">
            <svg className="bi">
              <use xlinkHref="#plus-circle" />
            </svg>
          </a>
        </h6>
        <ul className="nav flex-column mb-auto">
          <li className="nav-item">
            <a className="nav-link d-flex align-items-center gap-2" href="#">
              <svg className="bi">
                <use xlinkHref="#file-earmark-text" />
              </svg>
              Current month
            </a>
          </li>
        </ul>

        <hr className="my-3" />

        <ul className="nav flex-column mb-auto">
          <li className="nav-item">
            <a className="nav-link d-flex align-items-center gap-2" href="#">
              <svg className="bi">
                <use xlinkHref="#gear-wide-connected" />
              </svg>
              Settings
            </a>
          </li>
          <li className="nav-item">
            <a className="nav-link d-flex align-items-center gap-2" href="#">
              <svg className="bi">
                <use xlinkHref="#door-closed" />
              </svg>
              Sign out
            </a>
          </li>
        </ul>
      </div>
    </div>
  </div>
);

export default Menu;

```

### my_projects/07_react_django_practical/react-admin/src/components/Dashboard.tsx:

```tsx
import React from "react";

const Dashboard = () => (
  <>
    <h2>Section title</h2>
    <div className="table-responsive small">
      <table className="table table-striped table-sm">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Header</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1,001</td>
            <td>random</td>
            <td>data</td>
            <td>placeholder</td>
            <td>text</td>
          </tr>
          <tr>
            <td>1,015</td>
            <td>random</td>
            <td>tabular</td>
            <td>information</td>
            <td>text</td>
          </tr>
        </tbody>
      </table>
    </div>

    {/* Chart  */}
    <div className="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
      <h1 className="h2">Dashboard</h1>
      <div className="btn-toolbar mb-2 mb-md-0">
        <div className="btn-group me-2">
          <button type="button" className="btn btn-sm btn-outline-secondary">
            Share
          </button>
          <button type="button" className="btn btn-sm btn-outline-secondary">
            Export
          </button>
        </div>
        <button
          type="button"
          className="btn btn-sm btn-outline-secondary dropdown-toggle d-flex align-items-center gap-1"
        >
          <svg className="bi">
            <use xlinkHref="#calendar3" />
          </svg>
          This week
        </button>
      </div>
    </div>

    <canvas
      className="my-4 w-100"
      id="myChart"
      width="900"
      height="380"
    ></canvas>
  </>
);

export default Dashboard;

```

![image](https://github.com/user-attachments/assets/b6b3578c-6764-4768-abfb-70cd0f2d77e7)
![image](https://github.com/user-attachments/assets/4e75e2d5-8ff0-4e0d-89c5-83c818cac6eb)
![image](https://github.com/user-attachments/assets/59534de0-8d93-4012-a444-a5b9b6c8f422)

<img width="1440" alt="image" src="https://github.com/user-attachments/assets/280ac8ac-01c5-4f71-ba60-2049f57d885f">
<img width="1440" alt="image" src="https://github.com/user-attachments/assets/2c3162c8-366c-428a-b384-2c672ffdb2d0">

# #END</details>

<details>
<summary>37. Frontend - Setup Routes </summary>

# Frontend - Setup Routes

### Install React-Router-DOM

```x
npm install react-router-dom @types/react-router-dom
```

### my_projects/07_react_django_practical/react-admin/src/index.tsx:

```tsx
import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";

const root = ReactDOM.createRoot(
  document.getElementById("root") as HTMLElement
);
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

### my_projects/07_react_django_practical/react-admin/src/App.tsx:

```tsx
import "./App.css";
import Nav from "./components/Nav";
import Menu from "./components/Menu";
import Dashboard from "./components/Dashboard";
import Users from "./components/secure/Users";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";

function App() {
  return (
    <Router>
      <div className="App">
        <Nav />
        <div className="container-fluid">
          <div className="row">
            <Menu />
            <main className="col-md-9 ms-sm-auto col-lg-10 px-md-4">
              <Routes>
                <Route path="/" index element={<Dashboard />} />
                <Route path="/users" element={<Users />} />
              </Routes>
            </main>
          </div>
        </div>
      </div>
    </Router>
  );
}

export default App;

```

### my_projects/07_react_django_practical/react-admin/src/components/secure/Users.tsx:

```tsx
import React from "react";

const Users = () => {
  return (
    <div>
      <h1>Users List</h1>
    </div>
  );
};

export default Users;

```

```x
GET: http://localhost:3000/
```

![image](https://github.com/user-attachments/assets/e86c3c32-3687-4a37-a50e-814f2903f773)


```x
GET: http://localhost:3000/users
```

![image](https://github.com/user-attachments/assets/3802f772-23e3-4c3f-8c3a-11b3544ab971)

<img width="1440" alt="image" src="https://github.com/user-attachments/assets/a091fafd-1490-4c8b-bb23-0895a3dad2f7">
<img width="1440" alt="image" src="https://github.com/user-attachments/assets/126070c8-f63e-4ff2-866e-21f32e83d48e">

# #END</details>

<details>
<summary>38. Frontend - Setup Layout for components as Child Props, including Login Form </summary>

# Frontend - Setup Layout for components as Child Props, including Login Form

### my_projects/07_react_django_practical/react-admin/src/App.tsx:

```tsx
import "./App.css";
import Dashboard from "./components/Dashboard";
import Users from "./components/secure/Users";
import Login from "./components/public/Login";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" index element={<Dashboard />} />
          <Route path="/users" element={<Users />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

```

### my_projects/07_react_django_practical/react-admin/src/components/Layout.tsx:

```tsx
import React, { Component } from "react";
import Nav from "./Nav";
import Menu from "./Menu";

class Layout extends Component {
  render() {
    return (
      <>
        <Nav />
        <div className="container-fluid">
          <div className="row">
            <Menu />
            <main className="col-md-9 ms-sm-auto col-lg-10 px-md-4">
              {(this.props as { children: React.ReactNode }).children}
            </main>
          </div>
        </div>
      </>
    );
  }
}

export default Layout;

```

### my_projects/07_react_django_practical/react-admin/src/components/Dashboard.tsx:

```tsx
import React from "react";
import Layout from "./Layout";

const Dashboard = () => (
  <Layout>
    <h2>Section title</h2>
    <div className="table-responsive small">
      <table className="table table-striped table-sm">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Header</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1,001</td>
            <td>random</td>
            <td>data</td>
            <td>placeholder</td>
            <td>text</td>
          </tr>
          <tr>
            <td>1,015</td>
            <td>random</td>
            <td>tabular</td>
            <td>information</td>
            <td>text</td>
          </tr>
        </tbody>
      </table>
    </div>

    {/* Chart  */}
    <div className="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
      <h1 className="h2">Dashboard</h1>
      <div className="btn-toolbar mb-2 mb-md-0">
        <div className="btn-group me-2">
          <button type="button" className="btn btn-sm btn-outline-secondary">
            Share
          </button>
          <button type="button" className="btn btn-sm btn-outline-secondary">
            Export
          </button>
        </div>
        <button
          type="button"
          className="btn btn-sm btn-outline-secondary dropdown-toggle d-flex align-items-center gap-1"
        >
          <svg className="bi">
            <use xlinkHref="#calendar3" />
          </svg>
          This week
        </button>
      </div>
    </div>

    <canvas
      className="my-4 w-100"
      id="myChart"
      width="900"
      height="380"
    ></canvas>
  </Layout>
);

export default Dashboard;

```

### my_projects/07_react_django_practical/react-admin/src/components/secure/Users.tsx:

```tsx
import React from "react";
import Layout from "../Layout";

const Users = () => {
  return (
    <Layout>
      <h1>Users List</h1>
    </Layout>
  );
};

export default Users;

```

### my_projects/07_react_django_practical/react-admin/src/components/public/Login.tsx:

```tsx
import React, { Component } from "react";
import "./Login.css";

class Login extends Component {
  render() {
    return (
      <>
        <section className="container my-5 form-signin w-100 m-auto">
          <form>
            <h1 className="h3 mb-3 fw-normal">Please sign in</h1>

            <div className="form-floating">
              <input
                type="email"
                className="form-control"
                id="floatingInput"
                placeholder="name@example.com"
              />
              <label htmlFor="floatingInput">Email address</label>
            </div>
            <div className="form-floating">
              <input
                type="password"
                className="form-control"
                id="floatingPassword"
                placeholder="Password"
              />
              <label htmlFor="floatingPassword">Password</label>
            </div>

            <button className="btn btn-primary w-100 py-2" type="submit">
              Sign in
            </button>
          </form>
        </section>
      </>
    );
  }
}

export default Login;

```

### my_projects/07_react_django_practical/react-admin/src/components/public/Login.css:

```css
.form-signin {
    max-width: 330px;
    padding: 1rem;
}

.form-signin .form-floating:focus-within {
    z-index: 2;
}

.form-signin input[type="email"] {
    margin-bottom: -1px;
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0;
}

.form-signin input[type="password"] {
    margin-bottom: 10px;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
}
```

[Bootstrap Login Form - https://getbootstrap.com/docs/5.3/examples/](https://getbootstrap.com/docs/5.3/examples/)

![image](https://github.com/user-attachments/assets/2c126804-0760-46e5-8e92-50bd8a057423)
![image](https://github.com/user-attachments/assets/ed9d1459-3acd-44d1-b0ac-a656ea2a1b9a)
![image](https://github.com/user-attachments/assets/a1132ad2-2012-40af-892c-6ded72ff6a4e)

```x
GET: http://localhost:3000/login
```

![image](https://github.com/user-attachments/assets/6b35023a-2aa0-4646-a52e-6114a550207f)

```x
GET: http://localhost:3000/users
```

![image](https://github.com/user-attachments/assets/f97d51f5-1fb9-4b35-823c-dfa8442a5dcb)

```x
GET: http://localhost:3000/
```

![image](https://github.com/user-attachments/assets/eb0346ec-501f-482c-b090-bfaadd675d28)

<img width="1440" alt="image" src="https://github.com/user-attachments/assets/aceb5b2d-0f90-4f52-8a5f-2266700265c0">
<img width="1440" alt="image" src="https://github.com/user-attachments/assets/6e9a496f-919a-496d-81e3-b4771be7588e">
<img width="1440" alt="image" src="https://github.com/user-attachments/assets/4c6f073b-336e-4699-91fb-595b55225078">
<img width="1440" alt="image" src="https://github.com/user-attachments/assets/5b0beec1-fdfa-465f-bcc7-9c942b8f36af">

# #END</details>

<details>
<summary>39. Frontend - Setup Register Form </summary>

# Frontend - Setup Register Form

### my_projects/07_react_django_practical/react-admin/src/App.tsx:

```tsx
import "./App.css";
import Dashboard from "./components/Dashboard";
import Users from "./components/secure/Users";
import Login from "./components/public/Login";
import Register from "./components/public/Register";

import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" index element={<Dashboard />} />
          <Route path="/users" element={<Users />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

```

### my_projects/07_react_django_practical/react-admin/src/components/public/Register.tsx:

```tsx
import React, { useState, useEffect } from "react";
import "./Register.css";

const Register = () => {
  const INITIAL_STATE = {
    first_name: "",
    last_name: "",
    email: "",
    password: "",
    password_confirm: "",
  };
  const [registerUser, setRegisterUser] = useState(INITIAL_STATE);

  const handleChange = (e: any) => {
    e.preventDefault();
    const { name, value } = e.target;
    setRegisterUser((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e: any) => {
    e.preventDefault();
    if (Object.values(registerUser).some((value) => !value)) {
      alert("Please fill in all fields...");
      return;
    }
    if (registerUser.password !== registerUser.password_confirm) {
      alert("Passwords do not match...");
      return;
    }
    console.log("Form submitted: " + JSON.stringify(registerUser));
    // setRegisterUser(INITIAL_STATE);
  };

  useEffect(() => {
    // console.log("User: " + JSON.stringify(registerUser));
    console.log("Change made...");
  }, [registerUser]);

  return (
    <>
      <section className="container my-5 form-signin w-100 m-auto">
        <form onSubmit={handleSubmit}>
          <h1 className="h3 mb-3 fw-normal">Please register</h1>

          <div className="form-floating">
            <input
              type="text"
              className="form-control"
              id="first_name"
              name="first_name"
              placeholder="bob"
              onChange={(e) => handleChange(e)}
            />
            <label htmlFor="first_name">First Name</label>
          </div>
          <div className="form-floating">
            <input
              type="text"
              className="form-control"
              id="last_name"
              name="last_name"
              placeholder="Smith..."
              onChange={(e) => handleChange(e)}
            />
            <label htmlFor="last_name">Last Name</label>
          </div>
          <div className="form-floating">
            <input
              type="email"
              className="form-control"
              id="email"
              name="email"
              placeholder="bobsmith@gmail.com..."
              onChange={(e) => handleChange(e)}
            />
            <label htmlFor="first_name">Email Address</label>
          </div>
          <div className="form-floating">
            <input
              type="password"
              className="form-control"
              id="password"
              name="password"
              placeholder="***************"
              onChange={(e) => handleChange(e)}
            />
            <label htmlFor="floatingPassword">Password</label>
          </div>
          <div className="form-floating">
            <input
              type="password"
              className="form-control"
              id="password_confirm"
              name="password_confirm"
              placeholder="***************"
              onChange={(e) => handleChange(e)}
            />
            <label htmlFor="floatingPassword">Confirm Password</label>
          </div>

          <button className="btn btn-primary w-100 py-2" type="submit">
            Sign up
          </button>
        </form>
      </section>
    </>
  );
};

export default Register;

```

### my_projects/07_react_django_practical/react-admin/src/components/public/Register.css:

```css
.form-signin {
    max-width: 330px;
    padding: 1rem;
}

.form-signin .form-floating:focus-within {
    z-index: 2;
}

.form-signin input[type="email"] {
    margin-bottom: 10px;
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0;
}

.form-signin input[type="password"] {
    margin-bottom: 10px;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
}
```

![image](https://github.com/user-attachments/assets/26f50101-8e50-40e2-bc92-4b95f294ef7c)

<img width="1440" alt="image" src="https://github.com/user-attachments/assets/a3556be6-2715-478a-b8ea-9c21bf7b6565">
<img width="1440" alt="image" src="https://github.com/user-attachments/assets/b5ac8667-c57b-4be5-8c76-b6c569c5c8b7">
<img width="1440" alt="image" src="https://github.com/user-attachments/assets/7a2c2c74-0e7a-466f-922b-8971d0bac6b5">

# #END</details>

<details>
<summary>40. Frontend - Setup register backend to accept data with default role=3 (Viewer) </summary>

# Frontend - Setup register backend to accept data with default role=3 (Viewer)

### my_projects/07_react_django_practical/users_app/models.py:

```py
from django.contrib.auth.models import AbstractUser
from django.db import models


class Permission(models.Model):
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Permissions'
        verbose_name = 'Permission'

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=200, null=True, blank=True)
    permissions = models.ManyToManyField(Permission)

    class Meta:
        verbose_name_plural = 'Roles'
        verbose_name = 'Role'

    def __str__(self):
        return self.name


class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    role = models.ForeignKey(
        Role, on_delete=models.SET_NULL, null=True, blank=True, default=3)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name_plural = 'Users'
        verbose_name = 'User'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

```

### my_projects/07_react_django_practical/users_app/urls.py:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('users/info', views.ProfileInfoAPIView.as_view(),
         name='users-profile-info'),
    path('users/password', views.ProfilePasswordAPIView.as_view(),
         name='users-profile-password'),
    path('users', views.UserGenericAPIView.as_view(), name='users'),
    path('users/<str:pk>', views.UserGenericAPIView.as_view(), name='users-detail'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('auth', views.AuthUser.as_view(), name='auth'),
    path('logout', views.logout, name='logout'),
    path('permissions', views.PermissionAPIView.as_view(), name='permissions'),
    path('roles', views.RoleViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='roles'),
    path('roles/<int:pk>', views.RoleViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='roles-detail'),

]

```

### my_projects/07_react_django_practical/users_app/views.py:

```py
from rest_framework import exceptions, viewsets, status, generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import PermissionSerializer, UserSerializer, RoleSerializer
from .models import User, Permission, Role
from .auth import generate_access_token, JWTAuth
from .pagination import CustomPagination
from .permissions import ViewPermissions


class ProfileInfoAPIView(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk=None):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ProfilePasswordAPIView(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk=None):
        user = request.user
        data = request.data

        if data['password'] != data['password_confirm']:
            raise exceptions.ValidationError('Passwords do not match')

        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

        # user.set_password(data['password'])
        # user.save()
        # return Response({'message': 'Password updated successfully!'})


class UserGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated & ViewPermissions]
    permission_object = 'users'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({"data": self.retrieve(request, pk).data})
        return Response({"data": self.list(request).data})

    def post(self, request):
        request.data.update({
            "password": 1234,
            "password_confirm": 1234,
            "role": request.data["role_id"]
        })
        return Response({"data": self.create(request).data})

    def put(self, request, pk=None):
        if (request.data['role_id']):
            request.data.update({
                "role": request.data["role_id"]
            })
        # return Response({"data": self.update(request, pk).data})
        return Response({"data": self.partial_update(request, pk).data})

    def delete(self, request, pk=None):
        return self.destroy(request, pk)


class AuthUser(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        data = serializer.data
        data["permissions"] = [
            permission['name'] for permission in data['role']['permissions']]
        return Response({'data': data})


class PermissionAPIView(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = PermissionSerializer(Permission.objects.all(), many=True)
        return Response({'data': serializer.data})


class RoleViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated & ViewPermissions]
    permission_object = 'roles'

    def list(self, request):
        queryset = Role.objects.all()
        serializer = RoleSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def create(self, request):
        serializer = RoleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(role)
        return Response({"data": serializer.data})

    def update(self, request, pk=None):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(instance=role, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        role = Role.objects.get(id=pk)
        role.delete()
        return Response({'message': 'Role deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def register(request):
    data = request.data
    if data['password'] != data['password_confirm']:
        raise exceptions.ValidationError('Passwords do not match')

    if User.objects.filter(email=data['email']).exists():
        raise exceptions.ValidationError('Email already exists')

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = User.objects.filter(email=email).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found')
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('Incorrect password')

    token = generate_access_token(user)
    # set token to http-only cookie
    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }
    return response


@api_view(['POST'])
def logout(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        'message': 'success'
    }
    return response

```

### my_projects/07_react_django_practical/users_app/serializers.py:

```py
from rest_framework import serializers
from .models import User, Permission, Role


class RoleRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return RoleSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)


class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    role = RoleRelatedField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name',
                  'email', 'password', 'password_confirm', 'role']  # '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError("Passwords do not match")

        # Set default role
        validated_data['role'] = Role.objects.get(pk=3)

        # user = User.objects.create(**validated_data)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)  # Need to hash Password
        instance.save()
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        password_confirm = validated_data.pop('password_confirm', None)

        if password and password_confirm and password != password_confirm:
            raise serializers.ValidationError("Passwords do not match")

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class PermissionRelatedField(serializers.StringRelatedField):
    def to_representation(self, value):
        return PermissionSerializer(value).data

    def to_internal_value(self, data):
        return data


class RoleSerializer(serializers.ModelSerializer):
    # permissions = PermissionSerializer(many=True)
    permissions = PermissionRelatedField(many=True)

    class Meta:
        model = Role
        fields = "__all__"

    def create(self, validated_data):
        permissions = validated_data.pop('permissions', None)

        if permissions == None:
            raise serializers.ValidationError(
                "You must set Permissions for the Role.")

        instance = self.Meta.model(**validated_data)
        instance.save()
        instance.permissions.add(*permissions)
        instance.save()
        return instance

```

```x
POST: http://localhost:8000/api/v1/register
```

<img width="1404" alt="image" src="https://github.com/user-attachments/assets/c324af41-6928-490f-80f9-53a676d4fd5d">
<img width="1404" alt="image" src="https://github.com/user-attachments/assets/88aff654-b56a-4b4b-93ed-45ec1772f5f2">

![image](https://github.com/user-attachments/assets/d270b227-c04c-4f99-8ac4-f61f7a01eba9)
![image](https://github.com/user-attachments/assets/8c346701-f931-44b9-8a33-ad776cf2a6a4)

<img width="1439" alt="image" src="https://github.com/user-attachments/assets/038cdc10-dab8-4972-acaf-8b941c40aaad">
<img width="1439" alt="image" src="https://github.com/user-attachments/assets/cbc2a0c3-9694-46ae-be13-a3e619fc9ffb">

# #END</details>

<details>
<summary>41. Frontend - Send Data to Server with Async Calls on Axios </summary>

# Frontend - Send Data to Server with Async Calls on Axios

## Install Axios

```x
npm install axios
```

### my_projects/07_react_django_practical/react-admin/package.json:

```json
{
  "name": "react-admin",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@testing-library/jest-dom": "^5.17.0",
    "@testing-library/react": "^13.4.0",
    "@testing-library/user-event": "^13.5.0",
    "@types/jest": "^27.5.2",
    "@types/node": "^16.18.104",
    "@types/react": "^18.3.3",
    "@types/react-dom": "^18.3.0",
    "@types/react-router-dom": "^5.3.3",
    "axios": "^1.7.3",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-router-dom": "^6.26.0",
    "react-scripts": "5.0.1",
    "typescript": "^4.9.5",
    "web-vitals": "^2.1.4"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}

```

### my_projects/07_react_django_practical/react-admin/src/App.tsx:

```tsx
import "./App.css";
import Dashboard from "./components/Dashboard";
import Users from "./components/secure/Users";
import Login from "./components/public/Login";
import Register from "./components/public/Register";

import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" index element={<Dashboard />} />
          <Route path="/users" element={<Users />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

```

### my_projects/07_react_django_practical/react-admin/src/components/public/Register.tsx:

```tsx
import React, { useState, useEffect } from "react";
import axios from "axios";
import "./Register.css";

const Register = () => {
  const INITIAL_STATE = {
    first_name: "",
    last_name: "",
    email: "",
    password: "",
    password_confirm: "",
  };
  const [registerUser, setRegisterUser] = useState(INITIAL_STATE);

  const handleChange = (e: any) => {
    e.preventDefault();
    const { name, value } = e.target;
    setRegisterUser((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    if (Object.values(registerUser).some((value) => !value)) {
      alert("Please fill in all fields...");
      return;
    }
    if (registerUser.password !== registerUser.password_confirm) {
      alert("Passwords do not match...");
      return;
    }

    // axios
    //   .post("http://localhost:8000/api/v1/register/", registerUser)
    //   .then((response) => {
    //     console.log("Response: " + JSON.stringify(response.data));
    //   })
    //   .catch((error) => {
    //     console.error("Error: " + error);
    //   });

    try {
      const response = await axios.post(
        "http://localhost:8000/api/v1/register",
        registerUser
      );
      console.log("Response: " + JSON.stringify(response.data));
      // setRegisterUser(INITIAL_STATE);
    } catch (err) {
      console.error("Error: " + err);
    }
  };

  useEffect(() => {
    // console.log("User: " + JSON.stringify(registerUser));
    console.log("Change made...");
  }, [registerUser]);

  return (
    <>
      <section className="container my-5 form-signin w-100 m-auto">
        <form onSubmit={handleSubmit}>
          <h1 className="h3 mb-3 fw-normal">Please register</h1>

          <div className="form-floating">
            <input
              type="text"
              className="form-control"
              id="first_name"
              name="first_name"
              placeholder="bob"
              onChange={(e) => handleChange(e)}
            />
            <label htmlFor="first_name">First Name</label>
          </div>
          <div className="form-floating">
            <input
              type="text"
              className="form-control"
              id="last_name"
              name="last_name"
              placeholder="Smith..."
              onChange={(e) => handleChange(e)}
            />
            <label htmlFor="last_name">Last Name</label>
          </div>
          <div className="form-floating">
            <input
              type="email"
              className="form-control"
              id="email"
              name="email"
              placeholder="bobsmith@gmail.com..."
              onChange={(e) => handleChange(e)}
            />
            <label htmlFor="first_name">Email Address</label>
          </div>
          <div className="form-floating">
            <input
              type="password"
              className="form-control"
              id="password"
              name="password"
              placeholder="***************"
              onChange={(e) => handleChange(e)}
            />
            <label htmlFor="floatingPassword">Password</label>
          </div>
          <div className="form-floating">
            <input
              type="password"
              className="form-control"
              id="password_confirm"
              name="password_confirm"
              placeholder="***************"
              onChange={(e) => handleChange(e)}
            />
            <label htmlFor="floatingPassword">Confirm Password</label>
          </div>

          <button className="btn btn-primary w-100 py-2" type="submit">
            Sign up
          </button>
        </form>
      </section>
    </>
  );
};

export default Register;

```

```x
(WEB) POST: http://localhost:3000/register
```

![image](https://github.com/user-attachments/assets/71941670-ed64-4bb6-9601-6a660c124ca9)
![image](https://github.com/user-attachments/assets/ede523fc-04bb-47ac-9a78-eb45d424df20)
![image](https://github.com/user-attachments/assets/bdc49274-8419-4fa5-8d2d-edb099a9fd10)

<img width="1439" alt="image" src="https://github.com/user-attachments/assets/80361039-a416-43a6-9eae-176adc1272b8">
<img width="1395" alt="image" src="https://github.com/user-attachments/assets/1dad8cee-5038-469a-ac3b-a1f4b544e060">

# #END</details>

<details>
<summary>42. Frontend - Redirect User after registration </summary>

# Frontend - Redirect User after registration

### my_projects/07_react_django_practical/react-admin/src/App.tsx:

```tsx
import "./App.css";
import Dashboard from "./components/Dashboard";
import Users from "./components/secure/Users";
import Login from "./components/public/Login";
import Register from "./components/public/Register";

import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" index element={<Dashboard />} />
          <Route path="/users" element={<Users />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

```

### my_projects/07_react_django_practical/react-admin/src/components/public/Register.tsx:

```tsx
import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import "./Register.css";

const Register = () => {
  const INITIAL_STATE = {
    first_name: "",
    last_name: "",
    email: "",
    password: "",
    password_confirm: "",
  };
  const [registerUser, setRegisterUser] = useState(INITIAL_STATE);

  const navigate = useNavigate();

  const handleChange = (e: any) => {
    e.preventDefault();
    const { name, value } = e.target;
    setRegisterUser((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    if (Object.values(registerUser).some((value) => !value)) {
      alert("Please fill in all fields...");
      return;
    }
    if (registerUser.password !== registerUser.password_confirm) {
      alert("Passwords do not match...");
      return;
    }

    // axios
    //   .post("http://localhost:8000/api/v1/register/", registerUser)
    //   .then((response) => {
    //     console.log("Response: " + JSON.stringify(response.data));
    //   })
    //   .catch((error) => {
    //     console.error("Error: " + error);
    //   });

    try {
      const response = await axios.post(
        "http://localhost:8000/api/v1/register",
        registerUser
      );
      console.log("Response: " + JSON.stringify(response.data));
      // setRegisterUser(INITIAL_STATE);
      return navigate("/login");
    } catch (err) {
      console.error("Error: " + err);
    }
  };

  useEffect(() => {
    // console.log("User: " + JSON.stringify(registerUser));
    console.log("Change made...");
  }, [registerUser]);

  return (
    <>
      <section className="container my-5 form-signin w-100 m-auto">
        <form onSubmit={handleSubmit}>
          <h1 className="h3 mb-3 fw-normal">Please register</h1>

          <div className="form-floating">
            <input
              type="text"
              className="form-control"
              id="first_name"
              name="first_name"
              placeholder="bob"
              onChange={(e) => handleChange(e)}
            />
            <label htmlFor="first_name">First Name</label>
          </div>
          <div className="form-floating">
            <input
              type="text"
              className="form-control"
              id="last_name"
              name="last_name"
              placeholder="Smith..."
              onChange={(e) => handleChange(e)}
            />
            <label htmlFor="last_name">Last Name</label>
          </div>
          <div className="form-floating">
            <input
              type="email"
              className="form-control"
              id="email"
              name="email"
              placeholder="bobsmith@gmail.com..."
              onChange={(e) => handleChange(e)}
            />
            <label htmlFor="first_name">Email Address</label>
          </div>
          <div className="form-floating">
            <input
              type="password"
              className="form-control"
              id="password"
              name="password"
              placeholder="***************"
              onChange={(e) => handleChange(e)}
            />
            <label htmlFor="floatingPassword">Password</label>
          </div>
          <div className="form-floating">
            <input
              type="password"
              className="form-control"
              id="password_confirm"
              name="password_confirm"
              placeholder="***************"
              onChange={(e) => handleChange(e)}
            />
            <label htmlFor="floatingPassword">Confirm Password</label>
          </div>

          <button className="btn btn-primary w-100 py-2" type="submit">
            Sign up
          </button>
        </form>
      </section>
    </>
  );
};

export default Register;

```

![image](https://github.com/user-attachments/assets/4a7b0a0c-f99d-40e4-8178-3ea72d325937)
![image](https://github.com/user-attachments/assets/b950e58c-bc5d-4677-bcb2-94ff6953be27)
![image](https://github.com/user-attachments/assets/4e39aa30-7755-4823-ad8d-182a96be52da)
![image](https://github.com/user-attachments/assets/275459c9-1a30-43c6-acf8-da602b147108)

<img width="1439" alt="image" src="https://github.com/user-attachments/assets/53b5cbf8-9a67-46c9-8f3a-efb6f9a24629">
<img width="1439" alt="image" src="https://github.com/user-attachments/assets/d4490fe9-9344-4f9f-aa24-1b71a412c8fd">

# #END</details>

<details>
<summary>43. Frontend - Setup Login Functionality </summary>

# Frontend - Setup Login Functionality

### my_projects/07_react_django_practical/react-admin/src/index.tsx:

```tsx
import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import axios from "axios";

axios.defaults.baseURL = "http://localhost:8000/api/v1/";
axios.defaults.withCredentials = true;

const root = ReactDOM.createRoot(
  document.getElementById("root") as HTMLElement
);
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

### my_projects/07_react_django_practical/react-admin/src/App.tsx:

```tsx
import "./App.css";
import Dashboard from "./components/Dashboard";
import Users from "./components/secure/Users";
import Login from "./components/public/Login";
import Register from "./components/public/Register";

import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" index element={<Dashboard />} />
          <Route path="/users" element={<Users />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

```

### my_projects/07_react_django_practical/react-admin/src/components/public/Login.tsx:

```tsx
import React, { Component } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import "./Login.css";

function withNavigation(Component: any) {
  return function WrappedComponent(props: any) {
    const navigate = useNavigate();
    return <Component {...props} navigate={navigate} />;
  };
}

class Login extends Component {
  INITIAL_STATE = {
    email: "",
    password: "",
  };

  constructor(props: any) {
    super(props);
    // Initialize state
    this.state = {
      email: "",
      password: "",
    };

    // Bind the event handler
    this.handleInputChange = this.handleInputChange.bind(this);
    this.handleButtonClick = this.handleButtonClick.bind(this);
  }

  // Event handler for input change
  handleInputChange(e: any) {
    this.setState({ [e.target.name]: e.target.value });
  }

  // Event handler for button click
  async handleButtonClick(e: any) {
    e.preventDefault();
    if (Object.values(this.state).some((value) => !value)) {
      alert("Please fill in all fields...");
      return;
    }

    try {
      const response = await axios.post("login", this.state);
      console.log("Response: " + JSON.stringify(response.data));
      // this.setState(this.INITIAL_STATE);
      (this.props as { navigate: (path: string) => void }).navigate("/");
    } catch (err) {
      console.error("Error: " + err);
    }
  }

  componentDidUpdate(
    prevProps: any,
    prevState: { email: string; password: string }
  ) {
    // Check if the email or password has changed
    if (
      prevState.email !==
        (this.state as { email: string; password: string }).email ||
      prevState.password !==
        (this.state as { email: string; password: string }).password
    ) {
      console.log(
        `Email: ${
          (this.state as { email: string; password: string }).email
        }, Password: ${
          (this.state as { email: string; password: string }).password
        }`
      );
    }
  }

  render() {
    return (
      <>
        <section className="container my-5 form-signin w-100 m-auto">
          <form onSubmit={(e) => this.handleButtonClick(e)}>
            <h1 className="h3 mb-3 fw-normal">Please sign in</h1>

            <div className="form-floating">
              <input
                type="email"
                className="form-control"
                id="email"
                name="email"
                placeholder="name@example.com..."
                onChange={(e) => this.handleInputChange(e)}
              />
              <label htmlFor="email">Email address</label>
            </div>
            <div className="form-floating">
              <input
                type="password"
                className="form-control"
                id="password"
                name="password"
                placeholder="**************"
                onChange={(e) => this.handleInputChange(e)}
              />
              <label htmlFor="password">Password</label>
            </div>

            <button className="btn btn-primary w-100 py-2" type="submit">
              Sign in
            </button>
          </form>
        </section>
      </>
    );
  }
}

export default withNavigation(Login);

```

```x
(WEB) POST: http://localhost:3000/login
```

![image](https://github.com/user-attachments/assets/3e43c96c-cebc-4b39-82fd-2772f4120613)
![image](https://github.com/user-attachments/assets/7e2abd0d-64f8-48bc-b44c-01ba29ae0df1)
![image](https://github.com/user-attachments/assets/11f0451a-8f69-44d6-8e9f-4f168cb94101)
![image](https://github.com/user-attachments/assets/2ad479f0-3097-4c68-9a73-de73f5c09089)

<img width="1439" alt="image" src="https://github.com/user-attachments/assets/15608f43-dfe4-450f-9168-01c61c3d259e">
<img width="1439" alt="image" src="https://github.com/user-attachments/assets/77681e85-2bce-4e2f-aec2-b14a6d78fb30">
<img width="1439" alt="image" src="https://github.com/user-attachments/assets/eaf8fba4-77f5-43f7-a9d8-d5c8f494cf3c">

# #END</details>

<details>
<summary>44. Frontend - GET all Users details in Layout after Login </summary>

# Frontend - GET all Users details in Layout after Login

## Update Backend Permissions file to include users_apps

### my_projects/07_react_django_practical/users_app/permissions.py:

```py
from rest_framework import permissions
from users_app.serializers import UserSerializer


class ViewPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        # if request.method == 'GET':
        #     return True
        # return False

        data = UserSerializer(request.user).data
        if view.permission_object == 'users':
            view.permission_object = 'users_apps'

        # print(data)
        # print(view.permission_object)

        view_access = any(
            p['name'] == 'view_' + view.permission_object for p in data['role']['permissions'])
        edit_access = any(
            p['name'] == 'edit_' + view.permission_object for p in data['role']['permissions'])

        if request.method == 'GET':
            return view_access or edit_access
        return edit_access

```

### my_projects/07_react_django_practical/react-admin/src/index.tsx:

```tsx
import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import axios from "axios";

axios.defaults.baseURL = "http://localhost:8000/api/v1/";
axios.defaults.withCredentials = true;

const root = ReactDOM.createRoot(
  document.getElementById("root") as HTMLElement
);
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

### my_projects/07_react_django_practical/react-admin/src/App.tsx:

```tsx
import "./App.css";
import Dashboard from "./components/Dashboard";
import Users from "./components/secure/Users";
import Login from "./components/public/Login";
import Register from "./components/public/Register";

import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" index element={<Dashboard />} />
          <Route path="/users" element={<Users />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

```

### my_projects/07_react_django_practical/react-admin/src/components/Layout.tsx:

```tsx
import React, { Component } from "react";
import Nav from "./Nav";
import Menu from "./Menu";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function withNavigation(Component: any) {
  return function WrappedComponent(props: any) {
    const navigate = useNavigate();
    return <Component {...props} navigate={navigate} />;
  };
}

class Layout extends Component {
  constructor(props: any) {
    super(props);
    this.state = {
      user: null,
    };
  }

  componentDidMount = async () => {
    try {
      const response = await axios.get("users");
      console.log(response);
      console.log("Response: " + JSON.stringify(response.data));
    } catch (e) {
      console.log(`${e}. The Users could not be fetched. Authentication is required.`);
      (this.props as { navigate: (path: string) => void }).navigate("/login");
    }

    // fetch("http://localhost:8000/api/v1/users", {
    //   credentials: "include",
    // })
    //   .then((res) => res.json())
    //   .then((user) => {
    //     this.setState({
    //       user: user.data,
    //     });
    //   });
  };

  render() {
    return (
      <>
        <Nav />
        <div className="container-fluid">
          <div className="row">
            <Menu />
            <main className="col-md-9 ms-sm-auto col-lg-10 px-md-4">
              {(this.props as { children: React.ReactNode }).children}
            </main>
          </div>
        </div>
      </>
    );
  }
}

export default withNavigation(Layout);

```

![image](https://github.com/user-attachments/assets/301eab05-4a39-48b0-91f2-862aee19634f)

<img width="1439" alt="image" src="https://github.com/user-attachments/assets/afe215a6-a2fb-4a99-a57f-0753ce1a7c34">
<img width="1439" alt="image" src="https://github.com/user-attachments/assets/67fe19a9-ed59-4798-9407-24013a0176aa">
<img width="1439" alt="image" src="https://github.com/user-attachments/assets/5d2f2025-7d34-49bd-83b5-f33a9b11cc58">
<img width="1439" alt="image" src="https://github.com/user-attachments/assets/84f69cd4-f22b-4873-8338-624e67bbb9b0">

# #END</details>

<details>
<summary>45. Frontend - Setup Logout Functionality </summary>

# Frontend - Setup Logout Functionality 

### my_projects/07_react_django_practical/react-admin/src/index.tsx:

```tsx
import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import axios from "axios";

axios.defaults.baseURL = "http://localhost:8000/api/v1/";
axios.defaults.withCredentials = true;

const root = ReactDOM.createRoot(
  document.getElementById("root") as HTMLElement
);
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

### my_projects/07_react_django_practical/react-admin/src/App.tsx:

```tsx
import "./App.css";
import Dashboard from "./components/Dashboard";
import Users from "./components/secure/Users";
import Login from "./components/public/Login";
import Register from "./components/public/Register";

import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" index element={<Dashboard />} />
          <Route path="/users" element={<Users />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

```

### my_projects/07_react_django_practical/react-admin/src/components/Layout.tsx:

```tsx
import React, { Component } from "react";
import Nav from "./Nav";
import Menu from "./Menu";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function withNavigation(Component: any) {
  return function WrappedComponent(props: any) {
    const navigate = useNavigate();
    return <Component {...props} navigate={navigate} />;
  };
}

class Layout extends Component {
  constructor(props: any) {
    super(props);
    this.state = {
      user: null,
    };
  }

  componentDidMount = async () => {
    try {
      const response = await axios.get("users");
      // console.log(response);
      console.log("Response: " + JSON.stringify(response.data));
    } catch (e) {
      console.log(
        `${e}. The Users could not be fetched. Authentication is required.`
      );
      (this.props as { navigate: (path: string) => void }).navigate("/login");
    }

    // fetch("http://localhost:8000/api/v1/users", {
    //   credentials: "include",
    // })
    //   .then((res) => res.json())
    //   .then((user) => {
    //     this.setState({
    //       user: user.data,
    //     });
    //   });
  };

  render() {
    return (
      <>
        <Nav />
        <div className="container-fluid">
          <div className="row">
            <Menu />
            <main className="col-md-9 ms-sm-auto col-lg-10 px-md-4">
              {(this.props as { children: React.ReactNode }).children}
            </main>
          </div>
        </div>
      </>
    );
  }
}

export default withNavigation(Layout);

```

### my_projects/07_react_django_practical/react-admin/src/components/Nav.tsx:

```tsx
import React, { Component } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function withNavigation(Component: any) {
  return function WrappedComponent(props: any) {
    const navigate = useNavigate();
    return <Component {...props} navigate={navigate} />;
  };
}

class Nav extends Component {
  handleLogout = async (e: React.MouseEvent) => {
    e.preventDefault();
    try {
      const response = await axios.post("logout", {});
      console.log("User is logged out.");
      console.log(response);
      (this.props as { navigate: (path: string) => void }).navigate("/login");
    } catch (e) {
      console.log(e);
    }
  };
  render() {
    return (
      <nav>
        {/* SVG SYMBOLS */}
        <svg xmlns="http://www.w3.org/2000/svg" className="d-none">
          <symbol id="cart" viewBox="0 0 16 16">
            <path d="M0 1.5A.5.5 0 0 1 .5 1H2a.5.5 0 0 1 .485.379L2.89 3H14.5a.5.5 0 0 1 .49.598l-1 5a.5.5 0 0 1-.465.401l-9.397.472L4.415 11H13a.5.5 0 0 1 0 1H4a.5.5 0 0 1-.491-.408L2.01 3.607 1.61 2H.5a.5.5 0 0 1-.5-.5zM3.102 4l.84 4.479 9.144-.459L13.89 4H3.102zM5 12a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm7 0a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm-7 1a1 1 0 1 1 0 2 1 1 0 0 1 0-2zm7 0a1 1 0 1 1 0 2 1 1 0 0 1 0-2z" />
          </symbol>
          <symbol id="door-closed" viewBox="0 0 16 16">
            <path d="M3 2a1 1 0 0 1 1-1h8a1 1 0 0 1 1 1v13h1.5a.5.5 0 0 1 0 1h-13a.5.5 0 0 1 0-1H3V2zm1 13h8V2H4v13z" />
            <path d="M9 9a1 1 0 1 0 2 0 1 1 0 0 0-2 0z" />
          </symbol>
          <symbol id="file-earmark" viewBox="0 0 16 16">
            <path d="M14 4.5V14a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h5.5L14 4.5zm-3 0A1.5 1.5 0 0 1 9.5 3V1H4a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V4.5h-2z" />
          </symbol>
          <symbol id="file-earmark-text" viewBox="0 0 16 16">
            <path d="M5.5 7a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1h-5zM5 9.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5zm0 2a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 0 1h-2a.5.5 0 0 1-.5-.5z" />
            <path d="M9.5 0H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V4.5L9.5 0zm0 1v2A1.5 1.5 0 0 0 11 4.5h2V14a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h5.5z" />
          </symbol>
          <symbol id="gear-wide-connected" viewBox="0 0 16 16">
            <path d="M7.068.727c.243-.97 1.62-.97 1.864 0l.071.286a.96.96 0 0 0 1.622.434l.205-.211c.695-.719 1.888-.03 1.613.931l-.08.284a.96.96 0 0 0 1.187 1.187l.283-.081c.96-.275 1.65.918.931 1.613l-.211.205a.96.96 0 0 0 .434 1.622l.286.071c.97.243.97 1.62 0 1.864l-.286.071a.96.96 0 0 0-.434 1.622l.211.205c.719.695.03 1.888-.931 1.613l-.284-.08a.96.96 0 0 0-1.187 1.187l.081.283c.275.96-.918 1.65-1.613.931l-.205-.211a.96.96 0 0 0-1.622.434l-.071.286c-.243.97-1.62.97-1.864 0l-.071-.286a.96.96 0 0 0-1.622-.434l-.205.211c-.695.719-1.888.03-1.613-.931l.08-.284a.96.96 0 0 0-1.186-1.187l-.284.081c-.96.275-1.65-.918-.931-1.613l.211-.205a.96.96 0 0 0-.434-1.622l-.286-.071c-.97-.243-.97-1.62 0-1.864l.286-.071a.96.96 0 0 0 .434-1.622l-.211-.205c-.719-.695-.03-1.888.931-1.613l.284.08a.96.96 0 0 0 1.187-1.186l-.081-.284c-.275-.96.918-1.65 1.613-.931l.205.211a.96.96 0 0 0 1.622-.434l.071-.286zM12.973 8.5H8.25l-2.834 3.779A4.998 4.998 0 0 0 12.973 8.5zm0-1a4.998 4.998 0 0 0-7.557-3.779l2.834 3.78h4.723zM5.048 3.967c-.03.021-.058.043-.087.065l.087-.065zm-.431.355A4.984 4.984 0 0 0 3.002 8c0 1.455.622 2.765 1.615 3.678L7.375 8 4.617 4.322zm.344 7.646.087.065-.087-.065z" />
          </symbol>
          <symbol id="graph-up" viewBox="0 0 16 16">
            <path
              fillRule="evenodd"
              d="M0 0h1v15h15v1H0V0Zm14.817 3.113a.5.5 0 0 1 .07.704l-4.5 5.5a.5.5 0 0 1-.74.037L7.06 6.767l-3.656 5.027a.5.5 0 0 1-.808-.588l4-5.5a.5.5 0 0 1 .758-.06l2.609 2.61 4.15-5.073a.5.5 0 0 1 .704-.07Z"
            />
          </symbol>
          <symbol id="house-fill" viewBox="0 0 16 16">
            <path d="M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L8 2.207l6.646 6.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.707 1.5Z" />
            <path d="m8 3.293 6 6V13.5a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 2 13.5V9.293l6-6Z" />
          </symbol>
          <symbol id="list" viewBox="0 0 16 16">
            <path
              fillRule="evenodd"
              d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5z"
            />
          </symbol>
          <symbol id="people" viewBox="0 0 16 16">
            <path d="M15 14s1 0 1-1-1-4-5-4-5 3-5 4 1 1 1 1h8Zm-7.978-1A.261.261 0 0 1 7 12.996c.001-.264.167-1.03.76-1.72C8.312 10.629 9.282 10 11 10c1.717 0 2.687.63 3.24 1.276.593.69.758 1.457.76 1.72l-.008.002a.274.274 0 0 1-.014.002H7.022ZM11 7a2 2 0 1 0 0-4 2 2 0 0 0 0 4Zm3-2a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM6.936 9.28a5.88 5.88 0 0 0-1.23-.247A7.35 7.35 0 0 0 5 9c-4 0-5 3-5 4 0 .667.333 1 1 1h4.216A2.238 2.238 0 0 1 5 13c0-1.01.377-2.042 1.09-2.904.243-.294.526-.569.846-.816ZM4.92 10A5.493 5.493 0 0 0 4 13H1c0-.26.164-1.03.76-1.724.545-.636 1.492-1.256 3.16-1.275ZM1.5 5.5a3 3 0 1 1 6 0 3 3 0 0 1-6 0Zm3-2a2 2 0 1 0 0 4 2 2 0 0 0 0-4Z" />
          </symbol>
          <symbol id="plus-circle" viewBox="0 0 16 16">
            <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z" />
            <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z" />
          </symbol>
          <symbol id="search" viewBox="0 0 16 16">
            <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z" />
          </symbol>
        </svg>

        <header
          className="navbar sticky-top bg-secondary flex-md-nowrap p-0 shadow"
          data-bs-theme="dark"
        >
          <a
            className="navbar-brand col-md-3 col-lg-2 me-0 px-3 fs-6 text-white"
            href="/"
          >
            Company name
          </a>

          <ul className="navbar-nav flex-row d-md-none">
            {/* SEARCH BUTTON */}
            <li className="nav-item text-nowrap">
              <button
                className="nav-link px-3 text-white"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#navbarSearch"
                aria-controls="navbarSearch"
                aria-expanded="false"
                aria-label="Toggle search"
              >
                <svg className="bi">
                  <use xlinkHref="#search" />
                </svg>
              </button>
            </li>
            {/* MENU BUTTON */}
            <li className="nav-item text-nowrap">
              <button
                className="nav-link px-3 text-white"
                type="button"
                data-bs-toggle="offcanvas"
                data-bs-target="#sidebarMenu"
                aria-controls="sidebarMenu"
                aria-expanded="false"
                aria-label="Toggle navigation"
              >
                <svg className="bi">
                  <use xlinkHref="#list" />
                </svg>
              </button>
            </li>
            {/* LOGOUT BUTTON */}
            <li className="nav-item text-nowrap">
              <a href="#" onClick={this.handleLogout}>
                <button
                  className="nav-link px-3 text-white"
                  type="button"
                  data-bs-toggle="offcanvas"
                  data-bs-target="#sidebarMenu"
                  aria-controls="sidebarMenu"
                  aria-expanded="false"
                  aria-label="Toggle navigation"
                >
                  <svg className="bi">
                    <use xlinkHref="#door-closed" />
                  </svg>
                </button>
              </a>
            </li>
          </ul>

          <div id="navbarSearch" className="navbar-search w-100 collapse">
            <input
              className="form-control w-100 rounded-0 border-0"
              type="text"
              placeholder="Search"
              aria-label="Search"
            />
          </div>
        </header>
      </nav>
    );
  }
}

export default withNavigation(Nav);

```

### my_projects/07_react_django_practical/react-admin/src/components/Menu.tsx:

```tsx
import React, { Component } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function withNavigation(Component: any) {
  return function WrappedComponent(props: any) {
    const navigate = useNavigate();
    return <Component {...props} navigate={navigate} />;
  };
}

class Menu extends Component {
  handleLogout = async (e: React.MouseEvent) => {
    e.preventDefault();
    try {
      const response = await axios.post("logout", {});
      console.log("User is logged out.");
      console.log(response);
      (this.props as { navigate: (path: string) => void }).navigate("/login");
    } catch (e) {
      console.log(e);
    }
  };

  render() {
    return (
      <div className="sidebar border border-right col-md-3 col-lg-2 p-0 bg-body-tertiary">
        <div
          className="offcanvas-md offcanvas-end bg-body-tertiary"
          tabIndex={-1}
          id="sidebarMenu"
          aria-labelledby="sidebarMenuLabel"
        >
          <div className="offcanvas-header">
            <h5 className="offcanvas-title" id="sidebarMenuLabel">
              Company name
            </h5>
            <button
              type="button"
              className="btn-close"
              data-bs-dismiss="offcanvas"
              data-bs-target="#sidebarMenu"
              aria-label="Close"
            ></button>
          </div>
          <div className="offcanvas-body d-md-flex flex-column p-0 pt-lg-3 overflow-y-auto">
            <ul className="nav flex-column">
              <li className="nav-item">
                <a
                  className="nav-link d-flex align-items-center gap-2 active"
                  aria-current="page"
                  href="#"
                >
                  <svg className="bi">
                    <use xlinkHref="#house-fill" />
                  </svg>
                  Dashboard
                </a>
              </li>
              <li className="nav-item">
                <a
                  className="nav-link d-flex align-items-center gap-2"
                  href="#"
                >
                  <svg className="bi">
                    <use xlinkHref="#file-earmark" />
                  </svg>
                  Orders
                </a>
              </li>
              <li className="nav-item">
                <a
                  className="nav-link d-flex align-items-center gap-2"
                  href="#"
                >
                  <svg className="bi">
                    <use xlinkHref="#cart" />
                  </svg>
                  Products
                </a>
              </li>
              <li className="nav-item">
                <a
                  className="nav-link d-flex align-items-center gap-2"
                  href="#"
                >
                  <svg className="bi">
                    <use xlinkHref="#people" />
                  </svg>
                  Customers
                </a>
              </li>
              <li className="nav-item">
                <a
                  className="nav-link d-flex align-items-center gap-2"
                  href="#"
                >
                  <svg className="bi">
                    <use xlinkHref="#graph-up" />
                  </svg>
                  Reports
                </a>
              </li>
            </ul>

            <h6 className="sidebar-heading d-flex justify-content-between align-items-center px-3 mt-4 mb-1 text-body-secondary text-uppercase">
              <span>Saved reports</span>
              <a
                className="link-secondary"
                href="#"
                aria-label="Add a new report"
              >
                <svg className="bi">
                  <use xlinkHref="#plus-circle" />
                </svg>
              </a>
            </h6>
            <ul className="nav flex-column mb-auto">
              <li className="nav-item">
                <a
                  className="nav-link d-flex align-items-center gap-2"
                  href="#"
                >
                  <svg className="bi">
                    <use xlinkHref="#file-earmark-text" />
                  </svg>
                  Current month
                </a>
              </li>
            </ul>

            <hr className="my-3" />

            <ul className="nav flex-column mb-auto">
              <li className="nav-item">
                <a
                  className="nav-link d-flex align-items-center gap-2"
                  href="#"
                >
                  <svg className="bi">
                    <use xlinkHref="#gear-wide-connected" />
                  </svg>
                  Settings
                </a>
              </li>
              {/* LOGOUT BUTTON */}
              <li className="nav-item">
                <a
                  className="nav-link d-flex align-items-center gap-2"
                  href="#"
                  onClick={this.handleLogout}
                >
                  <svg className="bi">
                    <use xlinkHref="#door-closed" />
                  </svg>
                  Sign out
                </a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    );
  }
}

export default withNavigation(Menu);

```

![image](https://github.com/user-attachments/assets/74f5a983-c304-4bee-9bd8-bbe909299c0a)
![image](https://github.com/user-attachments/assets/8c7e6ccb-a65b-4264-b1a9-46ff37e7bc09)
![image](https://github.com/user-attachments/assets/c014fdbe-3bdc-41a2-8f2d-66082bfd9c6a)

<img width="1439" alt="image" src="https://github.com/user-attachments/assets/a879da3a-7b4c-4f28-911d-9b44dd8feb88">
<img width="1439" alt="image" src="https://github.com/user-attachments/assets/8e0dc365-c86b-4c35-86c6-4511c7a5e039">
<img width="1439" alt="image" src="https://github.com/user-attachments/assets/9c4e5503-c01a-44b4-b4a6-d083e7f109f2">

# #END</details>

<details>
<summary>46. Frontend - Setup Users Component </summary>

# Frontend - Setup Users Component

```tsx

```

```tsx

```

```tsx

```

```tsx

```

```tsx

```

```tsx

```

```tsx

```

```tsx

```

```tsx

```

```tsx

```

```tsx

```

```tsx

```

```tsx

```

```tsx

```

```tsx

```

```tsx

```

# #END</details>
