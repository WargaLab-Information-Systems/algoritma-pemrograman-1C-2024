class PeminjamanBuku:
    def __init__(self, id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman):
        self.id_peminjaman = id_peminjaman
        self.nama_peminjam = nama_peminjam
        self.judul_buku = judul_buku
        self.tanggal_peminjaman = tanggal_peminjaman

    def __str__(self):
        return f"ID Peminjaman: {self.id_peminjaman}, Nama Peminjam: {self.nama_peminjam}, Judul Buku: {self.judul_buku}, Tanggal Peminjaman: {self.tanggal_peminjaman}"

peminjaman_list = []

def create_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman: ")
    nama_peminjam = input("Masukkan Nama Peminjam: ")
    judul_buku = input("Masukkan Judul Buku: ")
    tanggal_peminjaman = input("Masukkan Tanggal Peminjaman: ")
    peminjaman = PeminjamanBuku(id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    peminjaman_list.append(peminjaman)
    print("Data peminjaman telah ditambahkan.")

def read_peminjaman():
    if peminjaman_list:
        print("Data Peminjaman Buku:")
        for peminjaman in peminjaman_list:
            print(peminjaman)
    else:
        print("Tidak ada data peminjaman buku.")

def update_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin diupdate: ")
    for peminjaman in peminjaman_list:
        if peminjaman.id_peminjaman == id_peminjaman:
            peminjaman.nama_peminjam = input("Masukkan Nama Peminjam baru: ")
            peminjaman.judul_buku = input("Masukkan Judul Buku baru: ")
            peminjaman.tanggal_peminjaman = input("Masukkan Tanggal Peminjaman baru: ")
            print("Data peminjaman telah diperbarui.")
            return
    print("ID peminjaman tidak ditemukan.") #ID yang mereka masukkan tidak valid dan tidak ada peminjaman yang sesuai untuk diperbarui.

def delete_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin dihapus: ")
    global peminjaman_list
    peminjaman_list = [p for p in peminjaman_list if p.id_peminjaman != id_peminjaman] #membuat list baru dalam kondisi tertentu
    print("Data peminjaman telah dihapus.")

def main():
    while True:
        print("\nMenu:")
        print("1. Tambah Peminjaman")
        print("2. Tampilkan Peminjaman")
        print("3. Update Peminjaman")
        print("4. Hapus Peminjaman")
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
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()