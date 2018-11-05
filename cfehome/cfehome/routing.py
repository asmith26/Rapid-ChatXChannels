# c.f. urls.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.conf.urls import url

from chat.consumers import ChatConsumer

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    "websocket": AllowedHostsOriginValidator(  # ensure host doing request matches those in settings.ALLOWED_HOSTS
        AuthMiddlewareStack(  # adds ability to get user information within the websocket
            URLRouter(
                [
                    url(r"^messages/(?P<username>[\w.@+-]+)/$", ChatConsumer)  # i.e. ws://ourdomain/<username>
                ]
            )
        )
    )
})
