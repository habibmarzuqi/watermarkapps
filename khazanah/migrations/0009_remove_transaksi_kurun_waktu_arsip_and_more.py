# Generated by Django 4.2.3 on 2023-08-11 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khazanah', '0008_alter_transaksi_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaksi',
            name='kurun_waktu_arsip',
        ),
        migrations.AlterField(
            model_name='transaksi',
            name='waktu_produksi_kertas',
            field=models.DateField(blank=True, null=True),
        ),
    ]
