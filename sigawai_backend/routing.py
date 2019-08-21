from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from apichannels.middlewares import TokenAuthMiddlewareStack

from authmgmt import routing as authm
from pegawai import routing as peg

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
        TokenAuthMiddlewareStack(
            URLRouter(
                authm.websocket_urlpatterns + peg.websocket_urlpatterns
            )
        )
    ),
})
