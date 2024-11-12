# Daftar peminjaman buku 
peminjaman_list = []

# Fungsi untuk menambahkan data peminjaman (Create)
def create_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman: ")
    nama_peminjam = input("Masukkan Nama Peminjam: ")
    judul_buku = input("Masukkan Judul Buku: ")
    tanggal_peminjaman = input("Masukkan Tanggal Peminjaman (dd-mm-yyyy): ")
    
    peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    peminjaman_list.append(peminjaman)
    print("Peminjaman berhasil ditambahkan!")

# Fungsi untuk menampilkan semua data peminjaman (Read)
def read_peminjaman():
    if peminjaman_list:
        print("Daftar Peminjaman Buku:")
        for peminjaman in peminjaman_list:
            print(f"ID: {peminjaman[0]}, Nama: {peminjaman[1]}, Judul Buku: {peminjaman[2]}, Tanggal Peminjaman: {peminjaman[3]}")
    else:
        print("Tidak ada data peminjaman.")

# Fungsi untuk memperbarui data peminjaman (Update)
def update_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin diupdate: ")
    
    for i in range(len(peminjaman_list)):  
        peminjaman = peminjaman_list[i]
        if peminjaman[0] == id_peminjaman:
            print("Data Peminjaman ditemukan!")
            print(f"ID: {peminjaman[0]}, Nama: {peminjaman[1]}, Judul Buku: {peminjaman[2]}, Tanggal Peminjaman: {peminjaman[3]}")
            
            nama_peminjam = input("Masukkan Nama Peminjam baru: ")
            judul_buku = input("Masukkan Judul Buku baru: ")
            tanggal_peminjaman = input("Masukkan Tanggal Peminjaman baru (dd-mm-yyyy): ")
            
            peminjaman_list[i] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
            print("Peminjaman berhasil diperbarui!")
            return
    
    print("ID Peminjaman tidak ditemukan.")

# Fungsi untuk menghapus data peminjaman (Delete)
def delete_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin dihapus: ")
    
    for i in range(len(peminjaman_list)):  
        peminjaman = peminjaman_list[i]
        if peminjaman[0] == id_peminjaman:
            peminjaman_list.pop(i)
            print("Peminjaman berhasil dihapus!")
            return
    
    print("ID Peminjaman tidak ditemukan.")

# Fungsi untuk menampilkan menu
def menu():
    while True:
        print("--- Sistem Peminjaman Buku ---")
        print("1. Tambah Peminjaman (Create)")
        print("2. Lihat Daftar Peminjaman (Read)")
        print("3. Update Peminjaman (Update)")
        print("4. Hapus Peminjaman (Delete)")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            create_peminjaman()
        elif pilihan == '2':
            read_peminjaman()
        elif pilihan == '3':
            update_peminjaman()
        elif pilihan == '4':
            delete_peminjaman()
        elif pilihan == '5':
            print("Terima kasih telah menggunakan sistem!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

# Menjalankan program
menu()