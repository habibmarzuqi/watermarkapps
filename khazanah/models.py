# myapp/models.py
from django.db import models
from django import forms
from django.contrib import admin

class Khazanah(models.Model):
    nama_khazanah = models.CharField(max_length=100)
    lokasi_penggunaan = models.CharField(max_length=200)
    kurun_waktu_arsip = models.CharField(max_length=50)
    jenis_arsip = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_khazanah

class Pabrik(models.Model):
    nama_pabrik = models.CharField(max_length=100)
    negara = models.CharField(max_length=100)
    lokasi = models.CharField(max_length=200)

    def __str__(self):
        return self.nama_pabrik
class JenisKertas(models.Model):
    jenis_kertas = models.CharField(max_length=100)

    def __str__(self):
        return self.jenis_kertas
class KondisiFisikKertas(models.Model):
    kondisi_fisik_kertas = models.CharField(max_length=100)

    def __str__(self):
        return self.kondisi_fisik_kertas

class WarnaKertas(models.Model):
    warna_kertas = models.CharField(max_length=100)

    def __str__(self):
        return self.warna_kertas
class MotifWatermark(models.Model):
    motif_watermark = models.CharField(max_length=100)

    def __str__(self):
        return self.motif_watermark

class PosisiWatermark(models.Model):
    posisi_watermark = models.CharField(max_length=100)

    def __str__(self):
        return self.posisi_watermark

class MotifCountermark(models.Model):
    motif_countermark = models.CharField(max_length=100)

    def __str__(self):
        return self.motif_countermark

class PosisiCountermark(models.Model):
    posisi_countermark = models.CharField(max_length=100)

    def __str__(self):
        return self.posisi_countermark



class Transaksi(models.Model):
    khazanah = models.ForeignKey(Khazanah, on_delete=models.CASCADE, blank=True, null=True)
    nomor_inventaris = models.CharField(max_length=50, blank=True, null=True)
    lokasi_penggunaan = models.CharField(max_length=200,default='-', blank=True, null=True)
    tahun_kurun_waktu = models.PositiveIntegerField(null=True, blank=True)
    bulan_kurun_waktu = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 13)],null=True, blank=True)  # 1 to 12 for months
    kurun_waktu_arsip = models.CharField(max_length=7,null=True, blank=True)  # Format: YYYY-MM (misalnya 2023-08)
    jenis_kertas = models.ForeignKey(JenisKertas, on_delete=models.CASCADE,default='1')
    waktu_produksi_kertas = models.CharField(max_length=200,blank=True, null=True)
    kondisi_fisik_kertas = models.ForeignKey(KondisiFisikKertas, on_delete=models.CASCADE, blank=True, null=True)
    panjang_kertas = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Panjang Kertas (mm)', blank=True, null=True)
    lebar_kertas = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Lebar Kertas (mm)', blank=True, null=True)
    ketebalan_kertas = models.DecimalField(max_digits=10, decimal_places=2,default='',verbose_name='Tebal Kertas (mm)', blank=True, null=True)
    warna_kertas = models.ForeignKey(WarnaKertas, on_delete=models.CASCADE, blank=True, null=True)
    gramatur_kertas = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Gramatur Kertas (gr)', blank=True, null=True)
    tingkat_keasaman = models.CharField(max_length=50, blank=True, null=True)
    jarak_antara_kolom_garis = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    motif_watermark = models.ForeignKey(MotifWatermark, on_delete=models.CASCADE, blank=True, null=True)
    posisi_watermark = models.ForeignKey(PosisiWatermark, on_delete=models.CASCADE, blank=True, null=True)
    panjang_watermark = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Panjang Watermark (mm)', blank=True, null=True)
    lebar_watermark = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Lebar Watermark (mm)', blank=True, null=True)
    motif_countermark = models.ForeignKey(MotifCountermark, on_delete=models.CASCADE, blank=True, null=True)
    posisi_countermark = models.ForeignKey(PosisiCountermark, on_delete=models.CASCADE, blank=True, null=True)
    panjang_countermark = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Panjang Countermark (mm)', blank=True, null=True)
    lebar_countermark = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Lebar Countermark (mm)', blank=True, null=True)
    pabrik_kertas = models.ForeignKey(Pabrik, on_delete=models.CASCADE, blank=True, null=True)

    # Field untuk upload gambar
    gambar_watermark = models.ImageField(upload_to='watermark/',default='default_image.jpg')
    gambar_countermark = models.ImageField(upload_to='countermark/',default='default_image.jpg')
    ukuran_watermark = models.ImageField(upload_to='ukuran_watermark/',default='default_image.jpg')
    ukuran_countermark = models.ImageField(upload_to='ukuran_countermark/',default='default_image.jpg')
    jarak_garis = models.ImageField(upload_to='jarak_garis/',default='default_image.jpg')
    lembar_kertas = models.ImageField(upload_to='lembar_kertas/',default='default_image.jpg')

    def __str__(self):
        return f"Transaksi - {self.nomor_inventaris}"

    class Meta:
        verbose_name_plural = 'Data Watermark'

