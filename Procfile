web: sh -c 'cd ./exotik'
web: gunicorn exotik.wsgi --log-file - --log-level debug
python manage.py collectstatic --noinput
python manage.py migrate
