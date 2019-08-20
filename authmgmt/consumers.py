# from channels.generic.websocket import AsyncJsonWebsocketConsumer
# from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
# from djangochannelsrestframework import mixins
# from djangochannelsrestframework.permissions import IsAuthenticated
# from rest_framework import status

# from settings.models import Menu
# from settings.serializers import MenuSerializer
# from sigawai.consumers import GenericAsyncBroadcastAPIConsumer
# from sigawai.mixins import SubscribeModelMixin


# class MenuApiConsumer(mixins.ListModelMixin, mixins.CreateModelMixin,
#                       mixins.RetrieveModelMixin, SubscribeModelMixin,
#                       GenericAsyncBroadcastAPIConsumer):
#     queryset = Menu.get_menu()
#     serializer_class = MenuSerializer
#     permission_classes = [IsAuthenticated]

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#     def get_queryset(self, **kwargs):
#         if 'pk' in kwargs:
#             return Menu.objects.all()
#         else:
#             return super().get_queryset(**kwargs)

from django.contrib.auth.models import User
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework import mixins
from djangochannelsrestframework.permissions import IsAuthenticated
from rest_framework import status

from apichannels.consumers import GenericAsyncBroadcastAPIConsumer
from apichannels.mixins import SubscribeModelMixin

from .serializers import UserSerializer


class UserApiConsumer(mixins.ListModelMixin,
                      SubscribeModelMixin,
                      GenericAsyncBroadcastAPIConsumer):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
