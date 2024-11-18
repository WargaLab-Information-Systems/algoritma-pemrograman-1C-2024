# # program peminjaman alat untuk penelitian kesehatan
# # Membuat dictionary untuk mencatat jumlah alat berdasarkan jenis
# alat = {}

# # Fungsi tambah alat dengan dua parameter jenis, jumlah dengan type data string
# def tambah_alat(jenis, jumlah):
#     if jenis in alat:
#         alat[jenis] += jumlah
#     else:
#         alat[jenis] = jumlah

# # Fungsi kurangi alat dengan dua parameter jenis, jumlah dengan type data string
# def kurangi_alat(jenis, jumlah):
#     if jenis in alat:
#         alat[jenis] -= jumlah
#         if alat[jenis] <= 0:
#             del alat[jenis]  # Hapus jika jumlah 0 atau negatif

# # Fungsi untuk tukar alat
# def tukar_alat(jenis_dikembalikan, jumlah_dikembalikan, jenis_dipinjam, jumlah_dipinjam):
#     kurangi_alat(jenis_dikembalikan, jumlah_dikembalikan)
#     tambah_alat(jenis_dipinjam, jumlah_dipinjam)

# # proses inputan dinamis
# def proses_peminjaman():
#     while True:
#         print("\nMenu:")
#         print("1. Tambahkan alat")
#         print("2. kembalikan alat")
#         print("3. Tukar alat")
#         print("4. Lihat alat yang sedang dipinjam")
#         print("5. Selesai")
        
#         pilihan = input("Pilih opsi (1-5): ")

#         # jika variabel pilihan sama dengan 1 jalankan program di bawah ini
#         if pilihan == "1":
#             # program Tambahkan alat
#             jenis = input("Masukkan jenis alat yang dipinjam: ")
#             jumlah = int(input(f"Masukkan jumlah {jenis} yang dipinjam: "))
#             tambah_alat(jenis, jumlah)

#         # jika variabel pilihan tidak dengan 1 apakah variabel pilihan sama dengan 2 jalankan program di bawah ini
#         elif pilihan == "2":
#             # program kembalikan alat
#             jenis = input("Masukkan jenis alat yang dikembalikan: ")
#             jumlah = int(input(f"Masukkan jumlah {jenis} yang dikembalikan: "))

#             kurangi_alat(jenis, jumlah)
#         # jika variabel pilihan tidak dengan 3 apakah variabel pilihan sama dengan 4 jalan kan program di bawah ini
#         elif pilihan == "3":
#             # program Tukar alat
#             jenis_dikembalikan = input("Masukkan jenis alat yang dikembalikan: ")
#             jumlah_dikembalikan = int(input(f"Masukkan jumlah {jenis_dikembalikan} yang dikembalikan: "))
#             jenis_dipinjam = input("Masukkan jenis alat yang dipinjam: ")
#             jumlah_dipinjam = int(input(f"Masukkan jumlah {jenis_dipinjam} yang dipinjam: "))
#             tukar_alat(jenis_dikembalikan, jumlah_dikembalikan, jenis_dipinjam, jumlah_dipinjam)
        
#         elif pilihan == "4":
#             # program melihat alat yang sedang dipinjam
#             print("\nAlat yang sedang dipinjam:")
#             if alat:
#                 for jenis, jumlah in alat.items():
#                     print(f"- {jenis}: {jumlah} buah alat")
#             else:
#                 print("Tidak ada alat yang sedang dipinjam.")
        
#         elif pilihan == "5":
#             # Selesai
#             print("Proses selesai.")
#             break
        
#         else:
#             print("Pilihan tidak valid. Coba lagi.")

# # Jalankan program
# proses_peminjaman()

# Dictionary untuk menyimpan jumlah alat kesehatan
alat_kesehatan = {}
alat_yang_dipinjam = set()

# Fungsi untuk menambahkan alat ke dalam dictionary
def tambah_alat(nama_alat, jumlah):
    if nama_alat in alat_kesehatan:
        alat_kesehatan[nama_alat] += jumlah
    else:
        alat_kesehatan[nama_alat] = jumlah
    if jumlah > 0:
        alat_yang_dipinjam.add(nama_alat)

# Fungsi untuk memproses pengembalian alat
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

    if pilihan == "1":
        nama_alat = input("Masukkan nama alat: ")
        jumlah = int(input("Masukkan jumlah alat yang dipinjam: "))
        tambah_alat(nama_alat, jumlah)

    elif pilihan == "2":
        nama_alat = input("Masukkan nama alat: ")
        jumlah = int(input("Masukkan jumlah alat yang dikembalikan: "))
        kembalikan_alat(nama_alat, jumlah)

    elif pilihan == "3":
        nama_alat_kembali = input("Masukkan nama alat yang dikembalikan: ")
        jumlah_kembali = int(input("Masukkan jumlah alat yang dikembalikan: "))
        nama_alat_ambil = input("Masukkan nama alat yang ingin diambil: ")
        jumlah_ambil = int(input("Masukkan jumlah alat yang diambil: "))
        tukar_alat(nama_alat_ambil, jumlah_ambil, nama_alat_kembali, jumlah_kembali)

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
