klub_basket = {"Wisnu", "Heru", "Dimas", "iqbal", "Rio"}
klub_renang = {"Rio", "lusi", "Heru", "Rijal", "Rama"}
# hasil sama
siswa_kedua_klub= klub_basket.intersection(klub_renang)
# hasil tidak sama
satu_club=klub_basket.symmetric_difference(klub_renang)
# menggabungkan
semua_siswa_unik= klub_basket.union(klub_renang)
# isi
jumlah_siswa_unik = len(semua_siswa_unik)

print(f"Siswa yang mengikuti kedua club:{siswa_kedua_klub}")
print(f"siswa yang hanya mengikuti satu club:{satu_club}")
print(f"siswa yang mengikuti setidaknya satu dari kedua club;{semua_siswa_unik}")
print(f"Jumlah siswa unik yang mengikuti setidaknya satu klub:{jumlah_siswa_unik}")
