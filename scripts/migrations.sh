#!/bin/sh

poetry run python ./manage.py makemigrations --noinput

poetry run python ./manage.py migrate --noinput

