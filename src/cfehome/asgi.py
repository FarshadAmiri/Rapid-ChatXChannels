from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from django.urls import re_path, path
from chat.consumers import ChatConsumer
import os
import django
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cfehome.settings')

application = ProtocolTypeRouter({
"http": get_asgi_application(),
"websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                re_path(r"^messages/(?P<username>[\w.@+-]+)/$", ChatConsumer.as_asgi()),
            ])
        )
    )
})