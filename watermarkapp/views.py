# views.py
from django.shortcuts import render

# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from khazanah.models import Transaksi,MotifWatermark
from .forms import TransaksiForm
from django.db.models import Q

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Ganti 'home' dengan rute URL halaman setelah login
        else:
            error_message = "Username atau password salah."
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')
@login_required
def home_view(request):
    return render(request, 'home.html', {'user': request.user})

def transaksi_list(request):
    transaksi_data = Transaksi.objects.all()
    return render(request, 'transaksi_list.html', {'transaksi_data': transaksi_data})

def tambah_transaksi(request):
    if request.method == 'POST':
        form = TransaksiForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('transaksi-list')  # Ganti dengan rute URL lihat data transaksi
    else:
        form = TransaksiForm()
    return render(request, 'tambah_transaksi.html', {'form': form})

def edit_transaksi(request, transaksi_id):
    transaksi = get_object_or_404(Transaksi, pk=transaksi_id)
    if request.method == 'POST':
        form = TransaksiForm(request.POST, request.FILES, instance=transaksi)
        if form.is_valid():
            form.save()
            return redirect('transaksi-list')  # Ganti dengan rute URL lihat data transaksi
    else:
        form = TransaksiForm(instance=transaksi)
    return render(request, 'edit_transaksi.html', {'form': form})

def hapus_transaksi(request, transaksi_id):
    transaksi = get_object_or_404(Transaksi, pk=transaksi_id)
    transaksi.delete()
    return redirect('transaksi-list')  # Ganti dengan rute URL lihat data transaksi


####pencarian

def search_results(request):
    search_query = request.GET.get('search_query')
    filter_motif_watermark = request.GET.getlist('motif_watermark')
    selected_motif_watermarks = filter_motif_watermark
    search_results = None
    if search_query or filter_motif_watermark:
        search_results = Transaksi.objects.all()


    if search_query:
        # Membuat query kompleks dengan menggunakan Q objects
        search_results = search_results.filter(

            Q(nomor_inventaris__icontains=search_query) |
            Q(lokasi_penggunaan__icontains=search_query) |
            Q(tahun_kurun_waktu__icontains=search_query) |
            Q(bulan_kurun_waktu__icontains=search_query) |
            Q(kurun_waktu_arsip__icontains=search_query) |
            Q(motif_watermark__motif_watermark__icontains=search_query)|
            Q(khazanah__nama_khazanah__icontains=search_query)
        )

    if filter_motif_watermark:
        search_results = search_results.filter(motif_watermark__motif_watermark__in=filter_motif_watermark)

    watermark_options = MotifWatermark.objects.values_list('motif_watermark', flat=True)

    context = {
        'search_results': search_results,
        'watermark_options': watermark_options,
        'selected_motif_watermarks': selected_motif_watermarks,
    }
    return render(request, 'search.html', context)


def detail(request, pk):
    item = get_object_or_404(Transaksi, pk=pk)

    context = {
        'item': item,
    }
    return render(request, 'detail.html', context)

#belajarcommit