
# List untuk menyimpan data peminjaman
data_peminjaman = []

# Tambah data peminjaman
def tambah_peminjaman():
    id_peminjaman = input("ID Peminjaman: ")
    nama_peminjam = input("Nama Peminjam: ")
    judul_buku = input("Judul Buku: ")
    tanggal_peminjaman = input("Tanggal Peminjaman (YYYY-MM-DD): ")
    data_peminjaman.append((id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman))
    print("Data peminjaman berhasil ditambahkan.\n")

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
        if data_peminjaman[i][0]== id_peminjaman:
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




nama = [["apel","durian"],["bakso", "mie"]]
print(nama[0][0])