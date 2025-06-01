from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Produk

def list_produk(request):
    """Menampilkan daftar semua produk dengan fitur pencarian"""
    query = request.GET.get('q')
    kategori = request.GET.get('kategori')
    
    produk_list = Produk.objects.all()
    
    if query:
        produk_list = produk_list.filter(
            Q(nama__icontains=query) | Q(deskripsi__icontains=query)
        )
    
    if kategori:
        produk_list = produk_list.filter(kategori=kategori)
    
    # Untuk dropdown kategori
    kategori_choices = Produk.KATEGORI_CHOICES
    
    context = {
        'produk_list': produk_list,
        'query': query,
        'kategori_selected': kategori,
        'kategori_choices': kategori_choices,
    }
    return render(request, 'produk/list.html', context)

def tambah_produk(request):
    """Form untuk menambah produk baru"""
    if request.method == 'POST':
        nama = request.POST.get('nama')
        kategori = request.POST.get('kategori')
        harga = request.POST.get('harga')
        stok = request.POST.get('stok')
        deskripsi = request.POST.get('deskripsi')
        tersedia = request.POST.get('tersedia') == 'on'
        
        # Validasi sederhana
        errors = []
        if not nama:
            errors.append('Nama produk wajib diisi!')
        if not kategori:
            errors.append('Kategori wajib dipilih!')
        if not harga:
            errors.append('Harga wajib diisi!')
        if not stok:
            errors.append('Stok wajib diisi!')
            
        if errors:
            context = {
                'errors': errors,
                'nama': nama,
                'kategori': kategori,
                'harga': harga,
                'stok': stok,
                'deskripsi': deskripsi,
                'tersedia': tersedia,
                'kategori_choices': Produk.KATEGORI_CHOICES,
            }
            return render(request, 'produk/form.html', context)
        
        try:
            Produk.objects.create(
                nama=nama,
                kategori=kategori,
                harga=float(harga),
                stok=int(stok),
                deskripsi=deskripsi,
                tersedia=tersedia
            )
            messages.success(request, f'Produk "{nama}" berhasil ditambahkan!')
            return redirect('list_produk')
        except ValueError:
            messages.error(request, 'Harga dan stok harus berupa angka!')
    
    context = {
        'kategori_choices': Produk.KATEGORI_CHOICES,
    }
    return render(request, 'produk/form.html', context)

def edit_produk(request, id):
    """Form untuk edit produk"""
    produk = get_object_or_404(Produk, id=id)
    
    if request.method == 'POST':
        nama = request.POST.get('nama')
        kategori = request.POST.get('kategori')
        harga = request.POST.get('harga')
        stok = request.POST.get('stok')
        deskripsi = request.POST.get('deskripsi')
        tersedia = request.POST.get('tersedia') == 'on'
        
        # Validasi sederhana
        errors = []
        if not nama:
            errors.append('Nama produk wajib diisi!')
        if not kategori:
            errors.append('Kategori wajib dipilih!')
        if not harga:
            errors.append('Harga wajib diisi!')
        if not stok:
            errors.append('Stok wajib diisi!')
            
        if errors:
            context = {
                'errors': errors,
                'produk': produk,
                'kategori_choices': Produk.KATEGORI_CHOICES,
            }
            return render(request, 'produk/edit.html', context)
        
        try:
            produk.nama = nama
            produk.kategori = kategori
            produk.harga = float(harga)
            produk.stok = int(stok)
            produk.deskripsi = deskripsi
            produk.tersedia = tersedia
            produk.save()
            
            messages.success(request, f'Produk "{nama}" berhasil diupdate!')
            return redirect('list_produk')
        except ValueError:
            messages.error(request, 'Harga dan stok harus berupa angka!')
    
    context = {
        'produk': produk,
        'kategori_choices': Produk.KATEGORI_CHOICES,
    }
    return render(request, 'produk/edit.html', context)

def hapus_produk(request, id):
    """Hapus produk dengan konfirmasi"""
    produk = get_object_or_404(Produk, id=id)
    
    if request.method == 'POST':
        nama_produk = produk.nama
        produk.delete()
        messages.success(request, f'Produk "{nama_produk}" berhasil dihapus!')
        return redirect('list_produk')
    
    return render(request, 'produk/hapus.html', {'produk': produk})

def detail_produk(request, id):
    """Menampilkan detail produk"""
    produk = get_object_or_404(Produk, id=id)
    return render(request, 'produk/detail.html', {'produk': produk})