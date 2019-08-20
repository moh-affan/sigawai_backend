from django.urls import path
from authmgmt.views import LoginApiView, UserApiView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from rest_framework_simplejwt.authentication import JWTAuthentication

urlpatterns = [
    # api
    path('api/login', LoginApiView.as_view()),

    # JWT
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),

    # test api
    path('api/users', UserApiView.as_view(), name="api.users"),
]
