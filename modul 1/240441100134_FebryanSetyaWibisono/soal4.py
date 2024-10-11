n = 7 #semua orang
r = 4 #orang dipilih

# Menghitung kombinasi C(n.r)
# C(7.4) = 7! / (4! * (7.4)!)
# = 7! / (4! * 3!)
# = (7 * 6 * 5 * 4 * 3 * 2 * 1) / (4 * 3 * 2 * 1)

banyak_cara = 5040 / 144
print(f"Jumlah cara untuk memilih {r} orang dari {n} orang adalah {banyak_cara}")