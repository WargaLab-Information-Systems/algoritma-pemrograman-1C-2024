alat_kesehatan = {
    "pengukur tekanan darah": 0,
    "termometer": 0,
    "stetoskop": 0,
    "inhaler" : 0
}
alat_kesehatan["pengukur tekanan darah"] += int(input("jumnlah alat pengukur tekanan darah yang di pinjam: "))
alat_kesehatan["termometer"] += int(input("jumnlah alat termometer yang di pinjam: "))

alat_kesehatan["stetoskop"] += int(input("jumnlah stetoskop yang di pinjam: "))

alat_kesehatan["pengukur tekanan darah"] -= int(input("jumnlah alat pengukur tekanan darah yang di kembalikan: "))
alat_kesehatan["termometer"] -= int(input("jumnlah alat termometer yang di kembalikan: "))

alat_kesehatan["stetoskop"] -= int(input("jumnlah alat stetoskop yang di tukar: "))
alat_kesehatan["inhaler"] += int(input("jumnlah alat inhaler yang di pinjam: "))

total_saat_ini = {kunci:nilai for kunci, nilai in alat_kesehatan.items()}

print("Alat yang di pinjam saat ini:")
for kunci, nilai in total_saat_ini.items():
    print(f"{kunci}: {nilai} buah")
