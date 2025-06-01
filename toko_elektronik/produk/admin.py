from django.contrib import admin
from .models import Produk

@admin.register(Produk)
class ProdukAdmin(admin.ModelAdmin):
    list_display = ['nama', 'kategori', 'harga', 'stok', 'tersedia', 'tanggal_dibuat']
    list_filter = ['kategori', 'tersedia', 'tanggal_dibuat']
    search_fields = ['nama', 'deskripsi']
    list_editable = ['tersedia', 'stok']