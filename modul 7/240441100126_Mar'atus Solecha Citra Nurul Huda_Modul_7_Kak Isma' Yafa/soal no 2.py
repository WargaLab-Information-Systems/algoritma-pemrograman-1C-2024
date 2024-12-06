# Minta input dari pengguna
print("Masukkan nama-nama siswa yang mengikuti klub Basket:")
klub_basket = set(input().split(", "))

print("Masukkan nama-nama siswa yang mengikuti klub Renang:")
klub_renang = set(input().split(", "))

# Siswa yang mengikuti kedua klub
siswa_dua_klub = klub_basket.intersection(klub_renang)
print("\nSiswa yang mengikuti kedua klub:")
print(", ".join(siswa_dua_klub))

# Siswa yang hanya mengikuti satu klub
siswa_satu_klub = klub_basket.symmetric_difference(klub_renang)
print("\nSiswa yang hanya mengikuti satu klub:")
print(", ".join(siswa_satu_klub))

# Semua siswa unik yang mengikuti setidaknya satu klub
semua_siswa = klub_basket.union(klub_renang)
print("\nSemua siswa unik yang mengikuti setidaknya satu klub:")
print(", ".join(semua_siswa))

# Jumlah siswa unik yang mengikuti setidaknya satu klub
print(f"\nJumlah siswa unik yang mengikuti setidaknya satu klub: {len(semua_siswa)}")
