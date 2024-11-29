# List untuk menyimpan data peminjaman
peminjaman_list = []

# Fungsi untuk menambah data peminjaman (Create)
def tambah_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman: ")
    nama_peminjam = input("Masukkan Nama Peminjam: ")
    judul_buku = input("Masukkan Judul Buku: ")
    tanggal_peminjaman = input("Masukkan Tanggal Peminjaman (dd-mm-yyyy): ")
    peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    peminjaman_list.append(peminjaman)
    print("Peminjaman berhasil ditambahkan.")

# Fungsi untuk menampilkan data peminjaman (Read)
def lihat_peminjaman():
    if peminjaman_list:
        print("\nDaftar Peminjaman Buku:")
        for peminjaman in peminjaman_list:
            print(f"ID: {peminjaman[0]}, Nama: {peminjaman[1]}, Buku: {peminjaman[2]}, Tanggal: {peminjaman[3]}")
    else:
        print("Tidak ada data peminjaman.")

# Fungsi untuk mengupdate data peminjaman (Update)
def update_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin diubah: ")
    for i, peminjaman in enumerate(peminjaman_list):
        if peminjaman[0] == id_peminjaman:
            nama_peminjam = input("Masukkan Nama Peminjam baru: ")
            judul_buku = input("Masukkan Judul Buku baru: ")
            tanggal_peminjaman = input("Masukkan Tanggal Peminjaman baru (dd-mm-yyyy): ")
            peminjaman_list[i] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
            print("Data peminjaman berhasil diubah.")
            return
    print("ID peminjaman tidak ditemukan.")

# Fungsi untuk menghapus data peminjaman (Delete)
def hapus_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin dihapus: ")
    for i, peminjaman in enumerate(peminjaman_list):
        if peminjaman[0] == id_peminjaman:
            del peminjaman_list[i]
            print("Peminjaman berhasil dihapus.")
            return
    print("ID peminjaman tidak ditemukan.")

# Fungsi utama untuk menampilkan menu
def menu():
    while True:
        print("\n--- Menu Sistem Peminjaman Buku ---")
        print("1. Tambah Peminjaman (Create)")
        print("2. Lihat Peminjaman (Read)")
        print("3. Update Peminjaman (Update)")
        print("4. Hapus Peminjaman (Delete)")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            tambah_peminjaman()
        elif pilihan == '2':
            lihat_peminjaman()
        elif pilihan == '3':
            update_peminjaman()
        elif pilihan == '4':
            hapus_peminjaman()
        elif pilihan == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

# Menjalankan program
menu()
