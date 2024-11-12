pinjam_buku = []
hitung_id = 1
def tambah_peminjaman(nama, judul, tanggal):
    global hitung_id 
    pinjam =[hitung_id, nama, judul, tanggal]
    pinjam_buku.append(pinjam)
    print("Data berhasil ditambahkan")
    hitung_id += 1
def menampilkan_peminjaman():
    if not pinjam_buku:
        print("Belum ada data peminjaman")
    else:
        print("\nDaftar Peminjaman Buku Di Perpustakaan")
        for a, pinjam in enumerate(pinjam_buku, start=1):
            print(f"{a}. ID Peminjaman: {pinjam[0]}, Nama Peminjam: {pinjam[1]}, Judul Buku: {pinjam[2]}, Tanggal Peminjaman: {pinjam[3]}")
def update_peminjaman(id):
    for pinjam in pinjam_buku:
        if pinjam[0] == id:
            print(f"Data lama: [Nama: {pinjam[1]}, Judul: {pinjam[2]}, Tanggal Peminjaman: {pinjam[3]}]")
            nama = input("Masukkan nama peminjam yang baru: ")
            judul = input("Masukkan nama judul buku yang baru: ")
            tanggal = input("Masukkan tanggal peminjman buku yang baru: ")
            pinjam[1] = nama
            pinjam[2] = judul
            pinjam[3] = tanggal
            print("Data peminjaman buku telah diperbarui.")
            return
    print("Peminjaman dengan ID tersebut tidak ditemukan.")
def hapus_peminjaman(id):
    for b, pinjam in enumerate(pinjam_buku):
        if pinjam[0] == id:
            del pinjam_buku[b]
            print("Data peminjaman telah dihapus.")
            return
    print("Peminjaman dengan ID tersebut tidak ditemukan.")
while True:
    print("\nMenu CRUD Peminjaman Buku Di Perpustakaan")
    print("1. Tambah Data Peminjaman Buku")
    print("2. Tampilkan Data Peminjaman Buku")
    print("3. Perbarui Data Peminjaman Buku")
    print("4. Hapus Data Peminjaman Buku")
    print("5. Keluar Program")
    opsi = input("Masukkan pilihan (1-5): ")
    if opsi == "1":
        print("\nMenambahkan Data Peminjaman Buku")
        while True:
            nama = input("Masukkan nama peminjam buku: ")
            if nama.strip():
                break
            print("Nama tidak boleh kosong, harap masukkan Nama.")
        while True:
            judul = input("Masukkan judul buku yang ingin dipinjam: ")
            if judul.strip():
                break
            print("Judul tidak boleh kosong, harap masukkan Judul.")
        while True:
            tanggal = input("Masukkan tanggal peminjaman buku(DD/MM/YYYY): ")
            if tanggal.strip():
                break
            print("Tanggal Peminjaman tidak boleh kososng, harap masukkan Tanggal Peminjaman.")
        tambah_peminjaman(nama, judul, tanggal)
    elif opsi == "2":
        menampilkan_peminjaman()
    elif opsi == "3":
        try:
            id = int(input("Masukkan ID peminjaman buku yang ingin diperbarui: "))
            update_peminjaman(id)
        except ValueError:
            print("ID harus berupa angka")
    elif opsi == "4":
        try:
            id = int(input("Masukkan ID peminjaman buku yang ingin dihapus: "))
            hapus_peminjaman(id)
        except ValueError:
            print("ID harus berupa angka")
    elif opsi == "5":
        print("Program selesai")
        break
    else:
        print("Harap masukkan input yang tersedia")