# Daftar buku (Tuple: ID buku, Judul buku)
buku = [(1, "Python untuk Pemula"), (2, "Algoritma dan Struktur Data"), (3, "Kecerdasan Buatan")]

# Daftar peminjaman (List peminjaman)
peminjaman = []

def tambah_peminjaman():
    id_peminjaman = len(peminjaman) # id peminjaman di ambil dari panjang list peminjaman
    nama_peminjam = input("Masukkan nama peminjam: ")
    id_buku = int(input("Masukkan ID buku yang dipinjam: "))
    judul_buku = [buku[i][1] for i in range(len(buku)) if buku[i][0] == id_buku][0]
    tanggal_peminjaman = input("Masukkan tanggal peminjaman (YYYY-MM-DD): ")

    peminjaman.append({ # menambahkan nilai di akhir
        "id": id_peminjaman,
        "nama": nama_peminjam,
        "buku": judul_buku,
        "tanggal": tanggal_peminjaman
    })
    print("Data peminjaman berhasil ditambahkan.")

def lihat_semua_peminjaman():
    if not peminjaman:
        print("Belum ada data peminjaman.")
    else:
        print("Daftar Peminjaman:")
        for peminjaman_data in peminjaman:
            print(f"ID: {peminjaman_data['id']}")
            print(f"Nama Peminjam: {peminjaman_data['nama']}")
            print(f"Buku: {peminjaman_data['buku']}")
            print(f"Tanggal Peminjaman: {peminjaman_data['tanggal']}")

def ubah_peminjaman():
    id_ubah = int(input("Masukkan ID peminjaman yang ingin diubah: "))
    for i, peminjaman_data in enumerate(peminjaman): #untuk membuat kode lebih singkat dan mudah di baca
        if peminjaman_data['id'] == id_ubah:
            nama_baru = input("Masukkan nama peminjam baru (kosongkan jika tidak ingin mengubah): ")
            if nama_baru:
                peminjaman_data['nama'] = nama_baru

            print("Data peminjaman berhasil diubah.")
            return
    print("ID peminjaman tidak ditemukan.")

def hapus_peminjaman():
    id_hapus = int(input("Masukkan ID peminjaman yang ingin dihapus: "))
    for i, peminjaman_data in enumerate(peminjaman): #untuk membuat kode lebih singkat dan mudah di baca
        if peminjaman_data['id'] == id_hapus:
            del peminjaman[i]
            print("Data peminjaman berhasil dihapus.")
            return
    print("ID peminjaman tidak ditemukan.")

# Menu utama
while True:
    print("Menu:")
    print("1. Tambah peminjaman")
    print("2. Lihat semua peminjaman")
    print("3. Ubah data peminjaman")
    print("4. Hapus data peminjaman")
    print("5. keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        tambah_peminjaman()
    elif pilihan == '2':
        lihat_semua_peminjaman()
    elif pilihan == '3':
        ubah_peminjaman()
    elif pilihan == '4':
        hapus_peminjaman()
    elif pilihan == '5':
        break
    else:
        print("Pilihan tidak valid.")