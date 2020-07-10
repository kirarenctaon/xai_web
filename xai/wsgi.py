"""
WSGI config for xai project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/var/www/xai_web')
sys.path.append('/var/www/xai_web/xai')
sys.path.append('./myvenv/lib/python3.6/site-packages')


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xai.settings')
application = get_wsgi_application()
