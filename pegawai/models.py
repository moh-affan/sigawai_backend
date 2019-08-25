from django.contrib.auth.models import User
from django.db import models

# Create your models here.


GENDER = (('LAKI-LAKI', 'Laki-Laki'), ('PEREMPUAN', 'Perempuan'))
AGAMA = (('ISLAM', 'Islam'), ('KRISTEN KATOLIK', 'Kristen Katolik'), ('KRISTEN PROTESTAN', 'Kristen Protestan'))
STATUS_PERKAWINAN = (('KAWIN', 'Kawin'), ('BELUM KAWIN', 'Belum Kawin'), ('JANDA', 'Janda'), ('DUDA', 'Duda'))
JENJANG = (
    ('SD', 'SD'), ('MI', 'MI'), ('SMP', 'SMP'), ('MTS', 'MTs'), ('SMA', 'SMA'), ('SMK', 'SMK'), ('SMEA', 'SMEA'),
    ('STM', 'STM'), ('MA', 'MA'), ('MAK', 'MAK'), ('D1', 'D1'), ('D2', 'D2'), ('D3', 'D3'), ('D4', 'D4'),
    ('S1', 'S1'), ('S2', 'S2'), ('S3', 'S3'))
JENIS_PENDIDIKAN = (('SWASTA', 'SWASTA'), ('NEGERI', 'NEGERI'))
JENIS_AKREDITASI = (('-', '-'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'))
STATUS_HIDUP = (('HIDUP', 'Hidup'), ('MATI', 'Mati'))


class Pegawai(models.Model):
    nik = models.CharField(max_length=16, primary_key=True, unique=True)
    nama = models.CharField(max_length=100)
    tempat_lahir = models.CharField(max_length=100)
    tgl_lahir = models.DateField()
    jenis_kelamin = models.CharField(choices=GENDER, max_length=20)
    alamat = models.CharField(max_length=100)
    rt = models.CharField(max_length=3)
    rw = models.CharField(max_length=3)
    desa_kelurahan = models.CharField(max_length=20)
    kecamatan = models.CharField(max_length=20)
    kabupbaten_kota = models.CharField(max_length=20)
    provinsi = models.CharField(max_length=20)
    agama = models.CharField(choices=AGAMA, max_length=20)
    status_perkawinan = models.CharField(choices=STATUS_PERKAWINAN, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="created_pegawai", null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="updated_pegawai", null=True)

    def __str__(self):
        return "{ '{}':'{}' }".format(self.nik, self.nama)


class RiwayatPendidikan(models.Model):
    pegawai = models.ForeignKey(Pegawai, on_delete=models.CASCADE, related_name='riwayat_pendidikan')
    jenis = models.CharField(choices=JENIS_PENDIDIKAN, max_length=20)
    jurusan_prodi = models.CharField(max_length=50, null=True, blank=True)
    akreditasi = models.CharField(choices=JENIS_PENDIDIKAN, max_length=20)
    nama_instansi = models.CharField(max_length=50)
    alamat_instansi = models.CharField(max_length=200)
    no_ijazah = models.CharField(max_length=50)
    gelar_depan = models.CharField(max_length=10, blank=True, null=True)
    gelar_belakang = models.CharField(max_length=10, blank=True, null=True)
    tgl_ijazah = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="created_riwayat_pendidikan", null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="updated_riwayat_pendidikan", null=True)

    def __str__(self):
        return "{ '{}':'{}' }".format(self.pk, self.jenis)


class RiwayatKeluarga(models.Model):
    pegawai = models.ForeignKey(Pegawai, on_delete=models.CASCADE, related_name='riwayat_keluarga')
    nik = models.CharField(max_length=16, unique=True)
    nip = models.CharField(max_length=18, blank=True, null=True)
    nama = models.CharField(max_length=100)
    tempat_lahir = models.CharField(max_length=100)
    tgl_lahir = models.DateField()
    jenis_kelamin = models.CharField(choices=GENDER, max_length=20)
    pekerjaan = models.CharField(max_length=100)
    institusi = models.CharField(max_length=100)
    status_perkawinan = models.CharField(choices=STATUS_PERKAWINAN, max_length=20)
    no_akte = models.CharField(max_length=20)
    tgl_akte = models.DateField()
    hubungan = models.CharField(max_length=20)
    status_hidup = models.CharField(choices=STATUS_HIDUP, max_length=10)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="created_riwayat_keluarga", null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="updated_riwayat_keluarga", null=True)

    def __str__(self):
        return "{ '{}':'{}' }".format(self.pk, self.nama)
