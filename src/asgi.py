"""
ASGI config for gen-3f327ca1-e4a4-436a-af49-5491f92fe082 project.

It exposes the ASGI callable as a module-level variable named `application`.

For more information on this file, see:
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import myapp.routing  # Assuming 'myapp' is the Django app where websocket routing is defined

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gen-3f327ca1-e4a4-436a-af49-5491f92fe082.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            myapp.routing.websocket_urlpatterns  # Ensure you have defined websocket_urlpatterns in myapp/routing.py
        )
    ),
})
