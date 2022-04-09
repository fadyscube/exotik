# Exotik
A website that gives you ideas and many activities to manage your time and break the routine with new ideas.

# Setup
The used versions: Python 3.9 and Django 4.

## Create virtual environment
Exotik uses pipenv but you can use any other tool
```bash
$ pipenv shell # if you use pipenv
```

## Install dependencies
```bash
$ pipenv install # if you use pipenv
```

## Run the developpement server
```
$ cd exotik
$ python manage.py runserver
```

## Used dependencies
```
Django==4.0.3
  - asgiref [required: >=3.4.1,<4, installed: 3.5.0]
  - sqlparse [required: >=0.2.2, installed: 0.4.2]
gunicorn==20.1.0
  - setuptools [required: >=3.0, installed: 62.0.0]
psycopg2==2.9.3
python-decouple==3.6
```