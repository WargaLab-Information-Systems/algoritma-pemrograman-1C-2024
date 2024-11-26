# program peminjaman alat untuk penelitian kesehatan
# Membuat dictionary untuk mencatat jumlah alat berdasarkan jenis
alat_kesehatan = {}
alat_yang_dipinjam = set()

# Fungsi tambah alat dengan dua parameter jenis, jumlah dengan type data string
def tambah_alat(nama_alat, jumlah):
    if nama_alat in alat_kesehatan:
        alat_kesehatan[nama_alat] += jumlah
    else:
        alat_kesehatan[nama_alat] = jumlah
    if jumlah > 0:
        alat_yang_dipinjam.add(nama_alat)





# Fungsi kurangi alat dengan dua parameter jenis, jumlah dengan type data string
def kembalikan_alat(nama_alat, jumlah):
    if nama_alat in alat_kesehatan:
        alat_kesehatan[nama_alat] -= jumlah
        if alat_kesehatan[nama_alat] <= 0:
            alat_kesehatan[nama_alat] = 0
    else:
        print(f"Alat {nama_alat} belum pernah dipinjam.")

# Fungsi untuk menukar alat
def tukar_alat(nama_alat_ambil, jumlah_ambil, nama_alat_kembali, jumlah_kembali):
    kembalikan_alat(nama_alat_kembali, jumlah_kembali)
    tambah_alat(nama_alat_ambil, jumlah_ambil)

# Input data secara dinamis
while True:
    print("\nMenu:")
    print("1. Pinjam alat")
    print("2. Kembalikan alat")
    print("3. Tukar alat")
    print("4. Lihat status alat")
    print("5. Keluar")

    pilihan = input("Pilih opsi: ")

    # jika variabel pilihan sama dengan 1 jalankan program di bawah ini
    if pilihan == "1":
        nama_alat = input("Masukkan nama alat: ")
        jumlah = int(input("Masukkan jumlah alat yang dipinjam: "))
        tambah_alat(nama_alat, jumlah)

    # jika variabel pilihan tidak dengan 1 apakah variabel pilihan sama dengan 2 jalankan program di bawah ini
    elif pilihan == "2":
        nama_alat = input("Masukkan nama alat: ")
        jumlah = int(input("Masukkan jumlah alat yang dikembalikan: "))
        kembalikan_alat(nama_alat, jumlah)

    # jika variabel pilihan tidak dengan 2 apakah variabel pilihan sama dengan 3 jalan kan program di bawah ini
    elif pilihan == "3":
        nama_alat_kembali = input("Masukkan nama alat yang dikembalikan: ")
        jumlah_kembali = int(input("Masukkan jumlah alat yang dikembalikan: "))
        nama_alat_ambil = input("Masukkan nama alat yang ingin diambil: ")
        jumlah_ambil = int(input("Masukkan jumlah alat yang diambil: "))
        tukar_alat(nama_alat_ambil, jumlah_ambil, nama_alat_kembali, jumlah_kembali)

    # jika variabel pilihan tidak dengan 3 apakah variabel pilihan sama dengan 4 jalan kan program di bawah ini
    elif pilihan == "4":
        print("\nAlat yang masih dipinjam saat ini:")
        alat_dipinjam_sekarang = {alat: jumlah for alat, jumlah in alat_kesehatan.items() if jumlah > 0}
        for alat, jumlah in alat_dipinjam_sekarang.items():
            print(f"- {alat}: {jumlah} buah")

        print("\nAlat yang pernah dipinjam:")
        print(", ".join(alat_yang_dipinjam))

    elif pilihan == "5":
        print("Terima kasih! Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Coba lagi.")