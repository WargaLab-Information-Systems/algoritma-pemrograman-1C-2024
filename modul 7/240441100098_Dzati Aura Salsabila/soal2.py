klub_basket = {"Andre", "Van", "Aca", "Rara", "Salma"}
klub_renang = {"Van", "Aca", "Dimas", "Lani"}

# Siswa yang mengikuti kedua klub
kedua_klub = klub_basket.intersection(klub_renang)
print("Siswa yang mengikuti kedua klub:", kedua_klub)

# Siswa yang hanya mengikuti satu klub
hanya_satu_klub = klub_basket.symmetric_difference(klub_renang)
print("Siswa yang hanya mengikuti satu klub:", hanya_satu_klub)

# Semua siswa unik
semua_siswa_unik = klub_basket.union(klub_renang)
print("Semua siswa unik:", semua_siswa_unik)

# Jumlah siswa unik
jumlah_siswa = len(semua_siswa_unik)
print("Jumlah siswa unik:", jumlah_siswa)