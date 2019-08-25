from rest_framework import serializers

from pegawai.models import Pegawai


class PegawaiSrlz(serializers.ModelSerializer):
    class Meta:
        model = Pegawai
        fields = [field.name for field in Pegawai._meta.fields]
