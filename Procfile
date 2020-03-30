release: python manage.py makemigrations
release: python manage.py migrate --run-syncdb
web: gunicorn quicktutor.wsgi
