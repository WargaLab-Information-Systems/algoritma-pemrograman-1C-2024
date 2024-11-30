# a. Membuat dua set yang berisi nama siswa yang mengikuti klub Basket dan Renang
klub_basket = {"ali", "budi", "citra", "dina", "eka"}
klub_renang = {"budi", "dina", "faisal", "gita", "hani"}

# b. Menampilkan daftar siswa yang mengikuti kedua klub
siswa_kedua_klub = klub_basket.intersection(klub_renang)
print("Siswa yang mengikuti kedua klub:", siswa_kedua_klub)

# c. Menampilkan daftar siswa yang hanya mengikuti satu klub saja
siswa_hanya_satu_klub = klub_basket.symmetric_difference(klub_renang)
print("Siswa yang hanya mengikuti satu klub:", siswa_hanya_satu_klub)

# d. Menampilkan daftar semua siswa unik yang mengikuti setidaknya satu dari kedua klub tersebut
siswa_unik = klub_basket.union(klub_renang)
print("Siswa unik yang mengikuti setidaknya satu klub:", siswa_unik)

# e. Menampilkan jumlah siswa unik yang mengikuti setidaknya satu dari kedua klub tersebut
jumlah_siswa_unik = len(siswa_unik)
print("Jumlah siswa unik yang mengikuti setidaknya satu klub:", jumlah_siswa_unik)
