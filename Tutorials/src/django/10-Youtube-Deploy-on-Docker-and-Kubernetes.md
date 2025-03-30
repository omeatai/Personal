## +Youtube-Deploy-on-Docker-and-Kubernetes

## [COURSE](https://www.youtube.com/watch?v=-ANCcFQBk6I) - Deploy 12 apps to AWS, Azure, & Google Cloud

<details>
<summary>1. React on Docker - Create React App </summary>

# React on Docker - Create React App

```x
npx create-react-app my_demo_app
```

## Run React App

```x
npm run start
```

### my_projects/10_deploy_on_docker/my_demo_app/src/index.js:

```js
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
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

### my_projects/10_deploy_on_docker/my_demo_app/src/App.js:

```js
import logo from "./logo.svg";
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Welcome to REACT!</h1>
      </header>
    </div>
  );
}

export default App;

```

![image](https://github.com/user-attachments/assets/32522335-cc71-48d4-97e1-c2c93686ca25)

<img width="1439" alt="image" src="https://github.com/user-attachments/assets/004d4aa9-0408-4d87-8b3a-bd5d1129a7fd">
<img width="1439" alt="image" src="https://github.com/user-attachments/assets/66257601-8df5-4313-a97e-a2757d0f0022">

# #END</details>

<details>
<summary>2. React on Docker - Setup Docker for React App </summary>

# React on Docker - Setup Docker for React App

## Install Docker

```x
https://docs.docker.com/desktop/install/mac-install/
```

<img width="788" alt="image" src="https://github.com/user-attachments/assets/722d073d-025f-4271-a282-89040f006298">

## Check Docker Versions

```x
docker
docker --version
docker-compose --version
```

<img width="970" alt="image" src="https://github.com/user-attachments/assets/23f48e1f-7cf9-494e-a1d8-443520ab5a69">
<img width="1443" alt="image" src="https://github.com/user-attachments/assets/f6273484-bfd6-4515-83be-da1c66d24aa0">

### my_projects/10_deploy_on_docker/my_demo_app/Dockerfile:

```x
FROM node:15.4 as build

WORKDIR /app

COPY package*.json .
RUN npm install
COPY . .
RUN npm run build

```

### Run NPM Build

```x
npm run build
```

<img width="1350" alt="image" src="https://github.com/user-attachments/assets/0d1a0e86-10e9-4f51-a093-f210f6cdab21">
<img width="1350" alt="image" src="https://github.com/user-attachments/assets/51348bc1-301d-48bb-b273-39efe56726b0">

# #END</details>

<details>
<summary>3. React on Docker - Setup Nginx for Docker </summary>

# React on Docker - Setup Nginx for Docker

### my_projects/10_deploy_on_docker/my_demo_app/Dockerfile:

```x
FROM node:15.4 as build

WORKDIR /app

COPY package*.json .
RUN npm install
COPY . .
RUN npm run build

FROM nginx:1.19

COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
COPY --from=build /app/build /usr/share/nginx/html

```

### my_projects/10_deploy_on_docker/my_demo_app/nginx/nginx.conf:

```x
worker_processes 1;

events {
    worker_connections 1024;
}

http {
    server {
        listen 80;
        server_name localhost;

        root /usr/share/nginx/html;
        index index.html index.htm;
        include /etc/nginx/mime.types;

        gzip on;
        gzip_min_length 1000;
        gzip_proxied expired no-cache no-store private auth;
        gzip_types text/plain text/css application/json application/javascript application/x-javascript text/xml application/xml application/xml+rss text/javascript;

        location / {
            try_files $uri $uri/ /index.html;
        }
    }
}
```

## Build Dockerfile

```x
docker build -t app .
```

<img width="1306" alt="image" src="https://github.com/user-attachments/assets/66e4f0e5-af66-49e8-95b0-9dd7db866aac">

## Run Docker Container

```x
docker run -p 8888:80 app
```

```x
http://localhost:8888/
```

![image](https://github.com/user-attachments/assets/e0fc21b8-53c6-4ac6-b3a6-cfeb3f65c3c3)

<img width="1443" alt="image" src="https://github.com/user-attachments/assets/bbc7da8f-2614-4d34-8aab-c42bf31710f8">
<img width="1443" alt="image" src="https://github.com/user-attachments/assets/e74c46b8-82a3-4332-a101-d35c753b07d5">
<img width="1349" alt="image" src="https://github.com/user-attachments/assets/df5e23ce-0816-44e1-bf1d-1df6b7352d66">
<img width="1349" alt="image" src="https://github.com/user-attachments/assets/b1d241cf-742a-4dd8-ad5a-15058caeca72">

# #END</details>

<details>
<summary>4. Django on Docker - Create Django App </summary>

# Django on Docker - Create Django App

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

## Get dependencies

```x
pip freeze
```

```x
asgiref==3.8.1
Django==5.1
sqlparse==0.5.1
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
django-admin startproject my_project .
```

## Create Django App - my_app

```x
python manage.py startapp my_app
```

### my_projects/10_deploy_on_docker/my_django_app/my_project/settings.py:

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
    'my_app'
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
(venv) ➜  my_django_app python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
August 08, 2024 - 03:28:00
Django version 5.1, using settings 'my_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

![image](https://github.com/user-attachments/assets/1e8e8043-fee4-465c-82c9-87c1ae80705a)

# #END</details>

<details>
<summary>5. Django on Docker - Setup Django App Url, View and Template </summary>

# Django on Docker - Setup Django App Url, View and Template

```py

```

```py

```

```py

```

```py

```

# #END</details>

<details>
<summary>6. Django on Docker - Setup Docker for Django App </summary>

# Django on Docker - Setup Docker for Django App 

## Install Docker

```x
https://docs.docker.com/desktop/install/mac-install/
```

<img width="788" alt="image" src="https://github.com/user-attachments/assets/722d073d-025f-4271-a282-89040f006298">

## Check Docker Versions

```x
docker
docker --version
docker-compose --version
```

<img width="970" alt="image" src="https://github.com/user-attachments/assets/23f48e1f-7cf9-494e-a1d8-443520ab5a69">
<img width="1443" alt="image" src="https://github.com/user-attachments/assets/f6273484-bfd6-4515-83be-da1c66d24aa0">

```x

```

```x

```

```x

```

```x

```

```x

```

```x

```

```x

```

```x

```

```x

```

```x

```

# #END</details>
