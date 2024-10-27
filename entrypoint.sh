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

# Start the server
python manage.py runserver 0.0.0.0:8080

# # wait server
# sleep 10

# # send data to the API from CSV and JSON

# # wait for the server to finish
# wait