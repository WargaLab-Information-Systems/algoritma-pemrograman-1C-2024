# Fungsi untuk menambah peminjaman
def tambah_peminjaman(alat, jumlah, peminjaman):
    if alat in peminjaman:
        peminjaman[alat] += jumlah
    else:
        peminjaman[alat] = jumlah

# Fungsi untuk mengurangi peminjaman (misalnya untuk pengembalian atau penukaran)
def kurangi_peminjaman(alat, jumlah, peminjaman):
    if alat in peminjaman:
        peminjaman[alat] = max(0, peminjaman[alat] - jumlah)  # Pastikan tidak ada jumlah negatif
    else:
        print(f"Alat {alat} tidak ditemukan dalam daftar peminjaman.")

# Fungsi untuk menukar alat
def tukar_alat(alat_dikembalikan, alat_dipinjam, jumlah_dikembalikan, jumlah_dipinjam, peminjaman):
    kurangi_peminjaman(alat_dikembalikan, jumlah_dikembalikan, peminjaman)
    tambah_peminjaman(alat_dipinjam, jumlah_dipinjam, peminjaman)

# Fungsi untuk menampilkan alat yang dipinjam
def tampilkan_peminjaman(peminjaman):
    print("\nAlat kesehatan yang dipinjam saat ini:")
    for alat, jumlah in peminjaman.items():
        if jumlah > 0:
            print(f"{alat}: {jumlah}")

# Inisialisasi dictionary untuk mencatat alat yang dipinjam oleh Heni
peminjaman = {
    'alat_pengukur_tekanan_darah': 0,
    'termometer': 0,
    'alat_pengukur_kadar_gula_darah': 0,
    'alat_pengukur_tensi': 0
}

# Proses peminjaman, pengembalian, dan penukaran alat secara dinamis
def proses_peminjaman():
    while True:
        print("\nMenu:")
        print("1. Peminjaman alat")
        print("2. Pengembalian alat")
        print("3. Penukaran alat")
        print("4. Tampilkan peminjaman saat ini")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4/5): ")
        
        if pilihan == '1':
            alat = input("Masukkan nama alat yang dipinjam (contoh: alat_pengukur_tekanan_darah): ")
            jumlah = int(input(f"Masukkan jumlah {alat} yang dipinjam: "))
            tambah_peminjaman(alat, jumlah, peminjaman)
        
        elif pilihan == '2':
            alat = input("Masukkan nama alat yang dikembalikan: ")
            jumlah = int(input(f"Masukkan jumlah {alat} yang dikembalikan: "))
            kurangi_peminjaman(alat, jumlah, peminjaman)
        
        elif pilihan == '3':
            alat_dikembalikan = input("Masukkan nama alat yang dikembalikan: ")
            jumlah_dikembalikan = int(input(f"Masukkan jumlah {alat_dikembalikan} yang dikembalikan: "))
            alat_dipinjam = input("Masukkan nama alat yang dipinjam sebagai pengganti: ")
            jumlah_dipinjam = int(input(f"Masukkan jumlah {alat_dipinjam} yang dipinjam sebagai pengganti: "))
            tukar_alat(alat_dikembalikan, alat_dipinjam, jumlah_dikembalikan, jumlah_dipinjam, peminjaman)
        
        elif pilihan == '4':
            tampilkan_peminjaman(peminjaman)
        
        elif pilihan == '5':
            print("Terima kasih! Program selesai.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

# Menjalankan proses peminjaman
proses_peminjaman()
