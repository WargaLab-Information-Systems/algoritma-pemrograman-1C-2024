klub_basket= {"a","b","c","d","e"}
klub_renang={"d","e","f","g","h"}

# a. Menampilkan daftar siswa yang mengikuti kedua klub
siswa_kedua_klub = klub_basket.intersection(klub_renang)  # Operasi intersection
print("Siswa yang mengikuti kedua klub:")
print(siswa_kedua_klub)
# b. Menampilkan daftar siswa yang hanya mengikuti satu klub saja
siswa_hanya_satu_klub = klub_basket.symmetric_difference(klub_renang)  # Operasi symmetric_difference
print("Siswa yang hanya mengikuti satu klub:")
print(siswa_hanya_satu_klub)
# c. Menampilkan daftar semua siswa unik yang mengikuti setidaknya satu dari kedua klub
siswa_unik = klub_basket.union(klub_renang)  # Operasi union
print("Semua siswa unik yang mengikuti setidaknya satu klub:")
print(siswa_unik)
# d. Menampilkan jumlah siswa unik yang mengikuti setidaknya satu dari kedua klub tersebut
print("Jumlah siswa unik yang mengikuti setidaknya satu klub:", len(siswa_unik))
