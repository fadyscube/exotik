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

## Environment variables
In the `settings.py` module there is some values that are stored in local environment variables such as development database configuration, to create theme you need to create a file called `.env` in the same level as the `manage.py` module and in this file you are going to put all the variables in this format:

```
DATABASE_NAME='db_name'
DATABASE_USER='db_user'
DATABASE_PASSWORD='db_password'
DATABASE_PORT='db_port'
SECRET_KEY='random_secret_key'
```

For using those variables in the `settings.py` module we use the [`python-decouple`](https://pypi.org/project/python-decouple/) library like this:

```python
from decouple import config

# To use it:
my_variable = config('VARIABLE_NAME')
```

## Run migrations
You need to run the migrations to create the tables in your database
```bash
$ python manage.py migrate
```

## Load database data
You need to load the activities table in your database
```bash
$ python manage.py loaddata activities/dunps/activities/activities.json
```