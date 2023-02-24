#!/bin/bash

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata users.json
python manage.py loaddata dummy.json
python manage.py runserver

