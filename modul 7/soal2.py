# a. Membuat dua set berisi nama siswa
klub_basket = {"Andi", "Budi", "Citra", "Dewi", "Eko"}
klub_renang = {"Budi", "Citra", "Fajar", "Gita"}

# b. Menampilkan daftar siswa yang mengikuti kedua klub
siswa_kedua_klub = klub_basket & klub_renang
print("Siswa yang mengikuti kedua klub:")
print(siswa_kedua_klub)

# c. Menampilkan daftar siswa yang hanya mengikuti satu klub saja
siswa_satu_klub = (klub_basket ^ klub_renang)  # XOR operation
print("Siswa yang hanya mengikuti satu klub:")
print(siswa_satu_klub)

# d. Menampilkan daftar semua siswa unik yang mengikuti setidaknya satu klub
siswa_unik = klub_basket | klub_renang  # Union operation
print("Semua siswa unik yang mengikuti setidaknya satu klub:")
print(siswa_unik)

# e. Menampilkan jumlah siswa unik yang mengikuti setidaknya satu klub
jumlah_siswa_unik = len(siswa_unik)
print("Jumlah siswa unik yang mengikuti setidaknya satu klub:")
print(jumlah_siswa_unik)
