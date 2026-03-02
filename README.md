# Django Learning Path

This repository documents a **complete learning path for Python Django**.  
It covers everything from **environment setup → Django project creation → apps → database → development workflow**.

The goal of this repository is to help beginners understand **how Django works in real development environments**.

---

# What is Django?

**Django** is a high-level Python web framework that allows developers to build secure, scalable, and maintainable web applications quickly.

Main features of Django:

- Built with Python
- MTV Architecture (Model Template View)
- Built-in Admin Panel
- ORM (Object Relational Mapper)
- Authentication system
- URL routing system
- Security features

Official Website:  
https://www.djangoproject.com/

---

# Requirements

Before starting Django development, install the following tools.

### Python

Check Python installation:

```bash
python --version
```

or

```bash
python3 --version
```

If Python is not installed:

Download from:  
https://www.python.org/downloads/

Recommended version:

```
Python 3.10+
```

---

### pip (Python Package Manager)

Check pip:

```bash
pip --version
```

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

---

# Virtual Environment Setup (venv)

A **virtual environment** isolates project dependencies so different projects can use different package versions.

### Create Virtual Environment

```bash
python -m venv venv
```

After running this command, a folder will be created:

```
venv/
```

---

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Mac / Linux

```bash
source venv/bin/activate
```

When activated, terminal will look like:

```
(venv) C:\project-folder>
```

---

### Deactivate Virtual Environment

```bash
deactivate
```

---

# Installing Django

Install Django using pip:

```bash
pip install django
```

Check installation:

```bash
django-admin --version
```

Example output:

```
5.0.4
```

---

# Save Project Dependencies

Create a requirements file:

```bash
pip freeze > requirements.txt
```

Install dependencies from file:

```bash
pip install -r requirements.txt
```

---

# Creating a Django Project

Create a new Django project:

```bash
django-admin startproject myproject
```

Enter project folder:

```bash
cd myproject
```

Project structure:

```
myproject/
│
├── manage.py
├── myproject/
│
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
```

File explanations:

| File | Purpose |
|-----|------|
| manage.py | Django command line utility |
| settings.py | Project configuration |
| urls.py | URL routing |
| asgi.py | ASGI server config |
| wsgi.py | WSGI server config |

---

# Running Django Development Server

Run the development server:

```bash
python manage.py runserver
```

Server will start at:

```
http://127.0.0.1:8000/
```

Run on custom port:

```bash
python manage.py runserver 8080
```

---

# Creating a Django Application

Django projects contain **multiple apps**.

Create a new app:

```bash
python manage.py startapp blog
```

App structure:

```
blog/
│
├── admin.py
├── apps.py
├── models.py
├── views.py
├── tests.py
└── migrations/
```

File explanation:

| File | Purpose |
|-----|------|
| models.py | Database models |
| views.py | Application logic |
| admin.py | Admin panel configuration |
| apps.py | App configuration |

---

# Register App in Django

Open:

```
settings.py
```

Add your app:

```python
INSTALLED_APPS = [
    'blog',
]
```

---

# Django Models (Database Tables)

Example model:

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

---

# Database Migration

Create migration files:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

---

# Django Admin Panel

Create admin user:

```bash
python manage.py createsuperuser
```

Example:

```
Username: admin
Email: admin@email.com
Password: ********
```

Run server:

```bash
python manage.py runserver
```

Access admin panel:

```
http://127.0.0.1:8000/admin
```

Register model in admin:

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

---

# Django URL Routing

Example:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
]
```

---

# Django View Example

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Django Learning Path")
```

---

# Common Django Commands

Run server:

```bash
python manage.py runserver
```

Create app:

```bash
python manage.py startapp appname
```

Make migrations:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

Show migrations:

```bash
python manage.py showmigrations
```

Create superuser:

```bash
python manage.py createsuperuser
```

Open Django shell:

```bash
python manage.py shell
```

Collect static files:

```bash
python manage.py collectstatic
```

---

# Recommended Development Tools

Editor:

```
VS Code
```

Recommended Extensions:

- Python
- Django
- Pylance
- GitLens
- Prettier

---

# Learning Roadmap

Step-by-step Django learning order:

1. Python Fundamentals
2. Virtual Environment
3. Django Installation
4. Django Project Structure
5. Django Apps
6. Django Models
7. Django Admin
8. Templates
9. Static Files
10. Authentication
11. Django REST Framework
12. Deployment

---

# Author

Md. Nusrul Nakib Nahid  
Software Engineer
Daffodil International University

GitHub  
https://github.com/nusrulnakibnahid