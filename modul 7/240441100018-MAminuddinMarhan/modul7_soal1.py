alat_kesehatan = {
    "pengukur_tekanan_darah": 0,
    "termometer": 0,
    "stetoskop": 0,
    "inhaler": 0
}
def input_positive(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Input tidak boleh kurang dari nol. Silakan coba lagi.")
            else:
                return value
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
print("\nHari Pertama")
alat_kesehatan["pengukur_tekanan_darah"] += input_positive("Masukkan jumlah alat pengukur tekanan darah yang dipinjam pada hari pertama: ")
alat_kesehatan["termometer"] += input_positive("Masukkan jumlah alat termometer yang dipinjam pada hari pertama: ")
print("\nHari Kedua")
alat_kesehatan["stetoskop"] += input_positive("Masukkan jumlah stetoskop yang dipinjam pada hari kedua: ")
print("\nSetelah Satu Minggu")
def validasi_pengembalian(jenis_alat):
    while True:
        jumlah_kembali = input_positive(f"Masukkan jumlah alat {jenis_alat} yang dikembalikan: ")
        if jumlah_kembali > alat_kesehatan[jenis_alat]:
            print(f"Jumlah pengembalian melebihi jumlah peminjaman {jenis_alat}. Silakan coba lagi.")
        else:
            return jumlah_kembali
jumlah_kembali_ptd = validasi_pengembalian("pengukur_tekanan_darah")
alat_kesehatan["pengukur_tekanan_darah"] -= jumlah_kembali_ptd
jumlah_kembali_t = validasi_pengembalian("termometer")
alat_kesehatan["termometer"] -= jumlah_kembali_t
jumlah_kembali_s = validasi_pengembalian("stetoskop")
alat_kesehatan["stetoskop"] -= jumlah_kembali_s
alat_kesehatan["inhaler"] += input_positive("Masukkan jumlah alat inhaler yang dipinjam: ")
total_saat_ini = {kunci: nilai for kunci, nilai in alat_kesehatan.items() if nilai > 0}
print("\nAlat yang masih dipinjam saat ini:")
for kunci, nilai in total_saat_ini.items():
    print(f"{kunci}: {nilai} buah")