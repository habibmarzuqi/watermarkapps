from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from .models import Khazanah
from .models import Pabrik
from .models import Transaksi, JenisKertas, KondisiFisikKertas, WarnaKertas, MotifWatermark, PosisiWatermark, MotifCountermark, PosisiCountermark
from django_select2.forms import Select2Widget
from datetime import datetime


current_year = datetime.now().year
YEARS_CHOICES = [(year, year) for year in range(1950, current_year + 1)]
# Ganti judul admin
admin.site.site_header = "DITEKSI"
admin.site.site_title = "DITEKSI"
admin.site.index_title = "Selamat datang di halaman DITEKSI Administrator"

MONTHS_CHOICES = [
    ('1', 'Januari'), ('2', 'Februari'), ('3', 'Maret'),
    ('4', 'April'), ('5', 'Mei'), ('6', 'Juni'),
    ('7', 'Juli'), ('8', 'Agustus'), ('9', 'September'),
    ('10', 'Oktober'), ('11', 'November'), ('12', 'Desember')
]
# Register your models here.

class TransaksiAdminForm(forms.ModelForm):
    tahun_kurun_waktu = forms.IntegerField(widget=Select2Widget(choices=YEARS_CHOICES))
    bulan_kurun_waktu = forms.ChoiceField(choices=MONTHS_CHOICES, widget=Select2Widget)
    khazanah = forms.ModelChoiceField(queryset=Khazanah.objects.all(), widget=Select2Widget)
    jenis_kertas = forms.ModelChoiceField(queryset=JenisKertas.objects.all(),  widget=forms.RadioSelect)
    kondisi_fisik_kertas = forms.ModelChoiceField(queryset=KondisiFisikKertas.objects.all(), widget=forms.RadioSelect)

    class Meta:
        model = Khazanah
        fields = '__all__'

class TransaksiAdmin(admin.ModelAdmin):
    form = TransaksiAdminForm
    list_display = (
    'khazanah', 'nomor_inventaris','get_kurun_waktu_arsip', 'waktu_produksi_kertas', 'kondisi_fisik_kertas', 'panjang_kertas', 'lebar_kertas',
    'warna_kertas', 'gramatur_kertas', 'tingkat_keasaman', 'motif_watermark', 'posisi_watermark', 'panjang_watermark',
    'lebar_watermark', 'motif_countermark', 'posisi_countermark', 'panjang_countermark', 'lebar_countermark',
    'jarak_antara_kolom_garis', 'pabrik_kertas', 'gambar_watermark_tag', 'gambar_countermark_tag')

    list_filter = ('khazanah', 'motif_watermark', 'posisi_watermark', 'motif_countermark', 'posisi_countermark')
    search_fields = ('nomor_inventaris', 'kondisi_fisik_kertas', 'motif_watermark', 'motif_countermark')

    fieldsets = (
        ('Data Arsip', {
            'fields': ('khazanah', 'nomor_inventaris','lokasi_penggunaan','bulan_kurun_waktu','tahun_kurun_waktu', 'jenis_kertas','jarak_antara_kolom_garis')
        }),

        ('Data Lembaran Kertas', {
            'fields': ( 'waktu_produksi_kertas','kondisi_fisik_kertas', 'panjang_kertas', 'lebar_kertas','ketebalan_kertas',
                       'warna_kertas','gramatur_kertas', 'tingkat_keasaman', 'lembar_kertas','jarak_garis','pabrik_kertas')
        }),
        ('Data Watermark', {
            'fields': ('motif_watermark', 'posisi_watermark', 'panjang_watermark', 'lebar_watermark','gambar_watermark','ukuran_watermark')
        }),
        ('Data Countermark', {
            'fields': ('motif_countermark', 'posisi_countermark', 'panjang_countermark', 'lebar_countermark',  'gambar_countermark','ukuran_countermark' )
        }),
    )

    def get_kurun_waktu_arsip(self, obj):
        return f"{obj.tahun_kurun_waktu}-{obj.bulan_kurun_waktu:02}"  # Format: YYYY-MM

        get_kurun_waktu_arsip.short_description = 'Kurun Waktu Arsip'

    def gambar_watermark_tag(self, obj):
        return mark_safe(f'<img src="{obj.gambar_watermark.url}" width="50" height="50" />')

    def gambar_countermark_tag(self, obj):
        return mark_safe(f'<img src="{obj.gambar_countermark.url}" width="50" height="50" />')


admin.site.register(Transaksi, TransaksiAdmin)
admin.site.register(Khazanah)
admin.site.register(Pabrik)
admin.site.register(JenisKertas)
admin.site.register(KondisiFisikKertas)
admin.site.register(WarnaKertas)
admin.site.register(MotifWatermark)
admin.site.register(PosisiWatermark)
admin.site.register(MotifCountermark)
admin.site.register(PosisiCountermark)


