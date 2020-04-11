release: heroku restart && heroku pg:reset DATABASE --confirm APP-NAME && heroku run rake db:migrate
release: python manage.py makemigrations
release: python manage.py migrate --run-syncdb
web: gunicorn quicktutor.wsgi
