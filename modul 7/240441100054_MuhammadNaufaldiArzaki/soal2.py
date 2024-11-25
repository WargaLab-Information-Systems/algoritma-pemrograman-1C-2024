klub_basket = {"ironi", "Narji", "rusdi", "ambatukam", "fuad"}
klub_renang = {"lil nusnus", "rusdi", "Narji", "bernadit", "ambayu"}

kedua_klub = klub_basket.intersection(klub_renang)
only_klub = klub_basket.symmetric_difference(klub_renang)
all_klub = klub_basket.union(klub_renang)
total = len(all_klub)
print(f"\nSiswa yang mengikuti kedua klub: {kedua_klub}")
print(f"\nSiswa yang hanya mengikuti satu klub saja: {only_klub}")
print(f"\nDaftar semua siswa unik yang mengikuti setidaknya satu dari dua klub: {all_klub}")
print(f"\nJumlah siswa unik yang mengikuti setidaknya satu dari kedua klub: {total}")