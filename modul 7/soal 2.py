
# Contoh data (ganti dengan data siswa sebenarnya)
klub_basket = {"Andi", "Budi", "Cici", "Dedi", "Efi"}
klub_renang = {"Budi", "Cici", "Fatimah", "Gani"}

print("a. Himpunan (set) dari setiap Klub")
print("   Siswa yang mengikuti klub Basket:", klub_basket)
print("   Siswa yang mengikuti klub Renang:", klub_renang)

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

