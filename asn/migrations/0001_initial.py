# Generated by Django 2.2.1 on 2019-08-21 07:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pegawai', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ASN',
            fields=[
                ('nip', models.CharField(max_length=18, primary_key=True, serialize=False, unique=True)),
                ('nip_lama', models.CharField(default='-', max_length=18)),
                ('tmt_cpns', models.DateField()),
                ('tmt_pns', models.DateField()),
                ('no_sk_cpns', models.CharField(max_length=50)),
                ('no_sk_pns', models.CharField(max_length=50)),
                ('is_cpns', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_asn', to=settings.AUTH_USER_MODEL)),
                ('pegawai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asn', to='pegawai.Pegawai')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_asn', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Jabatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jabatan', models.CharField(max_length=20)),
                ('is_struktural', models.BooleanField(default=False)),
                ('kelas_jabatan', models.PositiveIntegerField()),
                ('eselon', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Pangkat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pangkat', models.CharField(max_length=20)),
                ('golongan', models.CharField(choices=[('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV')], max_length=50)),
                ('ruang', models.CharField(choices=[('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RiwayatPangkat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmt', models.DateField()),
                ('no_sk', models.CharField(max_length=50)),
                ('tgl_sk', models.DateField()),
                ('nama_pejabat', models.CharField(max_length=50)),
                ('jabatan_pejabat', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('asn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='riwayat_pangkat', to='asn.ASN')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_riwayat_pangkat', to=settings.AUTH_USER_MODEL)),
                ('pangkat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='riwayat', to='asn.Pangkat')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_riwayat_pangkat', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RiwayatJabatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmt', models.DateField()),
                ('no_sk', models.CharField(max_length=50)),
                ('tgl_sk', models.DateField()),
                ('nama_pejabat', models.CharField(max_length=50)),
                ('jabatan_pejabat', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('asn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='riwayat_jabatan', to='asn.ASN')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_riwayat_jabatan', to=settings.AUTH_USER_MODEL)),
                ('jabatan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='riwayat', to='asn.Jabatan')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_riwayat_jabatan', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
