from django.db import models

class Produk(models.Model):
    KATEGORI_CHOICES = [
        ('smartphone', 'Smartphone'),
        ('laptop', 'Laptop'),
        ('tablet', 'Tablet'),
        ('headphone', 'Headphone'),
        ('speaker', 'Speaker'),
        ('smartwatch', 'Smartwatch'),
        ('camera', 'Camera'),
        ('gaming', 'Gaming'),
    ]
    
    nama = models.CharField(max_length=100, verbose_name="Nama Produk")
    kategori = models.CharField(max_length=20, choices=KATEGORI_CHOICES, verbose_name="Kategori")
    harga = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Harga (Rp)")
    stok = models.PositiveIntegerField(default=0, verbose_name="Stok")
    deskripsi = models.TextField(blank=True, verbose_name="Deskripsi")
    tersedia = models.BooleanField(default=True, verbose_name="Tersedia")
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)
    tanggal_diupdate = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Produk"
        verbose_name_plural = "Produk"
        ordering = ['-tanggal_dibuat']
    
    def __str__(self):
        return f"{self.nama} - Rp {self.harga:,.0f}"