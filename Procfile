web: gunicorn --pythonpath exotik exotik.wsgi
python manage.py collectstatic --noinput
python manage.py migrate
