release: python manage.py migrate
python manage.py loaddata fixtures.json
web: gunicorn quicktutor.wsgi
