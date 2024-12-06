peminjaman_buku = []

def tambah_peminjaman():
    while True:
        id_peminjaman = input("Masukkan id Peminjaman: ")

        if any(peminjaman[0] == id_peminjaman for peminjaman in peminjaman_buku):
            print("ID peminjaman sudah ada. Silakan masukkan ID yang berbeda.")
            continue 
        nama_peminjam = input("masukkan Nama Peminjam : ")
        judul_buku = input("masukkan Judul Buku : ")
        tanggal_peminjaman = input("masukkan Tanggal Peminjaman : ")       
        peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
        peminjaman_buku.append(peminjaman)
        print("Data peminjaman berhasil ditambahkan.")
        break

def lihat_peminjaman():
    if not peminjaman_buku:
        print("Belum ada data peminjaman.")
    else:
        for peminjaman in peminjaman_buku:
            print(f"ID: {peminjaman[0]}, Nama: {peminjaman[1]}, Judul Buku: {peminjaman[2]}, Tanggal: {peminjaman[3]}")

def update_pinjaman():
    if not peminjaman_buku:
        print("Tidak ada data peminjaman untuk diupdate.")
        return 
    
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin diupdate: ")
    for index, peminjaman in enumerate(peminjaman_buku):
        if peminjaman[0] == id_peminjaman:
            print(f"Data lama: ID: {peminjaman[0]}, Nama: {peminjaman[1]}, Judul Buku: {peminjaman[2]}, Tanggal: {peminjaman[3]}")
            
            id_peminjaman = input("Masukkan ID Peminjaman baru: ")
            nama_peminjam = input("Masukkan Nama Peminjam baru: ")
            judul_buku = input("Masukkan Judul Buku baru: ")
            tanggal_peminjaman = input("Masukkan Tanggal Peminjaman baru: ")
            peminjaman_buku[index] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
            print("Data peminjaman berhasil diupdate.")
            return
    
    print("ID peminjaman tidak ditemukan.")
def hapus_peminjaman():
    if not peminjaman_buku:
        print("Tidak ada data peminjaman untuk dihapus.")
        return 
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin dihapus: ")
    for peminjaman in peminjaman_buku:
        if peminjaman[0] == id_peminjaman:
            peminjaman_buku.remove(peminjaman)
            print(f"Data peminjaman dengan ID {id_peminjaman} berhasil dihapus.")
            return 
    print("ID peminjaman tidak ditemukan.")

def main():
    while True:
        print("1. Tambah Peminjaman")
        print("2. Lihat Peminjaman")
        print("3. update peminjaman")
        print("4. Hapus Peminjaman")
        print("5. Keluar")
        pilihan = input("Pilih menu (1/2/3/4/5): ")

        if pilihan == '1':
            tambah_peminjaman()
        elif pilihan == '2':
            lihat_peminjaman()
        elif pilihan == '3':
            update_pinjaman()
        elif pilihan == '4':
            hapus_peminjaman()
        elif pilihan == '5':
            print("Terima kasih program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()
