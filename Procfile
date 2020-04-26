worker: heroku pg:reset DATABASE
worker: heroku run rake db:migrate
release: python manage.py migrate
release: python manage.py loaddata fixtures.json
web: gunicorn quicktutor.wsgi
