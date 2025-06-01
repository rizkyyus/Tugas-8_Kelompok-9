from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_produk, name='list_produk'),
    path('tambah/', views.tambah_produk, name='tambah_produk'),
    path('edit/<int:id>/', views.edit_produk, name='edit_produk'),
    path('hapus/<int:id>/', views.hapus_produk, name='hapus_produk'),
    path('detail/<int:id>/', views.detail_produk, name='detail_produk'),
]