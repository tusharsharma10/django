## Install

```bash
python3 -m venv venv
source venv/bin/activate
```

### Create requirements.txt file

- and run
```commandline
pip3 install -r requirements.txt
```

---

### Creating a Project

```commandline
django-admin startproject mysite
```

---
### Run dev server

```commandline
python manage.py runserver <port>
```

### Create a package

```commandline
python3 manage.py startapp api
```

- Add this under settings.py INSTALLED_APPS
---
### Converting json to python dictionary
```py
import json

## data = json.loads(body)

```
### Migrations

```commandline
 python manage.py makemigrations
 python manage.py migrate
```

---

### Binding with mysql

```commandline
pip3 install mysqlclient
```

```commandline
python manage.py inspectdb > yourapp/models.py
```

---

### References
- https://docs.djangoproject.com/en/5.0/intro/tutorial01/

---