from django.urls import path
from authmgmt.views import LoginApiView

urlpatterns = [
    # api
    path('api/login', LoginApiView.as_view()),
]
