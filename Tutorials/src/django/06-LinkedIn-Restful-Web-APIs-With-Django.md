## +Linkedin - Building Restful Web APIs with Django

## [COURSE](https://www.linkedin.com/learning/building-restful-web-apis-with-django/create-a-rest-api-with-django-and-django-rest-framework)

<details>
<summary>1. Creating a New Django Project: demo_project </summary>

# Creating a New Django Project: demo_project

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

## Install Other Project Dependencies: djangorestframework, django-filter, mock and Pillow

```x
pip install djangorestframework django-filter mock pillow
```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/c4226191-bb1f-42c4-83f0-08b1812d5831)

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/d963db78-6367-40d0-af49-1b90eaac8339)

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/b30e9e58-8cdc-4c3f-8b3f-5d96ef09882d)

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/84446ae5-a1fa-411f-9d09-b3de73ef66f9)

## Get dependencies

```x
pip freeze
```

```x
asgiref==3.8.1
Django==5.0.6
django-filter==24.2
djangorestframework==3.15.2
mock==5.1.0
pillow==10.3.0
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
django-admin startproject demo_project .
```

## Make Migrations

```x
python manage.py makemigrations
python manage.py migrate
```

## Start Local Server

```x
python manage.py runserver
```

```x
(venv) ➜  03_restful_apls_proj git:(main) ✗ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 30, 2024 - 01:32:55
Django version 5.0.6, using settings 'demo_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

<img width="1489" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/24efbb26-8bae-45cc-9887-303d6c606011">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/10b75f10-04cb-4b99-99ff-4f2a423269d7)

# #END</details>

<details>
<summary>2. Create new App - store </summary>

# Create new App - store

## Create App

```py
django-admin startapp store
```

### src-AI-Software/my_projects/03_restful_apls_proj/demo_project/settings.py:

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
    'rest_framework',
    'django_filters',
    'store',
]

```

<img width="1533" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/ba0867bc-93c8-48ea-b9c0-b4798d0e32da">

# #END</details>

<details>
<summary>3. Create URLs, Views and Templates </summary>

# Create URLs, Views and Templates

### src-AI-Software/my_projects/03_restful_apls_proj/demo_project/urls.py:

```py
"""
URL configuration for demo_project project.

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
    path('', include('store.urls')),
]

```

### src-AI-Software/my_projects/03_restful_apls_proj/store/urls.py:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list-products'),
]

```

### src-AI-Software/my_projects/03_restful_apls_proj/store/views.py:

```py
from django.shortcuts import render


def index(request):
    context = {
        'products': [
            {
                "id": 1,
                "name": "Product 1",
                "description": "Description of Product 1",
                "price": "10.99",
                "created_at": "2024-06-26T12:34:56Z"
            },
            {
                "id": 2,
                "name": "Product 2",
                "description": "Description of Product 2",
                "price": "20.99",
                "created_at": "2024-06-27T12:34:56Z"
            }
        ],
    }

    return render(request, 'store/product_list.html', context)

```

### src-AI-Software/my_projects/03_restful_apls_proj/store/templates/store/product_list.html:

```py
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Products</title>
</head>
<body>

<div class="product-list">
  {% for product in products %}
  <div class="product">
    <h2>S/N: 000{{ product.id }}</h2>
    <h2>{{ product.name }}</h2>
    <p>{{ product.description }}</p>
    <p>${{ product.price }}</p>
  </div>
  {% endfor %}
</div>


</body>
</html>
```

<img width="1533" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/8463fedb-2f6f-4aab-9e58-0fb4cd56304c">
<img width="1533" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/5ddaf4a5-6003-4013-943b-e5e97402807b">
<img width="1533" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/38411a04-d297-4728-bc5f-949ae80322f2">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/021ab1dc-9ff4-4904-9c79-47b4d11ba321)

# #END</details>

<details>
<summary>4. Create Base Template </summary>

# Create Base Template

### src-AI-Software/my_projects/03_restful_apls_proj/demo_project/settings.py:

```py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
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

### src-AI-Software/my_projects/03_restful_apls_proj/templates/store/base.html:

```py
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock title %}</title>
</head>
<body>

{% block content %}{% endblock content %}

</body>
</html>
```

### src-AI-Software/my_projects/03_restful_apls_proj/store/templates/store/product_list.html:

```py
{% extends 'store/base.html' %}

{% block title %}
Products
{% endblock title %}

{% block content %}

<div class="product-list">
  {% for product in products %}
  <div class="product">
    <h2>S/N: 000{{ product.id }}</h2>
    <h2>{{ product.name }}</h2>
    <p>{{ product.description }}</p>
    <p>${{ product.price }}</p>
  </div>
  <hr>

  {% endfor %}
</div>

{% endblock content %}

```

<img width="1533" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/ae9321c1-3254-4a5e-a42f-5a70e4fb9684">
<img width="1533" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/5380b272-6b6b-4ad5-a957-5ccf43ef30c7">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/f3ffe45c-f5d2-411a-b27b-ec975137a696)

# #END</details>

<details>
<summary>5. Setup Bootstrap Template </summary>

# Setup Bootstrap Template 

### Bootstrap default 

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  </head>
  <body>
    <h1>Hello, world!</h1>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  </body>
</html>
```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/4d8de945-af6d-40e6-abd4-343df5899b54)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/70e47928-735f-4416-b1d3-b989fc25b351)

### src-AI-Software/my_projects/03_restful_apls_proj/templates/store/base.html:

```html
<!DOCTYPE html>
<html lang="en" data-bs-theme="auto">
<head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{% block title %}{% endblock title %}</title>
    <link rel="canonical" href="https://getbootstrap.com/docs/5.3/examples/album/">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@docsearch/css@3">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  </head>
  <body>

<main>

  <section class="py-5 text-center container">
    <div class="row py-lg-5">
      <div class="col-lg-6 col-md-8 mx-auto">
        <h1 class="fw-light">Products</h1>
        <p class="lead text-body-secondary">Discover the best deals on a wide range of products tailored just for you. From the latest electronics and trendy fashion to home essentials and more, we have everything you need in one place. Enjoy seamless shopping, fast delivery, and excellent customer service. Happy shopping!</p>
        <p>
          <a href="#" class="btn btn-primary my-2">View Categories</a>
          <a href="#" class="btn btn-secondary my-2">My Cart</a>
        </p>
      </div>
    </div>
  </section>

  <div class="album py-5 bg-body-tertiary">
    <div class="container">
        {% block content %}{% endblock content %}
    </div>
  </div>

</main>


<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>

    </body>
</html>

```

### src-AI-Software/my_projects/03_restful_apls_proj/store/templates/store/product_list.html:

```html
{% extends 'store/base.html' %}

{% block title %}
Products
{% endblock title %}

{% block content %}

<div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">

    {% for product in products %}
    <div class="col">
        <div class="card shadow-sm">
        <svg class="bd-placeholder-img card-img-top" width="100%" height="225" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Thumbnail" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="#55595c"/>
        <text x="50%" y="50%" fill="#eceeef" dy=".3em">S/N: 000{{ product.id }}</text>
        </svg>
        <div class="card-body">
            <h2>{{ product.name }}</h2>
            <p class="card-text">{{ product.description }}</p>
            <div class="d-flex justify-content-between align-items-center">
            <div class="btn-group">
                <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
            </div>
            <small class="text-body-secondary">${{ product.price }}</small>
            </div>
        </div>
        </div>
    </div>
    {% endfor %}
</div>

{% endblock content %}

```

<img width="1493" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/56a989b1-4567-4ed7-90ce-d5a9d6cc3af2">
<img width="1493" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/592c028f-b922-42c2-84ce-4b05f9cc9c12">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/687dee76-5b56-43b0-9930-88543014418f)

# #END</details>

<details>
<summary>6. Adding Static and Media Files to Django </summary>

# Adding Static and Media Files to Django

### src-AI-Software/my_projects/03_restful_apls_proj/demo_project/settings.py:

```py
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'store', 'uploads'))
MEDIA_URL = '/uploads/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

### src-AI-Software/my_projects/03_restful_apls_proj/demo_project/urls.py:

```py
"""
URL configuration for demo_project project.

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
    path('', include('store.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

## Run Collectstatic (To add all static folders into a single main folder):

```py
python manage.py collectstatic
```

<img width="1493" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/42ed4634-c3fb-4a80-8fd3-ed12455e7e0f">
<img width="1493" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/81d822ec-97a9-44a9-8ed4-70efaebbf249">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/6e95459a-d5d5-4aa7-9d6e-4475be3f5996)

# #END</details>

<details>
<summary>7. Creating Models in Django </summary>

# Creating Models in Django

### src-AI-Software/my_projects/03_restful_apls_proj/store/models.py:

```py


from django.utils import timezone
from django.db import models


class Product(models.Model):
    DISCOUNT_RATE = 0.10

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    sale_start = models.DateTimeField(blank=True, null=True, default=None)
    sale_end = models.DateTimeField(blank=True, null=True, default=None)
    photo = models.ImageField(blank=True, null=True,
                              default=None, upload_to='products')

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def is_on_sale(self):
        now = timezone.now()
        if self.sale_start:
            if self.sale_end:
                return self.sale_start <= now <= self.sale_end
            return self.sale_start <= now
        return False

    def get_rounded_price(self):
        return round(self.price, 2)

    def current_price(self):
        if self.is_on_sale():
            discounted_price = self.price * (1 - self.DISCOUNT_RATE)
            return round(discounted_price, 2)
        return self.get_rounded_price()

    def __repr__(self):
        return '<Product object ({}) "{}">'.format(self.id, self.name)

    def __str__(self):
        return '{}-{}'.format(self.id, self.name)


class ShoppingCart(models.Model):
    TAX_RATE = 0.13

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    class Meta:
        verbose_name = "ShoppingCart"
        verbose_name_plural = "ShoppingCarts"

    def subtotal(self):
        amount = 0.0
        for item in self.shopping_cart_items:
            amount += item.quantity * item.product.get_price()
        return round(amount, 2)

    def taxes(self):
        return round(self.TAX_RATE * self.subtotal(), 2)

    def total(self):
        return round(self.subtotal() * self.taxes(), 2)

    def __repr__(self):
        name = self.name or '[Guest]'
        address = self.address or '[No Address]'
        return '<ShoppingCart object ({}) "{}" "{}">'.format(self.id, name, address)

    def __str__(self):
        return '{}-{}'.format(self.id, self.name)


class ShoppingCartItem(models.Model):
    shopping_cart = models.ForeignKey(
        ShoppingCart, related_name='items', related_query_name='item', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='+', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = "ShoppingCartItem"
        verbose_name_plural = "ShoppingCartItems"

    def total(self):
        return round(self.quantity * self.product.current_price())

    def __repr__(self):
        return '<ShoppingCartItem object ({}) {}x "{}">'.format(self.id, self.quantity, self.product.name)

    def __str__(self):
        return '{}-{}'.format(self.shopping_cart.id, self.product.name)


```

## Run migrations:

```x
python manage.py makemigrations
python manage.py migrate
```

```x
python manage.py runserver 
```

<img width="1527" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/18d496a7-e191-4619-a4be-c0c023ea32d5">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/865aaf48-b3dc-48aa-8341-d7018ac6b571)

# #END</details>

<details>
<summary>8. Setup Django Admin Panel </summary>

# Setup Django Admin Panel

## Create Super User

```x
python manage.py createsuperuser
```

### src-AI-Software/my_projects/03_restful_apls_proj/store/admin.py:

```py
from django.contrib import admin
from .models import Product, ShoppingCart, ShoppingCartItem


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price',
                    'sale_start', 'sale_end', 'photo', 'is_on_sale', 'get_rounded_price', 'current_price')


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'subtotal', 'taxes', 'total')


class ShoppingCartItemAdmin(admin.ModelAdmin):
    list_display = ('shopping_cart', 'product', 'quantity', 'total')


admin.site.register(Product, ProductAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
admin.site.register(ShoppingCartItem, ShoppingCartItemAdmin)

```

### src-AI-Software/my_projects/03_restful_apls_proj/store/models.py:

```py


from django.utils import timezone
from django.db import models


class Product(models.Model):
    DISCOUNT_RATE = 0.10

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    sale_start = models.DateTimeField(blank=True, null=True, default=None)
    sale_end = models.DateTimeField(blank=True, null=True, default=None)
    photo = models.ImageField(blank=True, null=True,
                              default=None, upload_to='products')

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def is_on_sale(self):
        now = timezone.now()
        if self.sale_start:
            if self.sale_end:
                return self.sale_start <= now <= self.sale_end
            return self.sale_start <= now
        return False

    def get_rounded_price(self):
        return round(self.price, 2)

    def current_price(self):
        if self.is_on_sale():
            discounted_price = self.price * (1 - self.DISCOUNT_RATE)
            return round(discounted_price, 2)
        return self.get_rounded_price()

    def __repr__(self):
        return '<Product object ({}) "{}">'.format(self.id, self.name)

    def __str__(self):
        return '{}-{}'.format(self.id, self.name)


class ShoppingCart(models.Model):
    TAX_RATE = 0.13

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    class Meta:
        verbose_name = "ShoppingCart"
        verbose_name_plural = "ShoppingCarts"

    def subtotal(self):
        amount = 0.0
        for item in self.shopping_cart_items:
            amount += item.quantity * item.product.get_price()
        return round(amount, 2)

    def taxes(self):
        return round(self.TAX_RATE * self.subtotal(), 2)

    def total(self):
        return round(self.subtotal() * self.taxes(), 2)

    def __repr__(self):
        name = self.name or '[Guest]'
        address = self.address or '[No Address]'
        return '<ShoppingCart object ({}) "{}" "{}">'.format(self.id, name, address)

    def __str__(self):
        return '{}-{}'.format(self.id, self.name)


class ShoppingCartItem(models.Model):
    shopping_cart = models.ForeignKey(
        ShoppingCart, related_name='items', related_query_name='item', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='+', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = "ShoppingCartItem"
        verbose_name_plural = "ShoppingCartItems"

    def total(self):
        return round(self.quantity * self.product.current_price())

    def __repr__(self):
        return '<ShoppingCartItem object ({}) {}x "{}">'.format(self.id, self.quantity, self.product.name)

    def __str__(self):
        return '{}-{}'.format(self.shopping_cart.id, self.product.name)


```

## Run migrations:

```x
python manage.py makemigrations
python manage.py migrate
```

```x
python manage.py runserver 
```

<img width="1527" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/35673948-d69f-4181-a5a7-a86318d00cfe">

<img width="1527" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/fd49bc99-eab4-47e1-a587-9e56dff4a5dc">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/a3aba51d-3aa1-43f7-aa74-89f620347e24)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/f427ffd5-48bd-41f6-8a6b-64ccd483f3b7)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/f36f519a-7fb6-4ec0-8a69-444497b5ef13)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/825fb62b-47b8-4515-84a5-49f23c2dec67)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/f7c310b9-f40a-473d-9b6d-23ed8af376e5)

# #END</details>

<details>
<summary>9. Add Products using Admin Panel </summary>

# Add Products using Admin Panel

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/671de37b-8a76-49b3-a53c-fbe959ab21b9)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/5e33c089-f630-471d-afd1-f80183934311)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/7dc40e19-7bf9-4234-b672-4acc51d0b99a)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/40995476-2d27-41a0-bea7-c729db03e643)

# #END</details>

<details>
<summary>10. Using Django shell for creating and querying data </summary>

# Using Django shell for creating and querying data

## Run Shell:

```x
python manage.py shell
```

## Get Instance of Model Object:

```py
>>> from store.models import Product

>>> Product
<class 'store.models.Product'>

>>> myproduct = Product.objects.get(name='Vitamin B-Complex (100 caplets)')

>>> myproduct
<Product object (5) "Vitamin B-Complex (100 caplets)">

>>> myproduct.id
5

>>> myproduct.name
'Vitamin B-Complex (100 caplets)'

>>> myproduct.price
3.0

>>> myproduct.description
'Contains a combination of essential B vitamins that help convert food to energy.'

```

## Get all Object Instances

```py
>>> Product.objects.all()
<QuerySet [<Product object (2) "Mineral Water Strawberry">, <Product object (3) "Mineral Water Raspberry">,
<Product object (4) "Vitamin A 10,000 IU (125 caplets)">, <Product object (5) "Vitamin B-Complex (100 caplets)">]>

```

## Create New Object Instance

```py
>>> new_product = Product.objects.create(name='Mineral Water Peach', description='Flavoured with peach, loaded with anti-oxidants.', price=2.0)

>>> new_product
<Product object (6) "Mineral Water Peach">

>>> Product.objects.get(pk=6)
<Product object (6) "Mineral Water Peach">

>>> Product.objects.all()                                                                 
<QuerySet [<Product object (2) "Mineral Water Strawberry">, <Product object (3) "Mineral Water Raspberry">,
<Product object (4) "Vitamin A 10,000 IU (125 caplets)">, <Product object (5) "Vitamin B-Complex (100 caplets)">, <Product object (6) "Mineral Water Peach">]>

```

## Filter and Exclude contents

```py

>>> Product.objects.filter(name__startswith="Mineral")
<QuerySet [<Product object (2) "Mineral Water Strawberry">, <Product object (3) "Mineral Water Raspberry">, <Product object (6) "Mineral Water Peach">]>


>>> Product.objects.filter(description__icontains="anti-oxidant")
<QuerySet [<Product object (2) "Mineral Water Strawberry">, <Product object (3) "Mineral Water Raspberry">, <Product object (6) "Mineral Water Peach">]>


>>> Product.objects.exclude(description__icontains="vitamin")
<QuerySet [<Product object (2) "Mineral Water Strawberry">, <Product object (3) "Mineral Water Raspberry">, <Product object (6) "Mineral Water Peach">]>


>>> Product.objects.filter(description__icontains="essential").exclude(name__icontains="10,000")
<QuerySet [<Product object (5) "Vitamin B-Complex (100 caplets)">]>

```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/b141596d-5392-486d-a5a0-52564ac09eb6)

# #END</details>

<details>
<summary>11. Display all Products in Template </summary>

# Display all Products in Template

### src-AI-Software/my_projects/03_restful_apls_proj/store/urls.py:

```py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='list-products'),
]

```

src-AI-Software/my_projects/03_restful_apls_proj/store/views.py:

```py
from django.shortcuts import render
from store.models import Product, ShoppingCart


def index(request):
    # context = {
    #     'products': [
    #         {
    #             "id": 1,
    #             "name": "Product 1",
    #             "description": "Description of Product 1",
    #             "price": "10.99",
    #             "created_at": "2024-06-26T12:34:56Z"
    #         },
    #         {
    #             "id": 2,
    #             "name": "Product 2",
    #             "description": "Description of Product 2",
    #             "price": "20.99",
    #             "created_at": "2024-06-27T12:34:56Z"
    #         }
    #     ],
    # }

    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'store/product_list.html', context)

```

### src-AI-Software/my_projects/03_restful_apls_proj/store/templates/store/product_list.html:

```html
{% extends 'store/base.html' %}

{% block title %}
Products
{% endblock title %}

{% block content %}

<div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">

    {% for product in products %}
    <div class="col">
        <div class="card shadow-sm">
        <a href="">
            {% if product.photo %}
            <img width="100%" src="uploads/{{ product.photo }}" />
            {% else %}
            <img width="100%" src="uploads/products/mineralwater-strawberry.jpg" />
            {% endif %}
        </a>

        <div class="card-body d-flex flex-column justify-content-between align-items-between" style="min-height: 25vh;">
            <h2>{{ product.name }}</h2>
            <p class="card-text">{{ product.description }}</p>
            <div class="d-flex justify-content-between align-items-center">
            <div class="btn-group">
                <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                {% if product.is_on_sale %}
                <button type="button" class="btn btn-sm btn-danger">SALE: {{ product.DISCOUNT_RATE|cut:"0."}}0% OFF</button>
                {% endif %}
            </div>
            <h3 class="text-body-secondary">${{ product.current_price }}</h3>
            </div>
        </div>
        </div>
    </div>
    {% endfor %}
</div>

{% endblock content %}

```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/53855d77-7f37-4966-8429-c7902a5ec4f5)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/579e769c-5b09-47da-b701-5bf9f459c653)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/899618f6-2fe4-4c00-be10-ef8ce1d3057d)

<img width="1470" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/2ad1c274-0d2c-4435-a157-a74c38429036">
<img width="1470" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/d56ebb2e-0913-453f-835c-04f8c37d0e3d">
<img width="1470" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/be934642-2eef-4428-9f89-e6dbfe081928">

# #END</details>

<details>
<summary>12. Display a single Product w 404 Page </summary>

# Display a single Product w 404 Page

### src-AI-Software/my_projects/03_restful_apls_proj/store/urls.py:

```py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='list-products'),
    path('products/<int:id>/', views.show, name='show-product'),
]

```

### src-AI-Software/my_projects/03_restful_apls_proj/store/views.py:

```py
from django.shortcuts import render
from django.http import Http404
from store.models import Product


def index(request):
    # context = {
    #     'products': [
    #         {
    #             "id": 1,
    #             "name": "Product 1",
    #             "description": "Description of Product 1",
    #             "price": "10.99",
    #             "created_at": "2024-06-26T12:34:56Z"
    #         },
    #         {
    #             "id": 2,
    #             "name": "Product 2",
    #             "description": "Description of Product 2",
    #             "price": "20.99",
    #             "created_at": "2024-06-27T12:34:56Z"
    #         }
    #     ],
    # }

    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'store/product_list.html', context)


def show(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        # return render(request, '404.html')
        raise Http404("Note does not exist")

    context = {
        'product': product,
    }
    return render(request, 'store/product.html', context)

```

### src-AI-Software/my_projects/03_restful_apls_proj/store/templates/store/product.html:

```py
{% extends 'store/base.html' %}

{% block title %}{{ product.name }}{% endblock %}

{% block content %}
<h2>{{ product.name }}</h2>
<p>{{ product.description }}</p>

{% if product.is_on_sale %}
  <p class="price sale-price">
    Regular Price:<del>${{ product.price|floatformat:2 }}</del> <br/>
    <strong>SALE: ${{ product.current_price|floatformat:2 }}</strong>
  </p>
{% else %}
  <p class="price price-regular">
    <strong>Price: ${{ product.price|floatformat:2 }}</strong>
  </p>
{% endif %}

 {% if product.photo %}
<img src="{{product.photo.url}}" width="300px" />
{% else %}
<img src="/uploads/products/mineralwater-strawberry.jpg" width="300px" />
{% endif %}

{% endblock %}

```

### src-AI-Software/my_projects/03_restful_apls_proj/store/templates/store/product_list.html:

```py
{% extends 'store/base.html' %}

{% block title %}
Products
{% endblock title %}

{% block content %}

<div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">

    {% for product in products %}
    <div class="col">
        <div class="card shadow-sm">
        <a href="{% url 'show-product' product.id %}">
            {% if product.photo %}
            <img width="100%" src="uploads/{{ product.photo }}" />
            {% else %}
            <img width="100%" src="uploads/products/mineralwater-strawberry.jpg" />
            {% endif %}
        </a>

        <div class="card-body d-flex flex-column justify-content-between align-items-between" style="min-height: 25vh;">
            <h2>{{ product.name }}</h2>
            <p class="card-text">{{ product.description }}</p>
            <div class="d-flex justify-content-between align-items-center">
            <div class="btn-group">
                <a href="{% url 'show-product' product.id %}">
                    <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                </a>

                {% if product.is_on_sale %}
                <button type="button" class="btn btn-sm btn-danger">SALE: {{ product.DISCOUNT_RATE|cut:"0."}}0% OFF</button>
                {% endif %}
            </div>
            <h3 class="text-body-secondary">${{ product.current_price|floatformat:2 }}</h3>
            </div>
        </div>
        </div>
    </div>
    {% endfor %}
</div>

{% endblock content %}

```

### src-AI-Software/my_projects/03_restful_apls_proj/templates/404.html:

```py
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>404 Page</title>
  </head>

  <body>
    <h1>404 - Ooops!</h1>
    <h2>I cannot find the Page you requested!</h2>
  </body>
</html>
```

### src-AI-Software/my_projects/03_restful_apls_proj/templates/store/base.html:

```py
<!DOCTYPE html>
<html lang="en" data-bs-theme="auto">
<head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{% block title %}{% endblock title %}</title>
    <link rel="canonical" href="https://getbootstrap.com/docs/5.3/examples/album/">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@docsearch/css@3">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  </head>
  <body>

<main>

  <section class="py-5 text-center container">
    <div class="row py-lg-5">
      <div class="col-lg-6 col-md-8 mx-auto">
        <h1 class="fw-light">Products</h1>
        <p class="lead text-body-secondary">Discover the best deals on a wide range of products tailored just for you. From the latest electronics and trendy fashion to home essentials and more, we have everything you need in one place. Enjoy seamless shopping, fast delivery, and excellent customer service. Happy shopping!</p>
        <p>
          <a href="{% url 'list-products' %}" class="btn btn-primary my-2">All Products</a>
          <a href="#" class="btn btn-secondary my-2">My Cart</a>
        </p>
      </div>
    </div>
  </section>

  <div class="album py-5 bg-body-tertiary">
    <div class="container">
        {% block content %}{% endblock content %}
    </div>
  </div>

</main>


<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>

    </body>
</html>

```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/e66b7fca-053b-423f-b879-9c33871de5b6)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/1cdba6cb-fceb-4860-aacb-19785aa810fd)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/58f45695-cb32-4417-9266-0778c9d129ba)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/35490631-9cf2-485b-9edf-bdbcc7248365)

<img width="1470" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/03998596-30be-4f07-ac3a-546a6224e6bf">
<img width="1470" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/7bf3fdbf-3eb5-4a75-8aae-231e68f23016">
<img width="1470" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/ec1b53f5-2b19-4ea6-b7d8-a2c1484ba99f">
<img width="1470" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/61035939-da65-4bbb-b581-c2ec7fa493db">
<img width="1470" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/7a5a0568-99e4-4aba-bb4c-749916706987">
<img width="1470" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/5de2f7bb-c271-4618-b88b-04c236f55c79">

# #END</details>

<details>
<summary>13. Setup Cart Page with dummy data </summary>

# Setup Cart Page with dummy data

### src-AI-Software/my_projects/03_restful_apls_proj/store/urls.py:

```py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='list-products'),
    path('products/<int:id>/', views.show, name='show-product'),
    path('cart/', views.cart, name='shopping-cart'),
]

```

### src-AI-Software/my_projects/03_restful_apls_proj/store/views.py:

```py
from django.shortcuts import render
from django.http import Http404
from store.models import Product, ShoppingCart


def index(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'store/product_list.html', context)


def show(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        # return render(request, '404.html')
        raise Http404("Note does not exist")

    context = {
        'product': product,
    }
    return render(request, 'store/product.html', context)


def cart(request):
    context = {
        'items': [],
        'subtotal': 1.0,
        'tax_rate': int(ShoppingCart.TAX_RATE * 100.0),
        'tax_total': 2.0,
        'total': 3.0,
    }
    return render(request, 'store/cart.html', context)

```

### src-AI-Software/my_projects/03_restful_apls_proj/store/templates/store/cart.html:

```html
{% extends 'store/base.html' %}

{% block title %}Shopping Cart{% endblock title %}

{% block content %}
<h2>Shopping Cart</h2>
<table class="table">
  <tbody>
    <tr>
      <th>Items</th>
      <td>
        {% for item in items %}
        <div>
          {{ item.quantity }}x
          {{ item.name }}
        </div>
        {% endfor %}
      </td>
    </tr>
    <tr>
      <th>Subtotal</th>
      <td>${{ subtotal|floatformat:2 }}</td>
    </tr>
    <tr>
      <th>Shipping</th>
      <td>Free</td>
    </tr>
    <tr>
      <th>Taxes ({{ tax_rate }}%)</th>
      <td>${{ tax_total|floatformat:2 }}</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <th>Total</th>
      <td>${{ total|floatformat:2 }}</td>
    </tr>
  </tfoot>
</table>
{% endblock content %}

```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/ee7d73f9-fb38-46fb-8131-18f71d645731)

<img width="1470" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/6c71a7be-b474-487b-af1f-3731f2204548">
<img width="1470" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/7a473315-b6c3-421d-8bec-be5dff2228e6">
<img width="1470" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/99eccbbc-755a-4410-b843-188d74dd71b9">

# #END</details>

<details>
<summary>14. DRF - Creating Serializer to Serialize Product Model </summary>

# DRF - Creating Serializer to Serialize Product Model

### src-AI-Software/my_projects/03_restful_apls_proj/store/serializers.py:

```py
from rest_framework import serializers

from store.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description',
                  'price', 'sale_start', 'sale_end')

    # add additional custom fields to the serializer.
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['is_on_sale'] = instance.is_on_sale()
        data['current_price'] = instance.current_price()
        return data

```

## Run Django Shell

```x
python manage.py shell
```

```py
>>> from store.models import Product
>>> product = Product.objects.all()[0]
>>> product
<Product object (2) "Mineral Water Strawberry">

>>> from store.serializers import ProductSerializer
>>> serializer = ProductSerializer()
>>> serializer
ProductSerializer():
    id = IntegerField(read_only=True)
    name = CharField(max_length=200)
    description = CharField(style={'base_template': 'textarea.html'})
    price = FloatField()
    sale_start = DateTimeField(allow_null=True, required=False)
    sale_end = DateTimeField(allow_null=True, required=False)

>>> data = serializer.to_representation(product)
>>> data
{'id': 2, 'name': 'Mineral Water Strawberry', 'description': 'Natural-flavored strawberry with an anti-oxidant kick.',
'price': 1.0, 'sale_start': None, 'sale_end': None, 'is_on_sale': False, 'current_price': 1.0}

>>> from rest_framework.renderers import JSONRenderer
>>> renderer = JSONRenderer()
>>> print(renderer.render(data))
b'{"id":2,"name":"Mineral Water Strawberry","description":"Natural-flavored strawberry with an anti-oxidant kick.",
"price":1.0,"sale_start":null,"sale_end":null,"is_on_sale":false,"current_price":1.0}'

```

<img width="1470" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/02f67553-b872-4f49-b09a-f8d62517bc33">


# #END</details>

<details>
<summary>15. DRF - Creating ListAPIView to view serialized Data </summary>

# DRF - Creating ListAPIView to view serialized Data

### src-AI-Software/my_projects/03_restful_apls_proj/store/api_views.py:

```py
from rest_framework.generics import ListAPIView

from store.serializers import ProductSerializer
from store.models import Product


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

```

### src-AI-Software/my_projects/03_restful_apls_proj/store/serializers.py:

```py
from rest_framework import serializers

from store.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description',
                  'price', 'sale_start', 'sale_end')

    # add additional custom fields to the serializer.
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['is_on_sale'] = instance.is_on_sale()
        data['current_price'] = instance.current_price()
        return data

```

<img width="1517" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/88aacef9-aea0-4172-b030-3fc058aa4210">

# #END</details>

<details>
<summary>16. DRF - Connecting ListAPIView to URL Route </summary>

# DRF - Connecting ListAPIView to URL Route

### src-AI-Software/my_projects/03_restful_apls_proj/store/urls.py:

```py
from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    path('', views.index, name='list-products'),
    path('products/<int:id>/', views.show, name='show-product'),
    path('cart/', views.cart, name='shopping-cart'),
    path('api/v1/products/', api_views.ProductList.as_view()),
]

```

### src-AI-Software/my_projects/03_restful_apls_proj/store/api_views.py:

```py
from rest_framework.generics import ListAPIView

from store.serializers import ProductSerializer
from store.models import Product


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

```

## http://127.0.0.1:8000/api/v1/products/

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/b08b65dd-e760-4938-9516-42785e824974)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/feb3dce3-a823-4c7a-96ea-0d39b6f6f43b)

<img width="1517" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/36329589-fc38-432e-87e8-08b722c04740">

# #END</details>

<details>
<summary>17. DRF - Filter results with URL Query Parameters - id, name, price </summary>

# DRF - Filter results with URL Query Parameters - id, name, price 

### src-AI-Software/my_projects/03_restful_apls_proj/store/api_views.py:

```py
from rest_framework.generics import ListAPIView
from django_filters import rest_framework as filters

from store.serializers import ProductSerializer
from store.models import Product


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('id', 'name', 'price')

```

## http://127.0.0.1:8000/api/v1/products/?id=3&name=&price=

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/a3a6bb39-705e-4043-b94d-0769e61990f0)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/ee179fe3-fe64-4c73-99d1-4df3eb115233)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/587cfeef-3246-4392-a4f9-471760eece69)

<img width="1517" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/6cc7617d-2be4-498f-9512-d1d25f5e8de6">

# #END</details>

<details>
<summary>18. DRF - Filter Results with URL Query Parameters - Customized Fields (is_on_sale) </summary>

# DRF - Filter Results with URL Query Parameters - Customized Fields (is_on_sale)

### src-AI-Software/my_projects/03_restful_apls_proj/store/api_views.py:

```py
from rest_framework.generics import ListAPIView
from django_filters import rest_framework as filters

from store.serializers import ProductSerializer
from store.models import Product


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('id', 'name', 'price')

    def get_queryset(self):
        on_sale = self.request.query_params.get('on_sale', None)
        if on_sale is None:
            return super().get_queryset()
        queryset = Product.objects.all()
        if on_sale.lower() == 'true':
            from django.utils import timezone
            now = timezone.now()
            return queryset.filter(
                sale_start__lte=now,
                sale_end__gte=now,
            )
        return queryset

```

## http://127.0.0.1:8000/api/v1/products/?on_sale=true

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/9d78fb87-a108-4710-bd26-fb796775580e)

<img width="1517" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/62695a5a-e2e3-4a92-93a6-06e0a7da1780">

# #END</details>

<details>
<summary>19. DRF - Filter Results with URL Query Parameters - Partial and Full text Search </summary>

# DRF - Filter Results with URL Query Parameters - Partial and Full text Search

### src-AI-Software/my_projects/03_restful_apls_proj/store/api_views.py:

```py
from rest_framework.generics import ListAPIView
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter

from store.serializers import ProductSerializer
from store.models import Product


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filterset_fields = ('id', 'name', 'price')
    search_fields = ('name', 'description')

    def get_queryset(self):
        on_sale = self.request.query_params.get('on_sale', None)
        if on_sale is None:
            return super().get_queryset()
        queryset = Product.objects.all()
        if on_sale.lower() == 'true':
            from django.utils import timezone
            now = timezone.now()
            return queryset.filter(
                sale_start__lte=now,
                sale_end__gte=now,
            )
        return queryset

```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/67837399-e150-41f1-bb4c-3551cffd27de)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/4269faa5-92ff-452a-996e-631455af413f)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/f260b4d8-cf8c-4f0a-94ca-9fcd150844e8)

# #END</details>

<details>
<summary>20. DRF - Enabling Pagination </summary>

# DRF - Enabling Pagination

### src-AI-Software/my_projects/03_restful_apls_proj/store/api_views.py:

```py
from rest_framework.generics import ListAPIView
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from store.serializers import ProductSerializer
from store.models import Product


class ProductsPagination(LimitOffsetPagination):
    default_limit = 10  # default limit set of 10 search results per page
    max_limit = 100  # maximum limit set of 100 search results per page by client
    # offset_query_param = 'offset'  # offset query parameter name
    # offset is the number of previous pages to skip

class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filterset_fields = ('id', 'name', 'price')
    search_fields = ('name', 'description')
    pagination_class = ProductsPagination

    def get_queryset(self):
        on_sale = self.request.query_params.get('on_sale', None)
        if on_sale is None:
            return super().get_queryset()
        queryset = Product.objects.all()
        if on_sale.lower() == 'true':
            from django.utils import timezone
            now = timezone.now()
            return queryset.filter(
                sale_start__lte=now,
                sale_end__gte=now,
            )
        return queryset

```

## http://127.0.0.1:8000/api/v1/products/?limit=2

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/c62ce380-e33c-4c2f-af20-00a733b2f42d)

## http://127.0.0.1:8000/api/v1/products/?limit=2&offset=1

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/ecefe038-6ed5-49bd-a530-3b9941356100)

## http://127.0.0.1:8000/api/v1/products/?limit=1&offset=3

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/32f8dd6f-eb97-44eb-8c0b-5d2bea96d6fa)

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/5d9654db-1f07-493c-84c0-b35212d33db8)

<img width="1517" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/feb191aa-c93c-4761-b0ef-33f65ca3db10">

# #END</details>

<details>
<summary>21. DRF - Create Products with CreateAPIView </summary>

# DRF - Create Products with CreateAPIView 

### src-AI-Software/my_projects/03_restful_apls_proj/store/urls.py:

```py
from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    path('', views.index, name='list-products'),
    path('products/<int:id>/', views.show, name='show-product'),
    path('cart/', views.cart, name='shopping-cart'),
    path('api/v1/products/', api_views.ProductList.as_view()),
    path('api/v1/products/new', api_views.ProductCreate.as_view()),
]

```

### src-AI-Software/my_projects/03_restful_apls_proj/store/api_views.py:

```py
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.exceptions import ValidationError
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from store.serializers import ProductSerializer
from store.models import Product


class ProductsPagination(LimitOffsetPagination):
    default_limit = 10  # default limit set of 10 search results per page
    max_limit = 100  # maximum limit set of 100 search results per page by client
    # offset_query_param = 'offset'  # offset query parameter name
    # offset is the number of previous pages to skip


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filterset_fields = ('id', 'name', 'price')
    search_fields = ('name', 'description')
    pagination_class = ProductsPagination

    def get_queryset(self):
        on_sale = self.request.query_params.get('on_sale', None)
        if on_sale is None:
            return super().get_queryset()
        queryset = Product.objects.all()
        if on_sale.lower() == 'true':
            from django.utils import timezone
            now = timezone.now()
            return queryset.filter(
                sale_start__lte=now,
                sale_end__gte=now,
            )
        return queryset


class ProductCreate(CreateAPIView):
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        try:
            price = request.data.get('price')
            if price is not None and float(price) <= 0.0:
                raise ValidationError({'price': 'Must be above $0.00'})
        except ValueError:
            raise ValidationError({'price': 'A valid number is required'})
        return super().create(request, *args, **kwargs)

```

## Test CreateAPI Route with Curl: 

```x
curl -X POST http://localhost:8000/api/v1/products/new -d price=1.00 -d name='My Product' -d description='Hello world'

{"id":7,"name":"My Product","description":"Hello world","price":1.0,"sale_start":null,
"sale_end":null,"is_on_sale":false,"current_price":1.0}
```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/e2512014-959d-4574-b3f3-4aa68d323d6e)

## Test CreateAPI Route with Postman:

<img width="1415" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/c5c47e12-1f1f-4536-91d7-a668df7dec1f">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/b35b1e4a-3e7a-4b7e-a067-67a782009e44)

## Test CreateAPI Route with Browser:

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/645ae70e-9537-43c6-ab46-65bfce568e93)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/b42232b0-8b1f-4f8f-af18-4b25e340ac67)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/9b85c192-e23c-4406-8cde-692e315fe81e)

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/7e559772-a853-428a-8082-34f8fb3bc931)

<img width="1453" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/e567b8f0-1e4f-4011-bceb-e8428a81bf89">
<img width="1453" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/4b643b86-866c-46bb-805b-23b03f990807">

# #END</details>

<details>
<summary>22. DRF - Delete Products with DestroyAPIView </summary>

# DRF - Delete Products with DestroyAPIView

### src-AI-Software/my_projects/03_restful_apls_proj/store/urls.py:

```py
from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    path('', views.index, name='list-products'),
    path('products/<int:id>/', views.show, name='show-product'),
    path('cart/', views.cart, name='shopping-cart'),
    path('api/v1/products/', api_views.ProductList.as_view()),
    path('api/v1/products/new', api_views.ProductCreate.as_view()),
    path('api/v1/products/<int:id>/destroy',
         api_views.ProductDestroy.as_view()),
]

```

### src-AI-Software/my_projects/03_restful_apls_proj/store/api_views.py:

```py
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.exceptions import ValidationError
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from store.serializers import ProductSerializer
from store.models import Product


class ProductsPagination(LimitOffsetPagination):
    default_limit = 10  # default limit set of 10 search results per page
    max_limit = 100  # maximum limit set of 100 search results per page by client
    # offset_query_param = 'offset'  # offset query parameter name
    # offset is the number of previous pages to skip


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filterset_fields = ('id', 'name', 'price')
    search_fields = ('name', 'description')
    pagination_class = ProductsPagination

    def get_queryset(self):
        on_sale = self.request.query_params.get('on_sale', None)
        if on_sale is None:
            return super().get_queryset()
        queryset = Product.objects.all()
        if on_sale.lower() == 'true':
            from django.utils import timezone
            now = timezone.now()
            return queryset.filter(
                sale_start__lte=now,
                sale_end__gte=now,
            )
        return queryset


class ProductCreate(CreateAPIView):
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        try:
            price = request.data.get('price')
            if price is not None and float(price) <= 0.0:
                raise ValidationError({'price': 'Must be above $0.00'})
        except ValueError:
            raise ValidationError({'price': 'A valid number is required'})
        return super().create(request, *args, **kwargs)


class ProductDestroy(DestroyAPIView):
    queryset = Product.objects.all()
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        product_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('product_data_{}'.format(product_id))
        return response

```

## Test DestoryAPI Route with Curl:

```x
curl -X DELETE http://localhost:8000/api/v1/products/7/destroy
```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/5d693f01-e568-4b83-b29b-644afc237d72)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/8df0e1b6-b8e8-44e6-aad4-bda34a8d6789)


## Test DestoryAPI Route with Postman:

<img width="1415" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/282289be-159b-400e-be75-aa2484e0d494">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/8df0e1b6-b8e8-44e6-aad4-bda34a8d6789)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/ed763665-526e-4ed2-aafa-7b45495d0977)

## Test DestoryAPI Route with Browser:

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/2c166ab0-4513-4aca-91ed-62100efe7b82)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/11fa00a2-4751-43ce-979a-f695abcce5f6)

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/ed763665-526e-4ed2-aafa-7b45495d0977)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/681eea82-bcc3-499f-9ffa-dd48ec51e4b0)

# #END</details>

<details>
<summary>23. DRF - Update Products with RetrieveUpdateDestroyAPIView </summary>

# DRF - Update Products with RetrieveUpdateDestroyAPIView

### src-AI-Software/my_projects/03_restful_apls_proj/store/urls.py:

```py
from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    path('', views.index, name='list-products'),
    path('products/<int:id>/', views.show, name='show-product'),
    path('cart/', views.cart, name='shopping-cart'),
    path('api/v1/products/', api_views.ProductList.as_view()),
    path('api/v1/products/new', api_views.ProductCreate.as_view()),
    path('api/v1/products/<int:id>/destroy',
         api_views.ProductDestroy.as_view()),
    path('api/v1/products/<int:id>/',
         api_views.ProductRetrieveUpdateDestroy.as_view()),
]

```

### src-AI-Software/my_projects/03_restful_apls_proj/store/api_views.py:

```py
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.exceptions import ValidationError
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from store.serializers import ProductSerializer
from store.models import Product


class ProductsPagination(LimitOffsetPagination):
    default_limit = 10  # default limit set of 10 search results per page
    max_limit = 100  # maximum limit set of 100 search results per page by client
    # offset_query_param = 'offset'  # offset query parameter name
    # offset is the number of previous pages to skip


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filterset_fields = ('id', 'name', 'price')
    search_fields = ('name', 'description')
    pagination_class = ProductsPagination

    def get_queryset(self):
        on_sale = self.request.query_params.get('on_sale', None)
        if on_sale is None:
            return super().get_queryset()
        queryset = Product.objects.all()
        if on_sale.lower() == 'true':
            from django.utils import timezone
            now = timezone.now()
            return queryset.filter(
                sale_start__lte=now,
                sale_end__gte=now,
            )
        return queryset


class ProductCreate(CreateAPIView):
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        try:
            price = request.data.get('price')
            if price is not None and float(price) <= 0.0:
                raise ValidationError({'price': 'Must be above $0.00'})
        except ValueError:
            raise ValidationError({'price': 'A valid number is required'})
        return super().create(request, *args, **kwargs)


class ProductDestroy(DestroyAPIView):
    queryset = Product.objects.all()
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        product_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('product_data_{}'.format(product_id))
        return response


class ProductRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    lookup_field = 'id'
    serializer_class = ProductSerializer

    def delete(self, request, *args, **kwargs):
        product_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('product_data_{}'.format(product_id))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            product = response.data
            cache.set('product_data_{}'.format(product['id']), {
                'name': product['name'],
                'description': product['description'],
                'price': product['price'],
            })
        return response

```

## Test RetrieveUpdateDestroyAPI Route with Browser to Update Record:

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/123cb76d-f930-4159-8593-eaed1c598c7a)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/87871b1d-1f3f-4b35-9301-bb2efe7f8bd7)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/153833de-6719-40fc-bc20-4f69443616f3)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/d65b9375-360a-483a-99de-11775d196ff4)

<img width="1453" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/b7cabaa3-6270-43b8-ad0d-096564b35afc">
<img width="1453" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/860107a1-1c44-4e93-8386-cdf387438777">

# #END</details>

<details>
<summary>24. DRF - Serializer with selected Customized Fields </summary>

# DRF - Serializer with selected Customized Fields

### src-AI-Software/my_projects/03_restful_apls_proj/store/serializers.py:

```py
from rest_framework import serializers

from store.models import Product


class ProductSerializer(serializers.ModelSerializer):
    is_on_sale = serializers.BooleanField(read_only=True)
    current_price = serializers.FloatField(read_only=True)
    description = serializers.CharField(min_length=2, max_length=200)

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'description', 'price', 'sale_start', 'sale_end',
            'is_on_sale', 'current_price',
        )

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ('id', 'name', 'description',
#                   'price', 'sale_start', 'sale_end')

#     # add additional custom fields to the serializer.
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         data['is_on_sale'] = instance.is_on_sale()
#         data['current_price'] = instance.current_price()
#         return data

```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/1aebac1f-c930-4895-815d-0715e309793c)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/b8f16118-0e50-4841-a708-455dcac0fa8e)

<img width="1527" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/44737416-d158-425d-83fa-d2f64fbe007d">

# #END</details>

<details>
<summary>25. DRF - Serializer Relationship - Adding Shopping Cart to Product Field </summary>

# DRF - Serializer Relationship - Adding Shopping Cart to Product Field

### src-AI-Software/my_projects/03_restful_apls_proj/store/serializers.py:

```py
from rest_framework import serializers

from store.models import Product, ShoppingCartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCartItem
        fields = ('product', 'quantity')


class ProductSerializer(serializers.ModelSerializer):
    is_on_sale = serializers.BooleanField(read_only=True)
    current_price = serializers.FloatField(read_only=True)
    description = serializers.CharField(min_length=2, max_length=200)
    cart_items = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'description', 'price', 'sale_start', 'sale_end',
            'is_on_sale', 'current_price', 'cart_items',
        )

    def get_cart_items(self, instance):
        items = ShoppingCartItem.objects.filter(product=instance)
        return CartItemSerializer(items, many=True).data

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ('id', 'name', 'description',
#                   'price', 'sale_start', 'sale_end')

#     # add additional custom fields to the serializer.
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         data['is_on_sale'] = instance.is_on_sale()
#         data['current_price'] = instance.current_price()
#         return data

```

### src-AI-Software/my_projects/03_restful_apls_proj/store/models.py:

```py

from django.utils import timezone
from django.db import models


class Product(models.Model):
    DISCOUNT_RATE = 0.10

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    sale_start = models.DateTimeField(blank=True, null=True, default=None)
    sale_end = models.DateTimeField(blank=True, null=True, default=None)
    photo = models.ImageField(blank=True, null=True,
                              default=None, upload_to='products')

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def is_on_sale(self):
        now = timezone.now()
        if self.sale_start:
            if self.sale_end:
                return self.sale_start <= now <= self.sale_end
            return self.sale_start <= now
        return False

    def get_rounded_price(self):
        return round(self.price, 2)

    def current_price(self):
        if self.is_on_sale():
            discounted_price = self.price * (1 - self.DISCOUNT_RATE)
            return round(discounted_price, 2)
        return self.get_rounded_price()

    def __repr__(self):
        return '<Product object ({}) "{}">'.format(self.id, self.name)

    def __str__(self):
        return '{}-{}'.format(self.id, self.name)


class ShoppingCart(models.Model):
    TAX_RATE = 0.13

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    class Meta:
        verbose_name = "ShoppingCart"
        verbose_name_plural = "ShoppingCarts"

    def subtotal(self):
        amount = 0.0
        for item in self.shopping_cart_items:
            amount += item.quantity * item.product.get_price()
        return round(amount, 2)

    def taxes(self):
        return round(self.TAX_RATE * self.subtotal(), 2)

    def total(self):
        return round(self.subtotal() * self.taxes(), 2)

    def __repr__(self):
        name = self.name or '[Guest]'
        address = self.address or '[No Address]'
        return '<ShoppingCart object ({}) "{}" "{}">'.format(self.id, name, address)

    def __str__(self):
        return '{}-{}'.format(self.id, self.name)


class ShoppingCartItem(models.Model):
    shopping_cart = models.ForeignKey(
        ShoppingCart, related_name='items', related_query_name='item', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='+', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = "ShoppingCartItem"
        verbose_name_plural = "ShoppingCartItems"

    def total(self):
        return round(self.quantity * self.product.current_price())

    def __repr__(self):
        return '<ShoppingCartItem object ({}) {}x "{}">'.format(self.id, self.quantity, self.product.name)

    def __str__(self):
        return '{}-{}'.format(self.shopping_cart.id, self.product.name)

```

## Run Python Shell

```py
python manage.py shell
```

```py
>>> import json
>>> from store.models import *
>>> from store.serializers import *

>>> product = Product.objects.all().first()
>>> product
<Product object (2) "Mineral Water Strawberry">

>>> cart = ShoppingCart(name='ifeanyi', address='234 Haven str., Calgary')
>>> cart
<ShoppingCart object (None) "ifeanyi" "234 Haven str., Calgary">
>>> cart.save()
>>> cart
<ShoppingCart object (1) "ifeanyi" "234 Haven str., Calgary">

>>> item = ShoppingCartItem(shopping_cart=cart, product=product, quantity=5)
>>> item
<ShoppingCartItem object (None) 5x "Mineral Water Strawberry">
>>> item.save()
>>> item
<ShoppingCartItem object (1) 5x "Mineral Water Strawberry">

>>> serializer = ProductSerializer(product)
>>> serializer
ProductSerializer(<Product object (2) "Mineral Water Strawberry">):
    id = IntegerField(read_only=True)
    name = CharField(max_length=200)
    description = CharField(max_length=200, min_length=2)
    price = FloatField()
    sale_start = DateTimeField(allow_null=True, required=False)
    sale_end = DateTimeField(allow_null=True, required=False)
    is_on_sale = BooleanField(read_only=True)
    current_price = FloatField(read_only=True)
    cart_items = SerializerMethodField()
>>> serializer.data
{'id': 2, 'name': 'Mineral Water Strawberry', 'description': 'Natural-flavored strawberry with an anti-oxidant kick.',
'price': 1.0, 'sale_start': None, 'sale_end': None, 'is_on_sale': False, 'current_price': 1.0, 'cart_items': [{'product': 2, 'quantity': 5}]}

>>> print(json.dumps(serializer.data, indent=2))
{
  "id": 2,
  "name": "Mineral Water Strawberry",
  "description": "Natural-flavored strawberry with an anti-oxidant kick.",
  "price": 1.0,
  "sale_start": null,
  "sale_end": null,
  "is_on_sale": false,
  "current_price": 1.0,
  "cart_items": [
    {
      "product": 2,
      "quantity": 5
    }
  ]
}
```

<img width="1527" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/cab50558-7374-4238-afb4-ab49c101c4ad">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/9b2666a9-9263-498b-b6c4-575289d324ca)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/eb257bd8-04c8-4f41-ad29-8664c7271576)

# #END</details>

<details>
<summary>26. DRF - Serializer with Custom Number Fields </summary>

# DRF - Serializer with Custom Number Fields 

### src-AI-Software/my_projects/03_restful_apls_proj/store/serializers.py:

```py
from rest_framework import serializers

from store.models import Product, ShoppingCartItem


class CartItemSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(min_value=1, max_value=100)

    class Meta:
        model = ShoppingCartItem
        fields = ('product', 'quantity')


class ProductSerializer(serializers.ModelSerializer):
    is_on_sale = serializers.BooleanField(read_only=True)
    current_price = serializers.FloatField(read_only=True)
    description = serializers.CharField(min_length=2, max_length=200)
    cart_items = serializers.SerializerMethodField()
    # price = serializers.FloatField(min_value=1.00, max_value=100000)
    price = serializers.DecimalField(
        min_value=1.00, max_value=100000,
        max_digits=None, decimal_places=2,
    )

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'description', 'price', 'sale_start', 'sale_end',
            'is_on_sale', 'current_price', 'cart_items',
        )

    def get_cart_items(self, instance):
        items = ShoppingCartItem.objects.filter(product=instance)
        return CartItemSerializer(items, many=True).data

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ('id', 'name', 'description',
#                   'price', 'sale_start', 'sale_end')

#     # add additional custom fields to the serializer.
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         data['is_on_sale'] = instance.is_on_sale()
#         data['current_price'] = instance.current_price()
#         return data

```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/d0b2d82e-dfcc-40f8-b37d-dcd1faaa5b6f)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/86f254ea-4229-49fb-b3a6-e700a4b3aa98)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/6bda82c5-35a6-4e49-99e3-e71539b0f553)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/0e450a2c-bec3-4fe2-afe2-1081db4865a2)

<img width="1483" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/9dbaea4c-cf21-4e10-90c9-0a97a6ebfc7e">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/25afe1fd-d535-435a-a801-7f26d76a01a8)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/847523d7-d88b-409d-910c-4d45f4f2f35c)

# #END</details>

<details>
<summary>27. DRF - Serializer with Custom Date and Time Fields </summary>

# DRF - Serializer with Custom Date and Time Fields

### src-AI-Software/my_projects/03_restful_apls_proj/store/serializers.py:

```py
from rest_framework import serializers

from store.models import Product, ShoppingCartItem


class CartItemSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(min_value=1, max_value=100)

    class Meta:
        model = ShoppingCartItem
        fields = ('product', 'quantity')


class ProductSerializer(serializers.ModelSerializer):
    is_on_sale = serializers.BooleanField(read_only=True)
    current_price = serializers.FloatField(read_only=True)
    description = serializers.CharField(min_length=2, max_length=200)
    cart_items = serializers.SerializerMethodField()
    # price = serializers.FloatField(min_value=1.00, max_value=100000)
    price = serializers.DecimalField(
        min_value=1.00, max_value=100000,
        max_digits=None, decimal_places=2,
    )

    sale_start = serializers.DateTimeField(
        input_formats=['%I:%M %p %d %B %Y'], format=None, allow_null=True,
        help_text='Accepted format is "12:01 PM 16 April 2019"',
        style={'input_type': 'text', 'placeholder': '12:01 AM 28 July 2019'},
    )
    sale_end = serializers.DateTimeField(
        input_formats=['%I:%M %p %d %B %Y'], format=None, allow_null=True,
        help_text='Accepted format is "12:01 PM 16 April 2019"',
        style={'input_type': 'text', 'placeholder': '12:01 AM 28 July 2019'},
    )

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'description', 'price', 'sale_start', 'sale_end',
            'is_on_sale', 'current_price', 'cart_items',
        )

    def get_cart_items(self, instance):
        items = ShoppingCartItem.objects.filter(product=instance)
        return CartItemSerializer(items, many=True).data

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ('id', 'name', 'description',
#                   'price', 'sale_start', 'sale_end')

#     # add additional custom fields to the serializer.
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         data['is_on_sale'] = instance.is_on_sale()
#         data['current_price'] = instance.current_price()
#         return data

```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/62c0411f-50f3-421a-a7e0-35ed13059973)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/9256deb8-af2a-4f50-860f-9c868e2cd2a4)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/afdd71c5-b5aa-4f46-b199-389601111fc9)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/a03f50a2-d873-430b-84d7-afc0ec424bdc)

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/57519e8b-433d-4d15-84b6-95c0d17939ee)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/5812498e-0be1-4b1b-a498-0ce8459e5e46)

<img width="1527" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/1318af90-703b-4016-86a5-37f93b4ed340">

# #END</details>

<details>
<summary>28. DRF - Serializer for Composite Fields (List, dicts and JSON Objects) </summary>

# DRF - Serializer for Composite Fields (List, dicts and JSON Objects)

### src-AI-Software/my_projects/03_restful_apls_proj/store/urls.py:

```py
from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    path('', views.index, name='list-products'),
    path('products/<int:id>/', views.show, name='show-product'),
    path('cart/', views.cart, name='shopping-cart'),
    path('api/v1/products/', api_views.ProductList.as_view()),
    path('api/v1/products/new', api_views.ProductCreate.as_view()),
    path('api/v1/products/<int:id>/destroy',
         api_views.ProductDestroy.as_view()),
    path('api/v1/products/<int:id>/',
         api_views.ProductRetrieveUpdateDestroy.as_view()),
    path('api/v1/products/<int:id>/stats',
         api_views.ProductStats.as_view(),
         ),
]

```

### src-AI-Software/my_projects/03_restful_apls_proj/store/api_views.py:

```py
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, \
    RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.exceptions import ValidationError
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from store.serializers import ProductSerializer, ProductStatSerializer
from store.models import Product


class ProductsPagination(LimitOffsetPagination):
    default_limit = 10  # default limit set of 10 search results per page
    max_limit = 100  # maximum limit set of 100 search results per page by client
    # offset_query_param = 'offset'  # offset query parameter name
    # offset is the number of previous pages to skip


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filterset_fields = ('id', 'name', 'price')
    search_fields = ('name', 'description')
    pagination_class = ProductsPagination

    def get_queryset(self):
        on_sale = self.request.query_params.get('on_sale', None)
        if on_sale is None:
            return super().get_queryset()
        queryset = Product.objects.all()
        if on_sale.lower() == 'true':
            from django.utils import timezone
            now = timezone.now()
            return queryset.filter(
                sale_start__lte=now,
                sale_end__gte=now,
            )
        return queryset


class ProductCreate(CreateAPIView):
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        try:
            price = request.data.get('price')
            if price is not None and float(price) <= 0.0:
                raise ValidationError({'price': 'Must be above $0.00'})
        except ValueError:
            raise ValidationError({'price': 'A valid number is required'})
        return super().create(request, *args, **kwargs)


class ProductDestroy(DestroyAPIView):
    queryset = Product.objects.all()
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        product_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('product_data_{}'.format(product_id))
        return response


class ProductRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    lookup_field = 'id'
    serializer_class = ProductSerializer

    def delete(self, request, *args, **kwargs):
        product_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('product_data_{}'.format(product_id))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            product = response.data
            cache.set('product_data_{}'.format(product['id']), {
                'name': product['name'],
                'description': product['description'],
                'price': product['price'],
            })
        return response


class ProductStats(GenericAPIView):
    lookup_field = 'id'
    serializer_class = ProductStatSerializer
    queryset = Product.objects.all()

    def get(self, request, format=None, id=None):
        obj = self.get_object()
        serializer = ProductStatSerializer({
            'stats': {
                '2019-01-01': [5, 10, 15],
                '2019-01-02': [20, 1, 1],
            }
        })
        return Response(serializer.data)

```

### src-AI-Software/my_projects/03_restful_apls_proj/store/serializers.py:

```py
from rest_framework import serializers

from store.models import Product, ShoppingCartItem


class CartItemSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(min_value=1, max_value=100)

    class Meta:
        model = ShoppingCartItem
        fields = ('product', 'quantity')


class ProductSerializer(serializers.ModelSerializer):
    is_on_sale = serializers.BooleanField(read_only=True)
    current_price = serializers.FloatField(read_only=True)
    description = serializers.CharField(min_length=2, max_length=200)
    cart_items = serializers.SerializerMethodField()
    # price = serializers.FloatField(min_value=1.00, max_value=100000)
    price = serializers.DecimalField(
        min_value=1.00, max_value=100000,
        max_digits=None, decimal_places=2,
    )

    sale_start = serializers.DateTimeField(
        input_formats=['%I:%M %p %d %B %Y'], format=None, allow_null=True,
        help_text='Accepted format is "12:01 PM 16 April 2019"',
        style={'input_type': 'text', 'placeholder': '12:01 AM 28 July 2019'},
    )
    sale_end = serializers.DateTimeField(
        input_formats=['%I:%M %p %d %B %Y'], format=None, allow_null=True,
        help_text='Accepted format is "12:01 PM 16 April 2019"',
        style={'input_type': 'text', 'placeholder': '12:01 AM 28 July 2019'},
    )

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'description', 'price', 'sale_start', 'sale_end',
            'is_on_sale', 'current_price', 'cart_items',
        )

    def get_cart_items(self, instance):
        items = ShoppingCartItem.objects.filter(product=instance)
        return CartItemSerializer(items, many=True).data

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ('id', 'name', 'description',
#                   'price', 'sale_start', 'sale_end')

#     # add additional custom fields to the serializer.
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         data['is_on_sale'] = instance.is_on_sale()
#         data['current_price'] = instance.current_price()
#         return data


class ProductStatSerializer(serializers.Serializer):
    stats = serializers.DictField(
        child=serializers.ListField(
            child=serializers.IntegerField(),
        )
    )

```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/d9af3591-f874-4a01-889b-0d567b1a9a59)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/f8f0f64e-7ce2-4a8f-874d-5f5847e89640)

<img width="1527" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/9a84dff1-996e-476d-8a62-b24e915aa039">
<img width="1527" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/a6409182-3e96-41a4-bc88-a539f8a9e321">
<img width="1527" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/1da344e6-bdcf-4d98-952c-2ad93a8cc0e9">

# #END</details>

<details>
<summary>29. DRF - Serializer for ImageField and FileField </summary>

# DRF - Serializer for ImageField and FileField

### src-AI-Software/my_projects/03_restful_apls_proj/store/serializers.py:

```py
from rest_framework import serializers

from store.models import Product, ShoppingCartItem


class CartItemSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(min_value=1, max_value=100)

    class Meta:
        model = ShoppingCartItem
        fields = ('product', 'quantity')


class ProductSerializer(serializers.ModelSerializer):
    is_on_sale = serializers.BooleanField(read_only=True)
    current_price = serializers.FloatField(read_only=True)
    description = serializers.CharField(min_length=2, max_length=200)
    cart_items = serializers.SerializerMethodField()
    # price = serializers.FloatField(min_value=1.00, max_value=100000)
    price = serializers.DecimalField(
        min_value=1.00, max_value=100000,
        max_digits=None, decimal_places=2,
    )

    sale_start = serializers.DateTimeField(
        input_formats=['%I:%M %p %d %B %Y'], format=None, allow_null=True,
        help_text='Accepted format is "12:01 PM 16 April 2019"',
        style={'input_type': 'text', 'placeholder': '12:01 AM 28 July 2019'},
    )
    sale_end = serializers.DateTimeField(
        input_formats=['%I:%M %p %d %B %Y'], format=None, allow_null=True,
        help_text='Accepted format is "12:01 PM 16 April 2019"',
        style={'input_type': 'text', 'placeholder': '12:01 AM 28 July 2019'},
    )
    photo = serializers.ImageField(default=None)
    warranty = serializers.FileField(write_only=True, default=None)

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'description', 'price', 'sale_start', 'sale_end',
            'is_on_sale', 'current_price', 'cart_items',
            'photo', 'warranty',
        )

    def get_cart_items(self, instance):
        items = ShoppingCartItem.objects.filter(product=instance)
        return CartItemSerializer(items, many=True).data

    def update(self, instance, validated_data):
        if validated_data.get('warranty', None):
            instance.description += '\n\nWarranty Information:\n'
            instance.description += b'; '.join(
                validated_data['warranty'].readlines()
            ).decode()
        return instance

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ('id', 'name', 'description',
#                   'price', 'sale_start', 'sale_end')

#     # add additional custom fields to the serializer.
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         data['is_on_sale'] = instance.is_on_sale()
#         data['current_price'] = instance.current_price()
#         return data


class ProductStatSerializer(serializers.Serializer):
    stats = serializers.DictField(
        child=serializers.ListField(
            child=serializers.IntegerField(),
        )
    )

```

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/5b3089cb-7762-4d3f-8523-90120f68115e)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/77e7ab13-4cca-41fa-8808-99db7f28ca0f)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/0c1aff10-7e93-4e7c-88e8-66ebaf8b5f94)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/0fbd8885-bb9e-4662-957e-616e379d58a6)

<img width="1385" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/aeedbfff-0456-4315-8fc7-b68b8fec2c96">

# #END</details>

<details>
<summary>30. DRF API UnitTesting - TestCase for CreateAPIView  </summary>

# DRF API UnitTesting - TestCase for CreateAPIView

### src-AI-Software/my_projects/03_restful_apls_proj/store/serializers.py:

```py
from rest_framework import serializers

from store.models import Product, ShoppingCartItem


class CartItemSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(min_value=1, max_value=100)

    class Meta:
        model = ShoppingCartItem
        fields = ('product', 'quantity')


class ProductSerializer(serializers.ModelSerializer):
    is_on_sale = serializers.BooleanField(read_only=True)
    current_price = serializers.FloatField(read_only=True)
    description = serializers.CharField(min_length=2, max_length=200)
    cart_items = serializers.SerializerMethodField()
    # price = serializers.FloatField(min_value=1.00, max_value=100000)
    price = serializers.DecimalField(
        min_value=1.00, max_value=100000,
        max_digits=None, decimal_places=2,
    )

    sale_start = serializers.DateTimeField(
        required=False,
        input_formats=['%I:%M %p %d %B %Y'], format=None, allow_null=True,
        help_text='Accepted format is "12:01 PM 16 April 2019"',
        style={'input_type': 'text', 'placeholder': '12:01 AM 28 July 2019'},
    )
    sale_end = serializers.DateTimeField(
        required=False,
        input_formats=['%I:%M %p %d %B %Y'], format=None, allow_null=True,
        help_text='Accepted format is "12:01 PM 16 April 2019"',
        style={'input_type': 'text', 'placeholder': '12:01 AM 28 July 2019'},
    )
    photo = serializers.ImageField(default=None)
    warranty = serializers.FileField(write_only=True, default=None)

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'description', 'price', 'sale_start', 'sale_end',
            'is_on_sale', 'current_price', 'cart_items',
            'photo', 'warranty',
        )

    def get_cart_items(self, instance):
        items = ShoppingCartItem.objects.filter(product=instance)
        return CartItemSerializer(items, many=True).data

    def update(self, instance, validated_data):
        if validated_data.get('warranty', None):
            instance.description += '\n\nWarranty Information:\n'
            instance.description += b'; '.join(
                validated_data['warranty'].readlines()
            ).decode()
        return instance

    def create(self, validated_data):
        validated_data.pop('warranty')
        return Product.objects.create(**validated_data)


class ProductStatSerializer(serializers.Serializer):
    stats = serializers.DictField(
        child=serializers.ListField(
            child=serializers.IntegerField(),
        )
    )

```

### src-AI-Software/my_projects/03_restful_apls_proj/store/tests.py:

```py
# from django.test import TestCase
from rest_framework.test import APITestCase

from store.models import Product


class ProductCreateTestCase(APITestCase):
    def test_create_product(self):
        # Get the Total number of created Products
        initial_product_count = Product.objects.count()

        # Create a new Product
        product_attrs = {
            'name': 'New Product',
            'description': 'Awesome product',
            'price': '123.45',
        }

        # Send a POST request to the ProductCreate API endpoint
        response = self.client.post('/api/v1/products/new', product_attrs)
        if response.status_code != 201:
            print(response.data)

        # Check that the Product was created successfully
        self.assertEqual(
            Product.objects.count(),
            initial_product_count + 1,
        )

        # Check that the Product was created with the correct attributes
        for attr, expected_value in product_attrs.items():
            self.assertEqual(response.data[attr], expected_value)

        # Check that the Product was created with the correct Custom Field attributes for is_on_sale and current_price
        self.assertEqual(response.data['is_on_sale'], False)
        self.assertEqual(
            response.data['current_price'],
            float(product_attrs['price']),
        )

```

<img width="1502" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/9052973f-eb99-4260-960d-f7d4d6fda671">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/23e92676-bda7-4210-99cf-2591fcbe8608)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/4063637a-fd06-4802-b9be-bc81c3610122)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/5b4dda46-8622-449c-9b3f-db823a7a57bf)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/62c14fa9-a1d7-41e7-b9b6-7c068d23cfe0)

# #END</details>

<details>
<summary>31. DRF API UnitTesting - TestCase for DestroyAPIView  </summary>

# DRF API UnitTesting - TestCase for DestroyAPIView

### src-AI-Software/my_projects/03_restful_apls_proj/store/tests.py:

```py
# from django.test import TestCase
from rest_framework.test import APITestCase

from store.models import Product


class ProductCreateTestCase(APITestCase):
    def test_create_product(self):
        # Get the Total number of created Products
        initial_product_count = Product.objects.count()

        # Create a new Product
        product_attrs = {
            'name': 'New Product',
            'description': 'Awesome product',
            'price': '123.45',
        }

        # Send a POST request to the ProductCreate API endpoint
        response = self.client.post('/api/v1/products/new', product_attrs)
        if response.status_code != 201:
            print(response.data)

        # Check that the Product was created successfully
        self.assertEqual(
            Product.objects.count(),
            initial_product_count + 1,
        )

        # Check that the Product was created with the correct attributes
        for attr, expected_value in product_attrs.items():
            self.assertEqual(response.data[attr], expected_value)

        # Check that the Product was created with the correct Custom Field attributes for is_on_sale and current_price
        self.assertEqual(response.data['is_on_sale'], False)
        self.assertEqual(
            response.data['current_price'],
            float(product_attrs['price']),
        )


class ProductDestroyTestCase(APITestCase):
    def test_delete_product(self):
        # Get the Total number of created Products
        initial_product_count = Product.objects.count()

        # Create a new Product
        product_attrs = {
            'name': 'New Product',
            'description': 'Awesome product',
            'price': '123.45',
        }
        # Send a POST request to the ProductCreate API endpoint
        response = self.client.post('/api/v1/products/new', product_attrs)
        if response.status_code != 201:
            print(response.data)

        # Get the first created Product
        product_id = Product.objects.first().id
        # print(product_id)

        # Send a DELETE request to the ProductDestroyAPI endpoint
        self.client.delete('/api/v1/products/{}/destroy'.format(product_id))

        # Check that the Product was deleted successfully
        self.assertEqual(
            Product.objects.count(),
            initial_product_count,
        )

        # Check that the Product was deleted from the database
        self.assertRaises(
            Product.DoesNotExist,
            Product.objects.get, id=product_id,
        )

```

<img width="1502" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/ddf243aa-c5ce-46d2-b57f-216e358dab1d">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/a2a866e8-49a5-4a0c-824f-ae647ff4b647)

# #END</details>

<details>
<summary>32. DRF API UnitTesting - TestCase for ListAPIView  </summary>

# DRF API UnitTesting - TestCase for ListAPIView

### src-AI-Software/my_projects/03_restful_apls_proj/Exercise Files/04_03_end/demo/store/tests.py:

```py
from rest_framework.test import APITestCase

from store.models import Product

class ProductCreateTestCase(APITestCase):
    def test_create_product(self):
        initial_product_count = Product.objects.count()
        product_attrs = {
            'name': 'New Product',
            'description': 'Awesome product',
            'price': '123.45',
        }
        response = self.client.post('/api/v1/products/new', product_attrs)
        if response.status_code != 201:
            print(response.data)
        self.assertEqual(
            Product.objects.count(),
            initial_product_count + 1,
        )
        for attr, expected_value in product_attrs.items():
            self.assertEqual(response.data[attr], expected_value)
        self.assertEqual(response.data['is_on_sale'], False)
        self.assertEqual(
            response.data['current_price'],
            float(product_attrs['price']),
        )

class ProductDestroyTestCase(APITestCase):
    def test_delete_product(self):
        initial_product_count = Product.objects.count()
        product_id = Product.objects.first().id
        self.client.delete('/api/v1/products/{}/'.format(product_id))
        self.assertEqual(
            Product.objects.count(),
            initial_product_count - 1,
        )
        self.assertRaises(
            Product.DoesNotExist,
            Product.objects.get, id=product_id,
        )

class ProductListTestCase(APITestCase):
    def test_list_products(self):
        products_count = Product.objects.count()
        response = self.client.get('/api/v1/products/')
        self.assertIsNone(response.data['next'])
        self.assertIsNone(response.data['previous'])
        self.assertEqual(response.data['count'], products_count)
        self.assertEqual(len(response.data['results']), products_count)

```

<img width="1502" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/3ae1855c-a0bc-46ed-b8df-2d211d902d53">

# #END</details>

<details>
<summary>33. DRF API UnitTesting - TestCase for UpdateAPIView  </summary>

# DRF API UnitTesting - TestCase for UpdateAPIView

### src-AI-Software/my_projects/03_restful_apls_proj/store/serializers.py:

```py
from rest_framework import serializers

from store.models import Product, ShoppingCartItem


class CartItemSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(min_value=1, max_value=100)

    class Meta:
        model = ShoppingCartItem
        fields = ('product', 'quantity')


class ProductSerializer(serializers.ModelSerializer):
    is_on_sale = serializers.BooleanField(read_only=True)
    current_price = serializers.FloatField(read_only=True)
    description = serializers.CharField(min_length=2, max_length=200)
    cart_items = serializers.SerializerMethodField()
    # price = serializers.FloatField(min_value=1.00, max_value=100000)
    price = serializers.DecimalField(
        min_value=1.00, max_value=100000,
        max_digits=None, decimal_places=2,
    )

    sale_start = serializers.DateTimeField(
        required=False,
        input_formats=['%I:%M %p %d %B %Y'], format=None, allow_null=True,
        help_text='Accepted format is "12:01 PM 16 April 2019"',
        style={'input_type': 'text', 'placeholder': '12:01 AM 28 July 2019'},
    )
    sale_end = serializers.DateTimeField(
        required=False,
        input_formats=['%I:%M %p %d %B %Y'], format=None, allow_null=True,
        help_text='Accepted format is "12:01 PM 16 April 2019"',
        style={'input_type': 'text', 'placeholder': '12:01 AM 28 July 2019'},
    )
    photo = serializers.ImageField(default=None)
    warranty = serializers.FileField(write_only=True, default=None)

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'description', 'price', 'sale_start', 'sale_end',
            'is_on_sale', 'current_price', 'cart_items',
            'photo', 'warranty',
        )

    def get_cart_items(self, instance):
        items = ShoppingCartItem.objects.filter(product=instance)
        return CartItemSerializer(items, many=True).data

    def update(self, instance, validated_data):
        if validated_data.get('warranty', None):
            instance.description += '\n\nWarranty Information:\n'
            instance.description += b'; '.join(
                validated_data['warranty'].readlines()
            ).decode()
        # return instance
        return super().update(instance, validated_data)

    def create(self, validated_data):
        validated_data.pop('warranty')
        return Product.objects.create(**validated_data)


class ProductStatSerializer(serializers.Serializer):
    stats = serializers.DictField(
        child=serializers.ListField(
            child=serializers.IntegerField(),
        )
    )

```

### src-AI-Software/my_projects/03_restful_apls_proj/store/tests.py:

```py
# from django.test import TestCase
from rest_framework.test import APITestCase

from store.models import Product


class ProductCreateTestCase(APITestCase):
    def test_create_product(self):
        # Get the Total number of created Products
        initial_product_count = Product.objects.count()

        # Create a new Product
        product_attrs = {
            'name': 'New Product',
            'description': 'Awesome product',
            'price': '123.45',
        }

        # Send a POST request to the ProductCreate API endpoint
        response = self.client.post('/api/v1/products/new', product_attrs)
        if response.status_code != 201:
            print(response.data)

        # Check that the Product was created successfully
        self.assertEqual(
            Product.objects.count(),
            initial_product_count + 1,
        )

        # Check that the Product was created with the correct attributes
        for attr, expected_value in product_attrs.items():
            self.assertEqual(response.data[attr], expected_value)

        # Check that the Product was created with the correct Custom Field attributes for is_on_sale and current_price
        self.assertEqual(response.data['is_on_sale'], False)
        self.assertEqual(
            response.data['current_price'],
            float(product_attrs['price']),
        )


class ProductDestroyTestCase(APITestCase):
    def test_delete_product(self):
        # Get the Total number of created Products
        initial_product_count = Product.objects.count()

        # Create a new Product
        product_attrs = {
            'name': 'New Product',
            'description': 'Awesome product',
            'price': '123.45',
        }
        # Send a POST request to the ProductCreate API endpoint
        response = self.client.post('/api/v1/products/new', product_attrs)
        if response.status_code != 201:
            print(response.data)

        # Get the first created Product
        product_id = Product.objects.first().id
        # print(product_id)

        # Send a DELETE request to the ProductDestroyAPI endpoint
        self.client.delete('/api/v1/products/{}/destroy'.format(product_id))

        # Check that the Product was deleted successfully
        self.assertEqual(
            Product.objects.count(),
            initial_product_count,
        )

        # Check that the Product was deleted from the database
        self.assertRaises(
            Product.DoesNotExist,
            Product.objects.get, id=product_id,
        )


class ProductListTestCase(APITestCase):
    def test_list_products(self):
        products_count = Product.objects.count()
        response = self.client.get('/api/v1/products/')
        self.assertIsNone(response.data['next'])
        self.assertIsNone(response.data['previous'])
        self.assertEqual(response.data['count'], products_count)
        self.assertEqual(len(response.data['results']), products_count)


class ProductUpdateTestCase(APITestCase):
    def test_update_product(self):
        # Create a new Product
        product_attrs = {
            'name': 'New Product',
            'description': 'Awesome product',
            'price': '123.45',
        }
        # Send a POST request to the ProductCreate API endpoint
        response = self.client.post('/api/v1/products/new', product_attrs)
        if response.status_code != 201:
            print(response.data)

        product = Product.objects.first()
        response = self.client.patch(
            '/api/v1/products/{}/'.format(product.id),
            {
                'name': 'New Product',
                'description': 'Awesome product',
                'price': 123.45,
            },
            format='json',
        )
        updated = Product.objects.get(id=product.id)
        self.assertEqual(updated.name, 'New Product')

```

<img width="1502" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/caed6e32-2671-4990-81f3-f40803fb1c30">

# #END</details>

<details>
<summary>34. DRF API UnitTesting - TestCase for Handling Image Uploads </summary>

# DRF API UnitTesting - TestCase for Handling Image Uploads

### src-AI-Software/my_projects/03_restful_apls_proj/store/tests.py:

```py
import os.path
from django.conf import settings

# from django.test import TestCase

from rest_framework.test import APITestCase

from store.models import Product


class ProductCreateTestCase(APITestCase):
    def test_create_product(self):
        # Get the Total number of created Products
        initial_product_count = Product.objects.count()

        # Create a new Product
        product_attrs = {
            'name': 'New Product',
            'description': 'Awesome product',
            'price': '123.45',
        }

        # Send a POST request to the ProductCreate API endpoint
        response = self.client.post('/api/v1/products/new', product_attrs)
        if response.status_code != 201:
            print(response.data)

        # Check that the Product was created successfully
        self.assertEqual(
            Product.objects.count(),
            initial_product_count + 1,
        )

        # Check that the Product was created with the correct attributes
        for attr, expected_value in product_attrs.items():
            self.assertEqual(response.data[attr], expected_value)

        # Check that the Product was created with the correct Custom Field attributes for is_on_sale and current_price
        self.assertEqual(response.data['is_on_sale'], False)
        self.assertEqual(
            response.data['current_price'],
            float(product_attrs['price']),
        )


class ProductDestroyTestCase(APITestCase):
    def test_delete_product(self):
        # Get the Total number of created Products
        initial_product_count = Product.objects.count()

        # Create a new Product
        product_attrs = {
            'name': 'New Product',
            'description': 'Awesome product',
            'price': '123.45',
        }
        # Send a POST request to the ProductCreate API endpoint
        response = self.client.post('/api/v1/products/new', product_attrs)
        if response.status_code != 201:
            print(response.data)

        # Get the first created Product
        product_id = Product.objects.first().id
        # print(product_id)

        # Send a DELETE request to the ProductDestroyAPI endpoint
        self.client.delete('/api/v1/products/{}/destroy'.format(product_id))

        # Check that the Product was deleted successfully
        self.assertEqual(
            Product.objects.count(),
            initial_product_count,
        )

        # Check that the Product was deleted from the database
        self.assertRaises(
            Product.DoesNotExist,
            Product.objects.get, id=product_id,
        )


class ProductListTestCase(APITestCase):
    def test_list_products(self):
        products_count = Product.objects.count()
        response = self.client.get('/api/v1/products/')
        self.assertIsNone(response.data['next'])
        self.assertIsNone(response.data['previous'])
        self.assertEqual(response.data['count'], products_count)
        self.assertEqual(len(response.data['results']), products_count)


class ProductUpdateTestCase(APITestCase):
    def test_update_product(self):
        # Create a new Product
        product_attrs = {
            'name': 'New Product',
            'description': 'Awesome product',
            'price': '123.45',
        }
        # Send a POST request to the ProductCreate API endpoint
        response = self.client.post('/api/v1/products/new', product_attrs)
        if response.status_code != 201:
            print(response.data)

        product = Product.objects.first()
        response = self.client.patch(
            '/api/v1/products/{}/'.format(product.id),
            {
                'name': 'New Product',
                'description': 'Awesome product',
                'price': 123.45,
            },
            format='json',
        )
        updated = Product.objects.get(id=product.id)
        self.assertEqual(updated.name, 'New Product')

   def test_upload_product_photo(self):
        product = Product.objects.first()
        original_photo = product.photo

        photo_path = os.path.join(
            settings.MEDIA_ROOT, 'products', 'vitamin-iron.jpg')

        with open(photo_path, 'rb') as photo_data:
            response = self.client.patch('/api/v1/products/{}/'.format(product.id), {
                'photo': photo_data,
            }, format='multipart')

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data['photo'], original_photo)

        try:
            updated = Product.objects.get(id=product.id)
            expected_photo = os.path.join(
                settings.MEDIA_ROOT, 'products', 'vitamin-iron')
            self.assertTrue(updated.photo.path.startswith(expected_photo))
        finally:
            os.remove(updated.photo.path)
```

<img width="1502" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/fecc8b52-3fba-4202-86ab-49a977d11086">


# #END</details>

# #END
