#!/bin/bash
# Install requirements
python3.12 -m pip install -r requirements.txt

# Run collectstatic
python3.12 djfintracker/manage.py collectstatic --noinput
