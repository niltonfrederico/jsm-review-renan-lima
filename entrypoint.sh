#!/bin/sh

# make migrations
python manage.py makemigrations

# migrate Django
python manage.py migrate

#Collect Static Files
python manage.py collectstatic --noinput

# creste superuser
python user_manager.py

python data_manager.py

python manage.py test

# Start the server
exec python manage.py runserver 0.0.0.0:8080