# Program Sistem Peminjaman Buku
# List untuk menyimpan data peminjaman
data_peminjaman = []

# Fungsi untuk menambah peminjaman baru (Create)
def tambah_peminjaman():
    print("--- Tambah Data Peminjaman ---")
    id_peminjaman = input("Masukkan ID Peminjaman: ")
    nama_peminjam = input("Masukkan Nama Peminjam: ")
    judul_buku = input("Masukkan Judul Buku: ")
    tanggal_peminjaman = input("Masukkan Tanggal Peminjaman (dd-mm-yyyy): ")

    # Menyimpan data peminjaman sebagai tuple
    peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    data_peminjaman.append(peminjaman)
    print("Data peminjaman berhasil ditambahkan!")

# Fungsi untuk menampilkan semua data peminjaman (Read)
def lihat_peminjaman():
    print("--- Daftar Data Peminjaman ---")
    if len(data_peminjaman) == 0:
        print("Belum ada data peminjaman.")
    else:
        for peminjaman in data_peminjaman:
            print(f"ID: {peminjaman[0]}, Nama: {peminjaman[1]}, Judul Buku: {peminjaman[2]}, Tanggal: {peminjaman[3]}")

# Fungsi untuk mengupdate data peminjaman (Update)
def update_peminjaman():
    print("--- Update Data Peminjaman ---")
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin diupdate: ")

    # Mencari data peminjaman berdasarkan ID
    found = False
    for i in range(len(data_peminjaman)):
        if data_peminjaman[i][0] == id_peminjaman:
            found = True
            nama_peminjam = input("Masukkan Nama Peminjam baru: ")
            judul_buku = input("Masukkan Judul Buku baru: ")
            tanggal_peminjaman = input("Masukkan Tanggal Peminjaman baru (dd-mm-yyyy): ")

            # Memperbarui data dengan tuple baru
            data_peminjaman[i] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
            print("Data peminjaman berhasil diperbarui!")
            break

    if not found:
        print("Data peminjaman tidak ditemukan.")

# Fungsi untuk menghapus data peminjaman (Delete)
def hapus_peminjaman():
    print("--- Hapus Data Peminjaman ---")
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin dihapus: ")

    # Mencari dan menghapus data peminjaman berdasarkan ID
    found = False
    for i in range(len(data_peminjaman)):
        if data_peminjaman[i][0] == id_peminjaman:
            found = True
            del data_peminjaman[i]
            print("Data peminjaman berhasil dihapus!")
            break

    if not found:
        print("Data peminjaman tidak ditemukan.")

# Fungsi utama untuk menjalankan program
def main():
    print("=== Sistem Peminjaman Buku Perpustakaan ===")
    while True:
        print("\nPilih menu:")
        print("1. Tambah Data Peminjaman")
        print("2. Lihat Data Peminjaman")
        print("3. Update Data Peminjaman")
        print("4. Hapus Data Peminjaman")
        print("5. Keluar")
        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            tambah_peminjaman()
        elif pilihan == "2":
            lihat_peminjaman()
        elif pilihan == "3":
            update_peminjaman()
        elif pilihan == "4":
            hapus_peminjaman()
        elif pilihan == "5":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program
main()
