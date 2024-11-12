data_peminjaman = []

def tambah_peminjaman():
    while True:
        id_peminjaman = input("ID Peminjaman: ")
        if not id_peminjaman:
            print("ID Peminjaman tidak boleh kosong. Silakan isi kembali.")
            continue
        for peminjaman in data_peminjaman:
            if peminjaman['id_peminjaman'] == id_peminjaman:
                print("ID peminjaman sudah ada. Gunakan ID lain.")
                return
        break
    
    while True:
        nama_peminjam = input("Nama Peminjam: ")
        if not nama_peminjam:
            print("Nama Peminjam tidak boleh kosong. Silakan isi kembali.")
            continue
        break
    
    while True:
        judul_buku = input("Judul Buku: ")
        if not judul_buku:
            print("Judul Buku tidak boleh kosong. Silakan isi kembali.")
            continue
        break

    while True:
        tanggal_peminjaman = input("Tanggal Peminjaman (DD-MM-YYYY): ")
        if not tanggal_peminjaman:
            print("Tanggal Peminjaman tidak boleh kosong. Silakan isi kembali.")
            continue
        break
    
    peminjaman = {
        'id_peminjaman': id_peminjaman,
        'nama_peminjam': nama_peminjam,
        'judul_buku': judul_buku,
        'tanggal_peminjaman': tanggal_peminjaman
    }
    
    data_peminjaman.append(peminjaman)
    print("Data peminjaman berhasil ditambahkan.")


def tampilkan_peminjaman():
    if not data_peminjaman:
        print("Belum ada data peminjaman.")
    else:
        print("Daftar Peminjaman Buku:")
        for peminjaman in data_peminjaman:
            print(f"ID: {peminjaman['id_peminjaman']}, Nama Peminjam: {peminjaman['nama_peminjam']}, "
                  f"Judul Buku: {peminjaman['judul_buku']}, Tanggal: {peminjaman['tanggal_peminjaman']}")

def update_peminjaman():
    id_peminjaman = input("Masukkan ID peminjaman yang akan diupdate: ")
    for peminjaman in data_peminjaman:
        if peminjaman['id_peminjaman'] == id_peminjaman:
            print("Masukkan data baru:")
            nama_peminjam = input("Nama Peminjam: ")
            judul_buku = input("Judul Buku: ")
            tanggal_peminjaman = input("Tanggal Peminjaman (DD-MM-YYYY): ")

            peminjaman['nama_peminjam'] = nama_peminjam
            peminjaman['judul_buku'] = judul_buku
            peminjaman['tanggal_peminjaman'] = tanggal_peminjaman
            print("Data peminjaman berhasil diperbarui.")
            return
    print("ID peminjaman tidak ditemukan.")

def hapus_peminjaman():
    id_peminjaman = input("Masukkan ID peminjaman yang akan dihapus: ")
    for peminjaman in data_peminjaman:
        if peminjaman['id_peminjaman'] == id_peminjaman:
            data_peminjaman.remove(peminjaman)
            print("Data peminjaman berhasil dihapus.")
            return
    print("ID peminjaman tidak ditemukan.")

def main():
    while True:
        print("=== Menu Sistem Peminjaman Buku ===")
        print("1. Tambah Peminjaman")
        print("2. Tampilkan Semua Peminjaman")
        print("3. Update Peminjaman")
        print("4. Hapus Peminjaman")
        print("5. Keluar")

        pilihan = input("Pilih menu (1/2/3/4/5): ")

        if pilihan == "1":
            tambah_peminjaman()

        elif pilihan == "2":
            tampilkan_peminjaman()

        elif pilihan == "3":
            update_peminjaman()

        elif pilihan == "4":
            hapus_peminjaman()

        elif pilihan == "5":
            print(" anda Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

main()

