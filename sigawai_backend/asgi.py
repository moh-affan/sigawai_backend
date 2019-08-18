import os
import django
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sigawai_backend.settings")
os.environ['HTTPS'] = 'on'
django.setup()
application = get_default_application()
