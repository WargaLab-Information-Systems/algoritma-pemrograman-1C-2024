# Jumlah anggota tim:
total_anggota = 7
jumlah_anggota_tim = 4

# Menghitung banyak cara Untuk membentuk tim:
banyak_cara = (total_anggota * (total_anggota - 1) * (total_anggota - 2) * (total_anggota - 3)) / (jumlah_anggota_tim * (jumlah_anggota_tim - 1) * (jumlah_anggota_tim - 2) * (jumlah_anggota_tim - 3))

# Output
print("Banyak cara membentuk tim:", int(banyak_cara))
print(f"Banyak cara membentuk tim: {int(banyak_cara)} cm")
