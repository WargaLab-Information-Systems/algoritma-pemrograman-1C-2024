# Total orang dan jumlah orang yang ingin dipilih
n = 7  # total orang
r = 4  # orang yang dipilih

# Menghitung faktorial secara manual
faktorial_n = 7 * 6 * 5 * 4 * 3 * 2 * 1  # 7! = 7 * 6 * 5 * 4 * 3 * 2 * 1
faktorial_r = 4 * 3 * 2 * 1  # 4! = 4 * 3 * 2 * 1
faktorial_n_r = 3 * 2 * 1  # 3! = 3 * 2 * 1

# Menghitung kombinasi
jumlah_cara = faktorial_n // (faktorial_r * faktorial_n_r)

print("Jumlah cara untuk memilih", r, "orang dari", n, "orang adalah:", jumlah_cara)
