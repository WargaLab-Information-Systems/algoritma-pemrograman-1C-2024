data_peminjaman = []


def tambah_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman: ")
    nama_peminjam = input("Masukkan Nama Peminjam: ")
    judul_buku = input("Masukkan Judul Buku: ")
    tanggal_peminjaman = input("Masukkan Tanggal Peminjaman (YYYY-MM-DD): ")
    peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    data_peminjaman.append(peminjaman)      #digunakan untuk menambahkan data peminjaman ke dalam list data_peminjaman
    print("Data peminjaman berhasil ditambahkan.")

def tampilkan_peminjaman():
    if not data_peminjaman:
        print("Tidak ada data peminjaman.")
    else:
        print("Data Peminjaman Buku:")
        for peminjaman in data_peminjaman:
            print(f"ID: {peminjaman[0]}, Nama: {peminjaman[1]}, Judul Buku: {peminjaman[2]}, Tanggal: {peminjaman[3]}")
    print()     
    
def perbarui_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman yang akan diperbarui: ")
    for i, peminjaman in enumerate(data_peminjaman):
        if peminjaman[0] == id_peminjaman:
            nama_peminjam = input("Masukkan Nama Peminjam baru (kosongkan jika tidak ingin mengubah): ") or peminjaman[1]
            judul_buku = input("Masukkan Judul Buku baru (kosongkan jika tidak ingin mengubah): ") or peminjaman[2]
            tanggal_peminjaman = input("Masukkan Tanggal Peminjaman baru YYYY-MM-DD, (kosongkan jika tidak ingin mengubah): ") or peminjaman[3]
            data_peminjaman[i] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
            print("Data peminjaman berhasil diperbarui.")
            return
    print("ID peminjaman tidak ditemukan.")

def hapus_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman yang akan dihapus: ")
    for i, peminjaman in enumerate(data_peminjaman): #Menggunakan enumerate() membuat kode lebih singkat dan mudah dibaca
        if peminjaman[0] == id_peminjaman:
            del data_peminjaman[i]        #del digunakan untuk menghapus elemen dari list data_peminjaman pada indeks i
            print("Data peminjaman berhasil dihapus.")
            return
    print("ID peminjaman tidak ditemukan.")

while True:
    print("Menu Peminjaman Buku Perpustakaan")
    print("1. Tambah Peminjaman")
    print("2. Tampilkan Semua Peminjaman")
    print("3. Perbarui Peminjaman")
    print("4. Hapus Peminjaman")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tambah_peminjaman()      
    elif pilihan == "2":
        tampilkan_peminjaman()  
    elif pilihan == "3":
        perbarui_peminjaman()    
    elif pilihan == "4":
        hapus_peminjaman()      
    elif pilihan == "5":
        print("Terima kasih! Program selesai.") 
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
=======
# Tambah data peminjaman
def tambah_peminjaman():
    id_peminjaman = input("ID Peminjaman: ")
    nama_peminjam = input("Nama Peminjam: ")
    judul_buku = input("Judul Buku: ")
    tanggal_peminjaman = input("Tanggal Peminjaman (YYYY-MM-DD): ")
    data_peminjaman.append((id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman))
    # list_id.append(id_peminjaman)
    # for i in list_id :
    #     if id_peminjaman == i:
    #         print("ID peminjaman sudah ada, silahkan masukkan ID yang berbeda")
    print("Data peminjaman berhasil ditambahkan.\n")
    
    # return
# Lihat semua data peminjaman
def lihat_peminjaman():
    if data_peminjaman:
        print("\nData Peminjaman:")
        for peminjaman in data_peminjaman:
            print(f"ID: {peminjaman[0]}, Nama: {peminjaman[1]}, Judul: {peminjaman[2]}, Tanggal: {peminjaman[3]}")
    else:
        print("\nBelum ada data peminjaman.\n")
    
    

# Update data peminjaman
def update_peminjaman():
    id_peminjaman = input("ID Peminjaman yang akan diupdate: ")
    for i in range(len(data_peminjaman)):
        if data_peminjaman[i][0] == id_peminjaman:
            nama_peminjam = input("Nama Peminjam Baru: ")
            judul_buku = input("Judul Buku Baru: ")
            tanggal_peminjaman = input("Tanggal Peminjaman Baru (YYYY-MM-DD): ")
            data_peminjaman[i] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
            print("Data peminjaman berhasil diperbarui.\n")
            return

        print("Data peminjaman tidak ditemukan.\n")

# Hapus data peminjaman
def hapus_peminjaman():
    id_peminjaman = input("ID Peminjaman yang akan dihapus: ")
    for i in range(len(data_peminjaman)):
        if data_peminjaman[i][0] == id_peminjaman:
            del data_peminjaman[i]
            print("Data peminjaman berhasil dihapus.\n")
            return
    print("Data peminjaman tidak ditemukan.\n")
# Fungsi utama untuk menjalankan program
def main():
    while True:
        print("=== Sistem Peminjaman Buku ===")
        print("1. Tambah Peminjaman")
        print("2. Lihat Peminjaman")
        print("3. Update Peminjaman")
        print("4. Hapus Peminjaman")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            tambah_peminjaman()
        elif pilihan == "2":
            lihat_peminjaman()
        elif pilihan == "3":
            update_peminjaman()
        elif pilihan == "4":
            hapus_peminjaman()
        elif pilihan == "5":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.\n")

# Jalankan program
main()

