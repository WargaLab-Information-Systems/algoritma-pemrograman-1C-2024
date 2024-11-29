# Inisialisasi dictionary untuk menyimpan alat kesehatan yang dipinjam
alat_kesehatan = {
    "alat_pengukur_tekanan_darah": 0,
    "termometer": 0,
    "alat_stetoskop": 0,
    "inhaler": 0
}

# Fungsi untuk menampilkan alat kesehatan yang dipinjam saat ini
def tampilkan_alat_kesehatan():
    print("\nAlat kesehatan yang dipinjam Heni saat ini:")
    for alat, jumlah in alat_kesehatan.items():
        if jumlah > 0:
            print(f"{alat}: {jumlah}")

# Input peminjaman hari pertama
print("Masukkan jumlah alat yang dipinjam pada hari pertama:")
alat_kesehatan["alat_pengukur_tekanan_darah"] += int(input("Alat pengukur tekanan darah: "))
alat_kesehatan["termometer"] += int(input("Termometer: "))

# Input peminjaman hari kedua
print("Masukkan jumlah alat yang dipinjam pada hari kedua:")
alat_kesehatan["alat_stetoskop"] += int(input("Alat stetoskop: "))

# Input pengembalian setelah seminggu
print("Masukkan jumlah alat yang dikembalikan setelah seminggu:")
alat_kesehatan["alat_pengukur_tekanan_darah"] -= int(input("Alat pengukur tekanan darah yang dikembalikan: "))
alat_kesehatan["termometer"] -= int(input("Termometer yang dikembalikan: "))

# Input penukaran alat
print("Masukkan jumlah alat yang ditukar:")
jumlah_tukar = int(input("Jumlah alat stetoskop yang ditukar: "))
alat_kesehatan["alat_stetoskop"] -= jumlah_tukar  # Mengurangi alat yang ditukar
alat_kesehatan["inhaler"] += int(input("Jumlah inhaler yang diterima: "))  # Menambah alat yang diterima

# Menampilkan hasil akhir
tampilkan_alat_kesehatan()


