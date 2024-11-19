klub_basket = {"Andi", "Budi", "Cici", "Dedi", "Eka"}
klub_renang = {"Budi", "Cici", "Fajar", "Gita", "Hana"}

siswa_kedua_klub = klub_basket.intersection(klub_renang) 
print("Siswa yang mengikuti kedua klub (Basket dan Renang):")
print(siswa_kedua_klub)

siswa_satu_klub = (klub_basket.symmetric_difference(klub_renang)) 
print("Siswa yang hanya mengikuti satu klub saja:")
print(siswa_satu_klub)

siswa_setidaknya_satu_klub = klub_basket.union(klub_renang)
print("Semua siswa unik yang mengikuti setidaknya satu dari kedua klub:")
print(siswa_setidaknya_satu_klub)

jumlah_siswa_klub = len(siswa_setidaknya_satu_klub)
print("Jumlah siswa unik yang mengikuti setidaknya satu dari kedua klub:")
print(jumlah_siswa_klub)

