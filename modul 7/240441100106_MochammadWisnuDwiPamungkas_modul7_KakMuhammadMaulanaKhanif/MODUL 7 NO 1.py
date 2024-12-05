alat_kesehatan = {
    "pengukur_tekanan_darah": 0,
    "termometer": 0,
    "pengukur_kadar_gula_darah": 0,
    "stetoskop": 0,
}
# Hari pertama
alat_kesehatan["pengukur_tekanan_darah"] += 2
alat_kesehatan["termometer"] += 3

# Hari kedua
alat_kesehatan["stetoskop"] += 4

# Mengembalikan alat
alat_kesehatan["pengukur_tekanan_darah"] -= 1
alat_kesehatan["termometer"] -= 2

alat_kesehatan["stetoskop"] -= 3
alat_kesehatan["termometer"] += 2
# perulangan dan penyeleksian
alat_tersisa = {alat for alat, jumlah in alat_kesehatan.items()if jumlah > 0 }

print("Alat kesehatan yang masih dipinjam Heni:")
for alat in alat_tersisa:
    print(f"- {alat}: {alat_kesehatan[alat]} unit") 
