#!/bin/sh

poetry shell

poetry run python manage.py runserver 0.0.0.0:8000