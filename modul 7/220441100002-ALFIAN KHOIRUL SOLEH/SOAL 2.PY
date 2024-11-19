# Membuat dua set yang berisi nama siswa
klub_basket = {"Andi", "Budi", "Citra", "Doni", "Eva"}
klub_renang = {"Budi", "Eva", "Fajar", "Gita", "Hadi"}

# a. Set sudah dibuat di atas

# b. Menampilkan siswa yang mengikuti kedua klub (intersection)
siswa_kedua_klub = klub_basket.intersection(klub_renang)
print("\nSiswa yang mengikuti kedua klub:")
print(siswa_kedua_klub)

# c. Menampilkan siswa yang hanya mengikuti satu klub
siswa_basket_saja = klub_basket - klub_renang
siswa_renang_saja = klub_renang - klub_basket

print("\nSiswa yang hanya ikut klub basket:")
print(siswa_basket_saja)
print("\nSiswa yang hanya ikut klub renang:")
print(siswa_renang_saja)

# d. Menampilkan semua siswa yang ikut setidaknya satu klub (union)
semua_siswa = klub_basket.union(klub_renang)
print("\nDaftar semua siswa yang mengikuti klub:")
print(semua_siswa)

# e. Menampilkan jumlah siswa unik
jumlah_siswa = len(semua_siswa)
print("\nJumlah siswa unik yang mengikuti klub:", jumlah_siswa)

