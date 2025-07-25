"""
WSGI config for gen-3f327ca1-e4a4-436a-af49-5491f92fe082 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gen-3f327ca1-e4a4-436a-af49-5491f92fe082.settings')

application = get_wsgi_application()