"""
URL configuration for watermarkapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import login_view, home_view, transaksi_list, tambah_transaksi, edit_transaksi, hapus_transaksi
from django.contrib.auth import views as auth_views  # Impor views autentikasi Django
from . import views


urlpatterns = [
    path('search/', views.search_results, name='search_results'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('home/', home_view, name='home'),

    path('transaksi/', transaksi_list, name='transaksi-list'),
    path('transaksi/tambah/', tambah_transaksi, name='tambah-transaksi'),
    path('transaksi/edit/<int:transaksi_id>/', edit_transaksi, name='edit-transaksi'),
    path('transaksi/hapus/<int:transaksi_id>/', hapus_transaksi, name='hapus-transaksi'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)