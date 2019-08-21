from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from pegawai.models import Pegawai

JENIS_GOLONGAN = (('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV'))
JENIS_RUANG = (('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd'))


class Jabatan(models.Model):
    jabatan = models.CharField(max_length=20)
    is_struktural = models.BooleanField(default=False)
    kelas_jabatan = models.PositiveIntegerField(max_length=15)
    eselon = models.CharField(max_length=4)

    def __str__(self):
        return "{ '{}':'{}' }".format(self.pk, self.jabatan)


class Pangkat(models.Model):
    pangkat = models.CharField(max_length=20)
    golongan = models.CharField(choices=JENIS_GOLONGAN)
    ruang = models.CharField(choices=JENIS_RUANG)

    def __str__(self):
        return "{ '{}':'{}' }".format(self.pk, self.pangkat)


class ASN(models.Model):
    nip = models.CharField(max_length=18, primary_key=True, unique=True)
    nip_lama = models.CharField(max_length=18, default='-')
    pegawai = models.ForeignKey(Pegawai, related_name='asn', on_delete=models.CASCADE)
    tmt_cpns = models.DateField()
    tmt_pns = models.DateField()
    no_sk_cpns = models.CharField(max_length=50)
    no_sk_pns = models.CharField(max_length=50)
    is_cpns = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="created_asn", null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="updated_asn", null=True)

    def __str__(self):
        return "{ '{}':'{}' }".format(self.pk, self.pegawai)


class RiwayatJabatan(models.Model):
    asn = models.ForeignKey(ASN, on_delete=models.CASCADE, related_name='riwayat_jabatan')
    tmt = models.DateField()
    jabatan = models.ForeignKey(Jabatan, on_delete=models.SET_NULL, related_name='riwayat_jabatan')
    no_sk = models.CharField(max_length=50)
    tgl_sk = models.DateField()
    nama_pejabat = models.CharField(max_length=50)
    jabatan_pejabat = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="created_riwayat_jabatan", null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="updated_riwayat_jabatan", null=True)

    def __str__(self):
        return "{ '{}':'{}' }".format(self.pk, self.asn)


class RiwayatPangkat(models.Model):
    asn = models.ForeignKey(ASN, on_delete=models.CASCADE, related_name='riwayat_jabatan')
    tmt = models.DateField()
    pangkat = models.ForeignKey(Pangkat, on_delete=models.SET_NULL, related_name='riwayat_pangkat')
    no_sk = models.CharField(max_length=50)
    tgl_sk = models.DateField()
    nama_pejabat = models.CharField(max_length=50)
    jabatan_pejabat = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="created_riwayat_pangkat", null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="updated_riwayat_pangkat", null=True)

    def __str__(self):
        return "{ '{}':'{}' }".format(self.pk, self.asn)
