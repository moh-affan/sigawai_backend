from channels.auth import AuthMiddlewareStack
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AnonymousUser
import re
from django.db import close_old_connections


class TokenAuthMiddleware:
    """
    Token authorization middleware for Django Channels 2
    """

    def __init__(self, inner):
        self.inner = inner

    def __call__(self, scope):
        headers = dict(scope['headers'])
        # print(headers)
        if b'cookie' in headers:
            try:
                cookies = headers[b'cookie'].decode()
                # print(cookies)
                token_key = re.search("authorization=(.*)(; )?", cookies).group(1)
                # print(token_key)
                if token_key:
                    token = Token.objects.get(key=token_key)
                    scope["user"] = token.user
                    # print(token.user)
                    # close_old_connections()
            except Token.DoesNotExist:
                scope['user'] = AnonymousUser()
        return self.inner(scope)


def TokenAuthMiddlewareStack(inner): return TokenAuthMiddleware(AuthMiddlewareStack(inner))
