#!/bin/bash
set -e
echo "Installing pip..."
python3 -m pip install --upgrade pip
echo "Installing requirements..."
python3 -m pip install -r requirements.txt
echo "Running collectstatic..."
python3 djfintracker/manage.py collectstatic --noinput
