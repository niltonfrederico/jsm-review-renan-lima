#!/bin/sh

# Exec make migrations
python manage.py makemigrations

# Exec migrate Django
python manage.py migrate

#Collect Static Files
python manage.py collectstatic

# Run server
exec python manage.py runserver 0.0.0.0:8080
