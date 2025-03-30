# Youtube-Python Django REST API Framework - DRF

## [COURSE](https://www.youtube.com/watch?v=-LVXBuYzi00) - Django and React Authentication

<details>
  <summary>1. Setup Django and React Apps </summary>

# Setup Django and React Apps  

## Create Folder Backend

```x
mkdir backend
cd backend
```

## Setup Django Environment
```x
pip install virtualenv
virtualenv env
source env/bin/activate

python -m venv env
source env/bin/activate
```

## Install Dependencies - Django, DjangoRestFramework, DjangoCorsHeaders

```x
pip install django djangorestframework django-cors-headers
```

## Create requirements.txt File

```x
pip freeze > requirements.txt
```

```txt
asgiref==3.8.1
Django==5.0.6
django-cors-headers==4.4.0
django-filter==24.2
django-mysql==4.14.0
djangorestframework==3.15.2
Markdown==3.6
mock==5.1.0
mysqlclient==2.2.4
numpy==2.0.0
pandas==2.2.2
pillow==10.4.0
PyJWT==2.8.0
python-dateutil==2.9.0.post0
python-decouple==3.8
pytz==2024.1
six==1.16.0
sqlparse==0.5.0
tzdata==2024.1
```

## Create Django Project - journal_project

```x
django-admin startproject journal_project .
```

## Create Django App - users

```x
django-admin startapp users
python manage.py startapp users
```

## Create React Frontend with Vite

```x
npm create vite@latest frontend -- --template react
cd frontend
npm install
```

## Run Frontenv Server

```x
npm run dev
```

## Run Backend Server

```x
python manage.py runserver
```

## Setup CORS

### dev_projects/03_drf_auth_project/backend/journal_project/settings.py:

```py

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

CORS_ALLOW_ORIGINS = [
    'http://localhost:5173',
    'http://127.0.0.1:5173',
    'http://127.0.0.1:8000',
    'http://localhost:8000',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # External Apps
    'rest_framework',
    'corsheaders',
    # Local Apps
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # CORS Middleware added
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

```

## Initialize git in Parent Directory

```x
cd ..
git init
touch .gitignore
```

## Copy .gitignore file for Django and React

```x
https://www.toptal.com/developers/gitignore/
```

![image](https://github.com/user-attachments/assets/bdf22290-9697-44c2-b5b2-2c43681717c8)
![image](https://github.com/user-attachments/assets/7ffe56b3-4dd0-4513-8c71-91f195c26d24)
![image](https://github.com/user-attachments/assets/c40e9834-fbaf-4cd5-94ba-650479263207)

<img width="1385" alt="image" src="https://github.com/user-attachments/assets/e63a2fd1-bc28-402d-af42-2746e5b0148f">
<img width="1385" alt="image" src="https://github.com/user-attachments/assets/aa712b5b-2a51-451b-8512-448ecb7df0e8">
<img width="1385" alt="image" src="https://github.com/user-attachments/assets/c0d1b40d-4c8d-492a-aafa-57c39af90159">
<img width="1385" alt="image" src="https://github.com/user-attachments/assets/69a68f89-51da-43e6-a221-d1ab59a93f29">

# #END </details>

<details>
  <summary>2. Setup Environment variable Files </summary>

# Setup Environment variable Files

## Install django-environ

```x
cd backend
pip install django-environ
```

## Create .env file

```x
touch .env
touch .env-example
```

### dev_projects/03_drf_auth_project/backend/journal_project/settings.py:

```py

from pathlib import Path

# added for environment variables
import environ
import os
env = environ.Env(DEBUG=(bool, False))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env')) #added

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY') #added

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG') #added

ALLOWED_HOSTS = []

CORS_ALLOW_ORIGINS = [
    'http://localhost:5173',
    'http://127.0.0.1:5173',
    'http://127.0.0.1:8000',
    'http://localhost:8000',
]

```

### dev_projects/03_drf_auth_project/backend/.env:

```x
SECRET_KEY=django-insecure-eq6-nya3g3)eci^)ugik2%3ili=)o2ly^r!_wqq
DEBUG=True
```

### dev_projects/03_drf_auth_project/backend/.env-example:

```x
SECRET_KEY=
DEBUG=
```

<img width="1385" alt="image" src="https://github.com/user-attachments/assets/8a7de207-bba8-4e2c-8b81-be55a74ef504">

# #END </details>

<details>
  <summary>3. Create Custom User Manager and Custom User Model </summary>

# Create Custom User Manager and Custom User Model

### dev_projects/03_drf_auth_project/backend/users/managers.py:

```py
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def email_validator(self, email):
        """
        Validate email
        """
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(
                _('%(email)s is not a valid email address'),
                params={'email': email},
            )

    def create_user(self, first_name, last_name, email, password, **extra_fields):
        """
        Create and save a User with the given first_name, last_name, email and password.
        """
        if not first_name:
            raise ValueError(_("Users must submit a first name"))
        if not last_name:
            raise ValueError(_("Users must submit a last name"))

        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        self.email_validator(email)

        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )

        user.set_password(password)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user.save()
        return user

    def create_superuser(self, first_name, last_name, email, password, **extra_fields):
        """
        Create and save a User with the given first_name, last_name, email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superusers must have is_superuser=True"))

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superusers must have is_staff=True"))

        if not password:
            raise ValueError(_("Superusers must have a password"))

        if not email:
            raise ValueError(_('The Admin Email must be set'))
        email = self.normalize_email(email)
        self.email_validator(email)

        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )

        user.set_password(password)
        user.save()
        return user

```

### dev_projects/03_drf_auth_project/backend/users/models.py:

```py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_("First Name"), max_length=100)
    last_name = models.CharField(_("Last Name"), max_length=100)
    email = models.EmailField(_('Email Address'), max_length=254, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

```

<img width="1385" alt="image" src="https://github.com/user-attachments/assets/313a01f1-452a-4988-818b-8e8f6505acde">
<img width="1385" alt="image" src="https://github.com/user-attachments/assets/283a01d1-347c-4654-80bb-ae89f271fb00">

# #END </details>

<details>
  <summary>4. Create Custom Django Forms </summary>

# Create Custom Django Forms

### dev_projects/03_drf_auth_project/backend/users/forms.py:

```py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ['email', 'first_name', 'last_name']
        error_class = "error"


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = ['email', 'first_name', 'last_name']
        error_class = "error"

```

<img width="1385" alt="image" src="https://github.com/user-attachments/assets/3e9468ea-8183-4907-a9f7-75ad7e7e6438">

# #END </details>

<details>
  <summary>5. Setup Admin Configurations </summary>

# Setup Admin Configurations

### dev_projects/03_drf_auth_project/backend/users/admin.py:

```py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    ordering = ['email']
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ('email', 'first_name', 'last_name',
                    'is_staff', 'is_active')
    list_display_links = ['email']
    list_filter = ('email', 'first_name', 'last_name',
                   'is_staff', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')

    fieldsets = (
        (_('Login Credentials'), {'fields': ('email', 'password',)}),
        (_('Personal information'), {
         'fields': ('first_name', 'last_name',)}),
        (_('Permissions and Groups'), {'fields': (
            'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2',
                       'is_staff', 'is_active'),
        }),
    )


admin.site.register(User, UserAdmin)


```

### dev_projects/03_drf_auth_project/backend/journal_project/settings.py:

```py
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'  # added

```

## Run Migrations

```x
python manage.py makemigrations
python manage.py migrate
```
## Create Super User

```x
python manage.py createsuperuser
```

```x
(env) ➜  backend git:(master) ✗ python manage.py createsuperuser
Email Address: admin@gmail.com
First Name: Ifeanyi
Last Name: Omeata
Password: 
Password (again): 
The password is too similar to the Email Address.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

(env) ➜  backend git:(master) ✗ 
```

### Run Backend Server

```x
python manage.py runserver
```

```x
http://127.0.0.1:8000/admin/
```

![image](https://github.com/user-attachments/assets/278526c7-340c-4c85-8260-c68f0647b6ac)
![image](https://github.com/user-attachments/assets/e3507c85-1672-4c81-8b7a-7941c90b0533)
![image](https://github.com/user-attachments/assets/3b4ec247-33c5-4440-a70e-01f4d58697d4)
![image](https://github.com/user-attachments/assets/1d6e03e1-2f2a-48f2-81e9-387cf7aac96c)
![image](https://github.com/user-attachments/assets/c0869fc0-cf13-4a9f-aa90-8c34dca6400b)
![image](https://github.com/user-attachments/assets/3f3ef430-a4ed-41d5-b73c-c65ac9d16be6)

<img width="1448" alt="image" src="https://github.com/user-attachments/assets/e7665230-8cd4-4415-bcd8-82832da36269">
<img width="1448" alt="image" src="https://github.com/user-attachments/assets/ec1afc65-5eab-406a-8a00-d73fef3c2605">

# #END </details>

<details>
  <summary> 6. Setup Djoser and JWT for Authentication </summary>

# Setup Djoser and JWT for Authentication

## Install dependencies 

```x
pip install djoser djangorestframework_simplejwt pyjwt
```

## Add dependecies to requirements.txt file

```x
pip freeze > requirements.txt
```

### dev_projects/03_drf_auth_project/backend/journal_project/settings.py:

```py
from pathlib import Path

from datetime import timedelta


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # External Apps
    'rest_framework',
    'corsheaders',
    'djoser',  # added
    'rest_framework_simplejwt',  # added
    # Local Apps
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # CORS Middleware added
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


AUTH_USER_MODEL = 'users.User'  # added

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": (
        "Bearer",
        "JWT"),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=120),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=60),
    "SIGNING_KEY": env("SIGNING_KEY"),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}

DJOSER = {
    'LOGIN_FIELD': 'email',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    'SEND_CONFIRMATION_EMAIL': True,
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'SET_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'USERNAME_RESET_CONFIRM_URL': 'username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS': {
        'user_create': 'users.serializers.CreateUserSerializer',
        'user': 'users.serializers.CreateUserSerializer',
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
    },
}

```

### dev_projects/03_drf_auth_project/backend/.env:

```x
SECRET_KEY=django-insecure-eq6-nya3g3)eci^)ugik2%3ili
DEBUG=True
SIGNING_KEY=ZsKeMTDjc3mL3kXdmCJIdj
```

```x
https://djoser.readthedocs.io/en/latest/getting_started.html
```

![image](https://github.com/user-attachments/assets/0247cd8c-6327-4b6a-a872-5d7d55e25281)
![image](https://github.com/user-attachments/assets/4d140e9a-8454-4d5b-819d-57535399a638)
![image](https://github.com/user-attachments/assets/ab8ce11b-aac2-4f80-9edc-d2b734cf1181)
![image](https://github.com/user-attachments/assets/28ea4860-d2a0-45a4-9043-6015ed714f84)
![image](https://github.com/user-attachments/assets/208bcaed-1620-4eba-9cf0-2682ee80cc14)
![image](https://github.com/user-attachments/assets/9c2e418d-645d-4bc1-9823-3c9f1bc7e6c0)
![image](https://github.com/user-attachments/assets/bcf8a341-2d2f-4e91-9891-f97b62680343)

<img width="1404" alt="image" src="https://github.com/user-attachments/assets/f03259ad-370c-4018-aaf2-9d7ef917427c">

# #END </details>

<details>
  <summary> 7. Setup Authentication Serializers and EndPoint Configuration </summary>

# Setup Authentication Serializers and EndPoint Configuration

### dev_projects/03_drf_auth_project/backend/users/serializers.py:

```py
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer

User = get_user_model()


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'password']
        # read_only_fields = ('id',)

```

### dev_projects/03_drf_auth_project/backend/journal_project/urls.py:

```py
"""
URL configuration for journal_project project.

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
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
]

```

<img width="1476" alt="image" src="https://github.com/user-attachments/assets/918c3ee9-6f0d-4591-ba8c-70cec20beca8">
<img width="1476" alt="image" src="https://github.com/user-attachments/assets/0804eae4-532f-4476-b210-21de34998cf3">

# #END </details>

<details>
  <summary> 8. Postman API Testing & Email Configuration </summary>

# Postman API Testing & Email Configuration

```py

```

```py

```

![image](https://github.com/user-attachments/assets/76e7f72c-c774-42da-84f8-4948ef39148e)
![image](https://github.com/user-attachments/assets/1794d444-5735-4123-9014-930a885a0aff)


```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

# #END </details>

# #END 

## [COURSE](https://www.youtube.com/watch?v=FdMf_3SurOA) - Complete Django and React Todo App

<details>
  <summary>1. I </summary>

```x
pip install virtualenv
virtualenv env

python -m venv env
```

```py

```

```py

```

```py

```

```py

```

```py

```

# #END </details>

<details>
  <summary>2. N </summary>

```py

```

```py

```

```py

```  

```py

```

```py

```

# #END </details>

# #END

## [COURSE](https://www.youtube.com/watch?v=-LVXBuYzi00) - Django and Django Rest Framework

<details>
  <summary>1. I </summary>

```x
pip install virtualenv
virtualenv env

python -m venv env
```

```py

```

```py

```

```py

```

```py

```

```py

```

# #END </details>

<details>
  <summary>2. N </summary>

```py

```

```py

```

```py

```  

```py

```

```py

```

# #END </details>

# #END 






