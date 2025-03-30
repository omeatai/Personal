
## +LinkedIn - Django Forms

## [COURSE](https://www.linkedin.com/learning/django-forms/deep-dive-into-django-forms)

<details>
<summary>1. Creating a New Django Project </summary>

# Creating a New Django Project

## Install venv

```py
python -m venv myproject-env

pip install virtualenv
virtualenv myproject-env
```

## Activate venv

```py
# myproject-env\Scripts\activate
source myproject-env/bin/activate
```

## Install Django

```py
python -m pip install Django

pip install Django
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
django-admin startproject anyisgarden .
```

## Start Local Server

```py
python manage.py runserver
```

```x
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
March 20, 2024 - 04:58:12
Django version 5.0.3, using settings 'smartnotes.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

# #END</details>

<details>
<summary>2. Create new App - Pizza </summary>

# Create new App - Pizza

[https://github.com/omeatai/src-python-flask-django/commit/df963c5ff37c50149f4ed82e4bca7451d4d0f71c](https://github.com/omeatai/src-python-flask-django/commit/df963c5ff37c50149f4ed82e4bca7451d4d0f71c)

```py
django-admin startapp pizza
```

<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/83f17f2c-e00f-4154-a02e-3812f7ed11b6">

# #END</details>

<details>
<summary>3. Create Homepage and Order Page </summary>

# Create Homepage and Order Page

[https://github.com/omeatai/src-python-flask-django/commit/c5141aba40c0f8e13be4e8cf1bc081aeec1810e4](https://github.com/omeatai/src-python-flask-django/commit/c5141aba40c0f8e13be4e8cf1bc081aeec1810e4)

### anyisgarden.settings:

```py
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pizza',
]

```

### anyisgarden.urls:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pizza.urls')),
]

```

### pizza.urls:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('order', views.order, name='order'),
]

```

### pizza.views:

```py
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    return render(request, 'pizza/order.html')

```

### src-python/linkedin/django-forms/pizza/templates/pizza/home.html:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Anyi's garden</title>
</head>

<body>
    <h1>Anyi's Garden</h1>
    <a href="{% url 'order' %}">Order a pizza</a>
</body>

</html>
```

### src-python/linkedin/django-forms/pizza/templates/pizza/order.html:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Order a Pizza</title>
</head>

<body>
    <h1>Order Pizza Form</h1>
</body>

</html>
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/839178ea-5101-492f-a904-f57f2678c8c5)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/138eca54-b81b-457b-b5b7-e0ba9d190809)

<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1c063cc4-0a77-492b-b172-5bc91d089b6b">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/41e065ce-2c52-4922-bef0-b51ed2b2e6f7">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/947ff739-77c8-4e6d-b20b-5aeff3081743">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e4df8a46-dadf-42af-b33a-a2cff102716b">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/8a90fcba-2eab-4e35-b581-29e79a81c208">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/cd994088-56f5-4d8e-8c87-79490dfd0202">

# #END</details>

<details>
<summary>4. Create Form Fields </summary>

# Create Form Fields

[https://github.com/omeatai/src-python-flask-django/commit/c736d189596b7caa3597f762b1afbe344912c42b](https://github.com/omeatai/src-python-flask-django/commit/c736d189596b7caa3597f762b1afbe344912c42b)

### src-python/linkedin/django-forms/pizza/templates/pizza/order.html:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Order a Pizza</title>
</head>

<body>
    <h1>Order Pizza Form</h1>

    <form>
        <div>
            <label for="topping1">Topping 1: </label>
            <input type="text" id="topping1" name="topping1">
            <label for="topping2">Topping 2: </label>
            <input type="text" id="topping2" name="topping2">
            <label for="size">Size: </label>
            <select name="size" id="size">
                <option value="small">Small</option>
                <option value="medium">Medium</option>
                <option value="large">Large</option>
            </select>
        </div>
    </form>
</body>

</html>
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/a0e9d418-23bb-438c-b6cf-d6462fd2ac63)

<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/eea37d7a-f6a2-4954-84c3-5c9ab5530bc0">

# #END</details>

<details>
<summary>5. Submitting Forms </summary>

# Submitting Forms

### src-python/linkedin/django-forms/pizza/templates/pizza/order.html:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Order a Pizza</title>
</head>

<body>
    <h1>Order Pizza Form</h1>

    <form action="{% url 'order' %}" method="post">
        {% csrf_token %}
        <div>
            <label for="topping1">Topping 1: </label>
            <input type="text" id="topping1" name="topping1">
            <label for="topping2">Topping 2: </label>
            <input type="text" id="topping2" name="topping2">
            <label for="size">Size: </label>
            <select name="size" id="size">
                <option value="small">Small</option>
                <option value="medium">Medium</option>
                <option value="large">Large</option>
            </select>
            <input type="submit" value="Order Pizza">
        </div>
    </form>
</body>

</html>
```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b5bb0727-f8c9-4e0a-8634-430117c3ea55">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/6a19534c-52c2-4c58-a57d-c3c4c5ebbc3f">

# #END</details>

<details>
<summary>6. Django Form Class </summary>

# Django Form Class

[https://github.com/omeatai/src-python-flask-django/commit/aac29045cc48a4a8130804c301196727c6076ccf](https://github.com/omeatai/src-python-flask-django/commit/aac29045cc48a4a8130804c301196727c6076ccf)

### pizza.forms:

```py
from django import forms


CHOICES = [('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')]


class PizzaForm(forms.Form):
    topping1 = forms.CharField(label='Topping 1', max_length=100)
    topping2 = forms.CharField(label='Topping 2', max_length=100)
    size = forms.ChoiceField(label='Size', choices=CHOICES)

```

### pizza.views:

```py
from django.shortcuts import render
from .forms import PizzaForm
# Create your views here.


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    form = PizzaForm()
    return render(request, 'pizza/order.html', {'form': form})

```

### src-python/linkedin/django-forms/pizza/templates/pizza/order.html:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Order a Pizza</title>
</head>

<body>
    <h1>Order Pizza Form</h1>

    <form action="{% url 'order' %}" method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Order Pizza">

        {% comment %} <div>
            <label for="topping1">Topping 1: </label>
            <input type="text" id="topping1" name="topping1">
            <label for="topping2">Topping 2: </label>
            <input type="text" id="topping2" name="topping2">
            <label for="size">Size: </label>
            <select name="size" id="size">
                <option value="small">Small</option>
                <option value="medium">Medium</option>
                <option value="large">Large</option>
            </select>
            <input type="submit" value="Order Pizza">
        </div> {% endcomment %}
    </form>
</body>

</html>

```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/8e3ec26a-ff38-406c-9876-71aa31cf2ceb">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a660edbe-8b71-49c4-a9e3-48ff05d1aa0d">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/963c5324-57b2-4428-8a6c-eb7055364908">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e972105a-a753-4b41-b065-5348fef9a26e">

# #END</details>

<details>
<summary>7. Using Submitted Data </summary>

# Using Submitted Data

[https://github.com/omeatai/src-python-flask-django/commit/fb0f8ea1b17786714e1a30a1e9fbb44c801276c7](https://github.com/omeatai/src-python-flask-django/commit/fb0f8ea1b17786714e1a30a1e9fbb44c801276c7)

### pizza.forms:

```py
from django import forms


CHOICES = [('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')]


class PizzaForm(forms.Form):
    topping1 = forms.CharField(label='Topping 1', max_length=100)
    topping2 = forms.CharField(label='Topping 2', max_length=100)
    size = forms.ChoiceField(label='Size', choices=CHOICES)

```

### pizza.views:

```py
from django.shortcuts import render
from .forms import PizzaForm
# Create your views here.


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            size = filled_form.cleaned_data['size']
            topping1 = filled_form.cleaned_data['topping1']
            topping2 = filled_form.cleaned_data['topping2']
            # note = f"Thanks for ordering! Your {size} pizza with {topping1} and {topping2} is on its way!"
            note = "Thanks for ordering! Your %s Pizza with %s and %s is on its way!" % (
                size, topping1, topping2)
            empty_form = PizzaForm()
            return render(request, 'pizza/order.html', {'form': empty_form, 'note': note})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'form': form})

```

### src-python/linkedin/django-forms/pizza/templates/pizza/order.html:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Order a Pizza</title>
</head>

<body>
    <h1>Order Pizza Form</h1>

    {% if note %}
    <h2 style="color: green;">{{ note }}</h2>
    {% endif %}

    <form action="{% url 'order' %}" method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Order Pizza">

    </form>
</body>

</html>
```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/21c1e785-3929-4076-89b5-df14c7ef6fe5">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/bcac377d-c2b0-41fe-b847-fe396890eafe">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/4dcc8164-592a-47dd-aed9-de696bedf658">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/547c4336-44cf-4724-a8db-2aadc808bab5">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/88dd2d26-aaf0-4004-b0dc-d7afed925ad3">

# #END</details>

<details>
<summary>8. Creating Models for Form </summary>

# Creating Models for Form

[https://github.com/omeatai/src-python-flask-django/commit/f89abad1ceb7bee49234637369082b023fa5ebf8](https://github.com/omeatai/src-python-flask-django/commit/f89abad1ceb7bee49234637369082b023fa5ebf8)

## Make Migrations 

```py
python manage.py makemigrations
python manage.py migrate
```

## Create Super User

```py
python manage.py createsuperuser
```

## Run Development Server

```py
python manage.py runserver
```

### pizza.forms:

```py
from django import forms


CHOICES = [('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')]


class PizzaForm(forms.Form):
    topping1 = forms.CharField(label='Topping 1', max_length=100)
    topping2 = forms.CharField(label='Topping 2', max_length=100)
    size = forms.ChoiceField(label='Size', choices=CHOICES)

```

### pizza.models:

```py
from django.db import models

# Create your models here.


class Size(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Pizza(models.Model):
    topping1 = models.CharField(max_length=100)
    topping2 = models.CharField(max_length=100)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

```

### pizza.admin:

```py
from django.contrib import admin
from .models import Size, Pizza
# Register your models here.

admin.site.register(Size)
admin.site.register(Pizza)

```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/02333abe-6f41-4ee2-98e8-5f670116a8c3">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a96685b8-a537-4d13-9086-8e155e36e076">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/df10d946-508c-42f7-87d1-cb9d34f0be74">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/c2d5e5a5-e994-4c4f-ad81-533753fdc4d1">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/0ce4832c-1485-409b-8f17-97ca24a61aa0">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/7373b861-af9b-470c-9c7b-a34935550018">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/8c8450d9-abd9-4b6a-b067-6b7a18d8efe5">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/92e1f04a-34e1-49db-8198-16b421312c28">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/864babcc-7712-4223-a852-e6508b215e90">

<img width="574" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/45d5e1ae-394e-48d4-b118-99fe34aa6540">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/c4077616-46e0-4c94-bdc4-d43c65d0c5db">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/7b90815a-73c2-47f5-abf7-41e7525a7e95">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/6645dc42-e412-47f9-94ed-4326c01d3541">

# #END</details>

<details>
<summary>9. Using Model Forms </summary>

# Using Model Forms

[https://github.com/omeatai/src-python-flask-django/commit/db771cdf8a0227c81712ed81236793b2866aff0d](https://github.com/omeatai/src-python-flask-django/commit/db771cdf8a0227c81712ed81236793b2866aff0d)

### pizza.models:

```py
from django.db import models

# Create your models here.


class Size(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Pizza(models.Model):
    topping1 = models.CharField(max_length=100)
    topping2 = models.CharField(max_length=100)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

```

### pizza.forms:

```py
from django import forms
from .models import Pizza

# CHOICES = [('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')]


# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label='Topping 1', max_length=100)
#     topping2 = forms.CharField(label='Topping 2', max_length=100)
#     size = forms.ChoiceField(label='Size', choices=CHOICES)

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {
            'topping1': 'Topping 1',
            'topping2': 'Topping 2',
            'size': 'Size',
        }

```

### pizza.views:

```py
from django.shortcuts import render
from .forms import PizzaForm
# Create your views here.


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            size = filled_form.cleaned_data['size']
            topping1 = filled_form.cleaned_data['topping1']
            topping2 = filled_form.cleaned_data['topping2']
            # note = f"Thanks for ordering! Your {size} pizza with {topping1} and {topping2} is on its way!"
            note = "Thanks for ordering! Your %s Pizza with %s and %s is on its way!" % (
                size, topping1, topping2)
            empty_form = PizzaForm()
            return render(request, 'pizza/order.html', {'form': empty_form, 'note': note})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'form': form})

```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e7b73289-e729-424e-86a8-089afc7850d1">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/e8a819a6-7d5e-486d-aead-d06369416097">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/58b91581-64bd-4f81-bfbd-390921624929">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a6680012-2f05-4e7a-bdc6-63cda3dae49d">

# #END</details>

<details>
<summary>10. Using Basic Widgets </summary>

# Using Basic Widgets

[https://github.com/omeatai/src-python-flask-django/commit/eec165edc52314c140f3851a194e3fbea367a04b](https://github.com/omeatai/src-python-flask-django/commit/eec165edc52314c140f3851a194e3fbea367a04b)

### pizza.forms:

```py
from django import forms
from .models import Pizza

CHOICES = [('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')]
TOPPING_CHOICES = [('pep', 'Pepperoni'), ('cheese',
                                          'Cheese'), ('olives', 'Olives')]


class PizzaForm(forms.Form):
    topping_1 = forms.CharField(label='Topping_1', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    topping_2 = forms.CharField(label='Topping_2', max_length=100, widget=forms.Textarea(
        attrs={'class': 'form-control'}))
    topping_3 = forms.CharField(
        label='Topping_3', max_length=100, widget=forms.PasswordInput)
    topping_4 = forms.MultipleChoiceField(
        label='Topping_4', choices=TOPPING_CHOICES)
    topping_5 = forms.MultipleChoiceField(
        label='Topping_5', choices=TOPPING_CHOICES, widget=forms.CheckboxSelectMultiple)

    topping1 = forms.CharField(label='Topping 1', max_length=100)
    topping2 = forms.CharField(label='Topping 2', max_length=100)
    size = forms.ChoiceField(label='Size', choices=CHOICES)

# class PizzaForm(forms.ModelForm):
#     class Meta:
#         model = Pizza
#         fields = ['topping1', 'topping2', 'size']
#         labels = {
#             'topping1': 'Topping 1',
#             'topping2': 'Topping 2',
#             'size': 'Size',
#         }

```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/023aeeb7-b388-488a-a8d7-70138f882e95">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/24c89464-963d-492e-8f96-1c0e241388fd">

# #END</details>

<details>
<summary>11. Using Widgets for Model Form </summary>

# Using Widgets for Model Form

[https://github.com/omeatai/src-python-flask-django/commit/9d3d91c02d14ecab171e51fb4410f5f81cefa426](https://github.com/omeatai/src-python-flask-django/commit/9d3d91c02d14ecab171e51fb4410f5f81cefa426)

### pizza.forms:

```py
from django import forms
from .models import Pizza, Size

CHOICES = [('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')]
TOPPING_CHOICES = [('pep', 'Pepperoni'), ('cheese',
                                          'Cheese'), ('olives', 'Olives')]


# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label='Topping 1', max_length=100)
#     topping2 = forms.CharField(label='Topping 2', max_length=100)
#     size = forms.ChoiceField(label='Size', choices=CHOICES)

class PizzaForm(forms.ModelForm):

    size = forms.ModelChoiceField(
        # queryset=Size.objects.all(), to_field_name='title', empty_label=None, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}))
        queryset=Size.objects.all(), to_field_name='title', empty_label=None, widget=forms.RadioSelect(attrs={'class': 'form-control'}))

    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {
            'topping1': 'Topping 1',
            'topping2': 'Topping 2',
            'size': 'Size',
        }

        # widgets = {
        #     'topping1': forms.TextInput(attrs={'class': 'form-control'}),
        #     'topping2': forms.TextInput(attrs={'class': 'form-control'}),
        #     'size': forms.Select(attrs={'class': 'form-control'}),
        # }

        # widgets = {
        #     'topping1': forms.Textarea(attrs={'class': 'form-control'}),
        #     'topping2': forms.TextInput(attrs={'class': 'form-control'}),
        #     'size': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        # }

```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/fea26596-9a4b-45d7-8435-212a3e1edd8c">
<img width="1464" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/b82bf792-bb2f-47b2-89a9-72336bdd7460">

# #END</details>

<details>
<summary>12. Adding Files to Forms </summary>

# Adding Files to Forms

[https://github.com/omeatai/src-python-flask-django/commit/b507f6a78c7d9e2ab0f26dd8aa0426caf39d8f70](https://github.com/omeatai/src-python-flask-django/commit/b507f6a78c7d9e2ab0f26dd8aa0426caf39d8f70)

## Install Pillow:

```py
pip install pillow
```

### pizza.views:

```py
from django.shortcuts import render
from .forms import PizzaForm
# Create your views here.


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, request.FILES)
        if filled_form.is_valid():
            size = filled_form.cleaned_data['size']
            topping1 = filled_form.cleaned_data['topping1']
            topping2 = filled_form.cleaned_data['topping2']
            # note = f"Thanks for ordering! Your {size} pizza with {topping1} and {topping2} is on its way!"
            note = "Thanks for ordering! Your %s Pizza with %s and %s is on its way!" % (
                size, topping1, topping2)
            empty_form = PizzaForm()
            return render(request, 'pizza/order.html', {'form': empty_form, 'note': note})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'form': form})

```

### pizza.forms:

```py
from django import forms
from .models import Pizza, Size

CHOICES = [('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')]
TOPPING_CHOICES = [('pep', 'Pepperoni'), ('cheese',
                                          'Cheese'), ('olives', 'Olives')]


# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label='Topping 1', max_length=100)
#     topping2 = forms.CharField(label='Topping 2', max_length=100)
#     size = forms.ChoiceField(label='Size', choices=CHOICES)

class PizzaForm(forms.ModelForm):

    image = forms.ImageField(label='Image', required=False)

    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {
            'topping1': 'Topping 1',
            'topping2': 'Topping 2',
            'size': 'Size',
        }

        widgets = {
            'topping1': forms.TextInput(attrs={'class': 'form-control'}),
            'topping2': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.RadioSelect(attrs={'class': 'form-control'}),
        }

```

### src-python/linkedin/django-forms/pizza/templates/pizza/order.html:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Order a Pizza</title>
</head>

<body>
    <h1>Order Pizza Form</h1>

    {% if note %}
    <h2 style="color: green;">{{ note }}</h2>
    {% endif %}

    <form enctype="multipart/form-data" action="{% url 'order' %}" method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Order Pizza">

    </form>
</body>

</html>
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/351a6625-b2aa-4b54-b7d0-17dc44d50f38)

<img width="1457" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/cf8af387-957e-4e5d-bb3e-1b8f99516098">
<img width="1457" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ba6fe724-ae09-4e60-902e-d23b4b6bc0c5">
<img width="1457" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/87a24092-afeb-42d2-960a-97448b09fdd5">

# #END</details>

<details>
<summary>13. Using Formsets - Multiple Forms on a page </summary>

# Using Formsets - Multiple Forms on a page 

[https://github.com/omeatai/src-python-flask-django/commit/afd858b787522e90f3a0cab463c9384db471177a](https://github.com/omeatai/src-python-flask-django/commit/afd858b787522e90f3a0cab463c9384db471177a)

### pizza.urls:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('order', views.order, name='order'),
    path('orders', views.orders, name='orders'),
]

```

### pizza.views:

```py
from django.shortcuts import render
from .forms import PizzaForm, MultiplePizzaForm
from django.forms import formset_factory
# Create your views here.


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            size = filled_form.cleaned_data['size']
            topping1 = filled_form.cleaned_data['topping1']
            topping2 = filled_form.cleaned_data['topping2']
            # note = f"Thanks for ordering! Your {size} pizza with {topping1} and {topping2} is on its way!"
            note = "Thanks for ordering! Your %s Pizza with %s and %s is on its way!" % (
                size, topping1, topping2)
            empty_form = PizzaForm()
            return render(request, 'pizza/order.html', {'form': empty_form, 'note': note, "multiple_form": multiple_form})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'form': form, "multiple_form": multiple_form})


def orders(request):
    number_of_pizzas = 2
    filled_multi_form = MultiplePizzaForm(request.GET)

    if filled_multi_form.is_valid():
        number_of_pizzas = filled_multi_form.cleaned_data['number']

    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()

    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data)
            note = "Multiple Pizzas have been ordered"
        else:
            note = "Order was not created, please try again"
        return render(request, 'pizza/orders.html', {'note': note, 'formset': formset})
    else:
        return render(request, 'pizza/orders.html', {'formset': formset})

```

### pizza.forms:

```py
from django import forms
from .models import Pizza, Size

CHOICES = [('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')]
TOPPING_CHOICES = [('pep', 'Pepperoni'), ('cheese',
                                          'Cheese'), ('olives', 'Olives')]


# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label='Topping 1', max_length=100)
#     topping2 = forms.CharField(label='Topping 2', max_length=100)
#     size = forms.ChoiceField(label='Size', choices=CHOICES)

class PizzaForm(forms.ModelForm):

    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {
            'topping1': 'Topping 1',
            'topping2': 'Topping 2',
            'size': 'Size',
        }

        widgets = {
            'topping1': forms.TextInput(attrs={'class': 'form-control'}),
            'topping2': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.RadioSelect(attrs={'class': 'form-control'}),
        }


class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)

```

### src-python/linkedin/django-forms/pizza/templates/pizza/order.html:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Order a Pizza</title>
</head>

<body>
    <h1>Order Pizza Form</h1>

    {% if note %}
    <h2 style="color: green;">{{ note }}</h2>
    {% endif %}

    <div>
        <form action="{% url 'order' %}" method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <input type="submit" value="Order Pizza">
        </form>
        <br /><br />
    </div>

    <div>
        <h3>Want more than one pizza?</h3>

        <form action="{% url 'orders' %}" method="get">
            {% csrf_token %}
            {{ multiple_form.as_p }}
            <input type="submit" value="Get Pizzas">
        </form>
    </div>

</body>

</html>
```

### src-python/linkedin/django-forms/pizza/templates/pizza/orders.html:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Multiple Orders</title>
</head>

<body>
    <h1>Make your orders</h1>

    {% if note %}
    <h2 style="color: green;">{{ note }}</h2>
    {% endif %}

    <div>
        <form action="{% url 'orders' %}" method="post">
            {% csrf_token %}
            {{ formset.management_form }}

            {% for form in formset %}
            {{ form.as_p }}
            <br />
            <hr>
            {% endfor %}
            <input type="submit" value="Order Pizzas">
            <a type="button" style="padding: 5px 20px; background: red; border-radius: 50px; color: white; "
                href="{% url 'order' %}">I
                want more
                orders</a>
        </form>
    </div>

</body>

</html>
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/ce9acb71-82bf-44a9-837e-20a9964d3830)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/8a89d00e-8628-482b-b2a4-822e841a94c7)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/23b9bfa5-c6a4-4ad6-84a3-42fec59cf5d8)

<img width="1457" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/c99e3a90-aa0f-43ae-a74a-0ab8f1eb81a3">
<img width="1457" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/17149a9d-bcac-4fb9-887d-508c2e718ee4">
<img width="1457" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ea4a7d77-216a-4c86-bd60-a1d6d0f16727">
<img width="1457" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1c1b44cf-d754-4b9f-90c7-785dbaad46e8">
<img width="1457" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/fd0f7177-5311-414b-8b0d-f45c49093313">

# #END</details>

<details>
<summary>14. Editing Pizza Orders </summary>

# Editing Pizza Orders

[https://github.com/omeatai/src-python-flask-django/commits/main/](https://github.com/omeatai/src-python-flask-django/commits/main/)

### pizza.models:

```py
from django.db import models

# Create your models here.


class Size(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Pizza(models.Model):
    topping1 = models.CharField(max_length=100)
    topping2 = models.CharField(max_length=100)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.size} pizza with {self.topping1} and {self.topping2}."

```

### pizza.urls:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('order', views.order, name='order'),
    path('orders', views.orders, name='orders'),
    path('order/<int:pk>', views.edit_order, name='edit-order'),
]

```

### pizza.views:

```py
from django.shortcuts import render, get_object_or_404
from django.forms import formset_factory
from .forms import PizzaForm, MultiplePizzaForm
from .models import Pizza
# Create your views here.


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            created_pizza = filled_form.save()
            created_pizza_pk = created_pizza.id
            size = filled_form.cleaned_data['size']
            topping1 = filled_form.cleaned_data['topping1']
            topping2 = filled_form.cleaned_data['topping2']
            # note = f"Thanks for ordering! Your {size} pizza with {topping1} and {topping2} is on its way!"
            note = "Thanks for ordering! Your %s Pizza with %s and %s is on its way!" % (
                size, topping1, topping2)
            empty_form = PizzaForm()
            return render(request, 'pizza/order.html', {'created_pizza_pk': created_pizza_pk, 'form': empty_form, 'note': note, "multiple_form": multiple_form})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'form': form, "multiple_form": multiple_form})


def orders(request):
    number_of_pizzas = 2
    filled_multi_form = MultiplePizzaForm(request.GET)

    if filled_multi_form.is_valid():
        number_of_pizzas = filled_multi_form.cleaned_data['number']

    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()

    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data)
            note = "Multiple Pizzas have been ordered"
        else:
            note = "Order was not created, please try again"
        return render(request, 'pizza/orders.html', {'note': note, 'formset': formset})
    else:
        return render(request, 'pizza/orders.html', {'formset': formset})


def edit_order(request, pk):
    # pizza = Pizza.objects.get(pk=pk)
    pizza = get_object_or_404(Pizza, pk=pk)
    filled_form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            note = "Your order has been updated"
            return render(request, 'pizza/edit_order.html', {'form': filled_form, 'pizza': pizza, 'note': note})
    else:
        return render(request, 'pizza/edit_order.html', {'form': filled_form, 'pizza': pizza})

```

### src-python/linkedin/django-forms/pizza/templates/pizza/edit_order.html:

```py
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Pizza</title>
</head>

<body>
    <h1>Edit Pizza Form</h1>

    {% if note %}
    <h2 style="color: green;">{{ note }}</h2>
    {% endif %}

    <div>
        <form action="{% url 'edit-order' pizza.pk %}" method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <input type="submit" value="Edit Your Order">
        </form>
        <br />
        <hr>
    </div>

</body>

</html>
```

### src-python/linkedin/django-forms/pizza/templates/pizza/order.html:

```py
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Order a Pizza</title>
    <style>
        .btn {
            background-color: blue;
            border: none;
            border-radius: 50px;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }
    </style>
</head>

<body>
    <h1>Order Pizza Form</h1>

    {% if note %}
    <h2 style="color: green;">{{ note }}</h2>
    {% endif %}

    {% if created_pizza_pk %}
    <a href="{% url 'edit-order' created_pizza_pk %}" class="btn">Edit Your Order</a>
    {% endif %}

    <div>
        <form action="{% url 'order' %}" method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <input type="submit" value="Order Pizza">
        </form>
        <br /><br />
    </div>

    <div>
        <h3>Want more than one pizza?</h3>

        <form action="{% url 'orders' %}" method="get">
            {% csrf_token %}
            {{ multiple_form.as_p }}
            <input type="submit" value="Get Pizzas">
        </form>
    </div>

</body>

</html>
```

<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a562667c-f6c3-4cb2-b524-e2047bde0db4">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ad62630b-08d6-4ccc-9aea-cff10e82dafd">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/7d5b89c9-a063-49d3-acc6-45a34cca2020">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/d94221cf-0bfd-4b9a-9078-83da01df3e98">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/28e93711-3018-41f8-ac25-bfaa769e71a9">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/22d67e7e-2e41-4535-b1f6-80e0ec61dd4e">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/78712b66-e122-4ee4-9f75-c5b3f001bd0a">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/d3ac196d-1b11-4540-8f44-28681e09c087">
<img width="960" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/8f3938fd-6f72-4ea7-bb48-15ca656d73ba">

<img width="1369" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/34cd5e26-e5f6-4b69-8618-82782f802f39">
<img width="1369" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ba5d2371-f225-496b-9c48-4b603fef6252">
<img width="1369" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a1de2933-e7bc-4f24-8821-9b0fa0d80e40">
<img width="1369" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/bb3f776b-b186-4eb9-bbb5-31a10afd7731">
<img width="1369" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/3a883bed-719e-4363-bf24-64de5ef5ec28">

# #END</details>

<details>
<summary>15. Local and Server-based Validation Errors + Form Rendering </summary>

# Local and Server-based Validation Errors + Form Rendering

[https://github.com/omeatai/src-python-flask-django/commit/7381d6d1461ea4493f333249256d03973aac584b](https://github.com/omeatai/src-python-flask-django/commit/7381d6d1461ea4493f333249256d03973aac584b)

### pizza.views:

```py
from django.shortcuts import render, get_object_or_404
from django.forms import formset_factory
from .forms import PizzaForm, MultiplePizzaForm
from .models import Pizza
# Create your views here.


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            created_pizza = filled_form.save()
            created_pizza_pk = created_pizza.id
            size = filled_form.cleaned_data['size']
            topping1 = filled_form.cleaned_data['topping1']
            topping2 = filled_form.cleaned_data['topping2']
            # note = f"Thanks for ordering! Your {size} pizza with {topping1} and {topping2} is on its way!"
            note = "Thanks for ordering! Your %s Pizza with %s and %s is on its way!" % (
                size, topping1, topping2)
            filled_form = PizzaForm()
        else:
            created_pizza_pk = None
            note = "Order was not created, please try again"
        return render(request, 'pizza/order.html', {'created_pizza_pk': created_pizza_pk, 'form': filled_form, 'note': note, "multiple_form": multiple_form})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'form': form, "multiple_form": multiple_form})


def orders(request):
    number_of_pizzas = 2
    filled_multi_form = MultiplePizzaForm(request.GET)

    if filled_multi_form.is_valid():
        number_of_pizzas = filled_multi_form.cleaned_data['number']

    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()

    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data)
            note = "Multiple Pizzas have been ordered"
        else:
            note = "Order was not created, please try again"
        return render(request, 'pizza/orders.html', {'note': note, 'formset': formset})
    else:
        return render(request, 'pizza/orders.html', {'formset': formset})


def edit_order(request, pk):
    # pizza = Pizza.objects.get(pk=pk)
    pizza = get_object_or_404(Pizza, pk=pk)
    filled_form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            note = "Your order has been updated"
            return render(request, 'pizza/edit_order.html', {'form': filled_form, 'pizza': pizza, 'note': note})
    else:
        return render(request, 'pizza/edit_order.html', {'form': filled_form, 'pizza': pizza})

```

### pizza.forms:

```py
from django import forms
from .models import Pizza, Size

CHOICES = [('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')]
TOPPING_CHOICES = [('pep', 'Pepperoni'), ('cheese',
                                          'Cheese'), ('olives', 'Olives')]


# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label='Topping 1', max_length=100)
#     topping2 = forms.CharField(label='Topping 2', max_length=100)
#     size = forms.ChoiceField(label='Size', choices=CHOICES)

class PizzaForm(forms.ModelForm):

    email = forms.EmailField()
    website = forms.URLField()

    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {
            'topping1': 'Topping 1',
            'topping2': 'Topping 2',
            'size': 'Size',
        }

        widgets = {
            'topping1': forms.TextInput(attrs={'class': 'form-control'}),
            'topping2': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.RadioSelect(attrs={'class': 'form-control'}),
        }


class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)

```

### src-python/linkedin/django-forms/pizza/templates/pizza/order.html:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Order a Pizza</title>
    <style>
        .btn {
            background-color: blue;
            border: none;
            border-radius: 50px;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }
    </style>
</head>

<body>
    <h1>Order Pizza Form</h1>

    {% if note %}
    <h2 style="color: green;">{{ note }}</h2>
    {% endif %}

    {% if created_pizza_pk %}
    <a href="{% url 'edit-order' created_pizza_pk %}" class="btn">Edit Your Order</a>
    {% endif %}

    <div>
        {% comment %} <form action="{% url 'order' %}" method="post" novalidate> {% endcomment %}
            <form action="{% url 'order' %}" method="post">
                {% csrf_token %}
                {{ form.as_p }}

                <hr>
                <table>
                    {{ form.as_table }}
                </table>

                <hr>
                <ul>
                    {{ form.as_ul }}
                </ul>

                <hr>
                <ol>
                    {{ form.as_ul }}
                </ol>

                <hr>
                <input type="submit" value="Order Pizza">
            </form>
            <br /><br />
    </div>

    <div>
        <h3>Want more than one pizza?</h3>

        <form action="{% url 'orders' %}" method="get">
            {% csrf_token %}
            {{ multiple_form.as_p }}
            <input type="submit" value="Get Pizzas">
        </form>
    </div>

</body>

</html>
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/7f32d26e-cd50-4d3d-920c-08967032210a)

<img width="1454" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a45d64c8-9973-4156-8bd3-f815c6c85e12">
<img width="1454" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/f93b5c1f-7849-426a-a48a-fa699f7a6dc3">
<img width="1454" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/a7a3e182-09d7-4853-8258-75cc7ff3003e">

# #END</details>

<details>
<summary>16. Customizing Form Fields </summary>

# Customizing Form Fields

[https://github.com/omeatai/src-python-flask-django/commit/ee30329b2e87cb46b4869ee97399ae586f047316](https://github.com/omeatai/src-python-flask-django/commit/ee30329b2e87cb46b4869ee97399ae586f047316)

### src-python/linkedin/django-forms/pizza/templates/pizza/order.html:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Order a Pizza</title>
    <style>
        .btn {
            background-color: blue;
            border: none;
            border-radius: 50px;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }
    </style>
</head>

<body>
    <h1>Order Pizza Form</h1>

    {% if note %}
    <h2 style="color: green;">{{ note }}</h2>
    {% endif %}

    {% if created_pizza_pk %}
    <a href="{% url 'edit-order' created_pizza_pk %}" class="btn">Edit Your Order</a>
    {% endif %}

    <div>
        {% comment %} <form action="{% url 'order' %}" method="post" novalidate> {% endcomment %}
            <form action="{% url 'order' %}" method="post">
                {% csrf_token %}

                <div>
                    {{ form.topping1.label_tag }}
                    {{ form.topping1 }}
                    {{ form.topping1.errors }}
                </div>
                <br />
                <div>
                    {{ form.topping2.label_tag }}
                    {{ form.topping2 }}
                    {{ form.topping2.errors }}
                </div>
                <br />
                <div>
                    <label for="{{ form.size.id_for_label }}">Size for your Pizza:</label>
                    {% comment %} {{ form.size.label_tag }} {% endcomment %}
                    {{ form.size }}
                    {{ form.size.errors }}
                </div>
                <br />

                <input type="submit" value="Order Pizza">
            </form>
            <br /><br />
    </div>

    <div>
        <h3>Want more than one pizza?</h3>

        <form action="{% url 'orders' %}" method="get">
            {% csrf_token %}
            {{ multiple_form.as_p }}
            <input type="submit" value="Get Pizzas">
        </form>
    </div>

</body>

</html>
```

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/1395404d-ee25-4617-8f04-481504e3155f)

<img width="1454" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/1fee9e3d-d27d-4c0f-b846-c4b0b379eb07">

# #END</details>

<details>
<summary>17. Using Base Template and Styling with Django-Widget-Tweaks and Bootstrap </summary>

# Using Base Template and Styling with Django-Widget-Tweaks and Bootstrap 

[https://github.com/omeatai/src-python-flask-django/commit/cc5e531355f58bffa3fd110c1a7d0b25c29272d7](https://github.com/omeatai/src-python-flask-django/commit/cc5e531355f58bffa3fd110c1a7d0b25c29272d7)

## Install Django Widget Tweaks

```py
pip install django-widget-tweaks
```

## Run Collect Static

```py
python manage.py collectstatic
```

### anyisgarden.settings:

```py
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pizza',
    'widget_tweaks',
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

### src-python/linkedin/django-forms/pizza/templates/pizza/base.html:

```html
<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Anyi's Garden</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>

<body>

    <nav class="navbar navbar-expand-lg navbar-dark" style="background-color: #238a44">
        <div class="container">
            <a class="navbar-brand" href="{% url 'home' %}">Nandia's Garden</a>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item active">
                        <a class="nav-link" href="{% url 'order' %}">Order Pizza</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    {% block content %}
    {% endblock content %}

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous">
    </script>

</body>

</html>
```

### src-python/linkedin/django-forms/pizza/templates/pizza/order.html:

```html
{% extends "pizza/base.html" %}

{% block content %}

{% load widget_tweaks %}

<div class="container">
    <h1 class="my-4">Order Pizza Form</h1>

    {% if note %}
    <h2 style="color: green;">{{ note }}</h2>
    {% endif %}

    {% if created_pizza_pk %}
    <a href="{% url 'edit-order' created_pizza_pk %}" class="btn btn-lg btn-primary">Edit Your Order</a>
    {% endif %}

    <div>
        {% comment %} <form action="{% url 'order' %}" method="post" novalidate> {% endcomment %}
            <form action="{% url 'order' %}" method="post">
                {% csrf_token %}

                {% for field in form %}

                <div class="form-group">
                    {{ field.label_tag }}
                    {% render_field field class="form-control" %}
                    {{ field.errors }}
                </div>
                <br />

                {% endfor %}

                <input type="submit" class="btn btn-lg btn-success" value="Order Pizza">
            </form>
            <br />
            <hr>
    </div>

    <div>
        <h3>Want more than one pizza?</h3>

        <form action="{% url 'orders' %}" method="get">
            {% csrf_token %}
            {{ multiple_form.as_p }}
            <input type="submit" class="btn btn-lg btn-primary" value="Get Pizzas">
        </form>
    </div>

</div>

{% endblock content %}
```

### src-python/linkedin/django-forms/pizza/templates/pizza/orders.html:

```html
{% extends "pizza/base.html" %}

{% block content %}

<div class="container">
    <h1>Make your orders</h1>

    {% if note %}
    <h2 style="color: green;">{{ note }}</h2>
    {% endif %}

    <div>
        <form action="{% url 'orders' %}" method="post">
            {% csrf_token %}
            {{ formset.management_form }}

            {% for form in formset %}
            {{ form.as_p }}
            <br />
            <hr>
            {% endfor %}
            <input type="submit" value="Order Pizzas">
            <a type="button" style="padding: 5px 20px; background: red; border-radius: 50px; color: white; "
                href="{% url 'order' %}">I
                want more
                orders</a>
        </form>
    </div>

</div>

{% endblock content %}
```

### src-python/linkedin/django-forms/pizza/templates/pizza/edit_order.html:

```html
{% extends "pizza/base.html" %}

{% block content %}

<div class="container">
    <h1>Edit Pizza Form</h1>

    {% if note %}
    <h2 style="color: green;">{{ note }}</h2>
    {% endif %}

    <div>
        <form action="{% url 'edit-order' pizza.pk %}" method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <input type="submit" value="Edit Your Order">
        </form>
        <br />
        <hr>
    </div>

</div>

{% endblock content %}
```

### src-python/linkedin/django-forms/pizza/templates/pizza/home.html:

```html
{% extends "pizza/base.html" %}
{% load static %}

{% block content %}


<img src="{% static 'pizza.jpeg' %}" class="img-fluid w-100 min-h-screen" alt='Anyis Garden'></img>

<div>
    <a href="{% url 'order' %}" class="btn btn-toolbar btn-primary py-5">Order pizza</a>
</div>


{% endblock content%}
```

### pizza.forms:

```py
from django import forms
from .models import Pizza, Size

CHOICES = [('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')]
TOPPING_CHOICES = [('pep', 'Pepperoni'), ('cheese',
                                          'Cheese'), ('olives', 'Olives')]


# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label='Topping 1', max_length=100)
#     topping2 = forms.CharField(label='Topping 2', max_length=100)
#     size = forms.ChoiceField(label='Size', choices=CHOICES)

class PizzaForm(forms.ModelForm):

    # email = forms.EmailField()
    # website = forms.URLField()

    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {
            'topping1': 'Topping 1',
            'topping2': 'Topping 2',
            'size': 'Size',
        }

        widgets = {
            'topping1': forms.TextInput(attrs={'class': 'form-control'}),
            'topping2': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.Select(attrs={'class': 'form-control'}),
        }


class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)

```

[https://getbootstrap.com/docs/5.3/getting-started/introduction/](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/8166e251-8d37-493a-80a7-e45dd1ebaf85)

![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/58250154-03cb-4e62-8cd4-82c14457cd37)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/4e6d0d2f-412a-4c5e-ace0-898a583f29c8)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/e18c2df2-4eba-47d3-a49c-c7c6442df37e)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/18232db0-5f9b-4b1f-9b51-c57a38e41466)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/dcc200c8-19da-4631-8cdd-40df5696d7b6)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/28ec3b6c-61f5-4e66-868c-7f07ee47954b)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/f0c9c0f1-69c1-4b57-99c8-c54fa8497537)
![image](https://github.com/omeatai/src-python-flask-django/assets/32337103/43ec87d1-ac41-47d0-8a2b-b170d5d8bbed)

<img width="1454" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/48551516-dd43-46dd-b65c-1c535018b932">
<img width="1454" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/2ec4204e-001e-4b17-b605-25811714691b">
<img width="1454" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/50835de6-07e6-42e8-a2ff-33d98c0873aa">
<img width="1454" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/629b9df2-7039-49bf-a85f-24b980475196">
<img width="1454" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/4a1219a0-00d4-4682-a40c-cb8b31047757">
<img width="1454" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/ccbd8316-617d-4867-820d-79a295ecc85a">
<img width="1454" alt="image" src="https://github.com/omeatai/src-python-flask-django/assets/32337103/88c21cf2-3dd6-460b-8b58-c9123e5c1b2c">

# #END</details>

# #END
