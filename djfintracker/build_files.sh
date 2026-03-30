#!/bin/bash

# Install dependencies
pip install -r ../requirements.txt

# Collect static files into staticfiles_build/static
python manage.py collectstatic --noinput --clear
