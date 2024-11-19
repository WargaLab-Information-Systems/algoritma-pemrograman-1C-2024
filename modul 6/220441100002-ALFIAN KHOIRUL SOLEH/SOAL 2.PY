# Inisialisasi list kosong untuk menyimpan data peminjaman
peminjaman = []

# Fungsi untuk menambahkan data peminjaman baru
def tambah():
    id = input("ID Peminjaman: ")

    # Validasi ID unik agar tidak ada data dengan ID yang sama
    for p in peminjaman:
        if p[0] == id:
            print("ID sudah ada. Silakan masukkan ID yang berbeda.")
            return
    
    nama = input("Nama Peminjam: ")
    buku = input("Judul Buku: ")
    tanggal = input("Tanggal Pinjam (dd-mm-yyyy): ")

    # Menyimpan data sebagai tuple
    data = (id, nama, buku, tanggal)
    peminjaman.append(data)
    print("Data berhasil ditambahkan!")

# Fungsi untuk melihat semua data peminjaman
def lihat():
    if not peminjaman:
        print("Belum ada data peminjaman.")
        return
    
    print("\nDaftar Peminjaman:")
    print("ID\tNama\t\tJudul Buku\t\tTanggal")
    print("-" * 50)
    for p in peminjaman:
        print(f"{p[0]}\t{p[1]:<15}\t{p[2]:<20}\t{p[3]}")
    print("-" * 50)

# Fungsi untuk mengupdate data peminjaman berdasarkan ID
def update():
    id = input("Masukkan ID yang akan diupdate: ")
    
    for i, p in enumerate(peminjaman):
        if p[0] == id:
            print("Data ditemukan. Masukkan data baru:")
            nama = input("Nama baru: ")
            buku = input("Judul buku baru: ")
            tanggal = input("Tanggal baru (dd-mm-yyyy): ")

            # Memperbarui data dengan data baru
            peminjaman[i] = (id, nama, buku, tanggal)
            print("Data berhasil diupdate!")
            return
    
    print("ID tidak ditemukan.")

# Fungsi untuk menghapus data peminjaman berdasarkan ID
def hapus():
    id = input("Masukkan ID yang akan dihapus: ")
    
    for i, p in enumerate(peminjaman):
        if p[0] == id:
            peminjaman.pop(i)  # Menghapus data peminjaman dari list
            print("Data berhasil dihapus!")
            return
    
    print("ID tidak ditemukan.")

# Fungsi untuk mencari data peminjaman berdasarkan ID atau nama peminjam
def cari():
    keyword = input("Masukkan ID atau Nama Peminjam untuk dicari: ")
    
    results = [p for p in peminjaman if keyword.lower() in p[0].lower() or keyword.lower() in p[1].lower()]
    if results:
        print("\nHasil Pencarian:")
        for p in results:
            print(f"ID: {p[0]}, Nama: {p[1]}, Buku: {p[2]}, Tanggal: {p[3]}")
    else:
        print("Data tidak ditemukan.")

# Menu utama
while True:
    print("\nMenu:")
    print("1. Tambah Peminjaman")
    print("2. Lihat Peminjaman")
    print("3. Update Peminjaman")
    print("4. Hapus Peminjaman")
    print("5. Cari Peminjaman")
    print("6. Keluar")
    
    pilihan = input("Pilih menu (1-6): ")
    
    if pilihan == '1':
        tambah()
    elif pilihan == '2':
        lihat()
    elif pilihan == '3':
        update()
    elif pilihan == '4':
        hapus()
    elif pilihan == '5':
        cari()
    elif pilihan == '6':
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")
