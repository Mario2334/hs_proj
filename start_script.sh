#!/usr/bin/env bash

pip install -r requirements.txt

python manage.py createdb --noinput

python manage.py migrate

python manage.py runserver
