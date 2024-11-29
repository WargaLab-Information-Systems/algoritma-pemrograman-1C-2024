data_peminjaman = []
def tambah_peminjaman(data_peminjaman):
    while True:
        id_peminjaman = input("Masukkan ID Peminjaman: ")
        if id_peminjaman:
            break
        print("ID Peminjaman tidak boleh kosong.")
    while True:
        nama_peminjam = input("Masukkan Nama Peminjam: ")
        if nama_peminjam:
            break
        print("Nama Peminjam tidak boleh kosong.")
    while True:
        judul_buku = input("Masukkan Judul Buku: ")
        if judul_buku:
            break
        print("Judul Buku tidak boleh kosong.")
    while True:
        tanggal_peminjaman = input("Masukkan Tanggal Peminjaman: ")
        if tanggal_peminjaman:
            break
        print("Tanggal Peminjaman tidak boleh kosong.")
    peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    data_peminjaman.append(peminjaman)
    print("Peminjaman berhasil ditambahkan.")
def tampilkan_peminjaman(data_peminjaman):
    print("\nData Peminjaman:")
    for peminjaman in data_peminjaman:
        print("ID Peminjaman   :", peminjaman[0])
        print("Nama Peminjam   :", peminjaman[1])
        print("Judul Buku      :", peminjaman[2])
        print("Tanggal Pinjam  :", peminjaman[3])
        print("-" * 20)
def perbarui_peminjaman(data_peminjaman):
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin diperbarui: ")
    peminjaman_ditemukan = None
    for peminjaman in data_peminjaman:
        if peminjaman[0] == id_peminjaman:
            peminjaman_ditemukan = peminjaman
            break
    if peminjaman_ditemukan:
        while True:
            nama_peminjam = input("Masukkan Nama Peminjam baru: ")
            if nama_peminjam:
                break
            print("Nama Peminjam tidak boleh kosong.")
        while True:
            judul_buku = input("Masukkan Judul Buku baru: ")
            if judul_buku:
                break
            print("Judul Buku tidak boleh kosong.")
        while True:
            tanggal_peminjaman = input("Masukkan Tanggal Peminjaman baru: ")
            if tanggal_peminjaman:
                break
            print("Tanggal Peminjaman tidak boleh kosong.")
        data_peminjaman.remove(peminjaman_ditemukan)
        data_peminjaman.append((id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman))
        print("Data peminjaman berhasil diperbarui.")
    else:
        print("ID Peminjaman tidak ditemukan.")
def hapus_peminjaman(data_peminjaman):
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin dihapus: ")
    peminjaman_ditemukan = None
    for peminjaman in data_peminjaman:
        if peminjaman[0] == id_peminjaman:
            peminjaman_ditemukan = peminjaman
            break
    if peminjaman_ditemukan:
        data_peminjaman.remove(peminjaman_ditemukan)
        print("Data peminjaman berhasil dihapus.")
    else:
        print("ID Peminjaman tidak ditemukan.") 
while True:
    print("\nSistem Peminjaman Buku Perpustakaan")
    print("1. Tambah Peminjaman")
    print("2. Tampilkan Peminjaman")
    print("3. Perbarui Peminjaman")
    print("4. Hapus Peminjaman")
    print("5. Keluar")
    pilihan = input("Pilih opsi (1-5): ")
    if pilihan == "1":
        tambah_peminjaman(data_peminjaman)
    elif pilihan == "2":
        tampilkan_peminjaman(data_peminjaman)
    elif pilihan == "3":
        perbarui_peminjaman(data_peminjaman)
    elif pilihan == "4":
        hapus_peminjaman(data_peminjaman)
    elif pilihan == "5":
        print("Terima kasih telah menggunakan sistem ini!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")