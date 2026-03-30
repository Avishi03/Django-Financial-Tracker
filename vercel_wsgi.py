# vercel_wsgi.py
import os
import sys

# Add the 'djfintracker' module to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'djfintracker'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djfintracker.settings')

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
