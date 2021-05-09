
release: python manage.py migrate --no-input
web: gunicorn urlshortner.wsgi:application --log-file -
