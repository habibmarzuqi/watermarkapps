# forms.py
from django import forms
from khazanah.models import Transaksi

class TransaksiForm(forms.ModelForm):
    class Meta:
        model = Transaksi
        fields = '__all__'  # Atau tentukan field yang ingin Anda tampilkan dalam form
