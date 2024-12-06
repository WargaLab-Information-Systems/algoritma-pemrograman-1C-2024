alat_kesehatan = {
    "pengukur tekanan darah": 0,
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
alat_kesehatan["pengukur tekanan darah"] += input_positive("Masukkan jumlah alat pengukur tekanan darah yang dipinjam: ")
alat_kesehatan["termometer"] += input_positive("Masukkan jumlah alat termometer yang dipinjam: ")

print("\nHari Kedua")
alat_kesehatan["stetoskop"] += input_positive("Masukkan jumlah alat stetoskop yang dipinjam: ")


print("\nSetelah Satu Minggu")

alat_kesehatan["pengukur tekanan darah"] -= input_positive("Masukkan jumlah alat pengukur tekanan darah yang dikembalikan: ")
alat_kesehatan["termometer"] -= input_positive("Masukkan jumlah alat termometer yang dikembalikan: ")


alat_kesehatan["stetoskop"] -= input_positive("Masukkan jumlah stetoskop yang ditukar: ")
alat_kesehatan["inhaler"] += input_positive("Masukkan jumlah inhaler yang diterima dari penukaran: ")

total_saat_ini = {kunci: nilai for kunci, nilai in alat_kesehatan.items() if nilai > 0}

print("\nAlat kesehatan yang masih dipinjam Heni saat ini:")
for kunci, nilai in total_saat_ini.items():
    print(f"{kunci}: {nilai} buah")
