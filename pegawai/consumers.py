from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework import mixins
from djangochannelsrestframework.permissions import IsAuthenticated
from rest_framework import status

from apichannels.consumers import GenericAsyncBroadcastAPIConsumer
from apichannels.mixins import SubscribeModelMixin
from .models import Pegawai
from .serializers import PegawaiSrlz


class PegawaiApiCsr(mixins.ListModelMixin,
                    SubscribeModelMixin,
                    GenericAsyncBroadcastAPIConsumer):
    queryset = Pegawai.objects.all()
    serializer_class = PegawaiSrlz
    permission_classes = [IsAuthenticated]
